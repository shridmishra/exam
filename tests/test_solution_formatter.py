import re

def format_solution_html(html):
    html = html.replace("<br>\n<br>", "<br>").replace("<br><br>", "<br>")
    
    html = re.sub(
        r'\s*(?:<br>\s*)?(?:<em>\s*Example:?\s*</em>|\bExample:)\s*(.*?)(?=(?:<br>|\Z))',
        r'<div class="sol-example"><span class="example-tag">Eg</span> <span class="sol-example-text">\1</span></div>',
        html,
        flags=re.IGNORECASE
    )
    
    parts = re.split(r'<br>\s*(?=(?:<strong>|[0-9]+\.\s+|[A-Z]\.\s+|[a-z]\)\s+|&bull;\s+))', html)
    formatted = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        p = re.sub(r'^(\d+\.|[a-z]\)|[A-Z]\.|&bull;)\s*', r'<span class="sol-item-num">\1</span> ', p)
        formatted.append(f'<div class="sol-step">{p}</div>')
    return "".join(formatted)

sample = """<strong>1. Earth Pressure at Rest (P<sub>0</sub>):</strong> Occurs when the retaining structure undergoes zero lateral yield or movement (&Delta;x = 0). <em>Example:</em> Basement walls anchored to rigid bedrock, or bridge abutments supported on unyielding pile foundations.<br>
<strong>2. Active Earth Pressure (P<sub>a</sub>):</strong> Occurs when the wall moves slightly away from the retained backfill, allowing the soil to expand laterally and mobilize internal shear resistance, reducing lateral stress to a minimum value. <em>Example:</em> Cantilever gravity retaining walls yielding outward at the top.<br>
<strong>3. Passive Earth Pressure (P<sub>p</sub>):</strong> Occurs when the wall is pushed forcibly into the soil mass, compressing it horizontally until full shear resistance is mobilized to maximum lateral resistance. <em>Example:</em> Anchor deadmen slabs pulled into soil, or the passive toe resisting sliding in a sheet pile wall."""

print(format_solution_html(sample))
