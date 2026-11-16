"""
User Progress Persistence Engine.
Manages disk-based persistence of completed questions and study progress to user_progress.json.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, List

def get_progress_file() -> Path:
    return Path(__file__).resolve().parent.parent / "user_progress.json"

def load_all_progress() -> Dict[str, Any]:
    file_path = get_progress_file()
    if not file_path.exists():
        return {
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "subjects": {}
        }
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Warning: could not read progress file: {e}")
        return {"last_updated": datetime.now(timezone.utc).isoformat(), "subjects": {}}

def get_subject_progress(subject_id: str) -> Dict[str, Any]:
    data = load_all_progress()
    subjects = data.get("subjects", {})
    return subjects.get(subject_id, {
        "completed_questions": [],
        "filters": {},
        "active_view": "questions",
        "hide_2023": False
    })

def save_subject_progress(subject_id: str, completed_questions: List[str] = None, filters: Dict[str, Any] = None, active_view: str = None, hide_2023: bool = None, hide_2022: bool = None) -> Dict[str, Any]:
    data = load_all_progress()
    if "subjects" not in data:
        data["subjects"] = {}
        
    sub_data = data["subjects"].get(subject_id, {})
    
    if completed_questions is not None:
        # Preserve order, deduplicate
        sub_data["completed_questions"] = list(dict.fromkeys(completed_questions))
    if filters is not None:
        sub_data["filters"] = filters
    if active_view is not None:
        sub_data["active_view"] = active_view
    if hide_2023 is not None:
        sub_data["hide_2023"] = hide_2023
    elif hide_2022 is not None:
        sub_data["hide_2023"] = hide_2022

    sub_data["last_saved"] = datetime.now(timezone.utc).isoformat()
    data["subjects"][subject_id] = sub_data
    data["last_updated"] = datetime.now(timezone.utc).isoformat()
    data["active_subject"] = subject_id

    file_path = get_progress_file()
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    return sub_data
