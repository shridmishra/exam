"""
Subject Loader & Registry Engine.
Orchestrates multi-subject discovery, loading, and creation.
"""

import os
import sys
import json
import shutil
import importlib.util
from pathlib import Path
from typing import Dict, Any, List, Optional

def get_repo_root() -> Path:
    """Returns the absolute path to the repository root."""
    return Path(__file__).resolve().parent.parent

def get_registry_path() -> Path:
    """Returns path to subjects/registry.json."""
    return get_repo_root() / "subjects" / "registry.json"

def get_registry() -> Dict[str, Any]:
    """Loads subjects/registry.json."""
    path = get_registry_path()
    if not path.exists():
        return {"active_subject": "geotech-2", "subjects": []}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_registry(registry: Dict[str, Any]) -> None:
    """Saves updated registry."""
    path = get_registry_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def list_subjects() -> List[Dict[str, Any]]:
    """Returns list of registered subjects."""
    return get_registry().get("subjects", [])

def get_active_subject_id() -> str:
    """Returns ID of active subject, default 'geotech-2'."""
    return get_registry().get("active_subject", "geotech-2")

def load_module_from_path(module_name: str, file_path: Path):
    """Dynamically loads a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module {module_name} from {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

class SubjectContext:
    """Encapsulates all data and modules for an individual subject."""
    def __init__(self, subject_id: str, subject_dir: Path, meta: Dict[str, Any]):
        self.id = subject_id
        self.dir = subject_dir
        self.meta = meta
        self.name = meta.get("name", subject_id)
        self.short_name = meta.get("short_name", subject_id)
        self.code = meta.get("code", "")
        self.alt_codes = meta.get("alt_codes", [])
        self.storage_prefix = meta.get("storage_prefix", subject_id.replace("-", "_"))
        self.output_filename = meta.get("output_filename", f"{subject_id}_pyq_analysis.html")
        self.unit_titles = {int(k): v for k, v in meta.get("unit_titles", {}).items()}
        self.exam_years = meta.get("exam_years", [2025, 2024, 2023, 2022])
        self.hide_year_toggle = meta.get("hide_year_toggle", 2023)
        
        # Data containers
        self.canonical_topics = []
        self.raw_questions = []
        self.master_formulas = []
        self.formula_module = None

    def __repr__(self):
        return f"<SubjectContext id='{self.id}' name='{self.name}' questions={len(self.raw_questions)}>"

def load_subject(subject_id: Optional[str] = None) -> SubjectContext:
    """
    Loads all data files, questions, and formula helpers for a subject.
    If subject_id is None, loads active subject.
    """
    repo_root = get_repo_root()
    if not subject_id:
        subject_id = get_active_subject_id()
        
    subject_dir = repo_root / "subjects" / subject_id
    if not subject_dir.exists():
        # Fallback check for root geotech files
        if subject_id == "geotech-2" and (repo_root / "canonical_data.json").exists():
            subject_dir = repo_root
        else:
            raise FileNotFoundError(f"Subject directory not found: {subject_dir}")

    meta_file = subject_dir / "subject.json"
    if meta_file.exists():
        with open(meta_file, "r", encoding="utf-8") as f:
            meta = json.load(f)
    else:
        meta = {
            "id": subject_id,
            "name": "Geotechnical Engineering - II",
            "short_name": "Geo-2",
            "code": "CE 41007",
            "storage_prefix": "geotech",
            "output_filename": "geotech_pyq_analysis.html",
            "unit_titles": {
                1: "Lateral Earth Pressure",
                2: "Shear Strength & Slope Stability",
                3: "Shallow Foundations",
                4: "Deep Foundations (Piles)",
                5: "Soil Exploration & Testing"
            }
        }

    ctx = SubjectContext(subject_id, subject_dir, meta)

    # 1. Load canonical topics
    canonical_file = subject_dir / "canonical_data.json"
    if not canonical_file.exists():
        canonical_file = repo_root / "canonical_data.json"
    if canonical_file.exists():
        with open(canonical_file, "r", encoding="utf-8") as f:
            ctx.canonical_topics = json.load(f)

    # 2. Load compiled questions
    compile_file = subject_dir / "compile_data.py"
    if not compile_file.exists():
        compile_file = repo_root / "compile_data.py"
    if compile_file.exists():
        compile_mod = load_module_from_path(f"subject_{subject_id}_compile_data", compile_file)
        ctx.raw_questions = getattr(compile_mod, "questions", [])

    # 3. Load formulas JSON
    formulas_file = subject_dir / "master_formulas.json"
    if not formulas_file.exists():
        formulas_file = repo_root / "master_formulas.json"
    if formulas_file.exists():
        with open(formulas_file, "r", encoding="utf-8") as f:
            ctx.master_formulas = json.load(f)

    # 4. Load formula showcase module
    formula_mod_file = subject_dir / "formula_showcase.py"
    if not formula_mod_file.exists():
        formula_mod_file = repo_root / "formula_showcase.py"
    if formula_mod_file.exists():
        ctx.formula_module = load_module_from_path(f"subject_{subject_id}_formula_showcase", formula_mod_file)

    return ctx

def scaffold_new_subject(subject_id: str, name: str, code: str, short_name: Optional[str] = None) -> Path:
    """
    Creates a new subject scaffold from template and registers it in registry.json.
    """
    repo_root = get_repo_root()
    template_dir = repo_root / "subjects" / "_template"
    target_dir = repo_root / "subjects" / subject_id
    
    if target_dir.exists():
        raise FileExistsError(f"Subject '{subject_id}' already exists at {target_dir}")
        
    shutil.copytree(template_dir, target_dir)
    (target_dir / "papers").mkdir(exist_ok=True)
    
    # Update subject.json
    subject_json_path = target_dir / "subject.json"
    with open(subject_json_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
        
    meta["id"] = subject_id
    meta["name"] = name
    meta["code"] = code
    meta["short_name"] = short_name or subject_id.upper()
    meta["storage_prefix"] = subject_id.replace("-", "_")
    meta["output_filename"] = f"{subject_id}_pyq_analysis.html"
    
    with open(subject_json_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
        
    # Register in registry.json
    reg = get_registry()
    existing_ids = [s["id"] for s in reg.get("subjects", [])]
    if subject_id not in existing_ids:
        reg["subjects"].append({
            "id": subject_id,
            "path": f"subjects/{subject_id}",
            "name": name,
            "short_name": meta["short_name"],
            "code": code,
            "status": "in-progress",
            "output_filename": meta["output_filename"]
        })
        save_registry(reg)
        
    return target_dir
