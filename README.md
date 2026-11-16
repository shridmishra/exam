# Exam Intelligence & PYQ Analysis Platform (`exam`)

A high-performance, offline-capable examination intelligence, Previous Year Question (PYQ) analysis, and formula mastery platform built with modular multi-subject scalability, KaTeX mathematical typesetting, and an un-cardified editorial design system.

---

## 1. Architecture Overview

The platform is designed with a **modular multi-subject architecture** (`subjects/`), decoupling subject data and formulas from the core analytical and rendering engine (`core/`).

```
exam/
├── .gitignore                          # Ignores local timetable, caches, scratch, and OS files
├── README.md                           # Platform engineering & architectural guide
├── AGENTS.md                           # Autonomous agent operating directives
├── RULES.md                            # Design tokens, typography & formatting rules
│
├── core/                               # Reusable core analytical engine (subject-agnostic)
│   ├── __init__.py                     # Core package exports
│   ├── subjects.py                     # Subject loader, registry manager, & scaffolding
│   └── formatter.py                    # Solution formatting engine (Zero Wall-of-Text)
│
├── subjects/                           # Central repository of all academic subjects
│   ├── registry.json                   # Subject catalog, metadata & active default pointer
│   ├── _template/                      # Rapid onboarding scaffold for any new subject
│   │   ├── subject.json                # Metadata (name, code, units, storage keys)
│   │   ├── canonical_data.json         # Deduplicated topic clusters & frequency ranks
│   │   ├── compile_data.py             # Verified raw question bank dataset
│   │   ├── master_formulas.json        # Governing formulas, LaTeX parameters & notes
│   │   └── formula_showcase.py         # LaTeX mathematical enhancements & post-processing
│   └── geotech-2/                      # Geotechnical Engineering - II (CE 41007)
│       ├── subject.json                # Metadata & syllabus configuration
│       ├── canonical_data.json         # 59 deduplicated core topic clusters
│       ├── compile_data.py             # 106 verified questions (2025, 2024, 2023, 2022)
│       ├── master_formulas.json        # 21 master formulas & governing equations
│       ├── formula_showcase.py         # KaTeX typography rules & interactive showcase
│       └── papers/                     # Verified examination paper source scans
│
├── vendor/                             # Shared offline vendor libraries
│   └── katex/                          # KaTeX 0.16.11 (CSS, JS, and WOFF2 fonts)
│
├── tests/                              # Automated validation & test suites
│   ├── test_clustering.py              # Canonical clustering verification
│   ├── test_dedup_gen.py               # Question-to-cluster mapping checks
│   ├── test_solution_formatter.py      # Solution formatting & example tag tests
│   └── test_solution_transformation.py # Editorial row transformation verification
│
├── tools/                              # Tooling & local utilities
│   ├── timetable/                      # (Local Only) Timetable generation engine & OCR tools
│   │   ├── build_timetable.py          # Standalone timetable generator
│   │   ├── Civil_Final_Year_*.pdf      # Timetable source documents
│   │   ├── Revised Exam Timetable*.pdf # Revised date schedules
│   │   └── ocr_*.txt                   # OCR extractions & layout logs
│   └── archive/                        # Archived legacy exploratory scripts
│
├── generate_dashboard.py               # Master CLI generator: python3 generate_dashboard.py [subject]
├── index.html                          # Primary production dashboard (active default subject)
├── geotech_pyq_analysis.html           # Canonical standalone Geotech-2 production build
├── timetable.html                      # (Local Only, Gitignored) Civil examination timetable
├── compile_data.py                     # Root compatibility proxy -> subjects/geotech-2
└── formula_showcase.py                 # Root compatibility proxy -> subjects/geotech-2
```

---

## 2. Quickstart: Run the App Fully

To run the application with a single terminal command:

```bash
./run
```

This single command automatically:
1. Re-compiles and validates the active subject dashboard (`generate_dashboard.py`).
2. Starts a local HTTP server on port `3000` (or the next available port).
3. Automatically launches the full application in your default browser.
4. Provides live links to the Question Bank, PYQ Checklist, Formula Hub, and local Timetable.

#### Optional Run Flags:
- Custom port: `./run 8080`
- Headless (no auto browser launch): `./run --no-open`
- Skip re-compilation: `./run --no-build`

---

## 3. Multi-Subject System

Each academic subject is fully self-contained inside `subjects/<subject_id>/`.

### Registered Subjects
| Subject ID | Course Code | Name | Status |
| :--- | :--- | :--- | :--- |
| `geotech-2` | CE 41007 | Geotechnical Engineering - II | **Ready (106 Qs)** |
| `rcc` | CE 41001 | Design of Reinforced Concrete Structures | Planned |
| `dhs` | CE 41006 | Design of Hydraulic Structures | Planned |
| `water` | CE 31713 | Water Resources Engineering | Planned |
| `sa-2` | CE 31505 | Structural Analysis - II | Planned |
| `sa-1` | CE 31007 | Structural Analysis - I | Planned |
| `geotech-1` | CE 31517 | Geotechnical Engineering - I | Planned |

### Subject Directory Anatomy
Each subject directory contains:
1. `subject.json`: Course code, full name, short name, storage prefix, and unit definitions.
2. `canonical_data.json`: Deduplicated topic clusters across examination sessions.
3. `compile_data.py`: Verified questions array containing verbatim paper questions, marks, type, blooms levels, and solutions.
4. `master_formulas.json`: Governing equations, LaTeX strings, variable definitions, and engineering notes.
5. `formula_showcase.py`: Subject-specific LaTeX parsing and formula display enhancements.
6. `papers/`: High-resolution question paper scans and raw sources.

### State Isolation
Each subject uses an isolated `storage_prefix` defined in `subject.json` (e.g. `geotech`, `rcc`). This guarantees that student study progress (`*_completed_questions`) and filter selections (`*_filters`) never collide across different subjects, while sharing the global theme (`geotech_theme`).

---

## 3. CLI & Build Pipeline

The master dashboard generator is invoked via `generate_dashboard.py`:

```bash
# 1. Build active default subject (geotech-2 -> index.html & geotech_pyq_analysis.html)
python3 generate_dashboard.py

# 2. Build a specific subject
python3 generate_dashboard.py geotech-2
python3 generate_dashboard.py rcc

# 3. List all registered subjects and their build status
python3 generate_dashboard.py --list

# 4. Build all ready subjects in batch
python3 generate_dashboard.py --all

# 5. Scaffold a brand-new subject instantly from template
python3 generate_dashboard.py --new rcc "Design of Reinforced Concrete Structures" "CE 41001"
```

---

## 4. Local Timetable System (Gitignored)

Per project policy:
- The exam timetable is **strictly for local use** and is excluded from git tracking (`.gitignore`).
- `timetable.html` lives at the workspace root so links from `index.html` resolve seamlessly in local browsers.
- Timetable source scripts and PDFs reside in `tools/timetable/`.
- To regenerate the timetable locally:
  ```bash
  python3 build_timetable.py
  ```

---

## 5. Editorial Standards & Directives

All questions and solutions generated by the platform strictly adhere to:
1. **Zero Wall-of-Text Policy**:
   - Solutions format as clean, un-cardified typographic rows (`.sol-item-row`).
   - Every example is moved to its own dedicated line with a micro-badge (`<span class="example-label">Example:</span>`).
   - Multi-point criteria, assumptions, and steps format into numbered lists (`1.`, `2.`, `3.`) with zero inline continuation.
2. **Typography System**:
   - Refined type scale constrained to 65–80 characters measure for comfortable reading.
   - Design tokens referenced via CSS variables (`var(--background)`, `var(--foreground)`, `var(--card)`).
   - Unified canvas palette shared across Dark Mode (`#09090b`) and Light Mode (`#fbfaf8`).
3. **No Generative AI Sparkle Icons**: Sparkle or star glyphs are strictly forbidden across all views.
