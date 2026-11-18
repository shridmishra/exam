import re
import json
import sys
from pathlib import Path

# Add root and tools to sys.path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(root_dir / "tools"))

import generate_diagrams

d_caisson = generate_diagrams.get_diagram_open_caisson()
d_rebhann = generate_diagrams.get_diagram_rebhann()
d_shear_curves = generate_diagrams.get_diagram_shear_curves()
d_shear_modes = generate_diagrams.get_diagram_shear_modes_3panels()
d_strap = generate_diagrams.get_diagram_strap_footing()
d_spt = generate_diagrams.get_diagram_spt()
d_borelog = generate_diagrams.get_diagram_borelog()

def replace_in_text(text):
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Cross-Section of Open Caisson.*?</svg>\s*</div>',
        d_caisson,
        text,
        flags=re.DOTALL
    )
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Rebhann\'s Graphical Construction.*?</svg>\s*</div>',
        d_rebhann,
        text,
        flags=re.DOTALL
    )
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Load-Settlement \(q vs s\) Curves.*?</svg>\s*</div>',
        d_shear_curves,
        text,
        flags=re.DOTALL
    )
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Modes of Shear Failure &amp; Rupture Surfaces.*?</svg>\s*</div>',
        d_shear_modes,
        text,
        flags=re.DOTALL
    )
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Elevation &amp; Structural Action of Strap.*?</svg>\s*</div>',
        d_strap,
        text,
        flags=re.DOTALL
    )
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Standard Penetration Test \(SPT\) Setup.*?</svg>\s*</div>',
        d_spt,
        text,
        flags=re.DOTALL
    )
    text = re.sub(
        r'<div class="sol-diagram-box">\s*<div class="sol-diagram-title">Figure: Typical Soil Investigation Borelog Layout.*?</svg>\s*</div>',
        d_borelog,
        text,
        flags=re.DOTALL
    )
    return text

if __name__ == '__main__':
    for path in ['canonical_data.json', 'subjects/geotech-2/canonical_data.json']:
        file_path = root_dir / path
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = 0
        for c in data:
            orig = c.get('master_solution', '')
            if '<svg' in orig:
                new_sol = replace_in_text(orig)
                if new_sol != orig:
                    c['master_solution'] = new_sol
                    updated += 1
                    print(f'[{path}] Updated {c["id"]}')
                else:
                    print(f'[{path}] FAILED {c["id"]}')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f'Saved {path}: {updated} topics updated.\n')

    compile_py = root_dir / 'subjects/geotech-2/compile_data.py'
    with open(compile_py, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = replace_in_text(content)
    if new_content != content:
        with open(compile_py, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Saved {compile_py} with updated diagram SVGs!')
    else:
        print(f'WARNING: No replacements made in {compile_py}')
