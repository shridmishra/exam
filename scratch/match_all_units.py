import json
import re
import compile_data

with open("canonical_data.json", "r", encoding="utf-8") as f:
    canonical = json.load(f)

from scratch.match_2025 import q2025

print(f"Total 2025 questions: {len(q2025)}")

for item in q2025:
    matches = []
    words_a = set(re.findall(r'\w{4,}', item['question'].lower()))
    for q in compile_data.questions:
        words_b = set(re.findall(r'\w{4,}', q['question'].lower()))
        overlap = words_a.intersection(words_b)
        if len(overlap) >= 3 or (len(words_a) <= 5 and len(overlap) >= 2):
            matches.append((q['id'], q['year'], q['q_no'], q['unit'], q['topic'], len(overlap)))
    matches.sort(key=lambda x: x[5], reverse=True)
    top_m = matches[:3]
    print(f"\n2025 {item['q_no']} ({item['marks']}M, Unit {item['unit']}): {item['question'][:70]}...")
    if top_m:
        for m in top_m:
            print(f"   -> Match: {m[0]} ({m[1]} {m[2]}, Unit {m[3]}) Topic: {m[4]} (overlap {m[5]})")
    else:
        print("   -> NO MATCH FOUND (NEW TOPIC)")
