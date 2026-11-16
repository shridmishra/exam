"""
Exam Intelligence & PYQ Analysis Platform Core Engine.
Provides modular multi-subject loading, formatting, and dashboard generation.
"""

from .subjects import load_subject, list_subjects, get_active_subject_id, scaffold_new_subject
from .formatter import format_solution
from .progress import get_subject_progress, save_subject_progress, load_all_progress

__all__ = [
    "load_subject",
    "list_subjects",
    "get_active_subject_id",
    "scaffold_new_subject",
    "format_solution",
    "get_subject_progress",
    "save_subject_progress",
    "load_all_progress",
]
