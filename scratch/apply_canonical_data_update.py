# scratch/apply_canonical_data_update.py
import json
import sys
sys.path.insert(0, '.')
sys.path.append('scratch')
import generate_all_theory_solutions

sols = generate_all_theory_solutions.SOLUTIONS

with open('canonical_data.json', 'r', encoding='utf-8') as f:
    cdata = json.load(f)

updated_topics = 0
for t in cdata:
    qids = [q['id'] if isinstance(q, dict) else q for q in t.get('questions', [])]
    matching = [sols[qid] for qid in qids if qid in sols]
    if matching:
        best_sol = max(matching, key=len)
        t['master_solution'] = best_sol
        updated_topics += 1
        print(f"Updated canonical topic [{t['id']}]: {t['title']} ({len(best_sol)} chars)")

with open('canonical_data.json', 'w', encoding='utf-8') as f:
    json.dump(cdata, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully updated {updated_topics} canonical topics in canonical_data.json!")
