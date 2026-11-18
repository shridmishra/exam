import json
import re

# 21 Master Formulas definition
master_formulas = [
    # Unit 1: Lateral Earth Pressure & Retaining Walls
    {
        "id": "f1-rankine-active",
        "unit": 1,
        "title": "Rankine Active Earth Pressure & Tension Crack Depth",
        "frequency": "100% Guaranteed (4/4 Papers)",
        "freq_badge": "badge-repeated",
        "latex_main": r"p_a = K_a \sigma'_v - 2c \sqrt{K_a}",
        "latex_sub": r"K_a = \frac{1 - \sin\phi}{1 + \sin\phi} = \tan^2\left(45^\circ - \frac{\phi}{2}\right) \qquad z_c = \frac{2c}{\gamma \sqrt{K_a}}",
        "latex_raw": r"p_a = K_a \sigma'_v - 2c \sqrt{K_a}, \quad z_c = \frac{2c}{\gamma \sqrt{K_a}}",
        "params": [
            {"sym": "p_a", "name": "Active lateral earth pressure", "unit": "kPa"},
            {"sym": "K_a", "name": "Rankine active pressure coefficient", "unit": "dimensionless"},
            {"sym": r"\sigma'_v", "name": r"Effective vertical overburden stress (\gamma z)", "unit": "kPa"},
            {"sym": "c", "name": "Cohesion intercept of soil", "unit": "kPa"},
            {"sym": r"\phi", "name": "Angle of internal friction", "unit": "degrees"},
            {"sym": "z_c", "name": "Critical depth of unsupported tension crack", "unit": "m"},
            {"sym": r"\gamma", "name": "Soil bulk unit weight", "unit": "kN/m³"}
        ],
        "notes": "At ground surface (z = 0), p_a = -2c√K_a (tensile zone). Tension crack develops to depth z_c. Total net active thrust before water enters crack is P_a = 0.5 K_a γ (H - z_c)² acting at (H - z_c)/3 from the base. Depth of zero net pressure is 2z_c."
    },
    {
        "id": "f2-rankine-passive",
        "unit": 1,
        "title": "Rankine Passive Earth Pressure Coefficient",
        "frequency": "Core Numerical / Theory",
        "freq_badge": "badge-subtle",
        "latex_main": r"p_p = K_p \sigma'_v + 2c \sqrt{K_p}",
        "latex_sub": r"K_p = \frac{1 + \sin\phi}{1 - \sin\phi} = \tan^2\left(45^\circ + \frac{\phi}{2}\right) = \frac{1}{K_a}",
        "latex_raw": r"p_p = K_p \sigma'_v + 2c \sqrt{K_p}, \quad K_p = \frac{1 + \sin\phi}{1 - \sin\phi}",
        "params": [
            {"sym": "p_p", "name": "Passive lateral earth resistance", "unit": "kPa"},
            {"sym": "K_p", "name": "Rankine passive earth coefficient", "unit": "dimensionless"},
            {"sym": r"\sigma'_v", "name": "Effective vertical overburden stress", "unit": "kPa"},
            {"sym": "c", "name": "Cohesion intercept", "unit": "kPa"}
        ],
        "notes": "Passive pressure represents the maximum resisting force when a wall is pushed into backfill. Full mobilization requires 4 to 10 times greater wall displacement than active state."
    },
    {
        "id": "f3-coulomb-thrust",
        "unit": 1,
        "title": "Coulomb Earth Thrust on Gravity Retaining Walls",
        "frequency": "75% (3/4 Papers - 7M Numerical)",
        "freq_badge": "badge-repeated",
        "latex_main": r"P_a = \frac{1}{2} \gamma H^2 K_a \qquad P_p = \frac{1}{2} \gamma H^2 K_p",
        "latex_sub": r"K_a = \frac{\cos^2\phi}{\cos\delta \left[ 1 + \sqrt{\frac{\sin(\phi+\delta)\sin\phi}{\cos\delta}} \right]^2} \quad (\text{for } \alpha=90^\circ, \beta=0^\circ)",
        "latex_raw": r"P_a = \frac{1}{2} \gamma H^2 K_a, \quad P_p = \frac{1}{2} \gamma H^2 K_p",
        "params": [
            {"sym": "P_a, P_p", "name": "Total active / passive thrust per lineal metre", "unit": "kN/m"},
            {"sym": "H", "name": "Total vertical height of retaining wall", "unit": "m"},
            {"sym": r"\delta", "name": "Angle of wall interface friction (typically 20° or 2/3 φ)", "unit": "degrees"},
            {"sym": r"\gamma", "name": "Unit weight of backfill soil", "unit": "kN/m³"}
        ],
        "notes": "Thrust acts at H/3 from the base, inclined at angle δ to the normal of the wall face (downward for active, upward for passive). For vertical smooth walls (δ=0, α=90°), Coulomb's equation reduces identically to Rankine's formula."
    },
    {
        "id": "f4-at-rest-pressure",
        "unit": 1,
        "title": "At-Rest Earth Pressure Coefficient (Elastic & Empirical)",
        "frequency": "Core Theory Derivation",
        "freq_badge": "badge-subtle",
        "latex_main": r"K_0 = \frac{\mu}{1 - \mu} \quad (\text{Elastic Theory}) \qquad K_0 = 1 - \sin\phi \quad (\text{Jaky's Equation})",
        "latex_sub": r"\sigma_h = K_0 \cdot \sigma'_v \qquad \text{Condition: } \varepsilon_x = \varepsilon_y = 0 \text{ (Zero Lateral Yield)}",
        "latex_raw": r"K_0 = \frac{\mu}{1-\mu} \quad (\text{Elastic}), \quad K_0 = 1 - \sin\phi \quad (\text{Jaky})",
        "params": [
            {"sym": "K_0", "name": "Coefficient of earth pressure at rest", "unit": "dimensionless"},
            {"sym": r"\mu", "name": "Poisson's ratio of soil (typically 0.25 - 0.35)", "unit": "dimensionless"},
            {"sym": r"\sigma_h", "name": "At-rest horizontal lateral effective stress", "unit": "kPa"},
            {"sym": r"\phi", "name": "Effective friction angle of normally consolidated soil", "unit": "degrees"}
        ],
        "notes": "Derived from Hooke's 3D law by setting lateral strain ε_x = (1/E)[σ_x - μ(σ_y + σ_z)] = 0. Governs rigid unyielding structures like basement walls keyed into bedrock and bridge abutments on fixed piles."
    },
    {
        "id": "f5-rebhann-graphical",
        "unit": 1,
        "title": "Rebhann's Graphical Construction for Active Earth Thrust",
        "frequency": "75% (3/4 Papers - 6-7M Derivation)",
        "freq_badge": "badge-repeated",
        "latex_main": r"P_a = \gamma \cdot \text{Area}(\Delta BGH) = \frac{1}{2}\gamma \cdot (GH \cdot BG \sin\psi)",
        "latex_sub": r"\text{Critical Rupture Criterion: } GH = \frac{BG}{\sin\psi} \iff \frac{dP_a}{d\theta} = 0",
        "latex_raw": r"P_a = \gamma \cdot \text{Area}(\Delta BGH) = \frac{1}{2}\gamma \cdot (GH \cdot BG \sin\psi)",
        "params": [
            {"sym": "P_a", "name": "Total active thrust from sliding wedge", "unit": "kN/m"},
            {"sym": r"\Delta BGH", "name": "Earth pressure triangle constructed on rupture plane", "unit": "m²"},
            {"sym": r"\psi", "name": "Inclination angle between ground and rupture plane", "unit": "degrees"}
        ],
        "notes": "Poncelet's semicircle theorem geometrically maximizes the trial wedge thrust without solving complex differential calculus. Critical rupture surface AH isolates the failure wedge."
    },

    # Unit 2: Shear Strength & Slope Stability
    {
        "id": "f6-mohr-coulomb",
        "unit": 2,
        "title": "Mohr-Coulomb Failure Criterion & Principal Stress Relation",
        "frequency": "100% Guaranteed (4/4 Papers - 7M)",
        "freq_badge": "badge-repeated",
        "latex_main": r"\sigma'_1 = \sigma'_3 \tan^2\left(45^\circ + \frac{\phi'}{2}\right) + 2c'\tan\left(45^\circ + \frac{\phi'}{2}\right)",
        "latex_sub": r"\sigma'_1 = \sigma'_3 N_\phi + 2c'\sqrt{N_\phi} \qquad \theta_{\text{cr}} = 45^\circ + \frac{\phi'}{2} \quad (\text{Failure Plane Angle})",
        "latex_raw": r"\sigma'_1 = \sigma'_3 \tan^2\left(45^\circ + \frac{\phi'}{2}\right) + 2c'\tan\left(45^\circ + \frac{\phi'}{2}\right)",
        "params": [
            {"sym": r"\sigma'_1", "name": "Major effective principal stress at failure", "unit": "kPa"},
            {"sym": r"\sigma'_3", "name": "Minor effective principal stress (cell confining pressure)", "unit": "kPa"},
            {"sym": "c'", "name": "Effective cohesion intercept", "unit": "kPa"},
            {"sym": r"\phi'", "name": "Effective angle of internal friction", "unit": "degrees"},
            {"sym": r"N_\phi", "name": "Flow value parameter tan²(45° + φ'/2)", "unit": "dimensionless"},
            {"sym": r"\theta_{\text{cr}}", "name": "Critical shear failure angle with major principal plane", "unit": "degrees"}
        ],
        "notes": "Fundamental governing equation for triaxial shear tests, unconfined compression tests, and direct shear tests. For purely cohesive soil (φ=0): σ₁ - σ₃ = 2c_u = q_u. For cohesionless sand (c=0): σ'₁/σ'₃ = tan²(45° + φ'/2)."
    },
    {
        "id": "f7-triaxial-area",
        "unit": 2,
        "title": "Triaxial Specimen Area Correction (Axial Strain)",
        "frequency": "Core Numerical Step (Every Triaxial Problem)",
        "freq_badge": "badge-repeated",
        "latex_main": r"A = \frac{A_0}{1 - \varepsilon} \qquad \text{where } \varepsilon = \frac{\Delta L}{L_0}",
        "latex_sub": r"\Delta\sigma = \sigma_1 - \sigma_3 = \frac{\text{Failure Deviator Load}}{A} \qquad A_0 = \frac{\pi}{4} D_0^2",
        "latex_raw": r"A = \frac{A_0}{1 - \varepsilon}, \quad \varepsilon = \frac{\Delta L}{L_0}, \quad \Delta\sigma = \frac{P}{A}",
        "params": [
            {"sym": "A", "name": "Corrected cross-sectional area of specimen at failure", "unit": "m²"},
            {"sym": "A_0", "name": "Initial cross-sectional area before shearing", "unit": "m²"},
            {"sym": r"\varepsilon", "name": "Axial compressive strain at failure", "unit": "dimensionless / %"},
            {"sym": r"\Delta L", "name": "Axial deformation / shortening at failure", "unit": "mm"},
            {"sym": "L_0", "name": "Initial height of cylindrical specimen (typically 76 mm)", "unit": "mm"},
            {"sym": r"\Delta\sigma", "name": "Deviator stress at failure", "unit": "kPa"}
        ],
        "notes": "Assumes cylindrical specimen deforms as a right cylinder with zero net volume change during undrained shear (or uniform lateral bulging). Forgetting area correction falsely overestimates deviator stress by 10-25%."
    },
    {
        "id": "f8-infinite-slope",
        "unit": 2,
        "title": "Infinite Slope Stability with Steady Seepage Parallel to Slope",
        "frequency": "100% Guaranteed (4/4 Papers - 7M)",
        "freq_badge": "badge-repeated",
        "latex_main": r"FS = \frac{c' + \gamma' z \cos^2\beta \tan\phi'}{\gamma_{\text{sat}} z \sin\beta \cos\beta}",
        "latex_sub": r"\text{For granular soil } (c'=0): \quad FS = \frac{\gamma'}{\gamma_{\text{sat}}} \cdot \frac{\tan\phi'}{\tan\beta} \approx 0.5 \cdot \frac{\tan\phi'}{\tan\beta}",
        "latex_raw": r"FS = \frac{c' + \gamma' z \cos^2\beta \tan\phi'}{\gamma_{\text{sat}} z \sin\beta \cos\beta}",
        "params": [
            {"sym": "FS", "name": "Factor of safety against shear sliding along slope plane", "unit": "dimensionless"},
            {"sym": "c'", "name": "Effective cohesion along slip surface", "unit": "kPa"},
            {"sym": r"\phi'", "name": "Effective angle of internal friction", "unit": "degrees"},
            {"sym": r"\beta", "name": "Slope inclination angle to horizontal", "unit": "degrees"},
            {"sym": "z", "name": "Depth of planar slip surface parallel to ground", "unit": "m"},
            {"sym": r"\gamma_{\text{sat}}", "name": "Saturated soil unit weight", "unit": "kN/m³"},
            {"sym": r"\gamma'", "name": "Submerged unit weight (γ_sat - γ_w = γ_sat - 9.81)", "unit": "kN/m³"}
        ],
        "notes": "Seepage force parallel to the slope cuts effective normal stress by roughly half, dropping the factor of safety of granular slopes by ~50% compared to dry conditions (FS_dry = tanφ'/tanβ)."
    },
    {
        "id": "f9-vane-shear",
        "unit": 2,
        "title": "Vane Shear Test: Undrained Cohesion Formula",
        "frequency": "Core Practical / Theory (3/4 Papers)",
        "freq_badge": "badge-subtle",
        "latex_main": r"T = c_u \pi D^2 \left( \frac{H}{2} + \frac{D}{6} \right) \implies c_u = \frac{T}{\pi D^2 \left( \frac{H}{2} + \frac{D}{6} \right)}",
        "latex_sub": r"\text{If top end not submerged: } \quad T = c_u \pi D^2 \left( \frac{H}{2} + \frac{D}{12} \right)",
        "latex_raw": r"c_u = \frac{T}{\pi D^2 \left( \frac{H}{2} + \frac{D}{6} \right)}",
        "params": [
            {"sym": "c_u", "name": "Undrained shear strength of soft sensitive clay", "unit": "kPa"},
            {"sym": "T", "name": "Applied failure torque reading from spring dial", "unit": "N·m"},
            {"sym": "D", "name": "Diameter / blade width of the four-bladed vane", "unit": "m"},
            {"sym": "H", "name": "Overall height of vane blades (standard H = 2D)", "unit": "m"}
        ],
        "notes": "Used exclusively for in-situ testing of very soft to soft saturated clays where undisturbed sampling is virtually impossible. Standard lab vane: D = 12 mm, H = 24 mm. Field vane: D = 50-100 mm."
    },

    # Unit 3: Shallow Foundations & Bearing Capacity
    {
        "id": "f10-terzaghi-bearing",
        "unit": 3,
        "title": "Terzaghi Ultimate Bearing Capacity Equation",
        "frequency": "100% Guaranteed (4/4 Papers - 7M Numerical)",
        "freq_badge": "badge-repeated",
        "latex_main": r"q_{\text{ult}} = c N_c + \gamma D_f N_q R_{w1} + \frac{1}{2} \gamma B N_\gamma R_{w2}",
        "latex_sub": r"\text{Square: } q_{\text{ult}} = 1.3 c N_c + q N_q R_{w1} + 0.4 \gamma B N_\gamma R_{w2} \qquad \text{Circular: } 1.3 c N_c + q N_q R_{w1} + 0.3 \gamma B N_\gamma R_{w2}",
        "latex_raw": r"q_{\text{ult}} = c N_c + \gamma D_f N_q R_{w1} + \frac{1}{2}\gamma B N_\gamma R_{w2}",
        "params": [
            {"sym": r"q_{\text{ult}}", "name": "Ultimate bearing capacity of foundation base", "unit": "kPa (kN/m²)"},
            {"sym": "c", "name": "Soil cohesion intercept", "unit": "kPa"},
            {"sym": r"\gamma", "name": "Unit weight of soil above / below footing base", "unit": "kN/m³"},
            {"sym": "D_f", "name": "Depth of foundation footing below ground surface", "unit": "m"},
            {"sym": "B", "name": "Footing width (or diameter of circular footing)", "unit": "m"},
            {"sym": r"N_c, N_q, N_\gamma", "name": "Terzaghi bearing capacity factors (functions of φ)", "unit": "dimensionless"},
            {"sym": "R_{w1}, R_{w2}", "name": "Water table correction factors (0.5 to 1.0)", "unit": "dimensionless"}
        ],
        "notes": "Safe bearing capacity: q_safe = (q_ult - γ D_f)/FS + γ D_f. For pure cohesive clay (φ=0): N_c = 5.7, N_q = 1.0, N_γ = 0. For general shear failure; for local shear failure, use c' = (2/3)c and tanφ' = (2/3)tanφ."
    },
    {
        "id": "f11-water-table-factors",
        "unit": 3,
        "title": "Water Table Correction Factors (Rw1 & Rw2)",
        "frequency": "100% Guaranteed (4/4 Papers - 7M)",
        "freq_badge": "badge-repeated",
        "latex_main": r"R_{w1} = 0.5 \left( 1 + \frac{z_{w1}}{D_f} \right) \qquad R_{w2} = 0.5 \left( 1 + \frac{z_{w2}}{B} \right)",
        "latex_sub": r"\text{Boundary Limits: } 0.5 \le R_{w1}, R_{w2} \le 1.0 \qquad \text{At Ground Level: } R_{w1} = R_{w2} = 0.5",
        "latex_raw": r"R_{w1} = 0.5 \left(1 + \frac{z_{w1}}{D_f}\right), \quad R_{w2} = 0.5 \left(1 + \frac{z_{w2}}{B}\right)",
        "params": [
            {"sym": "R_{w1}", "name": "Surcharge water table reduction factor (modifies γ D_f N_q)", "unit": "dimensionless"},
            {"sym": "R_{w2}", "name": "Wedge zone water table reduction factor (modifies 0.5 γ B N_γ)", "unit": "dimensionless"},
            {"sym": "z_{w1}", "name": "Depth of water table below ground surface (0 to D_f)", "unit": "m"},
            {"sym": "z_{w2}", "name": "Depth of water table below foundation base (0 to B)", "unit": "m"}
        ],
        "notes": "When water table rises from deep below (depth > D_f + B) to the ground surface, both R_w1 and R_w2 drop from 1.0 to 0.5, halving both surcharge resistance and shear wedge resistance (~50% capacity loss)."
    },
    {
        "id": "f12-housel-plate",
        "unit": 3,
        "title": "Housel's Two-Plate Method for Foundation Bearing Capacity",
        "frequency": "Core Numerical / Theory (3/4 Papers)",
        "freq_badge": "badge-subtle",
        "latex_main": r"Q_1 = A_1 m + P_1 n \qquad Q_2 = A_2 m + P_2 n",
        "latex_sub": r"Q_F = A_F \cdot m + P_F \cdot n \quad (\text{Prototype Foundation Permissible Load})",
        "latex_raw": r"Q_1 = A_1 m + P_1 n, \quad Q_2 = A_2 m + P_2 n \implies Q_F = A_F m + P_F n",
        "params": [
            {"sym": "Q_1, Q_2", "name": "Test loads on plate 1 and plate 2 at permissible settlement", "unit": "kN"},
            {"sym": "A_1, A_2", "name": "Contact surface areas of test plates 1 and 2", "unit": "m²"},
            {"sym": "P_1, P_2", "name": "Perimeters of test plates 1 and 2", "unit": "m"},
            {"sym": "m", "name": "Perimeter shear factor (side shear mobilization)", "unit": "kN/m"},
            {"sym": "n", "name": "Direct bearing factor (base pressure mobilization)", "unit": "kN/m²"},
            {"sym": "Q_F", "name": "Allowable design load of full-scale prototype footing", "unit": "kN"}
        ],
        "notes": "Housel's method bypasses plate size extrapolation errors by testing two plates of different sizes (e.g. 30 cm and 60 cm) at the identical permissible settlement, solving simultaneous equations for m and n."
    },
    {
        "id": "f13-elastic-settlement",
        "unit": 3,
        "title": "Immediate (Elastic) Settlement of Shallow Footings",
        "frequency": "Core Numerical / Theory",
        "freq_badge": "badge-subtle",
        "latex_main": r"S_i = \frac{q B (1 - \mu^2)}{E_s} \cdot I_f",
        "latex_sub": r"\text{Rigid Footing: } I_f \approx 0.82 \qquad \text{Center of Flexible Footing: } I_f \approx 1.12 \text{ (Square)}",
        "latex_raw": r"S_i = \frac{q B (1 - \mu^2)}{E_s} \cdot I_f",
        "params": [
            {"sym": "S_i", "name": "Immediate elastic settlement under foundation load", "unit": "m (or mm)"},
            {"sym": "q", "name": "Net foundation contact pressure", "unit": "kPa"},
            {"sym": "B", "name": "Characteristic footing width / diameter", "unit": "m"},
            {"sym": r"\mu", "name": "Poisson's ratio of foundation soil", "unit": "dimensionless"},
            {"sym": "E_s", "name": "Modulus of elasticity of soil deposit", "unit": "kPa"},
            {"sym": "I_f", "name": "Influence shape and rigidity factor", "unit": "dimensionless"}
        ],
        "notes": "Calculates instantaneous elastic distortion occurring before primary consolidation. Critical for sand deposits and initial settlement in stiff clay layers."
    },

    # Unit 4: Deep Foundations (Piles & Caissons)
    {
        "id": "f14-single-pile-capacity",
        "unit": 4,
        "title": "Single Driven / Bored Pile Capacity in Cohesive Soil",
        "frequency": "100% Guaranteed (4/4 Papers - 7M)",
        "freq_badge": "badge-repeated",
        "latex_main": r"Q_u = Q_b + Q_s = 9 c_u A_b + \alpha \bar{c}_u A_s",
        "latex_sub": r"A_b = \frac{\pi d^2}{4} \qquad A_s = \pi d L \qquad Q_{\text{safe}} = \frac{Q_u}{\text{FS}}",
        "latex_raw": r"Q_u = 9 c_u A_b + \alpha \bar{c}_u A_s, \quad A_b = \frac{\pi d^2}{4}, \quad A_s = \pi d L",
        "params": [
            {"sym": "Q_u", "name": "Ultimate single pile axial compressive capacity", "unit": "kN"},
            {"sym": "Q_b", "name": "Base end-bearing resistance (N_c = 9 per Skempton)", "unit": "kN"},
            {"sym": "Q_s", "name": "Shaft skin friction resistance along pile perimeter", "unit": "kN"},
            {"sym": "c_u", "name": "Undrained cohesion at pile base tip", "unit": "kPa"},
            {"sym": r"\bar{c}_u", "name": "Average undrained cohesion along pile shaft embedment", "unit": "kPa"},
            {"sym": r"\alpha", "name": "Adhesion factor between clay and pile material (0.4 - 0.8)", "unit": "dimensionless"},
            {"sym": "d", "name": "Pile diameter", "unit": "m"},
            {"sym": "L", "name": "Embedded pile length", "unit": "m"}
        ],
        "notes": "Adopt factor of safety FS = 2.5 to 3.0. In soft clay, skin friction Q_s typically accounts for 80-90% of total single pile capacity. For piles driven in sand: Q_u = σ'_v N_q A_b + K_s σ'_v tanδ A_s."
    },
    {
        "id": "f15-pile-group-block",
        "unit": 4,
        "title": "Pile Group Block Failure Capacity in Soft Clay",
        "frequency": "100% Guaranteed (Verbatim 2024 Q4d & 2022 Q4e - 7M)",
        "freq_badge": "badge-repeated",
        "latex_main": r"Q_{\text{ug}} = 9 c_u B^2 + 4 B L \bar{c}_u",
        "latex_sub": r"B = (n_1 - 1)s + d \qquad Q_{\text{safe, group}} = \frac{\min(Q_{\text{ug}}, \, n \cdot Q_u)}{\text{FS}}",
        "latex_raw": r"Q_{\text{ug}} = 9 c_u B^2 + 4 B L \bar{c}_u, \quad B = (n_1 - 1)s + d",
        "params": [
            {"sym": "Q_{\\text{ug}}", "name": "Ultimate block failure capacity of entire pile group mass", "unit": "kN"},
            {"sym": "B", "name": "Overall width of square pile group block perimeter", "unit": "m"},
            {"sym": "s", "name": "Center-to-center pile spacing", "unit": "m"},
            {"sym": "d", "name": "Individual pile diameter", "unit": "m"},
            {"sym": "n_1", "name": "Number of piles in one row (e.g. 3 for a 3x3 group)", "unit": "count"},
            {"sym": "n", "name": "Total number of piles in group (n = n_1²)", "unit": "count"},
            {"sym": "L", "name": "Embedded length of piles", "unit": "m"},
            {"sym": "c_u", "name": "Undrained cohesion of clay", "unit": "kPa"}
        ],
        "notes": "Notice that for block shear, adhesion factor α = 1.0 because failure occurs soil-on-soil along the outer block envelope, not pile-to-soil. Safe group capacity is ALWAYS the smaller of block capacity and individual sum divided by FS."
    },
    {
        "id": "f16-optimum-spacing",
        "unit": 4,
        "title": "Optimum Pile Spacing in Cohesive Soil",
        "frequency": "75% (3/4 Papers - 6-7M Derivation)",
        "freq_badge": "badge-repeated",
        "latex_main": r"s = d + \frac{2d}{\pi \alpha}",
        "latex_sub": r"\text{Derivation Condition: } \text{Block Skin Friction Perimeter} = \sum \text{Individual Pile Skin Friction}",
        "latex_raw": r"s = d + \frac{2d}{\pi \alpha}",
        "params": [
            {"sym": "s", "name": "Optimum center-to-center pile spacing", "unit": "m"},
            {"sym": "d", "name": "Diameter of pile", "unit": "m"},
            {"sym": r"\alpha", "name": "Pile-soil adhesion factor (typically 0.6 - 0.8)", "unit": "dimensionless"}
        ],
        "notes": "Equating group perimeter capacity 4BL c_u to n individual friction sum n(πα d L c_u) yields s = d + (2d / πα). For α = 0.7, s ≈ 2.5d to 3.0d, perfectly matching standard Indian Standard spacing guidelines (s ≥ 2.5d to 3d)."
    },
    {
        "id": "f17-converse-labarre",
        "unit": 4,
        "title": "Converse-Labarre Pile Group Efficiency Formula",
        "frequency": "Core Numerical / Theory",
        "freq_badge": "badge-subtle",
        "latex_main": r"\eta = 1 - \frac{\theta}{90^\circ} \left[ \frac{(m-1)n + (n-1)m}{m \cdot n} \right]",
        "latex_sub": r"\text{where } \theta = \arctan\left(\frac{d}{s}\right) \text{ (in degrees)} \qquad Q_{\text{group}} = \eta \cdot n \cdot Q_{\text{single}}",
        "latex_raw": r"\eta = 1 - \frac{\theta}{90^\circ} \left[\frac{(m-1)n + (n-1)m}{mn}\right], \quad \theta = \arctan(d/s)",
        "params": [
            {"sym": r"\eta", "name": "Group efficiency factor (typically 0.65 - 0.85 for clays)", "unit": "fraction / %"},
            {"sym": "m, n", "name": "Number of pile rows and columns in rectangular group", "unit": "count"},
            {"sym": "d", "name": "Diameter of pile", "unit": "m"},
            {"sym": "s", "name": "Center-to-center pile spacing", "unit": "m"},
            {"sym": r"\theta", "name": "Overlap interference angle arctan(d/s)", "unit": "degrees"}
        ],
        "notes": "Reflects overlapping stress bulbs between adjacent piles. In friction piles driven in dense sand, soil compaction can cause η > 1.0. In clays, overlapping shear zones always reduce capacity (η < 1.0)."
    },

    # Unit 5: Subsoil Exploration & Testing
    {
        "id": "f18-spt-overburden",
        "unit": 5,
        "title": "SPT Overburden Pressure Correction (CN)",
        "frequency": "100% Guaranteed (4/4 Papers - 7M Numerical)",
        "freq_badge": "badge-repeated",
        "latex_main": r"N' = N \cdot C_N = N \cdot \left[ \frac{350}{\sigma'_v + 70} \right] \quad (\text{per IS: 2131})",
        "latex_sub": r"\text{Constraint: } C_N \le 2.0 \quad (\sigma'_v \le 280\text{ kPa}) \qquad \text{Peck \& Hanson: } N' = N \cdot \sqrt{\frac{100}{\sigma'_v}}",
        "latex_raw": r"N' = N \cdot C_N = N \cdot \left[\frac{350}{\sigma'_v + 70}\right] \quad (C_N \le 2.0)",
        "params": [
            {"sym": "N", "name": "Observed field SPT blow count for final 300 mm drive", "unit": "blows / 300 mm"},
            {"sym": "N'", "name": "Overburden-corrected SPT blow count", "unit": "blows / 300 mm"},
            {"sym": "C_N", "name": "Overburden correction factor (capped at 2.0)", "unit": "dimensionless"},
            {"sym": r"\sigma'_v", "name": "Effective vertical overburden stress at test elevation", "unit": "kPa"}
        ],
        "notes": "Low confining stress at shallow depths artificially underestimates density; deep overburden artificially overestimates blow counts. Must always be calculated and applied BEFORE dilatancy correction."
    },
    {
        "id": "f19-spt-dilatancy",
        "unit": 5,
        "title": "SPT Dilatancy Correction (Terzaghi & Peck)",
        "frequency": "100% Guaranteed (4/4 Papers - 7M Numerical)",
        "freq_badge": "badge-repeated",
        "latex_main": r"N'' = 15 + \frac{1}{2}(N' - 15) \qquad (\text{Applied when } N' > 15 \text{ below WT})",
        "latex_sub": r"\text{Condition: Fine saturated sand or silty sand below groundwater table with } N' > 15",
        "latex_raw": r"N'' = 15 + 0.5(N' - 15)",
        "params": [
            {"sym": "N''", "name": "Final design SPT blow count after dilatancy correction", "unit": "blows / 300 mm"},
            {"sym": "N'", "name": "Overburden-corrected blow count from Step 1", "unit": "blows / 300 mm"}
        ],
        "notes": "In saturated fine sand/silt, rapid hammer impacts cause dynamic volume expansion (dilatancy), creating transient negative pore water pressures that falsely increase shear resistance and blow counts. The dilatancy correction removes this non-conservative artifact."
    },
    {
        "id": "f20-sampler-area-ratio",
        "unit": 5,
        "title": "Soil Sampler Design Criteria (Ar, Ci, Co)",
        "frequency": "100% Guaranteed (4/4 Papers - 3-7M)",
        "freq_badge": "badge-repeated",
        "latex_main": r"A_r = \frac{D_{\text{ext}}^2 - D_{\text{int}}^2}{D_{\text{int}}^2} \times 100\%",
        "latex_sub": r"C_i = \frac{D_s - D_c}{D_c} \times 100\% \quad (1\%\text{--}3\%) \qquad C_o = \frac{D_w - D_t}{D_t} \times 100\% \quad (0\%\text{--}2\%)",
        "latex_raw": r"A_r = \frac{D_{\text{ext}}^2 - D_{\text{int}}^2}{D_{\text{int}}^2} \times 100\%, \quad C_i = \frac{D_s - D_c}{D_c} \times 100\%",
        "params": [
            {"sym": "A_r", "name": "Area ratio of sampler cutting edge (disturbed vs undisturbed indicator)", "unit": "%"},
            {"sym": "C_i", "name": "Inside clearance ratio (prevents tube friction & internal swelling)", "unit": "%"},
            {"sym": "C_o", "name": "Outside clearance ratio (reduces outside driving resistance)", "unit": "%"},
            {"sym": "D_{\\text{ext}}", "name": "External diameter of cutting shoe", "unit": "mm"},
            {"sym": "D_{\\text{int}}", "name": "Internal diameter of cutting edge orifice", "unit": "mm"},
            {"sym": "D_s", "name": "Internal diameter of main sampler liner tube", "unit": "mm"}
        ],
        "notes": "For undisturbed sampling in soft/sensitive clay: A_r must be ≤ 10% to 12% (thin-walled Shelby tube). Thick-walled split-spoon samplers have A_r ≈ 30-45%, producing heavily disturbed samples suitable only for index classification."
    },
    {
        "id": "f21-rock-rqd",
        "unit": 5,
        "title": "Rock Quality Designation (RQD) & Core Recovery",
        "frequency": "Core Practical / Theory (3/4 Papers)",
        "freq_badge": "badge-subtle",
        "latex_main": r"\text{RQD} = \frac{\sum (\text{Length of sound core pieces } \ge 10\text{ cm})}{\text{Total core drill run length}} \times 100\%",
        "latex_sub": r"\text{TCR (Total Core Recovery)} = \frac{\text{Total recovered core length}}{\text{Total run length}} \times 100\%",
        "latex_raw": r"\text{RQD} = \frac{\sum (L_{\text{core}} \ge 10\text{ cm})}{L_{\text{total}}} \times 100\%",
        "params": [
            {"sym": r"\text{RQD}", "name": "Rock Quality Designation index percentage", "unit": "%"},
            {"sym": r"\text{TCR}", "name": "Total Core Recovery ratio", "unit": "%"},
            {"sym": "L_{\\text{core}}", "name": "Individual sound cylindrical rock core piece length", "unit": "cm / mm"}
        ],
        "notes": "Standard Deere classification: RQD < 25% (Very Poor), 25-50% (Poor), 50-75% (Fair), 75-90% (Good), 90-100% (Excellent). Pieces showing mechanical breaks from drilling must be fitted together as a single intact piece."
    }
]

formulas_css = """
        /* ----------------------------------------------------
           FORMULA SHOWCASE & KATEX MATHEMATICAL DISPLAY
           ---------------------------------------------------- */
        .sol-math-block {
            display: block;
            background-color: var(--secondary);
            border-radius: var(--radius-md);
            padding: 0.85rem 1.25rem;
            margin: 0.75rem 0;
            overflow-x: auto;
            overflow-y: hidden;
            font-size: 1.0625rem;
            line-height: 1.6;
            color: var(--foreground);
            text-align: center;
        }

        .sol-math-block .katex-display {
            margin: 0.25rem 0;
        }

        /* KATEX FRACTION DIVIDING LINE & MATHEMATICAL BORDER ENFORCEMENT */
        .katex * {
            border-color: currentColor;
        }

        .katex .mfrac .frac-line {
            display: inline-block !important;
            width: 100% !important;
            border-bottom-style: solid !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
            min-height: 1.2px !important;
        }

        .katex .overline .overline-line,
        .katex .underline .underline-line {
            border-bottom-style: solid !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
            min-height: 1.2px !important;
        }

        .katex .hdashline {
            border-bottom-style: dashed !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
        }

        .katex .hline {
            border-bottom-style: solid !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
        }

        .katex .rule {
            border-style: solid !important;
            border-color: currentColor !important;
        }

        .sol-math-inline {
            display: inline-block;
            background-color: var(--secondary);
            border-radius: var(--radius-sm);
            padding: 0.125rem 0.4rem;
            font-size: 0.9375rem;
            margin: 0 0.15rem;
            vertical-align: baseline;
            color: var(--foreground);
        }

        .syllabus-formula-stack {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            min-width: 290px;
        }

        .syllabus-formula-item {
            background-color: var(--secondary);
            border-radius: var(--radius-sm);
            padding: 0.5rem 0.85rem;
            transition: background-color 0.15s ease;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }

        .syllabus-formula-item:hover {
            background-color: var(--secondary-hover);
        }

        .syllabus-formula-label {
            font-size: 0.6875rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--muted-foreground);
            line-height: 1.2;
        }

        .syllabus-formula-math {
            font-size: 0.96875rem;
            color: var(--foreground);
            overflow-x: auto;
            overflow-y: hidden;
            padding: 0.15rem 0;
            line-height: 1.4;
        }

        .syllabus-formula-math .katex {
            font-size: 1.05rem;
        }

        /* Formula Reference Hub */
        .formula-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2rem;
        }

        @media (max-width: 640px) {
            .formula-cards-grid {
                grid-template-columns: 1fr;
            }
        }

        .formula-card {
            background-color: var(--card);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-sm);
            padding: 1.35rem 1.5rem;
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }

        .formula-card:hover {
            box-shadow: var(--shadow-md);
        }

        .formula-card-header {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 0.75rem;
        }

        .formula-card-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            align-items: center;
        }

        .formula-card-actions {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            flex-shrink: 0;
        }

        .btn-copy-formula {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.71875rem;
            font-weight: 500;
            padding: 0.3rem 0.55rem;
            background-color: var(--math-copy-btn-bg);
            color: var(--muted-foreground);
            border-radius: var(--radius-sm);
            border: none;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .btn-copy-formula:hover {
            background-color: var(--math-copy-btn-hover);
            color: var(--foreground);
        }

        .btn-copy-formula.copied {
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
        }

        .formula-card-title {
            font-size: 1.0625rem;
            font-weight: 700;
            color: var(--foreground);
            line-height: 1.35;
            margin: 0;
        }

        .formula-equation-box {
            background-color: var(--math-display-bg);
            border-radius: var(--radius-md);
            padding: 1.1rem 1.25rem;
            text-align: center;
            overflow-x: auto;
            overflow-y: hidden;
            line-height: 1.5;
            margin: 0.25rem 0;
        }

        .formula-equation-box .katex-display {
            margin: 0.25rem 0;
        }

        .formula-equation-box .katex {
            font-size: 1.22rem;
            color: var(--foreground);
        }

        .formula-secondary-box {
            background-color: var(--secondary);
            border-radius: var(--radius-sm);
            padding: 0.65rem 0.95rem;
            font-size: 0.875rem;
            overflow-x: auto;
            text-align: center;
            color: var(--foreground);
        }

        .formula-secondary-box .katex {
            font-size: 0.98rem;
        }

        .formula-param-section {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-top: 0.25rem;
        }

        .formula-param-header {
            font-size: 0.6875rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--muted-foreground);
        }

        .formula-param-grid {
            display: grid;
            grid-template-columns: auto 1fr auto;
            row-gap: 0.45rem;
            column-gap: 0.85rem;
            align-items: baseline;
        }

        .formula-param-row,
        .formula-param-pill {
            display: contents;
        }

        .formula-param-row .param-sym,
        .formula-param-pill .param-sym {
            font-weight: 600;
            color: var(--foreground);
            white-space: nowrap;
        }

        .formula-param-row .param-sym .katex,
        .formula-param-pill .param-sym .katex {
            font-size: 0.9375rem;
        }

        .formula-param-row .param-desc,
        .formula-param-pill .param-desc {
            color: var(--foreground);
            font-size: 0.875rem;
            line-height: 1.5;
        }

        .formula-param-row .param-unit,
        .formula-param-pill .param-unit {
            background: none !important;
            color: var(--muted-foreground);
            font-size: 0.8125rem;
            font-weight: 500;
            white-space: nowrap;
            text-align: right;
            justify-self: end;
            padding: 0;
            border-radius: 0;
        }

        @media (max-width: 540px) {
            .formula-param-grid {
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }

            .formula-param-row,
            .formula-param-pill {
                display: flex;
                flex-wrap: wrap;
                align-items: baseline;
                gap: 0.25rem 0.6rem;
            }

            .formula-param-row .param-sym,
            .formula-param-pill .param-sym {
                min-width: 44px;
            }

            .formula-param-row .param-desc,
            .formula-param-pill .param-desc {
                flex: 1 1 180px;
            }

            .formula-param-row .param-unit,
            .formula-param-pill .param-unit {
                margin-left: auto;
            }
        }

        .table-formula-cell {
            padding: 0.25rem 0;
            line-height: 1.4;
        }

        .table-formula-cell .katex-display {
            margin: 0.25rem 0;
        }

        /* Minimal Formula Control Bar */
        .formula-control-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            width: 100%;
            margin-bottom: 1.5rem;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
        }

        .formula-control-left {
            display: inline-flex;
            align-items: center;
            gap: 0.85rem;
            flex-wrap: wrap;
        }

        .formula-unit-wrapper {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background-color: var(--secondary);
            padding: 2.5px 3px 2.5px 0.75rem;
            border-radius: var(--radius-full);
            max-width: 100%;
        }

        .formula-unit-label {
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
            user-select: none;
            white-space: nowrap;
            padding-right: 0.15rem;
        }

        #formulaUnitFilters {
            display: inline-flex;
            align-items: center;
            gap: 2px;
            overflow-x: auto;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }

        #formulaUnitFilters::-webkit-scrollbar {
            display: none;
        }

        .formula-search-box {
            margin-left: auto;
            width: 260px;
            max-width: 100%;
            position: relative;
        }

        .formula-search-box .search-input {
            width: 100%;
            background-color: var(--input-bg);
            border-radius: var(--radius-full);
            padding: 0.4rem 2rem 0.4rem 2.2rem;
            font-size: 0.8125rem;
            color: var(--foreground);
            height: 32px;
            box-sizing: border-box;
            border: none;
            outline: none;
            transition: background-color 0.15s ease, box-shadow 0.15s ease;
        }

        .formula-search-box .search-input:focus {
            background-color: var(--card);
            box-shadow: 0 0 0 2px var(--secondary-hover);
        }

        @media (max-width: 768px) {
            .formula-cards-grid {
                grid-template-columns: 1fr !important;
                gap: 1rem;
            }
            .formula-card {
                padding: 1rem 1rem;
                gap: 0.75rem;
                border-radius: var(--radius-md);
            }
            .formula-equation-box {
                padding: 0.75rem 0.65rem;
            }
            .formula-equation-box .katex {
                font-size: 1.05rem;
            }
            .syllabus-formula-stack {
                min-width: 100%;
            }
            .formula-control-bar {
                flex-direction: column;
                align-items: stretch;
                gap: 0.75rem;
            }
            .formula-control-left {
                width: 100%;
                justify-content: space-between;
            }
            .formula-search-box {
                width: 100%;
                margin-left: 0;
            }
        }
"""

view_formulas_html = """<div class="app-page-view" id="view-formulas">
            <!-- Minimal Formula Control Bar: Unit & Counter on Left, Minimal Search on Right -->
            <div class="formula-control-bar">
                <div class="formula-control-left">
                    <div class="formula-unit-wrapper">
                        <span class="formula-unit-label">Unit</span>
                        <div class="filter-pills-row" id="formulaUnitFilters">
                            <button class="filter-pill-btn active" data-unit="all">All</button>
                            <button class="filter-pill-btn" data-unit="1" title="Unit 1: Earth Pressure (5 formulas)">Unit 1</button>
                            <button class="filter-pill-btn" data-unit="2" title="Unit 2: Shear &amp; Slopes (4 formulas)">Unit 2</button>
                            <button class="filter-pill-btn" data-unit="3" title="Unit 3: Foundations (4 formulas)">Unit 3</button>
                            <button class="filter-pill-btn" data-unit="4" title="Unit 4: Piles &amp; Caissons (4 formulas)">Unit 4</button>
                            <button class="filter-pill-btn" data-unit="5" title="Unit 5: Soil Exploration (4 formulas)">Unit 5</button>
                        </div>
                    </div>

                    <span class="match-counter-pill" id="formulaMatchCounter">21 formulas</span>

                    <button class="reset-filters-btn" id="formulaResetBtn" title="Reset search & filters" style="display: none;">
                        <i class="icon icon-xs hgi-stroke hgi-arrow-reload-horizontal"></i>
                        Reset
                    </button>
                </div>

                <div class="search-box-wrapper formula-search-box">
                    <i class="icon icon-sm search-icon hgi-stroke hgi-search-01"></i>
                    <input type="text" class="search-input" id="formulaSearchInput" placeholder="Search formulas..." aria-label="Search formulas">
                    <button class="search-clear-btn" id="formulaSearchClearBtn" title="Clear search" aria-label="Clear search" style="display: none;">
                        <i class="icon icon-xs hgi-stroke hgi-cancel-01"></i>
                    </button>
                </div>
            </div>

            <!-- Cards Container (Default & Permanent) -->
            <div class="formula-cards-grid" id="formulaCardsGrid">
                <!-- Rendered dynamically by JavaScript -->
            </div>
        </div>"""

u1_formulas_html = r"""<div class="syllabus-formula-stack">
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Rankine Active Coeff</span>
        <div class="syllabus-formula-math">$$K_a = \frac{1 - \sin\phi}{1 + \sin\phi} = \tan^2\left(45^\circ - \frac{\phi}{2}\right)$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Tension Crack Depth</span>
        <div class="syllabus-formula-math">$$z_c = \frac{2c}{\gamma \sqrt{K_a}}$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">At-Rest Earth Pressure</span>
        <div class="syllabus-formula-math">$$K_0 = \frac{\mu}{1 - \mu} \approx 1 - \sin\phi$$</div>
    </div>
</div>"""

u2_formulas_html = r"""<div class="syllabus-formula-stack">
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Mohr-Coulomb Failure</span>
        <div class="syllabus-formula-math">$$\sigma'_1 = \sigma'_3 N_\phi + 2c'\sqrt{N_\phi}$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Triaxial Area Correction</span>
        <div class="syllabus-formula-math">$$A = \frac{A_0}{1 - \varepsilon} \quad (\varepsilon = \Delta L / L_0)$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Infinite Slope Seepage FS</span>
        <div class="syllabus-formula-math">$$FS = \frac{c' + \gamma' z \cos^2\beta \tan\phi'}{\gamma_{\text{sat}} z \sin\beta \cos\beta}$$</div>
    </div>
</div>"""

u3_formulas_html = r"""<div class="syllabus-formula-stack">
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Terzaghi Bearing Capacity</span>
        <div class="syllabus-formula-math">$$q_{\text{ult}} = c N_c + q N_q R_{w1} + \frac{1}{2}\gamma B N_\gamma R_{w2}$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Water Table Corrections</span>
        <div class="syllabus-formula-math">$$R_{w1}, R_{w2} = 0.5\left(1 + \frac{z_w}{d}\right)$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Immediate Elastic Settlement</span>
        <div class="syllabus-formula-math">$$S_i = \frac{q B (1 - \mu^2)}{E_s} \cdot I_f$$</div>
    </div>
</div>"""

u4_formulas_html = r"""<div class="syllabus-formula-stack">
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Block Failure Capacity</span>
        <div class="syllabus-formula-math">$$Q_{\text{ug}} = 9 c_u B^2 + 4 B L \bar{c}_u$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Individual Pile Sum</span>
        <div class="syllabus-formula-math">$$Q_{\text{ui}} = n \cdot (9 c_u A_b + \alpha c_u A_s)$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Optimum Spacing in Clay</span>
        <div class="syllabus-formula-math">$$s = d + \frac{2d}{\pi \alpha} \approx 2.5d\text{--}3d$$</div>
    </div>
</div>"""

u5_formulas_html = r"""<div class="syllabus-formula-stack">
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">SPT Overburden Correction</span>
        <div class="syllabus-formula-math">$$N' = N \cdot \left[\frac{350}{\sigma'_v + 70}\right] \le 2N$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">SPT Dilatancy Correction</span>
        <div class="syllabus-formula-math">$$N'' = 15 + \frac{1}{2}(N' - 15)$$</div>
    </div>
    <div class="syllabus-formula-item">
        <span class="syllabus-formula-label">Sampler Area Ratio</span>
        <div class="syllabus-formula-math">$$A_r = \left(\frac{D_{\text{ext}}^2 - D_{\text{int}}^2}{D_{\text{int}}^2}\right) \times 100\% \le 10\%$$</div>
    </div>
</div>"""

formulas_js_template = """
<script>
(function() {
    const MASTER_FORMULAS = __MASTER_FORMULAS_JSON__;
    const STORAGE_KEY_FORMULA_FILTERS = 'geotech_formula_filters';
    let currentFormulaUnit = 'all';
    let formulaSearchQuery = '';

    try {
        const savedF = JSON.parse(localStorage.getItem(STORAGE_KEY_FORMULA_FILTERS) || '{}');
        if (savedF.unit) currentFormulaUnit = savedF.unit;
        if (typeof savedF.search === 'string') formulaSearchQuery = savedF.search;
    } catch(e) {}

    function saveFormulaFilters() {
        try {
            localStorage.setItem(STORAGE_KEY_FORMULA_FILTERS, JSON.stringify({
                unit: currentFormulaUnit,
                search: formulaSearchQuery,
                layout: 'cards'
            }));
        } catch(e) {}
    }

    function renderAllMath() {
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(document.body, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '\\\\(', right: '\\\\)', display: false},
                    {left: '\\\\[', right: '\\\\]', display: true}
                ],
                ignoredTags: ["script", "noscript", "style", "textarea"],
                preProcess: function(math) {
                    if (!math) return "";
                    var s = math;
                    s = s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '\\\\&').replace(/&nbsp;/g, ' ').replace(/&mdash;/g, '\\\\text{ --- }').replace(/&ndash;/g, '\\\\text{ -- }');
                    s = s.replace(/\\\\_/g, '_');
                    s = s.replace(/[⁻^\\\\-]*⁻[⁻^\\\\-]*\\^?(\\d+)/g, '^{-$1}');
                    s = s.replace(/10\\s*\\^-\\s*(\\d+)/g, '10^{-$1}');
                    var sup = {"⁰":"0","¹":"1","²":"2","³":"3","⁴":"4","⁵":"5","⁶":"6","⁷":"7","⁸":"8","⁹":"9","⁺":"+","⁻":"-"};
                    s = s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+/g, function(m) {
                        var res = '';
                        for (var i = 0; i < m.length; i++) { res += sup[m[i]] || m[i]; }
                        return '^{' + res + '}';
                    });
                    s = s.replace(/(?<!\\\\)%/g, '\\\\%');
                    s = s.replace(/Peck\\s*&\\s*Hanson/g, 'Peck \\\\& Hanson');
                    return s;
                },
                throwOnError: false,
                minRuleThickness: 0.05
            });
        }
    }
    window.renderAllMath = renderAllMath;

    window.setFormulaLayout = function(layout) {
        const cardsGrid = document.getElementById('formulaCardsGrid');
        if (cardsGrid) {
            cardsGrid.style.display = 'grid';
        }
        renderAllMath();
    };

    window.copyLatex = function(btn, latex) {
        navigator.clipboard.writeText(latex).then(() => {
            const originalHtml = btn.innerHTML;
            btn.classList.add('copied');
            btn.innerHTML = `
                <i class="icon icon-sm hgi-stroke hgi-tick-01"></i>
                Copied!
            `;
            setTimeout(() => {
                btn.classList.remove('copied');
                btn.innerHTML = originalHtml;
            }, 1800);
        }).catch(err => {
            console.error('Copy failed', err);
        });
    };

    function renderFormulas() {
        const cardsGrid = document.getElementById('formulaCardsGrid');
        const tableBody = document.getElementById('formulaTableBody');
        const summaryEl = document.getElementById('formulaFilterSummary');
        const counterEl = document.getElementById('formulaMatchCounter');

        if (!cardsGrid) return;

        const filtered = MASTER_FORMULAS.filter(item => {
            if (currentFormulaUnit !== 'all' && String(item.unit) !== String(currentFormulaUnit)) {
                return false;
            }
            if (formulaSearchQuery) {
                const q = formulaSearchQuery.toLowerCase();
                const titleMatch = (item.title || '').toLowerCase().includes(q);
                const notesMatch = (item.notes || '').toLowerCase().includes(q);
                const latexMatch = (item.latex_main + ' ' + (item.latex_sub || '')).toLowerCase().includes(q);
                const paramMatch = (item.params || []).some(p => 
                    (p.sym || '').toLowerCase().includes(q) || 
                    (p.name || '').toLowerCase().includes(q) ||
                    (p.unit || '').toLowerCase().includes(q)
                );
                if (!titleMatch && !notesMatch && !latexMatch && !paramMatch) {
                    return false;
                }
            }
            return true;
        });

        if (counterEl) {
            if (filtered.length === MASTER_FORMULAS.length) {
                counterEl.textContent = `${MASTER_FORMULAS.length} formulas`;
            } else {
                counterEl.textContent = `${filtered.length} of ${MASTER_FORMULAS.length} matched`;
            }
        }
        if (summaryEl) summaryEl.textContent = `Showing ${filtered.length} master engineering formulas`;

        const resetBtn = document.getElementById('formulaResetBtn');
        if (resetBtn) {
            const isCustom = (currentFormulaUnit !== 'all' || Boolean(formulaSearchQuery));
            resetBtn.style.display = isCustom ? 'inline-flex' : 'none';
        }

        if (filtered.length === 0) {
            cardsGrid.innerHTML = `
                <div class="empty-results" style="grid-column: 1 / -1;">
                    <i class="icon icon-lg hgi-stroke hgi-search-01" style="margin-bottom: 0.5rem; color: var(--muted-foreground);"></i>
                    <div class="empty-results-title">No matching formulas found</div>
                    <p class="text-body-small">Try clearing search terms or selecting "All Units".</p>
                </div>
            `;
            if (tableBody) tableBody.innerHTML = `<tr><td colspan="4" style="text-align: center; padding: 2rem; color: var(--muted-foreground);">No matching formulas found.</td></tr>`;
            return;
        }

        // Render Cards
        cardsGrid.innerHTML = filtered.map(item => {
            const paramsHtml = item.params.map(p => `
                <div class="formula-param-row">
                    <span class="param-sym">$${p.sym}$</span>
                    <span class="param-desc">${p.name}</span>
                    <span class="param-unit">${p.unit}</span>
                </div>
            `).join('');

            const subBox = item.latex_sub ? `
                <div class="formula-secondary-box">
                    $$${item.latex_sub}$$
                </div>
            ` : '';

            const safeLatex = item.latex_raw.replace(/'/g, "\\\\'").replace(/"/g, '&quot;');

            return `
            <div class="formula-card" id="${item.id}">
                <div class="formula-card-header">
                    <div class="formula-card-badges">
                        <span class="badge badge-unit-${item.unit}">Unit ${item.unit}</span>
                        <span class="badge ${item.freq_badge}">${item.frequency}</span>
                    </div>
                    <div class="formula-card-actions">
                        <button class="btn-copy-formula" onclick="copyLatex(this, '${safeLatex}')" title="Copy LaTeX code">
                            <i class="icon icon-sm hgi-stroke hgi-copy-01"></i>
                            Copy LaTeX
                        </button>
                    </div>
                </div>

                <h3 class="formula-card-title">${item.title}</h3>

                <div class="formula-equation-box">
                    $$${item.latex_main}$$
                </div>
                ${subBox}

                <div class="formula-param-section">
                    <span class="formula-param-header">Parameter Breakdown &amp; SI Units:</span>
                    <div class="formula-param-grid">
                        ${paramsHtml}
                    </div>
                </div>
            </div>
            `;
        }).join('');

        // Render Table (if present)
        if (tableBody) {
            tableBody.innerHTML = filtered.map(item => {
                const paramsList = (item.params || []).map(p => `
                    <li><strong>$${p.sym}$</strong> &ndash; ${p.name} <span class="text-body-small" style="color: var(--muted-foreground);">(${p.unit})</span></li>
                `).join('');

                return `
                <tr>
                    <td><span class="badge badge-unit-${item.unit}">Unit ${item.unit}</span></td>
                    <td>
                        <strong>${item.title}</strong>
                        <div class="text-body-small" style="color: var(--muted-foreground); margin-top: 0.25rem;">${item.frequency}</div>
                    </td>
                    <td>
                        <div class="table-formula-cell">
                            $$${item.latex_main}$$
                            ${item.latex_sub ? `<div style="font-size: 0.85rem; color: var(--muted-foreground); margin-top: 0.35rem;">$$${item.latex_sub}$$</div>` : ''}
                        </div>
                    </td>
                    <td>
                        <ul class="table-list table-list-compact" style="margin: 0; padding-left: 1rem;">
                            ${paramsList}
                        </ul>
                    </td>
                </tr>
                `;
            }).join('');
        }

        renderAllMath();
    }
    window.renderFormulas = renderFormulas;

    function initFormulaListeners() {
        const unitFilters = document.querySelectorAll('#formulaUnitFilters .filter-pill-btn');
        unitFilters.forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-unit') === String(currentFormulaUnit));
            btn.addEventListener('click', () => {
                unitFilters.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentFormulaUnit = btn.getAttribute('data-unit');
                saveFormulaFilters();
                renderFormulas();
            });
        });

        let formulaSearchTimeout;
        const fInput = document.getElementById('formulaSearchInput');
        const fClearBtn = document.getElementById('formulaSearchClearBtn');
        const fResetBtn = document.getElementById('formulaResetBtn');

        if (fInput) {
            if (formulaSearchQuery) {
                fInput.value = formulaSearchQuery;
                if (fClearBtn) fClearBtn.style.display = 'inline-flex';
            }
            fInput.addEventListener('input', (e) => {
                clearTimeout(formulaSearchTimeout);
                formulaSearchTimeout = setTimeout(() => {
                    formulaSearchQuery = e.target.value.trim();
                    if (fClearBtn) {
                        fClearBtn.style.display = formulaSearchQuery ? 'inline-flex' : 'none';
                    }
                    saveFormulaFilters();
                    renderFormulas();
                }, 200);
            });
        }

        if (fClearBtn && fInput) {
            fClearBtn.addEventListener('click', () => {
                fInput.value = '';
                formulaSearchQuery = '';
                fClearBtn.style.display = 'none';
                saveFormulaFilters();
                renderFormulas();
                fInput.focus();
            });
        }

        window.resetFormulaFilters = function() {
            currentFormulaUnit = 'all';
            formulaSearchQuery = '';
            if (fInput) fInput.value = '';
            if (fClearBtn) fClearBtn.style.display = 'none';
            unitFilters.forEach(b => {
                b.classList.toggle('active', b.getAttribute('data-unit') === 'all');
            });
            saveFormulaFilters();
            renderFormulas();
        };

        if (fResetBtn) {
            fResetBtn.addEventListener('click', window.resetFormulaFilters);
        }

        // Hook into switchPageView
        if (typeof window.switchPageView === 'function') {
            const originalSwitch = window.switchPageView;
            window.switchPageView = function(pageId) {
                originalSwitch(pageId);
                if (pageId === 'formulas') {
                    renderFormulas();
                } else {
                    setTimeout(renderAllMath, 50);
                }
            };
        }

        // Hook into renderQuestions
        if (typeof window.renderQuestions === 'function') {
            const originalRenderQuestions = window.renderQuestions;
            window.renderQuestions = function() {
                originalRenderQuestions();
                setTimeout(renderAllMath, 50);
            };
        }

        // Hook into toggleSolution
        if (typeof window.toggleSolution === 'function') {
            const originalToggle = window.toggleSolution;
            window.toggleSolution = function(id, event) {
                originalToggle(id, event);
                setTimeout(renderAllMath, 30);
            };
        }

        // Hook into toggleChecklistSolution
        if (typeof window.toggleChecklistSolution === 'function') {
            const originalChecklistToggle = window.toggleChecklistSolution;
            window.toggleChecklistSolution = function(id, event) {
                originalChecklistToggle(id, event);
                setTimeout(renderAllMath, 30);
            };
        }

        renderFormulas();
        setTimeout(renderAllMath, 100);
        setTimeout(renderAllMath, 500);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFormulaListeners);
    } else {
        initFormulaListeners();
    }
    window.addEventListener('load', () => setTimeout(renderAllMath, 200));
})();
</script>
"""

def build_initial_cards_html():
    cards = []
    for item in master_formulas:
        params_html = "".join([
            f'<div class="formula-param-row"><span class="param-sym">${p["sym"]}$</span><span class="param-desc">{p["name"]}</span><span class="param-unit">{p["unit"]}</span></div>' for p in item["params"]
        ])
        sub_box = f'<div class="formula-secondary-box">$${item["latex_sub"]}$$</div>' if item.get("latex_sub") else ""
        safe_latex = item["latex_raw"].replace("'", "\\'").replace('"', '&quot;')
        cards.append(f'''
        <div class="formula-card" id="{item['id']}">
            <div class="formula-card-header">
                <div class="formula-card-badges">
                    <span class="badge badge-unit-{item['unit']}">Unit {item['unit']}</span>
                    <span class="badge {item['freq_badge']}">{item['frequency']}</span>
                </div>
                <div class="formula-card-actions">
                    <button class="btn-copy-formula" onclick="copyLatex(this, '{safe_latex}')" title="Copy LaTeX code">
                        <i class="icon icon-sm hgi-stroke hgi-copy-01"></i>
                        Copy LaTeX
                    </button>
                </div>
            </div>

            <h3 class="formula-card-title">{item['title']}</h3>

            <div class="formula-equation-box">
                $${item['latex_main']}$$
            </div>
            {sub_box}

            <div class="formula-param-section">
                <span class="formula-param-header">Parameter Breakdown &amp; SI Units:</span>
                <div class="formula-param-grid">
                    {params_html}
                </div>
            </div>
        </div>''')
    return "\n".join(cards)

def build_initial_table_rows():
    rows = []
    for item in master_formulas:
        sub_latex = f'<div style="font-size: 0.85rem; color: var(--muted-foreground); margin-top: 0.35rem;">$${item["latex_sub"]}$$</div>' if item.get("latex_sub") else ""
        params_list = "".join([
            f'<li><strong>${p["sym"]}$</strong> &ndash; {p["name"]} <span class="text-body-small" style="color: var(--muted-foreground);">({p["unit"]})</span></li>' for p in item["params"]
        ])
        rows.append(f'''
        <tr>
            <td><span class="badge badge-unit-{item['unit']}">Unit {item['unit']}</span></td>
            <td>
                <strong>{item['title']}</strong>
                <div class="text-body-small" style="color: var(--muted-foreground); margin-top: 0.25rem;">{item['frequency']}</div>
            </td>
            <td>
                <div class="table-formula-cell">
                    $${item['latex_main']}$$
                    {sub_latex}
                </div>
            </td>
            <td>
                <ul class="table-list table-list-compact" style="margin: 0; padding-left: 1rem;">
                    {params_list}
                </ul>
            </td>
        </tr>''')
    return "\n".join(rows)

def html_to_katex(html_str):
    if not html_str:
        return ""
    s = html_str.strip()
    
    # 0. Equation labels at end
    s = re.sub(r"(?:&nbsp;|\s)*(?:&mdash;|—|--|-)\s*\((Equation\s*\d+|\d+)\)", r"\\qquad\\text{--- (\1)}", s)
    
    # 1. Clean bold & italics
    s = re.sub(r'<strong>(.*?)</strong>', lambda m: r'\mathbf{' + m.group(1) + '}', s)
    s = re.sub(r'<em>(.*?)</em>', lambda m: m.group(1), s)
    
    # 2. Unicode subscripts
    sub_unicode = {
        '₀': '_0', '₁': '_1', '₂': '_2', '₃': '_3', '₄': '_4',
        '₅': '_5', '₆': '_6', '₇': '_7', '₈': '_8', '₉': '_9',
        '₊': '_+', '₋': '_-', '₌': '_=', '₍': '_(', '₎': '_)',
        'ᵤ': '_u', 'ᵥ': '_v', 'ₚ': '_p', 'ₛ': '_s', 'ₐ': '_a', 'ᵣ': '_r'
    }
    for k, v in sub_unicode.items():
        s = s.replace(k, v)

    # 3. Subscripts & Superscripts tags and entities
    s = re.sub(r'<sub>(.*?)</sub>', lambda m: '_{' + m.group(1) + '}', s)
    s = re.sub(r'<sup>(.*?)</sup>', lambda m: '^{' + m.group(1) + '}', s)
    s = s.replace('&sup1;', '¹').replace('&sup2;', '²').replace('&sup3;', '³').replace('&deg;', '^\\circ')
    s = s.replace('°', '^\\circ')

    # 3b. Normalize negative exponents and Unicode superscript runs (e.g. 10⁻³, 10⁻^3, 10^-3, 10⁻⁶)
    s = re.sub(r'[⁻^\\-]*⁻[⁻^\\-]*\^?(\d+)', r'^{-\1}', s)
    s = re.sub(r'10\s*\^-\s*\{?(\d+)\}?', r'10^{-\1}', s)
    s = re.sub(r'(?<!\^)\^-\s*\{?(\d+)\}?', r'^{-\1}', s)
    sup_map = {
        '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
        '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
        '⁺': '+', '⁻': '-', '⁼': '=', '⁽': '(', '⁾': ')'
    }
    s = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾]+)', lambda m: '^{' + ''.join(sup_map.get(c, c) for c in m.group(1)) + '}', s)

    # 4. Greek and Math Entities & HTML Entities
    rep = {
        '&lt;': '<', '&gt;': '>', '&nbsp;': ' ', '&mdash;': r'\text{ --- }', '&ndash;': r'\text{ -- }',
        '&beta;': r'\beta ', '&phi;': r'\phi ', '&gamma;': r'\gamma ', '&delta;': r'\delta ',
        '&sigma;': r'\sigma ', '&tau;': r'\tau ', '&mu;': r'\mu ', '&epsilon;': r'\varepsilon ',
        '&alpha;': r'\alpha ', '&theta;': r'\theta ', '&lambda;': r'\lambda ', '&eta;': r'\eta ',
        '&psi;': r'\psi ', '&Delta;': r'\Delta ', '&times;': r'\times ', '&middot;': r'\cdot ',
        '&rArr;': r'\implies ', '&approx;': r'\approx ', '&le;': r'\le ', '&ge;': r'\ge ',
        '&ne;': r'\ne ', '&plusmn;': r'\pm ', '&pi;': r'\pi ', '&infin;': r'\infty ',
        'β': r'\beta ', 'φ': r'\phi ', 'γ': r'\gamma ', 'δ': r'\delta ', 'σ': r'\sigma ',
        'τ': r'\tau ', 'μ': r'\mu ', 'ε': r'\varepsilon ', 'α': r'\alpha ', 'θ': r'\theta ',
        'Δ': r'\Delta ', 'π': r'\pi ', '×': r'\times ', '·': r'\cdot ', '⇒': r'\implies ',
        '≈': r'\approx ', '≤': r'\le ', '≥': r'\ge ', '±': r'\pm ',
    }
    for k, v in rep.items():
        s = s.replace(k, v)

    # 4b. Escape unescaped % (LaTeX comment character)
    s = re.sub(r'(?<!\\)%', r'\%', s)

    # 4c. Fix unescaped ampersand in common texts (e.g. Peck & Hanson)
    s = re.sub(r'\bPeck\s*&\s*Hanson\b', r'Peck \\& Hanson', s)
    s = re.sub(r'(?<=\\text\{)(.*?)(?=\})', lambda m: m.group(1).replace('&', r'\&'), s)
        
    # 5. Roots with balanced parentheses/brackets
    s = s.replace('&radic;', r'\sqrt ').replace('√', r'\sqrt ')
    def parse_sqrt(text):
        pos = 0
        out_parts = []
        while True:
            m = re.search(r'\\sqrt\s*([(\[])', text[pos:])
            if not m:
                out_parts.append(text[pos:])
                break
            start = pos + m.start()
            open_char = m.group(1)
            close_char = ')' if open_char == '(' else ']'
            open_idx = pos + m.end() - 1
            out_parts.append(text[pos:start])
            depth = 0
            idx = open_idx
            while idx < len(text):
                ch = text[idx]
                if ch == open_char:
                    depth += 1
                elif ch == close_char:
                    depth -= 1
                    if depth == 0:
                        break
                idx += 1
            if depth == 0 and idx < len(text):
                inside = text[open_idx + 1:idx].strip()
                out_parts.append(r'\sqrt{' + inside + '}')
                pos = idx + 1
            else:
                out_parts.append(r'\sqrt ')
                pos = open_idx + 1
        return ''.join(out_parts)
    s = parse_sqrt(s)
    s = re.sub(r'\\sqrt\s*([0-9]+(?:\.[0-9]+)?)', lambda m: r'\sqrt{' + m.group(1) + '}', s)
    s = re.sub(r'\\sqrt\s*([A-Za-z]+(?:_[A-Za-z0-9{}]+)?)', lambda m: r'\sqrt{' + m.group(1) + '}', s)
    
    # 6. Units
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:kN/m\^2|kN/m\^\{2\}|kN/m²)(?![a-zA-Z0-9])', r'\g<1>\\text{ kN/m}^2', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:kN/m\^3|kN/m\^\{3\}|kN/m³)(?![a-zA-Z0-9])', r'\g<1>\\text{ kN/m}^3', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:kN/m\b)', r'\g<1>\\text{ kN/m}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:kN\b)', r'\g<1>\\text{ kN}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:N/m\^2|N/m\^\{2\}|N/m²)(?![a-zA-Z0-9])', r'\g<1>\\text{ N/m}^2', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:N/m\^3|N/m\^\{3\}|N/m³)(?![a-zA-Z0-9])', r'\g<1>\\text{ N/m}^3', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*N(?:\s*\\cdot\s*|\s*·\s*|\.)m\b', r'\g<1>\\text{ N}\\cdot\\text{m}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:kPa\b)', r'\g<1>\\text{ kPa}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:MPa\b)', r'\g<1>\\text{ MPa}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:m\^2|m\^\{2\}|m²)(?![a-zA-Z0-9])', r'\g<1>\\text{ m}^2', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:m\^3|m\^\{3\}|m³)(?![a-zA-Z0-9])', r'\g<1>\\text{ m}^3', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:cm\^2|cm\^\{2\}|cm²)(?![a-zA-Z0-9])', r'\g<1>\\text{ cm}^2', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:cm\^3|cm\^\{3\}|cm³)(?![a-zA-Z0-9])', r'\g<1>\\text{ cm}^3', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:cm\b)', r'\g<1>\\text{ cm}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:mm\b)', r'\g<1>\\text{ mm}', s)
    s = re.sub(r'(\d+(?:\.\d+)?|\})\s*(?:m\b)', r'\g<1>\\text{ m}', s)

    # 7. Math & Trig Functions
    s = re.sub(r'(?<!\\)\b(sin|cos|tan|cot|sec|cosec|log|ln|arctan|arcsin|arccos)\b', lambda m: chr(92) + m.group(1) + ' ', s)

    # 8. Fractions: [A] / [B] or (A) / (B)
    s = re.sub(r'\[\s*(.*?)\s*\]\s*/\s*\[\s*(.*?)\s*\]', lambda m: r'\frac{' + m.group(1) + '}{' + m.group(2) + '}', s)
    s = re.sub(r'\(\s*([^\(\)]+?)\s*\)\s*/\s*\(\s*([^\(\)]+?)\s*\)', lambda m: r'\frac{' + m.group(1) + '}{' + m.group(2) + '}', s)

    # Clean multi-spaces
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return s

def transform_code_block(match):
    code_content = match.group(1)
    latex = html_to_katex(code_content)
    if '=' in code_content or len(code_content) > 18:
        return f'<div class="sol-math-block">$${latex}$$</div>'
    else:
        return f'<span class="sol-math-inline">${latex}$</span>'

def enhance_solution_math(html):
    if not html:
        return ""
    res = re.sub(r'<code>(.*?)</code>', transform_code_block, html, flags=re.DOTALL)
    res = re.sub(r'<span class="formula-chip(?:-sm)?">(.*?)</span>', lambda m: f'<span class="sol-math-inline">${html_to_katex(m.group(1))}$</span>', res, flags=re.DOTALL)
    return res

def enhance_html(html_str):
    import re
    formulas_json = json.dumps(master_formulas).replace("</script>", "<\\/script>")
    formulas_js = formulas_js_template.replace("__MASTER_FORMULAS_JSON__", formulas_json)

    # Pre-render initial cards into view_formulas_html
    view_html_ready = view_formulas_html.replace(
        '<!-- Rendered dynamically by JavaScript -->', build_initial_cards_html(), 1
    )

    out = html_str

    # 1. KaTeX scripts & CSS into <head>
    katex_head = """    <!-- KaTeX Mathematical Typography Engine (CDN with offline local fallback) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" onerror="this.onerror=null;this.href='vendor/katex/katex.min.css'">
    <link rel="stylesheet" href="vendor/katex/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" onerror="this.onerror=null;this.src='vendor/katex/katex.min.js'"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" onerror="this.onerror=null;this.src='vendor/katex/auto-render.min.js'"></script>
    <script defer src="vendor/katex/katex.min.js"></script>
    <script defer src="vendor/katex/auto-render.min.js"></script>
</head>"""
    out = out.replace("</head>", katex_head, 1)

    # 2. Formula Showcase CSS
    out = out.replace("</style>", formulas_css + "\n    </style>", 1)

    # 3. Replace Syllabus formula chips (Key Governing Formulas column)
    patterns_replacements = [
        (r'<td>\s*<span class="formula-chip">K<sub>a</sub> = \(1-sin&phi;\)/\(1\+sin&phi;\)</span>.*?</td>', f'<td>{u1_formulas_html}</td>'),
        (r'<td>\s*<span class="formula-chip">&sigma;\'₁ = &sigma;\'₃ N<sub>&phi;</sub>.*?</td>', f'<td>{u2_formulas_html}</td>'),
        (r'<td>\s*<span class="formula-chip">q<sub>ult</sub> = c N<sub>c</sub>.*?</td>', f'<td>{u3_formulas_html}</td>'),
        (r'<td>\s*<span class="formula-chip">Q<sub>ug</sub> = 9 c<sub>u</sub> B&sup2;.*?</td>', f'<td>{u4_formulas_html}</td>'),
        (r'<td>\s*<span class="formula-chip">N\' = N &middot; 350.*?</td>', f'<td>{u5_formulas_html}</td>'),
    ]
    for pattern, repl in patterns_replacements:
        out = re.sub(pattern, lambda m, r=repl: r, out, count=1, flags=re.DOTALL)

    # 3b. Replace remaining formula-chip-sm in Syllabus High-Yield column with KaTeX inline math
    syllabus_inline_reps = [
        (r'<span class="formula-chip-sm">z<sub>c</sub> = 2c / &gamma;&radic;K<sub>a</sub></span>', r'<span class="sol-math-inline">$z_c = \frac{2c}{\gamma\sqrt{K_a}}$</span>'),
        (r'<span class="formula-chip-sm">A = A<sub>0</sub> / \(1-&epsilon;\)</span>', r'<span class="sol-math-inline">$A = \frac{A_0}{1-\varepsilon}$</span>'),
        (r'<span class="formula-chip-sm">c, &phi;</span>', r'<span class="sol-math-inline">$c\', \phi\'$</span>'),
        (r'<span class="formula-chip-sm">Q = Am \+ Pn</span>', r'<span class="sol-math-inline">$Q = Am + Pn$</span>'),
        (r'<span class="formula-chip-sm">s = d \+ 2d/&pi;&alpha;</span>', r'<span class="sol-math-inline">$s = d + \frac{2d}{\pi\alpha}$</span>'),
        (r'<span class="formula-chip-sm">A<sub>r</sub> &le; 10%</span>', r'<span class="sol-math-inline">$A_r \le 10\%$</span>'),
        (r'<span class="formula-chip-sm">C<sub>i</sub></span>', r'<span class="sol-math-inline">$C_i$</span>'),
        (r'<span class="formula-chip-sm">C<sub>o</sub></span>', r'<span class="sol-math-inline">$C_o$</span>'),
    ]
    for pat, rep_str in syllabus_inline_reps:
        out = re.sub(pat, lambda m, r=rep_str: r, out)

    # 4. Replace view-formulas
    old_formulas_view_regex = r'<div class="app-page-view" id="view-formulas">.*?\s*</div>\s*</div>(?=\s*\n\s*(?:<!-- =+\s*\n\s*PAGE VIEW: NOTES|<div class="app-page-view" id="view-notes"|<!-- Embedded High-Performance Data Arrays))'
    out = re.sub(old_formulas_view_regex, lambda m, r=view_html_ready: r, out, count=1, flags=re.DOTALL)

    # 5. Insert formulas_js before </body>
    out = out.replace("</body>", formulas_js + "\n</body>", 1)

    return out

