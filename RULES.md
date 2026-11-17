# Repository Rules & Constraints (`exam`)

> **Active Guidelines for all changes and code generation.**  
> *Always review and keep this file updated with every session.*

---

### [RULE 1] Anti-Wall-of-Text: Always Bullet Multi-Clause & Dense Text
- **Never display continuous, single-line, run-on text** for strategies, parameters, occurrences, criteria, or steps in tables, cards, or modals.
- **Always format as vertical, styled bullet lists**:
  - Tables: `<ul class="table-list"><li>...</li></ul>`
  - Compact lists (e.g. occurrences): `<ul class="table-list table-list-compact"><li>...</li></ul>`
  - Solution steps: `<ul class="sol-list"><li><span class="sol-item-num">...</span> ...</li></ul>`
- **Answers & Solutions Formatting (Zero Inline Continuation)**:
  - NEVER let examples, secondary notes, or sub-points continue inline on the same sentence line.
  - ALWAYS place examples on their own dedicated new line with a small micro-badge `<span class="example-tag">Eg</span> ...` or dedicated `.sol-item-example`.
  - Numbered items (`1.`, `2.`, `3.`) and bullet points (`&bull;`, `•`) MUST be split into distinct structured blocks with `<span class="sol-item-num">` for clear, readable vertical hierarchy.
  - Multi-part questions asking two or more concepts (e.g. "Types of Earth Pressure and Theories of Earth Pressure") MUST structure as dedicated numbered section headings (`1.`, `2.`) followed by distinct typographic sub-item rows (`a.`, `b.`, `c.` or `&bull;`), never collapsing bullets into the heading line or an example block.
- **2M (2 Marks) Question Answering Standard**:
  - Tone & Depth: Exactly to the point, not overly simple and not complex. Complete, clear, direct engineering facts for full 2/2 marks without fluff.
  - Definitions with Examples: Bold concept title, crisp one-line definition, followed by `Example: <practical engineering example>` on its own dedicated line.
  - Lists (Assumptions, Criteria, Factors, Functions, Objectives): Direct numbered list (`1.`, `2.`, `3.`, `4.`, etc.), where each point is a single, clear, self-contained statement.
  - Differences: Direct numbered contrast points highlighting failure plane, drainage control, stress distribution, and applicability.
  - Short Numericals: Given parameters, governing formula, step-by-step substitution, and final result with units.
- **Use semantic micro-chips**: `<span class="formula-chip-sm">` for formulas/symbols and `<span class="note-highlight">` for notable highlights.

---

### [RULE 2] Strict Typography System
- Always adhere to the defined typography tokens:
  - H1 (56/72), H2 (40/56), H3 (28/40), H4 (26/32), H5 (22/32), H6 (20/28).
  - Body Large (16/27), Body Medium (14.5/22), Body Small (13/18), Button (14/21).
  - Stat cards: 24px (`--font-size-stat`).
  - Overlines: 11px uppercase (`--font-size-overline`).
- Constrain reading line-length (65–80 characters) to preserve readability.

---

### [RULE 3] Pure Background Separation (Zero Borders) & Unified Canvas Palette
- Maintain zero 1px structural borders throughout the application.
- Unified canvas palette shared between Examination Timetable (`timetable.html`) and PYQ Analysis Platform (`index.html`):
  - **Light Mode**: `--background: #fbfaf8` (warm linen/paper ivory), `--card: #ffffff`, `--secondary: #f3f1ec`, `--muted: #f3f1ec`, `--foreground: #1e293b`.
  - **Dark Mode**: `--background: #09090b` (zinc-950 deep obsidian black), `--card: #141416`, `--secondary: #1c1c1f`, `--muted: #1c1c1f`, `--foreground: #fcfcfd`.
- Separate regions, cards, and tables using background tonal elevation:
  - `--background`: base canvas
  - `--card`: elevated surface
  - `--secondary`: pills, chips, inputs, code blocks
  - `--table-header-bg` & `--table-row-hover`: subtle contrast for data tables

---

### [RULE 4] No Hardcoded Colors & No Sparkle Icons
- NEVER use hex values, rgb(), or arbitrary color codes directly in markup. Always use CSS variables.
- NEVER use sparkle icons, AI star glyphs, or sparkles in any UI component or graphic.

---

### [RULE 5] Pipeline Integrity & Automated Build Verification
- Any modification to UI structure or content must be made in `generate_dashboard.py` (and relevant source data).
- **Question Bank Control Panel**:
  - Unnecessary top headings and subheadings are removed from the Question Bank view for an immediate, high-efficiency dashboard workspace.
  - **Balanced Control Panel & Segmented Filter Matrix (Zero Awkward Wrapping)**:
    - **Top Toolbar (`.control-panel-toolbar`)**: Responsive search input with search shortcut hint badge (`/`) on the left, paired horizontally with live session metrics and quick actions on the right (`2023 Toggle`, `Match counter`, `Completion progress`, `Clear Done`, `Reset`). Eliminates awkward wrapping and prevents lopsided empty lines.
    - **Filter Matrix Rows (`.control-panel-filters`)**: Two clean, symmetrically balanced rows of segmented controls:
      - **Row 1 (Scope, Frequency & Status)**: `Year` (`All`, `2025`, `2024`, `2023`, `2022`), `Repeated` (`All`, `Most Repeated`, `4x`, `3x`, `2x`), and `Status` (`All`, `Incomplete`, `Completed`).
      - **Row 2 (Syllabus, Format & Marks)**: `Unit` (`All`, `Unit 1..5`), `Type` (`All`, `Theory`, `Numerical`, `Derivation`), and `Marks` (`All`, `2M`, `3M`, `7M/6M`).
    - **Apple/Linear Segmented Capsule Track (`.filter-pills-row`)**: Recessed background track (`var(--secondary)`), clean label overlines without colon noise, and elevated active buttons (`var(--filter-pill-active-bg)` / `var(--filter-pill-active-shadow)`), completely eliminating harsh whiteout blobs in dark mode.
    - **Uniform Action Metrics & Toggles**: All top action badges, toggle switches, and buttons maintain uniform 30px height, responsive horizontal scroll on mobile, and smooth hover/active scaling transitions.
- The Question Bank view presents complete examination papers exclusively (106 questions across 2025, 2024, 2023, 2022). Recurring questions display frequency badges (`4x`, `3x`, `2x` with no text "Repeated") with tooltips. When `Most Repeated` (or repeat frequency: `4x`, `3x`, `2x`) is active, recurring questions are organized strictly by repeat frequency tier FIRST (Tier 1: 4x repeated across all 4 papers first, Tier 2: 3x repeated across 3 papers second, Tier 3: 2x repeated third), and within each tier by Unit (Unit 1–5), rendering a clear `.q-tier-section-divider` for each tier and `.q-topic-section-header` for each concept, followed by the question cards streaming consecutively in adjacent chronological order (e.g. 2025 card, followed by 2024, 2023, then 2022 card). Individual question cards are free of redundant topic overlines, keeping focus directly on the verbatim question statement. Selecting any repeat filter automatically resets Year, Type, and Marks to `All` so all cross-paper occurrences are visible. Generous distinguishing spacing (`.q-topic-section-header`, 2.5rem) separates topic sections, and Unit dividers (`.q-unit-section-divider`, 2rem) separate units. No nested sub-boxes and no batch headers. Standalone "Most Repeated" and "Overview" tabs are deprecated in favor of integrated filtering.
- **Persistence Across Refresh**: Filter selections, search input, active page view, formula filters, and question completion states (`localStorage`) must persist reliably across reloads.
- **Completion & Removal Controls**: Users must be able to mark individual questions as Done / Incomplete via dedicated card buttons (without toggling the solution open/closed). Completed questions must be filterable via the Status pills (`Incomplete` hides/removes completed questions, `Completed` isolates them). A progress badge and reset controls must be provided.
- Always verify generation by executing:
  ```bash
  python3 generate_dashboard.py
  ```
- Confirm `index.html` and `geotech_pyq_analysis.html` are regenerated cleanly with exit code 0.

---

### [RULE 6] Question Presentation, Header Layout & Un-Cardified Solutions
- **Question Card Header Layout (Number Left, Badges Right Corner)**:
  - Every question card positions the question number (e.g. `Q.1 (b)`) on the **far left** (`.q-item-qno`).
  - All metadata badges (`Year`, `Unit`, `Type`, `Marks`, `Repeat`, `Done`) are grouped on the **far right corner** (`.q-item-right-meta`) alongside the `Mark Done` button and accordion toggle chevron.
- **Clean & Un-Cardified Editorial Solutions (Zero Sub-Card Boxes)**:
  - Individual solution points, assumptions, and steps must NEVER be wrapped in nested card containers (`.sol-item-card`), background fills (`--solution-card-bg`), box shadows, or square badge boxes (`.sol-item-badge`).
  - Solutions format as clean, elegant typographic rows (`.sol-item-row`) with natural numbers (`1.`, `2.`), bold concept titles, comfortable line-height (`1.75`), and dedicated lines for examples (`Example: ...`).
  - Flex alignment ensures wrapped multi-line text wraps cleanly under the text margin, not under the number, guaranteeing effortless legibility and zero wall-of-text fatigue.
- **Actual PYQ Question as Headline**: In the Question Bank cards (`#view-questions`), the primary bold headline (`.q-item-title`) must ALWAYS be the actual verbatim question asked in the PYQ paper (`item.question`), never an abstract or syllabus-only topic label.
- **Marks Display (`2M`, `3M`, `7M`) as Normal Badge**: Marks must be displayed as a normal badge (`.badge-subtle`) in the question header badges (`<span class="badge badge-subtle">${item.marks}M</span>`) with standard sans font and normal weight—NO monospace font, NO bold font, and NO bracket `[]` or parenthesis marks cluttering the question title or overline headline.
- **Dedicated Marks Filter & Search**: Dedicated Marks filter pills (`All`, `2M`, `3M`, `7M / 6M`) in the control panel and full-text search match mark queries (`2M`, `3M`, `7M`).
- **Zero Topic Clutter on Question Cards**: Question cards present the verbatim question statement cleanly and directly without any `Topic:` overline or topic label clutter. Topic metadata remains searchable in full-text search, and recurring concept headers (`.q-topic-section-header`) organize clusters when `Most Repeated` is active.
- **Complete Metadata**: Badges must clearly reflect Exam Year, Unit, Question Type, Marks (`2M`, `3M`, `7M`), and Repeat Count (`<Nx> Repeated`), alongside Question Number (`Q.1 (a) (2M)`).
- **Cross-Year PYQ Question Variations**: For repeated topics/concepts, all question variations asked in other examination sessions must be cleanly rendered within a pure-background `.q-other-pyqs-box` displaying the year, question number, marks (`(2M)`, `(3M)`, `(7M)`), and exact question statement from those other papers.

---

### [RULE 7] PYQ Checklist (Year-wise, then Unit-wise) & Distinct Year Badges
- **Year-wise, then Unit-wise Structure**: The checklist organizes questions primarily by Exam Year (2025, 2024, 2023, 2022), and inside each year by syllabus Unit (Unit 1 to 5).
- **Distinct Color Year Badges**: Always use dedicated pastel color classes for exam years across both Question Bank and Checklist cards:
  - 2025: Sage Green (`.badge-year-2025`)
  - 2024: Sky Blue (`.badge-year-2024`)
  - 2023: Lavender Purple (`.badge-year-2023`)
  - 2022: Warm Sand / Gold (`.badge-year-2022`)
- **Zero-Clutter Directive & In-Place Answer Expansion**: Eliminate redundant explanatory paragraphs, boilerplate slogans, and duplicate action buttons. The entire card is clickable to reveal its complete step-by-step verified solution right there in place without redirecting to the Question Bank. A subtle "Open in Question Bank &rarr;" jump button is located at the bottom of the expanded solution for deep cross-question study when needed.
- **Two-Way Completion Synchronization**: Toggling question completion from either the Question Bank or the Checklist immediately synchronizes `localStorage` (`geotech_completed_questions`), overall completion counters, year-level progress bars, and unit subhead counters.
- **In-Place Solution Accordion (`toggleChecklistSolution`)**: Clicking any checklist card smoothly toggles its solution container (`chk-sol-*`), rotates the chevron icon (`.chk-chevron`), and sets `.is-open`. Clicking inside the solution text, copying formulas, or clicking the completion button never collapses the card. KaTeX math typesetting is automatically triggered on toggle.

---

### [RULE 8] Living Rules Maintenance
- Always maintain and update `AGENTS.md` and `RULES.md` as new conventions, data structures, or styling rules are introduced.

---

### [RULE 9] Floating Back-to-Top Action Button
- A floating back-to-top button (`.scroll-to-top-btn`) must be permanently visible in the bottom-right corner (`position: fixed; bottom: 2rem; right: 2rem; z-index: 99999; width: 48px; height: 48px; border-radius: var(--radius-full);`).
- Must use high-contrast theme tokens (`--primary` background, `--primary-foreground` arrow color, `box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28)`) for immediate prominence and zero hardcoded colors.
- Uses an accessible feather/lucide upward arrow SVG icon (`line` + `polyline` with stroke width 2.5), smoothly scrolls to top on click (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
- Responsive styling adjusts margins for mobile viewports (`max-width: 640px` adjusts offset to `1.25rem`).

---

### [RULE 10] Smart Auto-Hide Header Navbar on Scroll
- The sticky header navbar (`.header`) automatically translates off-screen (`transform: translateY(-100%)`, `.header.header-hidden`) on downward scroll, and smoothly reveals (`transform: translateY(0)`) on upward scroll via hardware-accelerated cubic-bezier transitions (`will-change: transform`).
- Near top of page (`scrollY <= 64px`), the header is guaranteed visible and protected against trackpad rubber-band bounce.
- Switching views via `switchPageView()` or clicking back-to-top immediately resets and surfaces the navbar.
- The header brand displays the clean title without redundant course code or colored brand badges.

---

### [RULE 11] Global 2023 Exam Paper Visibility Toggle
- **Universal Scope**: Provides an instant global toggle to include or hide the entire 2023 examination paper across all views (Question Bank, Unit Checklist, repeat analysis, and completion metrics).
- **In-View Contextual Controls (Clean Navbar)**:
  - **Header Navbar**: Top navbar remains clean, focused, and free of the 2023 toggle.
  - **Control Panel Quick Toggle (`#panelToggle2023Btn`)**: Integrated directly into the Top Toolbar of the Question Bank Control Panel alongside session metrics (`Match Counter`, `Completion Progress`, and `Reset`) for frictionless one-click toggling without redundant outer labels.
  - **Unit Checklist Quick Inclusion (`#checklistToggle2023Btn`)**: Accessible in the Unit Checklist summary to easily restore the 2023 paper.
- **Dynamic Scope & Metrics Recalculation**:
  - **Question Bank**: Removes all 2023 question cards from the DOM, hides the `2023` filter pill (`#filterPill2023`, resetting to `'all'` if active), and updates match counts (`X of 78 matched` when hidden vs `X of 106 matched` when shown).
  - **Unit Checklist**: Hides the entire `#year-section-2023` container and `#checklistYearPill-2023`, rendering a dashed quick-include button (`#checklistToggle2023Btn`), while updating total counts (`78 Completed / Incomplete`) and progress percentages.
  - **Repeat Concept Analysis**: Uses `getRepeatInfo(item, items)` to dynamically compute cluster repeat counts (`3x`, `2x`) strictly among visible papers, preventing false recurring tags for concepts that only occurred in 2023 and another single paper.
  - **Completion Metrics & Clear Done**: Counts and unmarks completed questions strictly within the active scope.
- **State Persistence & Deep Jump Recovery**:
  - Persisted in `localStorage` under `geotech_hide_2023` (`"true"` / `"false"`).
  - Calling `jumpToQuestionBank(id)` for a 2023 question automatically restores 2023 visibility, ensuring the requested question is rendered, expanded, and focused smoothly.

---

### [RULE 12] Canonical Question Grouping & Repeat Integrity (Zero False Clustering)
- **Conceptual Homogeneity**: Questions must NEVER be lumped together into artificial buckets simply because they share generic keywords (e.g., lumping unsupported cut tension crack calculations with retaining walls with water tables, or lumping generic pile functions with group action of piles).
- **True Multi-Paper Repeats**: A topic is classified as repeated (`4x`, `3x`, `2x`) ONLY if it appears across 4, 3, or 2 distinct examination papers (`clusterYears.length >= 2`). Questions appearing only in a single paper are classified as 1x topics and must never masquerade as repeats.
- **Specific Topic Separation**:
  - `u4-pile-group-action`: Contains only group action of piles (`2024-Q4a`). Pile functions (`2022-Q4a`) and shallow vs deep foundation differences (`2022-Q4b`) are maintained as separate topics.
  - `u1-tension-crack-cut`: Contains only tension crack and critical depth of unsupported cut in cohesive soil (`2022-Q1a`). Retaining wall active pressure with water table (`2025-Q1biii`, `2023-Q1biii`) is maintained as its own dedicated 2x repeat topic.
  - `u3-bearing-capacity-suffixes`: Unifies identical definitions & terminology suffix questions (`2025-Q2a` and `2023-Q2a`) under Unit 3 as a true 2x repeated topic.
  - `u3-eccentric-footing-numerical`: Contains only rectangular footings with biaxial eccentricity (`2025-Q2c-OR`, `2023-Q2c-OR`). Circular footing diameter on saturated clay (`2022-Q3e-OR`) is separated.
  - `u3-square-footing-clay`: Contains only square footing net safe bearing capacity in pure clay (`2025-Q2biii`, `2023-Q2biii`). Strip footing width design in $c-\phi$ soil (`2025-Q4c-OR`, `2023-Q4c-OR`) is maintained as its own topic.

---

### [RULE 13] Responsive Web App Architecture (Mobile & Tablet Experience)
- **Viewport & PWA Foundation**: Every HTML entry point must set `<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">`, enable PWA standalone/mobile-web-app-capable tags, and keep `#metaThemeColor` synced with theme changes.
- **Native App Mobile Bottom Navigation Bar**: Fixed at the viewport bottom on screens `<= 768px` with iOS safe area inset support (`env(safe-area-inset-bottom)`), hosting Questions, Checklist, Formulas, and Timetable with synchronized routing.
- **Fluid Container Padding**: Maintain `padding-left: max(1rem, env(safe-area-inset-left)); padding-right: max(1rem, env(safe-area-inset-right));` on mobile screens instead of harsh fixed desktop paddings.
- **Immediate Touch Response & Zero Tap Delay**: Apply `-webkit-tap-highlight-color: transparent` and `touch-action: manipulation` across all buttons, interactive pills, and tabs.
- **Overflow Immunity**: Ensure all KaTeX display equations (`.katex-display`) and data tables enforce `overflow-x: auto` and `max-width: 100%`, preventing horizontal document blowouts.

---

### [RULE 14] Calendar Current Date Tracking & Blue Box System
- **Current Date Blue Box in Calendar View**: The Separated Calendar view (`timetable.html`) must display a dedicated blue box (`.cal-today-box`) showing the active client date and an automatic countdown pill to the next upcoming examination paper.
- **Calendar Grid Day Highlight**: The active day's cell in the November/December grid must be styled with the blue palette token (`.cal-cell.today` / `.cal-cell.current-date`), rendering `<span>[Day]</span><span class="cal-cell-tag">Today</span>` alongside the existing green (Regular) and peach (Old Syllabus) exam boxes.
- **Color Token Compliance**: Never hardcode hex values. Use `var(--pastel-sky-bg)`, `var(--pastel-sky-border)`, and `var(--pastel-sky-foreground)` across all current date indicators.
- **Automatic Client Synchronization**: `initCurrentDateTracker()` must dynamically match `new Date()` against `[data-date]` attributes while safely handling fallbacks.

---

### [RULE 15] Modular Multi-Subject Architecture & Local Timetable Isolation
- **Self-Contained Subject Units**: All academic subjects must reside under `subjects/<subject_id>/` containing `subject.json`, `canonical_data.json`, `compile_data.py`, `master_formulas.json`, `formula_showcase.py`, and `papers/`.
- **Subject State Isolation**: Each subject must declare a unique `storage_prefix` in `subject.json` (e.g. `geotech`, `rcc`) so user completion data and filters do not collide, while maintaining the shared `geotech_theme` key for global light/dark theme preference.
- **Local Timetable Policy (Gitignored)**: The examination timetable is local-only. `timetable.html`, `build_timetable.py`, `tools/timetable/`, and source PDFs must remain in `.gitignore` and never be committed to git.
- **Master CLI Generation Engine**: `python3 generate_dashboard.py` builds the active default subject (`geotech-2`) into `index.html` and `geotech_pyq_analysis.html`. Passing `<subject_id>` builds that subject, `--list` inspects the registry, and `--new <id> "<name>" "<code>"` scaffolds a new subject module.
- **Root Proxy Immutability**: Root `compile_data.py` and `formula_showcase.py` proxy directly to `subjects/geotech-2/` ensuring 100% backward compatibility for all scripts and agents.

---

### [RULE 16] Personal Notes, Custom Answers & Study Scratchpad Engine
- **In-Card Pen Action Button (`.note-action-btn`)**: Question cards in both the Question Bank (`.q-item-actions`) and PYQ Checklist (`.checklist-card-actions`) must include an accessible pen icon button to add, edit, or toggle personal notes/answers. Questions with saved notes must display a visual dot indicator (`.note-indicator-dot`) and subtle active styling.
- **In-Card Solution Toggle Switch (`.sol-view-switch-row`)**: The solution block of every question card must feature a capsule toggle switch allowing seamless switching between `Verified Solution` and `My Answer ✍️` directly on the card. This toggle must remain strictly isolated to the specific card without affecting any other question.
- **Zero Wall-of-Text Formatting**: Custom answers must be rendered via `renderUserAnswerHtml()` preserving structured vertical bullet lists (`.sol-list`), numbered points, dedicated `Example:` micro-tags (`.example-tag`), and clean paragraph spacing.
- **Dedicated Notes Page (`#view-notes`)**:
  - Must be navigable from the sticky top header (`Notes` with live count badge) and mobile bottom navigation bar.
  - Hosts the General Revision Scratchpad (`.general-scratchpad-card`) for subject-wide formulas and notes with real-time auto-saving.
  - Features real-time keyword search and Unit filter capsules (`All`, `Unit 1..5`).
  - Displays the saved questions archive with formatted answers, quick edit/delete actions, and an "Open in Bank &rarr;" jump button (`jumpFromNotesToQuestion`).
- **Multi-Tier Persistence Guarantee ("Never Lose Notes")**:
  - Primary instant persistence in `localStorage` (`<prefix>_user_notes`, `<prefix>_general_notes`).
  - Asynchronous background synchronization to disk via `POST /api/progress` (`user_progress.json`).
  - Embedded data bootstrap in generated HTML (`EMBEDDED_NOTES`, `EMBEDDED_GEN_NOTES`).
  - JSON Backup export (`exportNotesJSON`) and import (`triggerImportNotes`), plus clipboard copy utilities on the Notes page.
