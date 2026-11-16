# scratch/apply_compile_data_update.py
import sys
sys.path.insert(0, '.')
sys.path.append('scratch')
import generate_all_theory_solutions
import compile_data

sols = generate_all_theory_solutions.SOLUTIONS
qs = compile_data.questions

updated = 0
for q in qs:
    if q['id'] in sols:
        q['solution'] = sols[q['id']]
        updated += 1

print(f"Updated in-memory questions: {updated} / {len(sols)}")

# Generate the python file content cleanly
lines = [
    'import json',
    'import os',
    '',
    '# Complete question dataset for Geotechnical Engineering - II (CE 41007 / CE 4107 / CE 4151)',
    '# Derived from 3 examination papers: Nov-Dec 2024, Nov-Dec 2023, Dec 2022',
    '',
    'questions = ['
]

for idx, q in enumerate(qs):
    lines.append('    {')
    keys = ['id', 'year', 'unit', 'unit_name', 'q_no', 'marks', 'type', 'co', 'bl', 'pi', 'topic', 'repeated', 'rep_frequency', 'question', 'solution']
    for k in keys:
        if k not in q:
            continue
        v = q[k]
        if k in ['solution', 'question'] and '\n' in str(v):
            lines.append(f'        "{k}": r"""{v}""",')
        elif k in ['solution', 'question']:
            lines.append(f'        "{k}": r"""{v}""",')
        elif isinstance(v, str):
            lines.append(f'        "{k}": {repr(v)},')
        elif isinstance(v, bool):
            lines.append(f'        "{k}": {v},')
        elif isinstance(v, (int, float)):
            lines.append(f'        "{k}": {v},')
        else:
            lines.append(f'        "{k}": {repr(v)},')
    lines[-1] = lines[-1].rstrip(',')
    if idx < len(qs) - 1:
        lines.append('    },')
    else:
        lines.append('    }')

lines.append(']')
lines.append('')
lines.append('print(f"Loaded {len(questions)} verified questions.")')
lines.append('')

output_content = '\n'.join(lines)

with open('compile_data.py', 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"Successfully wrote {len(qs)} questions to compile_data.py")
