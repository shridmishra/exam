import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import compile_data
import json

questions = compile_data.questions

# Direct canonical mapping lookup for all 106 verified questions
QID_MAP = {
    # UNIT 1: Lateral Earth Pressure & Retaining Walls
    '2025-Q1a': ('u1-earth-pressure-types', 1, 'Earth Pressure Types (At-Rest, Active, Passive) & Theories', 'Theory', 'CO1'),
    '2024-Q1a': ('u1-earth-pressure-types', 1, 'Earth Pressure Types (At-Rest, Active, Passive) & Theories', 'Theory', 'CO1'),
    '2023-Q1a': ('u1-earth-pressure-types', 1, 'Earth Pressure Types (At-Rest, Active, Passive) & Theories', 'Theory', 'CO1'),

    '2024-Q1b': ('u1-theory-assumptions', 1, 'Earth Pressure Theories & Assumptions (Rankine vs Coulomb Wedge Theory)', 'Theory', 'CO1'),
    '2022-Q1c': ('u1-theory-assumptions', 1, 'Earth Pressure Theories & Assumptions (Rankine vs Coulomb Wedge Theory)', 'Theory', 'CO1'),

    '2024-Q1c': ('u1-at-rest-derivation', 1, 'At-Rest Earth Pressure Coefficient Derivation (K0 = mu / (1 - mu))', 'Derivation', 'CO1'),

    '2025-Q1c': ('u1-sliding-wedge-derivation', 1, 'Coulomb Sliding Wedge Theory: Maximum Active Earth Pressure Derivation', 'Derivation', 'CO1'),
    '2023-Q1c': ('u1-sliding-wedge-derivation', 1, 'Coulomb Sliding Wedge Theory: Maximum Active Earth Pressure Derivation', 'Derivation', 'CO1'),

    '2025-Q1c-OR': ('u1-rebhann', 1, "Rebhann's Graphical Construction for Active Earth Thrust & Proof", 'Theory / Derivation', 'CO1'),
    '2023-Q1c-OR': ('u1-rebhann', 1, "Rebhann's Graphical Construction for Active Earth Thrust & Proof", 'Theory / Derivation', 'CO1'),
    '2022-Q1e-OR': ('u1-rebhann', 1, "Rebhann's Graphical Construction for Active Earth Thrust & Proof", 'Theory / Derivation', 'CO1'),

    '2025-Q1bii': ('u1-gravity-wall', 1, 'Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)', 'Numerical', 'CO1'),
    '2024-Q1d': ('u1-gravity-wall', 1, 'Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)', 'Numerical', 'CO1'),
    '2023-Q1bii': ('u1-gravity-wall', 1, 'Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)', 'Numerical', 'CO1'),
    '2022-Q1d': ('u1-gravity-wall', 1, 'Coulomb Retaining Wall Active & Passive Earth Pressure Numericals (12m / 7.5m / 15m with Wall Friction)', 'Numerical', 'CO1'),

    '2025-Q1bi': ('u1-sloping-backfill-rankine', 1, 'Retaining Wall Supporting Inclined Non-Cohesive Backfill (Rankine Theory at 10 deg)', 'Numerical', 'CO1'),
    '2023-Q1bi': ('u1-sloping-backfill-rankine', 1, 'Retaining Wall Supporting Inclined Non-Cohesive Backfill (Rankine Theory at 10 deg)', 'Numerical', 'CO1'),

    '2024-Q1e-OR': ('u1-battered-coulomb-wall', 1, 'Battered Retaining Wall with Sloping Backfill Numerical (Coulomb Wedge Theory)', 'Numerical', 'CO1'),

    '2022-Q1b': ('u1-surcharge-retaining-wall', 1, 'Active Earth Pressure Intensity Increase Due to Uniform Surcharge (Ka * q)', 'Numerical', 'CO1'),

    '2025-Q1biii': ('u1-retaining-wall-water-table-cohesion', 1, 'Active Earth Pressure Distribution with Water Table & Submerged Cohesive Soil (4.5m Retaining Wall)', 'Numerical', 'CO1'),
    '2023-Q1biii': ('u1-retaining-wall-water-table-cohesion', 1, 'Active Earth Pressure Distribution with Water Table & Submerged Cohesive Soil (4.5m Retaining Wall)', 'Numerical', 'CO1'),

    '2022-Q1a': ('u1-tension-crack-cut', 1, 'Depth of Tension Cracks & Critical Depth of Unsupported Cut in Cohesive Soil', 'Numerical', 'CO1'),

    # UNIT 2: Shear Strength & Slope Stability
    '2025-Q2bi': ('u2-shear-failure-modes', 2, 'Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves', 'Theory', 'CO2'),
    '2024-Q2b': ('u2-shear-failure-modes', 2, 'Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves', 'Theory', 'CO2'),
    '2023-Q2bi': ('u2-shear-failure-modes', 2, 'Modes of Shear Failure (General, Local, Punching) & Load-Settlement Curves', 'Theory', 'CO2'),

    '2025-Q3biii': ('u2-triaxial-drainage', 2, 'Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria', 'Theory', 'CO2'),
    '2024-Q2c': ('u2-triaxial-drainage', 2, 'Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria', 'Theory', 'CO2'),
    '2023-Q3biii': ('u2-triaxial-drainage', 2, 'Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria', 'Theory', 'CO2'),
    '2022-Q2b': ('u2-triaxial-drainage', 2, 'Triaxial Test Drainage Conditions (UU, CU, CD) & Test Selection Criteria', 'Theory', 'CO2'),

    '2025-Q3a': ('u2-coulomb-shear-law', 2, "Coulomb's Law of Shear Strength & Failure Envelope (tau = c + sigma tan phi)", 'Theory', 'CO2'),
    '2023-Q3a': ('u2-coulomb-shear-law', 2, "Coulomb's Law of Shear Strength & Failure Envelope (tau = c + sigma tan phi)", 'Theory', 'CO2'),

    '2025-Q3c': ('u2-principal-stress-derivation', 2, 'Mohr-Coulomb Principal Stress Relationship Derivation (sigma1 vs sigma3)', 'Derivation', 'CO2'),
    '2023-Q3c': ('u2-principal-stress-derivation', 2, 'Mohr-Coulomb Principal Stress Relationship Derivation (sigma1 vs sigma3)', 'Derivation', 'CO2'),

    '2025-Q3bi': ('u2-triaxial-failure-plane-stresses', 2, 'Shear and Normal Stresses on Failure Plane Numerical (tau = 4 kPa, sigma = 10 kPa)', 'Numerical', 'CO2'),
    '2023-Q3bi': ('u2-triaxial-failure-plane-stresses', 2, 'Shear and Normal Stresses on Failure Plane Numerical (tau = 4 kPa, sigma = 10 kPa)', 'Numerical', 'CO2'),

    '2025-Q3bii': ('u2-triaxial-multistage-parameters', 2, 'Triaxial Test Specimen Shear Parameters & Deviator Stress Numerical (38mm Specimen, 100/200 kPa)', 'Numerical', 'CO2'),
    '2023-Q3bii': ('u2-triaxial-multistage-parameters', 2, 'Triaxial Test Specimen Shear Parameters & Deviator Stress Numerical (38mm Specimen, 100/200 kPa)', 'Numerical', 'CO2'),

    '2025-Q3c-OR': ('u2-triaxial-effective-cu', 2, 'CU Triaxial Test Total and Effective Shear Parameters with Pore Water Pressure (Multi-Stage Observations)', 'Numerical', 'CO2'),
    '2023-Q3c-OR': ('u2-triaxial-effective-cu', 2, 'CU Triaxial Test Total and Effective Shear Parameters with Pore Water Pressure (Multi-Stage Observations)', 'Numerical', 'CO2'),

    '2024-Q2e-OR': ('u2-triaxial-effective-strain-numerical', 2, 'Triaxial Test Axial & Volumetric Strain with Mohr-Coulomb Parameters (50mm x 100mm Specimen)', 'Numerical', 'CO2'),
    '2022-Q2d': ('u2-triaxial-cd-clay-numerical', 2, 'CD Triaxial Test on Normally Consolidated Clay (sigma3 = 250 kPa, sigmad = 275 kPa)', 'Numerical', 'CO2'),
    '2022-Q2e-OR': ('u2-infinite-slope-granular', 2, 'Infinite Slope Stability in Granular Soil with Seepage & Water Table Numerical', 'Numerical', 'CO2'),
    '2024-Q2a': ('u2-infinite-slope-clay-factors', 2, 'Factors Affecting Factor of Safety of Infinite Slope in Clay', 'Theory', 'CO2'),
    '2024-Q2d': ('u2-slope-stabilization', 2, 'Methods for Improving Stability of Slopes & Remedial Measures', 'Theory', 'CO2'),
    '2022-Q2c': ('u2-vane-shear', 2, 'Vane Shear Test Formula & Shear Strength in Soft Clay Numerical', 'Numerical', 'CO2'),
    '2022-Q2a': ('u2-direct-shear-vs-triaxial', 2, 'Direct Box Shear Test vs Triaxial Shear Test Comparison', 'Theory', 'CO2'),

    # UNIT 3: Shallow Foundations & Bearing Capacity
    '2025-Q2a': ('u3-bearing-capacity-suffixes', 3, 'Bearing Capacity Definitions & Terminology Suffixes (Gross, Net, Safe, Allowable)', 'Theory', 'CO3'),
    '2023-Q2a': ('u3-bearing-capacity-suffixes', 3, 'Bearing Capacity Definitions & Terminology Suffixes (Gross, Net, Safe, Allowable)', 'Theory', 'CO3'),

    '2025-Q2bii': ('u3-water-table-theory', 3, 'Ground Water Table Effect on Ultimate & Safe Bearing Capacity (Theory & 50% Drop)', 'Theory', 'CO3'),
    '2023-Q2bii': ('u3-water-table-theory', 3, 'Ground Water Table Effect on Ultimate & Safe Bearing Capacity (Theory & 50% Drop)', 'Theory', 'CO3'),
    '2022-Q3c': ('u3-water-table-theory', 3, 'Ground Water Table Effect on Ultimate & Safe Bearing Capacity (Theory & 50% Drop)', 'Theory', 'CO3'),

    '2025-Q2c': ('u3-terzaghi-water-table-numerical', 3, 'Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)', 'Numerical', 'CO3'),
    '2024-Q3e-OR': ('u3-terzaghi-water-table-numerical', 3, 'Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)', 'Numerical', 'CO3'),
    '2023-Q2c': ('u3-terzaghi-water-table-numerical', 3, 'Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)', 'Numerical', 'CO3'),
    '2022-Q3d': ('u3-terzaghi-water-table-numerical', 3, 'Terzaghi Bearing Capacity Numerical with Water Table (Square & Strip Footings)', 'Numerical', 'CO3'),

    '2025-Q2c-OR': ('u3-eccentric-footing-numerical', 3, 'Rectangular Footing with Biaxial Eccentricity Numerical (3m x 2m, P = 1500 kN, eL = 0.3m, eB = 0.2m)', 'Numerical', 'CO3'),
    '2023-Q2c-OR': ('u3-eccentric-footing-numerical', 3, 'Rectangular Footing with Biaxial Eccentricity Numerical (3m x 2m, P = 1500 kN, eL = 0.3m, eB = 0.2m)', 'Numerical', 'CO3'),

    '2022-Q3e-OR': ('u3-circular-footing-clay', 3, 'Circular Footing Diameter Determination on Saturated Stiff Clay (Q = 600 kN, qu = 250 kPa)', 'Numerical', 'CO3'),

    '2025-Q4a': ('u3-shallow-foundation-types', 3, 'Types of Shallow Foundations & Strap Footing Sketch', 'Theory', 'CO3'),
    '2023-Q4a': ('u3-shallow-foundation-types', 3, 'Types of Shallow Foundations & Strap Footing Sketch', 'Theory', 'CO3'),

    '2025-Q4bi': ('u3-foundation-requirements-criteria', 3, 'Requirements of Satisfactory Foundations & Design Criteria (Shear Failure & Settlement)', 'Theory', 'CO3'),
    '2024-Q3a': ('u3-foundation-requirements-criteria', 3, 'Requirements of Satisfactory Foundations & Design Criteria (Shear Failure & Settlement)', 'Theory', 'CO3'),
    '2023-Q4bi': ('u3-foundation-requirements-criteria', 3, 'Requirements of Satisfactory Foundations & Design Criteria (Shear Failure & Settlement)', 'Theory', 'CO3'),

    '2025-Q4bii': ('u3-site-foundation-selection', 3, 'Site-Specific Foundation Selection for Subsoil Profiles (Compressible Clay vs Expansive Soil)', 'Theory', 'CO3'),
    '2023-Q4bii': ('u3-site-foundation-selection', 3, 'Site-Specific Foundation Selection for Subsoil Profiles (Compressible Clay vs Expansive Soil)', 'Theory', 'CO3'),

    '2025-Q4biii': ('u3-immediate-settlement-numerical', 3, 'Immediate Elastic Settlement of Footing Numerical (Square Footing, E = 50,000 kPa, mu = 0.3)', 'Numerical', 'CO3'),
    '2023-Q4biii': ('u3-immediate-settlement-numerical', 3, 'Immediate Elastic Settlement of Footing Numerical (Square Footing, E = 50,000 kPa, mu = 0.3)', 'Numerical', 'CO3'),

    '2025-Q2biii': ('u3-square-footing-clay', 3, 'Square Footing Net Safe Bearing Capacity in Pure Cohesive Clay (qu = 150 kPa, 2.5m Footing)', 'Numerical', 'CO3'),
    '2023-Q2biii': ('u3-square-footing-clay', 3, 'Square Footing Net Safe Bearing Capacity in Pure Cohesive Clay (qu = 150 kPa, 2.5m Footing)', 'Numerical', 'CO3'),

    '2025-Q4c-OR': ('u3-strip-footing-cphi-design', 3, 'Strip Footing Width Design in c-phi Soil for 1000 kN/m Column Load', 'Numerical', 'CO3'),
    '2023-Q4c-OR': ('u3-strip-footing-cphi-design', 3, 'Strip Footing Width Design in c-phi Soil for 1000 kN/m Column Load', 'Numerical', 'CO3'),

    '2022-Q3a': ('u3-terzaghi-assumptions', 3, "Terzaghi's Bearing Capacity Theory: Assumptions & Factors Affecting Bearing Capacity", 'Theory', 'CO3'),
    '2022-Q3b': ('u3-terzaghi-assumptions', 3, "Terzaghi's Bearing Capacity Theory: Assumptions & Factors Affecting Bearing Capacity", 'Theory', 'CO3'),

    '2024-Q3b': ('u3-settlement-foundation-theory', 3, 'Settlement of Foundations (Immediate Elastic, Consolidation & Permissible Limits)', 'Theory', 'CO3'),
    '2024-Q3c': ('u3-shallow-foundation-failures', 3, 'Modes of Failure in Shallow Foundations (Bearing Capacity, Differential Settlement & Structural)', 'Theory', 'CO3'),
    '2024-Q3d': ('u3-plate-load-housel', 3, "Plate Load Test Procedure & Housel's Two-Plate Method (Q = Am + Pn)", 'Numerical', 'CO3'),

    # UNIT 4: Deep Foundations (Piles & Caissons)
    '2024-Q4d': ('u4-9pile-group-clay-numerical', 4, '9-Pile Group Safe Load Capacity in Soft Clay Numerical (30cm Dia, 9m Length, qu = 90 kPa)', 'Numerical', 'CO4'),
    '2022-Q4e-OR': ('u4-9pile-group-clay-numerical', 4, '9-Pile Group Safe Load Capacity in Soft Clay Numerical (30cm Dia, 9m Length, qu = 90 kPa)', 'Numerical', 'CO4'),

    '2025-Q4c': ('u4-pile-group-design-500kn', 4, 'Design of Square Pile Group in Soft Clay for 500 kN Column Load (qu = 50 kPa, 400mm Dia, 6m Length)', 'Numerical', 'CO4'),
    '2023-Q4c': ('u4-pile-group-design-500kn', 4, 'Design of Square Pile Group in Soft Clay for 500 kN Column Load (qu = 50 kPa, 400mm Dia, 6m Length)', 'Numerical', 'CO4'),

    '2024-Q4a': ('u4-pile-group-action', 4, 'Group Action of Piles (Block Failure vs Individual Failure & Efficiency)', 'Theory', 'CO4'),
    '2022-Q4a': ('u4-pile-functions', 4, 'Functions and Classification of Pile Foundations', 'Theory', 'CO4'),
    '2022-Q4b': ('u4-shallow-vs-deep-computation', 4, 'Bearing Capacity Computation: Shallow vs Deep Foundations (Skin Friction vs End Bearing Mechanisms)', 'Theory', 'CO4'),

    '2022-Q4c': ('u4-single-pile-clay-friction', 4, 'Single Pile Frictional Resistance in Uniform Clay Deposit Numerical (Qs = alpha * cu * As)', 'Numerical', 'CO4'),
    '2022-Q4d': ('u4-single-pile-sand-capacity', 4, 'Single Pile Static Ultimate Load Capacity in Sand Deposit (Qu = Qb + Qs, phi = 40 deg)', 'Numerical', 'CO4'),

    '2024-Q4e-OR': ('u4-optimum-spacing-derivation', 4, 'Optimum Spacing Derivation for Square Pile Group in Soft Clay (s = d + 2d / (pi * alpha))', 'Derivation', 'CO4'),
    '2024-Q4c': ('u4-open-caisson-well', 4, 'Open Caisson (Well Foundation) Components, Forces, & Cutting Edge Sketches', 'Theory', 'CO4'),
    '2024-Q4b': ('u4-under-reamed-piles', 4, 'Under-Reamed Pile Foundations for Expansive Soils (Black Cotton Soils)', 'Theory', 'CO4'),

    # UNIT 5: Soil Exploration & In-Situ Testing
    '2025-Q5c-OR': ('u5-spt-test-corrections', 5, 'Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections', 'Theory / Numerical', 'CO5'),
    '2024-Q5e-OR': ('u5-spt-test-corrections', 5, 'Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections', 'Theory / Numerical', 'CO5'),
    '2023-Q5c-OR': ('u5-spt-test-corrections', 5, 'Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections', 'Theory / Numerical', 'CO5'),
    '2022-Q5d': ('u5-spt-test-corrections', 5, 'Standard Penetration Test (SPT): Procedure, Overburden & Dilatancy Corrections', 'Theory / Numerical', 'CO5'),

    '2025-Q5c': ('u5-rock-core-rqd', 5, 'Rock Mass Rating (RMR) & Core Recovery (TCR / RQD) Numerical', 'Numerical', 'CO5'),
    '2023-Q5c': ('u5-rock-core-rqd', 5, 'Rock Mass Rating (RMR) & Core Recovery (TCR / RQD) Numerical', 'Numerical', 'CO5'),

    '2025-Q5a': ('u5-soil-samples-disturbed-undisturbed', 5, 'Soil Samples: Disturbed vs Undisturbed Samples & Methods of Sampling', 'Theory', 'CO5'),
    '2023-Q5a': ('u5-soil-samples-disturbed-undisturbed', 5, 'Soil Samples: Disturbed vs Undisturbed Samples & Methods of Sampling', 'Theory', 'CO5'),

    '2025-Q5b': ('u5-subsoil-exploration-methods', 5, 'Methods of Subsoil Exploration (Boring, Sounding, Trial Pits, Geophysical)', 'Theory', 'CO5'),
    '2023-Q5b': ('u5-subsoil-exploration-methods', 5, 'Methods of Subsoil Exploration (Boring, Sounding, Trial Pits, Geophysical)', 'Theory', 'CO5'),
    '2022-Q5e-OR': ('u5-subsoil-exploration-methods', 5, 'Methods of Subsoil Exploration (Boring, Sounding, Trial Pits, Geophysical)', 'Theory', 'CO5'),

    '2024-Q5a': ('u5-exploration-objectives-purpose', 5, 'Objectives & Purpose of Geotechnical Soil Exploration / Investigation', 'Theory', 'CO5'),
    '2022-Q5b': ('u5-exploration-objectives-purpose', 5, 'Objectives & Purpose of Geotechnical Soil Exploration / Investigation', 'Theory', 'CO5'),

    '2024-Q5c': ('u5-sampler-design-criteria', 5, 'Soil Sampler Criteria: Area Ratio (Ar), Clearance Ratios (Ci, Co) & Recovery Ratio', 'Theory / Numerical', 'CO5'),
    '2022-Q5c': ('u5-sampler-design-criteria', 5, 'Soil Sampler Criteria: Area Ratio (Ar), Clearance Ratios (Ci, Co) & Recovery Ratio', 'Theory / Numerical', 'CO5'),

    '2024-Q5b': ('u5-borelog-features', 5, 'Borelog Preparation & Subsoil Profile Documentation', 'Theory', 'CO5'),
    '2024-Q5d': ('u5-depth-of-exploration', 5, 'Significant Depth of Exploration for Foundations & Structures', 'Theory', 'CO5'),
    '2022-Q5a': ('u5-lab-field-tests-investigation', 5, 'Laboratory and Field Tests for Soil Investigation Work', 'Theory', 'CO5'),
}

unit_names = {
    1: 'Lateral Earth Pressure & Retaining Walls',
    2: 'Shear Strength & Slope Stability',
    3: 'Shallow Foundations & Bearing Capacity',
    4: 'Deep Foundations (Piles & Caissons)',
    5: 'Soil Exploration & In-Situ Testing'
}

canonical_map = {}
for q in questions:
    cid, unit, title, qtype, co = QID_MAP[q['id']]
    if cid not in canonical_map:
        canonical_map[cid] = {
            'id': cid,
            'unit': unit,
            'unit_name': unit_names[unit],
            'title': title,
            'type': qtype,
            'co': co,
            'questions': [],
            'years': set(),
            'total_marks': 0,
            'rep_frequency': '',
            'is_repeated': False,
            'master_solution': q['solution'],
            'canonical_question': q['question']
        }
    canonical_map[cid]['questions'].append({
        'id': q['id'],
        'year': str(q['year']),
        'q_no': q['q_no'],
        'marks': q['marks'],
        'type': q['type'],
        'question': q['question']
    })
    canonical_map[cid]['years'].add(str(q['year']))
    canonical_map[cid]['total_marks'] += q['marks']
    if len(q['solution']) > len(canonical_map[cid]['master_solution']):
        canonical_map[cid]['master_solution'] = q['solution']

for cid, c in canonical_map.items():
    years = sorted(list(c['years']), reverse=True)
    c['years'] = years
    if len(years) >= 4:
        c['rep_frequency'] = '4 of 4 Papers (100% Guaranteed)'
        c['is_repeated'] = True
    elif len(years) == 3:
        c['rep_frequency'] = '3 of 4 Papers (75% High Probability)'
        c['is_repeated'] = True
    elif len(years) == 2:
        c['rep_frequency'] = '2 of 4 Papers (50% Medium Probability)'
        c['is_repeated'] = True
    else:
        c['rep_frequency'] = f'1 of 4 Papers ({years[0]})'
        c['is_repeated'] = False

canonical_list = sorted(canonical_map.values(), key=lambda x: (x['unit'], not x['is_repeated'], -len(x['years']), -x['total_marks']))

print(f"Generated {len(canonical_list)} canonical topics from {len(questions)} questions.")

with open('canonical_data.json', 'w', encoding='utf-8') as f:
    json.dump(canonical_list, f, indent=2)

print("Saved canonical_data.json successfully.")
