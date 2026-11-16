import re
import json
import sys
import os

sys.path.insert(0, os.path.abspath("."))

# Read compile_data.py
with open("compile_data.py", "r", encoding="utf-8") as f:
    compile_code = f.read()

# Also import compile_data to get the SVG blocks
import compile_data

q_dict = {q['id']: q for q in compile_data.questions}

# Extract diagram boxes
def get_diagram_box(qid):
    sol = q_dict[qid]['solution']
    m = re.search(r'(<div class="sol-diagram-box">.*?</div>\s*)$', sol, re.DOTALL)
    if m:
        return "\n" + m.group(1).strip()
    return ""

diag_2024_q2b = get_diagram_box('2024-Q2b')
diag_2024_q5b = get_diagram_box('2024-Q5b')
diag_2023_q4a = get_diagram_box('2023-Q4a')

assert diag_2024_q2b, "Missing diagram box for 2024-Q2b"
assert diag_2024_q5b, "Missing diagram box for 2024-Q5b"
assert diag_2023_q4a, "Missing diagram box for 2023-Q4a"
print("Extracted SVG diagram boxes successfully!")

NEW_SOLUTIONS = {
    '2024-Q1a': r"""<strong>Three Types of Earth Pressure with Examples:</strong><br>
1. <strong>Active Earth Pressure:</strong> Pressure exerted by soil when the retaining wall moves away from the backfill.<br>
<em>Example:</em> A retaining wall tilting away from soil.<br>
2. <strong>Passive Earth Pressure:</strong> Resistance offered by soil when the retaining wall moves towards the backfill.<br>
<em>Example:</em> Soil resisting the movement of a sheet pile wall.<br>
3. <strong>Earth Pressure at Rest:</strong> Pressure exerted by soil when the retaining wall does not move.<br>
<em>Example:</em> Basement walls restrained by rigid supports.""",

    '2024-Q1b': r"""<strong>Assumptions of Coulomb's Earth Pressure Theory:</strong><br>
1. Soil is homogeneous and isotropic.<br>
2. Soil is dry and cohesionless.<br>
3. Backfill surface is a plane.<br>
4. Failure surface is a plane passing through the heel of the wall.<br>
5. Wall surface is straight and rigid.<br>
6. Friction develops between the wall and soil.<br>
7. Soil wedge behaves as a rigid body at failure.""",

    '2024-Q2a': r"""<strong>Factors Affecting Factor of Safety of Infinite Slope in Clay:</strong><br>
1. <strong>Slope Angle (&beta;):</strong> Steeper slope angle increases gravitational shear stress along the slip plane, reducing the factor of safety.<br>
2. <strong>Soil Cohesion (c'):</strong> Cohesion provides the primary shearing resistance in clay; higher cohesion directly increases the factor of safety.<br>
3. <strong>Depth of Slip Plane (H):</strong> In clay slopes, factor of safety decreases with depth because driving weight increases faster than cohesive resistance.<br>
4. <strong>Groundwater Seepage &amp; Pore Pressure:</strong> Seepage creates pore water pressure, reducing effective normal stress and cutting safety by up to 50%.<br>
5. <strong>Unit Weight of Soil (&gamma;):</strong> Higher unit weight of saturated soil increases the downslope driving force.""",

    '2024-Q2b': r"""<strong>Three Types of Shear Failure in Soil:</strong><br>
1. <strong>General Shear Failure:</strong> Occurs in dense sand and stiff clay. Continuous failure surface extends from footing edge to ground surface with distinct soil bulging and sudden tilting.<br>
2. <strong>Local Shear Failure:</strong> Occurs in medium dense sand and medium clay. Failure surfaces terminate within the soil mass, resulting in slight ground heave and gradual settlement.<br>
3. <strong>Punching Shear Failure:</strong> Occurs in loose sand and soft clay. Footing sinks vertically straight down into the soil by perimeter shearing, with zero ground heave and continuous plunging settlement.<br>""" + diag_2024_q2b,

    '2024-Q3a': r"""<strong>Major Design Criteria for Foundations:</strong><br>
1. <strong>Shear Failure Criterion:</strong> Foundation must have an adequate factor of safety (FOS &ge; 2.5 to 3.0) against shear failure of supporting soil under maximum applied loads.<br>
2. <strong>Settlement Criterion:</strong> Total and differential settlements must stay within safe permissible limits specified by codes (IS: 1904) to prevent structural damage or distortion.<br>
3. <strong>Depth Criterion:</strong> Foundation must be placed at sufficient depth below topsoil, frost line, and seasonal moisture swelling/shrinkage zone (minimum depth &ge; 0.5 m to 1.0 m).<br>
4. <strong>Location &amp; Environmental Safety:</strong> Foundation must be safe against scour from flowing water, erosion, and undermining from adjacent excavations.""",

    '2024-Q3b': r"""<strong>Settlement of Foundation:</strong><br>
Total foundation settlement consists of three components:<br>
<code>S_{total} = S_i + S_c + S_s</code><br>
1. <strong>Immediate (Elastic) Settlement (S<sub>i</sub>):</strong> Occurs instantly upon load application due to elastic deformation without change in water content.<br>
2. <strong>Primary Consolidation Settlement (S<sub>c</sub>):</strong> Time-dependent settlement in saturated clay caused by the gradual expulsion of pore water under sustained load.<br>
3. <strong>Secondary Settlement (S<sub>s</sub>):</strong> Very slow plastic deformation of soil skeleton occurring after excess pore water pressure has fully dissipated.<br>
4. <strong>Permissible Limits:</strong> Maximum permissible total settlement for isolated footings is 40 mm in sand and 65 mm in clay (per IS: 1904).""",

    '2024-Q4a': r"""<strong>Group Action of Piles:</strong><br>
1. <strong>Group Action:</strong> Piles are installed in clusters connected by a rigid pile cap to transmit heavy structural loads into the ground.<br>
2. <strong>Stress Overlap:</strong> Stress zones of closely spaced individual piles overlap in the soil, which can reduce individual pile efficiency and increase group settlement.<br>
3. <strong>Failure Modes:</strong> A pile group in clay may fail either by individual pile failure (Q<sub>g</sub> = n &middot; Q<sub>u</sub>) or as one large solid block (Q<sub>block</sub>). Design capacity is the lesser of the two.<br>
4. <strong>Group Efficiency (&eta;<sub>g</sub>):</strong> Ratio of group capacity to the sum of individual capacities: &eta;<sub>g</sub> = Q<sub>group</sub> / (n &middot; Q<sub>single</sub>) &times; 100%. In sand &eta;<sub>g</sub> &gt; 100%, while in clay &eta;<sub>g</sub> &le; 100%.<br>
5. <strong>Pile Spacing:</strong> Standard center-to-center spacing is 2.5 to 3.5 times the pile diameter for friction piles.""",

    '2024-Q4b': r"""<strong>Under-Reamed Pile Foundation:</strong><br>
1. <strong>Definition:</strong> Bored cast-in-situ concrete piles with one or more enlarged bulbs (under-reams) along their shaft.<br>
2. <strong>Primary Application:</strong> Specially designed for expansive soils (Black Cotton soil) that undergo severe swelling in monsoon and shrinkage in summer.<br>
3. <strong>Bulb Dimensions:</strong> Bulb diameter is typically 2.0 to 2.5 times the stem diameter, drilled using an under-reaming tool.<br>
4. <strong>Anchorage Mechanism:</strong> The bulb is anchored deep below the active seasonal moisture zone (&gt; 1.5 m to 3.5 m) to resist upward swelling and pullout forces.<br>
5. <strong>Load Capacity:</strong> Enlarged bulb provides a large base bearing area for downward compressive loads and high uplift resistance.""",

    '2024-Q5a': r"""<strong>Objectives of Soil Exploration:</strong><br>
1. To determine the depth, thickness, and extent of each soil and rock stratum across the site.<br>
2. To locate the groundwater table and monitor its seasonal fluctuations.<br>
3. To obtain disturbed and undisturbed soil samples for identification and laboratory testing.<br>
4. To evaluate engineering properties of soil (shear strength, compressibility, permeability, and bearing capacity).<br>
5. To select the most suitable, safe, and economical type and depth of foundation.<br>
6. To identify potential construction hazards (excavation collapse, dewatering requirements, expansive soils).""",

    '2024-Q5b': r"""<strong>Typical Borelog Layout and Features:</strong><br>
1. <strong>Header Information:</strong> Project title, borehole number (BH-01), ground surface elevation (RL), date of boring, and drilling method.<br>
2. <strong>Strata Description:</strong> Layer depth boundaries, thickness, and standard engineering classification/symbols of each stratum.<br>
3. <strong>Groundwater Level:</strong> Exact depth where groundwater table (GWT) was encountered during drilling and stabilized.<br>
4. <strong>Sampling &amp; Field Test Data:</strong> Depth of collected samples, sample type (disturbed/undisturbed), and recorded SPT N-values.<br>""" + diag_2024_q5b,

    '2023-Q1a': r"""<strong>Types of Earth Pressure and Classical Theories:</strong><br>
1. <strong>Three Types of Earth Pressure:</strong><br>
• <strong>Active Earth Pressure:</strong> Pressure exerted when the retaining wall moves away from the backfill.<br>
<em>Example:</em> A cantilever retaining wall tilting away from soil.<br>
• <strong>Passive Earth Pressure:</strong> Resistance offered when the retaining wall moves towards the backfill.<br>
<em>Example:</em> Soil resisting the movement of an anchor deadman or sheet pile.<br>
• <strong>Earth Pressure at Rest:</strong> Pressure exerted when the retaining wall does not move.<br>
<em>Example:</em> Rigid basement walls restrained by floor slabs.<br>
2. <strong>Two Classical Theories:</strong><br>
• <strong>Rankine's Theory (1857):</strong> Considers plastic equilibrium of a semi-infinite soil mass, assuming a vertical, smooth (frictionless) wall back.<br>
• <strong>Coulomb's Theory (1776):</strong> Considers equilibrium of a planar sliding rigid soil wedge, accounting for wall friction and inclined wall back.""",

    '2023-Q2a': r"""<strong>Bearing Capacity Definitions and Common Suffixes:</strong><br>
<strong>Bearing Capacity:</strong> The load carrying capacity of soil per unit area without undergoing shear failure or excessive settlement.<br>
1. <strong>Ultimate Bearing Capacity (q<sub>u</sub>):</strong> The minimum gross contact pressure at which the supporting soil fails completely in shear.<br>
2. <strong>Net Ultimate Bearing Capacity (q<sub>net_u</sub>):</strong> The minimum net pressure above overburden pressure causing shear failure: q<sub>net_u</sub> = q<sub>u</sub> - &gamma;D<sub>f</sub>.<br>
3. <strong>Safe Bearing Capacity (q<sub>safe</sub>):</strong> The safe gross pressure on soil with an adequate factor of safety: q<sub>safe</sub> = q<sub>net_u</sub> / FOS + &gamma;D<sub>f</sub>.<br>
4. <strong>Allowable Bearing Capacity (q<sub>a</sub>):</strong> The maximum net pressure permitted on soil considering both shear failure safety and permissible settlement limits.""",

    '2023-Q3a': r"""<strong>Coulomb's Law of Shear Strength of Soil:</strong><br>
1. <strong>Total Stress Equation (Coulomb, 1776):</strong> Shear strength (&tau;) consists of cohesive resistance and frictional resistance:<br>
<code>\tau = c + \sigma \tan\phi</code><br>
where c = cohesion, &sigma; = total normal stress on failure plane, &phi; = angle of internal friction.<br>
2. <strong>Effective Stress Equation (Terzaghi, 1925):</strong> Shear strength is governed by effective stress between soil grains:<br>
<code>\tau = c' + \sigma' \tan\phi' = c' + (\sigma - u) \tan\phi'</code><br>
where c' = effective cohesion, &sigma;' = effective normal stress, u = pore water pressure, &phi;' = effective friction angle.<br>
3. <strong>Special Cases:</strong><br>
• Pure Sand (c = 0): &tau; = &sigma; tan&phi;<br>
• Saturated Clay in Undrained Shear (&phi; = 0): &tau; = c<sub>u</sub>""",

    '2023-Q4a': r"""<strong>Types of Shallow Foundations and Strap Footing:</strong><br>
1. <strong>Types of Shallow Foundations:</strong><br>
• Isolated column footing (pad, stepped, sloped)<br>
• Strip or continuous wall footing<br>
• Combined footing (rectangular or trapezoidal)<br>
• Strap (cantilever) footing<br>
• Raft (mat) foundation<br>
2. <strong>Strap Footing Concept:</strong><br>
• Used when an exterior column sits on a property line and its footing cannot extend outward.<br>
• A rigid RCC strap beam connects the eccentric exterior footing to an adjacent interior footing to prevent overturning.<br>
• The strap beam is suspended above ground (no contact with soil underneath) so it transfers bending moment and shear only.<br>""" + diag_2023_q4a,

    '2022-Q1a': r"""<strong>Depth of Tension Cracks Calculation:</strong><br>
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
<em>(Maximum critical unsupported excavation depth H<sub>c</sub> = 2 z<sub>c</sub> = 9.53 m).</em>""",

    '2022-Q1b': r"""<strong>Increase in Active Earth Pressure Intensity Calculation:</strong><br>
<strong>Given Data:</strong><br>
Wall height H = 5 m, &phi; = 30&deg;, &gamma; = 18 kN/m&sup3;, Surcharge q = 45 kN/m&sup2;.<br>
1. <strong>Active Earth Pressure Coefficient (K<sub>a</sub>):</strong><br>
<code>K_a = \frac{1 - \sin 30^\circ}{1 + \sin 30^\circ} = \frac{1 - 0.5}{1 + 0.5} = \frac{0.5}{1.5} = \frac{1}{3} = 0.3333</code><br>
2. <strong>Increase in Active Pressure Intensity (&Delta;p<sub>a</sub>):</strong><br>
A uniform surface surcharge q transmits a constant horizontal pressure intensity over the entire depth of the wall:<br>
<code>\Delta p_a = K_a \cdot q = \frac{1}{3} \times 45 = 15.0\text{ kN/m}^2\text{ (15 kPa)}</code><br>
3. <strong>Final Result:</strong><br>
Increase in active earth pressure intensity at the bottom = <strong>15.0 kN/m&sup2;</strong>.""",

    '2022-Q2a': r"""<strong>Differences Between Direct Shear Box Test and Triaxial Shear Test:</strong><br>
1. <strong>Failure Plane:</strong> Direct shear test forces failure along a predetermined horizontal plane, whereas in a triaxial test, failure occurs along the natural weakest plane.<br>
2. <strong>Drainage Control:</strong> Direct shear test provides poor drainage control and cannot measure pore water pressure, whereas triaxial test provides complete drainage control and accurate pore pressure measurement.<br>
3. <strong>Stress Distribution:</strong> Direct shear test has non-uniform stress distribution with stress concentrations at edges, whereas triaxial test maintains uniform stress conditions throughout the cylindrical sample.<br>
4. <strong>Soil Applicability:</strong> Direct shear test is best suited for coarse-grained cohesionless sands, whereas triaxial test is suitable for all soil types under UU, CU, and CD conditions.<br>
5. <strong>Strength Parameters:</strong> Direct shear test measures total stress parameters only, whereas triaxial test determines both total and effective stress parameters.""",

    '2022-Q2b': r"""<strong>Unconsolidated Undrained (UU) and Consolidated Drained (CD) Tests:</strong><br>
1. <strong>Unconsolidated Undrained (UU) Test:</strong> Drainage is kept closed during both the cell pressure stage and shearing stage. It is a rapid test (takes 5 to 10 minutes) with no dissipation of excess pore water pressure, measuring undrained shear strength (c<sub>u</sub>).<br>
<em>Example:</em> Short-term foundation stability immediately after rapid construction on clay.<br>
2. <strong>Consolidated Drained (CD) Test:</strong> Drainage is kept open during both the cell pressure stage and shearing stage. It is a very slow test (takes days to weeks) allowing excess pore water pressure to fully dissipate (u = 0), measuring effective shear strength parameters (c', &phi;').<br>
<em>Example:</em> Long-term permanent stability analysis of natural earth slopes and retaining walls.""",

    '2022-Q3a': r"""<strong>Assumptions of Terzaghi's Bearing Capacity Theory:</strong><br>
1. Soil is homogeneous, isotropic, and semi-infinite.<br>
2. Footing is a continuous strip with infinite length (L/B &rarr; &infin;), forming a two-dimensional plane-strain condition.<br>
3. Foundation is shallow, with depth of embedment D<sub>f</sub> &le; width of footing B.<br>
4. Base of the footing is rough, preventing soil slipping along the contact surface.<br>
5. Soil above the foundation base level is replaced by an equivalent surcharge q = &gamma;D<sub>f</sub> (shear resistance above base level is neglected).<br>
6. General shear failure occurs in the supporting soil mass.<br>
7. Soil behaves as a rigid-plastic material obeying Mohr-Coulomb failure criterion (&tau; = c + &sigma; tan&phi;).""",

    '2022-Q3b': r"""<strong>Factors Affecting Bearing Capacity of a Shallow Footing:</strong><br>
1. <strong>Shear Strength of Soil (c and &phi;):</strong> Higher cohesion and higher angle of internal friction increase bearing capacity factors exponentially.<br>
2. <strong>Footing Width (B):</strong> In granular soils (sand), bearing capacity increases linearly with footing width (0.5 &gamma; B N<sub>&gamma;</sub>).<br>
3. <strong>Depth of Embedment (D<sub>f</sub>):</strong> Deeper footing placement increases the confining surcharge pressure (&gamma; D<sub>f</sub> N<sub>q</sub>), directly increasing bearing capacity.<br>
4. <strong>Water Table Location:</strong> When groundwater rises to the foundation level, submerged unit weight (&gamma;') replaces &gamma;, reducing bearing capacity by up to 50%.<br>
5. <strong>Shape of Footing:</strong> Circular and square footings have higher bearing capacities per unit area than continuous strip footings due to 3D shape factors.<br>
6. <strong>Unit Weight of Soil (&gamma;):</strong> Denser soil with higher unit weight provides greater resistance to shear displacement.""",

    '2022-Q4a': r"""<strong>Functions of Pile Foundation:</strong><br>
1. <strong>End-Bearing Load Transfer:</strong> Transfers heavy building loads through weak, compressible top layers down to deep stiff soil or solid bedrock.<br>
2. <strong>Skin Friction Load Transfer:</strong> Distributes structural loads along the surface area of the pile shaft by friction in deep uniform clay or sand strata.<br>
3. <strong>Resisting Uplift Forces:</strong> Anchors tall structures (transmission towers, chimneys, transmission masts) against upward tension and wind overturning moments.<br>
4. <strong>Resisting Lateral Loads:</strong> Resists horizontal lateral forces caused by wind, earthquakes, earth pressures, and water wave impacts on bridge piers and docks.<br>
5. <strong>Soil Compaction:</strong> Compaction piles densify loose granular deposits, increasing bearing capacity and mitigating earthquake liquefaction risk.""",

    '2022-Q4b': r"""<strong>Differences in Bearing Capacity Computation of Shallow and Deep Foundations:</strong><br>
1. <strong>Load Transfer Mechanism:</strong> Shallow foundations carry load through base contact bearing pressure only (q<sub>u</sub>), whereas deep foundations (piles) carry load through both base resistance (Q<sub>b</sub>) and shaft skin friction (Q<sub>s</sub>).<br>
2. <strong>Surcharge Pressure:</strong> In shallow foundations, surcharge is taken as full depth q = &gamma;D<sub>f</sub>, whereas in deep foundations, effective vertical stress increases only up to a critical depth (10d to 20d) and then stays constant.<br>
3. <strong>Bearing Capacity Factors:</strong> Shallow foundations use Terzaghi factors (e.g., N<sub>c</sub> = 5.7 for strip footing in clay), whereas deep foundations use deep cavity expansion factors (e.g., N<sub>c</sub>* = 9.0 per Skempton).<br>
4. <strong>Failure Surface Extent:</strong> Shallow foundation failure planes extend outwards and upwards all the way to ground surface with visible heave, whereas pile failure surfaces are localized around the pile tip and shaft without ground heaving.<br>
5. <strong>Settlement Influence:</strong> Shallow foundations are often governed and restricted by settlement criteria, whereas deep foundations mobilize high load capacity at small settlements.""",

    '2022-Q5a': r"""<strong>Laboratory and Field Tests in Soil Investigation:</strong><br>
1. <strong>Field (In-Situ) Tests:</strong><br>
• <strong>Standard Penetration Test (SPT):</strong> Determines N-value, relative density of sands, and consistency of clays.<br>
• <strong>Cone Penetration Test (CPT):</strong> Measures point resistance and sleeve friction continuously with depth.<br>
• <strong>Plate Load Test (PLT):</strong> Evaluates ultimate bearing capacity and settlement of footings in-situ.<br>
• <strong>Field Vane Shear Test:</strong> Determines in-situ undrained shear strength of soft cohesive soils.<br>
2. <strong>Laboratory Tests:</strong><br>
• <strong>Grain Size Analysis:</strong> Sieve analysis and hydrometer test for soil classification.<br>
• <strong>Atterberg Limits:</strong> Liquid limit and plastic limit tests to determine soil plasticity.<br>
• <strong>Shear Strength Tests:</strong> Direct shear box test and triaxial shear test (UU, CU, CD) to find c and &phi;.<br>
• <strong>Consolidation Test:</strong> Oedometer test to determine compression index and rate of settlement.""",

    '2022-Q5b': r"""<strong>Purpose of Soil Investigation:</strong><br>
1. <strong>Foundation Selection:</strong> To determine the most suitable, safe, and economical type and depth of foundation for the proposed structure.<br>
2. <strong>Bearing Capacity Evaluation:</strong> To calculate the safe bearing capacity of soil to prevent shear failure under building loads.<br>
3. <strong>Settlement Prediction:</strong> To estimate total and differential settlements and ensure they remain within permissible structural limits.<br>
4. <strong>Earth Pressure Assessment:</strong> To provide design parameters (K<sub>a</sub>, K<sub>p</sub>) for retaining walls, basement walls, and temporary shoring.<br>
5. <strong>Groundwater Observation:</strong> To locate the groundwater table and its seasonal fluctuations, identifying dewatering and waterproofing requirements.<br>
6. <strong>Construction Risk Mitigation:</strong> To identify problematic soils (expansive Black Cotton soil, collapsible soils, high water seepage) before construction begins."""
}

assert len(NEW_SOLUTIONS) == 24, f"Expected 24 solutions, got {len(NEW_SOLUTIONS)}"

# Update compile_code using regex replacement for each question block
for qid, new_sol in NEW_SOLUTIONS.items():
    # Find question block with this id
    pattern = rf'({re.escape(qid)}[\'\"]\s*,.*?\"solution\":\s*r?\"\"\")(.*?)(\"\"\"\s*}})'
    m = re.search(pattern, compile_code, re.DOTALL)
    if not m:
        # Try alternate pattern with single quotes
        pattern = rf'({re.escape(qid)}[\'\"]\s*,.*?\"solution\":\s*r?\'\'\')(.*?)(\'\'\'\s*}})'
        m = re.search(pattern, compile_code, re.DOTALL)
    
    assert m, f"Could not find solution block for {qid}"
    
    # Escape backslashes for replacement if needed
    prefix = m.group(1)
    suffix = m.group(3)
    
    # We do direct string replacement around match span
    start, end = m.span()
    replacement = prefix + new_sol + suffix
    compile_code = compile_code[:start] + replacement + compile_code[end:]
    print(f"Updated {qid} in compile_code")

# Write updated compile_data.py
with open("compile_data.py", "w", encoding="utf-8") as f:
    f.write(compile_code)

print("Saved updated compile_data.py successfully!")

# Also update canonical_data.json where relevant
with open("canonical_data.json", "r", encoding="utf-8") as f:
    canonical = json.load(f)

for topic in canonical:
    if topic['id'] == 'u1-earth-pressure-types':
        topic['master_solution'] = NEW_SOLUTIONS['2024-Q1a']
        print("Updated canonical topic u1-earth-pressure-types")
    elif topic['id'] == 'u2-direct-shear-vs-triaxial':
        topic['master_solution'] = NEW_SOLUTIONS['2022-Q2a']
        print("Updated canonical topic u2-direct-shear-vs-triaxial")
    elif topic['id'] == 'u3-terzaghi-assumptions':
        topic['master_solution'] = NEW_SOLUTIONS['2022-Q3a'] + "<br><br>" + NEW_SOLUTIONS['2022-Q3b']
        print("Updated canonical topic u3-terzaghi-assumptions")
    elif topic['id'] == 'u4-pile-group-action-efficiency':
        topic['master_solution'] = NEW_SOLUTIONS['2024-Q4a'] + "<br><br>" + NEW_SOLUTIONS['2022-Q4b']
        print("Updated canonical topic u4-pile-group-action-efficiency")
    elif topic['id'] == 'u4-under-reamed-piles':
        topic['master_solution'] = NEW_SOLUTIONS['2024-Q4b']
        print("Updated canonical topic u4-under-reamed-piles")

with open("canonical_data.json", "w", encoding="utf-8") as f:
    json.dump(canonical, f, indent=2, ensure_ascii=False)

print("Saved updated canonical_data.json successfully!")
