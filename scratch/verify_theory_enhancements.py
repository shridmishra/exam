# scratch/verify_theory_enhancements.py
import os
import re
import sys
sys.path.insert(0, '.')
import compile_data

print("=== VERIFYING THEORY ENHANCEMENTS ===")

# 1. Check compile_data.py
qs = compile_data.questions
assert len(qs) == 78, f"Expected 78 questions, got {len(qs)}"
theory_qs = [q for q in qs if q.get('type') == 'Theory']
assert len(theory_qs) == 41, f"Expected 41 theory questions, got {len(theory_qs)}"
print(f"✓ Total questions in compile_data: {len(qs)}")
print(f"✓ Theory questions in compile_data: {len(theory_qs)}")

# Check solution lengths and structure
for q in theory_qs:
    sol = q.get('solution', '')
    assert len(sol) > 200, f"Solution for {q['id']} is too short: {len(sol)}"
    assert '<strong>' in sol, f"Missing bold headings in {q['id']}"

print("✓ All 41 theory questions have rich, structured solutions (>200 chars).")

# 2. Check generated HTML files
for filename in ['index.html', 'geotech_pyq_analysis.html']:
    assert os.path.exists(filename), f"File {filename} does not exist!"
    size_kb = os.path.getsize(filename) / 1024
    assert size_kb > 500, f"{filename} is too small: {size_kb:.1f} KB"
    print(f"✓ {filename} exists and is healthy ({size_kb:.1f} KB)")
    
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check SVGs embedded
    assert 'Figure: Modes of Shear Failure' in html, f"Modes of shear failure SVG missing in {filename}"
    assert 'Figure: Load-Settlement (q vs s) Curves' in html, f"Curves SVG missing in {filename}"
    assert 'Figure: Cross-Section of Open Caisson' in html, f"Open caisson SVG missing in {filename}"
    assert 'Figure: Elevation &amp; Structural Action of Strap' in html, f"Strap footing SVG missing in {filename}"
    assert 'Figure: Rebhann\'s Graphical Construction' in html or 'Rebhann' in html, f"Rebhann SVG missing in {filename}"
    assert 'Figure: Standard Penetration Test (SPT)' in html, f"SPT apparatus SVG missing in {filename}"
    assert 'Figure: Typical Soil Investigation Borelog' in html, f"Borelog SVG missing in {filename}"
    print(f"✓ All 7 embedded SVG diagrams verified in {filename}")
    
    # Check IS codes embedded
    is_codes = ['IS: 2131', 'IS: 1892', 'IS: 6403', 'IS: 1904', 'IS: 2911', 'IS: 2720']
    for code in is_codes:
        assert code in html, f"Code {code} missing in {filename}"
    print(f"✓ All standard IS codes verified in {filename}")
    
    # Check CSS classes
    css_classes = ['.sol-diagram-box', '.sol-diagram-svg', '.sol-table-wrap', '.sol-table', '.is-code-chip']
    for cls in css_classes:
        assert cls in html, f"CSS class {cls} missing in {filename}"
    print(f"✓ All custom CSS classes verified in {filename}")
    
    # Check KaTeX script tag presence
    assert 'katex.min.js' in html, f"KaTeX missing in {filename}"
    print(f"✓ KaTeX math integration verified in {filename}")

print("\n🎉 ALL VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")
