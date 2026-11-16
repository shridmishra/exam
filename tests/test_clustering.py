import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import compile_data
questions = compile_data.questions

# Let's inspect each question's topic and see how we can group them
from collections import defaultdict
groups = defaultdict(list)

for q in questions:
    topic_clean = q['topic']
    # Normalize topics
    if "Earth Pressure" in topic_clean and ("Types" in topic_clean or "Theories" in topic_clean or "Rankine's Theory Assumptions" in topic_clean):
        key = ("Unit 1", "Earth Pressure Types & Rankine Assumptions")
    elif "Coulomb" in topic_clean and ("Assumptions" in topic_clean or "Maximum Thrust" in topic_clean or "Sliding Wedge" in topic_clean):
        key = ("Unit 1", "Coulomb Wedge Theory & Sliding Wedge Maximum Thrust Derivation")
    elif "Rebhann" in topic_clean:
        key = ("Unit 1", "Rebhann's Graphical Construction Method & Proof")
    elif "Gravity Retaining Wall Coulomb" in topic_clean:
        key = ("Unit 1", "Gravity Retaining Wall Coulomb Active & Passive Thrust Numerical (12m / 15m)")
    elif "Tension Crack" in topic_clean:
        key = ("Unit 1", "Tension Crack Depth & Active Pressure in Cohesive Soil")
    elif "Battered Retaining Wall" in topic_clean or "Rankine Surcharged Backfill" in topic_clean or "Increase in Earth Pressure" in topic_clean:
        key = ("Unit 1", "Retaining Wall with Surcharge & Sloping/Battered Backfill")
    elif "At-Rest Earth Pressure" in topic_clean:
        key = ("Unit 1", "At-Rest Earth Pressure Derivation (Elastic Theory)")
    elif "Coulomb Passive Earth Pressure with Wall Friction" in topic_clean:
        key = ("Unit 1", "Coulomb Passive Earth Pressure with Wall Friction (delta > 0)")
    elif "Modes of Shear Failure" in topic_clean:
        key = ("Unit 2", "Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves")
    elif "Triaxial Test Drainage" in topic_clean or "UU Test vs CD Test" in topic_clean or "Triaxial Tests & Best Test" in topic_clean:
        key = ("Unit 2", "Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection")
    elif "Mohr-Coulomb Principal Stress" in topic_clean or "Coulomb's Law of Shear" in topic_clean:
        key = ("Unit 2", "Mohr-Coulomb Failure Criterion & Principal Stress Relationship Derivation")
    elif "Direct Box Shear Test" in topic_clean:
        key = ("Unit 2", "Direct Shear Box Test vs Triaxial Shear Test Comparison")
    elif "Vane Shear Test" in topic_clean:
        key = ("Unit 2", "Vane Shear Test Formula & Shear Strength in Soft Clay")
    elif "Infinite Slope Stability" in topic_clean:
        key = ("Unit 2", "Infinite Slope Stability Analysis (Clay vs Granular Soil with Seepage)")
    elif "Methods of Slope Stabilization" in topic_clean:
        key = ("Unit 2", "Methods of Slope Stabilization & Remedial Measures")
    elif "Triaxial Test Strain & Mohr-Coulomb Parameters" in topic_clean or "Triaxial Test Corrected Area" in topic_clean or "CU Triaxial Test" in topic_clean or "CD Triaxial Test" in topic_clean or "Failure Plane Stresses" in topic_clean:
        key = ("Unit 2", "Triaxial Test Data Analysis: Area Correction & Shear Parameters (c, phi)")
    elif "Effect of Water Table on Bearing Capacity" in topic_clean or "Water Table Effect on Safe Bearing Capacity" in topic_clean:
        key = ("Unit 3", "Water Table Effect on Ultimate & Safe Bearing Capacity (Theory)")
    elif "Strip Footing Bearing Capacity with Water Table" in topic_clean or "Square Footing Bearing Capacity with Water Table" in topic_clean or "Square Footing Safe Bearing Capacity & Water Table Reduction" in topic_clean:
        key = ("Unit 3", "Terzaghi Bearing Capacity Numerical with Water Table (Square/Strip)")
    elif "Terzaghi's Bearing Capacity Assumptions" in topic_clean or "Factors Affecting Bearing Capacity" in topic_clean:
        key = ("Unit 3", "Terzaghi Bearing Capacity Theory: Assumptions & Limitations")
    elif "Foundation Design Criteria" in topic_clean or "Requirements of Satisfactory Foundations" in topic_clean or "Types of Shallow Foundations" in topic_clean or "Site-Specific Foundation Selection" in topic_clean:
        key = ("Unit 3", "Foundation Design Criteria, Selection Principles & Types of Shallow Foundations")
    elif "Settlement of Foundations" in topic_clean or "Immediate Elastic Settlement" in topic_clean or "Failures in Shallow Foundations" in topic_clean:
        key = ("Unit 3", "Foundation Settlement (Elastic, Consolidation) & Modes of Failure")
    elif "Plate Load Test" in topic_clean:
        key = ("Unit 3", "Plate Load Test Procedure & Housel's Two-Plate Method (Q = Am + Pn)")
    elif "Design of Strip Footing (Width Determination)" in topic_clean or "Square Footing in Purely Cohesive Soil" in topic_clean:
        key = ("Unit 3", "Design of Strip / Square Footing for Column Load in Pure Clay")
    elif "Circular Footing Diameter on Saturated Clay" in topic_clean or "Eccentrically Loaded Rectangular Footing" in topic_clean:
        key = ("Unit 3", "Circular Footing Diameter Determination & Eccentric Loading")
    elif "9-Pile Group Capacity in Clay" in topic_clean or "Design of Square Pile Group in Clay" in topic_clean:
        key = ("Unit 4", "9-Pile Group Safe Load Capacity in Soft Clay Numerical (VERBATIM REPEAT)")
    elif "Group Action of Piles" in topic_clean or "Functions of Pile Foundations" in topic_clean or "Bearing Capacity: Shallow vs Deep" in topic_clean:
        key = ("Unit 4", "Group Action of Piles: Block Failure vs Individual Pile Failure & Efficiency")
    elif "Optimum Spacing of 16-Pile Group" in topic_clean:
        key = ("Unit 4", "Optimum Spacing Derivation for Square Pile Group in Clay (s = d + 2d/pi alpha)")
    elif "Under-Reamed Pile Foundation" in topic_clean:
        key = ("Unit 4", "Under-Reamed Pile Foundations for Expansive Soils (Black Cotton Soils)")
    elif "Open Caisson (Well Foundation) Components" in topic_clean:
        key = ("Unit 4", "Open Caisson (Well Foundation) Components, Forces, & Cutting Edge Sketches")
    elif "Single Pile Frictional Resistance in Clay" in topic_clean or "Single Pile Load Capacity in Sand" in topic_clean:
        key = ("Unit 4", "Single Pile Static Load Capacity in Sand and Clay (Skin Friction + End Bearing)")
    elif "Standard Penetration Test" in topic_clean or "SPT Corrections Numerical" in topic_clean:
        key = ("Unit 5", "Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections (100% Guaranteed)")
    elif "Sampler Design Parameters" in topic_clean or "Area Ratio Calculation" in topic_clean:
        key = ("Unit 5", "Soil Sampler Criteria: Area Ratio (Ar), Inside/Outside Clearance (Ci, Co) & Recovery Ratio")
    elif "Objectives of Soil Exploration" in topic_clean or "Methods of Subsoil Exploration" in topic_clean or "Purpose of Soil Investigation" in topic_clean or "Classification of Soil Exploration Methods" in topic_clean or "Laboratory & Field Tests" in topic_clean or "Soil Samples (Disturbed vs Undisturbed)" in topic_clean:
        key = ("Unit 5", "Soil Exploration Objectives, Planning, Disturbed vs Undisturbed Samples & Methods")
    elif "Borelog Features" in topic_clean or "Depth of Exploration Guidelines" in topic_clean:
        key = ("Unit 5", "Borelog Preparation, Soil Profile Documentation & Significant Depth of Exploration")
    elif "Rock Core Recovery (TCR) & RQD" in topic_clean:
        key = ("Unit 5", "Rock Core Drilling: Total Core Recovery (TCR) & Rock Quality Designation (RQD)")
    else:
        key = (f"Unit {q['unit']}", topic_clean)

    groups[key].append(q)

print(f"Total clustered unique topics: {len(groups)}")
total_mapped = sum(len(v) for v in groups.values())
print(f"Total questions mapped: {total_mapped} / {len(questions)}")

for (u, name), qlist in sorted(groups.items()):
    years = [f"{q['year']} {q['q_no']}" for q in qlist]
    print(f"[{u}] {name} ({len(qlist)} questions: {', '.join(years)})")
