# scratch/generate_all_theory_solutions.py
"""
Generates balanced, intuitive, easy-to-understand solutions for all 41 Theory questions,
3 Derivations, and 1 Practical question in Geotechnical Engineering PYQ platform.
Calibrated strictly according to user's exemplar: clear, crisp, high-scoring, zero fluff.
"""

import sys
sys.path.append('scratch')
from theory_svgs import (
    SVG_MODES_OF_SHEAR_FAILURE,
    SVG_LOAD_SETTLEMENT_CURVES,
    SVG_OPEN_CAISSON,
    SVG_STRAP_FOOTING,
    SVG_REBHANN_CONSTRUCTION,
    SVG_SPT_APPARATUS,
    SVG_BORELOG
)

SOLUTIONS = {}

# =============================================================================
# UNIT 1: LATERAL EARTH PRESSURE & RETAINING WALLS
# =============================================================================

SOLUTIONS["2024-Q1a"] = """<strong>Three Types of Earth Pressure with Examples:</strong><br>
1. <strong>Active Earth Pressure:</strong> Pressure exerted by soil when the retaining wall moves slightly away from the backfill. Soil expands and relaxes, so lateral pressure drops to a minimum.<br>
<em>Example:</em> A retaining wall tilting away from soil.<br>
2. <strong>Passive Earth Pressure:</strong> Resistance offered by soil when the retaining wall moves towards or is pushed into the backfill. Soil compresses, mobilizing maximum resistance.<br>
<em>Example:</em> Soil resisting the movement of a sheet pile wall or anchor deadman block.<br>
3. <strong>Earth Pressure at Rest:</strong> Pressure exerted by soil when the retaining wall does not move at all (zero movement). Soil remains in its natural undisturbed state.<br>
<em>Example:</em> Basement walls restrained by rigid floor slabs or bridge abutments resting on rock.<br>
<code>P_a < P_0 < P_p \\qquad (K_a < K_0 < K_p)</code>"""

SOLUTIONS["2024-Q1b"] = """<strong>Assumptions of Coulomb's Earth Pressure Theory (1776):</strong><br>
1. Soil is homogeneous, isotropic, dry, and cohesionless (c = 0, possessing only friction angle φ).<br>
2. Backfill surface is a plane (horizontal or inclined).<br>
3. Failure surface is a plane passing through the heel of the wall.<br>
4. Wall back is straight, rigid, and inclined at angle α.<br>
5. Friction develops between the wall and soil (wall friction angle δ).<br>
6. Failing soil wedge behaves as a rigid body and moves as a single unit."""

SOLUTIONS["2024-Q1c"] = """<strong>Derive Expression for Earth Pressure at Rest (3 Marks):</strong><br>
At-rest earth pressure occurs when the retaining wall does not move (zero lateral strain: ε<sub>x</sub> = ε<sub>y</sub> = 0).<br>
1. <strong>Vertical Stress at Depth z:</strong><br>
<code>\\sigma_v = \\gamma z</code><br>
2. <strong>Horizontal Lateral Stress:</strong><br>
<code>\\sigma_h = K_0 \\sigma_v = K_0 \\gamma z</code><br>
3. <strong>Elastic Theory Derivation:</strong> From 3D Hooke's Law with zero lateral strain:<br>
<code>\\varepsilon_x = \\frac{1}{E}[\\sigma_h - \\mu(\\sigma_h + \\sigma_v)] = 0 \\implies K_0 = \\frac{\\sigma_h}{\\sigma_v} = \\frac{\\mu}{1 - \\mu}</code><br>
4. <strong>Using Jaky's Equation (Normally Consolidated Soil):</strong><br>
<code>K_0 = 1 - \\sin\\phi \\implies \\sigma_h = (1 - \\sin\\phi) \\gamma z</code><br>
5. <strong>Total Earth Thrust (P<sub>0</sub>) at Wall Height H:</strong><br>
<code>P_0 = \\frac{1}{2} K_0 \\gamma H^2 = \\frac{1}{2} (1 - \\sin\\phi) \\gamma H^2</code><br>
Point of application acts at H/3 above the base."""

SOLUTIONS["2023-Q1a"] = """<strong>Types of Earth Pressure and Classical Theories:</strong><br>
1. <strong>Three Types of Earth Pressure:</strong><br>
• <strong>Active Pressure (P<sub>a</sub>):</strong> Wall moves away from soil; pressure drops to minimum.<br>
• <strong>Passive Pressure (P<sub>p</sub>):</strong> Wall is pushed into soil; pressure reaches maximum.<br>
• <strong>At-Rest Pressure (P<sub>0</sub>):</strong> Wall undergoes zero movement.<br>
<code>P_a < P_0 < P_p</code><br>
2. <strong>Two Classical Theories:</strong><br>
• <strong>Rankine's Theory (1857):</strong> Considers plastic equilibrium of a semi-infinite soil mass. Assumes vertical, smooth (frictionless) wall back (δ = 0).<br>
• <strong>Coulomb's Theory (1776):</strong> Considers equilibrium of a sliding rigid wedge. Accounts for wall friction (δ &gt; 0) and inclined wall back."""

SOLUTIONS["2023-Q1c"] = """<strong>Condition of Maximum Active Earth Pressure (Sliding Wedge Method):</strong><br>
1. <strong>Forces Acting on Trial Soil Wedge:</strong><br>
• Weight of wedge (W) acting vertically downwards.<br>
• Soil reaction (R) on the slip plane, inclined at angle φ to the normal.<br>
• Active earth thrust (P<sub>a</sub>) on wall, inclined at wall friction angle δ to the normal.<br>
2. <strong>Force Equilibrium (Sine Rule):</strong> From the force triangle of the sliding wedge:<br>
<code>P_a = W \\cdot \\frac{\\sin(\\theta - \\phi)}{\\sin(\\theta - \\phi + \\alpha + \\delta)}</code><br>
Where θ is the inclination of the trial failure plane.<br>
3. <strong>Condition for Critical Failure Plane:</strong> The actual failure plane exerts the maximum possible thrust on the wall. Differentiating P<sub>a</sub> with respect to θ and setting to zero:<br>
<code>\\frac{dP_a}{d\\theta} = 0</code><br>
4. <strong>Result:</strong> For a vertical smooth wall (α = 90°, δ = 0) and level backfill, solving dP<sub>a</sub>/dθ = 0 gives:<br>
<code>\\theta_{cr} = 45^\\circ + \\frac{\\phi}{2} \\qquad P_a = \\frac{1}{2} \\gamma H^2 \\left(\\frac{1 - \\sin\\phi}{1 + \\sin\\phi}\\right)</code>"""

SOLUTIONS["2023-Q1c-OR"] = """<strong>Rebhann's Graphical Construction for Active Earth Thrust:</strong><br>
1. <strong>Principle:</strong> A graphical method based on Poncelet's solution to find the critical failure plane and total Coulomb active thrust (P<sub>a</sub>) directly without trial-and-error.<br>
2. <strong>Step-by-Step Construction Procedure:</strong><br>
• <strong>Step 1:</strong> Draw wall face AB and ground line AD.<br>
• <strong>Step 2:</strong> From heel B, draw φ-line BD at angle φ to horizontal, cutting ground at D.<br>
• <strong>Step 3:</strong> Draw ψ-line BL at angle ψ = β - δ to the φ-line.<br>
• <strong>Step 4:</strong> Draw a semi-circle with line BD as diameter.<br>
• <strong>Step 5:</strong> From crest A, draw line AE parallel to ψ-line, intersecting BD at E.<br>
• <strong>Step 6:</strong> At E, erect perpendicular EF cutting the semi-circle at F.<br>
• <strong>Step 7:</strong> With center B and radius BF, swing an arc to cut line BD at point C.<br>
• <strong>Step 8:</strong> Draw line CD parallel to ψ-line to cut ground line at D. Line BC is the <strong>critical failure plane</strong>!<br>
3. <strong>Graphical Construction Diagram:</strong><br>
__SVG_REBHANN_CONSTRUCTION__<br>
4. <strong>Total Active Earth Thrust:</strong><br>
<code>P_a = \\gamma \\cdot \\text{Area}(\\triangle BCD) = \\frac{1}{2} \\gamma \\cdot (CD) \\cdot h'</code><br>
Acting at H/3 above the base inclined at angle δ to the wall normal."""

SOLUTIONS["2022-Q1c"] = """<strong>Assumptions Made in Rankine's Earth Pressure Theory:</strong><br>
1. Soil is homogeneous, isotropic, dry, and cohesionless (c = 0).<br>
2. Ground surface is a plane (horizontal or uniformly sloping).<br>
3. Back of the retaining wall is smooth and vertical (zero wall friction, δ = 0).<br>
4. Soil is in a state of plastic equilibrium throughout the failure mass.<br>
5. Rupture surfaces are straight planes inclined at:<br>
<code>\\theta = 45^\\circ + \\frac{\\phi}{2} \\; \\text{(Active)} \\qquad \\theta = 45^\\circ - \\frac{\\phi}{2} \\; \\text{(Passive)}</code>"""

SOLUTIONS["2022-Q1e-OR"] = """<strong>Rebhann's Graphical Construction &amp; Advantages:</strong><br>
1. <strong>Objective:</strong> Graphically determines Coulomb active thrust (P<sub>a</sub>) and identifies the critical failure plane for retaining walls with wall friction (δ) and surcharge (β).<br>
2. <strong>Construction Steps:</strong><br>
• Draw wall AB and ground surface AD.<br>
• Draw φ-line BD at angle φ to horizontal from heel B.<br>
• Draw ψ-line BL at angle ψ = β - δ to line BD.<br>
• Draw semi-circle on BD as diameter.<br>
• Draw AE parallel to ψ-line, meeting BD at E.<br>
• Erect perpendicular EF to meet semi-circle at F.<br>
• With center B and radius BF, draw arc to cut BD at C.<br>
• Draw CD parallel to ψ-line to meet ground at D. Line BC is the failure plane.<br>
3. <strong>Rebhann's Diagram:</strong><br>
__SVG_REBHANN_CONSTRUCTION__<br>
4. <strong>Active Thrust:</strong><br>
<code>P_a = \\gamma \\cdot \\text{Area}(\\triangle BCD)</code><br>
5. <strong>Advantages:</strong><br>
• Avoids tedious trigonometric equations.<br>
• Easily handles broken or irregular backfill slopes.<br>
• Directly identifies critical failure plane BC without trial wedges."""

# =============================================================================
# UNIT 2: SHEAR STRENGTH & SLOPE STABILITY
# =============================================================================

SOLUTIONS["2024-Q2a"] = """<strong>Factors Affecting Factor of Safety of Infinite Slope in Clay:</strong><br>
1. <strong>Slope Angle (β):</strong> Steeper slope increases gravitational sliding stress, directly reducing FOS.<br>
2. <strong>Soil Cohesion (c'):</strong> Primary resisting force in clay; higher cohesion directly increases FOS.<br>
3. <strong>Depth of Slip Plane (H):</strong> In clay, safety decreases with depth because driving weight grows faster than cohesive strength.<br>
4. <strong>Groundwater Seepage:</strong> Water seepage creates pore pressure and reduces effective stress, reducing slope safety by up to 50%.<br>
<code>FOS = \\frac{c'}{\\gamma z \\sin\\beta \\cos\\beta} + \\frac{\\tan\\phi'}{\\tan\\beta}</code>"""

SOLUTIONS["2024-Q2b"] = """<strong>Three Types of Shear Failure in Soil:</strong><br>
1. <strong>General Shear Failure:</strong> Occurs in dense sand and stiff clay. Continuous failure surface reaches ground surface with clear ground heaving/bulging on both sides. Sudden failure with distinct peak load.<br>
2. <strong>Local Shear Failure:</strong> Occurs in medium dense sand and medium clay. Failure surfaces stop inside the soil mass. Slight surface bulging with gradual settlement.<br>
3. <strong>Punching Shear Failure:</strong> Occurs in loose sand and soft clay. Footing sinks vertically straight down by perimeter shear. Zero surface bulging with continuous plunging settlement.<br>
__SVG_MODES_OF_SHEAR_FAILURE__"""

SOLUTIONS["2024-Q2c"] = """<strong>Classification of Shear Tests by Drainage Condition:</strong><br>
<span class="is-code-chip">IS: 2720</span><br>
1. <strong>Unconsolidated Undrained (UU / Quick Test):</strong> Drainage valve is kept closed during both cell pressure application and shearing. Water cannot escape. Test is fast (5-10 min) and measures undrained strength (c<sub>u</sub>).<br>
<em>Example:</em> Foundation safety right after fast construction on saturated clay.<br>
2. <strong>Consolidated Undrained (CU Test):</strong> Drainage is allowed during cell pressure (complete consolidation), then the valve is closed during shearing while measuring pore pressure (u). Measures both total and effective parameters.<br>
<em>Example:</em> Sudden reservoir water level drawdown behind an earth dam.<br>
3. <strong>Consolidated Drained (CD / Slow Test):</strong> Drainage is allowed throughout both stages. Shearing is very slow so no excess pore pressure builds up. Measures long-term drained parameters (c', φ').<br>
<em>Example:</em> Long-term permanent stability of clay slopes after many years."""

SOLUTIONS["2024-Q2d"] = """<strong>Methods for Improving Stability of Slopes:</strong><br>
1. <strong>Slope Reshaping (Geometric Method):</strong> Flattening the slope angle, adding horizontal berms/benches, and removing weight from the top (crest) while loading the toe.<br>
2. <strong>Drainage Control (Most Effective):</strong> Providing surface ditches to catch rainwater, and deep horizontal perforated drains to lower the groundwater table and eliminate seepage forces.<br>
3. <strong>Retaining Structures:</strong> Building RCC retaining walls, gabions, or sheet piles at the toe to physically stop sliding.<br>
4. <strong>Soil Nailing &amp; Reinforcement:</strong> Inserting steel rods (soil nails) with shotcrete facing, or placing geogrids in compacted fill slopes.<br>
5. <strong>Bio-Engineering:</strong> Planting deep-rooted grass (vetiver) to bind surface soil and prevent rain erosion."""

SOLUTIONS["2023-Q2bi"] = """<strong>Three Modes of Shear Failure &amp; Load-Settlement Behavior:</strong><br>
1. <strong>General Shear Failure:</strong> Dense sand (D<sub>r</sub> &gt; 70%) and stiff clay. Rupture surface extends to ground with surface heave. Curve has a <strong>sharp peak failure load (q<sub>u</sub>)</strong> followed by sudden drop.<br>
2. <strong>Local Shear Failure:</strong> Medium sand (35% &lt; D<sub>r</sub> &lt; 70%). Rupture surface stops within soil mass; slight heave. Curve has <strong>no sharp peak</strong>, showing gradual yield.<br>
3. <strong>Punching Shear Failure:</strong> Loose sand (D<sub>r</sub> &lt; 35%) and soft clay. Footing punches straight down; zero heave. Curve <strong>plunges downward continuously</strong>.<br>
__SVG_LOAD_SETTLEMENT_CURVES__<br>
__SVG_MODES_OF_SHEAR_FAILURE__"""

SOLUTIONS["2023-Q3a"] = """<strong>Coulomb's Law of Shear Strength of Soil:</strong><br>
1. <strong>Historical Total Stress Equation (1776):</strong> Shear strength consists of cohesion and internal friction:<br>
<code>\\tau = c + \\sigma \\tan\\phi</code><br>
Where c = cohesion, σ = normal stress, φ = friction angle.<br>
2. <strong>Terzaghi's Effective Stress Equation (1925):</strong> Shear strength depends strictly on effective stress between soil grains:<br>
<code>\\tau_f = c' + \\sigma' \\tan\\phi' = c' + (\\sigma - u) \\tan\\phi'</code><br>
Where c' = effective cohesion, σ' = effective stress, u = pore water pressure, φ' = effective friction angle."""

SOLUTIONS["2023-Q3biii"] = """<strong>Kinds of Triaxial Tests &amp; Suitability for Saturated Clay:</strong><br>
<span class="is-code-chip">IS: 2720</span><br>
1. <strong>UU Test:</strong> No drainage allowed. Fast test (5-10 min). Gives undrained strength c<sub>u</sub>.<br>
2. <strong>CU Test:</strong> Consolidation allowed, then sheared undrained while measuring pore pressure u.<br>
3. <strong>CD Test:</strong> Drainage allowed in both stages. Very slow test (days to weeks).<br>
4. <strong>Best Test for Saturated Clay:</strong><br>
• <strong>Consolidated Undrained (CU) Test with pore pressure measurement.</strong><br>
• <strong>Reason:</strong> Saturated clay has low permeability, so a drained CD test takes weeks. The CU test allows consolidation, then shears quickly while measuring pore pressure u, giving <strong>both total and effective parameters (c', φ')</strong> in just one day."""

SOLUTIONS["2023-Q3c"] = """<strong>Relationship Between Effective Shear Parameters &amp; Principal Stresses:</strong><br>
1. <strong>Mohr Circle Geometry at Failure:</strong><br>
• Center: C = ((σ'<sub>1</sub> + σ'<sub>3</sub>) / 2, 0)<br>
• Radius: R = (σ'<sub>1</sub> - σ'<sub>3</sub>) / 2<br>
2. <strong>Right Triangle Relationship:</strong> In the right triangle formed by radius R and failure envelope inclined at φ' with intercept c':<br>
<code>\\sin\\phi' = \\frac{\\text{Radius}}{\\text{Hypotenuse}} = \\frac{\\frac{\\sigma'_1 - \\sigma'_3}{2}}{\\frac{c'}{\\tan\\phi'} + \\frac{\\sigma'_1 + \\sigma'_3}{2}}</code><br>
3. <strong>Simplifying:</strong> Multiplying terms and grouping σ'<sub>1</sub> and σ'<sub>3</sub>:<br>
<code>\\sigma'_1(1 - \\sin\\phi') = \\sigma'_3(1 + \\sin\\phi') + 2c'\\cos\\phi'</code><br>
4. <strong>Final Equation:</strong> Dividing by (1 - sinφ'):<br>
<code>\\sigma'_1 = \\sigma'_3 \\tan^2\\left(45^\\circ + \\frac{\\phi'}{2}\\right) + 2c'\\tan\\left(45^\\circ + \\frac{\\phi'}{2}\\right)</code>"""

SOLUTIONS["2022-Q2a"] = """<strong>Differences Between Direct Shear Box Test and Triaxial Shear Test:</strong><br>
<div class="sol-table-wrap">
<table class="sol-table">
<thead>
<tr>
<th>Feature</th>
<th>Direct Shear Test (IS: 2720 Pt 13)</th>
<th>Triaxial Shear Test (IS: 2720 Pt 12)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Failure Plane</strong></td>
<td>Forced along fixed horizontal plane.</td>
<td>Fails along natural weakest plane (45° + φ/2).</td>
</tr>
<tr>
<td><strong>2. Drainage Control</strong></td>
<td>Poor drainage control; cannot measure pore pressure.</td>
<td>Complete drainage control; measures pore pressure u accurately.</td>
</tr>
<tr>
<td><strong>3. Stress Distribution</strong></td>
<td>Non-uniform with stress concentrations at edges.</td>
<td>Uniform 3D stress throughout cylindrical sample.</td>
</tr>
<tr>
<td><strong>4. Best Suited For</strong></td>
<td>Clean sands and gravels.</td>
<td>All soils (clays, silts, sands) under UU, CU, and CD.</td>
</tr>
</tbody>
</table>
</div>"""

SOLUTIONS["2022-Q2b"] = """<strong>Comparison of UU and CD Shear Tests:</strong><br>
1. <strong>Unconsolidated Undrained (UU) Test:</strong><br>
• Drainage valve closed during both confining pressure and shearing.<br>
• Very fast test (5 to 10 minutes); excess pore pressure does not escape.<br>
• Measures undrained shear strength (c<sub>u</sub>).<br>
<em>Example:</em> Foundation stability right after rapid construction on clay.<br>
2. <strong>Consolidated Drained (CD) Test:</strong><br>
• Drainage valve open during both stages.<br>
• Very slow test (days to weeks); zero excess pore pressure builds up.<br>
• Measures drained effective strength parameters (c', φ').<br>
<em>Example:</em> Long-term permanent slope stability after decades."""

# =============================================================================
# UNIT 3: SHALLOW FOUNDATIONS
# =============================================================================

SOLUTIONS["2024-Q3a"] = """<strong>Major Design Criteria for Foundations:</strong><br>
<span class="is-code-chip">IS: 1904 &amp; IS: 6403</span><br>
1. <strong>Safety Against Shear Failure:</strong> Applied foundation pressure must not exceed safe bearing capacity, maintaining a factor of safety FOS ≥ 2.5 to 3.0.<br>
2. <strong>Settlement Limits:</strong> Total and differential settlements must stay within safe limits (IS: 1904: max 40 mm in sand, 65 mm in clay; angular distortion ≤ 1/500) to avoid building damage.<br>
3. <strong>Adequate Depth:</strong> Foundation must be placed below topsoil, frost line, and seasonal moisture swelling zone (minimum depth 0.5 m to 1.0 m)."""

SOLUTIONS["2024-Q3b"] = """<strong>Settlement of Foundation (IS: 1904):</strong><br>
Total settlement consists of three parts:<br>
<code>S_{total} = S_i + S_c + S_s</code><br>
1. <strong>Immediate Settlement (S<sub>i</sub>):</strong> Elastic deformation occurring instantly upon loading without volume change.<br>
2. <strong>Consolidation Settlement (S<sub>c</sub>):</strong> Time-dependent settlement in saturated clay as pore water squeezes out under load.<br>
3. <strong>Secondary Settlement (S<sub>s</sub>):</strong> Very slow plastic realignment of clay particles after excess pore pressure is gone.<br>
Permissible total settlement: 40 mm in sand, 65 mm in clay."""

SOLUTIONS["2024-Q3c"] = """<strong>Failures in Shallow Foundations:</strong><br>
1. <strong>Soil Shear Failure:</strong> General shear (sudden tilting), local shear (gradual sinking), or punching shear (vertical plunge).<br>
2. <strong>Settlement Failure:</strong> Excessive total settlement damages connected pipes; unequal differential settlement causes wall cracks, building tilt, and jammed doors.<br>
3. <strong>Structural Footing Failure:</strong> Footing concrete slab cracks due to excessive upward bending or column punching through the slab."""

SOLUTIONS["2023-Q2a"] = """<strong>Bearing Capacity Definitions &amp; Common Suffixes:</strong><br>
<strong>Bearing Capacity:</strong> Load-carrying ability of soil per unit area without shear failure or excessive settlement.<br>
1. <strong>Ultimate (q<sub>ult</sub>):</strong> Minimum gross contact pressure causing soil shear failure.<br>
2. <strong>Net Ultimate (q<sub>net_ult</sub>):</strong> Failure pressure minus overburden pressure (q<sub>ult</sub> - γD<sub>f</sub>).<br>
3. <strong>Safe (q<sub>safe</sub>):</strong> Safe gross pressure including factor of safety: q<sub>net_ult</sub> / FOS + γD<sub>f</sub> (FOS = 2.5 to 3.0).<br>
4. <strong>Allowable Bearing Pressure (q<sub>a</sub>):</strong> Design pressure satisfying <strong>both</strong> shear safety (FOS ≥ 2.5) and permissible settlement limits."""

SOLUTIONS["2023-Q2bii"] = """<strong>Effect of Water Table on Bearing Capacity (IS: 6403):</strong><br>
General equation with correction factors:<br>
<code>q_u = c N_c + \\gamma_1 D_f N_q W^*_1 + 0.5 \\gamma_2 B N_\\gamma W^*_2</code><br>
1. <strong>Case 1 (Water Table at Ground Level):</strong> Entire soil is submerged (γ' ≈ 0.5 γ<sub>sat</sub>). Bearing capacity drops by approximately <strong>50%</strong>.<br>
2. <strong>Case 2 (Water Table Between Ground &amp; Footing Base):</strong> Surcharge term uses weighted unit weight: W*<sub>1</sub> = 0.5 [1 + d<sub>w</sub> / D<sub>f</sub>].<br>
3. <strong>Case 3 (Water Table Below Base within Depth B):</strong> Shear zone is partially submerged: W*<sub>2</sub> = 0.5 [1 + z<sub>w</sub> / B].<br>
4. <strong>Case 4 (Water Table at Depth ≥ D<sub>f</sub> + B):</strong> Water table is below the failure zone; <strong>zero reduction</strong> in bearing capacity."""

SOLUTIONS["2023-Q4a"] = """<strong>Types of Shallow Foundations &amp; Strap Footing:</strong><br>
1. <strong>Types:</strong> Isolated pad footing, Strip/wall footing, Combined footing, Strap footing, Raft (mat) foundation.<br>
2. <strong>Strap Footing:</strong> Used when an exterior column sits on a property line where footing cannot extend outside. A rigid RCC strap beam connects the eccentric exterior footing to an adjacent interior footing.<br>
3. <strong>Key Rule:</strong> The strap beam is suspended above ground (no contact with soil underneath) so it only transfers bending moment and shear.<br>
__SVG_STRAP_FOOTING__"""

SOLUTIONS["2023-Q4bi"] = """<strong>Requirements of Satisfactory Foundations (IS: 1904):</strong><br>
1. <strong>Adequate Depth:</strong> Founded below topsoil, scour level, and seasonal moisture swelling/shrinkage zone.<br>
2. <strong>Safety Against Shear:</strong> Applied bearing pressure must not exceed safe bearing capacity (FOS ≥ 2.5 to 3.0).<br>
3. <strong>Safe Settlement:</strong> Total settlement ≤ 40 mm in sand, 65 mm in clay; differential angular distortion ≤ 1/500 to prevent wall cracks.<br>
4. <strong>Durability:</strong> Concrete and steel must resist groundwater chemical attack (sulfates per IS: 456)."""

SOLUTIONS["2023-Q4bii"] = """<strong>Foundation Recommendations for Two Site Conditions:</strong><br>
1. <strong>Site 1: Loose Sand with High Ground Water Table:</strong><br>
• <strong>Recommendation:</strong> <strong>Raft (Mat) Foundation</strong> or <strong>Piles</strong>.<br>
• <strong>Reason:</strong> Loose sand has low strength and high settlement; water table cuts bearing capacity by 50% and causes liquefaction risk. A rigid raft bridges weak spots, or piles transfer loads to deep dense strata.<br>
2. <strong>Site 2: Stiff Clay:</strong><br>
• <strong>Recommendation:</strong> <strong>Isolated Spread Footings</strong>.<br>
• <strong>Reason:</strong> Stiff clay has high shear strength and low settlement. Isolated footings founded at 1.5 m to 2 m depth are safe, simple, and most economical."""

SOLUTIONS["2022-Q3a"] = """<strong>Assumptions Made in Terzaghi's Bearing Capacity Theory:</strong><br>
1. Footing is a continuous strip with infinite length (L/B → ∞).<br>
2. Shallow foundation: Depth D<sub>f</sub> ≤ Width B.<br>
3. Base of footing is rough and rigid (no slipping at base).<br>
4. Soil above base level is replaced by equivalent surcharge q = γD<sub>f</sub> (its shear strength is neglected).<br>
5. General shear failure occurs in soil.<br>
6. Soil is homogeneous, isotropic, and obeys Mohr-Coulomb law (τ = c + σ tanφ)."""

SOLUTIONS["2022-Q3b"] = """<strong>Factors Affecting Bearing Capacity of a Shallow Footing:</strong><br>
1. <strong>Soil Strength (c and φ):</strong> Higher cohesion and friction angle exponentially increase bearing capacity.<br>
2. <strong>Footing Width (B):</strong> In sand, wider footings provide higher bearing capacity (0.5 γ B N<sub>γ</sub>).<br>
3. <strong>Depth of Embedment (D<sub>f</sub>):</strong> Deeper footing has higher confining surcharge (γ D<sub>f</sub> N<sub>q</sub>).<br>
4. <strong>Water Table:</strong> Rising water table submerges soil, reducing bearing capacity by up to 50%.<br>
5. <strong>Footing Shape:</strong> Circular and square footings have higher capacities than strip footings."""

SOLUTIONS["2022-Q3c"] = """<strong>Ground Water Table Effect on Safe Bearing Capacity:</strong><br>
<span class="is-code-chip">IS: 6403</span><br>
<code>q_{ult} = c N_c + \\gamma_1 D_f N_q W^*_1 + 0.5 \\gamma_2 B N_\\gamma W^*_2</code><br>
1. <strong>Surcharge Correction Factor (W*<sub>1</sub>):</strong> W*<sub>1</sub> = 0.5 [1 + d<sub>w</sub> / D<sub>f</sub>] for water table between ground level and footing base.<br>
2. <strong>Wedge Correction Factor (W*<sub>2</sub>):</strong> W*<sub>2</sub> = 0.5 [1 + z<sub>w</sub> / B] for water table within depth B below footing base.<br>
3. <strong>Maximum Reduction:</strong> When water table rises to ground level, effective unit weight is halved (γ' ≈ 0.5 γ<sub>sat</sub>), cutting bearing capacity of sand by <strong>50%</strong>."""

# =============================================================================
# UNIT 4: DEEP FOUNDATIONS (PILES & CAISSONS)
# =============================================================================

SOLUTIONS["2024-Q4a"] = """<strong>Group Action of Piles (IS: 2911):</strong><br>
1. <strong>Group Action:</strong> Piles are installed in clusters connected by a rigid pile cap. Due to overlapping stress zones, group capacity is not always equal to single pile capacity × n.<br>
2. <strong>Failure Modes in Clay:</strong> Piles can fail individually (Q = n · Q<sub>u</sub>) or as one large solid block (Q<sub>block</sub>). Actual capacity is the <strong>smaller</strong> of the two.<br>
3. <strong>Group Efficiency (η<sub>g</sub>):</strong> η<sub>g</sub> = Q<sub>group</sub> / (n · Q<sub>single</sub>) × 100%. In sands η<sub>g</sub> &gt; 100% due to soil compaction; in clays η<sub>g</sub> ≤ 100%.<br>
4. <strong>Standard Spacing:</strong> Center-to-center pile spacing is 2.5 d to 3.0 d for friction piles."""

SOLUTIONS["2024-Q4b"] = """<strong>Under-Reamed Pile Foundation (IS: 2911 Pt 3):</strong><br>
1. <strong>Purpose:</strong> Bored concrete piles with enlarged bulbs, specifically designed for expansive soils (Black Cotton Soil) that shrink and swell.<br>
2. <strong>Bulb Dimensions:</strong> Bulb diameter D = 2.0 to 2.5 times the stem diameter d.<br>
3. <strong>Bulb Depth:</strong> Placed at depth &gt; 1.5 m to 3.5 m, well below the active seasonal moisture zone.<br>
4. <strong>Function:</strong> Bulb anchors the pile against upward swelling forces and provides large bearing area for downward loads."""

SOLUTIONS["2024-Q4c"] = """<strong>Open Caisson (Well Foundation) Components:</strong><br>
<strong>Open Caisson:</strong> A hollow box or cylinder structure, open at top and bottom, sunk into riverbeds by dredging soil from inside, then sealed with concrete at the bottom. Used for heavy bridge piers.<br>
1. <strong>Cutting Edge:</strong> Hardened steel angle at bottom to cut soil during sinking.<br>
2. <strong>Well Curb:</strong> Concrete wedge guiding soil into the well.<br>
3. <strong>Steining:</strong> Thick wall providing sinking weight.<br>
4. <strong>Dredge Hole:</strong> Central opening for excavating soil.<br>
5. <strong>Bottom Plug:</strong> Concrete seal placed underwater at founding depth to transfer pier load.<br>
6. <strong>Sand Filling:</strong> Clean sand placed inside well for ballast and stability.<br>
7. <strong>Top Plug:</strong> Concrete slab placed over sand filling.<br>
8. <strong>Well Cap:</strong> Top RCC slab supporting the bridge pier.<br>
__SVG_OPEN_CAISSON__"""

SOLUTIONS["2022-Q4a"] = """<strong>Functions of Pile Foundation:</strong><br>
1. <strong>End-Bearing:</strong> Transfers heavy building loads through weak soft soil down to hard bedrock or dense gravel.<br>
2. <strong>Skin Friction:</strong> Distributes load through friction along the pile shaft in deep uniform clay or sand.<br>
3. <strong>Resist Uplift:</strong> Anchors transmission towers and tall chimneys against wind overturning.<br>
4. <strong>Resist Lateral Loads:</strong> Resists water wave and impact forces in bridge piers and harbour docks.<br>
5. <strong>Soil Compaction:</strong> Driven piles compact loose sand deposits, preventing earthquake liquefaction."""

SOLUTIONS["2022-Q4b"] = """<strong>Difference in Bearing Capacity of Shallow and Deep Foundations:</strong><br>
<div class="sol-table-wrap">
<table class="sol-table">
<thead>
<tr>
<th>Feature</th>
<th>Shallow Foundation (IS: 6403)</th>
<th>Deep Foundation / Piles (IS: 2911)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Load Transfer</strong></td>
<td>Base contact bearing pressure only (q<sub>u</sub>).</td>
<td>Dual components: Base end-bearing (Q<sub>b</sub>) PLUS shaft friction (Q<sub>s</sub>): Q<sub>u</sub> = Q<sub>b</sub> + Q<sub>s</sub>.</td>
</tr>
<tr>
<td><strong>2. Surcharge Effect</strong></td>
<td>Flat surface surcharge q = γD<sub>f</sub>.</td>
<td>Vertical stress increases up to critical depth (10d-20d), then stays constant.</td>
</tr>
<tr>
<td><strong>3. Clay Factor (N<sub>c</sub>)</strong></td>
<td>Terzaghi N<sub>c</sub> = 5.7 (strip footing).</td>
<td>Deep spherical cavity expansion N<sub>c</sub>* = 9.0 (Skempton).</td>
</tr>
<tr>
<td><strong>4. Failure Surface</strong></td>
<td>Failure planes burst out to ground surface with heave.</td>
<td>Localized failure confined around the pile tip and shaft.</td>
</tr>
</tbody>
</table>
</div>"""

# =============================================================================
# UNIT 5: SOIL EXPLORATION & IN-SITU TESTING
# =============================================================================

SOLUTIONS["2024-Q5a"] = """<strong>Objectives of Soil Exploration (IS: 1892):</strong><br>
1. <strong>Soil Profile:</strong> Determine the depth, thickness, and types of soil and rock layers.<br>
2. <strong>Water Table:</strong> Locate groundwater level and observe seasonal fluctuations.<br>
3. <strong>Engineering Properties:</strong> Collect samples to test shear strength (c, φ), compressibility (C<sub>c</sub>), and permeability.<br>
4. <strong>Foundation Selection:</strong> Select the safest and most economical foundation type and depth.<br>
5. <strong>Construction Safety:</strong> Anticipate excavation cave-ins, dewatering needs, and expansive clay problems."""

SOLUTIONS["2024-Q5b"] = """<strong>Typical Borelog Layout &amp; Features (IS: 1892):</strong><br>
1. <strong>Header Information:</strong> Project name, Borehole No (BH-01), ground elevation (RL), date, and drilling method.<br>
2. <strong>Key Columns:</strong> Depth range (m), standard soil hatch symbol, soil description (CLAY, SAND, ROCK), water table marker (GWT), and SPT N-values.<br>
__SVG_BORELOG__"""

SOLUTIONS["2024-Q5c"] = """<strong>Soil Sampler Criteria (IS: 1892):</strong><br>
Let D<sub>1</sub> = inside tip dia, D<sub>2</sub> = outside tip dia, D<sub>3</sub> = inside tube dia, D<sub>4</sub> = outside tube dia.<br>
1. <strong>Area Ratio (A<sub>r</sub>):</strong> Represents volume of soil displaced during driving. For undisturbed samples, A<sub>r</sub> ≤ 10% to 20%.<br>
<code>A_r = \\frac{D_2^2 - D_1^2}{D_1^2} \\times 100\\%</code><br>
2. <strong>Inside Clearance (C<sub>i</sub>):</strong> Allows sample to expand slightly inside tube, reducing wall friction and sticking (1% to 3%).<br>
<code>C_i = \\frac{D_3 - D_1}{D_1} \\times 100\\%</code><br>
3. <strong>Outside Clearance (C<sub>o</sub>):</strong> Reduces friction between soil and outside tube during driving and extraction (0% to 2%).<br>
<code>C_o = \\frac{D_2 - D_4}{D_4} \\times 100\\%</code>"""

SOLUTIONS["2024-Q5d"] = """<strong>Depth of Exploration Required for Structures (IS: 1892):</strong><br>
1. <strong>Significant Depth:</strong> Exploration must extend down to where vertical stress increase drops to <strong>10% (0.1 q)</strong> of applied contact pressure.<br>
2. <strong>Depth Guidelines:</strong><br>
• <strong>Isolated Footing:</strong> 1.5 B to 2.0 B below base.<br>
• <strong>Raft Foundation:</strong> 1.5 times the raft width (W).<br>
• <strong>Pile Foundation:</strong> 1.5 times pile group width (B<sub>g</sub>) below pile tips, or 5 m into rock.<br>
• <strong>Retaining Wall:</strong> 1.5 times wall height (H).<br>
• <strong>Earth Dam:</strong> 1.0 to 1.5 times dam height.<br>
3. <strong>Borehole Spacing:</strong> Multi-story buildings (15-30 m), Industrial plants (20-60 m), Highways (100-300 m), Dams (25-50 m)."""

SOLUTIONS["2024-Q5e-OR"] = """<strong>Standard Penetration Test (SPT) &amp; Required Corrections:</strong><br>
<span class="is-code-chip">IS: 2131</span><br>
1. <strong>Procedure:</strong> Split-spoon sampler (50.8 mm OD, 35 mm ID) driven into borehole bottom by 63.5 kg hammer falling freely from 750 mm height in 3 intervals of 150 mm. First 150 mm is seating drive (ignored). Sum of blows for last 300 mm = <strong>Observed N-value (N<sub>0</sub>)</strong>.<br>
__SVG_SPT_APPARATUS__<br>
2. <strong>Correction 1: Overburden Pressure (N'):</strong> Normalizes N for depth confining stress:<br>
<code>N' = N_0 \\times \\frac{350}{\\sigma'_v + 70} \\qquad (\\sigma'_v \\le 280\\text{ kPa})</code><br>
3. <strong>Correction 2: Dilatancy / Submergence (N''):</strong> Applied for saturated fine sand/silt below water table when N' &gt; 15:<br>
<code>N'' = 15 + 0.5 (N' - 15)</code>"""

SOLUTIONS["2023-Q5a"] = """<strong>Types of Soil Samples &amp; Obtaining Undisturbed Samples:</strong><br>
<span class="is-code-chip">IS: 1892</span><br>
1. <strong>Disturbed Samples:</strong> Soil structure is broken, but soil mineral grains are intact. Used for sieve analysis, liquid limit, plastic limit.<br>
2. <strong>Undisturbed Samples:</strong> Natural soil structure, water content, and void ratio are preserved. Required for shear strength (c, φ), consolidation (C<sub>c</sub>), and permeability.<br>
3. <strong>How to Obtain Undisturbed Samples:</strong><br>
• Use thin-walled tube sampler (Shelby tube) with area ratio A<sub>r</sub> ≤ 10%.<br>
• Push smoothly into borehole base using hydraulic jack (never hammered).<br>
• Rotate to shear the base, extract, and seal ends immediately with molten paraffin wax (min 25 mm thick) and airtight caps."""

SOLUTIONS["2023-Q5b"] = """<strong>Geotechnical Exploration — Meaning &amp; Methods:</strong><br>
<span class="is-code-chip">IS: 1892</span><br>
<strong>Meaning:</strong> Investigating subsurface soil and rock layers to design safe, economical foundations.<br>
1. <strong>Direct Methods (Test Pits):</strong> Shallow open excavations (depth 3-6 m) for direct visual inspection.<br>
2. <strong>Semi-Direct Methods (Borings):</strong><br>
• <strong>Auger Boring:</strong> Hand or power auger rotated into clays above water table.<br>
• <strong>Wash Boring:</strong> Water jet chops soil inside casing; good for sand and soft clay.<br>
• <strong>Rotary Drilling:</strong> Rotating diamond bit with drilling mud; penetrates hard rock and extracts cores.<br>
• <strong>Percussion Drilling:</strong> Heavy chisel dropped repeatedly to break hard bouldery strata.<br>
3. <strong>Indirect Methods (Geophysical):</strong> Seismic refraction (wave velocity) and electrical resistivity for rapid preliminary surveying of large sites."""

SOLUTIONS["2022-Q5a"] = """<strong>Laboratory and Field Tests in Soil Investigation:</strong><br>
<span class="is-code-chip">IS: 1892 &amp; IS: 2720</span><br>
1. <strong>Field (In-Situ) Tests:</strong><br>
• Standard Penetration Test (SPT, IS: 2131)<br>
• Cone Penetration Test (CPT, IS: 4968)<br>
• Plate Load Test (PLT, IS: 1888)<br>
• Field Vane Shear Test (IS: 4434, for soft clay)<br>
2. <strong>Laboratory Tests:</strong><br>
• Grain Size Sieve Analysis &amp; Atterberg Limits (LL, PL, PI)<br>
• Direct Shear Box Test (IS: 2720 Pt 13)<br>
• Triaxial Shear Test (UU, CU, CD per Pt 12)<br>
• 1D Oedometer Consolidation Test (IS: 2720 Pt 15)"""

SOLUTIONS["2022-Q5b"] = """<strong>Purpose of Soil Investigation (IS: 1892):</strong><br>
1. <strong>Foundation Selection:</strong> Decides whether shallow footings, raft, or deep piles are required.<br>
2. <strong>Safe Bearing Capacity:</strong> Provides measured shear parameters (c, φ) to calculate safe bearing capacity without risk of shear failure.<br>
3. <strong>Settlement Prediction:</strong> Predicts total and differential settlements, verifying they stay within safe structural limits (IS: 1904).<br>
4. <strong>Earth Pressure Design:</strong> Provides soil properties (K<sub>a</sub>, K<sub>p</sub>) to design retaining walls and basement shoring.<br>
5. <strong>Groundwater Conditions:</strong> Locates water table and identifies dewatering needs during construction."""

SOLUTIONS["2022-Q5d"] = """<strong>Standard Penetration Test (SPT) &amp; Information Obtained:</strong><br>
<span class="is-code-chip">IS: 2131</span><br>
1. <strong>Test Procedure:</strong> Split-spoon sampler (50.8 mm OD, 35 mm ID) driven into borehole bottom by 63.5 kg hammer falling 750 mm. Blows for last 300 mm = <strong>Observed N-value</strong>.<br>
__SVG_SPT_APPARATUS__<br>
2. <strong>Corrections:</strong><br>
• Overburden: N' = N<sub>0</sub> × [350 / (σ'<sub>v</sub> + 70)] for σ'<sub>v</sub> ≤ 280 kPa.<br>
• Dilatancy: N'' = 15 + 0.5 (N' - 15) for saturated fine sand/silt when N' &gt; 15.<br>
3. <strong>Information Obtained:</strong><br>
• <strong>Sand:</strong> Relative density D<sub>r</sub> (N &lt; 4 Very loose to N &gt; 50 Very dense), friction angle φ ≈ 27.1° + 0.3 N', liquefaction risk.<br>
• <strong>Clay:</strong> Unconfined compressive strength q<sub>u</sub> ≈ 12.5 N (kPa), consistency.<br>
• <strong>Design:</strong> Safe bearing capacity of footings and pile capacities."""

SOLUTIONS["2022-Q5e-OR"] = """<strong>Classification of Soil Exploration Methods &amp; Circumstances:</strong><br>
<span class="is-code-chip">IS: 1892</span><br>
<div class="sol-table-wrap">
<table class="sol-table">
<thead>
<tr>
<th>Method</th>
<th>Description</th>
<th>Best Suited Circumstances</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Open Test Pits</strong></td>
<td>Shallow manual or backhoe excavation (up to 3-5 m).</td>
<td>Shallow foundation sites; enables direct visual inspection and block sampling.</td>
</tr>
<tr>
<td><strong>2. Auger Boring</strong></td>
<td>Hand or power auger turned into ground.</td>
<td>Cohesive clays and silts above water table (up to 10-15 m depth).</td>
</tr>
<tr>
<td><strong>3. Wash Boring</strong></td>
<td>Water jet chops soil inside casing.</td>
<td>Sands and soft clays below water table; unsuitable for rock.</td>
</tr>
<tr>
<td><strong>4. Rotary Core Drilling</strong></td>
<td>Rotating diamond core barrel with drilling mud.</td>
<td>Medium to hard rock and boulders; recovers continuous rock cores (RQD).</td>
</tr>
<tr>
<td><strong>5. Percussion Drilling</strong></td>
<td>Heavy drill bit dropped repeatedly to crush soil.</td>
<td>Bouldery, stony ground and hard glacial till.</td>
</tr>
<tr>
<td><strong>6. Geophysical Methods</strong></td>
<td>Seismic refraction and electrical resistivity.</td>
<td>Rapid preliminary reconnaissance of large sites (highways, dams, pipelines).</td>
</tr>
</tbody>
</table>
</div>"""

# Post-process to inject SVGs safely
for qid in list(SOLUTIONS.keys()):
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_MODES_OF_SHEAR_FAILURE__", SVG_MODES_OF_SHEAR_FAILURE)
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_LOAD_SETTLEMENT_CURVES__", SVG_LOAD_SETTLEMENT_CURVES)
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_OPEN_CAISSON__", SVG_OPEN_CAISSON)
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_STRAP_FOOTING__", SVG_STRAP_FOOTING)
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_REBHANN_CONSTRUCTION__", SVG_REBHANN_CONSTRUCTION)
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_SPT_APPARATUS__", SVG_SPT_APPARATUS)
    SOLUTIONS[qid] = SOLUTIONS[qid].replace("__SVG_BORELOG__", SVG_BORELOG)

print(f"Total balanced theory solutions prepared: {len(SOLUTIONS)}")
