# AGENTS.md — Autonomous Agent Operating Directives

> **Repository:** Exam Intelligence & PYQ Analysis Platform (`exam`)  
> **Target Audience:** All AI Coding Agents, Subagents, and Developers working on this codebase.  
> **Mandate:** Read and adhere strictly to all directives below before modifying or creating code. Keep this document and `RULES.md` updated as requirements evolve.

---

## 1. Zero Wall-of-Text Policy (MANDATORY)

### The Problem
Dense paragraphs, continuous multi-clause sentences, and single-line comma/bullet-separated blocks are unreadable on wide displays, cause cognitive fatigue, and obscure key engineering facts.

### The Standard
- **NEVER** output continuous run-on text or dense paragraphs in table cells, solution blocks, cards, or summaries.
- **ALWAYS** format multi-step strategies, parameter definitions, criteria, occurrences, assumptions, and steps into structured, vertical **bulleted lists**:
  - In tables: Use `<ul class="table-list"><li>...</li></ul>` or `<ul class="table-list table-list-compact"><li>...</li></ul>`.
  - In solution steps: Use `<ul class="sol-list"><li><span class="sol-item-num">1.</span> ...</li></ul>`.
  - In formula definitions: Break down every variable, unit, and condition into an individual list item.
  - In occurrences: Place each exam session (e.g., `2024 Q5(e) OR (7M)`) on its own bullet point.
- **Answer & Solution Step Separation (Zero Inline Continuation)**:
  - **NEVER** continue examples, secondary notes, or sub-points inline on the same line as the explanation sentence.
  - **ALWAYS** move examples to a dedicated new line using a small micro-badge `<span class="example-tag">Eg</span> ...` or dedicated `.sol-item-example`.
  - Split numbered items (`1.`, `2.`, `3.`) and bullet points (`&bull;`, `•`) into separate structured containers so items never run together.
  - **Multi-Part & Sub-List Solutions (Zero Inline Collapse)**: Questions asking two or more distinct concepts (e.g., "Types of Earth Pressure and Theories of Earth Pressure") must format into dedicated numbered section headings (`1.`, `2.`) followed by distinct typographic sub-item rows (`a.`, `b.`, `c.` or `&bull;`). Never cram bullet points or secondary lists into the heading's line or into a previous item's example container.
- **2M (2 Marks) Question Answering Standard (MANDATORY)**:
  - **Tone & Depth**: Exactly to the point, not overly simple and not complex. Complete, clear, direct engineering facts that examiners look for to award full 2/2 marks without fluff or academic rambling.
  - **Definitions with Examples**: Bold concept title, crisp one-line definition, followed by `Example: <practical engineering example>` on its own dedicated line.
  - **Lists (Assumptions, Criteria, Factors, Functions, Objectives)**: Direct numbered list (`1.`, `2.`, `3.`, `4.`, etc.), where each point is a single, clear, self-contained statement. Avoid parenthetical symbol overload or historical tangents.
  - **Differences / Comparisons**: Direct numbered contrast points highlighting failure plane, drainage control, stress distribution, and applicability.
  - **Short Numericals**: Given parameters, governing formula, step-by-step substitution, and final result with units.
- **Micro-Chips & Highlights**:
  - Inline variables/formulas: Wrap with `<span class="formula-chip-sm">...</span>`.
  - Key notices/guaranteed repetitions: Wrap with `<span class="note-highlight">...</span>` or `<span class="note-highlight note-highlight-green">...</span>`.

---

## 2. Typography & Visual Hierarchy

Adhere strictly to the project typography hierarchy specification:

| Hierarchy | Weight | Size | Line Height | Utility / CSS Token |
| :--- | :--- | :--- | :--- | :--- |
| **H1 Headline** | Bold (700) | 56px | 72px | `--font-size-h1` / `--line-height-h1` |
| **H2 Headline** | Bold (700) | 40px | 56px | `--font-size-h2` / `--line-height-h2` |
| **H3 Headline** | Medium (500) | 28px | 40px | `--font-size-h3` / `--line-height-h3` |
| **H4 Headline** | Regular (400) | 26px | 32px | `--font-size-h4` / `--line-height-h4` |
| **H5 Headline** | Regular (400) | 22px | 32px | `--font-size-h5` / `--line-height-h5` |
| **H6 Headline** | Regular (400) | 20px | 28px | `--font-size-h6` / `--line-height-h6` |
| **Body Large** | Medium (500) | 16px | 27px | `--font-size-body-large` / `--line-height-body-large` |
| **Body Medium** | Medium (500) | 14.5px | 22px | `--font-size-body-medium` / `--line-height-body-medium` |
| **Body Small** | Regular (400) | 13px | 18px | `--font-size-body-small` / `--line-height-body-small` |
| **Button** | Semibold (600) | 14px | 21px | `--font-size-button` / `--line-height-button` |

- **Reading Measure Constraint**: Constrain line lengths to 65–80 characters (`max-width: 820px` to `1160px`) for comfortable reading. Never let text stretch indefinitely across wide screens.
- **Card Stat Numbers**: Must be `24px` (`--font-size-stat` / `--line-height-stat`).
- **Overline / Category Labels**: `11px`, `uppercase`, tracking `0.04em`, `var(--muted-foreground)`.

---

## 3. Pure Background Separation (Zero Arbitrary Borders) & Unified Canvas Palette

- **Unified Canvas Palette (Shared Across Timetable & PYQ Master)**:
  - **Light Mode Canvas**: `--background: #fbfaf8` (warm, natural linen/paper canvas), `--card: #ffffff`, `--secondary: #f3f1ec`, `--muted: #f3f1ec`, `--foreground: #1e293b`.
  - **Dark Mode Canvas**: `--background: #09090b` (zinc-950 deep obsidian neutral black), `--card: #141416` (zinc-900 surface), `--secondary: #1c1c1f`, `--muted: #1c1c1f`, `--foreground: #fcfcfd`.
- **No 1px Structural Borders**: Structure containers, cards, and table headers using tonal background shifts (`--background`, `--card`, `--secondary`, `--muted`) rather than harsh borders.
- **Design Tokens**: NEVER hardcode hex codes or RGB strings inside components or markup. Always reference semantic CSS variables (`var(--background)`, `var(--foreground)`, `var(--card)`, `var(--secondary)`).
- **Theme Support**: Ensure all colors work seamlessly across dark mode (`data-theme="dark"`) and light mode (`data-theme="light"`). Both Timetable and PYQ Master share the unified `geotech_theme` localStorage key.
- **No Sparkle Icons**: Never use sparkle icons, generative AI stars, or multi-point sparkle glyphs anywhere in the UI.

---

## 4. Single Source of Truth & Regeneration Pipeline

- The core analytical dashboard is generated programmatically via:
  ```bash
  python3 generate_dashboard.py
  ```
- **Files generated**:
  - `index.html` (Primary production dashboard)
  - `geotech_pyq_analysis.html` (Canonical standalone analysis)
- **Question Bank Engine Directives**:
  - **Zero Heading Clutter**: The Question Bank view starts immediately with the space-efficient Control Panel, removing unnecessary top headings and subheadings for maximum vertical workspace.
  - **Balanced Control Panel & Segmented Filter Matrix (Zero Awkward Wrapping)**:
    - **Top Utility & Search Toolbar (`.control-panel-toolbar`)**: Responsive search input with search shortcut hint badge (`/`) on the left, paired horizontally with live session metrics and quick actions on the right (`2022 Toggle`, `Match counter`, `Completion progress`, `Clear Done`, `Reset`). Eliminates awkward wrapping and prevents lopsided empty lines.
    - **Filter Matrix Rows (`.control-panel-filters`)**: Two clean, symmetrically balanced rows of segmented controls:
      - **Row 1 (Scope, Frequency & Status)**: `Year` (`All`, `2025`, `2024`, `2023`, `2022`), `Repeated` (`All`, `Most Repeated`, `4x`, `3x`, `2x`), and `Status` (`All`, `Incomplete`, `Completed`).
      - **Row 2 (Syllabus, Format & Marks)**: `Unit` (`All`, `Unit 1..5`), `Type` (`All`, `Theory`, `Numerical`, `Derivation`), and `Marks` (`All`, `2M`, `3M`, `7M/6M`).
    - **Apple/Linear Segmented Capsule Track (`.filter-pills-row`)**: Recessed background track (`var(--secondary)`), clean label overlines without colon noise, and elevated active buttons (`var(--filter-pill-active-bg)` / `var(--filter-pill-active-shadow)`), completely eliminating harsh whiteout blobs in dark mode.
    - **Uniform Action Metrics & Toggles**: All top action badges, toggle switches, and buttons maintain uniform 30px height, responsive horizontal scroll on mobile, and smooth hover/active scaling transitions.
  - **Repeated Filter Hierarchy Ordering (4x First, Then 3x, Then 2x - MANDATORY)**: Recurring questions display clean frequency multiplier badges (e.g., `4x`, `3x`, `2x` with no redundant "Repeated" label text) with tooltip details. When the `Most Repeated` filter is selected, verified recurring questions are organized strictly by frequency tier FIRST:
    1. **Tier 1 (4x Repeated)**: 100% Guaranteed concepts appearing across all 4 exam papers (2025, 2024, 2023, 2022) come first.
    2. **Tier 2 (3x Repeated)**: 75% High Probability concepts appearing across 3 exam papers come next.
    3. **Tier 3 (2x Repeated)**: 50% Medium Probability concepts appearing across 2 distinct exam papers come last.
    Within each tier, questions are cleanly organized by syllabus Unit (Unit 1 to Unit 5), then by canonical concept cluster, followed by the verbatim question cards streaming consecutively in adjacent chronological order (2025 card, followed by 2024, 2023, then 2022 card). Each recurring question topic renders a clear `.q-topic-section-header` displaying the canonical concept title, repeat badge (`4x`, `3x`, or `2x`), and frequency meta. Dedicated pill filters (`All`, `Most Repeated`, `4x`, `3x`, `2x`) allow instant one-click filtering. Individual question cards are free of redundant topic overlines, keeping focus directly on the verbatim question statement. Selecting any repeat filter automatically resets Year, Type, and Marks to `All` to ensure all cross-paper occurrences are visible. To clearly distinguish topics, a generous visual space (`.q-topic-section-header`, 2.5rem) is inserted before every new question topic/section, and a distinct Unit section divider (`.q-unit-section-divider`, 3.5rem) separates units. No nested sub-boxes and no artificial batch headers.
  - **Canonical Question Grouping Integrity (Zero False Clustering)**:
    - Questions must NEVER be lumped together into artificial buckets simply because they share generic keywords (e.g. lumping unsupported cut tension crack calculations with retaining walls with high water tables, or lumping generic pile functions with group action of piles).
    - Every cluster in `canonical_data.json` represents a cohesive, conceptually unified topic.
    - Multi-paper repeats require occurrence in distinct examination papers (`clusterYears.length >= 2`). Questions from only a single paper are classified as 1x topics and never masquerade as repeats.
  - **Local Persistence & Completion Engine**: All filters (`year`, `unit`, `type`, `marks`, `repeat`, `status`, `search`), active tab view (`geotech_active_view`), formula filters (`geotech_formula_filters`), and question completion records (`geotech_completed_questions`) are stored in `localStorage` and restored automatically on page load/refresh.
  - **Mark as Complete & Hide Completed**: Questions include an interactive `.complete-btn` that toggles completion status without expanding/collapsing the answer card. The `Status: Incomplete` filter immediately removes/hides completed questions from view, while `Status: Completed` isolates finished questions. Progress metrics (`X / 106 Done`) and "Reset Filters" / "Clear Done" controls provide seamless study session management.
  - **Question Card Header Layout (Number Left, Badges Right)**: Every question card anchors the question number (e.g. `Q.1 (b)`) prominently on the **far left** as `.q-item-qno`. All metadata badges (`Year`, `Unit`, `Type`, `Marks`, `Repeat`, `Done`) are grouped on the **far right corner** alongside the action controls (`Mark Done` button and accordion chevron).
  - **Clean & Un-Cardified Editorial Solutions (Zero Sub-Card Boxes)**: Individual solution points, assumptions, and steps must NEVER be wrapped in nested card containers (`.sol-item-card`), background fills (`--solution-card-bg`), box shadows, or square badge boxes (`.sol-item-badge`). Instead, solutions format as clean, elegant typographic rows (`.sol-item-row`) with natural numbers (`1.`, `2.`), bold concept titles, comfortable line-height (`1.75`), and dedicated lines for examples (`Example: ...`). Multi-line text wraps cleanly under the text margin via flex alignment, preserving effortless readability and zero wall-of-text fatigue.
  - **Verbatim PYQ Question as Card Headline & Zero Topic Clutter**: Every question card presents the actual verbatim question statement asked in the PYQ paper (`item.question`) cleanly as its primary heading (`.q-item-title`) without bracket `[]` marks and without any intermediate topic overlines (`Topic:` removed from question cards). Metadata chips clearly display Exam Year, Unit, Question Type, Marks (`2M`, `3M`, `7M` as a normal `.badge-subtle` badge with no mono font and no bold), and Repeat Count (`4x`, `3x`, or `2x`). Dedicated Marks filter and search support allow filtering specifically by marks.
- **Data inputs**:
  - `canonical_data.json` (59 clean, deduplicated core topics)
  - `compile_data.py` (106 verified raw questions across 4 exam years: 2025, 2024, 2023, 2022)
- **PYQ Checklist Engine Directives (Year-wise, then Unit-wise)**:
  - Replaces the legacy static syllabus breakdown table with an interactive, year-wise and unit-wise PYQ checklist across all 106 verified questions (2025: 28 Qs, 2024: 25 Qs, 2023: 28 Qs, 2022: 25 Qs, covering Units 1 to 5 within each exam paper).
  - **Distinct Color Year Badges**: Each exam year has its own unique, accessible pastel color token: 2025 (Sage Green `.badge-year-2025`), 2024 (Sky Blue `.badge-year-2024`), 2023 (Lavender Purple `.badge-year-2023`), 2022 (Warm Sand `.badge-year-2022`) across both Question Bank and Checklist cards.
  - **Minimal, Zero-Clutter Architecture & In-Place Answer Expansion**: Free of explanatory subtitles, redundant "View in Bank" buttons, and verbose labels. Entire question cards are clickable to expand and view the verified solution right there in place without redirecting to the Question Bank. An unobtrusive "Open in Question Bank &rarr;" jump button is provided at the bottom of the expanded solution for deep cross-question study when needed.
  - **Two-Way Real-Time Synchronization**: Toggling a question's completion state in either the Checklist or Question Bank instantly synchronizes `localStorage` (`geotech_completed_questions`), overall completion counters, year-level progress meters, and unit-level subhead counters.
  - **In-Place Accordion Engine (`toggleChecklistSolution`)**: Clicking any checklist card smoothly toggles its solution container (`chk-sol-*`), rotates the `.chk-chevron` icon (180&deg;), and sets `.is-open`. Clicking inside the solution text, highlighting/copying formulas, or toggling completion never collapses the card. KaTeX math typesetting is automatically triggered on toggle.
  - **Checklist Controls & Filtering**: Features total completion progress, quick year-jump pills (`2025`, `2024`, `2023`, `2022`), checklist status pills (`All`, `Incomplete`, `Done`), and live real-time filtering (including matching across solution text).
- **Rule**: Whenever modifying layout, tables, styles, or data, ALWAYS make changes in `generate_dashboard.py` (or data sources) and re-run `python3 generate_dashboard.py`. Do NOT make isolated manual edits to `index.html` without reflecting them in the generator.

---

## 5. Floating Back-to-Top Navigation

- A persistent, high-contrast floating back-to-top button (`.scroll-to-top-btn`) is fixed and permanently visible at the bottom-right corner of all views (`bottom: 2rem; right: 2rem; z-index: 99999; width: 48px; height: 48px; border-radius: var(--radius-full);`).
- Features a clean Lucide/Feather arrow-up SVG icon (`<polyline>` and `<line>` with 2.5px stroke), semantic design token styling (`--primary`, `--primary-foreground`, `box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28)`), and smooth scrolling behavior (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
- Always visible across desktop and mobile (`opacity: 0.95`, hover elevation to `scale(1.05)`).

---

## 6. Smart Auto-Hide Header Navbar on Scroll

- **Behavior**: The sticky header navbar (`.header`) automatically translates off-screen (`transform: translateY(-100%)`, `header-hidden`) on downward scroll, and smoothly glides back into view (`transform: translateY(0)`) on upward scroll.
- **Top Threshold Immunity**: The header is permanently visible when `scrollY <= 64px` (top of page or during elastic rubber-banding bounce).
- **Navigation & Jump Integration**: Switching view tabs (`switchPageView`), clicking the floating back-to-top button, or jumping to top immediately resets and displays the navbar (`header.classList.remove('header-hidden')`).
- **Clean Brand Header**: The navbar presents the clean course title (`.brand-title`) without redundant course code or colored brand badges.

---

## 7. Continuous Documentation Updates

- Whenever a new pattern, UI rule, or engineering requirement is established by the user, **immediately update this file (`AGENTS.md`) and `RULES.md`**.
- Keep all future agents aligned on the exact aesthetic and structural conventions.

---

## 8. Global 2022 Exam Paper Visibility Toggle

- **Universal Scope Control**: Allows users to include or completely hide the 2022 examination paper across all views and analytical computations in the Geotech application.
- **Dedicated In-View Control Architecture (Clean Navbar)**:
  - **Header Navbar**: Kept clean, uncluttered, and minimal with only page navigation and the theme toggle (the 2022 toggle is removed from the top navbar).
  - **Question Bank Control Panel (`#panelToggle2022Btn`)**: Integrated directly into the Top Toolbar of the control panel alongside session metrics (`Match Counter`, `Completion Progress`, and `Reset`) for immediate context-aware toggling without redundant outer labels.
  - **Unit Checklist Engine (`#checklistToggle2022Btn`)**: Integrated in the checklist summary units toolbar so users can easily include or hide the 2022 paper within the syllabus checklist.
- **Dynamic Scope Recalculation Engine**:
  - **Question Bank Engine**: When 2022 is hidden, filters out all 2022 question cards, hides the `2022` year filter pill (`#filterPill2022`, resetting to `all` if 2022 was selected), and updates match counters (`X of 81 matched` vs `X of 106 matched`).
  - **Unit Checklist Engine**: Completely hides `#year-section-2022` and `#checklistYearPill-2022`, presents `#checklistToggle2022Btn` for one-click re-inclusion, and updates total question base, completion meters, and status pill badges.
  - **Dynamic Repeat Analysis (`getRepeatInfo`)**: Recalculates cluster occurrence frequencies and `3x` / `2x` repeat badges strictly among visible papers.
  - **Study Progress & Completion Tracker**: Counts and clears completed questions strictly within the active scope.
- **State Persistence & Deep-Link Recovery**:
  - Automatically saved to and restored from `localStorage` (`geotech_hide_2022`).
  - If a user navigates or deep-links directly to a 2022 question (`jumpToQuestionBank`), the system automatically restores 2022 visibility to display and highlight the requested question.

---

## 9. Responsive Web App Architecture (Mobile & Tablet Experience)

- **Mobile Viewport & PWA Foundation**:
  - Viewport configured with `width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover`.
  - PWA tags enabled (`mobile-web-app-capable`, `apple-mobile-web-app-capable`, `apple-mobile-web-app-status-bar-style: default`).
  - Dynamic `#metaThemeColor` updates with theme toggle (`#fbfaf8` light, `#09090b` dark).
- **Native App-Style Mobile Bottom Navigation Bar**:
  - Fixed at viewport bottom on screens `<= 768px` with iOS safe area inset support (`env(safe-area-inset-bottom)`).
  - 4 primary destinations: **Questions**, **Checklist**, **Formulas**, and **Timetable**.
  - Synchronized in real time with `switchPageView(pageId)` and URL hash routing.
  - On desktop (`> 768px`), automatically hidden, displaying the top header navigation.
- **Fluid Container & Measure**:
  - Container padding defaults to `padding-left: max(1rem, env(safe-area-inset-left)); padding-right: max(1rem, env(safe-area-inset-right));` on mobile, scaling to `1.5rem` (tablets) and `2.5rem`-`3.5rem` (desktops).
  - `html, body { overflow-x: hidden; -webkit-text-size-adjust: 100%; }` prevents horizontal rubber-band blowout.
- **Touch Targets & Immediate Response**:
  - `-webkit-tap-highlight-color: transparent` and `touch-action: manipulation` across interactive controls.
  - Filter pills, checkboxes, and buttons maintain comfortable minimum touch targets (32px–44px).
  - Floating back-to-top button offsets automatically to `bottom: calc(72px + env(safe-area-inset-bottom))` on mobile to avoid bottom nav overlap.
- **Horizontal Swipe Momentum**:
  - Filter pill bars, formula unit filters, and checklist year pills glide horizontally with smooth touch scrolling (`overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none`).
- **Mathematical Formula & Table Overflow Immunity**:
  - All KaTeX mathematical display equations (`.katex-display`) and data tables enforce `overflow-x: auto` and `max-width: 100%`, guaranteeing mathematical clarity without breaking page boundaries.

---

## 10. Calendar Current Date Tracking & Visual Indicators (`timetable.html`)

- **Dedicated Blue Box Banner (`.cal-today-box`)**:
  - Located at the top of the Separated Calendar view (`#calendar-view`).
  - Styled with semantic design tokens: `var(--pastel-sky-bg)`, `var(--pastel-sky-border)`, `var(--pastel-sky-foreground)`.
  - Displays the current date formatted (e.g. `Current Date: Monday, 16 November 2026`) and an automated countdown badge to the nearest upcoming exam paper (e.g. `18 Nov (Geo-2) • in 2 days`).
- **Calendar Grid Cell Blue Box (`.cal-cell.today` / `.cal-cell.current-date`)**:
  - Highlights today's date in the calendar grid with a blue background, border, and `<span class="cal-cell-tag">Today</span>` micro-tag, seamlessly matching the sage green (Regular) and peach (Old Syllabus) exam boxes.
  - Handles exam collision gracefully (`.cal-cell.today.exam-reg` / `.cal-cell.today.exam-old`) by preserving exam category fills with a dual blue focus ring.
- **Header Badges & Key Legend Integration**:
  - Includes `Today` key indicator in the notice bar: `<span class="badge badge-sky">Today</span> Current Date`.
  - November and December month headers display context-sensitive `Today: [Day] [Month]` pills when active.
- **Real-Time Client Synchronization (`initCurrentDateTracker`)**:
  - Client-side JavaScript detects `new Date()`, calculates day offsets to remaining schedule papers, marks matching `[data-date]` cells, and preserves the active session reference when testing outside the timetable range.

---

## 11. Modular Multi-Subject Architecture & Directory Governance

- **Modular Subject Hierarchy (`subjects/`)**:
  - Every academic subject lives self-contained under `subjects/<subject_id>/` (e.g. `subjects/geotech-2/`, `subjects/rcc/`, `subjects/dhs/`, `subjects/water/`, `subjects/sa-2/`).
  - **Required Subject Files**:
    1. `subject.json`: Course code, name, short name, storage prefix, and unit titles.
    2. `canonical_data.json`: Deduplicated topic clusters and frequency metadata.
    3. `compile_data.py`: Verified questions array containing verbatim paper questions, solutions, marks, and taxonomy.
    4. `master_formulas.json`: Governing equations, LaTeX strings, parameters, and engineering notes.
    5. `formula_showcase.py`: Subject-specific LaTeX enhancements and formula display post-processing.
    6. `papers/`: High-resolution question paper scans and raw sources.
  - **Subject Registry (`subjects/registry.json`)**: Central catalog of all registered subjects, build status, and the `active_subject` pointer.
  - **Template Scaffold (`subjects/_template/`)**: Rapid onboarding scaffold for any new subject.
- **Root Compatibility Proxies**:
  - Root `compile_data.py` and `formula_showcase.py` proxy directly to `subjects/geotech-2/` so legacy tools and imports continue to function without disruption.
- **Local-Only Timetable Policy (Gitignored)**:
  - The exam timetable is **local-only** and must never be committed to git.
  - `timetable.html`, `build_timetable.py`, `tools/timetable/`, and timetable PDFs/OCR files are strictly listed in `.gitignore`.
  - `timetable.html` remains at the workspace root so local navigation from `index.html` resolves seamlessly in browsers.
- **Master CLI Generation Engine (`generate_dashboard.py`)**:
  - Default build: `python3 generate_dashboard.py` (builds active default subject `geotech-2` -> `index.html` & `geotech_pyq_analysis.html`).
  - Specific subject: `python3 generate_dashboard.py <subject_id>`.
  - List registered subjects: `python3 generate_dashboard.py --list`.
  - Batch build all ready subjects: `python3 generate_dashboard.py --all`.
  - Scaffold new subject: `python3 generate_dashboard.py --new <id> "<name>" "<code>"`.
- **Clean Workspace Rule**:
  - Tests reside in `tests/`.
  - Archived/legacy scripts reside in `archive/`.
  - No loose scratch or test scripts in the root directory.
