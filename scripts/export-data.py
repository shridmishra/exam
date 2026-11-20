#!/usr/bin/env python3
"""
Data Exporter: Exports Python questions, canonical clusters, formulas,
and timetable schedules into clean, strongly-typed JSON for the Next.js app.
"""

import sys
import json
from pathlib import Path

# Add repo root to sys.path
repo_root = Path(__file__).resolve().parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from core.subjects import load_subject, list_subjects
from core.formatter import format_solution

# Ensure output directory exists
out_dir = repo_root / "src" / "data"
out_dir.mkdir(parents=True, exist_ok=True)

DEFAULT_SCHEDULE = [
    {
        "id": 1,
        "date": "18 Nov 2026",
        "isoDate": "2026-11-18",
        "day": "Wednesday",
        "order": 18,
        "code": "CE 41007",
        "subject": "Geotechnical Engineering - II (Geo - 2)",
        "shortTag": "Geo-2",
        "tag": "Regular",
        "isOld": False,
        "gap": "First Exam",
        "completed": False
    },
    {
        "id": 5,
        "date": "09 Dec 2026",
        "isoDate": "2026-12-09",
        "day": "Wednesday",
        "order": 39,
        "code": "CE 41001",
        "subject": "Design of Reinforced Concrete Structures (RCC)",
        "shortTag": "RCC",
        "tag": "Regular",
        "isOld": False,
        "gap": "4 Days Gap",
        "completed": False
    },
    {
        "id": 7,
        "date": "12 Dec 2026",
        "isoDate": "2026-12-12",
        "day": "Saturday",
        "order": 42,
        "code": "CE 41006",
        "subject": "Design of Hydraulic Structures (DHS)",
        "shortTag": "DHS",
        "tag": "Regular",
        "isOld": False,
        "gap": "1 Day Gap",
        "completed": False
    }
]

FULL_BACKLOG_SCHEDULE = [
    {
        "id": 1,
        "date": "18 Nov 2026",
        "isoDate": "2026-11-18",
        "day": "Wednesday",
        "order": 18,
        "code": "CE 41007",
        "subject": "Geotechnical Engineering - II (Geo - 2)",
        "shortTag": "Geo-2",
        "tag": "Regular",
        "isOld": False,
        "gap": "First Exam",
        "completed": False
    },
    {
        "id": 2,
        "date": "26 Nov 2026",
        "isoDate": "2026-11-26",
        "day": "Thursday",
        "order": 26,
        "code": "CE 31505",
        "subject": "Structural Analysis - II (SA-2)",
        "shortTag": "SA-2",
        "tag": "Old Syllabus",
        "isOld": True,
        "gap": "8 Days Gap",
        "completed": False
    },
    {
        "id": 3,
        "date": "30 Nov 2026",
        "isoDate": "2026-11-30",
        "day": "Monday",
        "order": 30,
        "code": "CE 31007",
        "subject": "Structural Analysis - I (SA-I)",
        "shortTag": "SA-I",
        "tag": "Old Syllabus",
        "isOld": True,
        "gap": "4 Days Gap",
        "completed": False
    },
    {
        "id": 4,
        "date": "05 Dec 2026",
        "isoDate": "2026-12-05",
        "day": "Saturday",
        "order": 35,
        "code": "CE 31517",
        "subject": "Geotechnical Engineering - I (Geo I)",
        "shortTag": "Geo I",
        "tag": "Old Syllabus",
        "isOld": True,
        "gap": "5 Days Gap",
        "completed": False
    },
    {
        "id": 5,
        "date": "09 Dec 2026",
        "isoDate": "2026-12-09",
        "day": "Wednesday",
        "order": 39,
        "code": "CE 41001",
        "subject": "Design of Reinforced Concrete Structures (RCC)",
        "shortTag": "RCC",
        "tag": "Regular",
        "isOld": False,
        "gap": "4 Days Gap",
        "completed": False
    },
    {
        "id": 6,
        "date": "11 Dec 2026",
        "isoDate": "2026-12-11",
        "day": "Friday",
        "order": 41,
        "code": "CE 31713",
        "subject": "Water Resources Engineering (Water)",
        "shortTag": "Water",
        "tag": "Old Syllabus",
        "isOld": True,
        "gap": "2 Days Gap",
        "completed": False
    },
    {
        "id": 7,
        "date": "12 Dec 2026",
        "isoDate": "2026-12-12",
        "day": "Saturday",
        "order": 42,
        "code": "CE 41006",
        "subject": "Design of Hydraulic Structures (DHS)",
        "shortTag": "DHS",
        "tag": "Regular",
        "isOld": False,
        "gap": "1 Day Gap",
        "completed": False
    }
]

def export_geotech():
    ctx = load_subject("geotech-2")
    raw_qs = ctx.raw_questions
    
    # Calculate repeat multiplier
    canon_clusters = ctx.canonical_topics
    q_map = {q['id']: q for q in raw_qs}
    cluster_year_map = {}
    for c in canon_clusters:
        q_ids = [q['id'] if isinstance(q, dict) else q for q in c.get("questions", [])]
        years = c.get("years") or sorted(list(set(str(q_map[qid]['year']) for qid in q_ids if qid in q_map)), reverse=True)
        for qid in q_ids:
            cluster_year_map[qid] = (c.get("id"), len(years), f"{len(years)}x")

    math_enhancer = (
        getattr(ctx.formula_module, 'enhance_solution_math', None)
        if hasattr(ctx, 'formula_module') and ctx.formula_module
        else None
    )

    exported_qs = []
    for q in raw_qs:
        cid, y_count, rep_str = cluster_year_map.get(q.get("id"), (None, 1, "1x"))
        formatted_html = format_solution(q.get("solution", ""), math_enhancer=math_enhancer)
        exported_qs.append({
            "id": q.get("id"),
            "year": str(q.get("year")),
            "unit": q.get("unit"),
            "unit_name": q.get("unit_name", ""),
            "q_no": q.get("q_no"),
            "marks": q.get("marks"),
            "type": q.get("type"),
            "co": q.get("co"),
            "bl": q.get("bl"),
            "pi": q.get("pi"),
            "topic": q.get("topic"),
            "repeated": bool(q.get("repeated", False)),
            "rep_frequency": q.get("rep_frequency", ""),
            "repeat_multiplier": rep_str if y_count > 1 else "1x",
            "cluster_id": cid,
            "question": q.get("question"),
            "solution": q.get("solution"),
            "formatted_solution": formatted_html
        })

    # 1. Questions JSON
    with open(out_dir / "questions.json", "w", encoding="utf-8") as f:
        json.dump(exported_qs, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(exported_qs)} questions to src/data/questions.json")

    # 2. Canonical clusters JSON
    with open(out_dir / "canonical.json", "w", encoding="utf-8") as f:
        json.dump(canon_clusters, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(canon_clusters)} clusters to src/data/canonical.json")

    # 3. Master formulas JSON
    formulas = ctx.master_formulas
    with open(out_dir / "formulas.json", "w", encoding="utf-8") as f:
        json.dump(formulas, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(formulas)} formulas to src/data/formulas.json")

    # 4. Subject metadata JSON
    with open(out_dir / "subject.json", "w", encoding="utf-8") as f:
        json.dump(ctx.meta, f, indent=2, ensure_ascii=False)
    print("✓ Exported subject metadata to src/data/subject.json")

    # 5. Subjects registry (ready only)
    all_subjects = [s for s in list_subjects() if s.get("status") == "ready"]
    with open(out_dir / "subjects.json", "w", encoding="utf-8") as f:
        json.dump(all_subjects, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(all_subjects)} registered subjects to src/data/subjects.json")

    # 6. Timetable presets JSON
    timetable_data = {
        "default": DEFAULT_SCHEDULE,
        "backlog": FULL_BACKLOG_SCHEDULE
    }
    with open(out_dir / "timetable.json", "w", encoding="utf-8") as f:
        json.dump(timetable_data, f, indent=2, ensure_ascii=False)
    print("✓ Exported timetable presets to src/data/timetable.json")

def export_dhs():
    ctx = load_subject("dhs")
    raw_qs = ctx.raw_questions
    
    canon_clusters = ctx.canonical_topics
    q_map = {q['id']: q for q in raw_qs}
    cluster_year_map = {}
    for c in canon_clusters:
        q_ids = [q['id'] if isinstance(q, dict) else q for q in c.get("questions", [])]
        years = c.get("years") or sorted(list(set(str(q_map[qid]['year']) for qid in q_ids if qid in q_map)), reverse=True)
        for qid in q_ids:
            cluster_year_map[qid] = (c.get("id"), len(years), f"{len(years)}x")

    exported_qs = []
    for q in raw_qs:
        cid, y_count, rep_str = cluster_year_map.get(q.get("id"), (None, 1, "1x"))
        formatted_html = q.get("formatted_solution") or format_solution(q.get("solution", ""))
        exported_qs.append({
            "id": q.get("id"),
            "year": str(q.get("year")),
            "unit": q.get("unit"),
            "unit_name": q.get("unit_name", ""),
            "q_no": q.get("q_no"),
            "marks": q.get("marks"),
            "type": q.get("type"),
            "co": q.get("co", "CO1"),
            "bl": q.get("bl", "BL2"),
            "pi": q.get("pi", ""),
            "topic": q.get("topic"),
            "repeated": bool(q.get("repeated", False)),
            "rep_frequency": q.get("rep_frequency", ""),
            "repeat_multiplier": rep_str if y_count > 1 else "1x",
            "cluster_id": cid,
            "question": q.get("question"),
            "solution": q.get("solution"),
            "formatted_solution": formatted_html
        })

    # 1. Questions JSON
    with open(out_dir / "dhs_questions.json", "w", encoding="utf-8") as f:
        json.dump(exported_qs, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(exported_qs)} questions to src/data/dhs_questions.json")

    # 2. Canonical clusters JSON
    with open(out_dir / "dhs_canonical.json", "w", encoding="utf-8") as f:
        json.dump(canon_clusters, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(canon_clusters)} clusters to src/data/dhs_canonical.json")

    # 3. Master formulas JSON
    formulas = ctx.master_formulas
    with open(out_dir / "dhs_formulas.json", "w", encoding="utf-8") as f:
        json.dump(formulas, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(formulas)} formulas to src/data/dhs_formulas.json")

    # 4. Subject metadata JSON
    with open(out_dir / "dhs_subject.json", "w", encoding="utf-8") as f:
        json.dump(ctx.meta, f, indent=2, ensure_ascii=False)
    print("✓ Exported subject metadata to src/data/dhs_subject.json")

def export_rcc():
    ctx = load_subject("rcc")
    raw_qs = ctx.raw_questions
    
    canon_clusters = ctx.canonical_topics
    q_map = {q['id']: q for q in raw_qs}
    cluster_year_map = {}
    for c in canon_clusters:
        q_ids = [q['id'] if isinstance(q, dict) else q for q in c.get("questions", [])]
        years = c.get("years") or sorted(list(set(str(q_map[qid]['year']) for qid in q_ids if qid in q_map)), reverse=True)
        for qid in q_ids:
            cluster_year_map[qid] = (c.get("id"), len(years), f"{len(years)}x")

    math_enhancer = (
        getattr(ctx.formula_module, 'enhance_solution_math', None)
        if hasattr(ctx, 'formula_module') and ctx.formula_module
        else None
    )

    exported_qs = []
    for q in raw_qs:
        cid, y_count, rep_str = cluster_year_map.get(q.get("id"), (q.get("topic_id"), 1, q.get("rep_count", "1x")))
        formatted_html = q.get("formatted_solution") or format_solution(q.get("solution", ""), math_enhancer=math_enhancer)
        exported_qs.append({
            "id": q.get("id"),
            "year": str(q.get("year")),
            "unit": q.get("unit"),
            "unit_name": q.get("unit_name", ""),
            "q_no": q.get("q_no"),
            "marks": q.get("marks"),
            "type": q.get("type"),
            "co": q.get("co", "CO1"),
            "bl": q.get("bl", "BL2"),
            "pi": q.get("pi", "1.1.1"),
            "topic": q.get("topic"),
            "repeated": bool(q.get("repeated", False)),
            "rep_frequency": q.get("rep_frequency", "1 of 5 Papers"),
            "repeat_multiplier": q.get("rep_count") or (rep_str if y_count > 1 else "1x"),
            "cluster_id": cid,
            "question": q.get("question"),
            "solution": q.get("solution"),
            "formatted_solution": formatted_html
        })

    # 1. Questions JSON
    with open(out_dir / "rcc_questions.json", "w", encoding="utf-8") as f:
        json.dump(exported_qs, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(exported_qs)} questions to src/data/rcc_questions.json")

    # 2. Canonical clusters JSON
    with open(out_dir / "rcc_canonical.json", "w", encoding="utf-8") as f:
        json.dump(canon_clusters, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(canon_clusters)} clusters to src/data/rcc_canonical.json")

    # 3. Master formulas JSON
    formulas = ctx.master_formulas
    with open(out_dir / "rcc_formulas.json", "w", encoding="utf-8") as f:
        json.dump(formulas, f, indent=2, ensure_ascii=False)
    print(f"✓ Exported {len(formulas)} formulas to src/data/rcc_formulas.json")

    # 4. Subject metadata JSON
    with open(out_dir / "rcc_subject.json", "w", encoding="utf-8") as f:
        json.dump(ctx.meta, f, indent=2, ensure_ascii=False)
    print("✓ Exported subject metadata to src/data/rcc_subject.json")

if __name__ == "__main__":
    export_geotech()
    export_dhs()
    export_rcc()
