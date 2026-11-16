import json
import re
import compile_data

with open("canonical_data.json", "r", encoding="utf-8") as f:
    canonical = json.load(f)

# The 28 questions in 2025
q2025 = [
    {
        "q_no": "Q.1 (a)", "unit": 1, "marks": 2, "type": "Theory",
        "question": "What are different Types of Earth Pressure and what are different theories of Earth Pressures?"
    },
    {
        "q_no": "Q.1 (b) i", "unit": 1, "marks": 3, "type": "Numerical",
        "question": "A smooth vertical wall, 6 m high supports an inclined non cohesive backfill (φ = 32°; γ = 21 kN/m³) at an angle 10° with horizontal. Compute the total active & passive pressure at the bottom of wall."
    },
    {
        "q_no": "Q.1 (b) ii", "unit": 1, "marks": 3, "type": "Numerical",
        "question": "A rough vertical wall of 7.5 m height supports a horizontal backfill. If the angle of internal friction and angle of wall friction are respectively 33° and 12°, compute the passive earth pressure at the bottom of wall. Assume density of 18.5 kN/m³."
    },
    {
        "q_no": "Q.1 (b) iii", "unit": 1, "marks": 3, "type": "Numerical",
        "question": "A retaining wall of 4.5 m height carries a horizontal backfill with c = 35 kN/m², φ = 10°; γ = 17.2 kN/m³. The water table is located at 1.50 m below the ground. Sketch the distribution of active earth pressure. Assume the value of angle of internal friction is 14°; and cohesion c = 50 kN/m² in the submerged condition."
    },
    {
        "q_no": "Q.1 (c)", "unit": 1, "marks": 6, "type": "Derivation",
        "question": "Derive the condition of maximum active earth pressure from sliding wedge."
    },
    {
        "q_no": "Q.1 (c) OR", "unit": 1, "marks": 6, "type": "Theory / Derivation",
        "question": "Explain the Rebhann's graphical construction for active earth pressure and prove that it satisfy the condition of maximum earth pressure"
    },
    {
        "q_no": "Q.2 (a)", "unit": 2, "marks": 2, "type": "Theory",
        "question": "What do you mean by bearing capacity? What are the different suffixes to be used before bearing capacity?"
    },
    {
        "q_no": "Q.2 (b) i", "unit": 2, "marks": 3, "type": "Theory",
        "question": "Describe the three modes of shear failure in soil. Draw load-settlement curves for each mode and explain which type of soil exhibits each failure pattern."
    },
    {
        "q_no": "Q.2 (b) ii", "unit": 2, "marks": 3, "type": "Theory",
        "question": "Explain the effect of water table on bearing capacity of soils."
    },
    {
        "q_no": "Q.2 (b) iii", "unit": 2, "marks": 3, "type": "Numerical",
        "question": "Compute the net safe bearing capacity of a square footing of size 2.5 m, provided at 2.0 m depth in a purely cohesive soil with Unconfined Shear Strength of 150 kN/m² and density being 18 kN/m³. Use factor of safety as 2.5."
    },
    {
        "q_no": "Q.2 (c)", "unit": 2, "marks": 6, "type": "Numerical",
        "question": "A square footing of 3.5 m is resting at 3 m below the ground level. The shear parameters of soil are respectively 40 kN/m² and 12°. The density of soil is 20 kN/m³. The water table lies at 2 m below the base of footing. Calculate the net safe bearing capacity. Assume factor of safety of 3.0."
    },
    {
        "q_no": "Q.2 (c) OR", "unit": 2, "marks": 6, "type": "Numerical",
        "question": "A rectangular footing 3 m x 2 m carries a load of 1500 kN with eccentricity of 0.3 m along the length and 0.2 m along the width. The footing is located at 1.5 m depth in soil with c = 20 kN/m², φ = 25°, γ = 19 kN/m³. Calculate the maximum pressure at the base and check for safety."
    },
    {
        "q_no": "Q.3 (a)", "unit": 3, "marks": 2, "type": "Theory",
        "question": "Discuss Coulomb's law of shear strength of soil"
    },
    {
        "q_no": "Q.3 (b) i", "unit": 3, "marks": 3, "type": "Numerical",
        "question": "The shear stress and normal stress at a failure plane in a cohesionless soil mass were found to be 4 kPa and 10 kPa respectively. Determine the resultant stress on failure plane and inclination of failure plane. Also compute the shear parameters."
    },
    {
        "q_no": "Q.3 (b) ii", "unit": 3, "marks": 3, "type": "Numerical",
        "question": "The deviator force to shear the soil specimen of 38 mm diameter and 76 mm height under a confining pressure of 100 kN/m² is 251 N while it shears under a deviator force of 327 N at a confining pressure of 200 kN/m². The deformation at the time of failure is respectively 2.0 mm and 5.2 mm. Determine the shear parameters. Determine the deviator stress under confining pressure of 250 kPa."
    },
    {
        "q_no": "Q.3 (b) iii", "unit": 3, "marks": 3, "type": "Theory",
        "question": "Explain various kinds of triaxial tests. Which test is best suited for the cohesive soil deposit having a permeable layer immediately below the foundation level?"
    },
    {
        "q_no": "Q.3 (c)", "unit": 3, "marks": 6, "type": "Derivation",
        "question": "Derive a relationship between effective shear parameters and principal stresses."
    },
    {
        "q_no": "Q.3 (c) OR", "unit": 3, "marks": 6, "type": "Numerical",
        "question": "The following data refers to a triaxial compression tests performed on a soil sample. Determine the total and effective shear parameters of soil.\nCell Pressure: 80, 150, 210 kPa; Deviator Stress: 175, 240, 300 kPa; Pore pressure: 45, 50, 60 kPa"
    },
    {
        "q_no": "Q.4 (a)", "unit": 4, "marks": 2, "type": "Theory",
        "question": "What are different types of shallow foundations? Draw neat sketch of strap footing."
    },
    {
        "q_no": "Q.4 (b) i", "unit": 4, "marks": 3, "type": "Theory",
        "question": "Enumerate the requirements of satisfactory foundations."
    },
    {
        "q_no": "Q.4 (b) ii", "unit": 4, "marks": 3, "type": "Theory",
        "question": "Two buildings are to be constructed at two different sites. First site shows the low compressive cohesive soil profile up to 10 m depth followed by good quality rock up to 15 m depth below the ground while the second site is having expansive soil up to 5 m depth followed by good rock up to 10 m below the ground. G+4 story building is to be constructed at the first site while at the second site G+15 story building is to be constructed. Suggest the type of foundation at two different sites for the structures to be constructed."
    },
    {
        "q_no": "Q.4 (b) iii", "unit": 4, "marks": 3, "type": "Numerical",
        "question": "Using the soil properties (γ = 17.5 kN/m³, c = 20 kN/m², φ = 20°), and assuming the square footing (3.415 m x 3.415 m) located at a depth of 1.5 m carries a total load of 2000 kN. Calculate the immediate settlement of the footing using the elastic theory. Assume the soil is homogeneous and isotropic with a Poisson's ratio of 0.3 and Young's modulus of 50,000 kN/m². (assume influence factor 0.88 for square footing)"
    },
    {
        "q_no": "Q.4 (c)", "unit": 4, "marks": 6, "type": "Numerical",
        "question": "Design a square pile group to carry 500 kN load in clay with an unconfined compressive strength of 50 kN/m². Assume pile diameter of 400 mm and 6.0 m length. Adhesion factor may be taken as 0.6."
    },
    {
        "q_no": "Q.4 (c) OR", "unit": 4, "marks": 6, "type": "Numerical",
        "question": "Design a strip footing resting at 2.0 m below the ground and to carrying a load of 1000 kN/m, the shear parameters c = 50 kN/m² and angle of internal friction is 22° while the density of soil is 20 kN/m³. The factor of safety to be used is 2.5."
    },
    {
        "q_no": "Q.5 (a)", "unit": 5, "marks": 3, "type": "Theory",
        "question": "Discuss different types of soil samples. How will you obtain undisturbed samples?"
    },
    {
        "q_no": "Q.5 (b)", "unit": 5, "marks": 4, "type": "Theory",
        "question": "What do you understand by geotechnical exploration? What are the different methods of subsoil explorations?"
    },
    {
        "q_no": "Q.5 (c)", "unit": 5, "marks": 7, "type": "Theory / Numerical",
        "question": "Discuss Rock Mass Rating. How is it useful in finding the bearing capacity of rocks? The drilling carried out in a borehole from 6.00 m to 7.50 m below the ground level shows the 10 rock pieces of size 6, 8, 9, 10, 15, 18, 22 and 32 (all in centimeters). Determine the rock core recovery and rock quality designation. Comment on the quality of rock."
    },
    {
        "q_no": "Q.5 (c) OR", "unit": 5, "marks": 7, "type": "Theory / Numerical",
        "question": "Explain the Standard Penetration Test. What are the different corrections to be applied to observed SPT value?\nFollowing the observations of Standard Penetration Tests conducted at a site on sandy soil. Find the corrected N values: 1.50m (N=12, γ=15.5), 3.00m (N=18, γ=17.2), 4.50m (N=26, γ=19.0), 6.00m (N=32, γ=20.5)"
    }
]

print(f"Total 2025 questions: {len(q2025)}")

# Cross match each with compile_data
for item in q2025:
    matches = []
    for q in compile_data.questions:
        if q['unit'] == item['unit']:
            # simple keyword overlap
            words_a = set(re.findall(r'\w{4,}', item['question'].lower()))
            words_b = set(re.findall(r'\w{4,}', q['question'].lower()))
            overlap = words_a.intersection(words_b)
            if len(overlap) >= 3 or (len(words_a) <= 5 and len(overlap) >= 2):
                matches.append((q['id'], q['year'], q['q_no'], q['topic'], len(overlap)))
    matches.sort(key=lambda x: x[4], reverse=True)
    top_m = matches[:3]
    print(f"\n2025 {item['q_no']} ({item['marks']}M, Unit {item['unit']}): {item['question'][:70]}...")
    if top_m:
        for m in top_m:
            print(f"   -> Match: {m[0]} ({m[1]} {m[2]}) Topic: {m[3]} (overlap {m[4]})")
    else:
        print("   -> NO MATCH FOUND (NEW TOPIC)")
