import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import compile_data
import re

def format_solution(html):
    # Remove excess breaks
    html = html.replace("<br>\n<br>", "<br>").replace("<br><br>", "<br>")
    
    # Split by <br> followed by <strong>
    parts = re.split(r'<br>\s*(?=<strong>)', html)
    if len(parts) > 1:
        formatted = []
        for p in parts:
            p = p.strip()
            if not p:
                continue
            p = re.sub(r'<em>Example:?</em>', '<span class="example-tag">Eg</span>', p)
            formatted.append(f'<div class="sol-step">{p}</div>')
        return "".join(formatted)
    else:
        html = re.sub(r'<em>Example:?</em>', '<span class="example-tag">Eg</span>', html)
        return f'<div class="sol-step">{html}</div>'

for q in compile_data.questions[:5]:
    formatted = format_solution(q['solution'])
    print(f"[{q['id']}] Formatted length: {len(formatted)} | Steps: {formatted.count('class=\"sol-step\"')}")
