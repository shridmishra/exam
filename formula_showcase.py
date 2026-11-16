"""
Root compatibility proxy for Geotechnical Engineering - II formula showcase.
The canonical module is modularly maintained at subjects/geotech-2/formula_showcase.py
"""
import sys
from pathlib import Path

# Ensure root is in sys.path
root_dir = Path(__file__).resolve().parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from core.subjects import load_subject

_ctx = load_subject("geotech-2")
_mod = _ctx.formula_module

master_formulas = getattr(_mod, "master_formulas", [])
enhance_solution_math = getattr(_mod, "enhance_solution_math", lambda h: h)
enhance_html = getattr(_mod, "enhance_html", lambda h: h)

__all__ = ["master_formulas", "enhance_solution_math", "enhance_html"]
