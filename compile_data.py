"""
Root compatibility proxy for Geotechnical Engineering - II dataset.
The canonical dataset is modularly maintained at subjects/geotech-2/compile_data.py
"""
import sys
from pathlib import Path

# Ensure root is in sys.path
root_dir = Path(__file__).resolve().parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from core.subjects import load_subject

_ctx = load_subject("geotech-2")
questions = _ctx.raw_questions
verified_questions = _ctx.raw_questions

__all__ = ["questions", "verified_questions"]
