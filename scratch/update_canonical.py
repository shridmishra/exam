import json

with open("canonical_data.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

topic_map = {t["id"]: t for t in topics}

# 2025 Questions mapping to canonical topics
mappings = [
    ("u1-earth-pressure-types", {
        "id": "2025-Q1a", "year": "2025", "q_no": "Q.1 (a)", "marks": 2, "type": "Theory",
        "question": "What are different Types of Earth Pressure and what are different theories of Earth Pressures?"
    }),
    ("u1-surcharged-battered", {
        "id": "2025-Q1bi", "year": "2025", "q_no": "Q.1 (b) i", "marks": 3, "type": "Numerical",
        "question": "A smooth vertical wall, 6 m high supports an inclined non cohesive backfill (&phi; = 32&deg;; &gamma; = 21 kN/m&sup3;) at an angle 10&deg; with horizontal. Compute the total active & passive pressure at the bottom of wall."
    }),
    ("u1-gravity-wall", {
        "id": "2025-Q1bii", "year": "2025", "q_no": "Q.1 (b) ii", "marks": 3, "type": "Numerical",
        "question": "A rough vertical wall of 7.5 m height supports a horizontal backfill. If the angle of internal friction and angle of wall friction are respectively 33&deg; and 12&deg;, compute the passive earth pressure at the bottom of wall. Assume density of 18.5 kN/m&sup3;."
    }),
    ("u1-cohesive-retaining", {
        "id": "2025-Q1biii", "year": "2025", "q_no": "Q.1 (b) iii", "marks": 3, "type": "Numerical",
        "question": "A retaining wall of 4.5 m height carries a horizontal backfill with c = 35 kN/m&sup2;, &phi; = 10&deg;; &gamma; = 17.2 kN/m&sup3;. The water table is located at 1.50 m below the ground. Sketch the distribution of active earth pressure. Assume the value of angle of internal friction is 14&deg;; and cohesion c = 50 kN/m&sup2; in the submerged condition."
    }),
    ("u1-coulomb-wedge", {
        "id": "2025-Q1c", "year": "2025", "q_no": "Q.1 (c)", "marks": 6, "type": "Derivation",
        "question": "Derive the condition of maximum active earth pressure from sliding wedge."
    }),
    ("u1-rebhann", {
        "id": "2025-Q1c-OR", "year": "2025", "q_no": "Q.1 (c) OR", "marks": 6, "type": "Theory / Derivation",
        "question": "Explain the Rebhann's graphical construction for active earth pressure and prove that it satisfy the condition of maximum earth pressure"
    }),
    ("u2-shear-failure-modes", {
        "id": "2025-Q2bi", "year": "2025", "q_no": "Q.2 (b) i", "marks": 3, "type": "Theory",
        "question": "Describe the three modes of shear failure in soil. Draw load-settlement curves for each mode and explain which type of soil exhibits each failure pattern."
    }),
    ("u3-water-table-theory", {
        "id": "2025-Q2bii", "year": "2025", "q_no": "Q.2 (b) ii", "marks": 3, "type": "Theory",
        "question": "Explain the effect of water table on bearing capacity of soils."
    }),
    ("u3-footing-design-cohesive", {
        "id": "2025-Q2biii", "year": "2025", "q_no": "Q.2 (b) iii", "marks": 3, "type": "Numerical",
        "question": "Compute the net safe bearing capacity of a square footing of size 2.5 m, provided at 2.0 m depth in a purely cohesive soil with Unconfined Shear Strength of 150 kN/m&sup2; and density being 18 kN/m&sup3;. Use factor of safety as 2.5."
    }),
    ("u3-terzaghi-water-table-numerical", {
        "id": "2025-Q2c", "year": "2025", "q_no": "Q.2 (c)", "marks": 6, "type": "Numerical",
        "question": "A square footing of 3.5 m is resting at 3 m below the ground level. The shear parameters of soil are respectively 40 kN/m&sup2; and 12&deg;. The density of soil is 20 kN/m&sup3;. The water table lies at 2 m below the base of footing. Calculate the net safe bearing capacity. Assume factor of safety of 3.0."
    }),
    ("u3-circular-eccentric-footing", {
        "id": "2025-Q2c-OR", "year": "2025", "q_no": "Q.2 (c) OR", "marks": 6, "type": "Numerical",
        "question": "A rectangular footing 3 m x 2 m carries a load of 1500 kN with eccentricity of 0.3 m along the length and 0.2 m along the width. The footing is located at 1.5 m depth in soil with c = 20 kN/m&sup2;, &phi; = 25&deg;, &gamma; = 19 kN/m&sup3;. Calculate the maximum pressure at the base and check for safety."
    }),
    ("u2-mohr-coulomb-derivation", {
        "id": "2025-Q3a", "year": "2025", "q_no": "Q.3 (a)", "marks": 2, "type": "Theory",
        "question": "Discuss Coulomb's law of shear strength of soil"
    }),
    ("u2-triaxial-numericals", {
        "id": "2025-Q3bi", "year": "2025", "q_no": "Q.3 (b) i", "marks": 3, "type": "Numerical",
        "question": "The shear stress and normal stress at a failure plane in a cohesionless soil mass were found to be 4 kPa and 10 kPa respectively. Determine the resultant stress on failure plane and inclination of failure plane. Also compute the shear parameters."
    }),
    ("u2-triaxial-numericals", {
        "id": "2025-Q3bii", "year": "2025", "q_no": "Q.3 (b) ii", "marks": 3, "type": "Numerical",
        "question": "The deviator force to shear the soil specimen of 38 mm diameter and 76 mm height under a confining pressure of 100 kN/m&sup2; is 251 N while it shears under a deviator force of 327 N at a confining pressure of 200 kN/m&sup2;. The deformation at the time of failure is respectively 2.0 mm and 5.2 mm. Determine the shear parameters. Determine the deviator stress under confining pressure of 250 kPa."
    }),
    ("u2-triaxial-drainage", {
        "id": "2025-Q3biii", "year": "2025", "q_no": "Q.3 (b) iii", "marks": 3, "type": "Theory",
        "question": "Explain various kinds of triaxial tests. Which test is best suited for the cohesive soil deposit having a permeable layer immediately below the foundation level?"
    }),
    ("u2-mohr-coulomb-derivation", {
        "id": "2025-Q3c", "year": "2025", "q_no": "Q.3 (c)", "marks": 6, "type": "Derivation",
        "question": "Derive a relationship between effective shear parameters and principal stresses."
    }),
    ("u2-triaxial-numericals", {
        "id": "2025-Q3c-OR", "year": "2025", "q_no": "Q.3 (c) OR", "marks": 6, "type": "Numerical",
        "question": "The following data refers to a triaxial compression tests performed on a soil sample. Determine the total and effective shear parameters of soil.<br>Observation 1: &sigma;<sub>3</sub> = 80 kPa, &sigma;<sub>d</sub> = 175 kPa, u = 45 kPa<br>Observation 2: &sigma;<sub>3</sub> = 150 kPa, &sigma;<sub>d</sub> = 240 kPa, u = 50 kPa<br>Observation 3: &sigma;<sub>3</sub> = 210 kPa, &sigma;<sub>d</sub> = 300 kPa, u = 60 kPa"
    }),
    ("u3-foundation-criteria-types", {
        "id": "2025-Q4a", "year": "2025", "q_no": "Q.4 (a)", "marks": 2, "type": "Theory",
        "question": "What are different types of shallow foundations? Draw neat sketch of strap footing."
    }),
    ("u3-foundation-criteria-types", {
        "id": "2025-Q4bi", "year": "2025", "q_no": "Q.4 (b) i", "marks": 3, "type": "Theory",
        "question": "Enumerate the requirements of satisfactory foundations."
    }),
    ("u3-foundation-criteria-types", {
        "id": "2025-Q4bii", "year": "2025", "q_no": "Q.4 (b) ii", "marks": 3, "type": "Theory",
        "question": "Two buildings are to be constructed at two different sites. First site shows the low compressive cohesive soil profile up to 10 m depth followed by good quality rock up to 15 m depth below the ground while the second site is having expansive soil up to 5 m depth followed by good rock up to 10 m below the ground. G+4 story building is to be constructed at the first site while at the second site G+15 story building is to be constructed. Suggest the type of foundation at two different sites for the structures to be constructed."
    }),
    ("u3-foundation-settlement", {
        "id": "2025-Q4biii", "year": "2025", "q_no": "Q.4 (b) iii", "marks": 3, "type": "Numerical",
        "question": "Using the soil properties (&gamma; = 17.5 kN/m&sup3;, c = 20 kN/m&sup2;, &phi; = 20&deg;), and assuming the square footing (3.415 m x 3.415 m) located at a depth of 1.5 m carries a total load of 2000 kN. Calculate the immediate settlement of the footing using the elastic theory. Assume the soil is homogeneous and isotropic with a Poisson's ratio of 0.3 and Young's modulus of 50,000 kN/m&sup2;. (assume influence factor 0.88 for square footing)"
    }),
    ("u4-pile-group-clay-numerical", {
        "id": "2025-Q4c", "year": "2025", "q_no": "Q.4 (c)", "marks": 6, "type": "Numerical",
        "question": "Design a square pile group to carry 500 kN load in clay with an unconfined compressive strength of 50 kN/m&sup2;. Assume pile diameter of 400 mm and 6.0 m length. Adhesion factor may be taken as 0.6."
    }),
    ("u3-footing-design-cohesive", {
        "id": "2025-Q4c-OR", "year": "2025", "q_no": "Q.4 (c) OR", "marks": 6, "type": "Numerical",
        "question": "Design a strip footing resting at 2.0 m below the ground and to carrying a load of 1000 kN/m, the shear parameters c = 50 kN/m&sup2; and angle of internal friction is 22&deg; while the density of soil is 20 kN/m&sup3;. The factor of safety to be used is 2.5."
    }),
    ("u5-exploration-methods-samples", {
        "id": "2025-Q5a", "year": "2025", "q_no": "Q.5 (a)", "marks": 3, "type": "Theory",
        "question": "Discuss different types of soil samples. How will you obtain undisturbed samples?"
    }),
    ("u5-exploration-methods-samples", {
        "id": "2025-Q5b", "year": "2025", "q_no": "Q.5 (b)", "marks": 4, "type": "Theory",
        "question": "What do you understand by geotechnical exploration? What are the different methods of subsoil explorations?"
    }),
    ("u5-rock-core-rqd", {
        "id": "2025-Q5c", "year": "2025", "q_no": "Q.5 (c)", "marks": 7, "type": "Theory / Numerical",
        "question": "Discuss Rock Mass Rating. How is it useful in finding the bearing capacity of rocks? The drilling carried out in a borehole from 6.00 m to 7.50 m below the ground level shows the 10 rock pieces of size 6, 8, 9, 10, 15, 18, 22 and 32 (all in centimeters). Determine the rock core recovery and rock quality designation. Comment on the quality of rock."
    }),
    ("u5-spt-test-corrections", {
        "id": "2025-Q5c-OR", "year": "2025", "q_no": "Q.5 (c) OR", "marks": 7, "type": "Theory / Numerical",
        "question": "Explain the Standard Penetration Test. What are the different corrections to be applied to observed SPT value?<br>Following the observations of Standard Penetration Tests conducted at a site on sandy soil. Find the corrected N values.<br>Depth: 1.50 m, Observed SPT: 12, Density: 15.5 kN/m&sup3;<br>Depth: 3.00 m, Observed SPT: 18, Density: 17.2 kN/m&sup3;<br>Depth: 4.50 m, Observed SPT: 26, Density: 19.0 kN/m&sup3;<br>Depth: 6.00 m, Observed SPT: 32, Density: 20.5 kN/m&sup3;"
    })
]

# Add new topic for Q2a: Bearing Capacity Definitions & Suffixes
if "u2-bearing-capacity-suffixes" not in topic_map:
    new_t = {
        "id": "u2-bearing-capacity-suffixes",
        "unit": 2,
        "unit_name": "Bearing Capacity of Shallow Foundations",
        "title": "Bearing Capacity Definitions & Terminology Suffixes (Gross/Net Ultimate, Safe & Allowable)",
        "type": "Theory",
        "co": "CO2",
        "questions": [
            {
                "id": "2025-Q2a",
                "year": "2025",
                "q_no": "Q.2 (a)",
                "marks": 2,
                "type": "Theory",
                "question": "What do you mean by bearing capacity? What are the different suffixes to be used before bearing capacity?"
            }
        ],
        "years": ["2025"],
        "total_marks": 2,
        "rep_frequency": "1 of 4 Papers",
        "is_repeated": False,
        "master_solution": """<strong>1. Bearing Capacity of Soil:</strong><br>
The maximum load-carrying resistance per unit area that the underlying soil or rock mass can support without undergoing shear failure or excessive foundation settlement.<br>
<strong>2. Suffixes Used Before Bearing Capacity:</strong><br>
1. <strong>Gross Ultimate (q<sub>u</sub>):</strong> Total intensity of loading at base of foundation at which soil fails in shear.<br>
2. <strong>Net Ultimate (q<sub>nu</sub>):</strong> Ultimate intensity above initial effective surcharge: q<sub>nu</sub> = q<sub>u</sub> - &gamma; D<sub>f</sub>.<br>
3. <strong>Net Safe (q<sub>ns</sub>):</strong> Net ultimate capacity divided by factor of safety: q<sub>ns</sub> = q<sub>nu</sub> / FOS.<br>
4. <strong>Gross Safe (q<sub>s</sub>):</strong> Maximum gross intensity safe against shear: q<sub>s</sub> = q<sub>ns</sub> + &gamma; D<sub>f</sub>.<br>
5. <strong>Safe Bearing Pressure (q<sub>ps</sub>):</strong> Maximum net intensity that limits settlement to tolerable values (&le; 25 mm).<br>
6. <strong>Allowable Bearing Capacity (q<sub>a</sub>):</strong> Smaller of gross safe (q<sub>s</sub>) and safe bearing pressure (q<sub>ps</sub>).""",
        "canonical_question": "What do you mean by bearing capacity? What are the different suffixes to be used before bearing capacity?"
    }
    topics.append(new_t)
    topic_map["u2-bearing-capacity-suffixes"] = new_t

# Add questions to topics
for tid, q_obj in mappings:
    t = topic_map.get(tid)
    if not t:
        print(f"Warning: Topic {tid} not found!")
        continue
    # check if already added
    existing_ids = [q["id"] if isinstance(q, dict) else q for q in t["questions"]]
    if q_obj["id"] not in existing_ids:
        t["questions"].append(q_obj)
    if "2025" not in t["years"]:
        t["years"].append("2025")
        t["years"].sort(reverse=True)

# Update rep_frequency and is_repeated for all topics across 4 papers
for t in topics:
    num_years = len(set(t.get("years", [])))
    num_qs = len(t.get("questions", []))
    total_m = sum(q.get("marks", 0) if isinstance(q, dict) else 0 for q in t.get("questions", []))
    t["total_marks"] = total_m
    if num_years >= 4:
        t["is_repeated"] = True
        t["rep_frequency"] = "4 of 4 Papers (100% Guaranteed)"
    elif num_years == 3:
        t["is_repeated"] = True
        t["rep_frequency"] = "3 of 4 Papers (75% High Probability)"
    elif num_years == 2:
        t["is_repeated"] = True
        t["rep_frequency"] = "2 of 4 Papers (50% Medium Probability)"
    elif num_qs >= 2:
        t["is_repeated"] = True
        t["rep_frequency"] = f"{num_qs} Questions across {num_years} Paper{'s' if num_years > 1 else ''}"
    else:
        t["is_repeated"] = False
        t["rep_frequency"] = "1 of 4 Papers"

with open("canonical_data.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, indent=2, ensure_ascii=False)

print(f"Updated canonical_data.json: {len(topics)} topics successfully processed.")
