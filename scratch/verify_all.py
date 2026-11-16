import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("HTML length:", len(html))

# 1. Check all 106 IDs
import compile_data
qs = compile_data.questions
print(f"Total questions in compile_data: {len(qs)}")
assert len(qs) == 106, f"Expected 106 questions, got {len(qs)}"

missing_ids = []
for q in qs:
    if f'id="{q["id"]}"' not in html and f'id="chk-card-{q["id"]}"' not in html:
        missing_ids.append(q["id"])

print(f"Missing IDs in HTML: {len(missing_ids)}")
assert len(missing_ids) == 0, f"Missing IDs: {missing_ids}"

# 2. Check 2025 questions
q2025 = [q for q in qs if q["year"] == "2025"]
print(f"2025 questions count: {len(q2025)}")
assert len(q2025) == 28, f"Expected 28 2025 questions, got {len(q2025)}"

# 3. Check CSS badge-year-2025
assert ".badge-year-2025" in html, "Missing .badge-year-2025 in CSS"
assert "var(--pastel-sage-bg)" in html, "Missing --pastel-sage-bg in CSS"

# 4. Check year filter pill
assert 'data-year="2025">2025</button>' in html, "Missing 2025 year filter pill"

# 5. Check checklist 2025 section
assert 'id="year-section-2025"' in html, "Missing year-section-2025 in checklist"

# 6. Check repeat badges
assert '>4x<' in html, "Missing 4x badge"
assert '>3x<' in html, "Missing 3x badge"
assert '>2x<' in html, "Missing 2x badge"

# 7. Check sparkle icons
sparkle_terms = ["sparkle", "stars", "wand", "autoawesome"]
for term in sparkle_terms:
    matches = re.findall(rf'\b{term}\b', html, re.IGNORECASE)
    assert len(matches) == 0, f"Found forbidden sparkle term '{term}' in HTML!"

# 8. Check dynamic counter 106
assert "106 PYQs" in html, "Missing '106 PYQs' in nav badge"
assert "106 of 106 matched" in html, "Missing '106 of 106 matched' in match counter"
assert "0 / 106 Completed" in html, "Missing '0 / 106 Completed' in checklist total"

print("\nALL VERIFICATION CHECKS PASSED PERFECTLY!")
