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
- **KaTeX Fraction Line & Border Immunity (NEVER use `border: none !important` on universal `*`)**:
  - KaTeX mathematical rendering relies on CSS borders for fraction division bars (`.mfrac .frac-line`), square roots, overlines, and rules.
  - **NEVER** apply `border: none !important;` to universal selectors (`*`, `*::before`, `*::after`). Doing so strips fraction division bars and mathematical lines.
  - Target form control resets specifically (`button, input, select, textarea { border: none; outline: none; }`).
  - Explicitly enforce `.katex .mfrac .frac-line { border-bottom-style: solid !important; border-bottom-width: max(1.2px, 0.05em) !important; border-bottom-color: currentColor !important; min-height: 1.2px !important; }` to guarantee crisp, distinct fraction dividing lines across all screen resolutions and dark/light themes.
- Unified canvas palette shared between Examination Timetable (`timetable.html`) and PYQ Analysis Platform (`index.html`):
  - **Light Mode**: `--background: #fbfaf8` (warm linen/paper ivory), `--card: #ffffff`, `--secondary: #f3f1ec`, `--muted: #f3f1ec`, `--foreground: #1e293b`.
  - **Dark Mode**: `--background: #09090b` (zinc-950 deep obsidian black), `--card: #141416`, `--secondary: #1c1c1f`, `--muted: #1c1c1f`, `--foreground: #fcfcfd`.
- Separate regions, cards, and tables using background tonal elevation:
  - `--background`: base canvas (`#fbfaf8` light / `#09090b` dark)
  - `--card`: elevated surface for panels and closed question cards (`#ffffff` light / `#141416` dark)
  - `--secondary`: pills, chips, inputs, filter tracks, and code blocks
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
  - **Minimal Grid-Based Control Panel (Zero Separate Backgrounds & Proper Grid System)**:
    - **Top Toolbar (`.control-panel-toolbar`)**: Responsive search input with search shortcut hint badge (`/`) on the left spanning across (`flex: 1`), paired horizontally with live match counter pill, dynamic `Expand All` / `Collapse All` toggle button (`.expand-all-btn`), and `Reset` on the right. 2023 toggle is permanently removed.
    - **Zero Separate Pill Track Backgrounds**: Filter button groups (`.filter-pill-group`) feature NO separate recessed background capsule containers, NO divider lines (`|`), and NO nested background boxes. Inactive buttons are transparent with muted text; active buttons feature a refined, subtle elevated highlight pill.
    - **Proper CSS Grid System (`.control-panel-grid`)**: Symmetrical 3-column CSS Grid (`grid-template-columns: repeat(3, 1fr)`) utilizing 100% of the horizontal space without empty voids:
      - Column 1: `Year` (`All`, `2025`, `2024`, `2023`, `2022`) and `Unit` (`All`, `Unit 1..5`).
      - Column 2: `Repeated` (`All`, `Most Repeated`, `4x`, `3x`, `2x`) and `Type` (`All`, `Theory`, `Numerical`, `Derivation`).
      - Column 3: `Status` (`All`, `Incomplete`, `Completed`, `Starred`, `Later`) and `Marks` (`All`, `2M`, `3M`, `7M/6M`).
    - **Uniform 62px Label Alignment**: All filter labels (`.filter-grid-label`) maintain a uniform 62px width, aligning all button groups across columns.
    - **Responsive Grid Breakpoints**: 3 columns on desktop (`> 1100px`), 2 columns on tablet (`680px - 1100px`), and 1 column on mobile (`< 680px`).
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
- **Question Card Header Layout (Badges Left, Actions Right)**:
  - Every question card positions the question number (e.g. `Q.1 (b)`) and all metadata badges (`Year`, `Unit`, `Type`, `Marks`, `Repeat`) together on the **left side** (`.q-item-left-meta` / `.q-item-badges`).
  - Action controls (`Personal Note` button, `Mark Done` / `Completed` button, and accordion toggle chevron) remain cleanly anchored on the **far right corner** (`.q-item-right-meta` / `.q-item-actions`).
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
- **Distinct Color Year Badges**: All exam years use dedicated pastel color classes across both Question Bank and Checklist cards:
  - 2025: Sage Green (`.badge-year-2025`)
  - 2024: Sky Blue (`.badge-year-2024`)
  - 2023: Lavender Purple (`.badge-year-2023`)
  - 2022: Warm Sand / Gold (`.badge-year-2022`)
- **Card Background Separation (Closed vs Open)**:
  - Closed question cards (`.checklist-card`, `.q-item`) keep their clean background separation (`background-color: var(--card)`, `box-shadow: var(--shadow-sm)`) for distinct browsing.
  - When opened (`.is-open`), the background separation is completely removed (`background-color: transparent`, `box-shadow: none`), allowing the solution to merge seamlessly into the canvas background.
  - Control panels (`.control-panel`) retain their card background, and filter pill groups (`.filter-pill-group`) retain their muted capsule track (`var(--secondary)`).
- **Zero-Clutter Directive & In-Place Answer Expansion**: Eliminate uppercase overlines, redundant explanatory paragraphs, boilerplate slogans, duplicate action buttons, and bulky full-width summary cards. Completion progress is displayed via a precision circular progress indicator (`.checklist-progress-circle` with 42px diameter, edge-aligned SVG ring with gradient stroke, dark-mode luminous OLED glow, optical tabular percentage with subscript `%` unit, and click-to-filter action) positioned directly to the right of the `PYQ Checklist` title alongside the year jump pills (`.checklist-summary-units`). Monospace fonts are strictly prohibited for counters and percentages—standard app typography with tabular numbers is enforced. The entire card is clickable to reveal its complete step-by-step verified solution right there in place without redirecting to the Question Bank. A subtle "Open in Question Bank &rarr;" jump button is located at the bottom of the expanded solution for deep cross-question study when needed.
- **Two-Way Completion Synchronization**: Toggling question completion from either the Question Bank or the Checklist immediately synchronizes `localStorage` (`geotech_completed_questions`), overall completion counters, year-level toolbar progress pills, and unit subhead counters.
- **In-Place Solution Accordion (`toggleChecklistSolution`)**: Clicking any checklist card smoothly toggles its solution container (`chk-sol-*`), rotates the chevron icon (`.chk-chevron`), and sets `.is-open`. Clicking inside the solution text, copying formulas, or clicking the completion button never collapses the card. KaTeX math typesetting is automatically triggered on toggle.
- **Minimal Checklist Toolbar & Zero BG Separation**: The checklist toolbar (`.checklist-toolbar`) has `background: transparent; box-shadow: none; padding: 0;`, eliminating any boxy background separation from the canvas. Status filters (`All`, `Incomplete`, `Done`, `Starred`, `Later`) and Unit filters (`Unit` label + `All`, `Unit 1..5`) use unified `.filter-pill-btn` elements with transparent inactive states and subtle active highlight pills. The search box is minimal, small, and right-aligned (`width: 220px`, `height: 32px`, pill-shaped) with a clear button `✕`.

---

### [RULE 8] Living Rules Maintenance
- Always maintain and update `AGENTS.md` and `RULES.md` as new conventions, data structures, or styling rules are introduced.

---

### [RULE 9] Floating Back-to-Top Action Button
- A floating back-to-top button (`.scroll-to-top-btn`) must be permanently visible in the bottom-right corner (`position: fixed; bottom: 2rem; right: 2rem; z-index: 99999; width: 48px; height: 48px; border-radius: var(--radius-full);`).
- Must use high-contrast theme tokens (`--primary` background, `--primary-foreground` arrow color, `box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28)`) for immediate prominence and zero hardcoded colors.
- Uses an accessible Hugeicons upward arrow stroke icon (`i.hgi-stroke.hgi-arrow-up-01`), smoothly scrolls to top on click (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
- Responsive styling adjusts margins for mobile viewports (`max-width: 640px` adjusts offset to `1.25rem`).

---

### [RULE 10] Smart Auto-Hide Header Navbar on Scroll
- The sticky header navbar (`.header`) automatically translates off-screen (`transform: translateY(-100%)`, `.header.header-hidden`) on downward scroll, and smoothly reveals (`transform: translateY(0)`) on upward scroll via hardware-accelerated cubic-bezier transitions (`will-change: transform`).
- Near top of page (`scrollY <= 64px`), the header is guaranteed visible and protected against trackpad rubber-band bounce.
- Switching views via `switchPageView()` or clicking back-to-top immediately resets and surfaces the navbar.
- The header brand displays the clean title without redundant course code or colored brand badges.

---

### [RULE 11] Permanent Inclusion of All 4 Exam Papers (2023 Toggle Removed)
- **Complete 4-Paper Intelligence**: All 4 verified examination papers (2025, 2024, 2023, 2022 — totaling 106 verified questions) are permanently active across all views and computations.
- **Toggle Removed for Ultimate Minimalism**: The separate 2023 toggle switch has been completely removed from the UI. Users filter by year naturally via the standard `Year` filter pill buttons (`All`, `2025`, `2024`, `2023`, `2022`).
- **Clean, Clutter-Free Control Toolbar**: The search toolbar hosts solely the full-width responsive search box and context-sensitive `Reset` action.

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
- **Timetable Policy & Local Storage Isolation**: The examination timetable (`timetable.html`) is public and git-tracked, while heavy PDFs and OCR scratches remain gitignored. Default public repository schedule contains only the 3 regular syllabus subjects (Geo-2, RCC, DHS). User modifications, additions, and deletions persist in client-side localStorage (`civil_exam_timetable_custom_v1`) without collision. Local host environments automatically preserve the user's 7-paper backlog schedule, with quick preset toggles in the Edit Timetable modal.
- **Concluded / Done Examination Indicator (Muted Green)**: Concluded papers adopt a calm muted green palette (`--pastel-done-bg`, `--pastel-done-border`, `--pastel-done-foreground`, and tag `✓ Done`) across the calendar grid, table rows, and timeline cards. Upcoming countdowns automatically skip completed papers.
- **Master CLI Generation Engine**: `python3 generate_dashboard.py` builds the active default subject (`geotech-2`) into `index.html` and `geotech_pyq_analysis.html`. Passing `<subject_id>` builds that subject, `--list` inspects the registry, and `--new <id> "<name>" "<code>"` scaffolds a new subject module.
- **Root Proxy Immutability**: Root `compile_data.py` and `formula_showcase.py` proxy directly to `subjects/geotech-2/` ensuring 100% backward compatibility for all scripts and agents.

---

### [RULE 16] Personal Notes, Custom Answers & Study Scratchpad Engine
- **In-Card Pen Action Button (`.note-action-btn`)**: Question cards in both the Question Bank (`.q-item-actions`) and PYQ Checklist (`.checklist-card-actions`) must include an accessible pen icon button to add, edit, or toggle personal notes/answers. Questions with saved notes must display a visual dot indicator (`.note-indicator-dot`) and subtle active styling.
- **In-Card Solution Toggle Switch (`.sol-view-switch-row`)**: The solution block of question cards features a capsule toggle switch allowing seamless switching between `Verified Solution` and `My Answer ✍️` directly on the card.
  - **Zero-Clutter Visibility Rule**: When no personal answer is provided (`!hasNote`), all 3 elements in the switch row (`Verified Solution` tab, `My Answer` tab, and `Add My Answer` button) must be strictly **hidden** (`display: none`), displaying the verified solution cleanly and directly.
  - Only when a personal answer is provided / saved does `.sol-view-switch-row` appear (`display: flex`), allowing students to toggle between solutions and edit their notes.
  - Deleting a personal answer automatically hides all 3 elements and restores the direct verified solution view.
  - This toggle must remain strictly isolated to the specific card without affecting any other question.
- **Full Markdown & Zero Wall-of-Text Formatting**: Custom answers must be rendered via `renderUserAnswerHtml()` supporting full Markdown (headings `#..####`, pipe tables `|...|`, numbered lists `1.` and escaped `1\.`, bullet lists, `Note:` callout boxes, and `Example:` micro-tags) with zero raw markdown artifacts.
- **Default Tab Display**: When a question has a saved personal answer ("My Answer"), it must open and display "My Answer" by default instead of the verified solution.
- **Notes & Custom Answers Navigation Policy**:
  - The sticky top header and mobile bottom navigation retain the clean, minimal 4 primary destinations: `Questions`, `Checklist`, `Formulas`, and `Timetable` (using minimal 1-word titles, pure numeric badges such as `71` and `47/71` without redundant word suffixes, and the dedicated `hgi-file-question-mark` icon).
  - The standalone `Notes` navigation tab and count badge are excluded from both desktop and mobile navigation bars to keep the interface uncluttered. Personal answers and notes remain accessible directly in-card via the pen button (`.note-action-btn`) and solution tab switch.
- **Multi-Tier Persistence Guarantee ("Never Lose Notes")**:
  - Primary instant persistence in `localStorage` (`<prefix>_user_notes`, `<prefix>_general_notes`).
  - Asynchronous background synchronization to disk via `POST /api/progress` (`user_progress.json`).
  - Embedded data bootstrap in generated HTML (`EMBEDDED_NOTES`, `EMBEDDED_GEN_NOTES`).
  - JSON Backup export (`exportNotesJSON`) and import (`triggerImportNotes`), plus clipboard copy utilities on the Notes page.

---

## 13. KaTeX Mathematical Typography & Numerical Parsing Standards

- **Zero Red Errors Guarantee**: Equations must never render in raw red text (`.katex-error`).
- **Negative Exponents**: Always format negative exponents with braces as `10^{-3}` or `x^{-n}`. Never output `^-3` or corrupted `⁻^3`.
- **Entity Sanitization**: Replace all HTML entities (`&lt;` -> `<`, `&gt;` -> `>`, `&amp;` -> `\&`, `&nbsp;` -> ` `, `&mdash;` -> `\text{ --- }`).
- **Percent Escaping**: Literal `%` in math mode must be escaped as `\%` to prevent line comment truncation.
- **Client Pre-Processing**: Always ensure `renderMathInElement` runs with `preProcess` so all dynamic client math blocks are pre-sanitized before parsing (including escaped underscores like `\_` converted to valid subscripts `_`).
- **Personal Answers & Notes Math & Table Rendering**:
  - All LaTeX display blocks (`$$...$$`, `\\[...\\\]`, `\[...\]`) and inline formulas (`$...$`, `\\(...\\)`, `\(...\)`) in user answers are synchronously parsed into `.sol-math-block` and inline KaTeX spans via `katex.renderToString`.
  - Markdown tables in personal answers enforce `table-layout: fixed;` with balanced, proportional column widths (`width: (100 / colCount)%`), never restricting the first column to arbitrary widths (e.g. `230px`) or forcing bold font weights.

---

## 14. Star & Mark-for-Later Question Tracking Engine

- **Pure Icon-Only Buttons**: Star and Later controls must never contain text labels ("notext just icon"), only clean SVG glyphs.
- **Star Icon (`.star-action-btn`)**: 5-point star polygon. When active, lights up with warm amber gold (`var(--pastel-amber-bg)` / `var(--pastel-amber-foreground)`).
- **Later Icon (`.later-action-btn`)**: Clock icon. When active, highlights with soft lavender (`var(--pastel-lavender-bg)` / `var(--pastel-lavender-foreground)`).
- **Strict Exclusion from Total Count (MANDATORY)**: Questions marked as "Later" MUST NOT be counted in the total questions count or completion progress denominator across Question Bank metrics, PYQ Checklist metrics, navbar badges, and syllabus breakdown counters.
- **Visual Dimming (`.is-later`)**: Deferred question cards adopt a subtle `0.65` opacity, restoring to `1.0` on hover.
- **Segmented Status Filters**: `Starred` and `Later` filters are added to status filter pills across Question Bank and PYQ Checklist. Selecting `Incomplete` automatically excludes deferred items.
- **Multi-Tier Persistence**: Saved to `localStorage` (`<prefix>_starred_questions`, `<prefix>_later_questions`), synced to `user_progress.json`, and bootstrap seeded during dashboard generation.
- **Client Pre-Processing**: Always ensure `renderMathInElement` runs with `preProcess` so all dynamic client math blocks are pre-sanitized before parsing (including escaped underscores like `\_` converted to valid subscripts `_`).
- **Personal Answers & Notes Math & Table Rendering**:
  - All LaTeX display blocks (`$$...$$`, `\\[...\\\]`, `\[...\]`) and inline formulas (`$...$`, `\\(...\\)`, `\(...\)`) in user answers are synchronously parsed into `.sol-math-block` and inline KaTeX spans via `katex.renderToString`.
  - Markdown tables in personal answers enforce `table-layout: fixed;` with balanced, proportional column widths (`width: (100 / colCount)%`), never restricting the first column to arbitrary widths (e.g. `230px`) or forcing bold font weights.

---

## 15. Minimal Favicon & Touch Icon Standard

- **Minimalist Brandmark**: Obsidian/zinc squircle (`#09090b` canvas) with subtle border (`rgba(255, 255, 255, 0.15)`) enclosing a crisp geometric "E" monogram (`#fcfcfd`).
- **Mathematical Pixel Alignment**: 32×32 canvas aligned to even integer coordinates, scaling to 16×16 with exact 1-to-1 pixel sharpness and zero subpixel blur.
- **Universal Multi-Tier Delivery**:
  - Embedded inline URL-safe SVG data URI in `<link rel="icon">` without literal `</style>` tags for instantaneous local `file://` offline rendering.
  - Root `favicon.svg` for infinite retina scalability and dark/light system theme support.
  - Root `favicon.ico` (16×16, 32×32, 48×48) for legacy/Windows browsers.
  - Root `apple-touch-icon.png` (180×180) for iOS homescreen and Safari touch shortcuts.
- **Generator Enforcement**: Always declare the full favicon stack in both `generate_dashboard.py` and `tools/timetable/build_timetable.py`.

---

## 16. Formula Parameter Breakdown & Clean Typography Standard (Zero Separate Bg & Font)

- **Parameter Breakdown Clean Architecture**:
  - In formula cards (`#view-formulas`), parameter items must **NEVER** be wrapped in individual colored pill backgrounds (`--math-param-pill-bg`) or nested unit boxes (`--card`).
  - **No Monospace Font Clutter**: Parameter symbols and units must **NOT** force monospace font (`var(--font-family-mono)`). KaTeX renders the mathematical symbols with standard math typography; descriptions and units inherit the clean, natural application sans-serif typography.
  - **Structured 3-Column Alignment (`.formula-param-grid`)**: Parameters format as clean, seamless typographic rows using CSS Grid:
    - **Container**: `display: grid; grid-template-columns: auto 1fr auto; column-gap: 0.85rem; row-gap: 0.45rem; align-items: baseline;`
    - **Row Wrapper**: `.formula-param-row { display: contents; }` so that all rows across a card align into 3 synchronized columns.
    - **Column 1 (`.param-sym`)**: Bold symbol, rendered via KaTeX (`$p.sym$`), crisp and left-aligned.
    - **Column 2 (`.param-desc`)**: High-contrast, highly readable description (`color: var(--foreground); font-size: 0.875rem; line-height: 1.5;`).
    - **Column 3 (`.param-unit`)**: Clean, subtle SI unit (`color: var(--muted-foreground); font-size: 0.8125rem; font-weight: 500; justify-self: end; text-align: right; background: none; border-radius: 0; padding: 0;`).
  - **Mobile Fluidity (`@media (max-width: 540px)`)**: Switches smoothly to a flexible wrapping flex layout (`.param-sym { min-width: 44px; }`, `.param-desc { flex: 1 1 180px; }`, `.param-unit { margin-left: auto; }`).
- **Exam Insight Callout Removal**:
  - The redundant `.formula-exam-notes` ("Exam Insight") callout box at the bottom of formula cards is removed to eliminate visual clutter and keep cards focused strictly on governing equations and parameter definitions.
  - In the formula table view, the 4th column displays the clean parameter list rather than repetitive note blocks.

---

## 17. Master Formulas & Governing Equations Control Panel (Minimal & Clean Standard)

- **Zero Heading Clutter**:
  - The Formulas view (`#view-formulas`) completely eliminates the top `.page-header-row`, removing the redundant overline (`Interactive Mathematical Reference...`), giant H1 headline, and dense paragraph description for maximum vertical workspace.
- **Minimal Formula Control Bar (`.formula-control-bar`)**:
  - The outer bar eliminates arbitrary background separation (`background: transparent !important; box-shadow: none !important; border: none !important; padding: 0 !important; margin-bottom: 1.5rem;`), sitting seamlessly on the canvas.
  - Background separation is strictly maintained on:
    1. **The Unit Div (`.formula-unit-wrapper`)**: Tactile segmented capsule (`background-color: var(--secondary); border-radius: var(--radius-full); padding: 2.5px 3px 2.5px 0.75rem;`) housing the `Unit` label and all unit filter buttons in one unified pill track.
    2. **The Search Input**: Rounded pill input (`.search-input` with `background-color: var(--input-bg); border-radius: var(--radius-full);`).
- **Three-Part Symmetrical Layout**:
  - **Left - Unit Switcher**: Clean, non-wrapping uppercase label (`Unit`, `var(--font-size-overline)`, `var(--muted-foreground)`) followed by tactile unit pills (`All`, `Unit 1..5`).
  - **Left - Live Match Counter**: Minimal match counter pill (`.match-counter-pill`) displaying `21 formulas` or `X of 21 matched`, paired with a smart `Reset` button that appears when filters or queries are active.
  - **Right - Minimal Search Input**: Moved cleanly to the right side of the column with minimal placeholder (`Search formulas...`), search icon, clear button (`✕`), and zero `f` shortcut badge clutter.
- **Cards by Default**:
  - Cards layout is kept permanently by default (`#formulaCardsGrid`), eliminating the Cards/Table switch toggle buttons and layout switcher clutter.
- **Zero Redundant Status Row**:
  - Eliminates the duplicate all-caps summary row (`SHOWING 4 MASTER ENGINEERING FORMULATIONS`), saving ~180px-200px of vertical space so equations and cards appear immediately at the top of the viewport.

---

### [RULE 18] Unified Hugeicons Icon System Standard
- **Design Standard**: The application exclusively uses **Hugeicons** (Stroke-Rounded style) across desktop and mobile views.
- **CDN with Offline Local Vendored Fallback**:
  - All pages load Hugeicons via:
    ```html
    <link rel="stylesheet" href="https://use.hugeicons.com/font/icons.css" onerror="this.onerror=null;this.href='vendor/hugeicons/icons.css'">
    <link rel="stylesheet" href="vendor/hugeicons/icons.css">
    ```
  - Local assets in `vendor/hugeicons/` ensure zero-latency rendering when opened offline via `file://`.
- **Sizing Tokens**:
  - Base `.icon`: `1.25rem` (20px)
  - `.icon-xs`: `1rem` (16px)
  - `.icon-sm`: `1.125rem` (18px)
  - `.icon-md`: `1.375rem` (22px)
  - `.icon-lg`: `1.75rem` (28px)
  - Mobile bottom nav (`.mobile-nav-icon`): `22px`
  - Floating back-to-top (`.scroll-to-top-btn i`): `24px`
- **Zero Sparkle Mandate**: Never use AI sparkle icons or multi-point stars (`hgi-stars`, `hgi-sparkle`). Questions are starred strictly using standard 5-point star (`hgi-star`).

---

### [RULE 19] Layout ID Shared Sliding Pill Engine & Smooth Div Transitions
- **Layout ID Shared Pill Standard**:
  - In all switches, filters, tab bars, and segmented controls (`.filter-pill-group`, `.nav-links`, `.sol-view-pills`, `.notes-unit-pills`, `.mobile-bottom-nav`, `.filter-tabs-minimal`, `.view-switchers-minimal`), the active state must NEVER snap abruptly between buttons.
  - A single dedicated `.layout-pill-indicator` element sits inside the group container and physically glides, expands, and contracts across options using sub-pixel accurate translations (`transform: translate3d(x, y, 0)`) and dimensions (`width`, `height`).
  - **Motion Dynamics & Easing**:
    - Uses Apple / Emil Kowalski's custom cubic-bezier spring-like curve: `cubic-bezier(0.16, 1, 0.3, 1)`.
    - Timing: `0.28s` duration, ensuring snappy, fluid, and interruptible motion without perceptual lag.
  - **Single Background Integrity**:
    - When `.layout-pill-indicator` is active, the individual button itself (`.filter-pill-btn.active`, `.nav-link-btn.active`, `.sol-view-pill.active`, `.view-pill.active`, `.tab-pill.active`) has `background: transparent !important; box-shadow: none !important;`.
    - The moving indicator IS the active background. Buttons sit on `position: relative; z-index: 2;` with smooth text color transitions (`transition: color 0.18s ease`).
  - **Dynamic Color Morphing (Timetable Filter Tabs)**:
    - In `.filter-tabs-minimal`, the indicator dynamically adapts its background color (`#205c36` for Regular, `#9a4318` for Backlog, neutral for All) with `transition: background-color 0.28s cubic-bezier(0.16, 1, 0.3, 1)` so the pill glides and morphs its hue seamlessly.
- **Smooth Div & Content Pane Transitions (Zero Abrupt Display Swaps)**:
  - Whenever view containers, content panes, or solution tabs are shifted or toggled, elements must transition smoothly rather than snapping:
    - App page views (`.app-page-view.active`): `@keyframes appPageViewEnter { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }`
    - Solution panes (`.solution-pane`): `@keyframes solPaneFadeIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }`
    - Question accordions (`.checklist-solution-content.open`, `.q-solution-content.open`): `@keyframes chkSolSlideOpen { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }`
    - Timetable view switchers (`#calendar-view, #table-view, #timeline-view`): `@keyframes timetableViewEnter { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }`





