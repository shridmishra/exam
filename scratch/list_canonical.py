import json

with open("canonical_data.json", "r", encoding="utf-8") as f:
    canonical = json.load(f)

print(f"Total canonical topics: {len(canonical)}")
for idx, c in enumerate(canonical):
    years = c.get('years', [])
    q_ids = [q['id'] if isinstance(q, dict) else q for q in c.get('questions', [])]
    print(f"[{idx+1}] {c['id']} (Unit {c['unit']}): {c['title']} | Years: {years} | Qs: {len(q_ids)} | Rep: {c.get('rep_frequency', '')}")
