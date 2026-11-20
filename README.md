# Exam Intelligence & PYQ Analysis Platform (`exam`)

A modern, high-performance examination intelligence, Previous Year Question (PYQ) analysis, and formula mastery platform built with Next.js 15 (App Router), React 19, TypeScript, Tailwind CSS, KaTeX mathematical typesetting, and an un-cardified editorial design system.

---

## 1. Architecture Overview

The platform uses a Next.js App Router frontend powered by modular subject datasets (`subjects/`) and strong JSON typing (`src/data/`).

```
exam/
├── .gitignore                          # Ignores caches, scratch, and OS files
├── README.md                           # Platform engineering & architectural guide
├── AGENTS.md                           # Autonomous agent operating directives
├── RULES.md                            # Design tokens, typography & formatting rules
├── package.json                        # Next.js, React, Tailwind, and Radix dependencies
├── tsconfig.json                       # TypeScript configuration
├── tailwind.config.ts                  # Tailwind theme and custom typography tokens
│
├── src/                                # Next.js App Router frontend
│   ├── app/                            # Route layout and main application page
│   │   ├── layout.tsx                  # Root layout (Theme provider, font definitions)
│   │   ├── page.tsx                    # Multi-subject dashboard hub
│   │   └── globals.css                 # CSS variables, typography tokens & KaTeX imports
│   ├── components/                     # Modular React UI components
│   │   ├── checklist/                  # PYQ Checklist, Question Bank, and filters
│   │   ├── formulas/                   # Master Formulas & Governing Equations view
│   │   ├── timetable/                  # Examination Timetable & Calendar view
│   │   ├── notes/                      # Personal study notes archive
│   │   ├── common/                     # MathRenderer, BackToTop, MobileNav
│   │   └── ui/                         # Clean accessible UI primitives (buttons, dialogs, badges)
│   ├── data/                           # Typed JSON datasets (exported from Python subjects)
│   │   ├── questions.json              # Geotech-2 questions
│   │   ├── canonical.json              # Geotech-2 canonical topics
│   │   ├── formulas.json               # Geotech-2 formulas
│   │   ├── rcc_*.json                  # RCC datasets
│   │   ├── dhs_*.json                  # DHS datasets
│   │   └── timetable.json              # Timetable schedule presets
│   ├── lib/                            # Constants, storage keys, and utility functions
│   └── types/                          # TypeScript definitions for questions, clusters, formulas
│
├── core/                               # Analytical engine & subject utilities
│   ├── subjects.py                     # Subject loader, registry manager, & scaffolding
│   └── formatter.py                    # Solution formatting engine (Zero Wall-of-Text)
│
├── scripts/                            # Data processing & Next.js export utilities
│   └── export-data.py                  # Exports Python subject datasets into src/data/*.json
│
├── subjects/                           # Central repository of all academic subjects
│   ├── registry.json                   # Subject catalog, metadata & active default pointer
│   ├── _template/                      # Rapid onboarding scaffold for any new subject
│   ├── geotech-2/                      # Geotechnical Engineering - II (CE 41007)
│   ├── rcc/                            # Design of Reinforced Concrete Structures (CE 41001)
│   └── dhs/                            # Design of Hydraulic Structures (CE 41006)
└── run                                 # Convenience launcher script (npm run dev)
```

---

## 2. Quickstart: Run the App

To run the application with a single terminal command:

```bash
./run
# or
npm run dev
```

`npm run dev` automatically runs data synchronization (`scripts/export-data.py`) and starts the Next.js development server at `http://localhost:3000`.
- Headless (no auto browser launch): `./run --no-open`
- Skip data re-sync: `./run --no-build`

---

## 3. Build & Type Checking

To verify the TypeScript types and Next.js production build:

```bash
# TypeScript verification
npx tsc --noEmit

# Production build
npm run build
```

---

## 4. Multi-Subject System

Each academic subject is fully self-contained inside `subjects/<subject_id>/`.

### Registered Subjects
| Subject ID | Course Code | Name | Status |
| :--- | :--- | :--- | :--- |
| `geotech-2` | CE 41007 | Geotechnical Engineering - II | **Ready (106 Qs)** |
| `rcc` | CE 41001 | Design of Advanced RCC Structures | **Ready (56 Qs)** |
| `dhs` | CE 41006 | Design of Hydraulic Structures | **Ready (57 Qs)** |
| `water` | CE 31713 | Water Resources Engineering | Planned |
| `sa-2` | CE 31505 | Structural Analysis - II | Planned |
| `sa-1` | CE 31007 | Structural Analysis - I | Planned |
| `geotech-1` | CE 31517 | Geotechnical Engineering - I | Planned |

### State Isolation
Each subject uses an isolated `storage_prefix` defined in `subject.json` (e.g. `geotech`, `rcc`, `dhs`). This guarantees that student study progress (`*_completed_questions`) and filter selections (`*_filters`) never collide across different subjects, while sharing the global theme (`geotech_theme`).

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
