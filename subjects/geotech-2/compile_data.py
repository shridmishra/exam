import json
import os

# Complete question dataset for Geotechnical Engineering - II (CE 41007 / CE 4107 / CE 4151)
# Derived from 4 examination papers: Nov-Dec 2025, Nov-Dec 2024, Nov-Dec 2023, Dec 2022

questions = [
    {
        "id": '2025-Q1a',
        "year": '2025',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Earth Pressure Types (At-Rest, Active, Passive) & Theories",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
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
        "id": '2025-Q1bi',
        "year": '2025',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b) i',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Retaining Wall Supporting Inclined Non-Cohesive Backfill (Rankine Theory at 10 deg)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q1bii',
        "year": '2025',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b) ii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)",
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
        "id": '2025-Q1biii',
        "year": '2025',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b) iii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Active Earth Pressure Distribution with Water Table & Submerged Cohesive Soil (4.5m Retaining Wall)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q1c',
        "year": '2025',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (c)',
        "marks": 6,
        "type": 'Derivation',
        "co": 'CO1',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Coulomb Sliding Wedge Theory: Maximum Active Earth Pressure Derivation",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q1c-OR',
        "year": '2025',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (c) OR',
        "marks": 6,
        "type": 'Theory / Derivation',
        "co": 'CO1',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Rebhann's Graphical Construction for Active Earth Thrust & Proof",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
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
        "id": '2025-Q2a',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Bearing Capacity Definitions & Terminology Suffixes (Gross, Net, Safe, Allowable)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q2bi',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (b) i',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.3',
        "topic": "Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
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
        "id": '2025-Q2bii',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (b) ii',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Ground Water Table Effect on Ultimate & Safe Bearing Capacity (Theory & 50% Drop)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
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
        "id": '2025-Q2biii',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (b) iii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Square Footing Net Safe Bearing Capacity in Pure Cohesive Clay (qu = 150 kPa, 2.5m Footing)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q2c',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (c)',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)",
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
        "id": '2025-Q2c-OR',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (c) OR',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Rectangular Footing with Biaxial Eccentricity Numerical (3m x 2m, P = 1500 kN, eL = 0.3m, eB = 0.2m)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
<code>FOS = \frac{q_{ult}}{q'_{avg}} = \frac{396.02}{390.63} = <strong>1.01 < 2.5</strong></code>.<br>
<strong>Conclusion:</strong> UNSAFE in shear; footing dimensions must be increased or eccentricity reduced."""
    },
    {
        "id": '2025-Q3a',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Coulomb's Law of Shear Strength & Failure Envelope (tau = c + sigma tan phi)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q3bi',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (b) i',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Shear and Normal Stresses on Failure Plane Numerical (tau = 4 kPa, sigma = 10 kPa)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q3bii',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (b) ii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Triaxial Test Specimen Shear Parameters & Deviator Stress Numerical (38mm Specimen, 100/200 kPa)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q3biii',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (b) iii',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria",
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
        "id": '2025-Q3c',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (c)',
        "marks": 6,
        "type": 'Derivation',
        "co": 'CO3',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Mohr-Coulomb Principal Stress Relationship Derivation (sigma1 vs sigma3)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q3c-OR',
        "year": '2025',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (c) OR',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "CU Triaxial Test Total and Effective Shear Parameters with Pore Water Pressure (Multi-Stage Observations)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q4a',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Types of Shallow Foundations & Strap Footing Sketch",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q4bi',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (b) i',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Requirements of Satisfactory Foundations & Design Criteria (Shear Failure & Settlement)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
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
        "id": '2025-Q4bii',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (b) ii',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '4.1.1',
        "topic": "Site-Specific Foundation Selection for Subsoil Profiles (Compressible Clay vs Expansive Soil)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q4biii',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (b) iii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Immediate Elastic Settlement of Footing Numerical (Square Footing, E = 50,000 kPa, mu = 0.3)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q4c',
        "year": '2025',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (c)',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Design of Square Pile Group in Soft Clay for 500 kN Column Load (qu = 50 kPa, 400mm Dia, 6m Length)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
<code>\eta = \frac{Q_{ug}}{n \cdot Q_{up}} = \frac{3444}{9 \times 141.38} = \frac{3444}{1272.4} = 2.70 > 1.0 \implies \eta = 100\%</code>.<br>
Group safe capacity is governed by individual action: 9 &times; 56.55 = <strong>508.95 kN &gt; 500 kN</strong> (Safe)."""
    },
    {
        "id": '2025-Q4c-OR',
        "year": '2025',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (c) OR',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Strip Footing Width Design in c-phi Soil for 1000 kN/m Column Load",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q5a',
        "year": '2025',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (a)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Soil Samples: Disturbed vs Undisturbed Samples & Methods of Sampling",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q5b',
        "year": '2025',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (b)',
        "marks": 4,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Methods of Subsoil Exploration (Boring, Sounding, Trial Pits, Geophysical)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
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
        "id": '2025-Q5c',
        "year": '2025',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (c)',
        "marks": 7,
        "type": 'Theory / Numerical',
        "co": 'CO5',
        "bl": 'BL4 (Analyze)',
        "pi": '4.1.1',
        "topic": "Rock Mass Rating (RMR) & Core Recovery (TCR / RQD) Numerical",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
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
        "id": '2025-Q5c-OR',
        "year": '2025',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (c) OR',
        "marks": 7,
        "type": 'Theory / Numerical',
        "co": 'CO5',
        "bl": 'BL4 (Analyze)',
        "pi": '4.1.1',
        "topic": "Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections",
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
    },
    {
        "id": '2024-Q1a',
        "year": '2024',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Earth Pressure Types (At-Rest, Active, Passive) & Theories",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""List out the three types of earth pressure by giving examples.""",
        "solution": r"""<strong>Three Types of Earth Pressure with Examples:</strong><br>
1. <strong>Active Earth Pressure:</strong> Pressure exerted by soil when the retaining wall moves away from the backfill.<br>
<em>Example:</em> A retaining wall tilting away from soil.<br>
2. <strong>Passive Earth Pressure:</strong> Resistance offered by soil when the retaining wall moves towards the backfill.<br>
<em>Example:</em> Soil resisting the movement of a sheet pile wall.<br>
3. <strong>Earth Pressure at Rest:</strong> Pressure exerted by soil when the retaining wall does not move.<br>
<em>Example:</em> Basement walls restrained by rigid supports."""
    },
    {
        "id": '2024-Q1b',
        "year": '2024',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Earth Pressure Theories & Assumptions (Rankine vs Coulomb Wedge Theory)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""List out the assumptions of Coulomb's theory.""",
        "solution": r"""<strong>Assumptions of Coulomb's Earth Pressure Theory:</strong><br>
1. Soil is homogeneous and isotropic.<br>
2. Soil is dry and cohesionless.<br>
3. Backfill surface is a plane.<br>
4. Failure surface is a plane passing through the heel of the wall.<br>
5. Wall surface is straight and rigid.<br>
6. Friction develops between the wall and soil.<br>
7. Soil wedge behaves as a rigid body at failure."""
    },
    {
        "id": '2024-Q1c',
        "year": '2024',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (c)',
        "marks": 3,
        "type": 'Derivation',
        "co": 'CO1',
        "bl": 'BL6 (Create/Derive)',
        "pi": '1.4.1',
        "topic": "At-Rest Earth Pressure Coefficient Derivation (K0 = mu / (1 - mu))",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Derive an expression for earth pressure at-rest condition.""",
        "solution": r"""<strong>Derive Expression for Earth Pressure at Rest (3 Marks):</strong><br>
At-rest earth pressure occurs when the retaining wall does not move (zero lateral strain: ε<sub>x</sub> = ε<sub>y</sub> = 0).<br>
1. <strong>Vertical Stress at Depth z:</strong><br>
<code>\sigma_v = \gamma z</code><br>
2. <strong>Horizontal Lateral Stress:</strong><br>
<code>\sigma_h = K_0 \sigma_v = K_0 \gamma z</code><br>
3. <strong>Elastic Theory Derivation:</strong> From 3D Hooke's Law with zero lateral strain:<br>
<code>\varepsilon_x = \frac{1}{E}[\sigma_h - \mu(\sigma_h + \sigma_v)] = 0 \implies K_0 = \frac{\sigma_h}{\sigma_v} = \frac{\mu}{1 - \mu}</code><br>
4. <strong>Using Jaky's Equation (Normally Consolidated Soil):</strong><br>
<code>K_0 = 1 - \sin\phi \implies \sigma_h = (1 - \sin\phi) \gamma z</code><br>
5. <strong>Total Earth Thrust (P<sub>0</sub>) at Wall Height H:</strong><br>
<code>P_0 = \frac{1}{2} K_0 \gamma H^2 = \frac{1}{2} (1 - \sin\phi) \gamma H^2</code><br>
Point of application acts at H/3 above the base."""
    },
    {
        "id": '2024-Q1d',
        "year": '2024',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A gravity retaining wall retains 12 m of a backfill. &gamma; = 18 kN/m&sup3;, &phi; = 30&deg; with a uniform horizontal backfill. Assuming the wall interface to be vertical, determine the magnitude of active and passive earth pressure. Assume the angle of wall friction to be 20&deg;. Determine the point of action also.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Height H = 12 m, &gamma; = 18 kN/m&sup3;, &phi; = 30&deg;, &delta; = 20&deg;, vertical wall face (&alpha; = 90&deg;), horizontal backfill (&beta; = 0&deg;).<br>
<strong>1. Coulomb's Active Pressure Coefficient (K<sub>a</sub>):</strong><br>
<code>K<sub>a</sub> = cos&sup2;&phi; / [ cos &delta; &middot; (1 + &radic;(sin(&phi; + &delta;)sin &phi; / cos &delta;))&sup2; ]</code><br>
<code>sin(&phi;+&delta;) = sin 50&deg; = 0.7660, sin 30&deg; = 0.500, cos 20&deg; = 0.9397</code><br>
<code>&radic;[(0.7660 &times; 0.500) / 0.9397] = &radic;[0.4076] = 0.6384</code><br>
<code>K<sub>a</sub> = cos&sup2; 30&deg; / [0.9397 &times; (1 + 0.6384)&sup2;] = 0.750 / [0.9397 &times; 2.6845] = 0.750 / 2.5228 &approx; 0.2973</code><br>
<strong>Total Active Thrust:</strong><br>
<code>P<sub>a</sub> = 0.5 &middot; K<sub>a</sub> &middot; &gamma; &middot; H&sup2; = 0.5 &times; 0.2973 &times; 18 &times; 12&sup2; = 385.3 kN/m</code><br>
Acting at <strong>H/3 = 12/3 = 4.0 m</strong> above the base, inclined at <strong>&delta; = 20&deg;</strong> downward to the normal.<br>
<strong>2. Coulomb's Passive Pressure Coefficient (K<sub>p</sub>):</strong><br>
<code>K<sub>p</sub> = cos&sup2;&phi; / [ cos &delta; &middot; (1 - &radic;(sin(&phi; + &delta;)sin &phi; / cos &delta;))&sup2; ] = 0.750 / [0.9397 &times; (1 - 0.6384)&sup2;] = 0.750 / [0.9397 &times; 0.1308] &approx; 6.103</code><br>
<strong>Total Passive Thrust:</strong><br>
<code>P<sub>p</sub> = 0.5 &middot; K<sub>p</sub> &middot; &gamma; &middot; H&sup2; = 0.5 &times; 6.103 &times; 18 &times; 144 = 7909.5 kN/m</code><br>
Acting at <strong>4.0 m</strong> above the base, inclined at <strong>&delta; = 20&deg;</strong> upward to the normal."""
    },
    {
        "id": '2024-Q1e-OR',
        "year": '2024',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Battered Retaining Wall with Sloping Backfill Numerical (Coulomb Wedge Theory)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""A retaining wall is battered away from the fill from bottom to top at an angle of 15&deg; with the vertical. Height of the wall is 6 m. The fill slopes upwards at an angle 15&deg; away from the rest of the wall. The friction angle is 30&deg; and wall friction angle is 15&deg;. Using Coulomb's wedge theory, determine the total active and passive thrusts on the wall, per lineal metre assuming &gamma; = 20 kN/m&sup3;.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Height H = 6 m, &gamma; = 20 kN/m&sup3;, &phi; = 30&deg;, &delta; = 15&deg;, backfill slope &beta; = 15&deg;, wall batter &alpha; = 90&deg; - 15&deg; = 75&deg;.<br>
<strong>1. Coulomb Active Thrust:</strong><br>
Use Coulomb's general formula for inclined wall and sloping backfill:<br>
<code>K<sub>a</sub> = sin&sup2;(&alpha; + &phi;) / [ sin&sup2;&alpha; &middot; sin(&alpha; - &delta;) &middot; [1 + &radic;(sin(&phi;+&delta;)sin(&phi;-&beta;) / (sin(&alpha;-&delta;)sin(&alpha;+&beta;)))]&sup2; ]</code><br>
Substituting values yields <code>K<sub>a</sub> &approx; 0.448</code>.<br>
<code>P<sub>a</sub> = 0.5 &middot; K<sub>a</sub> &middot; &gamma; &middot; H&sup2; = 0.5 &times; 0.448 &times; 20 &times; 6&sup2; = 161.3 kN/m</code>.<br>
Line of action is at <strong>H/3 = 2.0 m</strong> above the base, inclined at <strong>&delta; = 15&deg;</strong> to the wall normal.<br>
<strong>2. Coulomb Passive Thrust:</strong><br>
Using Coulomb's passive coefficient with reversed friction signs: <code>K<sub>p</sub> &approx; 4.85</code>.<br>
<code>P<sub>p</sub> = 0.5 &middot; K<sub>p</sub> &middot; &gamma; &middot; H&sup2; = 0.5 &times; 4.85 &times; 20 &times; 36 = 1746.0 kN/m</code>."""
    },
    {
        "id": '2024-Q2a',
        "year": '2024',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Factors Affecting Factor of Safety of Infinite Slope in Clay",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""List the factors affecting the factor of safety of an infinite slope in a clay soil.""",
        "solution": r"""<strong>Factors Affecting Factor of Safety of Infinite Slope in Clay:</strong><br>
1. <strong>Slope Angle (&beta;):</strong> Steeper slope angle increases gravitational shear stress along the slip plane, reducing the factor of safety.<br>
2. <strong>Soil Cohesion (c'):</strong> Cohesion provides the primary shearing resistance in clay; higher cohesion directly increases the factor of safety.<br>
3. <strong>Depth of Slip Plane (H):</strong> In clay slopes, factor of safety decreases with depth because driving weight increases faster than cohesive resistance.<br>
4. <strong>Groundwater Seepage &amp; Pore Pressure:</strong> Seepage creates pore water pressure, reducing effective normal stress and cutting safety by up to 50%.<br>
5. <strong>Unit Weight of Soil (&gamma;):</strong> Higher unit weight of saturated soil increases the downslope driving force."""
    },
    {
        "id": '2024-Q2b',
        "year": '2024',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""What are different types of shear failure? Draw the sketches.""",
        "solution": r"""<strong>Three Types of Shear Failure in Soil:</strong><br>
1. <strong>General Shear Failure:</strong> Occurs in dense sand and stiff clay. Continuous failure surface extends from footing edge to ground surface with distinct soil bulging and sudden tilting.<br>
2. <strong>Local Shear Failure:</strong> Occurs in medium dense sand and medium clay. Failure surfaces terminate within the soil mass, resulting in slight ground heave and gradual settlement.<br>
3. <strong>Punching Shear Failure:</strong> Occurs in loose sand and soft clay. Footing sinks vertically straight down into the soil by perimeter shearing, with zero ground heave and continuous plunging settlement.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Modes of Shear Failure &amp; Rupture Surfaces (Terzaghi / Vesic)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" class="sol-diagram-svg" width="100%" style="max-width:760px;height:auto;display:block;">
    <defs>
      <marker id="mode-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- ==================== PANEL 1: GENERAL SHEAR ==================== -->
    <g transform="translate(15, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">General Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Dense Sand (Dr &gt; 70%)</text>
      
      <!-- Ground Line with Heave -->
      <path d="M 10 110 Q 40 92 75 110 L 155 110 Q 190 92 220 110" fill="none" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="42" y="90" fill="var(--pastel-peach-foreground, #f97316)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">Heave &uarr;</text>
      <text x="185" y="90" fill="var(--pastel-peach-foreground, #f97316)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">&uarr; Heave</text>

      <!-- Footing Block -->
      <rect x="90" y="85" width="50" height="25" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="101" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="52" x2="115" y2="82" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Zone I: Elastic Wedge -->
      <polygon points="90,110 140,110 115,135" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.2" />
      <text x="115" y="124" fill="var(--foreground)" font-size="8.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">I</text>

      <!-- Rupture Surfaces Reaching Ground Surface -->
      <path d="M 115 135 C 75 135, 45 125, 25 110" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      <path d="M 115 135 C 155 135, 185 125, 205 110" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      
      <text x="115" y="165" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Slip surface reaches ground</text>
      <text x="115" y="180" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Pronounced peak; sudden tilting</text>
      <text x="115" y="195" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Very small failure settlement</text>
    </g>

    <!-- ==================== PANEL 2: LOCAL SHEAR ==================== -->
    <g transform="translate(265, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Local Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Medium Sand (30% - 70%)</text>
      
      <!-- Ground Line (Minor Heave) -->
      <path d="M 10 110 Q 55 104 80 110 L 150 110 Q 175 104 220 110" fill="none" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="45" y="96" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="8.5" font-weight="700" font-family="system-ui, sans-serif">Minor</text>

      <!-- Footing Block -->
      <rect x="90" y="85" width="50" height="25" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="101" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="52" x2="115" y2="82" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Zone I: Elastic Wedge -->
      <polygon points="90,110 140,110 115,135" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.2" />

      <!-- Slip Surfaces Terminating Inside Soil -->
      <path d="M 115 135 C 85 135, 65 130, 48 122" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" stroke-dasharray="4 2" />
      <path d="M 115 135 C 145 135, 165 130, 182 122" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" stroke-dasharray="4 2" />
      <circle cx="48" cy="122" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <circle cx="182" cy="122" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      
      <text x="115" y="165" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Slip surfaces end inside soil</text>
      <text x="115" y="180" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; No distinct peak; gradual yield</text>
      <text x="115" y="195" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Significant settlement before yield</text>
    </g>

    <!-- ==================== PANEL 3: PUNCHING SHEAR ==================== -->
    <g transform="translate(515, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Punching Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-lavender-foreground, #a855f7)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Loose Sand (Dr &lt; 30%)</text>
      
      <!-- Ground Line (Zero Heave) -->
      <line x1="10" y1="100" x2="85" y2="100" stroke="var(--foreground)" stroke-width="1.6" />
      <line x1="145" y1="100" x2="220" y2="100" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="115" y="90" fill="var(--muted-foreground)" font-size="8.5" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">No Surface Heave</text>

      <!-- Footing Block Penetrating Deep -->
      <rect x="90" y="100" width="50" height="25" fill="var(--pastel-lavender-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="116" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="58" x2="115" y2="96" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Vertical Shearing Edges -->
      <line x1="90" y1="125" x2="90" y2="175" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2" stroke-dasharray="3 2" />
      <line x1="140" y1="125" x2="140" y2="175" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2" stroke-dasharray="3 2" />

      <text x="115" y="185" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Shearing along vertical edges</text>
      <text x="115" y="200" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Large continuous settlement</text>
      <text x="115" y="215" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; No tilting; soil around undisturbed</text>
    </g>
  </svg>
</div>"""
    },
    {
        "id": '2024-Q2c',
        "year": '2024',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (c)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Explain the classification of shear tests based on drainage condition.""",
        "solution": r"""<strong>Classification of Shear Tests by Drainage Condition:</strong><br>
<span class="is-code-chip">IS: 2720</span><br>
1. <strong>Unconsolidated Undrained (UU / Quick Test):</strong> Drainage valve is kept closed during both cell pressure application and shearing. Water cannot escape. Test is fast (5-10 min) and measures undrained strength (c<sub>u</sub>).<br>
<em>Example:</em> Foundation safety right after fast construction on saturated clay.<br>
2. <strong>Consolidated Undrained (CU Test):</strong> Drainage is allowed during cell pressure (complete consolidation), then the valve is closed during shearing while measuring pore pressure (u). Measures both total and effective parameters.<br>
<em>Example:</em> Sudden reservoir water level drawdown behind an earth dam.<br>
3. <strong>Consolidated Drained (CD / Slow Test):</strong> Drainage is allowed throughout both stages. Shearing is very slow so no excess pore pressure builds up. Measures long-term drained parameters (c', φ').<br>
<em>Example:</em> Long-term permanent stability of clay slopes after many years."""
    },
    {
        "id": '2024-Q2d',
        "year": '2024',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (d)',
        "marks": 7,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Methods for Improving Stability of Slopes & Remedial Measures",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Illustrate different methods for improving the stability of slopes.""",
        "solution": r"""<strong>Methods for Improving Stability of Slopes:</strong><br>
1. <strong>Slope Reshaping (Geometric Method):</strong> Flattening the slope angle, adding horizontal berms/benches, and removing weight from the top (crest) while loading the toe.<br>
2. <strong>Drainage Control (Most Effective):</strong> Providing surface ditches to catch rainwater, and deep horizontal perforated drains to lower the groundwater table and eliminate seepage forces.<br>
3. <strong>Retaining Structures:</strong> Building RCC retaining walls, gabions, or sheet piles at the toe to physically stop sliding.<br>
4. <strong>Soil Nailing &amp; Reinforcement:</strong> Inserting steel rods (soil nails) with shotcrete facing, or placing geogrids in compacted fill slopes.<br>
5. <strong>Bio-Engineering:</strong> Planting deep-rooted grass (vetiver) to bind surface soil and prevent rain erosion."""
    },
    {
        "id": '2024-Q2e-OR',
        "year": '2024',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Triaxial Test Axial & Volumetric Strain with Mohr-Coulomb Parameters (50mm x 100mm Specimen)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""A cylindrical sample of soil of 50 mm in diameter and 100 mm long was subjected to axial and radial effective stresses. When the vertical displacement was 2 mm, the soil failed. The stresses at failure are &sigma;₁ = 280 kPa and &sigma;₃ = 100 kPa. The change in soil volume at failure was 800 mm&sup3;. Determine (a) Axial and volumetric strain at failure (b) Friction angle (c) The inclination of the slip plane to the horizontal.""",
        "solution": r"""<strong>Initial Sample Geometry:</strong><br>
d = 50 mm &rArr; A<sub>0</sub> = (&pi;/4) &times; 50&sup2; = 1963.5 mm&sup2;, L<sub>0</sub> = 100 mm &rArr; V<sub>0</sub> = A<sub>0</sub> &times; L<sub>0</sub> = 196,350 mm&sup3;.<br>
<strong>(a) Strains at Failure:</strong><br>
&bull; Axial Strain &epsilon;<sub>a</sub> = &Delta;L / L<sub>0</sub> = 2 mm / 100 mm = <strong>0.02 (2.0%)</strong>.<br>
&bull; Volumetric Strain &epsilon;<sub>v</sub> = &Delta;V / V<sub>0</sub> = 800 mm&sup3; / 196,350 mm&sup3; = <strong>0.00407 (0.407%)</strong>.<br>
<strong>(b) Friction Angle (&phi;):</strong><br>
For cohesionless soil (c = 0):<br>
<code>&sigma;₁ / &sigma;₃ = tan&sup2;(45&deg; + &phi;/2)</code><br>
<code>280 / 100 = 2.80 &rArr; tan(45&deg; + &phi;/2) = &radic;2.80 = 1.6733</code><br>
<code>45&deg; + &phi;/2 = arctan(1.6733) = 59.14&deg; &rArr; &phi; = 2 &times; (59.14&deg; - 45&deg;) = <strong>28.28&deg;</strong></code>.<br>
<strong>(c) Inclination of Slip Plane to Horizontal:</strong><br>
Slip plane inclination &theta; = 45&deg; + &phi;/2 = <strong>59.14&deg;</strong>."""
    },
    {
        "id": '2024-Q3a',
        "year": '2024',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Requirements of Satisfactory Foundations & Design Criteria (Shear Failure & Settlement)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""List out the major criteria to be satisfied in the design of the foundation.""",
        "solution": r"""<strong>Major Design Criteria for Foundations:</strong><br>
1. <strong>Shear Failure Criterion:</strong> Foundation must have an adequate factor of safety (FOS &ge; 2.5 to 3.0) against shear failure of supporting soil under maximum applied loads.<br>
2. <strong>Settlement Criterion:</strong> Total and differential settlements must stay within safe permissible limits specified by codes (IS: 1904) to prevent structural damage or distortion.<br>
3. <strong>Depth Criterion:</strong> Foundation must be placed at sufficient depth below topsoil, frost line, and seasonal moisture swelling/shrinkage zone (minimum depth &ge; 0.5 m to 1.0 m).<br>
4. <strong>Location &amp; Environmental Safety:</strong> Foundation must be safe against scour from flowing water, erosion, and undermining from adjacent excavations."""
    },
    {
        "id": '2024-Q3b',
        "year": '2024',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Settlement of Foundations (Immediate Elastic, Consolidation & Permissible Limits)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Write brief notes on 'Settlement of foundation'.""",
        "solution": r"""<strong>Settlement of Foundation:</strong><br>
Total foundation settlement consists of three components:<br>
<code>S_{total} = S_i + S_c + S_s</code><br>
1. <strong>Immediate (Elastic) Settlement (S<sub>i</sub>):</strong> Occurs instantly upon load application due to elastic deformation without change in water content.<br>
2. <strong>Primary Consolidation Settlement (S<sub>c</sub>):</strong> Time-dependent settlement in saturated clay caused by the gradual expulsion of pore water under sustained load.<br>
3. <strong>Secondary Settlement (S<sub>s</sub>):</strong> Very slow plastic deformation of soil skeleton occurring after excess pore water pressure has fully dissipated.<br>
4. <strong>Permissible Limits:</strong> Maximum permissible total settlement for isolated footings is 40 mm in sand and 65 mm in clay (per IS: 1904)."""
    },
    {
        "id": '2024-Q3c',
        "year": '2024',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (c)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Modes of Failure in Shallow Foundations (Bearing Capacity, Differential Settlement & Structural)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Explain the failures in the shallow foundations.""",
        "solution": r"""<strong>Failures in Shallow Foundations:</strong><br>
1. <strong>Soil Shear Failure:</strong> General shear (sudden tilting), local shear (gradual sinking), or punching shear (vertical plunge).<br>
2. <strong>Settlement Failure:</strong> Excessive total settlement damages connected pipes; unequal differential settlement causes wall cracks, building tilt, and jammed doors.<br>
3. <strong>Structural Footing Failure:</strong> Footing concrete slab cracks due to excessive upward bending or column punching through the slab."""
    },
    {
        "id": '2024-Q3d',
        "year": '2024',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Plate Load Test Procedure & Housel's Two-Plate Method (Q = Am + Pn)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Two load tests were conducted at a site—one with a 0.5 m square test plate and the other with a 1.0 m square test plate. For a settlement of 25 mm, the loads were found to be 60 kN and 180 kN respectively in the two tests. Determine the allowable bearing pressure of the sand and the load which a square footing, 2 m × 2 m can carry with the settlement not exceeding 25 mm.""",
        "solution": r"""<strong>Housel's Equation:</strong> <code>Q = A &middot; m + P &middot; n</code><br>
where A = plate area, P = plate perimeter, m = perimeter shear resistance factor, n = base resistance factor.<br>
<strong>Test 1 (0.5 m square plate):</strong><br>
A<sub>1</sub> = 0.5 &times; 0.5 = 0.25 m&sup2;, P<sub>1</sub> = 4 &times; 0.5 = 2.0 m, Q<sub>1</sub> = 60 kN.<br>
<code>60 = 0.25 m + 2.0 n \qquad\text{--- (Equation 1)}</code><br>
<strong>Test 2 (1.0 m square plate):</strong><br>
A<sub>2</sub> = 1.0 &times; 1.0 = 1.0 m&sup2;, P<sub>2</sub> = 4 &times; 1.0 = 4.0 m, Q<sub>2</sub> = 180 kN.<br>
<code>180 = 1.0 m + 4.0 n \qquad\text{--- (Equation 2)}</code><br>
Multiply Eq. 1 by 2: <code>120 = 0.5 m + 4.0 n</code>.<br>
Subtract from Eq. 2: <code>60 = 0.5 m &rArr; m = 120 kN/m&sup2;</code>.<br>
Substitute into Eq. 1: <code>60 = 0.25(120) + 2n &rArr; 60 = 30 + 2n &rArr; n = 15 kN/m</code>.<br>
<strong>For Footing (2.0 m &times; 2.0 m):</strong><br>
A = 2 &times; 2 = 4.0 m&sup2;, P = 4 &times; 2 = 8.0 m.<br>
<code>Q<sub>footing</sub> = 4.0(120) + 8.0(15) = 480 + 120 = <strong>600 kN</strong></code>.<br>
<strong>Allowable Bearing Pressure:</strong><br>
<code>q<sub>a</sub> = Q / A = 600 / 4.0 = <strong>150 kN/m&sup2; (150 kPa)</strong></code>."""
    },
    {
        "id": '2024-Q3e-OR',
        "year": '2024',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A strip footing of 2.2 m width is to be founded at a depth of 1.2 m below GL. The soil profile shows the highest possible location of the water table at the site is estimated to be at 0.8 m below GL. The soil profile shows the presence of 0.5 m thick layer of fill material (&gamma; = 14.8 kN/m&sup3;), which is underlain by a deep sand stratum having the following average properties: &phi; = 25&deg;, e = 0.99, G = 2.72, water content above water table = 5%. Determine the safe bearing capacity of the footing with respect to a factor of safety of 2.5.""",
        "solution": r"""<strong>1. Sand Unit Weights:</strong><br>
Moist sand above WT (w = 5% = 0.05):<br>
<code>&gamma; = G(1+w)/(1+e) &middot; &gamma;<sub>w</sub> = 2.72(1.05)/1.99 &times; 9.81 = 14.07 kN/m&sup3;</code>.<br>
Submerged sand below WT:<br>
<code>&gamma;' = (G - 1)/(1 + e) &middot; &gamma;<sub>w</sub> = (2.72 - 1)/(1.99) &times; 9.81 = 8.48 kN/m&sup3;</code>.<br>
<strong>2. Effective Surcharge at Foundation Base (D<sub>f</sub> = 1.2 m):</strong><br>
Fill (0 to 0.5 m): <code>0.5 &times; 14.8 = 7.4 kPa</code>.<br>
Moist sand (0.5 to 0.8 m): <code>0.3 &times; 14.07 = 4.22 kPa</code>.<br>
Submerged sand (0.8 to 1.2 m): <code>0.4 &times; 8.48 = 3.39 kPa</code>.<br>
Total effective surcharge <code>q = 7.4 + 4.22 + 3.39 = 15.01 kN/m&sup2;</code>.<br>
<strong>3. Bearing Capacity (Terzaghi Strip Footing):</strong><br>
For &phi; = 25&deg;: N<sub>q</sub> = 10.66, N<sub>&gamma;</sub> = 10.88, c = 0.<br>
<code>q<sub>ult</sub> = q &middot; N<sub>q</sub> + 0.5 &middot; &gamma;' &middot; B &middot; N<sub>&gamma;</sub></code><br>
<code>q<sub>ult</sub> = (15.01 &times; 10.66) + 0.5 &times; (8.48) &times; 2.2 &times; 10.88 = 160.0 + 101.5 = 261.5 kN/m&sup2;</code>.<br>
<code>q<sub>net_ult</sub> = 261.5 - 15.01 = 246.5 kN/m&sup2;</code>.<br>
<strong>Safe Bearing Capacity (FS = 2.5):</strong><br>
<code>q<sub>safe</sub> = (q<sub>net_ult</sub> / 2.5) + q = (246.5 / 2.5) + 15.01 = 98.6 + 15.01 = <strong>113.61 kN/m&sup2;</strong></code>."""
    },
    {
        "id": '2024-Q4a',
        "year": '2024',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Group Action of Piles (Block Failure vs Individual Failure & Efficiency)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Write short notes on group action of piles.""",
        "solution": r"""<strong>Group Action of Piles:</strong><br>
1. <strong>Group Action:</strong> Piles are installed in clusters connected by a rigid pile cap to transmit heavy structural loads into the ground.<br>
2. <strong>Stress Overlap:</strong> Stress zones of closely spaced individual piles overlap in the soil, which can reduce individual pile efficiency and increase group settlement.<br>
3. <strong>Failure Modes:</strong> A pile group in clay may fail either by individual pile failure (Q<sub>g</sub> = n &middot; Q<sub>u</sub>) or as one large solid block (Q<sub>block</sub>). Design capacity is the lesser of the two.<br>
4. <strong>Group Efficiency (&eta;<sub>g</sub>):</strong> Ratio of group capacity to the sum of individual capacities: &eta;<sub>g</sub> = Q<sub>group</sub> / (n &middot; Q<sub>single</sub>) &times; 100%. In sand &eta;<sub>g</sub> &gt; 100%, while in clay &eta;<sub>g</sub> &le; 100%.<br>
5. <strong>Pile Spacing:</strong> Standard center-to-center spacing is 2.5 to 3.5 times the pile diameter for friction piles."""
    },
    {
        "id": '2024-Q4b',
        "year": '2024',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Under-Reamed Pile Foundations for Expansive Soils (Black Cotton Soils)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Describe about under-reamed pile foundation.""",
        "solution": r"""<strong>Under-Reamed Pile Foundation:</strong><br>
1. <strong>Definition:</strong> Bored cast-in-situ concrete piles with one or more enlarged bulbs (under-reams) along their shaft.<br>
2. <strong>Primary Application:</strong> Specially designed for expansive soils (Black Cotton soil) that undergo severe swelling in monsoon and shrinkage in summer.<br>
3. <strong>Bulb Dimensions:</strong> Bulb diameter is typically 2.0 to 2.5 times the stem diameter, drilled using an under-reaming tool.<br>
4. <strong>Anchorage Mechanism:</strong> The bulb is anchored deep below the active seasonal moisture zone (&gt; 1.5 m to 3.5 m) to resist upward swelling and pullout forces.<br>
5. <strong>Load Capacity:</strong> Enlarged bulb provides a large base bearing area for downward compressive loads and high uplift resistance."""
    },
    {
        "id": '2024-Q4c',
        "year": '2024',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (c)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Open Caisson (Well Foundation) Components, Forces, & Cutting Edge Sketches",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Explain an 'Open Caisson' with a neat sketch showing all the component parts.""",
        "solution": r"""<strong>Open Caisson (Well Foundation) Components:</strong><br>
<strong>Open Caisson:</strong> A hollow box or cylinder structure, open at top and bottom, sunk into riverbeds by dredging soil from inside, then sealed with concrete at the bottom. Used for heavy bridge piers.<br>
1. <strong>Cutting Edge:</strong> Hardened steel angle at bottom to cut soil during sinking.<br>
2. <strong>Well Curb:</strong> Concrete wedge guiding soil into the well.<br>
3. <strong>Steining:</strong> Thick wall providing sinking weight.<br>
4. <strong>Dredge Hole:</strong> Central opening for excavating soil.<br>
5. <strong>Bottom Plug:</strong> Concrete seal placed underwater at founding depth to transfer pier load.<br>
6. <strong>Sand Filling:</strong> Clean sand placed inside well for ballast and stability.<br>
7. <strong>Top Plug:</strong> Concrete slab placed over sand filling.<br>
8. <strong>Well Cap:</strong> Top RCC slab supporting the bridge pier.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Cross-Section of Open Caisson (Well Foundation) Components (IS: 3955)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 415" class="sol-diagram-svg" width="100%" style="max-width:660px;height:auto;display:block;">
    <defs>
      <!-- Concrete Pattern -->
      <pattern id="caisson-concrete" width="14" height="14" patternUnits="userSpaceOnUse">
        <path d="M 0 14 L 14 0" stroke="var(--muted-foreground)" stroke-width="0.6" opacity="0.25" />
        <circle cx="3" cy="3" r="0.6" fill="var(--muted-foreground)" opacity="0.35" />
        <circle cx="10" cy="9" r="0.6" fill="var(--muted-foreground)" opacity="0.35" />
      </pattern>
      <!-- Sand Ballast Pattern -->
      <pattern id="caisson-sand" width="10" height="10" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="0.75" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.5" />
        <circle cx="7" cy="7" r="0.75" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.5" />
      </pattern>
      <!-- Bedrock Pattern -->
      <pattern id="caisson-bedrock" width="14" height="14" patternUnits="userSpaceOnUse">
        <path d="M 0 14 L 14 0 M -2 2 L 2 -2 M 12 16 L 16 12" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="0.8" opacity="0.35" />
      </pattern>
      <marker id="caisson-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- River Water Wash between HFL and River Bed -->
    <rect x="110" y="100" width="145" height="125" fill="var(--pastel-sky-bg)" opacity="0.5" rx="2" />
    <rect x="405" y="100" width="145" height="125" fill="var(--pastel-sky-bg)" opacity="0.5" rx="2" />

    <!-- Water Levels -->
    <line x1="85" y1="100" x2="575" y2="100" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.4" stroke-dasharray="5 3" />
    <text x="580" y="104" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">▽ H.F.L.</text>

    <line x1="85" y1="225" x2="575" y2="225" stroke="var(--muted-foreground)" stroke-width="1.4" stroke-dasharray="4 2" />
    <text x="580" y="229" fill="var(--muted-foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">⏚ River Bed</text>

    <!-- Founding Stratum Bedrock Base -->
    <rect x="110" y="375" width="440" height="28" fill="var(--pastel-sage-bg)" rx="3" />
    <rect x="110" y="375" width="440" height="28" fill="url(#caisson-bedrock)" rx="3" />
    <line x1="85" y1="375" x2="575" y2="375" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="2" stroke-dasharray="6 3" />
    <text x="330" y="394" fill="var(--pastel-sage-foreground, #059669)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Founding Stratum (Hard Rock / Dense Bed)</text>

    <!-- Central Sinking Shaft (Dredge Hole) -->
    <rect x="290" y="52" width="80" height="268" fill="var(--secondary)" opacity="0.6" />

    <!-- Sand Filling (Ballast) - Warm Golden Sand Color -->
    <rect x="290" y="76" width="80" height="188" fill="var(--pastel-sand-bg)" />
    <rect x="290" y="76" width="80" height="188" fill="url(#caisson-sand)" />

    <!-- Bottom Plug (Tremie Concrete Seal) -->
    <path d="M 290 264 Q 330 246 370 264 L 370 320 L 290 320 Z" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.6" />
    <path d="M 290 264 Q 330 246 370 264 L 370 320 L 290 320 Z" fill="url(#caisson-concrete)" />

    <!-- Left Steining Wall -->
    <rect x="255" y="52" width="35" height="268" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <rect x="255" y="52" width="35" height="268" fill="url(#caisson-concrete)" />

    <!-- Right Steining Wall -->
    <rect x="370" y="52" width="35" height="268" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <rect x="370" y="52" width="35" height="268" fill="url(#caisson-concrete)" />

    <!-- Top Plug Concrete Slab -->
    <rect x="290" y="52" width="80" height="24" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.5" />
    <rect x="290" y="52" width="80" height="24" fill="url(#caisson-concrete)" />

    <!-- Left Well Curb (Tapered RCC Wedge) -->
    <polygon points="255,320 290,320 255,362" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <polygon points="255,320 290,320 255,362" fill="url(#caisson-concrete)" />

    <!-- Right Well Curb (Tapered RCC Wedge) -->
    <polygon points="405,320 370,320 405,362" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <polygon points="405,320 370,320 405,362" fill="url(#caisson-concrete)" />

    <!-- Left Cutting Edge (Hardened Steel Shoe) -->
    <polygon points="255,362 268,362 255,376" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1" />

    <!-- Right Cutting Edge (Hardened Steel Shoe) -->
    <polygon points="405,362 392,362 405,376" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1" />

    <!-- Well Cap (Top RCC Slab) - Subtle Peach Tint -->
    <rect x="240" y="28" width="180" height="24" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" rx="3" />
    
    <!-- Superstructure Pier Shaft & Load Q -->
    <rect x="305" y="8" width="50" height="20" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
    <text x="330" y="22" fill="var(--foreground)" font-size="9" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">PIER</text>
    <line x1="330" y1="-2" x2="330" y2="7" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.6" marker-end="url(#caisson-arrow)" />

    <!-- ==================== LEFT CALLOUTS (Clean & Concise) ==================== -->
    <!-- Pier Load -->
    <line x1="185" y1="18" x2="295" y2="18" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" />
    <circle cx="295" cy="18" r="2.5" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="180" y="16" fill="var(--pastel-peach-foreground, #f97316)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Pier Load (Q)</text>
    <text x="180" y="28" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Superstructure Load)</text>

    <!-- Steining Wall -->
    <line x1="185" y1="145" x2="225" y2="145" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="225" y1="145" x2="255" y2="160" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="255" cy="160" r="3" fill="var(--primary)" />
    <text x="180" y="142" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Steining Wall</text>
    <text x="180" y="155" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Massive RCC Self-Weight)</text>

    <!-- Central Dredge Hole -->
    <line x1="185" y1="195" x2="235" y2="195" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="235" y1="195" x2="310" y2="195" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="310" cy="195" r="3" fill="var(--primary)" />
    <text x="180" y="192" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Dredge Hole</text>
    <text x="180" y="205" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Excavation Shaft)</text>

    <!-- Cutting Edge -->
    <line x1="185" y1="362" x2="230" y2="362" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="230" y1="362" x2="255" y2="368" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="255" cy="368" r="3" fill="var(--primary)" />
    <text x="180" y="359" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Cutting Edge</text>
    <text x="180" y="372" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">(Steel Shoe Angle)</text>

    <!-- ==================== RIGHT CALLOUTS (Clean & Concise) ==================== -->
    <!-- Well Cap -->
    <line x1="420" y1="40" x2="470" y2="40" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" />
    <circle cx="420" cy="40" r="2.5" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="475" y="38" fill="var(--pastel-peach-foreground, #f97316)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Well Cap</text>
    <text x="475" y="50" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Top RCC Slab)</text>

    <!-- Top Plug -->
    <line x1="370" y1="64" x2="440" y2="64" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="440" y1="64" x2="470" y2="72" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="370" cy="64" r="3" fill="var(--primary)" />
    <text x="475" y="72" fill="var(--foreground)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Top Plug</text>
    <text x="475" y="85" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Concrete Seal)</text>

    <!-- Sand Filling -->
    <line x1="370" y1="155" x2="435" y2="155" stroke="var(--pastel-sand-foreground, #ca8a04)" stroke-width="1.2" />
    <line x1="435" y1="155" x2="470" y2="155" stroke="var(--pastel-sand-foreground, #ca8a04)" stroke-width="1.2" />
    <circle cx="370" cy="155" r="3" fill="var(--pastel-sand-foreground, #ca8a04)" />
    <text x="475" y="153" fill="var(--pastel-sand-foreground, #ca8a04)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Sand Filling</text>
    <text x="475" y="166" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Ballast &amp; Stability)</text>

    <!-- Bottom Plug -->
    <line x1="370" y1="288" x2="435" y2="288" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="435" y1="288" x2="470" y2="288" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="370" cy="288" r="3" fill="var(--primary)" />
    <text x="475" y="286" fill="var(--foreground)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Bottom Plug</text>
    <text x="475" y="299" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Tremie Concrete Arch)</text>

    <!-- Well Curb -->
    <line x1="405" y1="340" x2="445" y2="340" stroke="var(--foreground)" stroke-width="1.2" />
    <line x1="445" y1="340" x2="470" y2="340" stroke="var(--foreground)" stroke-width="1.2" />
    <circle cx="405" cy="340" r="3" fill="var(--primary)" />
    <text x="475" y="338" fill="var(--foreground)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">Well Curb</text>
    <text x="475" y="351" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">(Tapered RCC Wedge)</text>
  </svg>
</div>"""
    },
    {
        "id": '2024-Q4d',
        "year": '2024',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "9-Pile Group Safe Load Capacity in Soft Clay Numerical (30cm Dia, 9m Length, qu = 90 kPa)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""A square group of 9 piles was driven into soft clay extending to a large depth. The diameter and length of the piles were 30 cm and 9 m respectively. If the unconfined compression strength of the clay is 90 kN/m², and the pile spacing is 90 cm centre to centre, determine the capacity of the pile group? Assume a factor of safety of 2.5 and adhesion factor of 0.75.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Group configuration = 3 &times; 3 = 9 piles, d = 0.30 m, L = 9.0 m, spacing s = 0.90 m, q<sub>u</sub> = 90 kN/m&sup2; &rArr; c = q<sub>u</sub>/2 = 45 kN/m&sup2;, &alpha; = 0.75, FS = 2.5.<br>
<strong>1. Individual Pile Failure Mode (Q<sub>gi</sub>):</strong><br>
Base area A<sub>b</sub> = (&pi;/4)(0.3)&sup2; = 0.07068 m&sup2;.<br>
Surface area A<sub>s</sub> = &pi; &times; 0.3 &times; 9.0 = 8.482 m&sup2;.<br>
Single pile ultimate: <code>Q<sub>u</sub> = 9 c A<sub>b</sub> + &alpha; c A<sub>s</sub></code><br>
<code>Q<sub>u</sub> = 9(45)(0.07068) + 0.75(45)(8.482) = 28.63 + 286.28 = 314.91 kN</code>.<br>
Total for 9 piles: <code>Q<sub>gi</sub> = 9 &times; 314.91 = <strong>2834.2 kN</strong></code>.<br>
<strong>2. Block Failure Mode (Q<sub>gb</sub>):</strong><br>
Block width B = 2s + d = 2(0.9) + 0.3 = 2.1 m.<br>
Block base area A<sub>g</sub> = B&sup2; = 2.1&sup2; = 4.41 m&sup2;.<br>
Block perimeter P<sub>g</sub> = 4B = 4(2.1) = 8.4 m.<br>
<code>Q<sub>gb</sub> = 9 c B&sup2; + c P<sub>g</sub> L = 9(45)(4.41) + 45(8.4)(9.0) = 1786.05 + 3402.0 = <strong>5188.05 kN</strong></code>.<br>
<strong>3. Governing Ultimate & Safe Capacity:</strong><br>
Governing Q<sub>ug</sub> = min(2834.2, 5188.05) = <strong>2834.2 kN</strong> (Individual failure governs).<br>
Safe capacity = 2834.2 / 2.5 = <strong>1133.7 kN</strong>."""
    },
    {
        "id": '2024-Q4e-OR',
        "year": '2024',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Optimum Spacing Derivation for Square Pile Group in Soft Clay (s = d + 2d / (pi * alpha))",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""A 16-pile group has to be arranged in the form of a square in soft clay with uniform spacing. Neglecting end-bearing, determine the optimum value of the spacing of the piles in terms of the pile diameter, assuming a shear mobilisation factor of 0.6.""",
        "solution": r"""<strong>Derivation of Optimum Spacing:</strong><br>
16 piles in square group (4 &times; 4 array). Let d = pile diameter, s = center-to-center spacing, L = pile length, c = clay cohesion, &alpha; = 0.6.<br>
Neglecting end-bearing (friction piles only):<br>
<strong>1. Capacity by Individual Action:</strong><br>
<code>Q<sub>gi</sub> = 16 &middot; (&alpha; &middot; c &middot; &pi; &middot; d &middot; L) = 16 &times; 0.6 &times; &pi; &middot; d &middot; L &middot; c = 9.6 &pi; &middot; d &middot; L &middot; c &approx; 30.16 &middot; d &middot; L &middot; c</code>.<br>
<strong>2. Capacity by Block Action:</strong><br>
Width of block B = 3s + d. Block perimeter P<sub>g</sub> = 4(3s + d).<br>
<code>Q<sub>gb</sub> = P<sub>g</sub> &middot; L &middot; c = 4(3s + d) &middot; L &middot; c</code>.<br>
<strong>3. Equating for Optimum Spacing:</strong><br>
At optimum spacing, individual capacity equals block capacity:<br>
<code>4(3s + d) &middot; L &middot; c = 30.16 &middot; d &middot; L &middot; c</code><br>
<code>12 s + 4 d = 30.16 d &rArr; 12 s = 26.16 d &rArr; s = (26.16 / 12) d &approx; <strong>2.18 d</strong></code>.<br>
Therefore, optimum spacing is <strong>s &approx; 2.2 d</strong>."""
    },
    {
        "id": '2024-Q5a',
        "year": '2024',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Objectives & Purpose of Geotechnical Soil Exploration / Investigation",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""List out the objectives of soil exploration.""",
        "solution": r"""<strong>Objectives of Soil Exploration:</strong><br>
1. To determine the depth, thickness, and extent of each soil and rock stratum across the site.<br>
2. To locate the groundwater table and monitor its seasonal fluctuations.<br>
3. To obtain disturbed and undisturbed soil samples for identification and laboratory testing.<br>
4. To evaluate engineering properties of soil (shear strength, compressibility, permeability, and bearing capacity).<br>
5. To select the most suitable, safe, and economical type and depth of foundation.<br>
6. To identify potential construction hazards (excavation collapse, dewatering requirements, expansive soils)."""
    },
    {
        "id": '2024-Q5b',
        "year": '2024',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Borelog Preparation & Subsoil Profile Documentation",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Sketch a typical borelog and describe its features.""",
        "solution": r"""<strong>Typical Borelog Layout and Features:</strong><br>
1. <strong>Header Information:</strong> Project title, borehole number (BH-01), ground surface elevation (RL), date of boring, and drilling method.<br>
2. <strong>Strata Description:</strong> Layer depth boundaries, thickness, and standard engineering classification/symbols of each stratum.<br>
3. <strong>Groundwater Level:</strong> Exact depth where groundwater table (GWT) was encountered during drilling and stabilized.<br>
4. <strong>Sampling &amp; Field Test Data:</strong> Depth of collected samples, sample type (disturbed/undisturbed), and recorded SPT N-values.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Typical Soil Investigation Borelog Layout (IS: 1892)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 330" class="sol-diagram-svg" width="100%" style="max-width:660px;height:auto;display:block;">
    <defs>
      <!-- Clay Hatch Pattern -->
      <pattern id="bore-clay" width="18" height="10" patternUnits="userSpaceOnUse">
        <line x1="0" y1="5" x2="18" y2="5" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="0.8" stroke-dasharray="6 3" />
      </pattern>
      <!-- Sand Stipple Pattern -->
      <pattern id="bore-sand" width="10" height="10" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="0.7" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.6" />
        <circle cx="7" cy="7" r="0.7" fill="var(--pastel-sand-foreground, #ca8a04)" opacity="0.6" />
      </pattern>
      <!-- Gravel Pattern -->
      <pattern id="bore-gravel" width="20" height="16" patternUnits="userSpaceOnUse">
        <circle cx="5" cy="5" r="2.2" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="0.8" />
        <circle cx="15" cy="11" r="2.5" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="0.8" />
      </pattern>
      <!-- Rock Hatch Pattern -->
      <pattern id="bore-rock" width="14" height="14" patternUnits="userSpaceOnUse">
        <line x1="0" y1="14" x2="14" y2="0" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.2" opacity="0.5" />
      </pattern>
    </defs>

    <!-- Header Information Bar -->
    <rect x="20" y="15" width="620" height="32" fill="var(--secondary)" stroke="var(--card)" stroke-width="1" rx="4" />
    <text x="35" y="35" fill="var(--foreground)" font-size="10.5" font-weight="800" font-family="system-ui, sans-serif">Borehole: BH-01</text>
    <text x="180" y="35" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">Location: Pier P-2</text>
    <text x="310" y="35" fill="var(--foreground)" font-size="10" font-family="system-ui, sans-serif">G.L.: +104.50 m</text>
    <text x="440" y="35" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">GWT: -2.50 m</text>
    <text x="555" y="35" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">IS: 1892</text>

    <!-- Table Header Columns -->
    <g transform="translate(20, 52)">
      <rect x="0" y="0" width="620" height="24" fill="var(--card)" stroke="var(--foreground)" stroke-width="1" />
      <text x="35" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Depth</text>
      <text x="105" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Strata</text>
      <text x="260" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Soil Classification &amp; Parameters</text>
      <text x="490" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">SPT Blow Count N</text>
      <text x="585" y="16" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Sample</text>
      
      <!-- Vertical Dividing Lines -->
      <line x1="70" y1="0" x2="70" y2="225" stroke="var(--foreground)" stroke-width="1" />
      <line x1="140" y1="0" x2="140" y2="225" stroke="var(--foreground)" stroke-width="1" />
      <line x1="420" y1="0" x2="420" y2="225" stroke="var(--foreground)" stroke-width="1" />
      <line x1="550" y1="0" x2="550" y2="225" stroke="var(--foreground)" stroke-width="1" />

      <!-- Layer 1: 0.0 - 2.5 m (Silty Clay - Soft Lavender) -->
      <rect x="70" y="24" width="70" height="48" fill="var(--pastel-lavender-bg)" />
      <rect x="70" y="24" width="70" height="48" fill="url(#bore-clay)" />
      <text x="35" y="52" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">0 - 2.5 m</text>
      <text x="155" y="44" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Firm Brown Silty CLAY (CI)</text>
      <text x="155" y="58" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">LL = 38%, PL = 21%, cu = 45 kPa</text>
      
      <!-- SPT Bar for Layer 1 -->
      <rect x="435" y="38" width="24" height="18" fill="var(--pastel-sky-foreground, #0ea5e9)" rx="2" />
      <text x="470" y="51" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">N = 6</text>
      <text x="585" y="51" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">U1</text>
      <line x1="0" y1="72" x2="620" y2="72" stroke="var(--foreground)" stroke-width="0.8" />

      <!-- Layer 2: 2.5 - 6.0 m (Sand - Warm Gold) -->
      <rect x="70" y="72" width="70" height="52" fill="var(--pastel-sand-bg)" />
      <rect x="70" y="72" width="70" height="52" fill="url(#bore-sand)" />
      <text x="35" y="102" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">2.5 - 6.0 m</text>
      <text x="155" y="93" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Medium Dense Grey SAND (SP-SM)</text>
      <text x="155" y="107" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">Dr &asymp; 48%, &phi; = 32&deg;</text>
      
      <!-- Water Table Marker at -2.5m -->
      <polygon points="345,74 340,82 350,82" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <line x1="335" y1="84" x2="355" y2="84" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.8" />
      <line x1="338" y1="87" x2="352" y2="87" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" />
      <text x="362" y="83" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">GWT -2.5m</text>

      <!-- SPT Bar for Layer 2 -->
      <rect x="435" y="89" width="72" height="18" fill="var(--pastel-sky-foreground, #0ea5e9)" rx="2" />
      <text x="515" y="102" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">N = 18</text>
      <text x="585" y="102" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">D1</text>
      <line x1="0" y1="124" x2="620" y2="124" stroke="var(--foreground)" stroke-width="0.8" />

      <!-- Layer 3: 6.0 - 10.0 m (Gravel & Sand - Warm Peach) -->
      <rect x="70" y="124" width="70" height="52" fill="var(--pastel-peach-bg)" />
      <rect x="70" y="124" width="70" height="52" fill="url(#bore-gravel)" />
      <text x="35" y="154" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">6 - 10 m</text>
      <text x="155" y="145" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Dense SAND &amp; GRAVEL (GW)</text>
      <text x="155" y="159" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">Compacted, Dr &asymp; 76%, &phi; = 38&deg;</text>
      
      <!-- SPT Bar for Layer 3 -->
      <rect x="435" y="141" width="102" height="18" fill="var(--pastel-peach-foreground, #f97316)" rx="2" />
      <text x="515" y="154" fill="var(--foreground)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">N = 34</text>
      <text x="585" y="154" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">D2</text>
      <line x1="0" y1="176" x2="620" y2="176" stroke="var(--foreground)" stroke-width="0.8" />

      <!-- Layer 4: > 10.0 m (Sandstone Bedrock - Sage Green) -->
      <rect x="70" y="176" width="70" height="49" fill="var(--pastel-sage-bg)" />
      <rect x="70" y="176" width="70" height="49" fill="url(#bore-rock)" />
      <text x="35" y="204" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">&gt; 10 m</text>
      <text x="155" y="196" fill="var(--pastel-sage-foreground, #059669)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">Sandstone BEDROCK</text>
      <text x="155" y="210" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">TCR = 85%, RQD = 72% (Sound Rock)</text>
      
      <!-- SPT Refusal Bar -->
      <rect x="435" y="192" width="112" height="18" fill="var(--pastel-peach-foreground, #f97316)" rx="2" />
      <text x="445" y="205" fill="var(--primary-foreground, #ffffff)" font-size="9" font-weight="800" font-family="system-ui, sans-serif">&gt; 50 (Refusal)</text>
      <text x="585" y="205" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">C1</text>
      <line x1="0" y1="225" x2="620" y2="225" stroke="var(--foreground)" stroke-width="1.2" />
    </g>

    <!-- Outer Table Border -->
    <rect x="20" y="52" width="620" height="225" fill="none" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
  </svg>
</div>"""
    },
    {
        "id": '2024-Q5c',
        "year": '2024',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (c)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Soil Sampler Criteria: Area Ratio (Ar), Clearance Ratios (Ci, Co) & Recovery Ratio",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Explain inside clearance, outside clearance and area ratio.""",
        "solution": r"""<strong>Soil Sampler Criteria (IS: 1892):</strong><br>
Let D<sub>1</sub> = inside tip dia, D<sub>2</sub> = outside tip dia, D<sub>3</sub> = inside tube dia, D<sub>4</sub> = outside tube dia.<br>
1. <strong>Area Ratio (A<sub>r</sub>):</strong> Represents volume of soil displaced during driving. For undisturbed samples, A<sub>r</sub> ≤ 10% to 20%.<br>
<code>A_r = \frac{D_2^2 - D_1^2}{D_1^2} \times 100\%</code><br>
2. <strong>Inside Clearance (C<sub>i</sub>):</strong> Allows sample to expand slightly inside tube, reducing wall friction and sticking (1% to 3%).<br>
<code>C_i = \frac{D_3 - D_1}{D_1} \times 100\%</code><br>
3. <strong>Outside Clearance (C<sub>o</sub>):</strong> Reduces friction between soil and outside tube during driving and extraction (0% to 2%).<br>
<code>C_o = \frac{D_2 - D_4}{D_4} \times 100\%</code>"""
    },
    {
        "id": '2024-Q5d',
        "year": '2024',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (d)',
        "marks": 7,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Significant Depth of Exploration for Foundations & Structures",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2024)",
        "question": r"""Describe about the depth of exploration required for various types of structures/foundations.""",
        "solution": r"""<strong>Depth of Exploration Required for Structures (IS: 1892):</strong><br>
1. <strong>Significant Depth:</strong> Exploration must extend down to where vertical stress increase drops to <strong>10% (0.1 q)</strong> of applied contact pressure.<br>
2. <strong>Depth Guidelines:</strong><br>
• <strong>Isolated Footing:</strong> 1.5 B to 2.0 B below base.<br>
• <strong>Raft Foundation:</strong> 1.5 times the raft width (W).<br>
• <strong>Pile Foundation:</strong> 1.5 times pile group width (B<sub>g</sub>) below pile tips, or 5 m into rock.<br>
• <strong>Retaining Wall:</strong> 1.5 times wall height (H).<br>
• <strong>Earth Dam:</strong> 1.0 to 1.5 times dam height.<br>
3. <strong>Borehole Spacing:</strong> Multi-story buildings (15-30 m), Industrial plants (20-60 m), Highways (100-300 m), Dams (25-50 m)."""
    },
    {
        "id": '2024-Q5e-OR',
        "year": '2024',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (e) OR',
        "marks": 7,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Describe a standard penetration test. What are the corrections applied?""",
        "solution": r"""<strong>Standard Penetration Test (SPT) &amp; Required Corrections:</strong><br>
<span class="is-code-chip">IS: 2131</span><br>
1. <strong>Procedure:</strong> Split-spoon sampler (50.8 mm OD, 35 mm ID) driven into borehole bottom by 63.5 kg hammer falling freely from 750 mm height in 3 intervals of 150 mm. First 150 mm is seating drive (ignored). Sum of blows for last 300 mm = <strong>Observed N-value (N<sub>0</sub>)</strong>.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Standard Penetration Test (SPT) Setup per IS: 2131 &amp; Drive Sequence</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 370" class="sol-diagram-svg" width="100%" style="max-width:640px;height:auto;display:block;">
    <defs>
      <marker id="spt-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- ==================== LEFT: FIELD RIG ELEVATION ==================== -->
    <!-- Tripod Legs -->
    <line x1="50" y1="180" x2="165" y2="40" stroke="var(--foreground)" stroke-width="2.5" />
    <line x1="280" y1="180" x2="165" y2="40" stroke="var(--foreground)" stroke-width="2.5" />
    <line x1="165" y1="180" x2="165" y2="40" stroke="var(--muted-foreground)" stroke-width="1.4" stroke-dasharray="4 2" />

    <!-- Crown Pulley -->
    <circle cx="165" cy="40" r="12" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="2" />
    <circle cx="165" cy="40" r="3" fill="var(--foreground)" />

    <!-- Hoisting Rope -->
    <path d="M 153 40 L 153 105" stroke="var(--muted-foreground)" stroke-width="1.8" />
    <path d="M 177 40 L 250 140" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="2 2" />

    <!-- 63.5 kg Donut Drop Hammer - Vivid Coral -->
    <rect x="135" y="92" width="60" height="24" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" rx="3" />
    <text x="165" y="108" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">63.5 kg</text>

    <!-- Free Fall Height Dimension (750 mm) -->
    <line x1="210" y1="92" x2="210" y2="148" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <line x1="205" y1="92" x2="215" y2="92" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <line x1="205" y1="148" x2="215" y2="148" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <text x="220" y="124" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">750 mm</text>

    <!-- Anvil & Drive Head -->
    <rect x="145" y="148" width="40" height="12" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
    <text x="165" y="157" fill="var(--background)" font-size="7.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">ANVIL</text>

    <!-- Ground Level GL -->
    <line x1="30" y1="180" x2="310" y2="180" stroke="var(--foreground)" stroke-width="2" />
    <text x="35" y="174" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Ground Level (&plusmn;0.00)</text>

    <!-- Casing Pipe -->
    <rect x="147" y="180" width="36" height="105" fill="var(--pastel-sky-bg)" opacity="0.4" stroke="var(--foreground)" stroke-width="1.4" />
    <text x="135" y="235" fill="var(--muted-foreground)" font-size="8.5" text-anchor="end" font-family="system-ui, sans-serif">Casing</text>

    <!-- Drill Rods -->
    <line x1="165" y1="160" x2="165" y2="285" stroke="var(--foreground)" stroke-width="3" />

    <!-- Split Spoon Sampler at Borehole Base -->
    <rect x="153" y="285" width="24" height="60" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.6" />
    <polygon points="153,345 165,360 177,345" fill="var(--foreground)" />
    <text x="165" y="320" fill="var(--foreground)" font-size="8" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">IS: 2131</text>

    <!-- ==================== RIGHT: PENETRATION SEQUENCE INSET ==================== -->
    <g transform="translate(340, 25)">
      <rect x="0" y="0" width="280" height="320" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.4" rx="8" />
      
      <text x="140" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Split-Spoon Drive Sequence (450 mm)</text>
      <text x="140" y="38" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">Penetration divided into three 150 mm stages:</text>

      <!-- Stage 1: Seating Drive (0 - 150 mm) -->
      <g transform="translate(18, 52)">
        <rect x="0" y="0" width="45" height="42" fill="var(--secondary)" stroke="var(--muted-foreground)" stroke-width="1.2" rx="3" />
        <text x="22" y="25" fill="var(--muted-foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">150mm</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">0 - 150 mm (Seating Drive)</text>
        <text x="55" y="31" fill="var(--muted-foreground)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; DISCARDED (Disturbed soil)</text>
      </g>

      <!-- Stage 2: First Test Drive (150 - 300 mm) -->
      <g transform="translate(18, 102)">
        <rect x="0" y="0" width="45" height="42" fill="var(--pastel-sky-bg)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.6" rx="3" />
        <text x="22" y="26" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">N1</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">150 - 300 mm (Test Drive 1)</text>
        <text x="55" y="31" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; Record blow count = N1</text>
      </g>

      <!-- Stage 3: Second Test Drive (300 - 450 mm) -->
      <g transform="translate(18, 152)">
        <rect x="0" y="0" width="45" height="42" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.6" rx="3" />
        <text x="22" y="26" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">N2</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">300 - 450 mm (Test Drive 2)</text>
        <text x="55" y="31" fill="var(--pastel-peach-foreground, #f97316)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; Record blow count = N2</text>
      </g>

      <!-- SPT N Formula Badge -->
      <rect x="15" y="206" width="250" height="34" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" rx="5" />
      <text x="140" y="227" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">SPT Blow Count N = N1 + N2</text>

      <!-- Corrections Summary -->
      <text x="15" y="258" fill="var(--foreground)" font-size="9.5" font-weight="800" font-family="system-ui, sans-serif">Standard Corrections:</text>
      <text x="15" y="274" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">1. Overburden: N' = CN &times; N &nbsp;(CN = 350 / (&sigma;' + 70))</text>
      <text x="15" y="290" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">2. Dilatancy (Fine Sand, N'&gt;15): N'' = 15 + 0.5(N' - 15)</text>
    </g>
  </svg>
</div><br>
2. <strong>Correction 1: Overburden Pressure (N'):</strong> Normalizes N for depth confining stress:<br>
<code>N' = N_0 \times \frac{350}{\sigma'_v + 70} \qquad (\sigma'_v \le 280\text{ kPa})</code><br>
3. <strong>Correction 2: Dilatancy / Submergence (N''):</strong> Applied for saturated fine sand/silt below water table when N' &gt; 15:<br>
<code>N'' = 15 + 0.5 (N' - 15)</code>"""
    },
    {
        "id": '2023-Q1a',
        "year": '2023',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL2 (Understand)',
        "pi": '1.3',
        "topic": "Earth Pressure Types (At-Rest, Active, Passive) & Theories",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""What are different Types of Earth Pressure and what are different theories of Earth Pressures?""",
        "solution": r"""<strong>1. Three Types of Lateral Earth Pressure (Based on Wall Movement):</strong><br>
a) <strong>Active Earth Pressure (P<sub>a</sub>):</strong> Lateral pressure exerted by soil when the retaining wall moves <strong>away</strong> from the backfill.<br>
<em>Example:</em> A cantilever retaining wall tilting away from soil.<br>
b) <strong>Passive Earth Pressure (P<sub>p</sub>):</strong> Lateral resistance offered by soil when the retaining wall moves <strong>towards</strong> the backfill.<br>
<em>Example:</em> Soil resisting the movement of an anchor deadman or sheet pile.<br>
c) <strong>Earth Pressure at Rest (P<sub>0</sub>):</strong> Lateral pressure exerted by soil when the retaining wall undergoes <strong>zero lateral movement</strong> (&epsilon;<sub>x</sub> = 0).<br>
<em>Example:</em> Rigid basement walls restrained by floor slabs.<br>
<strong>2. Two Classical Earth Pressure Theories:</strong><br>
a) <strong>Rankine's Theory (1857):</strong> Considers plastic equilibrium of a semi-infinite soil mass, assuming a vertical, smooth (frictionless) wall back.<br>
b) <strong>Coulomb's Wedge Theory (1776):</strong> Considers equilibrium of a planar sliding rigid soil wedge, accounting for wall friction (&delta;) and inclined wall back."""
    },
    {
        "id": '2023-Q1bi',
        "year": '2023',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b) i',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1',
        "topic": "Retaining Wall Supporting Inclined Non-Cohesive Backfill (Rankine Theory at 10 deg)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""A smooth vertical wall, 6 m high supports an inclined non-cohesive backfill (&phi; = 32&deg;; &gamma; = 21 kN/m&sup3;) at an angle 10&deg; with horizontal. Compute the total active & passive pressure at the bottom of wall.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
H = 6 m, &gamma; = 21 kN/m&sup3;, &phi; = 32&deg;, backfill inclination &beta; = 10&deg;, smooth vertical wall.<br>
<strong>1. Rankine Surcharged Coefficients:</strong><br>
<code>cos &beta; = cos 10&deg; = 0.9848, cos &phi; = cos 32&deg; = 0.8480</code><br>
<code>&radic;(cos&sup2;&beta; - cos&sup2;&phi;) = &radic;(0.9698 - 0.7192) = &radic;0.2507 = 0.5007</code><br>
<code>K<sub>a</sub> = cos &beta; [cos &beta; - &radic;(cos&sup2;&beta; - cos&sup2;&phi;)] / [cos &beta; + &radic;(cos&sup2;&beta; - cos&sup2;&phi;)] = 0.9848 [0.9848 - 0.5007] / [0.9848 + 0.5007] = 0.9848(0.4841) / 1.4855 = <strong>0.3210</strong></code>.<br>
<code>K<sub>p</sub> = cos &beta; [cos &beta; + &radic;(cos&sup2;&beta; - cos&sup2;&phi;)] / [cos &beta; - &radic;(cos&sup2;&beta; - cos&sup2;&phi;)] = 0.9848(1.4855) / 0.4841 = <strong>3.0219</strong></code>.<br>
<strong>2. Intensities at Bottom of Wall (z = 6 m):</strong><br>
Active intensity <code>p<sub>a</sub> = K<sub>a</sub> &middot; &gamma; &middot; H = 0.3210 &times; 21 &times; 6 = <strong>40.45 kN/m&sup2;</strong></code>.<br>
Passive intensity <code>p<sub>p</sub> = K<sub>p</sub> &middot; &gamma; &middot; H = 3.0219 &times; 21 &times; 6 = <strong>380.76 kN/m&sup2;</strong></code>."""
    },
    {
        "id": '2023-Q1bii',
        "year": '2023',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b) ii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1',
        "topic": "Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A rough vertical wall of 7.5 m height supports a horizontal backfill. If the angle of internal friction and angle of wall friction are respectively 33&deg; and 12&deg;, compute the passive earth pressure at the bottom of wall. Assume density of 18.5 kN/m&sup3;.""",
        "solution": r"""<strong>Given:</strong> H = 7.5 m, &phi; = 33&deg;, &delta; = 12&deg;, &gamma; = 18.5 kN/m&sup3;, vertical back (&alpha; = 90&deg;), horizontal backfill (&beta; = 0&deg;).<br>
<strong>Coulomb Passive Coefficient K<sub>p</sub>:</strong><br>
<code>K<sub>p</sub> = cos&sup2;&phi; / [ cos &delta; &middot; (1 - &radic;[sin(&phi;+&delta;) &middot; sin &phi; / cos &delta;])&sup2; ]</code><br>
<code>cos 33&deg; = 0.8387 &rArr; cos&sup2; 33&deg; = 0.7034, cos 12&deg; = 0.9781</code><br>
<code>sin(&phi;+&delta;) = sin 45&deg; = 0.7071, sin 33&deg; = 0.5446</code><br>
<code>&radic;[(0.7071 &times; 0.5446)/0.9781] = &radic;[0.3851/0.9781] = &radic;0.3937 = 0.6275</code><br>
<code>K<sub>p</sub> = 0.7034 / [0.9781 &times; (1 - 0.6275)&sup2;] = 0.7034 / [0.9781 &times; 0.1388] = 0.7034 / 0.1358 = <strong>5.180</strong></code>.<br>
<strong>Passive Pressure Intensity at Bottom (z = 7.5 m):</strong><br>
<code>p<sub>p</sub> = K<sub>p</sub> &middot; &gamma; &middot; H = 5.180 &times; 18.5 &times; 7.5 = <strong>718.7 kN/m&sup2;</strong></code>.<br>
(Total passive force P<sub>p</sub> = 0.5 &times; 718.7 &times; 7.5 = 2695.2 kN/m)."""
    },
    {
        "id": '2023-Q1biii',
        "year": '2023',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b) iii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1',
        "topic": "Active Earth Pressure Distribution with Water Table & Submerged Cohesive Soil (4.5m Retaining Wall)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""A retaining wall of 4.5 m height carries a horizontal backfill with c = 35 kN/m², &phi; = 10&deg;; &gamma; = 17.2 kN/m&sup3;. The water table is located at 1.50 m below the ground. Sketch the distribution of active earth pressure. Assume the value of angle of internal friction is 14&deg;; and cohesion c = 50 kN/m² in the submerged condition.""",
        "solution": r"""<strong>Stratification:</strong><br>
&bull; <strong>Zone 1 (0 to 1.5 m, above WT):</strong> c = 35 kPa, &phi; = 10&deg;, &gamma; = 17.2 kN/m&sup3;.<br>
<code>K<sub>a1</sub> = tan&sup2;(45&deg; - 5&deg;) = tan&sup2;(40&deg;) = 0.7041, &radic;K<sub>a1</sub> = 0.8391</code>.<br>
At z = 0: <code>p<sub>a</sub> = 0 - 2(35)(0.8391) = -58.74 kPa (tension)</code>.<br>
Tension crack depth: <code>z<sub>c</sub> = 2c/(&gamma;&radic;K<sub>a1</sub>) = 2(35) / [17.2 &times; 0.8391] = 4.85 m > 1.5 m</code>.<br>
At z = 1.5 m (just above WT): <code>p<sub>a</sub> = (17.2 &times; 1.5 &times; 0.7041) - 58.74 = 18.17 - 58.74 = -40.57 kPa</code>.<br>
&bull; <strong>Zone 2 (1.5 to 4.5 m, submerged):</strong> c = 50 kPa, &phi; = 14&deg;, &gamma;<sub>sat</sub> &approx; 20 kN/m&sup3; &rArr; &gamma;' = 20 - 9.81 = 10.19 kN/m&sup3;.<br>
<code>K<sub>a2</sub> = tan&sup2;(45&deg; - 7&deg;) = tan&sup2;(38&deg;) = 0.6107, &radic;K<sub>a2</sub> = 0.7815</code>.<br>
At z = 4.5 m (effective surcharge &sigma;'<sub>v</sub> = 17.2 &times; 1.5 + 10.19 &times; 3.0 = 25.8 + 30.57 = 56.37 kPa):<br>
Effective soil thrust: <code>&sigma;'<sub>a</sub> = K<sub>a2</sub> &middot; &sigma;'<sub>v</sub> - 2 c &radic;K<sub>a2</sub> = 0.6107(56.37) - 2(50)(0.7815) = 34.43 - 78.15 = -43.72 kPa</code>.<br>
Hydrostatic pore water pressure: <code>u = &gamma;<sub>w</sub> &times; 3.0 = 9.81 &times; 3.0 = +29.43 kPa</code>."""
    },
    {
        "id": '2023-Q1c',
        "year": '2023',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (c)',
        "marks": 6,
        "type": 'Derivation',
        "co": 'CO1',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Coulomb Sliding Wedge Theory: Maximum Active Earth Pressure Derivation",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Derive the condition of maximum active earth pressure from sliding wedge.""",
        "solution": r"""<strong>Condition of Maximum Active Earth Pressure (Sliding Wedge Method):</strong><br>
1. <strong>Forces Acting on Trial Soil Wedge:</strong><br>
• Weight of wedge (W) acting vertically downwards.<br>
• Soil reaction (R) on the slip plane, inclined at angle φ to the normal.<br>
• Active earth thrust (P<sub>a</sub>) on wall, inclined at wall friction angle δ to the normal.<br>
2. <strong>Force Equilibrium (Sine Rule):</strong> From the force triangle of the sliding wedge:<br>
<code>P_a = W \cdot \frac{\sin(\theta - \phi)}{\sin(\theta - \phi + \alpha + \delta)}</code><br>
Where θ is the inclination of the trial failure plane.<br>
3. <strong>Condition for Critical Failure Plane:</strong> The actual failure plane exerts the maximum possible thrust on the wall. Differentiating P<sub>a</sub> with respect to θ and setting to zero:<br>
<code>\frac{dP_a}{d\theta} = 0</code><br>
4. <strong>Result:</strong> For a vertical smooth wall (α = 90°, δ = 0) and level backfill, solving dP<sub>a</sub>/dθ = 0 gives:<br>
<code>\theta_{cr} = 45^\circ + \frac{\phi}{2} \qquad P_a = \frac{1}{2} \gamma H^2 \left(\frac{1 - \sin\phi}{1 + \sin\phi}\right)</code>"""
    },
    {
        "id": '2023-Q1c-OR',
        "year": '2023',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (c) OR',
        "marks": 6,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Rebhann's Graphical Construction for Active Earth Thrust & Proof",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Explain the Rebhann's graphical construction for active earth pressure and prove that it satisfy the condition of maximum earth pressure.""",
        "solution": r"""<strong>Rebhann's Graphical Construction for Active Earth Thrust:</strong><br>
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
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Rebhann's Graphical Construction for Active Thrust (Pa)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 320" class="sol-diagram-svg" width="100%" style="max-width:620px;height:auto;display:block;">
    <defs>
      <marker id="rebhann-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- Backfill Soil Shading -->
    <polygon points="90,80 500,80 500,240 90,240" fill="var(--pastel-sand-bg)" opacity="0.3" />

    <!-- Retaining Wall Stem AB -->
    <polygon points="60,80 90,80 90,240 50,240" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <line x1="90" y1="80" x2="90" y2="240" stroke="var(--foreground)" stroke-width="2.5" />
    
    <!-- Wall Labels A and B -->
    <circle cx="90" cy="80" r="3" fill="var(--foreground)" />
    <text x="82" y="72" fill="var(--foreground)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">A (Crest)</text>
    <circle cx="90" cy="240" r="3" fill="var(--foreground)" />
    <text x="75" y="256" fill="var(--foreground)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">B (Heel)</text>

    <!-- Ground Surface Line AD -->
    <line x1="90" y1="80" x2="520" y2="80" stroke="var(--foreground)" stroke-width="2" />
    <text x="525" y="84" fill="var(--foreground)" font-size="11" font-weight="700" font-family="system-ui, sans-serif">D (Ground Line)</text>

    <!-- Earth Pressure phi-line BL -->
    <line x1="90" y1="240" x2="490" y2="80" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" />
    <circle cx="490" cy="80" r="3" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="495" y="74" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">L (&phi;-line)</text>
    
    <!-- Angle phi arc at B -->
    <path d="M 150 240 A 60 60 0 0 0 144 219" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.8" />
    <text x="158" y="228" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">&phi;</text>

    <!-- Semi-circle on BL as diameter -->
    <path d="M 90 240 A 215 215 0 0 1 490 80" fill="none" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6" />

    <!-- Poncelet Triangle BCD (Radiant Pastel Peach Fill) -->
    <polygon points="90,240 305,154 360,80" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.2" />
    <circle cx="305" cy="154" r="3" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="290" y="152" fill="var(--pastel-peach-foreground, #f97316)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">C</text>

    <!-- Critical Failure Slip Plane BD -->
    <line x1="90" y1="240" x2="360" y2="80" stroke="var(--foreground)" stroke-width="2" stroke-dasharray="5 3" />
    <circle cx="360" cy="80" r="3" fill="var(--foreground)" />
    <text x="360" y="68" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">D (Slip Surface)</text>

    <!-- Perpendicular Line FJ to semi-circle -->
    <line x1="360" y1="80" x2="260" y2="28" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />
    <circle cx="260" cy="28" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="255" y="22" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">F</text>

    <!-- Tangent Arc from F to C -->
    <path d="M 260 28 A 230 230 0 0 1 305 154" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />

    <!-- Active Thrust Vector Pa -->
    <line x1="90" y1="187" x2="160" y2="160" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.6" marker-end="url(#rebhann-arrow)" />
    <text x="165" y="155" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" font-family="system-ui, sans-serif">Pa (at H/3)</text>

    <!-- Formula & Intelligence Card -->
    <g transform="translate(350, 205)">
      <rect x="0" y="0" width="245" height="66" fill="var(--card)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.4" rx="6" />
      <text x="14" y="22" fill="var(--foreground)" font-size="10.5" font-weight="800" font-family="system-ui, sans-serif">Rebhann's Active Thrust:</text>
      <text x="14" y="42" fill="var(--pastel-peach-foreground, #f97316)" font-size="13" font-weight="800" font-family="system-ui, sans-serif">Pa = &gamma; &times; Area(&Delta;BCD)</text>
      <text x="14" y="56" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">Inclined at angle &delta; at H/3 above base</text>
    </g>
  </svg>
</div><br>
4. <strong>Total Active Earth Thrust:</strong><br>
<code>P_a = \gamma \cdot \text{Area}(\triangle BCD) = \frac{1}{2} \gamma \cdot (CD) \cdot h'</code><br>
Acting at H/3 above the base inclined at angle δ to the wall normal."""
    },
    {
        "id": '2023-Q2a',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '1.3',
        "topic": "Bearing Capacity Definitions & Terminology Suffixes (Gross, Net, Safe, Allowable)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""What do you mean by bearing capacity? What are the different suffixes to be used before bearing capacity?""",
        "solution": r"""<strong>Bearing Capacity Definitions and Common Suffixes:</strong><br>
<strong>Bearing Capacity:</strong> The load carrying capacity of soil per unit area without undergoing shear failure or excessive settlement.<br>
1. <strong>Ultimate Bearing Capacity (q<sub>u</sub>):</strong> The minimum gross contact pressure at which the supporting soil fails completely in shear.<br>
2. <strong>Net Ultimate Bearing Capacity (q<sub>net_u</sub>):</strong> The minimum net pressure above overburden pressure causing shear failure: q<sub>net_u</sub> = q<sub>u</sub> - &gamma;D<sub>f</sub>.<br>
3. <strong>Safe Bearing Capacity (q<sub>safe</sub>):</strong> The safe gross pressure on soil with an adequate factor of safety: q<sub>safe</sub> = q<sub>net_u</sub> / FOS + &gamma;D<sub>f</sub>.<br>
4. <strong>Allowable Bearing Capacity (q<sub>a</sub>):</strong> The maximum net pressure permitted on soil considering both shear failure safety and permissible settlement limits."""
    },
    {
        "id": '2023-Q2bi',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (b) i',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '2.1',
        "topic": "Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Describe the three modes of shear failure in soil. Draw load-settlement curves for each mode and explain which type of soil exhibits each failure pattern.""",
        "solution": r"""<strong>Three Modes of Shear Failure &amp; Load-Settlement Behavior:</strong><br>
1. <strong>General Shear Failure:</strong> Dense sand (D<sub>r</sub> &gt; 70%) and stiff clay. Rupture surface extends to ground with surface heave. Curve has a <strong>sharp peak failure load (q<sub>u</sub>)</strong> followed by sudden drop.<br>
2. <strong>Local Shear Failure:</strong> Medium sand (35% &lt; D<sub>r</sub> &lt; 70%). Rupture surface stops within soil mass; slight heave. Curve has <strong>no sharp peak</strong>, showing gradual yield.<br>
3. <strong>Punching Shear Failure:</strong> Loose sand (D<sub>r</sub> &lt; 35%) and soft clay. Footing punches straight down; zero heave. Curve <strong>plunges downward continuously</strong>.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Load-Settlement (q vs s) Curves for Modes of Failure</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 300" class="sol-diagram-svg" width="100%" style="max-width:580px;height:auto;display:block;">
    <defs>
      <marker id="curve-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--foreground)" />
      </marker>
    </defs>

    <!-- Subtle Grid Lines -->
    <line x1="80" y1="190" x2="520" y2="190" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3" />
    <line x1="80" y1="130" x2="520" y2="130" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3" />
    <line x1="80" y1="70" x2="520" y2="70" stroke="var(--muted-foreground)" stroke-width="0.5" stroke-dasharray="2 4" opacity="0.3" />

    <!-- Axes -->
    <line x1="80" y1="250" x2="530" y2="250" stroke="var(--foreground)" stroke-width="1.8" marker-end="url(#curve-arrow)" />
    <line x1="80" y1="250" x2="80" y2="25" stroke="var(--foreground)" stroke-width="1.8" marker-end="url(#curve-arrow)" />

    <text x="535" y="254" fill="var(--foreground)" font-size="11" font-weight="700" font-family="system-ui, sans-serif">Settlement s &rarr;</text>
    <text x="75" y="18" fill="var(--foreground)" font-size="11" font-weight="700" text-anchor="end" font-family="system-ui, sans-serif">Load Intensity q &rarr;</text>

    <!-- Curve 1: General Shear Failure (Sharp Peak qu, Abrupt Plunge) -->
    <path d="M 80 250 C 130 170, 180 75, 230 70 C 260 70, 290 140, 340 180" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="3" />
    
    <!-- Projection Lines for qu -->
    <line x1="80" y1="70" x2="230" y2="70" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" stroke-dasharray="3 3" />
    <line x1="230" y1="70" x2="230" y2="250" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.2" stroke-dasharray="3 3" />
    <circle cx="230" cy="70" r="3.5" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="72" y="73" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">qu</text>
    <text x="230" y="56" fill="var(--pastel-peach-foreground, #f97316)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Peak (qu)</text>

    <!-- Curve 2: Local Shear Failure (Initial Yield qu1, Plastic Stretch) -->
    <path d="M 80 250 C 150 200, 240 145, 310 140 C 380 135, 430 130, 480 125" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.6" />
    <circle cx="310" cy="140" r="3" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="310" y="128" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Yield (qu1)</text>

    <!-- Curve 3: Punching Shear Failure (Continuous Yield, No Peak) -->
    <path d="M 80 250 C 180 235, 300 220, 420 190 C 460 180, 490 170, 520 160" fill="none" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.4" stroke-dasharray="5 3" />
    
    <!-- Legend & Labels -->
    <g transform="translate(290, 22)">
      <rect x="0" y="0" width="260" height="82" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.2" rx="6" />
      
      <!-- Item 1 -->
      <line x1="12" y1="18" x2="35" y2="18" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="3" />
      <text x="42" y="21" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">General Shear (Dense, Dr &gt; 70%)</text>
      
      <!-- Item 2 -->
      <line x1="12" y1="42" x2="35" y2="42" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.6" />
      <text x="42" y="45" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Local Shear (Medium, 30-70%)</text>
      
      <!-- Item 3 -->
      <line x1="12" y1="64" x2="35" y2="64" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.4" stroke-dasharray="4 2" />
      <text x="42" y="67" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Punching Shear (Loose, Dr &lt; 30%)</text>
    </g>
  </svg>
</div><br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Modes of Shear Failure &amp; Rupture Surfaces (Terzaghi / Vesic)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 260" class="sol-diagram-svg" width="100%" style="max-width:760px;height:auto;display:block;">
    <defs>
      <marker id="mode-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- ==================== PANEL 1: GENERAL SHEAR ==================== -->
    <g transform="translate(15, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">General Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Dense Sand (Dr &gt; 70%)</text>
      
      <!-- Ground Line with Heave -->
      <path d="M 10 110 Q 40 92 75 110 L 155 110 Q 190 92 220 110" fill="none" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="42" y="90" fill="var(--pastel-peach-foreground, #f97316)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">Heave &uarr;</text>
      <text x="185" y="90" fill="var(--pastel-peach-foreground, #f97316)" font-size="8.5" font-weight="800" font-family="system-ui, sans-serif">&uarr; Heave</text>

      <!-- Footing Block -->
      <rect x="90" y="85" width="50" height="25" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="101" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="52" x2="115" y2="82" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Zone I: Elastic Wedge -->
      <polygon points="90,110 140,110 115,135" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.2" />
      <text x="115" y="124" fill="var(--foreground)" font-size="8.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">I</text>

      <!-- Rupture Surfaces Reaching Ground Surface -->
      <path d="M 115 135 C 75 135, 45 125, 25 110" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      <path d="M 115 135 C 155 135, 185 125, 205 110" fill="none" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" />
      
      <text x="115" y="165" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Slip surface reaches ground</text>
      <text x="115" y="180" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Pronounced peak; sudden tilting</text>
      <text x="115" y="195" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Very small failure settlement</text>
    </g>

    <!-- ==================== PANEL 2: LOCAL SHEAR ==================== -->
    <g transform="translate(265, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Local Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Medium Sand (30% - 70%)</text>
      
      <!-- Ground Line (Minor Heave) -->
      <path d="M 10 110 Q 55 104 80 110 L 150 110 Q 175 104 220 110" fill="none" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="45" y="96" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="8.5" font-weight="700" font-family="system-ui, sans-serif">Minor</text>

      <!-- Footing Block -->
      <rect x="90" y="85" width="50" height="25" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="101" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="52" x2="115" y2="82" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Zone I: Elastic Wedge -->
      <polygon points="90,110 140,110 115,135" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.2" />

      <!-- Slip Surfaces Terminating Inside Soil -->
      <path d="M 115 135 C 85 135, 65 130, 48 122" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" stroke-dasharray="4 2" />
      <path d="M 115 135 C 145 135, 165 130, 182 122" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" stroke-dasharray="4 2" />
      <circle cx="48" cy="122" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      <circle cx="182" cy="122" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
      
      <text x="115" y="165" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Slip surfaces end inside soil</text>
      <text x="115" y="180" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; No distinct peak; gradual yield</text>
      <text x="115" y="195" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Significant settlement before yield</text>
    </g>

    <!-- ==================== PANEL 3: PUNCHING SHEAR ==================== -->
    <g transform="translate(515, 10)">
      <rect x="0" y="0" width="230" height="235" fill="var(--card)" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="1.4" rx="6" />
      <text x="115" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Punching Shear Failure</text>
      <text x="115" y="38" fill="var(--pastel-lavender-foreground, #a855f7)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Loose Sand (Dr &lt; 30%)</text>
      
      <!-- Ground Line (Zero Heave) -->
      <line x1="10" y1="100" x2="85" y2="100" stroke="var(--foreground)" stroke-width="1.6" />
      <line x1="145" y1="100" x2="220" y2="100" stroke="var(--foreground)" stroke-width="1.6" />
      <text x="115" y="90" fill="var(--muted-foreground)" font-size="8.5" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">No Surface Heave</text>

      <!-- Footing Block Penetrating Deep -->
      <rect x="90" y="100" width="50" height="25" fill="var(--pastel-lavender-bg)" stroke="var(--foreground)" stroke-width="1.6" rx="2" />
      <text x="115" y="116" fill="var(--foreground)" font-size="9.5" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Footing</text>
      <line x1="115" y1="58" x2="115" y2="96" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2.2" marker-end="url(#mode-arrow)" />

      <!-- Vertical Shearing Edges -->
      <line x1="90" y1="125" x2="90" y2="175" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2" stroke-dasharray="3 2" />
      <line x1="140" y1="125" x2="140" y2="175" stroke="var(--pastel-lavender-foreground, #a855f7)" stroke-width="2" stroke-dasharray="3 2" />

      <text x="115" y="185" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Shearing along vertical edges</text>
      <text x="115" y="200" fill="var(--foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">&bull; Large continuous settlement</text>
      <text x="115" y="215" fill="var(--muted-foreground)" font-size="8.5" text-anchor="middle" font-family="system-ui, sans-serif">&bull; No tilting; soil around undisturbed</text>
    </g>
  </svg>
</div>"""
    },
    {
        "id": '2023-Q2bii',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (b) ii',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '2.1',
        "topic": "Ground Water Table Effect on Ultimate & Safe Bearing Capacity (Theory & 50% Drop)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Explain the effect of water table on bearing capacity of soils.""",
        "solution": r"""<strong>Effect of Water Table on Bearing Capacity (IS: 6403):</strong><br>
General equation with correction factors:<br>
<code>q_u = c N_c + \gamma_1 D_f N_q W^*_1 + 0.5 \gamma_2 B N_\gamma W^*_2</code><br>
1. <strong>Case 1 (Water Table at Ground Level):</strong> Entire soil is submerged (γ' ≈ 0.5 γ<sub>sat</sub>). Bearing capacity drops by approximately <strong>50%</strong>.<br>
2. <strong>Case 2 (Water Table Between Ground &amp; Footing Base):</strong> Surcharge term uses weighted unit weight: W*<sub>1</sub> = 0.5 [1 + d<sub>w</sub> / D<sub>f</sub>].<br>
3. <strong>Case 3 (Water Table Below Base within Depth B):</strong> Shear zone is partially submerged: W*<sub>2</sub> = 0.5 [1 + z<sub>w</sub> / B].<br>
4. <strong>Case 4 (Water Table at Depth ≥ D<sub>f</sub> + B):</strong> Water table is below the failure zone; <strong>zero reduction</strong> in bearing capacity."""
    },
    {
        "id": '2023-Q2biii',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (b) iii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL3 (Apply)',
        "pi": '2.1',
        "topic": "Square Footing Net Safe Bearing Capacity in Pure Cohesive Clay (qu = 150 kPa, 2.5m Footing)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Compute the net safe bearing capacity of a square footing of size 2.5 m provided at 2.0 m depth in a purely cohesive soil with Unconfined Shear Strength of 150 kN/m² and density being 18 kN/m&sup3;. Use factor of safety as 2.5.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Square footing B = 2.5 m, D<sub>f</sub> = 2.0 m, &gamma; = 18 kN/m&sup3;, FS = 2.5.<br>
Purely cohesive soil: &phi; = 0&deg;, cohesion <code>c = q<sub>u</sub> / 2 = 150 / 2 = 75 kN/m&sup2;</code>.<br>
<strong>Terzaghi Bearing Capacity Factors for &phi; = 0&deg;:</strong><br>
N<sub>c</sub> = 5.7, N<sub>q</sub> = 1.0, N<sub>&gamma;</sub> = 0.<br>
For a square footing, ultimate bearing capacity:<br>
<code>q<sub>ult</sub> = 1.3 c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> = 1.3(75)(5.7) + (18)(2.0)(1.0) = 555.75 + 36 = 591.75 kN/m&sup2;</code>.<br>
<strong>Net Ultimate Bearing Capacity:</strong><br>
<code>q<sub>nu</sub> = q<sub>ult</sub> - &gamma; D<sub>f</sub> = 555.75 kN/m&sup2;</code>.<br>
<strong>Net Safe Bearing Capacity:</strong><br>
<code>q<sub>ns</sub> = q<sub>nu</sub> / FS = 555.75 / 2.5 = <strong>222.3 kN/m&sup2; (kPa)</strong></code>.<br>
<em>(Using Skempton's N<sub>c</sub> = 6.0(1 + 0.2 D<sub>f</sub>/B) = 6.0(1 + 0.16) = 6.96 &rArr; q<sub>ns</sub> = 6.96 &times; 75 / 2.5 = 208.8 kN/m&sup2;).</em>"""
    },
    {
        "id": '2023-Q2c',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (c)',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A square footing of 3.5 m is resting at 3 m below the ground level. The shear parameters of soil are respectively 40 kN/m² and 12&deg;. The density of soil is 20 kN/m&sup3;. The water table lies at 2 m below the base of footing. Calculate the net safe bearing capacity. Assume factor of safety of 3.0.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
B = 3.5 m, D<sub>f</sub> = 3.0 m, c = 40 kN/m&sup2;, &phi; = 12&deg;, &gamma; = 20 kN/m&sup3;, FS = 3.0.<br>
Water table is at d<sub>w</sub> = 2.0 m below the footing base.<br>
<strong>1. Bearing Capacity Factors (Interpolated for &phi; = 12&deg; from Table 1):</strong><br>
From Table: &phi;=10&deg; &rArr; (N<sub>c</sub>=6.49, N<sub>q</sub>=1.57, N<sub>&gamma;</sub>=0.45); &phi;=15&deg; &rArr; (N<sub>c</sub>=8.35, N<sub>q</sub>=2.47, N<sub>&gamma;</sub>=1.22).<br>
For &phi; = 12&deg;:<br>
<code>N<sub>c</sub> = 6.49 + (2/5)(8.35 - 6.49) = 7.23</code>.<br>
<code>N<sub>q</sub> = 1.57 + (2/5)(2.47 - 1.57) = 1.93</code>.<br>
<code>N<sub>&gamma;</sub> = 0.45 + (2/5)(1.22 - 0.45) = 0.76</code>.<br>
<strong>2. Water Table Correction Factors:</strong><br>
WT is below footing base &rArr; R<sub>w1</sub> = 1.0.<br>
Since d<sub>w</sub> = 2.0 m < B = 3.5 m: <code>R<sub>w2</sub> = 0.5 [1 + (d<sub>w</sub> / B)] = 0.5 [1 + (2.0 / 3.5)] = 0.5 &times; 1.5714 = 0.786</code>.<br>
<strong>3. Terzaghi Equation for Square Footing:</strong><br>
<code>q<sub>ult</sub> = 1.3 c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> &middot; R<sub>w1</sub> + 0.4 &gamma; B N<sub>&gamma;</sub> &middot; R<sub>w2</sub></code><br>
<code>q<sub>ult</sub> = 1.3(40)(7.23) + (20)(3.0)(1.93)(1.0) + 0.4(20)(3.5)(0.76)(0.786)</code><br>
<code>q<sub>ult</sub> = 375.96 + 115.80 + 16.73 = 508.49 kN/m&sup2;</code>.<br>
<strong>4. Net Safe Bearing Capacity:</strong><br>
<code>q<sub>nu</sub> = q<sub>ult</sub> - &gamma; D<sub>f</sub> = 508.49 - (20 &times; 3.0) = 448.49 kN/m&sup2;</code>.<br>
<code>q<sub>ns</sub> = q<sub>nu</sub> / FS = 448.49 / 3.0 = <strong>149.50 kN/m&sup2; (kPa)</strong></code>."""
    },
    {
        "id": '2023-Q2c-OR',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.2 (c) OR',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Rectangular Footing with Biaxial Eccentricity Numerical (3m x 2m, P = 1500 kN, eL = 0.3m, eB = 0.2m)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""A rectangular footing 3 m × 2 m carries a load of 1500 kN with eccentricity of 0.3 m along the length and 0.2 m along the width. The footing is located at 1.5 m depth in soil with c = 20 kN/m², &phi; = 25&deg;, &gamma; = 19 kN/m&sup3;. Calculate the maximum pressure at the base and check for safety.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
L = 3.0 m, B = 2.0 m, Q = 1500 kN, e<sub>L</sub> = 0.3 m, e<sub>B</sub> = 0.2 m, D<sub>f</sub> = 1.5 m, c = 20 kPa, &phi; = 25&deg;, &gamma; = 19 kN/m&sup3;.<br>
<strong>1. Maximum Base Contact Pressure (Elastic Stress Formula):</strong><br>
<code>q<sub>max</sub> = (Q / A) &middot; [ 1 + (6 e<sub>L</sub> / L) + (6 e<sub>B</sub> / B) ]</code><br>
Area A = 3 &times; 2 = 6 m&sup2;.<br>
<code>6 e<sub>L</sub> / L = 6(0.3)/3.0 = 0.60</code>, <code>6 e<sub>B</sub> / B = 6(0.2)/2.0 = 0.60</code>.<br>
<code>q<sub>max</sub> = (1500 / 6) &middot; [ 1 + 0.60 + 0.60 ] = 250 &times; 2.20 = <strong>550.0 kN/m&sup2;</strong></code>.<br>
<code>q<sub>min</sub> = 250 &times; [ 1 - 0.60 - 0.60 ] = -50 kN/m&sup2; (Tension at corner)</code>.<br>
<strong>2. Ultimate Capacity using Meyerhof's Effective Area Method:</strong><br>
Effective dimensions: <code>L' = L - 2 e<sub>L</sub> = 3.0 - 0.6 = 2.4 m</code>, <code>B' = B - 2 e<sub>B</sub> = 2.0 - 0.4 = 1.6 m</code>.<br>
Effective area A' = 2.4 &times; 1.6 = 3.84 m&sup2;.<br>
For &phi; = 25&deg;: N<sub>c</sub> = 20.2, N<sub>q</sub> = 10.66, N<sub>&gamma;</sub> = 10.88.<br>
Compute shape and depth factors; safe load Q<sub>safe</sub> = q<sub>safe</sub> &times; A'. If q<sub>max</sub> &le; q<sub>safe</sub>, the footing is verified safe."""
    },
    {
        "id": '2023-Q3a',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Coulomb's Law of Shear Strength & Failure Envelope (tau = c + sigma tan phi)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Discuss Coulomb's law of shear strength of soil.""",
        "solution": r"""<strong>Coulomb's Law of Shear Strength of Soil:</strong><br>
1. <strong>Total Stress Equation (Coulomb, 1776):</strong> Shear strength (&tau;) consists of cohesive resistance and frictional resistance:<br>
<code>\tau = c + \sigma \tan\phi</code><br>
where c = cohesion, &sigma; = total normal stress on failure plane, &phi; = angle of internal friction.<br>
2. <strong>Effective Stress Equation (Terzaghi, 1925):</strong> Shear strength is governed by effective stress between soil grains:<br>
<code>\tau = c' + \sigma' \tan\phi' = c' + (\sigma - u) \tan\phi'</code><br>
where c' = effective cohesion, &sigma;' = effective normal stress, u = pore water pressure, &phi;' = effective friction angle.<br>
3. <strong>Special Cases:</strong><br>
• Pure Sand (c = 0): &tau; = &sigma; tan&phi;<br>
• Saturated Clay in Undrained Shear (&phi; = 0): &tau; = c<sub>u</sub>"""
    },
    {
        "id": '2023-Q3bi',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (b) i',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Shear and Normal Stresses on Failure Plane Numerical (tau = 4 kPa, sigma = 10 kPa)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""The shear stress and normal stress at a failure plane in a cohesionless soil mass were found to be 4 kPa and 10 kPa respectively. Determine the resultant stress on failure plane and inclination of failure plane. Also compute the shear parameters.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Cohesionless soil &rArr; c = 0. Normal stress &sigma; = 10 kPa, Shear stress &tau; = 4 kPa.<br>
<strong>1. Resultant Stress on Failure Plane:</strong><br>
<code>R = &radic;(&sigma;&sup2; + &tau;&sup2;) = &radic;(10&sup2; + 4&sup2;) = &radic;(100 + 16) = &radic;116 = <strong>10.77 kPa</strong></code>.<br>
<strong>2. Shear Parameters:</strong><br>
Since c = 0: <code>&tau; = &sigma; tan &phi; &rArr; tan &phi; = &tau; / &sigma; = 4 / 10 = 0.40</code>.<br>
<code>&phi; = arctan(0.40) = <strong>21.80&deg;</strong></code>, and <code>c = 0</code>.<br>
<strong>3. Inclination of Failure Plane with Major Principal Plane (&theta;):</strong><br>
<code>&theta; = 45&deg; + &phi;/2 = 45&deg; + (21.80&deg;/2) = 45&deg; + 10.90&deg; = <strong>55.90&deg;</strong></code>."""
    },
    {
        "id": '2023-Q3bii',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (b) ii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Triaxial Test Specimen Shear Parameters & Deviator Stress Numerical (38mm Specimen, 100/200 kPa)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""The deviator force to shear the soil specimen of 38 mm diameter and 76 mm height under a confining pressure of 100 kN/m² is 251 N while it shears under a deviator force of 327 N at a confining pressure of 200 kN/m². The deformation at the time of failure is respectively 2.0 mm and 5.2 mm. Determine the shear parameters. Determine the deviator stress under a confining pressure of 250 kPa.""",
        "solution": r"""<strong>Initial Dimensions:</strong><br>
d = 38 mm &rArr; A<sub>0</sub> = (&pi;/4)(0.038)&sup2; = 1.134 &times; 10⁻&sup3; m&sup2;, L<sub>0</sub> = 76 mm.<br>
<strong>Test 1 (&sigma;₃ = 100 kPa):</strong><br>
&Delta;L₁ = 2.0 mm &rArr; &epsilon;₁ = 2.0/76 = 0.02632.<br>
Corrected Area A₁ = A<sub>0</sub>/(1 - &epsilon;₁) = 1.134 &times; 10⁻&sup3; / (1 - 0.02632) = 1.1647 &times; 10⁻&sup3; m&sup2;.<br>
Deviator stress: <code>&sigma;<sub>d1</sub> = 251 &times; 10^{-3} kN / (1.1647 &times; 10^{-3} m&sup2;) = 215.5 kPa</code>.<br>
Major principal stress: <code>&sigma;₁ = 100 + 215.5 = 315.5 kPa</code>.<br>
<strong>Test 2 (&sigma;₃ = 200 kPa):</strong><br>
&Delta;L₂ = 5.2 mm &rArr; &epsilon;₂ = 5.2/76 = 0.06842.<br>
Corrected Area A₂ = 1.134 &times; 10⁻&sup3; / (1 - 0.06842) = 1.2173 &times; 10⁻&sup3; m&sup2;.<br>
Deviator stress: <code>&sigma;<sub>d2</sub> = 327 &times; 10^{-3} / (1.2173 &times; 10^{-3}) = 268.6 kPa</code>.<br>
Major principal stress: <code>&sigma;₁ = 200 + 268.6 = 468.6 kPa</code>.<br>
<strong>Solve for Shear Parameters:</strong><br>
<code>&sigma;₁ = &sigma;₃ tan&sup2;(45&deg; + &phi;/2) + 2c tan(45&deg; + &phi;/2)</code>.<br>
Subtracting equations: <code>(468.6 - 315.5) = (200 - 100) N<sub>&phi;</sub> &rArr; 153.1 = 100 N<sub>&phi;</sub> &rArr; N<sub>&phi;</sub> = 1.531</code>.<br>
<code>tan(45&deg; + &phi;/2) = &radic;1.531 = 1.2373 &rArr; 45&deg; + &phi;/2 = 51.05&deg; &rArr; <strong>&phi; = 12.1&deg;</strong></code>.<br>
From Test 1: <code>315.5 = 100(1.531) + 2c(1.2373) &rArr; 162.4 = 2.4746 c &rArr; <strong>c = 65.63 kPa</strong></code>.<br>
<strong>At &sigma;₃ = 250 kPa:</strong><br>
<code>&sigma;₁ = 250(1.531) + 2(65.63)(1.2373) = 382.75 + 162.4 = 545.15 kPa</code>.<br>
Deviator stress: <code>&sigma;<sub>d</sub> = &sigma;₁ - &sigma;₃ = 545.15 - 250 = <strong>295.15 kPa</strong></code>."""
    },
    {
        "id": '2023-Q3biii',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (b) iii',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Explain various kinds of triaxial tests. Which test is best suited for the cohesive soil deposit having a permeable layer immediately below the foundation level?""",
        "solution": r"""<strong>Kinds of Triaxial Tests &amp; Suitability for Saturated Clay:</strong><br>
<span class="is-code-chip">IS: 2720</span><br>
1. <strong>UU Test:</strong> No drainage allowed. Fast test (5-10 min). Gives undrained strength c<sub>u</sub>.<br>
2. <strong>CU Test:</strong> Consolidation allowed, then sheared undrained while measuring pore pressure u.<br>
3. <strong>CD Test:</strong> Drainage allowed in both stages. Very slow test (days to weeks).<br>
4. <strong>Best Test for Saturated Clay:</strong><br>
• <strong>Consolidated Undrained (CU) Test with pore pressure measurement.</strong><br>
• <strong>Reason:</strong> Saturated clay has low permeability, so a drained CD test takes weeks. The CU test allows consolidation, then shears quickly while measuring pore pressure u, giving <strong>both total and effective parameters (c', φ')</strong> in just one day."""
    },
    {
        "id": '2023-Q3c',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (c)',
        "marks": 6,
        "type": 'Derivation',
        "co": 'CO3',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "Mohr-Coulomb Principal Stress Relationship Derivation (sigma1 vs sigma3)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Derive a relationship between effective shear parameters and principal stresses.""",
        "solution": r"""<strong>Relationship Between Effective Shear Parameters &amp; Principal Stresses:</strong><br>
1. <strong>Mohr Circle Geometry at Failure:</strong><br>
• Center: C = ((σ'<sub>1</sub> + σ'<sub>3</sub>) / 2, 0)<br>
• Radius: R = (σ'<sub>1</sub> - σ'<sub>3</sub>) / 2<br>
2. <strong>Right Triangle Relationship:</strong> In the right triangle formed by radius R and failure envelope inclined at φ' with intercept c':<br>
<code>\sin\phi' = \frac{\text{Radius}}{\text{Hypotenuse}} = \frac{\frac{\sigma'_1 - \sigma'_3}{2}}{\frac{c'}{\tan\phi'} + \frac{\sigma'_1 + \sigma'_3}{2}}</code><br>
3. <strong>Simplifying:</strong> Multiplying terms and grouping σ'<sub>1</sub> and σ'<sub>3</sub>:<br>
<code>\sigma'_1(1 - \sin\phi') = \sigma'_3(1 + \sin\phi') + 2c'\cos\phi'</code><br>
4. <strong>Final Equation:</strong> Dividing by (1 - sinφ'):<br>
<code>\sigma'_1 = \sigma'_3 \tan^2\left(45^\circ + \frac{\phi'}{2}\right) + 2c'\tan\left(45^\circ + \frac{\phi'}{2}\right)</code>"""
    },
    {
        "id": '2023-Q3c-OR',
        "year": '2023',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.3 (c) OR',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL4 (Analyze)',
        "pi": '2.3.1',
        "topic": "CU Triaxial Test Total and Effective Shear Parameters with Pore Water Pressure (Multi-Stage Observations)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""The following data refers to triaxial compression tests performed on a soil sample. Determine the total and effective shear parameters of soil.
Observation 1: Cell Pressure = 80 kPa, Max Deviator Stress = 175 kPa, Pore Pressure at failure = 45 kPa.
Observation 2: Cell Pressure = 150 kPa, Max Deviator Stress = 240 kPa, Pore Pressure at failure = 50 kPa.
Observation 3: Cell Pressure = 300 kPa, Max Deviator Stress = 300 kPa, Pore Pressure at failure = 60 kPa.""",
        "solution": r"""<strong>1. Compilation of Stress States:</strong><br>
&bull; <strong>Test 1:</strong> &sigma;₃ = 80 kPa, &sigma;₁ = 80 + 175 = 255 kPa, u = 45 kPa &rArr; &sigma;'₃ = 80 - 45 = 35 kPa, &sigma;'₁ = 255 - 45 = 210 kPa.<br>
&bull; <strong>Test 2:</strong> &sigma;₃ = 150 kPa, &sigma;₁ = 150 + 240 = 390 kPa, u = 50 kPa &rArr; &sigma;'₃ = 150 - 50 = 100 kPa, &sigma;'₁ = 390 - 50 = 340 kPa.<br>
&bull; <strong>Test 3:</strong> &sigma;₃ = 300 kPa, &sigma;₁ = 300 + 300 = 600 kPa, u = 60 kPa &rArr; &sigma;'₃ = 300 - 60 = 240 kPa, &sigma;'₁ = 600 - 60 = 540 kPa.<br>
<strong>2. Effective Shear Parameters (c', &phi;'):</strong><br>
Using Tests 1 and 2: <code>&Delta;&sigma;'₁ / &Delta;&sigma;'₃ = (340 - 210) / (100 - 35) = 130 / 65 = 2.0 = N<sub>&phi;'</sub></code>.<br>
<code>tan(45&deg; + &phi;'/2) = &radic;2.0 = 1.414 &rArr; 45&deg; + &phi;'/2 = 54.74&deg; &rArr; <strong>&phi;' = 19.5&deg;</strong></code>.<br>
Substitute into Test 1: <code>210 = 35(2.0) + 2 c'(1.414) &rArr; 140 = 2.828 c' &rArr; <strong>c' = 49.5 kPa</strong></code>.<br>
<strong>3. Total Shear Parameters (c, &phi;):</strong><br>
Using Tests 1 and 2: <code>&Delta;&sigma;₁ / &Delta;&sigma;₃ = (390 - 255) / (150 - 80) = 135 / 70 = 1.928 = N<sub>&phi;</sub></code>.<br>
<code>tan(45&deg; + &phi;/2) = &radic;1.928 = 1.3887 &rArr; 45&deg; + &phi;/2 = 54.24&deg; &rArr; <strong>&phi; = 18.5&deg;</strong></code>.<br>
Substitute into Test 1: <code>255 = 80(1.928) + 2 c(1.3887) &rArr; 100.7 = 2.777 c &rArr; <strong>c = 36.26 kPa</strong></code>."""
    },
    {
        "id": '2023-Q4a',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL2 (Understand)',
        "pi": '1.3.1',
        "topic": "Types of Shallow Foundations & Strap Footing Sketch",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""What are different types of shallow foundations? Draw neat sketch of strap footing.""",
        "solution": r"""<strong>Types of Shallow Foundations and Strap Footing:</strong><br>
1. <strong>Types of Shallow Foundations:</strong><br>
• Isolated column footing (pad, stepped, sloped)<br>
• Strip or continuous wall footing<br>
• Combined footing (rectangular or trapezoidal)<br>
• Strap (cantilever) footing<br>
• Raft (mat) foundation<br>
2. <strong>Strap Footing Concept:</strong><br>
• Used when an exterior column sits on a property line and its footing cannot extend outward.<br>
• A rigid RCC strap beam connects the eccentric exterior footing to an adjacent interior footing to prevent overturning.<br>
• The strap beam is suspended above ground (no contact with soil underneath) so it transfers bending moment and shear only.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Elevation &amp; Structural Action of Strap (Cantilever) Footing</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 280" class="sol-diagram-svg" width="100%" style="max-width:640px;height:auto;display:block;">
    <defs>
      <marker id="strap-arrow-up" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 9 L 5 0 L 10 9 z" fill="var(--pastel-sage-foreground, #059669)" />
      </marker>
      <marker id="strap-arrow-down" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--foreground)" />
      </marker>
    </defs>

    <!-- Property Line Boundary Limit -->
    <line x1="80" y1="15" x2="80" y2="245" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" stroke-dasharray="6 3" />
    <text x="75" y="32" fill="var(--pastel-peach-foreground, #f97316)" font-size="10.5" font-weight="800" text-anchor="end" font-family="system-ui, sans-serif">Property Line</text>
    <text x="75" y="46" fill="var(--muted-foreground)" font-size="8.5" text-anchor="end" font-family="system-ui, sans-serif">(Boundary Limit)</text>

    <!-- Ground Line -->
    <line x1="60" y1="95" x2="600" y2="95" stroke="var(--foreground)" stroke-width="1.4" />
    <text x="595" y="88" fill="var(--muted-foreground)" font-size="9" text-anchor="end" font-family="system-ui, sans-serif">Ground Level (G.L.)</text>

    <!-- Exterior Column C1 (Flush with Property Line) -->
    <rect x="80" y="35" width="28" height="95" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <text x="94" y="65" fill="var(--foreground)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">C1</text>
    <line x1="94" y1="10" x2="94" y2="33" stroke="var(--foreground)" stroke-width="2.2" marker-end="url(#strap-arrow-down)" />
    <text x="94" y="8" fill="var(--foreground)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">P1</text>

    <!-- Exterior Eccentric Footing -->
    <rect x="80" y="130" width="85" height="32" fill="var(--pastel-peach-bg)" stroke="var(--foreground)" stroke-width="1.8" rx="2" />
    <text x="122" y="150" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Footing 1</text>

    <!-- Interior Column C2 (Concentric) -->
    <rect x="470" y="35" width="30" height="95" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <text x="485" y="65" fill="var(--foreground)" font-size="10.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">C2</text>
    <line x1="485" y1="10" x2="485" y2="33" stroke="var(--foreground)" stroke-width="2.2" marker-end="url(#strap-arrow-down)" />
    <text x="485" y="8" fill="var(--foreground)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">P2</text>

    <!-- Interior Footing (Larger & Concentric) -->
    <rect x="415" y="130" width="140" height="32" fill="var(--pastel-sky-bg)" stroke="var(--foreground)" stroke-width="1.8" rx="2" />
    <text x="485" y="150" fill="var(--foreground)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Footing 2 (Concentric)</text>

    <!-- Rigid Strap (Cantilever) Beam - Prominent Tint -->
    <rect x="80" y="115" width="475" height="26" fill="var(--pastel-sky-bg)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2.2" rx="3" />
    <text x="290" y="132" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">RIGID STRAP BEAM</text>

    <!-- Air Gap / No Soil Contact Note -->
    <line x1="170" y1="145" x2="410" y2="145" stroke="var(--muted-foreground)" stroke-width="1" stroke-dasharray="3 3" opacity="0.6" />
    <text x="290" y="162" fill="var(--muted-foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Air Gap / No Soil Reaction on Strap</text>

    <!-- Upward Soil Reactions q1 under Footing 1 (Vibrant Green) -->
    <line x1="95" y1="195" x2="95" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="122" y1="195" x2="122" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="150" y1="195" x2="150" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <text x="122" y="210" fill="var(--pastel-sage-foreground, #059669)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Uniform q1</text>

    <!-- Upward Soil Reactions q2 under Footing 2 -->
    <line x1="435" y1="195" x2="435" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="468" y1="195" x2="468" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="502" y1="195" x2="502" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <line x1="535" y1="195" x2="535" y2="165" stroke="var(--pastel-sage-foreground, #059669)" stroke-width="1.8" marker-end="url(#strap-arrow-up)" />
    <text x="485" y="210" fill="var(--pastel-sage-foreground, #059669)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Uniform q2</text>

    <!-- Structural Action Callout Card -->
    <g transform="translate(130, 222)">
      <rect x="0" y="0" width="380" height="45" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.2" rx="6" />
      <text x="190" y="18" fill="var(--foreground)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Cantilever Action: Strap Undergoes Hogging Moment</text>
      <text x="190" y="32" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">Main longitudinal tensile reinforcement placed near top face</text>
    </g>
  </svg>
</div>"""
    },
    {
        "id": '2023-Q4bi',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (b) i',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.3',
        "topic": "Requirements of Satisfactory Foundations & Design Criteria (Shear Failure & Settlement)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Enumerate the requirements of satisfactory foundations.""",
        "solution": r"""<strong>Requirements of Satisfactory Foundations (IS: 1904):</strong><br>
1. <strong>Adequate Depth:</strong> Founded below topsoil, scour level, and seasonal moisture swelling/shrinkage zone.<br>
2. <strong>Safety Against Shear:</strong> Applied bearing pressure must not exceed safe bearing capacity (FOS ≥ 2.5 to 3.0).<br>
3. <strong>Safe Settlement:</strong> Total settlement ≤ 40 mm in sand, 65 mm in clay; differential angular distortion ≤ 1/500 to prevent wall cracks.<br>
4. <strong>Durability:</strong> Concrete and steel must resist groundwater chemical attack (sulfates per IS: 456)."""
    },
    {
        "id": '2023-Q4bii',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (b) ii',
        "marks": 3,
        "type": 'Practical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '4.1.1',
        "topic": "Site-Specific Foundation Selection for Subsoil Profiles (Compressible Clay vs Expansive Soil)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Two buildings are to be constructed at two different sites. First site shows the low compressive cohesive soil profile up to 10 m depth followed by good quality rock up to 15 m depth below the ground while the second site is having expansive soil up to 5 m depth followed by good rock up to 10 m below the ground. G+4 story building is to be constructed at the first site while at the second site G+15 story building is to be constructed. Suggest the type of foundation at two different sites for the structures to be constructed.""",
        "solution": r"""<strong>Foundation Recommendations for Two Site Conditions:</strong><br>
1. <strong>Site 1: Loose Sand with High Ground Water Table:</strong><br>
• <strong>Recommendation:</strong> <strong>Raft (Mat) Foundation</strong> or <strong>Piles</strong>.<br>
• <strong>Reason:</strong> Loose sand has low strength and high settlement; water table cuts bearing capacity by 50% and causes liquefaction risk. A rigid raft bridges weak spots, or piles transfer loads to deep dense strata.<br>
2. <strong>Site 2: Stiff Clay:</strong><br>
• <strong>Recommendation:</strong> <strong>Isolated Spread Footings</strong>.<br>
• <strong>Reason:</strong> Stiff clay has high shear strength and low settlement. Isolated footings founded at 1.5 m to 2 m depth are safe, simple, and most economical."""
    },
    {
        "id": '2023-Q4biii',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (b) iii',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.3',
        "topic": "Immediate Elastic Settlement of Footing Numerical (Square Footing, E = 50,000 kPa, mu = 0.3)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Using the soil properties (&gamma; = 17.5 kN/m&sup3;, c = 20 kN/m², &phi; = 20&deg;), and assuming the square footing (3.415 m × 3.415 m) located at a depth of 1.5 m carries a total load of 2000 kN. Calculate the immediate settlement of the footing using the elastic theory. Assume the soil is homogeneous and isotropic with a Poisson's ratio of 0.3 and Young's modulus of 50,000 kN/m². (assume influence factor 0.88 for square footing)""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Square footing B = 3.415 m, Area A = 3.415&sup2; = 11.662 m&sup2;, Load Q = 2000 kN, D<sub>f</sub> = 1.5 m.<br>
Soil properties: &mu; = 0.3, E<sub>s</sub> = 50,000 kN/m&sup2;, Influence factor I<sub>f</sub> = 0.88.<br>
<strong>1. Net Contact Pressure (q):</strong><br>
<code>q = Q / A = 2000 / 11.662 = 171.50 kN/m&sup2;</code>.<br>
<strong>2. Elastic Settlement Equation (IS: 8009 Part 1):</strong><br>
<code>S<sub>i</sub> = [ q &middot; B &middot; (1 - &mu;&sup2;) / E<sub>s</sub> ] &middot; I<sub>f</sub></code><br>
<code>(1 - &mu;&sup2;) = 1 - 0.3&sup2; = 1 - 0.09 = 0.91</code>.<br>
<code>S<sub>i</sub> = [ (171.50 &times; 3.415 &times; 0.91) / 50000 ] &times; 0.88</code><br>
<code>S<sub>i</sub> = [ 532.96 / 50000 ] &times; 0.88 = 0.010659 &times; 0.88 = 0.00938 m = <strong>9.38 mm</strong></code>.<br>
The immediate elastic settlement is <strong>9.38 mm</strong> (well within the permissible limit of 25 mm)."""
    },
    {
        "id": '2023-Q4c',
        "year": '2023',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (c)',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL4 (Analyze)',
        "pi": '4.1',
        "topic": "Design of Square Pile Group in Soft Clay for 500 kN Column Load (qu = 50 kPa, 400mm Dia, 6m Length)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Design a square pile group to carry 500 kN load in clay with an unconfined compressive strength of 50 kN/m². Assume pile diameter of 400 mm and 6.0 m length. Adhesion factor may be taken as 0.6.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Design load Q = 500 kN, q<sub>u</sub> = 50 kPa &rArr; c = q<sub>u</sub>/2 = 25 kPa, d = 0.4 m, L = 6.0 m, &alpha; = 0.6. Adopt FS = 2.5.<br>
<strong>1. Single Pile Ultimate Capacity (Q<sub>u1</sub>):</strong><br>
Base area A<sub>b</sub> = (&pi;/4)(0.4)&sup2; = 0.1257 m&sup2;.<br>
Surface area A<sub>s</sub> = &pi; &times; 0.4 &times; 6.0 = 7.540 m&sup2;.<br>
<code>Q<sub>u1</sub> = 9 c A<sub>b</sub> + &alpha; c A<sub>s</sub> = 9(25)(0.1257) + 0.6(25)(7.540) = 28.28 + 113.10 = 141.38 kN</code>.<br>
Allowable load per single pile: <code>Q<sub>all</sub> = 141.38 / 2.5 = 56.55 kN</code>.<br>
Number of piles required: <code>n = 500 / 56.55 = 8.84 &rArr; Select 9 piles (3 &times; 3 square array)</code>.<br>
<strong>2. Group Geometry & Spacing:</strong><br>
Adopt center-to-center spacing s = 3d = 3(0.4) = 1.2 m.<br>
Block width B = 2s + d = 2(1.2) + 0.4 = 2.8 m.<br>
<strong>3. Check Block Failure Capacity:</strong><br>
Block base area A<sub>g</sub> = 2.8&sup2; = 7.84 m&sup2;, Perimeter P<sub>g</sub> = 4 &times; 2.8 = 11.2 m.<br>
<code>Q<sub>ug</sub> = 9 c A<sub>g</sub> + c P<sub>g</sub> L = 9(25)(7.84) + 25(11.2)(6.0) = 1764.0 + 1680.0 = 3444.0 kN</code>.<br>
Safe block capacity = 3444.0 / 2.5 = <strong>1377.6 kN >> 500 kN</strong> (Extremely safe).<br>
<strong>Final Design:</strong> 3 &times; 3 group of 9 piles, 400 mm diameter, 6 m long, spaced at 1.2 m c/c under a 3.4 m &times; 3.4 m pile cap."""
    },
    {
        "id": '2023-Q4c-OR',
        "year": '2023',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.4 (c) OR',
        "marks": 6,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL4 (Analyze)',
        "pi": '4.1',
        "topic": "Strip Footing Width Design in c-phi Soil for 1000 kN/m Column Load",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Design a strip footing resting at 2.0 m below the ground and to carrying a load of 1000 kN/m, the shear parameters c = 50 kN/m² and angle of internal friction is 22&deg; while the density is of soil is 20 kN/m&sup3;. The factor of safety to be used is 2.5.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Load per meter run Q' = 1000 kN/m, D<sub>f</sub> = 2.0 m, c = 50 kPa, &phi; = 22&deg;, &gamma; = 20 kN/m&sup3;, FS = 2.5.<br>
<strong>1. Bearing Capacity Factors (Interpolated for &phi; = 22&deg; from Table 1):</strong><br>
For &phi; = 22&deg;: N<sub>c</sub> &approx; 14.67, N<sub>q</sub> &approx; 6.63, N<sub>&gamma;</sub> &approx; 5.94.<br>
<strong>2. Terzaghi Strip Footing Equation:</strong><br>
<code>q<sub>ult</sub> = c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> + 0.5 &gamma; B N<sub>&gamma;</sub></code><br>
<code>q<sub>ult</sub> = 50(14.67) + 20(2.0)(6.63) + 0.5(20)(B)(5.94) = 733.5 + 265.2 + 59.4 B = 998.7 + 59.4 B</code>.<br>
<code>q<sub>nu</sub> = q<sub>ult</sub> - &gamma; D<sub>f</sub> = (998.7 + 59.4 B) - 40 = 958.7 + 59.4 B</code>.<br>
<code>q<sub>safe</sub> = (q<sub>nu</sub> / 2.5) + &gamma; D<sub>f</sub> = 383.48 + 23.76 B + 40 = 423.48 + 23.76 B</code>.<br>
<strong>3. Equate to Applied Pressure:</strong><br>
<code>1000 / B = 423.48 + 23.76 B &rArr; 23.76 B&sup2; + 423.48 B - 1000 = 0</code>.<br>
Solving the quadratic equation:<br>
<code>B = [ -423.48 + &radic;(423.48&sup2; - 4(23.76)(-1000)) ] / [ 2(23.76) ]</code><br>
<code>&radic;[ 179,335 + 95,040 ] = &radic;274,375 = 523.81</code>.<br>
<code>B = (523.81 - 423.48) / 47.52 = 100.33 / 47.52 = <strong>2.11 m</strong></code>.<br>
Provide a strip footing of width <strong>B = 2.15 m to 2.20 m</strong>."""
    },
    {
        "id": '2023-Q5a',
        "year": '2023',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (a)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '1.4',
        "topic": "Soil Samples: Disturbed vs Undisturbed Samples & Methods of Sampling",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Discuss different types of soil samples. How will you obtain undisturbed samples?""",
        "solution": r"""<strong>Types of Soil Samples &amp; Obtaining Undisturbed Samples:</strong><br>
<span class="is-code-chip">IS: 1892</span><br>
1. <strong>Disturbed Samples:</strong> Soil structure is broken, but soil mineral grains are intact. Used for sieve analysis, liquid limit, plastic limit.<br>
2. <strong>Undisturbed Samples:</strong> Natural soil structure, water content, and void ratio are preserved. Required for shear strength (c, φ), consolidation (C<sub>c</sub>), and permeability.<br>
3. <strong>How to Obtain Undisturbed Samples:</strong><br>
• Use thin-walled tube sampler (Shelby tube) with area ratio A<sub>r</sub> ≤ 10%.<br>
• Push smoothly into borehole base using hydraulic jack (never hammered).<br>
• Rotate to shear the base, extract, and seal ends immediately with molten paraffin wax (min 25 mm thick) and airtight caps."""
    },
    {
        "id": '2023-Q5b',
        "year": '2023',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (b)',
        "marks": 4,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL3 (Apply)',
        "pi": '4.1',
        "topic": "Methods of Subsoil Exploration (Boring, Sounding, Trial Pits, Geophysical)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""What do you understand by geotechnical exploration? What are the different methods of subsoil explorations?""",
        "solution": r"""<strong>Geotechnical Exploration — Meaning &amp; Methods:</strong><br>
<span class="is-code-chip">IS: 1892</span><br>
<strong>Meaning:</strong> Investigating subsurface soil and rock layers to design safe, economical foundations.<br>
1. <strong>Direct Methods (Test Pits):</strong> Shallow open excavations (depth 3-6 m) for direct visual inspection.<br>
2. <strong>Semi-Direct Methods (Borings):</strong><br>
• <strong>Auger Boring:</strong> Hand or power auger rotated into clays above water table.<br>
• <strong>Wash Boring:</strong> Water jet chops soil inside casing; good for sand and soft clay.<br>
• <strong>Rotary Drilling:</strong> Rotating diamond bit with drilling mud; penetrates hard rock and extracts cores.<br>
• <strong>Percussion Drilling:</strong> Heavy chisel dropped repeatedly to break hard bouldery strata.<br>
3. <strong>Indirect Methods (Geophysical):</strong> Seismic refraction (wave velocity) and electrical resistivity for rapid preliminary surveying of large sites."""
    },
    {
        "id": '2023-Q5c',
        "year": '2023',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (c)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO5',
        "bl": 'BL4 (Analyze)',
        "pi": '4.1',
        "topic": "Rock Mass Rating (RMR) & Core Recovery (TCR / RQD) Numerical",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Discuss Rock Mass Rating. How is it useful in finding the bearing capacity of rocks? The drilling carried out in a borehole from 6.00 m to 7.50 m below the ground level shows the 10 rock pieces of size 6, 8, 9, 10, 15, 18, 22 and 32 (all in centimeters). Determine the rock core recovery and rock quality designation. Comment on the quality of rock.""",
        "solution": r"""<strong>1. Rock Mass Rating (RMR - Bieniawski):</strong><br>
A geomechanical classification based on 6 parameters: Uniaxial compressive strength of intact rock, RQD, Discontinuity spacing, Condition of discontinuities, Groundwater conditions, and Joint orientation adjustment. RMR provides safe rock bearing capacity and rock deformation modulus.<br>
<strong>2. Core Run Calculation:</strong><br>
Drill run length L = 7.50 m - 6.00 m = 1.50 m = <strong>150 cm</strong>.<br>
Recovered pieces (cm): 6, 8, 9, 10, 15, 18, 22, 32 (and remaining 2 pieces: e.g. sum of 10 pieces = 120 cm).<br>
Sum of all recovered rock core pieces = 6 + 8 + 9 + 10 + 15 + 18 + 22 + 32 = <strong>120 cm</strong>.<br>
<strong>Total Core Recovery (TCR):</strong><br>
<code>TCR = (Total length of all core pieces / Drill run length) &times; 100% = (120 / 150) &times; 100% = <strong>80.0%</strong></code>.<br>
<strong>3. Rock Quality Designation (RQD - Deere):</strong><br>
Only sound core pieces of length &ge; 10 cm are counted: 10, 15, 18, 22, 32 cm.<br>
Sum of pieces &ge; 10 cm = 10 + 15 + 18 + 22 + 32 = <strong>97 cm</strong>.<br>
<code>RQD = (Sum of lengths of core pieces &ge; 10 cm / Drill run length) &times; 100% = (97 / 150) &times; 100% = <strong>64.67%</strong></code>.<br>
<strong>4. Comment on Rock Quality:</strong><br>
According to Deere's classification (RQD 0-25%: Very Poor, 25-50%: Poor, <strong>50-75%: Fair</strong>, 75-90%: Good, 90-100%: Excellent):<br>
Since RQD = 64.67%, the rock stratum is classified as <strong>FAIR QUALITY ROCK</strong>."""
    },
    {
        "id": '2023-Q5c-OR',
        "year": '2023',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (c) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO5',
        "bl": 'BL4 (Analyze)',
        "pi": '4.1',
        "topic": "Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Explain the Standard Penetration Test. What are the different corrections to be applied to observed SPT value? Following the observations of Standard Penetration Tests conducted at a site on sandy soil. Find the corrected N values.
Depth: 1.50 m, Observed SPT: 12, Density: 15.5 kN/m³
Depth: 3.00 m, Observed SPT: 18, Density: 17.2 kN/m³
Depth: 4.50 m, Observed SPT: 26, Density: 19.0 kN/m³
Depth: 6.00 m, Observed SPT: 32, Density: 20.5 kN/m³""",
        "solution": r"""<strong>1. Standard Penetration Test & Corrections:</strong><br>
&bull; <strong>Overburden Correction:</strong> <code>C<sub>N</sub> = 350 / (&sigma;'<sub>v</sub> + 70)</code> (per IS: 2131) and <code>N' = N &middot; C<sub>N</sub></code> (where C<sub>N</sub> &le; 2.0).<br>
&bull; <strong>Dilatancy Correction:</strong> <code>N" = 15 + 0.5 (N' - 15)</code> (applied when N' > 15 below WT).<br>
<strong>2. Tabulation of Corrections:</strong><br>
&bull; <strong>Depth 1.50 m (N = 12, &gamma; = 15.5 kN/m&sup3;):</strong><br>
&sigma;'<sub>v</sub> = 1.5 &times; 15.5 = 23.25 kPa.<br>
C<sub>N</sub> = 350 / (23.25 + 70) = 350 / 93.25 = 3.75 &rArr; Cap at <strong>2.0</strong>.<br>
<code>N' = 12 &times; 2.0 = 24</code>. Dilatancy: <code>N" = 15 + 0.5(24 - 15) = <strong>19.5 &approx; 20</strong></code>.<br><br>
&bull; <strong>Depth 3.00 m (N = 18, &gamma; = 17.2 kN/m&sup3;):</strong><br>
&sigma;'<sub>v</sub> = 23.25 + (1.5 &times; 17.2) = 23.25 + 25.8 = 49.05 kPa.<br>
C<sub>N</sub> = 350 / (49.05 + 70) = 350 / 119.05 = 2.94 &rArr; Cap at <strong>2.0</strong>.<br>
<code>N' = 18 &times; 2.0 = 36</code>. Dilatancy: <code>N" = 15 + 0.5(36 - 15) = <strong>25.5 &approx; 26</strong></code>.<br><br>
&bull; <strong>Depth 4.50 m (N = 26, &gamma; = 19.0 kN/m&sup3;):</strong><br>
&sigma;'<sub>v</sub> = 49.05 + (1.5 &times; 19.0) = 49.05 + 28.5 = 77.55 kPa.<br>
C<sub>N</sub> = 350 / (77.55 + 70) = 350 / 147.55 = <strong>2.37</strong> &rArr; (C<sub>N</sub> &le; 2.0 &rArr; 2.0 or &radic;[100/77.55]=1.136). Using standard Peck/Hanson &radic;(100/&sigma;'<sub>v</sub>): C<sub>N</sub> = 1.136 &rArr; N' = 26 &times; 1.136 = 29.5 &approx; 30. Dilatancy: N" = 15 + 0.5(30 - 15) = <strong>22.5 &approx; 23</strong>.<br><br>
&bull; <strong>Depth 6.00 m (N = 32, &gamma; = 20.5 kN/m&sup3;):</strong><br>
&sigma;'<sub>v</sub> = 77.55 + (1.5 &times; 20.5) = 77.55 + 30.75 = 108.3 kPa.<br>
C<sub>N</sub> = &radic;(100 / 108.3) = 0.961.<br>
<code>N' = 32 &times; 0.961 = 30.75 &approx; 31</code>. Dilatancy: <code>N" = 15 + 0.5(31 - 15) = <strong>23</strong></code>."""
    },
    {
        "id": '2022-Q1a',
        "year": '2022',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (a)',
        "marks": 2,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '1.4.1',
        "topic": "Depth of Tension Cracks & Critical Depth of Unsupported Cut in Cohesive Soil",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""Determine the depth of tension cracks developed if unsupported excavation is to be made in a soil layer of having &gamma; = 15 kN/m&sup3;, c = 30 kN/m² and &phi; = 10&deg;.""",
        "solution": r"""<strong>Depth of Tension Cracks Calculation:</strong><br>
<strong>Given Data:</strong><br>
Unit weight &gamma; = 15 kN/m&sup3;, Cohesion c = 30 kN/m&sup2;, Friction angle &phi; = 10&deg;.<br>
1. <strong>Active Earth Pressure Coefficient (K<sub>a</sub>):</strong><br>
<code>K_a = \tan^2(45^\circ - \phi/2) = \tan^2(45^\circ - 5^\circ) = \tan^2(40^\circ) = 0.8391^2 = 0.7041</code><br>
<code>\sqrt{K_a} = 0.8391</code><br>
2. <strong>Depth of Tension Cracks (z<sub>c</sub>):</strong><br>
Active lateral pressure in cohesive soil is p<sub>a</sub> = &gamma;z K<sub>a</sub> - 2c&radic;K<sub>a</sub>. Tension crack depth occurs where p<sub>a</sub> = 0:<br>
<code>z_c = \frac{2c}{\gamma \sqrt{K_a}} = \frac{2 \times 30}{15 \times 0.8391} = \frac{60}{12.5865} = 4.77\text{ m}</code><br>
3. <strong>Final Result:</strong><br>
Depth of tension cracks developed = <strong>4.77 m</strong>.<br>
<em>(Maximum critical unsupported excavation depth H<sub>c</sub> = 2 z<sub>c</sub> = 9.53 m).</em>"""
    },
    {
        "id": '2022-Q1b',
        "year": '2022',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (b)',
        "marks": 2,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '1.4.1',
        "topic": "Active Earth Pressure Intensity Increase Due to Uniform Surcharge (Ka * q)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""Calculate the increase in active earth pressure intensity at the bottom of 5 m retaining wall, retaining the soil of &phi; = 30&deg; and &gamma; = 18 kN/m&sup3; due to the application of surcharge of 45 kN/m² at the top of the soil mass.""",
        "solution": r"""<strong>Increase in Active Earth Pressure Intensity Calculation:</strong><br>
<strong>Given Data:</strong><br>
Wall height H = 5 m, &phi; = 30&deg;, &gamma; = 18 kN/m&sup3;, Surcharge q = 45 kN/m&sup2;.<br>
1. <strong>Active Earth Pressure Coefficient (K<sub>a</sub>):</strong><br>
<code>K_a = \frac{1 - \sin 30^\circ}{1 + \sin 30^\circ} = \frac{1 - 0.5}{1 + 0.5} = \frac{0.5}{1.5} = \frac{1}{3} = 0.3333</code><br>
2. <strong>Increase in Active Pressure Intensity (&Delta;p<sub>a</sub>):</strong><br>
A uniform surface surcharge q transmits a constant horizontal pressure intensity over the entire depth of the wall:<br>
<code>\Delta p_a = K_a \cdot q = \frac{1}{3} \times 45 = 15.0\text{ kN/m}^2\text{ (15 kPa)}</code><br>
3. <strong>Final Result:</strong><br>
Increase in active earth pressure intensity at the bottom = <strong>15.0 kN/m&sup2;</strong>."""
    },
    {
        "id": '2022-Q1c',
        "year": '2022',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (c)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Earth Pressure Theories & Assumptions (Rankine vs Coulomb Wedge Theory)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Explain the various assumptions made in Rankine's earth pressure theory.""",
        "solution": r"""<strong>Assumptions Made in Rankine's Earth Pressure Theory:</strong><br>
1. Soil is homogeneous, isotropic, dry, and cohesionless (c = 0).<br>
2. Ground surface is a plane (horizontal or uniformly sloping).<br>
3. Back of the retaining wall is smooth and vertical (zero wall friction, δ = 0).<br>
4. Soil is in a state of plastic equilibrium throughout the failure mass.<br>
5. Rupture surfaces are straight planes inclined at:<br>
<code>\theta = 45^\circ + \frac{\phi}{2} \; \text{(Active)} \qquad \theta = 45^\circ - \frac{\phi}{2} \; \text{(Passive)}</code>"""
    },
    {
        "id": '2022-Q1d',
        "year": '2022',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO1',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""A gravity retaining wall retains 15 m of a backfill &gamma; = 20 kN/m&sup3; and &phi; = 30&deg; with a uniform horizontal backfill. Assuming the wall interface to be vertical, determine the magnitude of active and passive earth pressure and the point of action of total pressure. Assume the angle of wall friction to be 20&deg;.""",
        "solution": r"""<strong>Given:</strong> H = 15 m, &gamma; = 20 kN/m&sup3;, &phi; = 30&deg;, &delta; = 20&deg;, vertical back (&alpha; = 90&deg;), horizontal fill (&beta; = 0&deg;).<br>
<strong>1. Active Condition (Coulomb Theory):</strong><br>
For &phi; = 30&deg;, &delta; = 20&deg;: <code>K<sub>a</sub> &approx; 0.2973</code>.<br>
Total active thrust: <code>P<sub>a</sub> = 0.5 &middot; K<sub>a</sub> &middot; &gamma; &middot; H&sup2; = 0.5 &times; 0.2973 &times; 20 &times; 15&sup2; = <strong>668.9 kN/m</strong></code>.<br>
<strong>Point of Action:</strong> Acts at <strong>H/3 = 15/3 = 5.0 m</strong> above the wall base, inclined at <strong>&delta; = 20&deg;</strong> downward to the normal.<br>
<strong>2. Passive Condition (Coulomb Theory):</strong><br>
For &phi; = 30&deg;, &delta; = 20&deg;: <code>K<sub>p</sub> &approx; 6.103</code>.<br>
Total passive thrust: <code>P<sub>p</sub> = 0.5 &middot; K<sub>p</sub> &middot; &gamma; &middot; H&sup2; = 0.5 &times; 6.103 &times; 20 &times; 225 = <strong>13,731.8 kN/m</strong></code>.<br>
<strong>Point of Action:</strong> Acts at <strong>5.0 m</strong> above the base, inclined at <strong>20&deg;</strong> upward to the normal."""
    },
    {
        "id": '2022-Q1e-OR',
        "year": '2022',
        "unit": 1,
        "unit_name": "Lateral Earth Pressure & Retaining Walls",
        "q_no": 'Q.1 (e) OR',
        "marks": 7,
        "type": 'Theory',
        "co": 'CO1',
        "bl": 'BL4 (Analyze)',
        "pi": '2.1.2',
        "topic": "Rebhann's Graphical Construction for Active Earth Thrust & Proof",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Illustrate Rebhann's graphical construction method to evaluate the earth pressure on a retaining wall.""",
        "solution": r"""<strong>Rebhann's Graphical Construction &amp; Advantages:</strong><br>
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
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Rebhann's Graphical Construction for Active Thrust (Pa)</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 320" class="sol-diagram-svg" width="100%" style="max-width:620px;height:auto;display:block;">
    <defs>
      <marker id="rebhann-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- Backfill Soil Shading -->
    <polygon points="90,80 500,80 500,240 90,240" fill="var(--pastel-sand-bg)" opacity="0.3" />

    <!-- Retaining Wall Stem AB -->
    <polygon points="60,80 90,80 90,240 50,240" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.8" />
    <line x1="90" y1="80" x2="90" y2="240" stroke="var(--foreground)" stroke-width="2.5" />
    
    <!-- Wall Labels A and B -->
    <circle cx="90" cy="80" r="3" fill="var(--foreground)" />
    <text x="82" y="72" fill="var(--foreground)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">A (Crest)</text>
    <circle cx="90" cy="240" r="3" fill="var(--foreground)" />
    <text x="75" y="256" fill="var(--foreground)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">B (Heel)</text>

    <!-- Ground Surface Line AD -->
    <line x1="90" y1="80" x2="520" y2="80" stroke="var(--foreground)" stroke-width="2" />
    <text x="525" y="84" fill="var(--foreground)" font-size="11" font-weight="700" font-family="system-ui, sans-serif">D (Ground Line)</text>

    <!-- Earth Pressure phi-line BL -->
    <line x1="90" y1="240" x2="490" y2="80" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="2" />
    <circle cx="490" cy="80" r="3" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="495" y="74" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">L (&phi;-line)</text>
    
    <!-- Angle phi arc at B -->
    <path d="M 150 240 A 60 60 0 0 0 144 219" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.8" />
    <text x="158" y="228" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">&phi;</text>

    <!-- Semi-circle on BL as diameter -->
    <path d="M 90 240 A 215 215 0 0 1 490 80" fill="none" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6" />

    <!-- Poncelet Triangle BCD (Radiant Pastel Peach Fill) -->
    <polygon points="90,240 305,154 360,80" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.2" />
    <circle cx="305" cy="154" r="3" fill="var(--pastel-peach-foreground, #f97316)" />
    <text x="290" y="152" fill="var(--pastel-peach-foreground, #f97316)" font-size="12" font-weight="800" font-family="system-ui, sans-serif">C</text>

    <!-- Critical Failure Slip Plane BD -->
    <line x1="90" y1="240" x2="360" y2="80" stroke="var(--foreground)" stroke-width="2" stroke-dasharray="5 3" />
    <circle cx="360" cy="80" r="3" fill="var(--foreground)" />
    <text x="360" y="68" fill="var(--foreground)" font-size="11" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">D (Slip Surface)</text>

    <!-- Perpendicular Line FJ to semi-circle -->
    <line x1="360" y1="80" x2="260" y2="28" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />
    <circle cx="260" cy="28" r="2.5" fill="var(--pastel-sky-foreground, #0ea5e9)" />
    <text x="255" y="22" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="11" font-weight="800" font-family="system-ui, sans-serif">F</text>

    <!-- Tangent Arc from F to C -->
    <path d="M 260 28 A 230 230 0 0 1 305 154" fill="none" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.2" stroke-dasharray="3 3" />

    <!-- Active Thrust Vector Pa -->
    <line x1="90" y1="187" x2="160" y2="160" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2.6" marker-end="url(#rebhann-arrow)" />
    <text x="165" y="155" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" font-family="system-ui, sans-serif">Pa (at H/3)</text>

    <!-- Formula & Intelligence Card -->
    <g transform="translate(350, 205)">
      <rect x="0" y="0" width="245" height="66" fill="var(--card)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.4" rx="6" />
      <text x="14" y="22" fill="var(--foreground)" font-size="10.5" font-weight="800" font-family="system-ui, sans-serif">Rebhann's Active Thrust:</text>
      <text x="14" y="42" fill="var(--pastel-peach-foreground, #f97316)" font-size="13" font-weight="800" font-family="system-ui, sans-serif">Pa = &gamma; &times; Area(&Delta;BCD)</text>
      <text x="14" y="56" fill="var(--muted-foreground)" font-size="9" font-family="system-ui, sans-serif">Inclined at angle &delta; at H/3 above base</text>
    </g>
  </svg>
</div><br>
4. <strong>Active Thrust:</strong><br>
<code>P_a = \gamma \cdot \text{Area}(\triangle BCD)</code><br>
5. <strong>Advantages:</strong><br>
• Avoids tedious trigonometric equations.<br>
• Easily handles broken or irregular backfill slopes.<br>
• Directly identifies critical failure plane BC without trial wedges."""
    },
    {
        "id": '2022-Q2a',
        "year": '2022',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Direct Box Shear Test vs Triaxial Shear Test Comparison",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""List the basic differences between a box shear test and a triaxial shear test for soils.""",
        "solution": r"""<strong>Differences Between Direct Shear Box Test and Triaxial Shear Test:</strong><br>
1. <strong>Failure Plane:</strong> Direct shear test forces failure along a predetermined horizontal plane, whereas in a triaxial test, failure occurs along the natural weakest plane.<br>
2. <strong>Drainage Control:</strong> Direct shear test provides poor drainage control and cannot measure pore water pressure, whereas triaxial test provides complete drainage control and accurate pore pressure measurement.<br>
3. <strong>Stress Distribution:</strong> Direct shear test has non-uniform stress distribution with stress concentrations at edges, whereas triaxial test maintains uniform stress conditions throughout the cylindrical sample.<br>
4. <strong>Soil Applicability:</strong> Direct shear test is best suited for coarse-grained cohesionless sands, whereas triaxial test is suitable for all soil types under UU, CU, and CD conditions.<br>
5. <strong>Strength Parameters:</strong> Direct shear test measures total stress parameters only, whereas triaxial test determines both total and effective stress parameters."""
    },
    {
        "id": '2022-Q2b',
        "year": '2022',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '1.4.1',
        "topic": "Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Describe unconsolidated undrained test and a drained test.""",
        "solution": r"""<strong>Unconsolidated Undrained (UU) and Consolidated Drained (CD) Tests:</strong><br>
1. <strong>Unconsolidated Undrained (UU) Test:</strong> Drainage is kept closed during both the cell pressure stage and shearing stage. It is a rapid test (takes 5 to 10 minutes) with no dissipation of excess pore water pressure, measuring undrained shear strength (c<sub>u</sub>).<br>
<em>Example:</em> Short-term foundation stability immediately after rapid construction on clay.<br>
2. <strong>Consolidated Drained (CD) Test:</strong> Drainage is kept open during both the cell pressure stage and shearing stage. It is a very slow test (takes days to weeks) allowing excess pore water pressure to fully dissipate (u = 0), measuring effective shear strength parameters (c', &phi;').<br>
<em>Example:</em> Long-term permanent stability analysis of natural earth slopes and retaining walls."""
    },
    {
        "id": '2022-Q2c',
        "year": '2022',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (c)',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "Vane Shear Test Formula & Shear Strength in Soft Clay Numerical",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""A vane, 10.8 cm long, 7.2 cm in diameter, was pressed into a soft clay at the bottom of a bore hole. Torque was applied and the value at failure was 45 N·m. Calculate the shear strength of the clay on a horizontal plane.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
H = 10.8 cm = 0.108 m, D = 7.2 cm = 0.072 m, Torque T = 45 N&middot;m.<br>
<strong>Vane Shear Torque Formula (Shearing at both ends):</strong><br>
<code>T = c<sub>u</sub> &middot; &pi; &middot; D&sup2; &middot; [ (H / 2) + (D / 6) ]</code><br>
<code>&pi; &middot; D&sup2; = &pi; &times; (0.072)&sup2; = 0.016286 m&sup2;</code>.<br>
<code>(H / 2) + (D / 6) = (0.108 / 2) + (0.072 / 6) = 0.054 + 0.012 = 0.066 m</code>.<br>
<code>T = c<sub>u</sub> &times; 0.016286 &times; 0.066 = c<sub>u</sub> &times; (1.0749 &times; 10^{-3} m&sup3;)</code>.<br>
<strong>Undrained Shear Strength (c<sub>u</sub>):</strong><br>
<code>c<sub>u</sub> = 45 / (1.0749 &times; 10^{-3}) = 41,864 N/m&sup2; = <strong>41.86 kPa</strong></code>.<br>
Shear strength of clay on horizontal plane is <strong>41.86 kN/m&sup2;</strong>."""
    },
    {
        "id": '2022-Q2d',
        "year": '2022',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "CD Triaxial Test on Normally Consolidated Clay (sigma3 = 250 kPa, sigmad = 275 kPa)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""A consolidated-drained triaxial test was conducted on a normally consolidated clay yielding the following data: &sigma;₃ = 250 kN/m²; &sigma;_d = 275 kN/m². Determine: (i) The angle of friction, (ii) Angle which the failure plane makes with the major principal plane, (iii) Normal stress and shear stress on the failure plane, (iv) Normal stress on the plane of &tau;_max.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Normally consolidated clay &rArr; c' = 0.<br>
Confining stress &sigma;'₃ = 250 kPa, Deviator stress &sigma;_d = 275 kPa.<br>
Major principal stress: <code>&sigma;'₁ = &sigma;'₃ + &sigma;_d = 250 + 275 = 525 kPa</code>.<br>
<strong>(i) Angle of Friction (&phi;'):</strong><br>
From Mohr-Coulomb for c = 0:<br>
<code>sin &phi;' = (&sigma;'₁ - &sigma;'₃) / (&sigma;'₁ + &sigma;'₃) = 275 / (525 + 250) = 275 / 775 = 0.3548</code>.<br>
<code>&phi;' = arcsin(0.3548) = <strong>20.78&deg;</strong></code>.<br>
<strong>(ii) Failure Plane Angle with Major Principal Plane (&theta;):</strong><br>
<code>&theta; = 45&deg; + &phi;'/2 = 45&deg; + 10.39&deg; = <strong>55.39&deg;</strong></code>.<br>
<strong>(iii) Stresses on Failure Plane:</strong><br>
<code>&sigma;_f = [(&sigma;'₁+&sigma;'₃)/2] + [(&sigma;'₁-&sigma;'₃)/2] &middot; cos 2&theta; = 387.5 + 137.5 &middot; cos(110.78&deg;) = 387.5 + 137.5(-0.3548) = 387.5 - 48.78 = <strong>338.72 kPa</strong></code>.<br>
<code>&tau;_f = [(&sigma;'₁-&sigma;'₃)/2] &middot; sin 2&theta; = 137.5 &middot; sin(110.78&deg;) = 137.5(0.9350) = <strong>128.56 kPa</strong></code>.<br>
<em>(Check: &tau;_f / &sigma;_f = 128.56 / 338.72 = 0.3795 = tan 20.78&deg; &check;).</em><br>
<strong>(iv) Normal Stress on the Plane of &tau;<sub>max</sub>:</strong><br>
The plane of maximum shear stress occurs at 2&theta; = 90&deg; (&theta; = 45&deg;):<br>
<code>&sigma; = (&sigma;'₁ + &sigma;'₃) / 2 = (525 + 250) / 2 = <strong>387.5 kPa</strong></code> (with &tau;<sub>max</sub> = 137.5 kPa)."""
    },
    {
        "id": '2022-Q2e-OR',
        "year": '2022',
        "unit": 2,
        "unit_name": "Shear Strength & Slope Stability",
        "q_no": 'Q.2 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO2',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "Infinite Slope Stability in Granular Soil with Seepage & Water Table Numerical",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""A granular soil has G = 2.70, e = 0.5 and &phi; = 35&deg;. A slope has to be made of this material. If a factor of safety of 1.15 is needed against failure, determine the safe angle of slope when: (i) The slope is dry or submerged without seepage, (ii) If seepage occurs at and parallel to the surface of the slope, (iii) If seepage occurs parallel to the slope with the water table at a depth of 1.5 m, what is the factor of safety available on a slip plane parallel to the ground surface at a depth of 4 m. Assume slope angle is 30&deg;.""",
        "solution": r"""<strong>Soil Parameters:</strong> G = 2.70, e = 0.5, &phi; = 35&deg;, c = 0.<br>
<code>&gamma;<sub>sat</sub> = [(G + e)/(1 + e)] &middot; &gamma;<sub>w</sub> = [(2.7 + 0.5)/1.5] &times; 9.81 = 20.93 kN/m&sup3;</code>.<br>
<code>&gamma;' = &gamma;<sub>sat</sub> - &gamma;<sub>w</sub> = 20.93 - 9.81 = 11.12 kN/m&sup3;</code>.<br>
<code>&gamma;<sub>d</sub> = [G / (1 + e)] &middot; &gamma;<sub>w</sub> = (2.7/1.5) &times; 9.81 = 17.66 kN/m&sup3;</code>.<br>
<strong>(i) Dry or Submerged without Seepage:</strong><br>
<code>FS = tan &phi; / tan &beta; &rArr; 1.15 = tan 35&deg; / tan &beta; &rArr; tan &beta; = 0.7002 / 1.15 = 0.6089</code>.<br>
Safe slope angle <code>&beta; = arctan(0.6089) = <strong>31.34&deg;</strong></code>.<br>
<strong>(ii) Seepage Parallel to Surface at Ground Level:</strong><br>
<code>FS = (&gamma;' / &gamma;<sub>sat</sub>) &middot; (tan &phi; / tan &beta;)</code>.<br>
<code>1.15 = (11.12 / 20.93) &middot; (0.7002 / tan &beta;) = 0.5313 &times; 0.7002 / tan &beta; = 0.3720 / tan &beta;</code>.<br>
<code>tan &beta; = 0.3720 / 1.15 = 0.3235 &rArr; &beta; = arctan(0.3235) = <strong>17.93&deg;</strong></code>.<br>
<strong>(iii) Partially Submerged with WT at 1.5 m, Slip Plane at z = 4 m, &beta; = 30&deg;:</strong><br>
Dry/moist zone (0 to 1.5 m): &Delta;W₁ = 17.66 &times; 1.5 = 26.49 kPa.<br>
Submerged zone (1.5 to 4 m): &Delta;W₂ = 20.93 &times; 2.5 = 52.33 kPa.<br>
Total vertical stress &sigma;<sub>v</sub> = 26.49 + 52.33 = 78.82 kPa.<br>
Pore water pressure u = 9.81 &times; 2.5 &times; cos&sup2; 30&deg; = 24.53 &times; 0.75 = 18.40 kPa.<br>
Normal effective stress &sigma;' = &sigma;<sub>v</sub> cos&sup2; 30&deg; - u = (78.82 &times; 0.75) - 18.40 = 59.12 - 18.40 = 40.72 kPa.<br>
Shear stress &tau; = &sigma;<sub>v</sub> sin 30&deg; cos 30&deg; = 78.82 &times; 0.5 &times; 0.866 = 34.13 kPa.<br>
Available Factor of Safety: <code>FS = &sigma;' tan &phi; / &tau; = (40.72 &times; tan 35&deg;) / 34.13 = (40.72 &times; 0.7002) / 34.13 = 28.51 / 34.13 = <strong>0.835 (Unstable!)</strong></code>."""
    },
    {
        "id": '2022-Q3a',
        "year": '2022',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Terzaghi's Bearing Capacity Theory: Assumptions & Factors Affecting Bearing Capacity",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""List the assumptions made in Terzaghi's analysis of bearing capacity of a continuous footing.""",
        "solution": r"""<strong>Assumptions of Terzaghi's Bearing Capacity Theory:</strong><br>
1. Soil is homogeneous, isotropic, and semi-infinite.<br>
2. Footing is a continuous strip with infinite length (L/B &rarr; &infin;), forming a two-dimensional plane-strain condition.<br>
3. Foundation is shallow, with depth of embedment D<sub>f</sub> &le; width of footing B.<br>
4. Base of the footing is rough, preventing soil slipping along the contact surface.<br>
5. Soil above the foundation base level is replaced by an equivalent surcharge q = &gamma;D<sub>f</sub> (shear resistance above base level is neglected).<br>
6. General shear failure occurs in the supporting soil mass.<br>
7. Soil behaves as a rigid-plastic material obeying Mohr-Coulomb failure criterion (&tau; = c + &sigma; tan&phi;)."""
    },
    {
        "id": '2022-Q3b',
        "year": '2022',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Terzaghi's Bearing Capacity Theory: Assumptions & Factors Affecting Bearing Capacity",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""Discuss the various factors that affect the bearing capacity of a shallow footing.""",
        "solution": r"""<strong>Factors Affecting Bearing Capacity of a Shallow Footing:</strong><br>
1. <strong>Shear Strength of Soil (c and &phi;):</strong> Higher cohesion and higher angle of internal friction increase bearing capacity factors exponentially.<br>
2. <strong>Footing Width (B):</strong> In granular soils (sand), bearing capacity increases linearly with footing width (0.5 &gamma; B N<sub>&gamma;</sub>).<br>
3. <strong>Depth of Embedment (D<sub>f</sub>):</strong> Deeper footing placement increases the confining surcharge pressure (&gamma; D<sub>f</sub> N<sub>q</sub>), directly increasing bearing capacity.<br>
4. <strong>Water Table Location:</strong> When groundwater rises to the foundation level, submerged unit weight (&gamma;') replaces &gamma;, reducing bearing capacity by up to 50%.<br>
5. <strong>Shape of Footing:</strong> Circular and square footings have higher bearing capacities per unit area than continuous strip footings due to 3D shape factors.<br>
6. <strong>Unit Weight of Soil (&gamma;):</strong> Denser soil with higher unit weight provides greater resistance to shear displacement."""
    },
    {
        "id": '2022-Q3c',
        "year": '2022',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (c)',
        "marks": 3,
        "type": 'Theory',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '1.4.1',
        "topic": "Ground Water Table Effect on Ultimate & Safe Bearing Capacity (Theory & 50% Drop)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Illustrate the effect of ground water table on the safe bearing capacity.""",
        "solution": r"""<strong>Ground Water Table Effect on Safe Bearing Capacity:</strong><br>
<span class="is-code-chip">IS: 6403</span><br>
<code>q_{ult} = c N_c + \gamma_1 D_f N_q W^*_1 + 0.5 \gamma_2 B N_\gamma W^*_2</code><br>
1. <strong>Surcharge Correction Factor (W*<sub>1</sub>):</strong> W*<sub>1</sub> = 0.5 [1 + d<sub>w</sub> / D<sub>f</sub>] for water table between ground level and footing base.<br>
2. <strong>Wedge Correction Factor (W*<sub>2</sub>):</strong> W*<sub>2</sub> = 0.5 [1 + z<sub>w</sub> / B] for water table within depth B below footing base.<br>
3. <strong>Maximum Reduction:</strong> When water table rises to ground level, effective unit weight is halved (γ' ≈ 0.5 γ<sub>sat</sub>), cutting bearing capacity of sand by <strong>50%</strong>."""
    },
    {
        "id": '2022-Q3d',
        "year": '2022',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Calculate the safe bearing capacity of a square footing 1.5 m × 1.5 m, located at a depth of 1 m below the ground level in a soil of average density 20 kN/m&sup3;. &phi; = 20&deg;, N<sub>c</sub> = 17.7, N<sub>q</sub> = 7.4, and N<sub>&gamma;</sub> = 5.0. Assume a suitable factor of safety and that the water table is very deep. Also compute the reduction in safe bearing capacity of the footing if the water table rises to the ground level.""",
        "solution": r"""<strong>Given:</strong> Square footing B = 1.5 m, D<sub>f</sub> = 1.0 m, &gamma; = 20 kN/m&sup3;, &phi; = 20&deg;, N<sub>c</sub> = 17.7, N<sub>q</sub> = 7.4, N<sub>&gamma;</sub> = 5.0. Soil is cohesionless (c = 0). Adopt FS = 3.0.<br>
<strong>Case A: Water table very deep (R<sub>w1</sub> = 1.0, R<sub>w2</sub> = 1.0):</strong><br>
Terzaghi square footing (c = 0):<br>
<code>q<sub>ult</sub> = &gamma; D<sub>f</sub> N<sub>q</sub> + 0.4 &gamma; B N<sub>&gamma;</sub> = (20 &times; 1.0 &times; 7.4) + (0.4 &times; 20 &times; 1.5 &times; 5.0) = 148.0 + 60.0 = 208.0 kN/m&sup2;</code>.<br>
<code>q<sub>nu</sub> = q<sub>ult</sub> - &gamma; D<sub>f</sub> = 208.0 - 20.0 = 188.0 kN/m&sup2;</code>.<br>
<code>q<sub>safe</sub> = (q<sub>nu</sub> / 3.0) + &gamma; D<sub>f</sub> = (188.0 / 3.0) + 20.0 = 62.67 + 20.0 = <strong>82.67 kN/m&sup2;</strong></code>.<br>
<strong>Case B: Water table rises to ground level:</strong><br>
Submerged unit weight <code>&gamma;' = &gamma;<sub>sat</sub> - &gamma;<sub>w</sub> = 20 - 9.81 = 10.19 kN/m&sup3;</code>.<br>
<code>q<sub>ult_sub</sub> = &gamma;' D<sub>f</sub> N<sub>q</sub> + 0.4 &gamma;' B N<sub>&gamma;</sub> = (10.19 &times; 1.0 &times; 7.4) + (0.4 &times; 10.19 &times; 1.5 &times; 5.0) = 75.41 + 30.57 = 105.98 kN/m&sup2;</code>.<br>
<code>q<sub>nu_sub</sub> = 105.98 - (10.19 &times; 1.0) = 95.79 kN/m&sup2;</code>.<br>
<code>q<sub>safe_sub</sub> = (95.79 / 3.0) + 10.19 = 31.93 + 10.19 = <strong>42.12 kN/m&sup2;</strong></code>.<br>
<strong>Percentage Reduction in Safe Bearing Capacity:</strong><br>
<code>Reduction = [ (82.67 - 42.12) / 82.67 ] &times; 100% = <strong>49.05%</strong></code>."""
    },
    {
        "id": '2022-Q3e-OR',
        "year": '2022',
        "unit": 3,
        "unit_name": "Shallow Foundations & Bearing Capacity",
        "q_no": 'Q.3 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO3',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Circular Footing Diameter Determination on Saturated Stiff Clay (Q = 600 kN, qu = 250 kPa)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""A circular footing is resting on a stiff saturated clay with q<sub>u</sub> = 250 kN/m². The depth of foundation is 2 m. Determine the diameter of the footing if the column load is 600 kN. Assume a factor of safety as 2.5. The bulk unit weight of soil is 20 kN/m&sup3;.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Circular footing, D<sub>f</sub> = 2.0 m, Column load Q = 600 kN, FS = 2.5, &gamma; = 20 kN/m&sup3;.<br>
Saturated stiff clay (&phi; = 0&deg;): <code>c = q<sub>u</sub> / 2 = 250 / 2 = 125 kN/m&sup2;</code>.<br>
<strong>1. Terzaghi Factors for &phi; = 0&deg;:</strong> N<sub>c</sub> = 5.7, N<sub>q</sub> = 1.0, N<sub>&gamma;</sub> = 0.<br>
For a circular footing:<br>
<code>q<sub>ult</sub> = 1.3 c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> = 1.3(125)(5.7) + (20 &times; 2 &times; 1) = 926.25 + 40 = 966.25 kN/m&sup2;</code>.<br>
<code>q<sub>nu</sub> = 926.25 kN/m&sup2;</code>.<br>
<code>q<sub>ns</sub> = q<sub>nu</sub> / 2.5 = 926.25 / 2.5 = 370.5 kN/m&sup2;</code>.<br>
Safe gross pressure: <code>q<sub>safe</sub> = q<sub>ns</sub> + &gamma; D<sub>f</sub> = 370.5 + 40 = 410.5 kN/m&sup2;</code>.<br>
<strong>2. Required Bearing Area & Diameter:</strong><br>
<code>A = Q / q<sub>safe</sub> = 600 / 410.5 = 1.4616 m&sup2;</code>.<br>
Since A = (&pi;/4) D&sup2;:<br>
<code>D = &radic;[ (4 &times; 1.4616) / &pi; ] = &radic;1.8610 = <strong>1.364 m</strong></code>.<br>
Provide a circular footing of diameter <strong>D = 1.40 m</strong>."""
    },
    {
        "id": '2022-Q4a',
        "year": '2022',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Functions and Classification of Pile Foundations",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""Explain the function of pile foundation.""",
        "solution": r"""<strong>Functions of Pile Foundation:</strong><br>
1. <strong>End-Bearing Load Transfer:</strong> Transfers heavy building loads through weak, compressible top layers down to deep stiff soil or solid bedrock.<br>
2. <strong>Skin Friction Load Transfer:</strong> Distributes structural loads along the surface area of the pile shaft by friction in deep uniform clay or sand strata.<br>
3. <strong>Resisting Uplift Forces:</strong> Anchors tall structures (transmission towers, chimneys, transmission masts) against upward tension and wind overturning moments.<br>
4. <strong>Resisting Lateral Loads:</strong> Resists horizontal lateral forces caused by wind, earthquakes, earth pressures, and water wave impacts on bridge piers and docks.<br>
5. <strong>Soil Compaction:</strong> Compaction piles densify loose granular deposits, increasing bearing capacity and mitigating earthquake liquefaction risk."""
    },
    {
        "id": '2022-Q4b',
        "year": '2022',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO4',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Bearing Capacity Computation: Shallow vs Deep Foundations (Skin Friction vs End Bearing Mechanisms)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""Discuss the basic difference in the bearing capacity computation of shallow and deep foundations.""",
        "solution": r"""<strong>Differences in Bearing Capacity Computation of Shallow and Deep Foundations:</strong><br>
1. <strong>Load Transfer Mechanism:</strong> Shallow foundations carry load through base contact bearing pressure only (q<sub>u</sub>), whereas deep foundations (piles) carry load through both base resistance (Q<sub>b</sub>) and shaft skin friction (Q<sub>s</sub>).<br>
2. <strong>Surcharge Pressure:</strong> In shallow foundations, surcharge is taken as full depth q = &gamma;D<sub>f</sub>, whereas in deep foundations, effective vertical stress increases only up to a critical depth (10d to 20d) and then stays constant.<br>
3. <strong>Bearing Capacity Factors:</strong> Shallow foundations use Terzaghi factors (e.g., N<sub>c</sub> = 5.7 for strip footing in clay), whereas deep foundations use deep cavity expansion factors (e.g., N<sub>c</sub>* = 9.0 per Skempton).<br>
4. <strong>Failure Surface Extent:</strong> Shallow foundation failure planes extend outwards and upwards all the way to ground surface with visible heave, whereas pile failure surfaces are localized around the pile tip and shaft without ground heaving.<br>
5. <strong>Settlement Influence:</strong> Shallow foundations are often governed and restricted by settlement criteria, whereas deep foundations mobilize high load capacity at small settlements."""
    },
    {
        "id": '2022-Q4c',
        "year": '2022',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (c)',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "Single Pile Frictional Resistance in Uniform Clay Deposit Numerical (Qs = alpha * cu * As)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""A pile is driven in a uniform clay of large depth. The clay has an unconfined compression strength of 90 kN/m². The pile is 90 cm diameter and 6 m long. Determine the safe frictional resistance of the pile, assuming a factor of safety of 3. Assume the adhesion factor &alpha; = 0.7.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
Clay q<sub>u</sub> = 90 kPa &rArr; c = q<sub>u</sub> / 2 = 45 kPa.<br>
Pile diameter d = 0.90 m, Length L = 6.0 m, Adhesion factor &alpha; = 0.7, FS = 3.<br>
<strong>1. Surface Area of Pile Shaft (A<sub>s</sub>):</strong><br>
<code>A<sub>s</sub> = &pi; &middot; d &middot; L = &pi; &times; 0.90 &times; 6.0 = 16.965 m&sup2;</code>.<br>
<strong>2. Ultimate Skin Friction Resistance (Q<sub>s</sub>):</strong><br>
<code>Q<sub>s</sub> = &alpha; &middot; c &middot; A<sub>s</sub> = 0.7 &times; 45 &times; 16.965 = <strong>534.40 kN</strong></code>.<br>
<strong>3. Safe Frictional Resistance:</strong><br>
<code>Q<sub>safe_friction</sub> = Q<sub>s</sub> / FS = 534.40 / 3.0 = <strong>178.13 kN</strong></code>."""
    },
    {
        "id": '2022-Q4d',
        "year": '2022',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (d)',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "Single Pile Static Ultimate Load Capacity in Sand Deposit (Qu = Qb + Qs, phi = 40 deg)",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""A 12 m long, 300 mm diameter pile is driven in a uniform deposit of sand (&phi; = 40&deg;). The water table is at a great depth and is not likely to rise. The average dry unit weight of sand is 18 kN/m&sup3;. Using N<sub>q</sub> = 137, calculate the safe load capacity of the pile with a factor of safety of 2.5.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
L = 12 m, d = 0.30 m, &gamma; = 18 kN/m&sup3;, &phi; = 40&deg;, N<sub>q</sub> = 137, FS = 2.5.<br>
<strong>1. Base Resistance (Q<sub>b</sub>):</strong><br>
Base area A<sub>b</sub> = (&pi;/4)(0.3)&sup2; = 0.07068 m&sup2;.<br>
Critical depth in dense sand: L<sub>c</sub> &approx; 15 d = 15(0.3) = 4.5 m (or 20 d = 6.0 m).<br>
At critical depth L<sub>c</sub> = 15 d = 4.5 m, effective overburden reaches limiting value:<br>
<code>&sigma;'<sub>v</sub> = &gamma; &middot; L<sub>c</sub> = 18 &times; 4.5 = 81.0 kPa</code>.<br>
Limiting unit base resistance: <code>q<sub>b</sub> = &sigma;'<sub>v</sub> &middot; N<sub>q</sub> = 81.0 &times; 137 = 11,097 kPa</code>.<br>
<code>Q<sub>b</sub> = q<sub>b</sub> &middot; A<sub>b</sub> = 11,097 &times; 0.07068 = <strong>784.3 kN</strong></code>.<br>
<strong>2. Shaft Resistance (Q<sub>s</sub>):</strong><br>
For &phi; = 40&deg;, earth pressure coefficient K &approx; 1.0, wall friction &delta; &approx; 0.75 &phi; = 30&deg;.<br>
Average vertical stress along shaft from 0 to 4.5 m: <code>&sigma;<sub>v1</sub> = 0.5(81) = 40.5 kPa</code>.<br>
Average vertical stress from 4.5 to 12 m (capped): <code>&sigma;<sub>v2</sub> = 81.0 kPa</code>.<br>
<code>f<sub>s1</sub> = K &sigma;<sub>v1</sub> tan &delta; = 1.0(40.5) tan 30&deg; = 23.38 kPa</code> over A<sub>s1</sub> = &pi;(0.3)(4.5) = 4.241 m&sup2; &rArr; Q<sub>s1</sub> = 99.1 kN.<br>
<code>f<sub>s2</sub> = K &sigma;<sub>v2</sub> tan &delta; = 1.0(81.0) tan 30&deg; = 46.76 kPa</code> over A<sub>s2</sub> = &pi;(0.3)(7.5) = 7.068 m&sup2; &rArr; Q<sub>s2</sub> = 330.5 kN.<br>
Total skin friction: <code>Q<sub>s</sub> = 99.1 + 330.5 = <strong>429.6 kN</strong></code>.<br>
<strong>3. Total Safe Capacity:</strong><br>
<code>Q<sub>u</sub> = Q<sub>b</sub> + Q<sub>s</sub> = 784.3 + 429.6 = 1213.9 kN</code>.<br>
<code>Q<sub>safe</sub> = Q<sub>u</sub> / FS = 1213.9 / 2.5 = <strong>485.56 kN</strong></code>."""
    },
    {
        "id": '2022-Q4e-OR',
        "year": '2022',
        "unit": 4,
        "unit_name": "Deep Foundations (Piles & Caissons)",
        "q_no": 'Q.4 (e) OR',
        "marks": 7,
        "type": 'Numerical',
        "co": 'CO4',
        "bl": 'BL3 (Apply)',
        "pi": '2.1.2',
        "topic": "9-Pile Group Safe Load Capacity in Soft Clay Numerical (30cm Dia, 9m Length, qu = 90 kPa)",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""A square group of 9 piles was driven into soft clay extending to a large depth. The diameter and length of the piles were 30 cm and 9 m respectively. If the unconfined compression strength of the clay is 90 kN/m², and the pile spacing is 90 cm centre to centre. Calculate the capacity of the pile group? Assume a factor of safety of 2.5 and adhesion factor of 0.75.""",
        "solution": r"""<strong>Given Parameters:</strong><br>
3 &times; 3 array (n = 9), d = 0.3 m, L = 9 m, s = 0.9 m, q<sub>u</sub> = 90 kPa &rArr; c = 45 kPa, &alpha; = 0.75, FS = 2.5.<br>
<strong>1. Individual Pile Failure:</strong><br>
A<sub>b</sub> = (&pi;/4)(0.3)&sup2; = 0.07068 m&sup2;, A<sub>s</sub> = &pi;(0.3)(9) = 8.482 m&sup2;.<br>
Single pile: <code>Q<sub>u</sub> = 9(45)(0.07068) + 0.75(45)(8.482) = 28.63 + 286.28 = 314.91 kN</code>.<br>
Total for group: <code>Q<sub>gi</sub> = 9 &times; 314.91 = <strong>2834.2 kN</strong></code>.<br>
<strong>2. Block Failure:</strong><br>
Block width B = 2s + d = 2(0.9) + 0.3 = 2.1 m.<br>
<code>Q<sub>gb</sub> = 9 c B&sup2; + 4 B L c = 9(45)(2.1&sup2;) + 4(2.1)(9)(45) = 1786.05 + 3402.0 = <strong>5188.05 kN</strong></code>.<br>
<strong>3. Governing Capacity:</strong><br>
Governing ultimate Q<sub>ug</sub> = min(2834.2, 5188.05) = <strong>2834.2 kN</strong>.<br>
Safe capacity = 2834.2 / 2.5 = <strong>1133.68 kN</strong>."""
    },
    {
        "id": '2022-Q5a',
        "year": '2022',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (a)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Laboratory and Field Tests for Soil Investigation Work",
        "repeated": False,
        "rep_frequency": "1 of 4 Papers (2022)",
        "question": r"""List the laboratory and field tests used for the soil investigation work.""",
        "solution": r"""<strong>Laboratory and Field Tests in Soil Investigation:</strong><br>
1. <strong>Field (In-Situ) Tests:</strong><br>
• <strong>Standard Penetration Test (SPT):</strong> Determines N-value, relative density of sands, and consistency of clays.<br>
• <strong>Cone Penetration Test (CPT):</strong> Measures point resistance and sleeve friction continuously with depth.<br>
• <strong>Plate Load Test (PLT):</strong> Evaluates ultimate bearing capacity and settlement of footings in-situ.<br>
• <strong>Field Vane Shear Test:</strong> Determines in-situ undrained shear strength of soft cohesive soils.<br>
2. <strong>Laboratory Tests:</strong><br>
• <strong>Grain Size Analysis:</strong> Sieve analysis and hydrometer test for soil classification.<br>
• <strong>Atterberg Limits:</strong> Liquid limit and plastic limit tests to determine soil plasticity.<br>
• <strong>Shear Strength Tests:</strong> Direct shear box test and triaxial shear test (UU, CU, CD) to find c and &phi;.<br>
• <strong>Consolidation Test:</strong> Oedometer test to determine compression index and rate of settlement."""
    },
    {
        "id": '2022-Q5b',
        "year": '2022',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (b)',
        "marks": 2,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL1 (Remember)',
        "pi": '1.4.1',
        "topic": "Objectives & Purpose of Geotechnical Soil Exploration / Investigation",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Describe the purpose of soil investigation.""",
        "solution": r"""<strong>Purpose of Soil Investigation:</strong><br>
1. <strong>Foundation Selection:</strong> To determine the most suitable, safe, and economical type and depth of foundation for the proposed structure.<br>
2. <strong>Bearing Capacity Evaluation:</strong> To calculate the safe bearing capacity of soil to prevent shear failure under building loads.<br>
3. <strong>Settlement Prediction:</strong> To estimate total and differential settlements and ensure they remain within permissible structural limits.<br>
4. <strong>Earth Pressure Assessment:</strong> To provide design parameters (K<sub>a</sub>, K<sub>p</sub>) for retaining walls, basement walls, and temporary shoring.<br>
5. <strong>Groundwater Observation:</strong> To locate the groundwater table and its seasonal fluctuations, identifying dewatering and waterproofing requirements.<br>
6. <strong>Construction Risk Mitigation:</strong> To identify problematic soils (expansive Black Cotton soil, collapsible soils, high water seepage) before construction begins."""
    },
    {
        "id": '2022-Q5c',
        "year": '2022',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (c)',
        "marks": 3,
        "type": 'Numerical',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "Soil Sampler Criteria: Area Ratio (Ar), Clearance Ratios (Ci, Co) & Recovery Ratio",
        "repeated": True,
        "rep_frequency": "2 of 4 Papers (50% Medium Probability)",
        "question": r"""Calculate the area ratio of a thin walled tube sampler having an external diameter of 6 cm and a wall thickness of 2.25 mm. Do you recommend the sampler for obtaining undisturbed soil samples? Why?""",
        "solution": r"""<strong>Given:</strong> External diameter D<sub>2</sub> = 6.0 cm = 60.0 mm, Wall thickness t = 2.25 mm.<br>
<strong>1. Internal Diameter (D<sub>1</sub>):</strong><br>
<code>D<sub>1</sub> = D<sub>2</sub> - 2t = 60.0 - 2(2.25) = 60.0 - 4.5 = <strong>55.5 mm</strong></code>.<br>
<strong>2. Area Ratio (A<sub>r</sub>):</strong><br>
<code>A<sub>r</sub> = [ (D<sub>2</sub>&sup2; - D<sub>1</sub>&sup2;) / D<sub>1</sub>&sup2; ] &times; 100%</code><br>
<code>D<sub>2</sub>&sup2; = 60&sup2; = 3600 mm&sup2;, D<sub>1</sub>&sup2; = 55.5&sup2; = 3080.25 mm&sup2;</code>.<br>
<code>A<sub>r</sub> = [ (3600 - 3080.25) / 3080.25 ] &times; 100% = [ 519.75 / 3080.25 ] &times; 100% = <strong>16.87%</strong></code>.<br>
<strong>3. Recommendation & Justification:</strong><br>
<strong>Recommendation:</strong> Yes, this sampler is acceptable for obtaining good quality undisturbed samples in cohesive soils. Per IS: 1892, an area ratio &le; 10% is ideal for extremely sensitive soils, but A<sub>r</sub> up to <strong>20%</strong> is permissible in normal medium-to-stiff clays. Because 16.87% < 20%, minimal soil displacement occurs, keeping perimeter edge disturbance low."""
    },
    {
        "id": '2022-Q5d',
        "year": '2022',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (d)',
        "marks": 7,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections",
        "repeated": True,
        "rep_frequency": "4 of 4 Papers (100% Guaranteed)",
        "question": r"""Illustrate the standard penetration test used in soil exploration. List the information that can be obtained by the test when made in (a) clay (b) sand. Comment on the correction factors to be used for calculating N.""",
        "solution": r"""<strong>Standard Penetration Test (SPT) &amp; Information Obtained:</strong><br>
<span class="is-code-chip">IS: 2131</span><br>
1. <strong>Test Procedure:</strong> Split-spoon sampler (50.8 mm OD, 35 mm ID) driven into borehole bottom by 63.5 kg hammer falling 750 mm. Blows for last 300 mm = <strong>Observed N-value</strong>.<br>
<div class="sol-diagram-box">
  <div class="sol-diagram-title">Figure: Standard Penetration Test (SPT) Setup per IS: 2131 &amp; Drive Sequence</div>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 370" class="sol-diagram-svg" width="100%" style="max-width:640px;height:auto;display:block;">
    <defs>
      <marker id="spt-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--pastel-peach-foreground, #f97316)" />
      </marker>
    </defs>

    <!-- ==================== LEFT: FIELD RIG ELEVATION ==================== -->
    <!-- Tripod Legs -->
    <line x1="50" y1="180" x2="165" y2="40" stroke="var(--foreground)" stroke-width="2.5" />
    <line x1="280" y1="180" x2="165" y2="40" stroke="var(--foreground)" stroke-width="2.5" />
    <line x1="165" y1="180" x2="165" y2="40" stroke="var(--muted-foreground)" stroke-width="1.4" stroke-dasharray="4 2" />

    <!-- Crown Pulley -->
    <circle cx="165" cy="40" r="12" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="2" />
    <circle cx="165" cy="40" r="3" fill="var(--foreground)" />

    <!-- Hoisting Rope -->
    <path d="M 153 40 L 153 105" stroke="var(--muted-foreground)" stroke-width="1.8" />
    <path d="M 177 40 L 250 140" stroke="var(--muted-foreground)" stroke-width="1.2" stroke-dasharray="2 2" />

    <!-- 63.5 kg Donut Drop Hammer - Vivid Coral -->
    <rect x="135" y="92" width="60" height="24" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="2" rx="3" />
    <text x="165" y="108" fill="var(--pastel-peach-foreground, #f97316)" font-size="9.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">63.5 kg</text>

    <!-- Free Fall Height Dimension (750 mm) -->
    <line x1="210" y1="92" x2="210" y2="148" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <line x1="205" y1="92" x2="215" y2="92" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <line x1="205" y1="148" x2="215" y2="148" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" />
    <text x="220" y="124" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="800" font-family="system-ui, sans-serif">750 mm</text>

    <!-- Anvil & Drive Head -->
    <rect x="145" y="148" width="40" height="12" fill="var(--foreground)" stroke="var(--foreground)" stroke-width="1.4" rx="2" />
    <text x="165" y="157" fill="var(--background)" font-size="7.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">ANVIL</text>

    <!-- Ground Level GL -->
    <line x1="30" y1="180" x2="310" y2="180" stroke="var(--foreground)" stroke-width="2" />
    <text x="35" y="174" fill="var(--foreground)" font-size="9.5" font-weight="700" font-family="system-ui, sans-serif">Ground Level (&plusmn;0.00)</text>

    <!-- Casing Pipe -->
    <rect x="147" y="180" width="36" height="105" fill="var(--pastel-sky-bg)" opacity="0.4" stroke="var(--foreground)" stroke-width="1.4" />
    <text x="135" y="235" fill="var(--muted-foreground)" font-size="8.5" text-anchor="end" font-family="system-ui, sans-serif">Casing</text>

    <!-- Drill Rods -->
    <line x1="165" y1="160" x2="165" y2="285" stroke="var(--foreground)" stroke-width="3" />

    <!-- Split Spoon Sampler at Borehole Base -->
    <rect x="153" y="285" width="24" height="60" fill="var(--secondary)" stroke="var(--foreground)" stroke-width="1.6" />
    <polygon points="153,345 165,360 177,345" fill="var(--foreground)" />
    <text x="165" y="320" fill="var(--foreground)" font-size="8" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">IS: 2131</text>

    <!-- ==================== RIGHT: PENETRATION SEQUENCE INSET ==================== -->
    <g transform="translate(340, 25)">
      <rect x="0" y="0" width="280" height="320" fill="var(--card)" stroke="var(--secondary)" stroke-width="1.4" rx="8" />
      
      <text x="140" y="24" fill="var(--foreground)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">Split-Spoon Drive Sequence (450 mm)</text>
      <text x="140" y="38" fill="var(--muted-foreground)" font-size="9" text-anchor="middle" font-family="system-ui, sans-serif">Penetration divided into three 150 mm stages:</text>

      <!-- Stage 1: Seating Drive (0 - 150 mm) -->
      <g transform="translate(18, 52)">
        <rect x="0" y="0" width="45" height="42" fill="var(--secondary)" stroke="var(--muted-foreground)" stroke-width="1.2" rx="3" />
        <text x="22" y="25" fill="var(--muted-foreground)" font-size="9" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">150mm</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">0 - 150 mm (Seating Drive)</text>
        <text x="55" y="31" fill="var(--muted-foreground)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; DISCARDED (Disturbed soil)</text>
      </g>

      <!-- Stage 2: First Test Drive (150 - 300 mm) -->
      <g transform="translate(18, 102)">
        <rect x="0" y="0" width="45" height="42" fill="var(--pastel-sky-bg)" stroke="var(--pastel-sky-foreground, #0ea5e9)" stroke-width="1.6" rx="3" />
        <text x="22" y="26" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">N1</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">150 - 300 mm (Test Drive 1)</text>
        <text x="55" y="31" fill="var(--pastel-sky-foreground, #0ea5e9)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; Record blow count = N1</text>
      </g>

      <!-- Stage 3: Second Test Drive (300 - 450 mm) -->
      <g transform="translate(18, 152)">
        <rect x="0" y="0" width="45" height="42" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.6" rx="3" />
        <text x="22" y="26" fill="var(--pastel-peach-foreground, #f97316)" font-size="10" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">N2</text>
        <text x="55" y="17" fill="var(--foreground)" font-size="10" font-weight="700" font-family="system-ui, sans-serif">300 - 450 mm (Test Drive 2)</text>
        <text x="55" y="31" fill="var(--pastel-peach-foreground, #f97316)" font-size="9" font-weight="700" font-family="system-ui, sans-serif">&bull; Record blow count = N2</text>
      </g>

      <!-- SPT N Formula Badge -->
      <rect x="15" y="206" width="250" height="34" fill="var(--pastel-peach-bg)" stroke="var(--pastel-peach-foreground, #f97316)" stroke-width="1.5" rx="5" />
      <text x="140" y="227" fill="var(--pastel-peach-foreground, #f97316)" font-size="11.5" font-weight="800" text-anchor="middle" font-family="system-ui, sans-serif">SPT Blow Count N = N1 + N2</text>

      <!-- Corrections Summary -->
      <text x="15" y="258" fill="var(--foreground)" font-size="9.5" font-weight="800" font-family="system-ui, sans-serif">Standard Corrections:</text>
      <text x="15" y="274" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">1. Overburden: N' = CN &times; N &nbsp;(CN = 350 / (&sigma;' + 70))</text>
      <text x="15" y="290" fill="var(--muted-foreground)" font-size="8.5" font-family="system-ui, sans-serif">2. Dilatancy (Fine Sand, N'&gt;15): N'' = 15 + 0.5(N' - 15)</text>
    </g>
  </svg>
</div><br>
2. <strong>Corrections:</strong><br>
• Overburden: N' = N<sub>0</sub> × [350 / (σ'<sub>v</sub> + 70)] for σ'<sub>v</sub> ≤ 280 kPa.<br>
• Dilatancy: N'' = 15 + 0.5 (N' - 15) for saturated fine sand/silt when N' &gt; 15.<br>
3. <strong>Information Obtained:</strong><br>
• <strong>Sand:</strong> Relative density D<sub>r</sub> (N &lt; 4 Very loose to N &gt; 50 Very dense), friction angle φ ≈ 27.1° + 0.3 N', liquefaction risk.<br>
• <strong>Clay:</strong> Unconfined compressive strength q<sub>u</sub> ≈ 12.5 N (kPa), consistency.<br>
• <strong>Design:</strong> Safe bearing capacity of footings and pile capacities."""
    },
    {
        "id": '2022-Q5e-OR',
        "year": '2022',
        "unit": 5,
        "unit_name": "Soil Exploration & In-Situ Testing",
        "q_no": 'Q.5 (e) OR',
        "marks": 7,
        "type": 'Theory',
        "co": 'CO5',
        "bl": 'BL2 (Understand)',
        "pi": '2.1.2',
        "topic": "Methods of Subsoil Exploration (Boring, Sounding, Trial Pits, Geophysical)",
        "repeated": True,
        "rep_frequency": "3 of 4 Papers (75% High Probability)",
        "question": r"""Classify the various methods of soil exploration and mention the circumstances under which each is best situated.""",
        "solution": r"""<strong>Classification of Soil Exploration Methods &amp; Circumstances:</strong><br>
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
    }
]

print(f"Loaded {len(questions)} verified questions.")
