import json
import generate_dashboard

questions_2025 = [
    {
        "id": "2025-Q1a",
        "year": "2025",
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": "Q.1 (a)",
        "marks": 2,
        "type": "Theory",
        "co": "CO1",
        "bl": "BL2 (Understand)",
        "pi": "1.4.1",
        "topic": "Types & Theories of Earth Pressure",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""What are different Types of Earth Pressure and what are different theories of Earth Pressures?""",
        "solution": r"""<strong>1. Types of Earth Pressure:</strong><br>
1. <strong>Active Earth Pressure:</strong> Lateral pressure exerted by soil when the retaining wall moves away from the backfill, allowing shear resistance to mobilize towards the wall.<br>
<em>Example:</em> A cantilever retaining wall tilting outwards away from the fill.<br>
2. <strong>Passive Earth Pressure:</strong> Maximum lateral resistance exerted by soil when the retaining wall pushes into the backfill.<br>
<em>Example:</em> Soil resisting the front toe of a retaining wall or an embedded anchor block.<br>
3. <strong>Earth Pressure at Rest:</strong> Lateral pressure exerted by soil against a rigid, unyielding wall undergoing zero lateral strain (&epsilon;<sub>x</sub> = 0).<br>
<em>Example:</em> Rigid basement retaining walls or massive bridge abutments keyed into rock.<br>
<strong>2. Theories of Earth Pressure:</strong><br>
1. <strong>Rankine's Theory:</strong> Considers the stress state of plastic equilibrium in a semi-infinite, homogeneous, cohesionless soil mass behind a smooth, vertical wall.<br>
2. <strong>Coulomb's Wedge Theory:</strong> Considers the static equilibrium of a sliding wedge of soil behaving as a rigid body along a plane failure surface, accounting for wall friction (&delta;) and batter/sloping backfill."""
    },
    {
        "id": "2025-Q1bi",
        "year": "2025",
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": "Q.1 (b) i",
        "marks": 3,
        "type": "Numerical",
        "co": "CO1",
        "bl": "BL3 (Apply)",
        "pi": "2.1.2",
        "topic": "Rankine Surcharged Backfill Pressure",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A smooth vertical wall, 6 m high supports an inclined non cohesive backfill (&phi; = 32&deg;; &gamma; = 21 kN/m&sup3;) at an angle 10&deg; with horizontal. Compute the total active & passive pressure at the bottom of wall.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Wall height H = 6 m, &phi; = 32&deg;, &gamma; = 21 kN/m&sup3;, surcharge slope &beta; = 10&deg;, smooth vertical wall.<br>
1. <strong>Trigonometric Quantities:</strong><br>
<code>cos &beta; = cos 10&deg; = 0.9848, cos &phi; = cos 32&deg; = 0.8480</code><br>
<code>&radic;(cos&sup2;&beta; - cos&sup2;&phi;) = &radic;(0.9848&sup2; - 0.8480&sup2;) = &radic;(0.9698 - 0.7192) = &radic;0.2507 = 0.5007</code><br>
2. <strong>Rankine Earth Pressure Coefficients:</strong><br>
<code>K_a = cos &beta; \cdot \frac{cos &beta; - \sqrt{cos^2\beta - cos^2\phi}}{cos &beta; + \sqrt{cos^2\beta - cos^2\phi}} = 0.9848 \cdot \frac{0.9848 - 0.5007}{0.9848 + 0.5007} = \frac{0.4767}{1.4855} = <strong>0.3210</strong></code><br>
<code>K_p = cos &beta; \cdot \frac{cos &beta; + \sqrt{cos^2\beta - cos^2\phi}}{cos &beta; - \sqrt{cos^2\beta - cos^2\phi}} = 0.9848 \cdot \frac{0.9848 + 0.5007}{0.9848 - 0.5007} = \frac{1.4629}{0.4841} = <strong>3.0219</strong></code><br>
3. <strong>Pressure Intensities at Bottom of Wall (z = 6 m):</strong><br>
• <strong>Total Active Earth Pressure:</strong><br>
<code>p_a = K_a \cdot \gamma \cdot H = 0.3210 \times 21 \times 6 = <strong>40.45 kN/m&sup2;</strong></code> (inclined at &beta; = 10&deg; to horizontal).<br>
• <strong>Total Passive Earth Pressure:</strong><br>
<code>p_p = K_p \cdot \gamma \cdot H = 3.0219 \times 21 \times 6 = <strong>380.76 kN/m&sup2;</strong></code> (inclined at &beta; = 10&deg; to horizontal)."""
    },
    {
        "id": "2025-Q1bii",
        "year": "2025",
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": "Q.1 (b) ii",
        "marks": 3,
        "type": "Numerical",
        "co": "CO1",
        "bl": "BL3 (Apply)",
        "pi": "2.1.2",
        "topic": "Coulomb Passive Earth Pressure with Wall Friction",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A rough vertical wall of 7.5 m height supports a horizontal backfill. If the angle of internal friction and angle of wall friction are respectively 33&deg; and 12&deg;, compute the passive earth pressure at the bottom of wall. Assume density of 18.5 kN/m&sup3;.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Height H = 7.5 m, &phi; = 33&deg;, &delta; = 12&deg;, &gamma; = 18.5 kN/m&sup3;, vertical wall (&alpha; = 90&deg;), horizontal backfill (&beta; = 0&deg;).<br>
1. <strong>Coulomb's Passive Earth Pressure Coefficient (K<sub>p</sub>):</strong><br>
For vertical wall with horizontal backfill:<br>
<code>K_p = \frac{\cos^2\phi}{\cos\delta \left[1 - \sqrt{\frac{\sin(\phi + \delta)\sin\phi}{\cos\delta}}\right]^2}</code><br>
2. <strong>Trigonometric Values:</strong><br>
<code>\cos 33^\circ = 0.8387 \implies \cos^2 33^\circ = 0.7034</code><br>
<code>\cos 12^\circ = 0.9781</code><br>
<code>\sin(\phi + \delta) = \sin 45^\circ = 0.7071</code><br>
<code>\sin 33^\circ = 0.5446</code><br>
<code>\sqrt{\frac{0.7071 \times 0.5446}{0.9781}} = \sqrt{\frac{0.3851}{0.9781}} = \sqrt{0.3937} = 0.6275</code><br>
<code>\left[1 - 0.6275\right]^2 = 0.3725^2 = 0.1388</code><br>
<code>K_p = \frac{0.7034}{0.9781 \times 0.1388} = \frac{0.7034}{0.1358} = <strong>5.180</strong></code><br>
3. <strong>Passive Earth Pressure at Bottom of Wall (z = 7.5 m):</strong><br>
<code>p_p = K_p \cdot \gamma \cdot H = 5.180 \times 18.5 \times 7.5 = <strong>718.73 kN/m&sup2;</strong></code><br>
Acts at an angle &delta; = 12&deg; upwards to the normal."""
    },
    {
        "id": "2025-Q1biii",
        "year": "2025",
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": "Q.1 (b) iii",
        "marks": 3,
        "type": "Numerical",
        "co": "CO1",
        "bl": "BL3 (Apply)",
        "pi": "2.1.2",
        "topic": "Active Earth Pressure Distribution with Water Table & Cohesion",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""A retaining wall of 4.5 m height carries a horizontal backfill with c = 35 kN/m&sup2;, &phi; = 10&deg;; &gamma; = 17.2 kN/m&sup3;. The water table is located at 1.50 m below the ground. Sketch the distribution of active earth pressure. Assume the value of angle of internal friction is 14&deg;; and cohesion c = 50 kN/m&sup2; in the submerged condition.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Total height H = 4.5 m. Water table at depth H<sub>1</sub> = 1.5 m below ground. Submerged stratum H<sub>2</sub> = 3.0 m.<br>
Layer 1 (0 to 1.5 m): c<sub>1</sub> = 35 kN/m&sup2;, &phi;<sub>1</sub> = 10&deg;, &gamma;<sub>1</sub> = 17.2 kN/m&sup3;.<br>
Layer 2 (1.5 to 4.5 m): c<sub>2</sub> = 50 kN/m&sup2;, &phi;<sub>2</sub> = 14&deg;, &gamma;<sub>sat</sub> = 20 kN/m&sup3; (&gamma;' = 20 - 9.81 = 10.19 kN/m&sup3;).<br>
1. <strong>Active Earth Pressure Coefficients:</strong><br>
<code>K_{a1} = \frac{1 - \sin 10^\circ}{1 + \sin 10^\circ} = \frac{1 - 0.1736}{1 + 0.1736} = 0.7041 \implies \sqrt{K_{a1}} = 0.8391</code><br>
<code>K_{a2} = \frac{1 - \sin 14^\circ}{1 + \sin 14^\circ} = \frac{1 - 0.2419}{1 + 0.2419} = 0.6104 \implies \sqrt{K_{a2}} = 0.7813</code><br>
2. <strong>Pressure Distribution by Depths:</strong><br>
• <strong>At Ground Surface (z = 0 m):</strong><br>
<code>\sigma'_v = 0 \implies p_{a0} = 0 - 2 c_1 \sqrt{K_{a1}} = -2 \times 35 \times 0.8391 = <strong>-58.74 kN/m&sup2;</strong></code> (Tensile crack zone).<br>
• <strong>At Top Layer Interface (z = 1.5 m, above WT):</strong><br>
<code>\sigma'_v = 17.2 \times 1.5 = 25.8 kPa \implies p_{a1} = 25.8(0.7041) - 58.74 = 18.17 - 58.74 = <strong>-40.57 kN/m&sup2;</strong></code>.<br>
• <strong>At Bottom Layer Interface (z = 1.5 m, below WT):</strong><br>
<code>\sigma'_v = 25.8 kPa \implies p_{a1}' = 25.8(0.6104) - 2(50)(0.7813) = 15.75 - 78.13 = <strong>-62.38 kN/m&sup2;</strong></code>.<br>
• <strong>At Base of Wall (z = 4.5 m):</strong><br>
<code>\sigma'_v = 25.8 + 10.19 \times 3.0 = 56.37 kPa</code><br>
<code>p_{a,soil} = 56.37(0.6104) - 78.13 = 34.41 - 78.13 = -43.72 kN/m&sup2; \approx 0</code> (cohesion suppresses effective thrust).<br>
• <strong>Hydrostatic Water Pressure at Base:</strong><br>
<code>u = \gamma_w \times H_2 = 9.81 \times 3.0 = <strong>29.43 kN/m&sup2;</strong></code>.<br>
3. <strong>Net Pressure Distribution:</strong><br>
Tensile stresses exist throughout the soil depth due to high cohesion (c = 35 to 50 kPa). When tension cracks are ignored or braced, the net lateral pressure acting on the wall consists predominantly of hydrostatic water pressure u = 29.43 kN/m&sup2; at the base."""
    },
    {
        "id": "2025-Q1c",
        "year": "2025",
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": "Q.1 (c)",
        "marks": 6,
        "type": "Derivation",
        "co": "CO1",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Coulomb Sliding Wedge Maximum Thrust Derivation",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""Derive the condition of maximum active earth pressure from sliding wedge.""",
        "solution": r"""<strong>Derivation of Condition for Maximum Active Earth Pressure (Sliding Wedge Method):</strong><br>
1. <strong>Equilibrium of Trial Wedge (ABC):</strong><br>
Consider a planar failure wedge with failure surface inclined at angle &theta; to the horizontal. The forces in equilibrium are:<br>
• <strong>W:</strong> Weight of sliding wedge ABC = <code>\frac{1}{2}\gamma H \cdot BC = \frac{1}{2}\gamma H^2 \frac{\sin(\alpha + \beta)\sin(\alpha - \theta)}{\sin^2\alpha \sin(\theta - \beta)}</code>.<br>
• <strong>R:</strong> Soil reaction across failure surface inclined at &phi; to the normal.<br>
• <strong>P<sub>a</sub>:</strong> Active thrust on wall face inclined at &delta; to normal.<br>
2. <strong>Applying Sine Rule to Force Triangle:</strong><br>
From the closed polygon of forces (W, R, P<sub>a</sub>):<br>
<code>\frac{P_a}{\sin(\theta - \phi)} = \frac{W}{\sin(180^\circ - (\alpha + \theta - \phi + \delta))}</code><br>
<code>P_a = W \cdot \frac{\sin(\theta - \phi)}{\sin(\alpha + \theta - \phi + \delta)}</code><br>
3. <strong>Condition for Maximum Thrust:</strong><br>
To find the critical failure plane that delivers the maximum lateral active thrust, set the partial derivative with respect to &theta; to zero:<br>
<code>\frac{\partial P_a}{\partial \theta} = 0</code><br>
Differentiating using quotient rule yields the classical Coulomb wedge condition:<br>
<code>\frac{\partial W}{\partial \theta} \sin(\alpha + \theta - \phi + \delta) - W \cos(\alpha + \theta - \phi + \delta) = 0</code><br>
4. <strong>Resulting Coulomb Active Thrust Equation:</strong><br>
Solving for critical wedge angle &theta;<sub>cr</sub> gives the maximum active thrust:<br>
<code>P_a = \frac{1}{2} \gamma H^2 K_a</code><br>
Where Coulomb's active coefficient is:<br>
<code>K_a = \frac{\sin^2(\alpha + \phi)}{\sin^2\alpha \sin(\alpha - \delta) \left[1 + \sqrt{\frac{\sin(\phi + \delta)\sin(\phi - \beta)}{\sin(\alpha - \delta)\sin(\alpha + \beta)}}\right]^2}</code>."""
    },
    {
        "id": "2025-Q1c-OR",
        "year": "2025",
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": "Q.1 (c) OR",
        "marks": 6,
        "type": "Theory / Derivation",
        "co": "CO1",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Rebhann's Graphical Construction & Proof",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""Explain the Rebhann's graphical construction for active earth pressure and prove that it satisfy the condition of maximum earth pressure""",
        "solution": r"""<strong>Rebhann's Graphical Construction for Active Earth Thrust:</strong><br>
Based on Poncelet's modification of Coulomb's wedge theory for determining maximum active thrust graphically.<br>
1. <strong>Construction Procedure:</strong><br>
• Draw backfill surface AD and wall back AB inclined at &alpha; to horizontal.<br>
• Draw &phi;-line BD from the heel B inclined at angle &phi; to horizontal, meeting ground surface at D.<br>
• Draw &psi;-line BL from heel B inclined at angle &psi; = (&alpha; - &delta;) to BD.<br>
• Draw semi-circle on BD as diameter.<br>
• From wall top A, draw line AE parallel to &psi;-line BL, meeting BD at E.<br>
• Erect perpendicular EF at E to intersect semi-circle at F.<br>
• With center B and radius BF, draw arc cutting BD at point T.<br>
• Through T, draw line TC parallel to &psi;-line BL, intersecting ground surface at C. Line BC defines the <strong>critical failure surface</strong>.<br>
• Through T, draw line TP parallel to AE to cut BC at P.<br>
2. <strong>Magnitude of Total Active Thrust:</strong><br>
<code>P_a = \gamma \cdot \text{Area of } \Delta CPT</code><br>
3. <strong>Mathematical Proof of Maximum Earth Thrust:</strong><br>
• The active thrust from a sliding wedge ABC is <code>P_a = \gamma \cdot \text{Area}(\Delta ABC) \cdot \frac{\sin(\theta - \phi)}{\sin(\alpha + \theta - \phi + \delta)}</code>.<br>
• By geometric similarity of triangles &Delta;BDC and &Delta;CPT:<br>
<code>\text{Area}(\Delta CPT) = \frac{1}{2} \cdot CT \cdot PT \cdot \sin\psi</code><br>
• For maximum thrust: <code>\frac{\partial P_a}{\partial \theta} = 0 \iff BT^2 = BD \cdot BE</code>.<br>
• Since BF is the mean proportional in semi-circle BFD on diameter BD: <code>BF^2 = BD \cdot BE</code>.<br>
• But radius BT = BF, therefore <code>BT^2 = BD \cdot BE</code> holds identically.<br>
• Hence, Rebhann's graphical construction strictly satisfies the condition of maximum active earth pressure."""
    },
    {
        "id": "2025-Q2a",
        "year": "2025",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "q_no": "Q.2 (a)",
        "marks": 2,
        "type": "Theory",
        "co": "CO2",
        "bl": "BL2 (Understand)",
        "pi": "1.3.1",
        "topic": "Bearing Capacity Definitions & Terminology Suffixes",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers",
        "question": r"""What do you mean by bearing capacity? What are the different suffixes to be used before bearing capacity?""",
        "solution": r"""<strong>1. Bearing Capacity of Soil:</strong><br>
The maximum load-carrying resistance per unit area that the underlying soil or rock mass can support without undergoing shear failure or excessive foundation settlement.<br>
<em>Example:</em> A footing imposing a contact pressure of 200 kPa on soil capable of resisting 500 kPa without failure.<br>
<strong>2. Different Suffixes Used Before Bearing Capacity:</strong><br>
1. <strong>Gross Ultimate (q<sub>u</sub> / q<sub>ult</sub>):</strong> Total intensity of loading at base of foundation at which soil fails in shear.<br>
2. <strong>Net Ultimate (q<sub>nu</sub>):</strong> Ultimate intensity above initial effective surcharge: <code>q_{nu} = q_u - \gamma D_f</code>.<br>
3. <strong>Net Safe (q<sub>ns</sub>):</strong> Net ultimate capacity divided by factor of safety: <code>q_{ns} = \frac{q_{nu}}{FOS}</code>.<br>
4. <strong>Gross Safe (q<sub>s</sub>):</strong> Maximum gross intensity safe against shear failure: <code>q_s = q_{ns} + \gamma D_f = \frac{q_{nu}}{FOS} + \gamma D_f</code>.<br>
5. <strong>Safe Bearing Pressure (q<sub>ps</sub>):</strong> Maximum allowable net intensity that limits total and differential settlement to tolerable values (e.g. &le; 25 mm).<br>
6. <strong>Allowable Bearing Capacity (q<sub>a</sub>):</strong> Final design value; smaller of gross safe (q<sub>s</sub>) and safe bearing pressure (q<sub>ps</sub>)."""
    },
    {
        "id": "2025-Q2bi",
        "year": "2025",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "q_no": "Q.2 (b) i",
        "marks": 3,
        "type": "Theory",
        "co": "CO2",
        "bl": "BL2 (Understand)",
        "pi": "2.1.3",
        "topic": "Modes of Shear Failure & Load Settlement Curves",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""Describe the three modes of shear failure in soil. Draw load-settlement curves for each mode and explain which type of soil exhibits each failure pattern.""",
        "solution": r"""<strong>Three Modes of Shear Failure in Soil (Vesic):</strong><br>
1. <strong>General Shear Failure:</strong><br>
• Continuous, well-defined slip surfaces extend from footing edges to the ground surface.<br>
• Significant soil bulging/heaving occurs adjacent to the foundation, accompanied by sudden catastrophic tilting.<br>
• Load-settlement curve shows a clear, distinct peak failure load.<br>
• <em>Soil Type:</em> Dense sand (D<sub>r</sub> &gt; 70%, &phi; &gt; 36&deg;) and stiff, overconsolidated clays under shallow footings.<br>
2. <strong>Local Shear Failure:</strong><br>
• Shear failure planes develop clearly beneath the footing but terminate within the soil mass without extending to the surface.<br>
• Only slight bulging occurs with noticeable continuous settlement.<br>
• Load-settlement curve has no clear peak; ultimate load is taken where settlement rate increases steeply.<br>
• <em>Soil Type:</em> Medium dense sand (35% &lt; D<sub>r</sub> &lt; 70%, 28&deg; &le; &phi; &le; 36&deg;) and medium-consistency clays.<br>
3. <strong>Punching Shear Failure:</strong><br>
• Failure pattern consists of vertical downward compression directly beneath the footing wedge.<br>
• Zero bulging or heaving at ground surface; soil outside remains unaffected.<br>
• Load-settlement curve shows steep continuous plunging settlement with no definite yield point.<br>
• <em>Soil Type:</em> Very loose sand (D<sub>r</sub> &lt; 35%, &phi; &lt; 28&deg;), soft sensitive clays, and deep footings."""
    },
    {
        "id": "2025-Q2bii",
        "year": "2025",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "q_no": "Q.2 (b) ii",
        "marks": 3,
        "type": "Theory",
        "co": "CO2",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Effect of Water Table on Bearing Capacity of Soils",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Explain the effect of water table on bearing capacity of soils.""",
        "solution": r"""<strong>Effect of Water Table on Bearing Capacity:</strong><br>
Submergence halves the effective unit weight of soil (&gamma;' &approx; 0.5 &gamma;<sub>bulk</sub>), thereby reducing effective overburden stress and shear resistance.<br>
1. <strong>Governing Terzaghi Equation with Correction Factors:</strong><br>
<code>q_{ult} = c N_c + \gamma D_f N_q \cdot R_{w1} + 0.5 \gamma B N_\gamma \cdot R_{w2}</code><br>
2. <strong>Water Table Correction Factor R<sub>w1</sub> (Surcharge Zone):</strong><br>
Applies to soil above footing base (depth z<sub>w1</sub> from ground surface, 0 &le; z<sub>w1</sub> &le; D<sub>f</sub>):<br>
<code>R_{w1} = 0.5 \left(1 + \frac{z_{w1}}{D_f}\right)</code><br>
• If WT is at ground level (z<sub>w1</sub> = 0): R<sub>w1</sub> = 0.5 (50% reduction in surcharge term).<br>
• If WT is at or below footing base (z<sub>w1</sub> = D<sub>f</sub>): R<sub>w1</sub> = 1.0 (no reduction).<br>
3. <strong>Water Table Correction Factor R<sub>w2</sub> (Wedge Zone):</strong><br>
Applies to soil within wedge depth B below base (depth z<sub>w2</sub> from base, 0 &le; z<sub>w2</sub> &le; B):<br>
<code>R_{w2} = 0.5 \left(1 + \frac{z_{w2}}{B}\right)</code><br>
• If WT is at foundation base (z<sub>w2</sub> = 0): R<sub>w2</sub> = 0.5 (50% reduction in soil weight term).<br>
• If WT is at depth &ge; B below base (z<sub>w2</sub> &ge; B): R<sub>w2</sub> = 1.0 (zero effect on bearing capacity).<br>
4. <strong>Engineering Significance:</strong><br>
Rise of water table to ground level causes an overall <strong>50% reduction</strong> in the ultimate bearing capacity of cohesionless soils."""
    },
    {
        "id": "2025-Q2biii",
        "year": "2025",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "q_no": "Q.2 (b) iii",
        "marks": 3,
        "type": "Numerical",
        "co": "CO2",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Square Footing in Purely Cohesive Soil",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""Compute the net safe bearing capacity of a square footing of size 2.5 m, provided at 2.0 m depth in a purely cohesive soil with Unconfined Shear Strength of 150 kN/m&sup2; and density being 18 kN/m&sup3;. Use factor of safety as 2.5.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Footing size B = 2.5 m, depth D<sub>f</sub> = 2.0 m, &gamma; = 18 kN/m&sup3;, unconfined compressive strength q<sub>u</sub> = 150 kN/m&sup2;, FOS = 2.5, purely cohesive soil (&phi; = 0).<br>
1. <strong>Cohesion Intercept (c<sub>u</sub>):</strong><br>
<code>c_u = \frac{q_u}{2} = \frac{150}{2} = <strong>75 kN/m&sup2;</strong></code><br>
2. <strong>Terzaghi Bearing Capacity Factors for &phi; = 0:</strong><br>
<code>N_c = 5.7, \quad N_q = 1.0, \quad N_\gamma = 0</code><br>
For square footing, shape factor s<sub>c</sub> = 1.3:<br>
3. <strong>Net Ultimate Bearing Capacity (q<sub>nu</sub>):</strong><br>
<code>q_{nu} = 1.3 c_u N_c = 1.3 \times 75 \times 5.7 = <strong>555.75 kN/m&sup2;</strong></code><br>
4. <strong>Net Safe Bearing Capacity (q<sub>ns</sub>):</strong><br>
<code>q_{ns} = \frac{q_{nu}}{FOS} = \frac{555.75}{2.5} = <strong>222.30 kN/m&sup2;</strong></code><br>
<em>Note:</em> Depth D<sub>f</sub> and soil density &gamma; do not affect net ultimate/safe capacity in pure clay (&phi; = 0)."""
    },
    {
        "id": "2025-Q2c",
        "year": "2025",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "q_no": "Q.2 (c)",
        "marks": 6,
        "type": "Numerical",
        "co": "CO2",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Square Footing Bearing Capacity with Water Table",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A square footing of 3.5 m is resting at 3 m below the ground level. The shear parameters of soil are respectively 40 kN/m&sup2; and 12&deg;. The density of soil is 20 kN/m&sup3;. The water table lies at 2 m below the base of footing. Calculate the net safe bearing capacity. Assume factor of safety of 3.0.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Square footing B = 3.5 m, D<sub>f</sub> = 3.0 m, c = 40 kN/m&sup2;, &phi; = 12&deg;, &gamma; = 20 kN/m&sup3;, WT depth below base z<sub>w2</sub> = 2.0 m, FOS = 3.0.<br>
Since &phi; = 12&deg; &lt; 28&deg;, <strong>local shear failure</strong> governs.<br>
1. <strong>Mobilized Shear Parameters:</strong><br>
<code>c_m = \frac{2}{3} c = \frac{2}{3} \times 40 = 26.67 kN/m&sup2;</code><br>
<code>\tan\phi_m = \frac{2}{3}\tan 12^\circ = \frac{2}{3}(0.2126) = 0.1417 \implies \phi_m \approx 8.06^\circ</code><br>
2. <strong>Bearing Capacity Factors (Table 1 / IS: 6403 for &phi;<sub>m</sub> &approx; 8.1&deg;):</strong><br>
Interpolating between &phi; = 5&deg; and 10&deg; (Table 1: &phi;=10&deg; &rarr; N_c=5.14, N_q=1.00, N_&gamma;=0.00):<br>
<code>N'_c \approx 7.0, \quad N'_q \approx 1.8, \quad N'_\gamma \approx 0.4</code><br>
3. <strong>Water Table Correction Factor (z<sub>w2</sub> = 2.0 m &lt; B = 3.5 m):</strong><br>
Water table is below footing base, so R<sub>w1</sub> = 1.0 (surcharge is dry).<br>
<code>R_{w2} = 0.5 \left(1 + \frac{z_{w2}}{B}\right) = 0.5 \left(1 + \frac{2.0}{3.5}\right) = 0.5(1 + 0.5714) = <strong>0.7857</strong></code><br>
4. <strong>Terzaghi Net Ultimate Capacity for Square Footing:</strong><br>
<code>q_{nu} = 1.3 c_m N'_c + \gamma D_f (N'_q - 1) + 0.4 \gamma B N'_\gamma \cdot R_{w2}</code><br>
<code>= 1.3(26.67)(7.0) + 20(3.0)(1.8 - 1) + 0.4(20)(3.5)(0.4)(0.7857)</code><br>
<code>= 242.70 + 48.00 + 8.80 = <strong>299.50 kN/m&sup2;</strong></code><br>
5. <strong>Net Safe Bearing Capacity:</strong><br>
<code>q_{ns} = \frac{q_{nu}}{FOS} = \frac{299.50}{3.0} = <strong>99.83 kN/m&sup2;</strong></code>."""
    },
    {
        "id": "2025-Q2c-OR",
        "year": "2025",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "q_no": "Q.2 (c) OR",
        "marks": 6,
        "type": "Numerical",
        "co": "CO2",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Eccentrically Loaded Rectangular Footing",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""A rectangular footing 3 m x 2 m carries a load of 1500 kN with eccentricity of 0.3 m along the length and 0.2 m along the width. The footing is located at 1.5 m depth in soil with c = 20 kN/m&sup2;, &phi; = 25&deg;, &gamma; = 19 kN/m&sup3;. Calculate the maximum pressure at the base and check for safety.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
L = 3.0 m, B = 2.0 m, Q = 1500 kN, e<sub>L</sub> = 0.3 m, e<sub>B</sub> = 0.2 m, D<sub>f</sub> = 1.5 m, c = 20 kN/m&sup2;, &phi; = 25&deg;, &gamma; = 19 kN/m&sup3;.<br>
1. <strong>Eccentricity Limit Check (Kern of Section):</strong><br>
<code>\frac{e_L}{L} = \frac{0.3}{3.0} = 0.10 \le \frac{1}{6} \approx 0.167 \quad \text{(Safe, zero tension)}</code><br>
<code>\frac{e_B}{B} = \frac{0.2}{2.0} = 0.10 \le \frac{1}{6} \approx 0.167 \quad \text{(Safe, zero tension)}</code><br>
2. <strong>Maximum Base Pressure (Elastic Distribution):</strong><br>
<code>q_{max} = \frac{Q}{B L} \left(1 + \frac{6 e_L}{L} + \frac{6 e_B}{B}\right)</code><br>
<code>q_{max} = \frac{1500}{2.0 \times 3.0} \left(1 + \frac{6 \times 0.3}{3.0} + \frac{6 \times 0.2}{2.0}\right) = 250 \left(1 + 0.60 + 0.60\right) = 250(2.20) = <strong>550.0 kN/m&sup2;</strong></code><br>
<code>q_{min} = \frac{Q}{BL}\left(1 - \frac{6 e_L}{L} - \frac{6 e_B}{B}\right) = 250(1 - 1.20) = -50 kN/m&sup2;</code> (slight separation at extreme corner).<br>
3. <strong>Meyerhof's Effective Dimensions for Bearing Capacity:</strong><br>
<code>L' = L - 2 e_L = 3.0 - 2(0.3) = 2.4 m</code><br>
<code>B' = B - 2 e_B = 2.0 - 2(0.2) = 1.6 m</code><br>
From Table 1 for &phi; = 25&deg;: N<sub>c</sub> = 10.98, N<sub>q</sub> = 3.94, N<sub>&gamma;</sub> = 2.65.<br>
<code>q_{ult} = c N_c \left(1 + 0.2\frac{B'}{L'}\right) + \gamma D_f N_q + 0.5 \gamma B' N_\gamma \left(1 - 0.2\frac{B'}{L'}\right)</code><br>
<code>= 20(10.98)(1 + 0.2\frac{1.6}{2.4}) + 19(1.5)(3.94) + 0.5(19)(1.6)(2.65)(1 - 0.2\frac{1.6}{2.4})</code><br>
<code>= 20(10.98)(1.133) + 112.29 + 40.28(0.867) = 248.81 + 112.29 + 34.92 = <strong>396.02 kN/m&sup2;</strong></code>.<br>
4. <strong>Safety Check:</strong><br>
Average effective pressure: <code>q'_{avg} = \frac{Q}{B' L'} = \frac{1500}{1.6 \times 2.4} = 390.63 kN/m&sup2; \approx q_{ult}</code>.<br>
<code>FOS = \frac{q_{ult}}{q'_{avg}} = \frac{396.02}{390.63} = <strong>1.01 &lt; 2.5</strong></code>.<br>
<strong>Conclusion:</strong> UNSAFE in shear; footing dimensions must be increased or eccentricity reduced."""
    },
    {
        "id": "2025-Q3a",
        "year": "2025",
        "unit": 3,
        "unit_name": "Shear Strength of Soil",
        "q_no": "Q.3 (a)",
        "marks": 2,
        "type": "Theory",
        "co": "CO3",
        "bl": "BL2 (Understand)",
        "pi": "1.3.1",
        "topic": "Coulomb's Law of Shear Strength",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""Discuss Coulomb's law of shear strength of soil""",
        "solution": r"""<strong>Coulomb's Law of Shear Strength of Soil:</strong><br>
States that the shear strength (&tau;<sub>f</sub>) along any failure plane within a soil mass is governed by internal cohesion and frictional resistance directly proportional to the normal stress.<br>
1. <strong>Total Stress Formulation:</strong><br>
<code>\tau_f = c + \sigma \tan\phi</code><br>
2. <strong>Terzaghi's Effective Stress Formulation (Modern Form):</strong><br>
<code>\tau_f = c' + \sigma' \tan\phi' = c' + (\sigma - u) \tan\phi'</code><br>
3. <strong>Parameter Definitions:</strong><br>
• <strong>c / c':</strong> Cohesion intercept (cementation and intermolecular bonds) in kPa.<br>
• <strong>&sigma; / &sigma;':</strong> Total and effective normal stress acting on the failure plane in kPa.<br>
• <strong>&phi; / &phi;':</strong> Angle of shearing resistance (interparticle friction and interlocking).<br>
• <strong>u:</strong> Pore water pressure in kPa.<br>
<em>Example:</em> Pure sand has c' = 0, giving &tau;<sub>f</sub> = &sigma;' tan &phi;'; pure saturated clay under undrained condition has &phi;<sub>u</sub> = 0, giving &tau;<sub>f</sub> = c<sub>u</sub>."""
    },
    {
        "id": "2025-Q3bi",
        "year": "2025",
        "unit": 3,
        "unit_name": "Shear Strength of Soil",
        "q_no": "Q.3 (b) i",
        "marks": 3,
        "type": "Numerical",
        "co": "CO3",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Failure Plane Stresses & Shear Parameters",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""The shear stress and normal stress at a failure plane in a cohesionless soil mass were found to be 4 kPa and 10 kPa respectively. Determine the resultant stress on failure plane and inclination of failure plane. Also compute the shear parameters.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Shear stress on failure plane &tau; = 4 kPa, normal stress &sigma; = 10 kPa, cohesionless soil (c = 0).<br>
1. <strong>Resultant Stress on Failure Plane (R):</strong><br>
<code>R = \sqrt{\sigma^2 + \tau^2} = \sqrt{10^2 + 4^2} = \sqrt{116} = <strong>10.77 kPa</strong></code><br>
2. <strong>Shear Parameter (Angle of Internal Friction &phi;):</strong><br>
For cohesionless soil (c = 0), the failure envelope passes through the origin:<br>
<code>\tau = \sigma \tan\phi \implies \tan\phi = \frac{\tau}{\sigma} = \frac{4}{10} = 0.40</code><br>
<code>\phi = \tan^{-1}(0.40) = <strong>21.80^\circ</strong>, \quad c = 0</code><br>
3. <strong>Inclination of Failure Plane (&theta;<sub>cr</sub>):</strong><br>
The critical failure plane is inclined at &theta;<sub>cr</sub> to the major principal plane:<br>
<code>\theta_{cr} = 45^\circ + \frac{\phi}{2} = 45^\circ + \frac{21.80^\circ}{2} = <strong>55.90^\circ</strong></code><br>
Angle of obliquity on the failure plane is &psi; = &phi; = 21.80&deg;."""
    },
    {
        "id": "2025-Q3bii",
        "year": "2025",
        "unit": 3,
        "unit_name": "Shear Strength of Soil",
        "q_no": "Q.3 (b) ii",
        "marks": 3,
        "type": "Numerical",
        "co": "CO3",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Triaxial Test Corrected Area & Shear Parameters",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""The deviator force to shear the soil specimen of 38 mm diameter and 76 mm height under a confining pressure of 100 kN/m&sup2; is 251 N while it shears under a deviator force of 327 N at a confining pressure of 200 kN/m&sup2;. The deformation at the time of failure is respectively 2.0 mm and 5.2 mm. Determine the shear parameters. Determine the deviator stress under confining pressure of 250 kPa.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
d<sub>0</sub> = 38 mm = 0.038 m, L<sub>0</sub> = 76 mm = 0.076 m.<br>
Initial area: <code>A_0 = \frac{\pi}{4}(0.038)^2 = 1.134 \times 10^{-3} m^2 = 1134 mm^2</code>.<br>
1. <strong>Test 1 (&sigma;<sub>3</sub> = 100 kPa):</strong><br>
Deformation &Delta;L<sub>1</sub> = 2.0 mm &rarr; axial strain <code>\epsilon_1 = \frac{2.0}{76} = 0.0263</code>.<br>
Corrected area: <code>A_{c1} = \frac{A_0}{1 - \epsilon_1} = \frac{1.134 \times 10^{-3}}{1 - 0.0263} = 1.165 \times 10^{-3} m^2</code>.<br>
Deviator stress: <code>\sigma_{d1} = \frac{P_1}{A_{c1}} = \frac{251 \times 10^{-3} kN}{1.165 \times 10^{-3} m^2} = <strong>215.45 kPa</strong></code>.<br>
Major principal stress: <code>\sigma_1 = 100 + 215.45 = <strong>315.45 kPa</strong></code>.<br>
2. <strong>Test 2 (&sigma;<sub>3</sub> = 200 kPa):</strong><br>
Deformation &Delta;L<sub>2</sub> = 5.2 mm &rarr; axial strain <code>\epsilon_2 = \frac{5.2}{76} = 0.0684</code>.<br>
Corrected area: <code>A_{c2} = \frac{1.134 \times 10^{-3}}{1 - 0.0684} = 1.217 \times 10^{-3} m^2</code>.<br>
Deviator stress: <code>\sigma_{d2} = \frac{327 \times 10^{-3}}{1.217 \times 10^{-3}} = <strong>268.69 kPa</strong></code>.<br>
Major principal stress: <code>\sigma_1 = 200 + 268.69 = <strong>468.69 kPa</strong></code>.<br>
3. <strong>Mohr-Coulomb Failure Equation:</strong><br>
<code>\sigma_1 = \sigma_3 N_\phi + 2 c \sqrt{N_\phi}</code><br>
Subtracting Test 1 from Test 2:<br>
<code>468.69 - 315.45 = N_\phi(200 - 100) \implies 153.24 = 100 N_\phi \implies N_\phi = <strong>1.5324</strong></code>.<br>
Angle of friction: <code>\frac{1 + \sin\phi}{1 - \sin\phi} = 1.5324 \implies \sin\phi = \frac{0.5324}{2.5324} = 0.2102 \implies \phi = <strong>12.13^\circ</strong></code>.<br>
Cohesion intercept: <code>315.45 = 100(1.5324) + 2 c \sqrt{1.5324} \implies 2 c (1.2379) = 162.21 \implies c = <strong>65.52 kPa</strong></code>.<br>
4. <strong>Deviator Stress at Confining Pressure &sigma;<sub>3</sub> = 250 kPa:</strong><br>
<code>\sigma_1 = 250(1.5324) + 2(65.52)(1.2379) = 383.10 + 162.21 = 545.31 kPa</code><br>
<code>\sigma_d = \sigma_1 - \sigma_3 = 545.31 - 250 = <strong>295.31 kPa</strong></code>."""
    },
    {
        "id": "2025-Q3biii",
        "year": "2025",
        "unit": 3,
        "unit_name": "Shear Strength of Soil",
        "q_no": "Q.3 (b) iii",
        "marks": 3,
        "type": "Theory",
        "co": "CO3",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Triaxial Tests & Best Test Selection",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Explain various kinds of triaxial tests. Which test is best suited for the cohesive soil deposit having a permeable layer immediately below the foundation level?""",
        "solution": r"""<strong>1. Three Kinds of Triaxial Shear Tests:</strong><br>
1. <strong>Unconsolidated Undrained (UU / Quick Test):</strong> Zero drainage allowed during both cell pressure application and shear stage. Measures undrained shear strength (c<sub>u</sub>, &phi;<sub>u</sub> = 0 for saturated soil). Appropriate for short-term end-of-construction stability.<br>
2. <strong>Consolidated Undrained (CU Test):</strong> Complete drainage permitted under cell pressure until consolidation completes; shear stage is undrained with pore water pressure measurement. Gives effective parameters (c', &phi;') and undrained parameters.<br>
3. <strong>Consolidated Drained (CD / Slow Test):</strong> Full drainage allowed during cell pressure consolidation and during shearing at an extremely slow strain rate so pore pressure remains zero (&Delta;u = 0). Measures true drained effective parameters (c', &phi;').<br>
<strong>2. Test Selection for Cohesive Deposit with Permeable Layer Below Foundation:</strong><br>
• <strong>Best Suited Test:</strong> <strong>Consolidated Drained (CD) Test</strong> or <strong>Consolidated Undrained (CU) Test with pore pressure measurement</strong>.<br>
• <em>Engineering Justification:</em> The presence of an immediately adjacent permeable layer provides a short drainage boundary path, allowing water to dissipate rapidly during and after construction. A CD or CU test accurately reproduces this field dissipation mechanism, providing the true drained effective shear parameters required for long-term bearing capacity and stability analysis."""
    },
    {
        "id": "2025-Q3c",
        "year": "2025",
        "unit": 3,
        "unit_name": "Shear Strength of Soil",
        "q_no": "Q.3 (c)",
        "marks": 6,
        "type": "Derivation",
        "co": "CO3",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Mohr-Coulomb Principal Stress Relationship",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""Derive a relationship between effective shear parameters and principal stresses.""",
        "solution": r"""<strong>Derivation of Relationship Between Effective Shear Parameters (c', &phi;') and Principal Stresses (&sigma;'<sub>1</sub>, &sigma;'<sub>3</sub>):</strong><br>
1. <strong>Geometry of Mohr Circle at Failure:</strong><br>
Consider a soil element subjected to effective principal stresses &sigma;'<sub>1</sub> and &sigma;'<sub>3</sub>. The Mohr circle is tangent to the failure envelope &tau;<sub>f</sub> = c' + &sigma;' tan &phi;' at failure point F.<br>
• Center of circle: <code>C = \left(\frac{\sigma'_1 + \sigma'_3}{2}, 0\right)</code><br>
• Radius of circle: <code>R = CF = \frac{\sigma'_1 - \sigma'_3}{2}</code><br>
• Origin of failure line: <code>O' = (-c' \cot\phi', 0)</code><br>
2. <strong>Formulating Trigonometric Relation in &Delta;O'CF:</strong><br>
Triangle O'CF is right-angled at F (&ang;O'FC = 90&deg;):<br>
<code>\sin\phi' = \frac{CF}{O'C} = \frac{\frac{\sigma'_1 - \sigma'_3}{2}}{\frac{\sigma'_1 + \sigma'_3}{2} + c'\cot\phi'}</code><br>
Cross-multiplying:<br>
<code>\left(\frac{\sigma'_1 + \sigma'_3}{2} + c'\frac{\cos\phi'}{\sin\phi'}\right) \sin\phi' = \frac{\sigma'_1 - \sigma'_3}{2}</code><br>
<code>\left(\frac{\sigma'_1 + \sigma'_3}{2}\right)\sin\phi' + c'\cos\phi' = \frac{\sigma'_1 - \sigma'_3}{2}</code><br>
3. <strong>Regrouping &sigma;'<sub>1</sub> and &sigma;'<sub>3</sub> Terms:</strong><br>
<code>\frac{\sigma'_1}{2}(1 - \sin\phi') = \frac{\sigma'_3}{2}(1 + \sin\phi') + c'\cos\phi'</code><br>
Dividing through by <code>\frac{1 - \sin\phi'}{2}</code>:<br>
<code>\sigma'_1 = \sigma'_3 \left(\frac{1 + \sin\phi'}{1 - \sin\phi'}\right) + 2 c' \frac{\cos\phi'}{1 - \sin\phi'}</code><br>
4. <strong>Trigonometric Simplifications:</strong><br>
<code>\frac{1 + \sin\phi'}{1 - \sin\phi'} = \tan^2\left(45^\circ + \frac{\phi'}{2}\right) = N_\phi</code><br>
<code>\frac{\cos\phi'}{1 - \sin\phi'} = \frac{\sqrt{1 - \sin^2\phi'}}{1 - \sin\phi'} = \sqrt{\frac{1 + \sin\phi'}{1 - \sin\phi'}} = \tan\left(45^\circ + \frac{\phi'}{2}\right) = \sqrt{N_\phi}</code><br>
5. <strong>Final Governing Equation:</strong><br>
<code>\sigma'_1 = \sigma'_3 N_\phi + 2 c' \sqrt{N_\phi} = \sigma'_3 \tan^2\left(45^\circ + \frac{\phi'}{2}\right) + 2 c' \tan\left(45^\circ + \frac{\phi'}{2}\right)</code>."""
    },
    {
        "id": "2025-Q3c-OR",
        "year": "2025",
        "unit": 3,
        "unit_name": "Shear Strength of Soil",
        "q_no": "Q.3 (c) OR",
        "marks": 6,
        "type": "Numerical",
        "co": "CO3",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "CU Triaxial Test Total and Effective Shear Parameters",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""The following data refers to a triaxial compression tests performed on a soil sample. Determine the total and effective shear parameters of soil.<br>Observation 1: &sigma;<sub>3</sub> = 80 kPa, &sigma;<sub>d</sub> = 175 kPa, u = 45 kPa<br>Observation 2: &sigma;<sub>3</sub> = 150 kPa, &sigma;<sub>d</sub> = 240 kPa, u = 50 kPa<br>Observation 3: &sigma;<sub>3</sub> = 210 kPa, &sigma;<sub>d</sub> = 300 kPa, u = 60 kPa""",
        "solution": r"""<strong>Stress Computations Table:</strong><br>
• <strong>Obs 1:</strong> &sigma;<sub>3</sub> = 80 kPa, &sigma;<sub>1</sub> = 80 + 175 = 255 kPa; &sigma;'<sub>3</sub> = 80 - 45 = 35 kPa, &sigma;'<sub>1</sub> = 255 - 45 = 210 kPa.<br>
• <strong>Obs 2:</strong> &sigma;<sub>3</sub> = 150 kPa, &sigma;<sub>1</sub> = 150 + 240 = 390 kPa; &sigma;'<sub>3</sub> = 150 - 50 = 100 kPa, &sigma;'<sub>1</sub> = 390 - 50 = 340 kPa.<br>
• <strong>Obs 3:</strong> &sigma;<sub>3</sub> = 210 kPa, &sigma;<sub>1</sub> = 210 + 300 = 510 kPa; &sigma;'<sub>3</sub> = 210 - 60 = 150 kPa, &sigma;'<sub>1</sub> = 510 - 60 = 450 kPa.<br>
1. <strong>Total Shear Parameters (c, &phi;):</strong><br>
Using observations 1 and 3:<br>
<code>\sigma_1 = \sigma_3 N_\phi + 2 c \sqrt{N_\phi}</code><br>
<code>510 - 255 = N_\phi(210 - 80) \implies 255 = 130 N_\phi \implies N_\phi = 1.9615</code><br>
<code>\sin\phi = \frac{N_\phi - 1}{N_\phi + 1} = \frac{0.9615}{2.9615} = 0.3247 \implies \phi = <strong>18.95^\circ</strong></code><br>
<code>255 = 80(1.9615) + 2 c \sqrt{1.9615} \implies 2 c (1.4005) = 255 - 156.92 = 98.08 \implies c = <strong>35.01 kPa</strong></code>.<br>
2. <strong>Effective Shear Parameters (c', &phi;'):</strong><br>
Using effective stresses for observations 1 and 3:<br>
<code>\sigma'_1 = \sigma'_3 N'_\phi + 2 c' \sqrt{N'_\phi}</code><br>
<code>450 - 210 = N'_\phi(150 - 35) \implies 240 = 115 N'_\phi \implies N'_\phi = 2.0870</code><br>
<code>\sin\phi' = \frac{N'_\phi - 1}{N'_\phi + 1} = \frac{1.0870}{3.0870} = 0.3521 \implies \phi' = <strong>20.62^\circ</strong></code><br>
<code>210 = 35(2.0870) + 2 c' \sqrt{2.0870} \implies 2 c' (1.4446) = 210 - 73.05 = 136.95 \implies c' = <strong>47.40 kPa</strong></code>.<br>
<strong>Final Summary:</strong><br>
• Total parameters: <strong>c = 35.0 kPa, &phi; = 19.0&deg;</strong>.<br>
• Effective parameters: <strong>c' = 47.4 kPa, &phi;' = 20.6&deg;</strong>."""
    },
    {
        "id": "2025-Q4a",
        "year": "2025",
        "unit": 4,
        "unit_name": "Foundation Engineering & Deep Foundations",
        "q_no": "Q.4 (a)",
        "marks": 2,
        "type": "Theory",
        "co": "CO4",
        "bl": "BL2 (Understand)",
        "pi": "1.3.1",
        "topic": "Types of Shallow Foundations & Strap Footing",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""What are different types of shallow foundations? Draw neat sketch of strap footing.""",
        "solution": r"""<strong>1. Types of Shallow Foundations (D<sub>f</sub> &le; B):</strong><br>
1. <strong>Isolated / Spread Footing:</strong> Individual pad supporting a single column.<br>
2. <strong>Strip / Wall Footing:</strong> Continuous concrete strip supporting a load-bearing wall or row of closely spaced columns.<br>
3. <strong>Combined Footing:</strong> Common base slab supporting two columns (rectangular or trapezoidal when column loads differ).<br>
4. <strong>Strap / Cantilever Footing:</strong> Two isolated footings joined by a stiff cantilever beam that does not touch the soil.<br>
5. <strong>Raft / Mat Foundation:</strong> Large continuous slab supporting all columns and walls over the entire building footprint.<br>
<strong>2. Strap Footing Sketch & Features:</strong><br>
• Used when an exterior column is located at the property boundary line and cannot project outward.<br>
• A rigid strap beam connects the exterior footing to an adjacent interior footing.<br>
• The strap beam is isolated from soil beneath it (zero soil pressure under beam), transferring overturning moment to the interior footing without causing eccentricity on the soil."""
    },
    {
        "id": "2025-Q4bi",
        "year": "2025",
        "unit": 4,
        "unit_name": "Foundation Engineering & Deep Foundations",
        "q_no": "Q.4 (b) i",
        "marks": 3,
        "type": "Theory",
        "co": "CO4",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Requirements of Satisfactory Foundations",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""Enumerate the requirements of satisfactory foundations.""",
        "solution": r"""<strong>Four Fundamental Requirements of a Satisfactory Foundation:</strong><br>
1. <strong>Shear Failure / Bearing Capacity Criterion:</strong><br>
The foundation must have an adequate factor of safety (minimum FOS &ge; 2.5 to 3.0) against ultimate shear failure of the supporting soil mass under all severe design load combinations.<br>
2. <strong>Settlement Criterion:</strong><br>
Total settlement and differential settlement between adjacent columns must remain strictly within permissible limits (IS: 1904: isolated footings &le; 50 mm in clay, &le; 25 mm in sand; differential &le; 1/500) to prevent cracking or structural distress.<br>
3. <strong>Location & Depth Criterion:</strong><br>
Must be placed below the depth of topsoil, frost penetration zone, seasonal volume change/shrinkage depth in expansive clays, and maximum scour depth in riverine foundations.<br>
4. <strong>Stability & Durability Criterion:</strong><br>
Must resist lateral sliding, overturning moments, and hydrostatic uplift; foundation concrete and reinforcement must be durable against sulfate and chloride ground attack."""
    },
    {
        "id": "2025-Q4bii",
        "year": "2025",
        "unit": 4,
        "unit_name": "Foundation Engineering & Deep Foundations",
        "q_no": "Q.4 (b) ii",
        "marks": 3,
        "type": "Theory",
        "co": "CO4",
        "bl": "BL3 (Apply)",
        "pi": "4.1.1",
        "topic": "Site-Specific Foundation Selection",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""Two buildings are to be constructed at two different sites. First site shows the low compressive cohesive soil profile up to 10 m depth followed by good quality rock up to 15 m depth below the ground while the second site is having expansive soil up to 5 m depth followed by good rock up to 10 m below the ground. G+4 story building is to be constructed at the first site while at the second site G+15 story building is to be constructed. Suggest the type of foundation at two different sites for the structures to be constructed.""",
        "solution": r"""<strong>1. Foundation Selection for Site 1 (G+4 Building on Soft Clay):</strong><br>
• <strong>Subsoil Profile:</strong> Low compressive strength cohesive soil (soft clay) up to 10 m depth, underlain by good quality rock extending to 15 m.<br>
• <strong>Structure:</strong> Medium-load 5-story frame (G+4).<br>
• <strong>Recommended Foundation:</strong> <strong>End-Bearing Driven Cast-in-Situ or Bored Concrete Piles</strong> (diameter 400-500 mm) terminating and socketed 1-2 m into the sound rock stratum at 10 m depth.<br>
• <em>Alternative:</em> Under-reamed piles if loads are modest, or a compensated raft foundation if settlement analysis allows.<br>
<strong>2. Foundation Selection for Site 2 (G+15 Building on Expansive Soil over Rock):</strong><br>
• <strong>Subsoil Profile:</strong> Highly expansive soil (black cotton clay) up to 5 m depth (active zone of severe seasonal heave/shrinkage), underlain by stable ground and sound rock at 10 m depth.<br>
• <strong>Structure:</strong> Heavy high-rise 16-story tower (G+15) with substantial column loads, moments, and wind shear.<br>
• <strong>Recommended Foundation:</strong> <strong>Large-Diameter Bored Cast-in-Situ Piles (Drilled Shafts / Piers) Socketed into Sound Rock</strong> at 10 m depth.<br>
• <em>Special Protection:</em> Provide sacrificial casing or low-friction bituminous coating through the top 5 m expansive zone to eliminate uplifting drag forces (negative skin friction during swelling) on the pile shaft."""
    },
    {
        "id": "2025-Q4biii",
        "year": "2025",
        "unit": 4,
        "unit_name": "Foundation Engineering & Deep Foundations",
        "q_no": "Q.4 (b) iii",
        "marks": 3,
        "type": "Numerical",
        "co": "CO4",
        "bl": "BL3 (Apply)",
        "pi": "2.1.3",
        "topic": "Immediate Elastic Settlement of Footing",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75%)",
        "question": r"""Using the soil properties (&gamma; = 17.5 kN/m&sup3;, c = 20 kN/m&sup2;, &phi; = 20&deg;), and assuming the square footing (3.415 m x 3.415 m) located at a depth of 1.5 m carries a total load of 2000 kN. Calculate the immediate settlement of the footing using the elastic theory. Assume the soil is homogeneous and isotropic with a Poisson's ratio of 0.3 and Young's modulus of 50,000 kN/m&sup2;. (assume influence factor 0.88 for square footing)""",
        "solution": r"""<strong>Given Parameters:</strong><br>
B = L = 3.415 m, D<sub>f</sub> = 1.5 m, Q = 2000 kN, &mu; = 0.3, E<sub>s</sub> = 50,000 kN/m&sup2;, I<sub>f</sub> = 0.88.<br>
1. <strong>Contact Pressure (q):</strong><br>
<code>q = \frac{Q}{B \times L} = \frac{2000}{3.415 \times 3.415} = \frac{2000}{11.6622} = <strong>171.49 kN/m&sup2;</strong></code><br>
2. <strong>Schleicher's Elastic Theory Equation:</strong><br>
Immediate elastic settlement of a flexible footing:<br>
<code>S_i = \frac{q B (1 - \mu^2)}{E_s} \cdot I_f</code><br>
3. <strong>Step-by-Step Substitution:</strong><br>
<code>1 - \mu^2 = 1 - (0.3)^2 = 1 - 0.09 = 0.91</code><br>
<code>S_i = \frac{171.49 \times 3.415 \times 0.91}{50000} \times 0.88</code><br>
<code>S_i = \frac{532.93}{50000} \times 0.88 = 0.01066 \times 0.88 = <strong>0.00938 m = 9.38 mm</strong></code><br>
<strong>Result:</strong> Immediate settlement S<sub>i</sub> = <strong>9.38 mm</strong> (&le; permissible 25 mm)."""
    },
    {
        "id": "2025-Q4c",
        "year": "2025",
        "unit": 4,
        "unit_name": "Foundation Engineering & Deep Foundations",
        "q_no": "Q.4 (c)",
        "marks": 6,
        "type": "Numerical",
        "co": "CO4",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Design of Square Pile Group in Clay",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Design a square pile group to carry 500 kN load in clay with an unconfined compressive strength of 50 kN/m&sup2;. Assume pile diameter of 400 mm and 6.0 m length. Adhesion factor may be taken as 0.6.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Working load Q<sub>w</sub> = 500 kN, q<sub>u</sub> = 50 kN/m&sup2;, d = 0.4 m, L = 6.0 m, adhesion factor &alpha; = 0.6, FOS = 2.5.<br>
1. <strong>Undrained Cohesion of Clay:</strong><br>
<code>c_u = \frac{q_u}{2} = \frac{50}{2} = <strong>25 kN/m&sup2;</strong></code><br>
2. <strong>Single Pile Ultimate Capacity (Q<sub>up</sub>):</strong><br>
• End bearing: <code>Q_b = 9 c_u A_b = 9(25)\left[\frac{\pi}{4}(0.4)^2\right] = 225(0.1257) = <strong>28.28 kN</strong></code>.<br>
• Skin friction: <code>Q_s = \alpha c_u A_s = 0.6(25)[\pi(0.4)(6.0)] = 15(7.5398) = <strong>113.10 kN</strong></code>.<br>
• Total single pile: <code>Q_{up} = 28.28 + 113.10 = <strong>141.38 kN</strong></code>.<br>
• Safe load per pile: <code>Q_{safe} = \frac{Q_{up}}{FOS} = \frac{141.38}{2.5} = <strong>56.55 kN</strong></code>.<br>
3. <strong>Number of Piles Required (n):</strong><br>
<code>n = \frac{Q_w}{Q_{safe}} = \frac{500}{56.55} = 8.84 \approx 9 \text{ piles}</code>.<br>
Adopt a <strong>3 &times; 3 square group (n = 9 piles)</strong>, or a 4-pile group with larger spacing.<br>
For a 3 &times; 3 group (n = 9):<br>
Spacing s = 3d = 3(0.4) = <strong>1.2 m</strong> center-to-center.<br>
Group width: <code>B_g = 2s + d = 2(1.2) + 0.4 = <strong>2.8 m</strong></code>.<br>
4. <strong>Block Failure Check (Q<sub>ug</sub>):</strong><br>
• Block base: <code>Q_{bg} = 9 c_u B_g^2 = 9(25)(2.8^2) = 225(7.84) = <strong>1764 kN</strong></code>.<br>
• Block perimeter: <code>Q_{sg} = 4 B_g L c_u = 4(2.8)(6.0)(25) = <strong>1680 kN</strong></code>.<br>
• Total block capacity: <code>Q_{ug} = 1764 + 1680 = <strong>3444 kN</strong></code>.<br>
Safe block capacity: <code>\frac{3444}{2.5} = 1377.6 kN \gg 500 kN \quad \text{(Safe)}</code>.<br>
5. <strong>Group Efficiency:</strong><br>
<code>\eta = \frac{Q_{ug}}{n \cdot Q_{up}} = \frac{3444}{9 \times 141.38} = \frac{3444}{1272.4} = 2.70 &gt; 1.0 \implies \eta = 100\%</code>.<br>
Group safe capacity is governed by individual action: 9 &times; 56.55 = <strong>508.95 kN &gt; 500 kN</strong> (Safe)."""
    },
    {
        "id": "2025-Q4c-OR",
        "year": "2025",
        "unit": 4,
        "unit_name": "Foundation Engineering & Deep Foundations",
        "q_no": "Q.4 (c) OR",
        "marks": 6,
        "type": "Numerical",
        "co": "CO4",
        "bl": "BL4 (Analyze)",
        "pi": "2.3.1",
        "topic": "Design of Strip Footing (Width Determination)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""Design a strip footing resting at 2.0 m below the ground and to carrying a load of 1000 kN/m, the shear parameters c = 50 kN/m&sup2; and angle of internal friction is 22&deg; while the density of soil is 20 kN/m&sup3;. The factor of safety to be used is 2.5.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
D<sub>f</sub> = 2.0 m, line load P = 1000 kN/m, c = 50 kN/m&sup2;, &phi; = 22&deg;, &gamma; = 20 kN/m&sup3;, FOS = 2.5.<br>
Since &phi; = 22&deg; &lt; 28&deg;, <strong>local shear failure</strong> governs.<br>
1. <strong>Mobilized Shear Parameters:</strong><br>
<code>c_m = \frac{2}{3} c = \frac{2}{3}(50) = 33.33 kN/m&sup2;</code><br>
<code>\tan\phi_m = \frac{2}{3}\tan 22^\circ = \frac{2}{3}(0.4040) = 0.2693 \implies \phi_m \approx 15.07^\circ</code><br>
2. <strong>Bearing Capacity Factors (Table 1 for &phi; &approx; 15&deg;):</strong><br>
<code>N'_c = 6.49, \quad N'_q = 1.57, \quad N'_\gamma = 0.45</code><br>
3. <strong>Terzaghi Net Ultimate Bearing Capacity for Strip Footing:</strong><br>
<code>q_{nu} = c_m N'_c + \gamma D_f (N'_q - 1) + 0.5 \gamma B N'_\gamma</code><br>
<code>q_{nu} = 33.33(6.49) + 20(2.0)(1.57 - 1) + 0.5(20)(B)(0.45)</code><br>
<code>q_{nu} = 216.31 + 22.80 + 4.50 B = 239.11 + 4.50 B</code><br>
4. <strong>Equating Safe Capacity to Applied Stress:</strong><br>
<code>q_{ns} = \frac{q_{nu}}{FOS} = \frac{239.11 + 4.50 B}{2.5} = 95.64 + 1.80 B</code><br>
Applied net pressure from line load P:<br>
<code>q_{app} = \frac{P}{B} = \frac{1000}{B}</code><br>
Setting q<sub>ns</sub> = q<sub>app</sub>:<br>
<code>95.64 + 1.80 B = \frac{1000}{B} \implies 1.80 B^2 + 95.64 B - 1000 = 0</code><br>
Solving quadratic equation:<br>
<code>B = \frac{-95.64 + \sqrt{95.64^2 - 4(1.80)(-1000)}}{2(1.80)} = \frac{-95.64 + \sqrt{9147.0 + 7200}}{3.60} = \frac{-95.64 + 127.86}{3.60} = \frac{32.22}{3.60} = <strong>8.95 m</strong></code>.<br>
5. <strong>Design Specification:</strong><br>
Provide strip footing of width <strong>B &approx; 9.0 m</strong> (or increase depth D<sub>f</sub> / provide pile foundation to reduce footing width)."""
    },
    {
        "id": "2025-Q5a",
        "year": "2025",
        "unit": 5,
        "unit_name": "Soil Exploration & Testing",
        "q_no": "Q.5 (a)",
        "marks": 3,
        "type": "Theory",
        "co": "CO5",
        "bl": "BL2 (Understand)",
        "pi": "1.3.1",
        "topic": "Soil Samples (Disturbed vs Undisturbed)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Discuss different types of soil samples. How will you obtain undisturbed samples?""",
        "solution": r"""<strong>1. Three Types of Soil Samples:</strong><br>
1. <strong>Non-Representative Disturbed Samples:</strong> Soil structure, moisture, and grain size distribution are all altered; mixture of soils from multiple strata (e.g. wash boring slurry, auger cuttings). Used only for preliminary identification.<br>
2. <strong>Representative Disturbed Samples:</strong> Soil natural structure is broken, but mineralogy, water content, and grain size distribution are fully preserved (e.g. split-spoon sampler). Used for classification, Atterberg limits, and specific gravity.<br>
3. <strong>Undisturbed Samples:</strong> Natural soil fabric, structure, density, void ratio, and moisture content are preserved with minimal disturbance. Essential for shear strength, consolidation, and permeability tests.<br>
<strong>2. How to Obtain Undisturbed Samples:</strong><br>
• <strong>Thin-Walled Sampler (Shelby Tube):</strong> Use seamless thin-walled steel tubes pushed steadily (never hammered) into soft-to-medium cohesive soils.<br>
• <strong>Area Ratio Criterion:</strong> Area ratio must be kept below 10%: <code>A_r = \frac{D_e^2 - D_i^2}{D_i^2} \times 100\% \le 10\%</code>.<br>
• <strong>Clearance Ratios:</strong> Inside clearance C<sub>i</sub> = 0.5% to 1.5% to reduce wall friction; outside clearance C<sub>o</sub> &approx; 0%.<br>
• <strong>Piston Sampler:</strong> For sensitive and soft saturated clays to prevent sample entry before sampling depth and provide vacuum suction during withdrawal.<br>
• <strong>Hand-Cut Block Samples:</strong> Carved directly from open test pits, wrapped in cheesecloth, and sealed with molten paraffin wax."""
    },
    {
        "id": "2025-Q5b",
        "year": "2025",
        "unit": 5,
        "unit_name": "Soil Exploration & Testing",
        "q_no": "Q.5 (b)",
        "marks": 4,
        "type": "Theory",
        "co": "CO5",
        "bl": "BL2 (Understand)",
        "pi": "1.3.1",
        "topic": "Methods of Subsoil Exploration",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""What do you understand by geotechnical exploration? What are the different methods of subsoil explorations?""",
        "solution": r"""<strong>1. Geotechnical Exploration:</strong><br>
The systematic process of acquiring subsurface geological and soil engineering data across a project site to determine soil stratigraphy, ground water table elevation, engineering properties (shear strength, compressibility, permeability), and depth to bedrock for safe, economical foundation design.<br>
<strong>2. Methods of Subsoil Exploration:</strong><br>
1. <strong>Open Test Pits (Trial Pits):</strong> Shallow manual or backhoe excavation up to 3-5 m depth. Enables direct visual examination of soil strata and collection of pristine hand-carved undisturbed block samples.<br>
2. <strong>Auger Boring:</strong> Hand or power-driven helical/post-hole augers advancing in cohesive soils above the water table up to 10-15 m depth.<br>
3. <strong>Wash Boring:</strong> Water jet chopped inside casing pipe. Fast advancement in sands and soft clays; yields disturbed slurry samples.<br>
4. <strong>Rotary Core Drilling:</strong> Rapidly rotating diamond or tungsten core barrel with circulating drilling mud to core medium to hard rock and extract continuous rock cylinders for RQD measurement.<br>
5. <strong>Percussion Drilling:</strong> Heavy chisel bit dropped repeatedly into borehole to pulverize boulders, hardpan, and coarse gravel.<br>
6. <strong>Geophysical Methods:</strong> Non-destructive seismic refraction and electrical resistivity surveys for rapid preliminary reconnaissance across large infrastructure alignments."""
    },
    {
        "id": "2025-Q5c",
        "year": "2025",
        "unit": 5,
        "unit_name": "Soil Exploration & Testing",
        "q_no": "Q.5 (c)",
        "marks": 7,
        "type": "Theory / Numerical",
        "co": "CO5",
        "bl": "BL4 (Analyze)",
        "pi": "4.1.1",
        "topic": "Rock Core Recovery (TCR) & RQD",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers",
        "question": r"""Discuss Rock Mass Rating. How is it useful in finding the bearing capacity of rocks? The drilling carried out in a borehole from 6.00 m to 7.50 m below the ground level shows the 10 rock pieces of size 6, 8, 9, 10, 15, 18, 22 and 32 (all in centimeters). Determine the rock core recovery and rock quality designation. Comment on the quality of rock.""",
        "solution": r"""<strong>1. Rock Mass Rating (RMR - Bieniawski):</strong><br>
A geomechanical classification system that evaluates rock mass quality on a scale of 0 to 100 based on 6 core parameters: Uniaxial compressive strength of intact rock, Rock Quality Designation (RQD), Spacing of discontinuities, Condition of discontinuities (roughness, separation, infilling, weathering), Groundwater conditions, and Joint orientation adjustment. RMR provides empirical correlations for allowable rock bearing capacity, tunnel support, and deformation modulus.<br>
<strong>2. Core Run Calculation:</strong><br>
Drill run length L = 7.50 m - 6.00 m = 1.50 m = <strong>150 cm</strong>.<br>
Sum of all 10 recovered rock core pieces (6, 8, 9, 10, 15, 18, 22, 32 cm + remaining pieces) = <strong>120 cm</strong>.<br>
<strong>Total Core Recovery (TCR):</strong><br>
<code>TCR = \frac{\text{Total length of all recovered core pieces}}{\text{Total drill run length}} \times 100\% = \frac{120}{150} \times 100\% = <strong>80.0\%</strong></code>.<br>
<strong>3. Rock Quality Designation (RQD - Deere):</strong><br>
Only sound core pieces of length &ge; 10 cm are summed:<br>
Core pieces &ge; 10 cm: 10, 15, 18, 22, 32 cm.<br>
<code>\sum L_{pieces \ge 10 cm} = 10 + 15 + 18 + 22 + 32 = <strong>97 cm</strong></code>.<br>
<code>RQD = \frac{\sum L_{pieces \ge 10 cm}}{\text{Total drill run length}} \times 100\% = \frac{97}{150} \times 100\% = <strong>64.67\%</strong></code>.<br>
<strong>4. Comment on Rock Quality:</strong><br>
According to Deere's RQD Engineering Classification:<br>
• &lt; 25%: Very Poor<br>
• 25% - 50%: Poor<br>
• <strong>50% - 75%: Fair</strong><br>
• 75% - 90%: Good<br>
• 90% - 100%: Excellent<br>
Since RQD = <strong>64.67%</strong>, the rock stratum between 6.00 m and 7.50 m is classified as <strong>FAIR QUALITY ROCK</strong>."""
    },
    {
        "id": "2025-Q5c-OR",
        "year": "2025",
        "unit": 5,
        "unit_name": "Soil Exploration & Testing",
        "q_no": "Q.5 (c) OR",
        "marks": 7,
        "type": "Theory / Numerical",
        "co": "CO5",
        "bl": "BL4 (Analyze)",
        "pi": "4.1.1",
        "topic": "SPT Corrections Numerical Across Depths",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Explain the Standard Penetration Test. What are the different corrections to be applied to observed SPT value?<br>Following the observations of Standard Penetration Tests conducted at a site on sandy soil. Find the corrected N values.<br>Depth: 1.50 m, Observed SPT: 12, Density: 15.5 kN/m&sup3;<br>Depth: 3.00 m, Observed SPT: 18, Density: 17.2 kN/m&sup3;<br>Depth: 4.50 m, Observed SPT: 26, Density: 19.0 kN/m&sup3;<br>Depth: 6.00 m, Observed SPT: 32, Density: 20.5 kN/m&sup3;""",
        "solution": r"""<strong>1. Standard Penetration Test (SPT - IS: 2131):</strong><br>
A standard split-spoon sampler (OD 50.8 mm, ID 35 mm) is driven into the bottom of a borehole using a 63.5 kg hammer falling freely from 750 mm height. The sampler is driven 450 mm in three 150 mm increments. The first 150 mm is seating drive (ignored). The sum of blows for the last 300 mm is the <strong>observed N-value</strong>.<br>
<strong>2. Standard Corrections:</strong><br>
• <strong>Overburden Pressure Correction (Liao & Whitman / Peck):</strong><br>
<code>N' = C_N \cdot N_0 = \sqrt{\frac{100}{\sigma'_v}} \cdot N_0 \quad \text{or} \quad N' = N_0 \cdot \frac{350}{\sigma'_v + 70} \quad (\text{for } \sigma'_v \le 280 kPa)</code>.<br>
• <strong>Dilatancy / Water Table Correction:</strong> Applied if N' &gt; 15 in saturated fine sand or silt below the water table:<br>
<code>N'' = 15 + 0.5 (N' - 15)</code>.<br>
<strong>3. Calculation Table for Given Site Data:</strong><br>
<div class="sol-table-wrap">
<table class="sol-table">
<thead>
<tr>
<th>Depth (m)</th>
<th>Density &gamma;</th>
<th>&sigma;'<sub>v</sub> (kPa)</th>
<th>Observed N</th>
<th>C<sub>N</sub> = 350/(&sigma;'<sub>v</sub>+70)</th>
<th>N' = C<sub>N</sub> &times; N</th>
<th>Corrected N (IS: 2131)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1.50 m</strong></td>
<td>15.5 kN/m&sup3;</td>
<td>15.5 &times; 1.5 = <strong>23.25</strong></td>
<td><strong>12</strong></td>
<td>350 / 93.25 = <strong>3.75</strong> (max 2.0) &rarr; 2.0</td>
<td>2.0 &times; 12 = <strong>24</strong></td>
<td><strong>24</strong></td>
</tr>
<tr>
<td><strong>3.00 m</strong></td>
<td>17.2 kN/m&sup3;</td>
<td>23.25 + 17.2(1.5) = <strong>49.05</strong></td>
<td><strong>18</strong></td>
<td>350 / 119.05 = <strong>2.94</strong> (max 2.0) &rarr; 2.0</td>
<td>2.0 &times; 18 = <strong>36</strong></td>
<td><strong>36</strong></td>
</tr>
<tr>
<td><strong>4.50 m</strong></td>
<td>19.0 kN/m&sup3;</td>
<td>49.05 + 19.0(1.5) = <strong>77.55</strong></td>
<td><strong>26</strong></td>
<td>350 / 147.55 = <strong>2.37</strong> (max 2.0) &rarr; 2.0</td>
<td>2.0 &times; 26 = <strong>52</strong></td>
<td><strong>52</strong></td>
</tr>
<tr>
<td><strong>6.00 m</strong></td>
<td>20.5 kN/m&sup3;</td>
<td>77.55 + 20.5(1.5) = <strong>108.30</strong></td>
<td><strong>32</strong></td>
<td>350 / 178.30 = <strong>1.96</strong></td>
<td>1.96 &times; 32 = <strong>63</strong></td>
<td><strong>63</strong></td>
</tr>
</tbody>
</table>
</div><br>
• If water table is present and dilatancy applies (fine sand/silt when N' &gt; 15):<br>
Depth 1.5m: N'' = 15 + 0.5(24 - 15) = <strong>20</strong>.<br>
Depth 3.0m: N'' = 15 + 0.5(36 - 15) = <strong>26</strong>.<br>
Depth 4.5m: N'' = 15 + 0.5(52 - 15) = <strong>34</strong>.<br>
Depth 6.0m: N'' = 15 + 0.5(63 - 15) = <strong>39</strong>."""
    }
]

print(f"Total 2025 questions defined: {len(questions_2025)}")

# Test formatting of all 28
for q in questions_2025:
    fmt = generate_dashboard.format_solution(q['solution'])
    assert len(fmt) > 0, f"Empty format for {q['id']}"
    assert 'sol-item-row' in fmt or 'sol-heading' in fmt or 'sol-step' in fmt or 'sol-table' in fmt, f"No structured row in {q['id']}"

print("All 28 questions passed formatting checks successfully!")
