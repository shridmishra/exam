import compile_data
from scratch.match_2025 import q2025

q2023 = [q for q in compile_data.questions if q['year'] == '2023']

print(f"2023 count: {len(q2023)}, 2025 count: {len(q2025)}")

for q25 in q2025:
    qno = q25['q_no']
    # find corresponding 2023 question
    match_23 = None
    for q23 in q2023:
        if q23['q_no'].replace(' ', '') == qno.replace(' ', ''):
            match_23 = q23
            break
    if match_23:
        exact = q25['question'].strip() == match_23['question'].strip()
        print(f"\n[{qno}] EXACT MATCH: {exact}")
        if not exact:
            print("  2025:", q25['question'])
            print("  2023:", match_23['question'])
    else:
        print(f"\n[{qno}] NO 2023 MATCH FOUND: {q25['question'][:60]}")
