"""
Exam Intelligence & PYQ Analysis Platform Core Engine.
Provides modular multi-subject loading, formatting, and dashboard generation.
"""

from .subjects import load_subject, list_subjects, get_active_subject_id, scaffold_new_subject
from .formatter import format_solution

__all__ = [
    "load_subject",
    "list_subjects",
    "get_active_subject_id",
    "scaffold_new_subject",
    "format_solution",
]
