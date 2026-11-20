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
- **Final Answer & Safety Verification Standards (Muted Minimal Green System - MANDATORY)**:
  - **Minimal Muted Green Palette**: Concluding statements, final calculated answers, and safety verification checks must NEVER look like plain monotone text. They use a delicate, minimal muted sage/emerald design token system (`--ans-muted-bg`, `--ans-muted-border`, `--ans-pill-bg`, `--ans-pill-fg`, `--ans-tag-bg`):
    - **Light Mode**: Warm sage paper wash (`rgba(30, 94, 58, 0.05)` bg, `#eaf4ed` pill, `#1e5e3a` text).
    - **Dark Mode**: Translucent obsidian emerald (`rgba(16, 185, 129, 0.07)` bg, `rgba(30, 94, 58, 0.32)` pill, `#86efac` text).
  - **Safety / Verification Badges (`.sol-badge-safe`)**:
    - Statements like `(Safe against Bligh creep)`, `[Safe & watertight]`, `(Safe)`, `(OK)`, `(Safe in Punching Shear)`, etc. render as chic, minimal muted green status badges: `<span class="sol-badge-safe"><span class="sol-badge-check">✓</span> Safe against Bligh creep</span>`.
    - Automatically extracted from both plain HTML text and LaTeX formulas (`\quad (\text{Safe})`).
  - **Final Answer & Summary Tags (`.sol-ans-tag`)**:
    - Prefixes like `Final Answer:`, `Ans:`, `Answer:`, and `Design Summary:` format into a crisp micro-badge: `<span class="sol-ans-tag"><span class="sol-ans-tag-dot"></span>Ans</span>`.
  - **Conclusive List Items & Rows (`.sol-item-final`)**:
    - List items (`<li>`) and numerical calculation rows (`.sol-item-row`) that culminate in a final answer or safety check receive `.sol-item-final`: a soft muted green background tint, a subtle 2px muted green accent line on the left, muted green bullets, and highlighted strong text.
- **Zero Tilted / Italic Text in Answers (MANDATORY)**:
  - **NEVER** render solution points, sub-item labels, notes, or explanations in tilted/italic font (`font-style: italic`).
  - **ALWAYS** render sub-labels (e.g. `<em>Applied Loads:</em>`, `<em>Critical Design Cases:</em>`, `<em>Structural Behavior:</em>`, `<em>Soil Type:</em>`) strictly upright (`font-style: normal !important`), with clean semi-bold typographic contrast (`font-weight: 600`) and high-contrast foreground color (`color: hsl(var(--foreground))`).
  - KaTeX mathematical variables and symbols typeset independently remain unaffected.

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
- **Dynamic Question Card Background Separation (Card when Closed, Seamless Canvas when Opened)**:
  - **Closed Question Cards (`.checklist-card`, `.q-item`)**: Maintain clean background separation (`background-color: var(--card)`, `box-shadow: var(--shadow-sm)`), sitting distinctly on the canvas for effortless browsing.
  - **Opened Question Cards (`.checklist-card.is-open`, `.q-item.is-open`)**: Background separation is completely removed (`background-color: transparent`, `box-shadow: none`), allowing the expanded answer and typography to merge seamlessly into the canvas background without giant gray box containers.
- **Control Panel & Filter Capsule Tracks**:
  - The control panel bar (`.control-panel`) retains its elevated surface background (`var(--card)`).
  - Filter button groups (`.filter-pill-group`) retain their muted capsule background track (`var(--secondary)`), providing clear tactile grouping for all units and filters.
- **Distinct Color Year Badges**:
  - All year badges use dedicated pastel color classes across both Question Bank and Checklist cards:
    - 2025: Sage Green (`.badge-year-2025`)
    - 2024: Sky Blue (`.badge-year-2024`)
    - 2023: Lavender Purple (`.badge-year-2023`)
    - 2022: Warm Sand / Gold (`.badge-year-2022`)
- **No 1px Structural Borders**: Structure containers, cards, and table headers using tonal background shifts (`--background`, `--card`, `--secondary`, `--muted`) rather than harsh borders.
- **KaTeX Mathematical Fraction Line & Border Immunity (Zero Universal `border: none !important` Anti-pattern)**:
  - KaTeX mathematical rendering relies on CSS borders for fraction division lines (`.mfrac .frac-line`), square roots (`.sqrt-line`), overlines, underlines, and rules.
  - **NEVER** apply `border: none !important;` to universal selectors (`*`, `*::before`, `*::after`). Doing so strips the division vinculum line from fractions (`\frac{a}{b}`), causing numerators and denominators to run together without a dividing bar.
  - Target form control resets specifically (`button, input, select, textarea { border: none; outline: none; }`).
  - Enforce `.katex .mfrac .frac-line { border-bottom-style: solid !important; border-bottom-width: max(1.2px, 0.05em) !important; border-bottom-color: currentColor !important; min-height: 1.2px !important; }` across all stylesheets to guarantee crisp, high-contrast, perfectly visible fraction division lines across all screen resolutions, pixel ratios, and dark/light modes.
- **Formula Robustness & Anti-Regression Testing (Zero Red KaTeX Errors - MANDATORY)**:
  - **Zero Raw HTML Entities in Math**: Math strings must never leak raw HTML entities (`&beta;`, `&phi;`, `&gamma;`, `&radic;`, `&sup2;`, etc.) or HTML formatting (`<sub>`, `<sup>`, `<b>`) into KaTeX. All Greek letters, square roots (`\sqrt{...}`), exponents, and operators must be valid LaTeX or sanitized via `cleanLatexString()`.
  - **Percent Sign & Ampersand Immunity**: Literal `%` in math mode acts as a LaTeX comment and must be escaped (`\%`). Bare `&` outside tabular/matrix environments causes syntax errors and must be escaped (`\&`).
  - **Automated Anti-Regression Verification Suite**: Every build runs `npm run test:formulas` (`node scripts/verify-formulas.js` and `npx tsx scripts/verify-formulas.ts`) which scans all 4,600+ mathematical expressions across `src/data/*.json` and `subjects/` to detect parse faults, unescaped characters, or red error output before deployment. Build fails immediately if any formula error occurs.
- **Design Tokens**: NEVER hardcode hex codes or RGB strings inside components or markup. Always reference semantic CSS variables (`var(--background)`, `var(--foreground)`, `var(--card)`, `var(--secondary)`).
- **Theme Support**: Ensure all colors work seamlessly across dark mode (`data-theme="dark"`) and light mode (`data-theme="light"`). Both Timetable and PYQ Master share the unified `geotech_theme` localStorage key.
- **No Sparkle Icons**: Never use sparkle icons, generative AI stars, or multi-point sparkle glyphs anywhere in the UI.

---

## 4. Single Source of Truth & Next.js Data Pipeline

- The core analytical data pipeline compiles and exports strongly-typed JSON for Next.js via:
  ```bash
  npm run export:data
  ```
- **Files generated in `src/data/`**:
  - `questions.json` (Geotech-2 verified questions)
  - `canonical.json` (Geotech-2 canonical topic clusters)
  - `formulas.json` (Geotech-2 formulas)
  - `rcc_*.json`, `dhs_*.json` (Subject-specific datasets)
  - `timetable.json` (Timetable schedules)
  - `subjects.json` (Registered ready subjects)
- **Question Bank Engine Directives**:
  - **Zero Heading Clutter**: The Question Bank view starts immediately with the space-efficient Control Panel, removing unnecessary top headings and subheadings for maximum vertical workspace.
  - **Minimal Grid-Based Control Panel (Zero Separate Backgrounds & Proper Grid System)**:
    - **Top Utility & Search Toolbar (`.control-panel-toolbar`)**: Clean, responsive search input spanning across (`flex: 1`) with search shortcut hint badge (`/`) and clear `✕` button, paired with the live match counter pill, dynamic `Expand All` / `Collapse All` toggle button (`.expand-all-btn`), and the `Reset` action on the right.
    - **Zero Separate Pill Track Backgrounds (Pure Minimal Flow)**: Filter button groups (`.filter-pill-group`) feature NO separate recessed background capsule containers (`var(--secondary)` track removed), NO divider lines (`|`), and NO nested background boxes. Inactive buttons are transparent with muted text, while the active filter button features a subtle, refined background highlight pill (`var(--secondary)` in light mode, `#27272a` in dark mode).
    - **Proper CSS Grid System (`.control-panel-grid`)**: All 6 filter dimensions are laid out in a symmetrical 3-column CSS Grid (`grid-template-columns: repeat(3, 1fr)`) that utilizes 100% of the horizontal workspace without empty voids:
      - **Column 1 (Scope & Syllabus)**: `Year` (`All`, `2025`, `2024`, `2023`, `2022`) and `Unit` (`All`, `Unit 1..5`).
      - **Column 2 (Intelligence & Format)**: `Repeated` (`All`, `Most Repeated`, `4x`, `3x`, `2x`) and `Type` (`All`, `Theory`, `Numerical`, `Derivation`).
      - **Column 3 (Workflow & Priority)**: `Status` (`All`, `Incomplete`, `Completed`, `Starred`, `Later`) and `Marks` (`All`, `2M`, `3M`, `7M/6M`).
    - **Uniform 62px Label Alignment**: All filter labels (`.filter-grid-label`) maintain a uniform 62px width, ensuring button groups in every column align down to the pixel across rows.
    - **2023 Toggle Removed**: All 4 examination years (2025, 2024, 2023, 2022) are permanently included and active in the Year filter without any separate toggle switch widget.
    - **Responsive Grid Breakpoints**: 3 columns on desktop (`> 1100px`), 2 columns on tablet (`680px - 1100px`), and 1 column on mobile (`< 680px`) with smooth horizontal momentum scrolling.
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
  - **Question Card Header Layout (Checkbox & Badges Left, Actions Right, Question Number beside Text)**: Every question card anchors the completion checkmark box at the leading left position immediately before the `Year` badge and metadata badges (`Year`, `Unit`, `Type`, `Marks`, `Repeat`) as `.q-item-left-meta` / `.q-item-badges`, while the question number (e.g. `Q.3 (a)`) is positioned directly beside the question headline text rather than in the badge row. Action controls (`Star`, `Save for Later`, `Personal Note`) remain cleanly anchored on the **far right corner** as a dedicated quick action island (`.action-island`). To provide clear, intuitive UX without cluttering the header, the isolated top-right chevron has been removed, and a subtle "View Answer" / "Hide Answer" affordance with a mini chevron sits at the bottom of the question statement. The completion checkmark box maintains a clean, light surface (`--checkbox-bg`) and crisp visible border (`--checkbox-border`), avoiding dark or recessed fills in both light and dark modes.
  - **Clean & Un-Cardified Editorial Solutions (Zero Sub-Card Boxes)**: Individual solution points, assumptions, and steps must NEVER be wrapped in nested card containers (`.sol-item-card`), background fills (`--solution-card-bg`), box shadows, or square badge boxes (`.sol-item-badge`). Instead, solutions format as clean, elegant typographic rows (`.sol-item-row`) with natural numbers (`1.`, `2.`), bold concept titles, comfortable line-height (`1.75`), and dedicated lines for examples (`Example: ...`). Multi-line text wraps cleanly under the text margin via flex alignment, preserving effortless readability and zero wall-of-text fatigue.
  - **Verbatim PYQ Question as Card Headline & Zero Topic Clutter**: Every question card presents the actual verbatim question statement asked in the PYQ paper (`item.question`) cleanly as its primary heading (`.q-item-title`) without bracket `[]` marks and without any intermediate topic overlines (`Topic:` removed from question cards). Metadata chips clearly display Exam Year, Unit, Question Type, Marks (`2M`, `3M`, `7M` as a normal `.badge-subtle` badge with no mono font and no bold), and Repeat Count (`4x`, `3x`, or `2x`). Dedicated Marks filter and search support allow filtering specifically by marks.
  - **Personal Notes & Custom Answers Engine (Markdown Tables & KaTeX Immunity)**:
    - **Balanced Comparison Tables (`table-layout: fixed`)**: Markdown tables in user personal answers dynamically assign proportional column widths (`width: (100 / colCount)%`) and enforce `table-layout: fixed;` with word-wrap protection (`word-wrap: break-word`, `overflow-wrap: break-word`). NEVER clamp the first column to an arbitrary width (e.g. `width: 230px`) and NEVER force bold weight (`font-weight: 600`) onto the first cell (`td:first-child`), ensuring two-column comparisons (such as Shallow vs Deep Foundations) span the full width symmetrically without lopsided void space.
    - **KaTeX Formula Rendering & Delimiter Immunity**: User solutions support all standard mathematical notation: LaTeX display blocks (`$$...$$`, `\\[...\\\]`, `\[...\]`) and inline formulas (`$...$`, `\\(...\\)`, `\(...\)`). Display math blocks are pre-extracted prior to line splitting to protect equations from being fractured across paragraphs, escaped underscores (e.g. `BN\_\gamma`) are automatically sanitized to valid subscript syntax (`BN_\gamma`), and math is synchronously rendered into `.sol-math-block` containers using KaTeX (`katex.renderToString`).
- **Data inputs**:
  - `canonical_data.json` (59 clean, deduplicated core topics)
  - `compile_data.py` (106 verified raw questions across 4 exam years: 2025, 2024, 2023, 2022)
- **Master Formulas & Governing Equations Engine Directives**:
  - **Zero Heading Clutter**: Removes redundant overlines, giant page titles, and dense paragraph descriptions. The view starts immediately with the minimal `.formula-control-bar`.
  - **Minimal Three-Part Control Bar (Zero Outer Background Separation)**:
    - Eliminates outer card background (`background: transparent !important; box-shadow: none !important; border: none !important; padding: 0 !important;`).
    - Background separation is kept strictly in the unit div (`.formula-unit-wrapper` with `var(--secondary)`) and on the search input (`var(--input-bg)`).
    - **Unit Switcher (Left)**: Uppercase `Unit` label with tactile unit pills (`All`, `Unit 1..5`).
    - **Formula Counter (Left)**: Live match counter pill (`21 formulas` or `X of 21 matched`) with reactive `Reset` button.
    - **Minimal Search Input (Right)**: Positioned on the right side of the column with minimal placeholder (`Search formulas...`), clear button (`✕`), and no `f` badge.
  - **Cards Layout by Default**: Permanent cards layout with Cards/Table switch toggle buttons removed.
  - **Zero Redundant Status Row**: Completely eliminates redundant all-caps summary bars (`SHOWING 4 MASTER ENGINEERING FORMULATIONS`), saving ~180px-200px of vertical viewport space so mathematical formulas appear immediately.
- **PYQ Checklist Engine Directives (Year-wise, then Unit-wise)**:
  - Replaces the legacy static syllabus breakdown table with an interactive, year-wise and unit-wise PYQ checklist across all 106 verified questions (2025: 28 Qs, 2024: 25 Qs, 2023: 28 Qs, 2022: 25 Qs, covering Units 1 to 5 within each exam paper).
  - **Distinct Color Year Badges**: Each exam year has its own unique, accessible pastel color token: 2025 (Sage Green `.badge-year-2025`), 2024 (Sky Blue `.badge-year-2024`), 2023 (Lavender Purple `.badge-year-2023`), 2022 (Warm Sand `.badge-year-2022`) across both Question Bank and Checklist cards.
  - **Minimal, Zero-Clutter Architecture & In-Place Answer Expansion**: Free of explanatory subtitles, uppercase overlines, redundant "View in Bank" buttons, and verbose labels. The separate bulky summary card below the title is replaced by a minimal inline header action row (`.checklist-header-right`) located directly to the right of the `PYQ Checklist` title (`.checklist-header-row`), featuring a precision circular progress indicator (`.checklist-progress-circle` with 42px diameter, edge-aligned SVG ring with gradient stroke, dark-mode luminous OLED glow, optical tabular percentage with subscript `%` unit, and click-to-filter action) alongside the year jump pills (`.checklist-summary-units`). No monospaced fonts (`font-family: var(--font-family-mono)`) are used for stats or pill counters; all counts and percentages use standard clean app typography with `font-variant-numeric: tabular-nums`. Entire question cards are clickable to expand and view the verified solution right there in place without redirecting to the Question Bank. An unobtrusive "Open in Question Bank &rarr;" jump button is provided at the bottom of the expanded solution for deep cross-question study when needed.
  - **Two-Way Real-Time Synchronization**: Toggling a question's completion state in either the Checklist or Question Bank instantly synchronizes `localStorage` (`geotech_completed_questions`), overall completion counters, year-level toolbar progress pills, and unit-level subhead counters.
  - **In-Place Accordion Engine (`toggleChecklistSolution`, `toggleSolution`)**: Clicking anywhere on an expanded question card or answer body smoothly collapses/closes the question (while selecting text to copy, clicking action buttons, checkboxes, tab switchers, or the note editor remains non-collapsing). Clicking a closed card expands its solution and sets `.is-open`. KaTeX math typesetting is automatically triggered on toggle.
  - **Checklist Controls & Filtering (Full 6-Dimension Control Panel & Live Question Counters)**: Features total completion progress, quick year-jump pills (`2025`, `2024`, `2023`, `2022`), and the complete 6-dimension `.control-panel`:
    - **Top Utility & Search Toolbar (`.control-panel-toolbar`)**: Sleek, compact search input (`.search-box-wrapper`, 260px) with `/` shortcut hint and `✕` clear button, paired with the live match counter pill (`.match-counter-pill`: e.g. `106 questions` or `24 of 106 questions`), dynamic `Expand All` / `Collapse All` toggle button (`.expand-all-btn`), and instant `Reset` button.
    - **Proper CSS Grid System (`.control-panel-grid`)**: Symmetrical 3-column grid containing all 6 filter dimensions with clean, uncluttered filter pill buttons:
      - **Column 1**: `Year` (`All`, `2025`, `2024`, `2023`, `2022`) and `Unit` (`All`, `Unit 1..5`).
      - **Column 2**: `Repeated` (`All`, `Most Repeated`, `4x`, `3x`, `2x`) and `Type` (`All`, `Theory`, `Numerical`, `Derivation`).
      - **Column 3**: `Status` (`All`, `Incomplete`, `Completed`, `Starred`, `Later`) and `Marks` (`All`, `2M`, `3M`, `7M / 6M`).
    - **Reactive Match Counter & Zero-Match Empty State**: Both Question Bank and Checklist display live match counts (`X of Y questions`) and display `.empty-results` with a one-click Reset button when active filter combinations yield 0 matches.
    - **Local Persistence**: Checklist filter preferences (`geotech_checklist_filters`) persist in `localStorage` across page reloads.
- **Rule**: Whenever modifying layout, tables, styles, or components, ALWAYS make changes in the Next.js components (`src/components/`, `src/app/`) or source data (`subjects/`, `src/data/`), and verify the build with `npm run build && npx tsc --noEmit`.

---

## 5. Floating Back-to-Top Navigation

- A persistent, high-contrast floating back-to-top button (`.scroll-to-top-btn`) is fixed and permanently visible at the bottom-right corner of all views (`bottom: 2rem; right: 2rem; z-index: 99999; width: 48px; height: 48px; border-radius: var(--radius-full);`).
- Features a clean Hugeicons arrow-up stroke icon (`hgi-stroke hgi-arrow-up-01`), semantic design token styling (`--primary`, `--primary-foreground`, `box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28)`), and smooth scrolling behavior (`window.scrollTo({ top: 0, behavior: 'smooth' })`).
- Always visible across desktop and mobile (`opacity: 0.95`, hover elevation to `scale(1.05)`).

---

## 6. Smart Auto-Hide Header Navbar on Scroll

- **Behavior**: The sticky header navbar (`.header`) automatically translates off-screen (`transform: translateY(-100%)`, `header-hidden`) on downward scroll, and smoothly glides back into view (`transform: translateY(0)`) on upward scroll.
- **Top Threshold Immunity**: The header is permanently visible when `scrollY <= 64px` (top of page or during elastic rubber-banding bounce).
- **Navigation & Jump Integration**: Switching view tabs (`switchPageView`), clicking the floating back-to-top button, or jumping to top immediately resets and displays the navbar (`header.classList.remove('header-hidden')`).
- **Clean Brand Header & Minimal Navigation Tabs**:
  - The navbar presents the clean course title (`.brand-title`) without redundant course code or colored brand badges.
  - **Minimal 1-Word Navigation Titles**: All primary navigation destinations use crisp, balanced 1-word titles: `Questions`, `Checklist`, `Formulas`, and `Timetable` (replacing verbose labels like `Question Bank` and `Unit Checklist`).
  - **Zero-Suffix Pure Numeric Badges**: Badges display pure numbers with tabular figures (`71` total questions, `47/71` checklist progress ratio) eliminating redundant word noise like `PYQs` and `Done`.
  - **Dedicated Question Icon**: The Questions navigation tab uses the crisp, universally recognizable `hgi-help-circle` icon (circle with centered `?`) in place of the generic textbook icon (`hgi-book-open-01`), ensuring sharp 16px rendering with zero stroke collisions.
  - **Tonal Badge Integration**: Inactive navigation badges use `var(--secondary)` background tokens, seamlessly blending into the navbar without harsh pitch-black cutouts.
  - **Balanced Navigation Hierarchy**: Navigation destination `Timetable` is a fully integrated in-page view (`switchPageView('timetable')`, `#view-timetable`), enabling 0ms fluid tab switching between Checklist, Formulas, and Timetable with the Apple/Emil spring layout pill indicator.
  - **Strict Container Nesting Guarantee**: All app page views (`#view-questions`, `#view-syllabus`, `#view-formulas`, `#view-timetable`, `#view-notes`) must remain strictly isolated inside `.container` so that internal card wrappers never leak across views on tab switching.
  - **Subject Switcher Dropdown & Background Separation (MANDATORY)**:
    - **Visual Separation**: Must feature clean, visible dividing lines between each subject option using `<DropdownMenuSeparator />` (`h-px bg-border/40`) and an uppercase category header (`SWITCH SUBJECT` with available count).
    - **Tonal Background Contrast ("Different BG")**: The selected subject must never blend invisibly into the popover surface; it must use distinct semantic tokens (`bg-secondary` in light mode, `dark:bg-filter-active` in dark mode) paired with a circular checkmark badge. Hovered and keyboard-focused items (`data-[highlighted]`) must visibly contrast (`hover:bg-secondary/70 dark:hover:bg-filter-active/50`).
    - **Standard Dropdown Behavior & Responsive Media**: Dropdown popover must maintain responsive bounds (`w-[calc(100vw-2rem)] sm:w-[340px] max-w-[340px]`), dismiss immediately upon option selection or clicking the backdrop overlay, and support fluid keyboard arrow navigation.

---

## 7. Continuous Documentation Updates

- Whenever a new pattern, UI rule, or engineering requirement is established by the user, **immediately update this file (`AGENTS.md`) and `RULES.md`**.
- Keep all future agents aligned on the exact aesthetic and structural conventions.

---

## 8. Permanent Inclusion of All 4 Exam Papers (2023 Toggle Removed)

- **Complete 4-Paper Exam Intelligence**: All 4 verified examination papers (2025, 2024, 2023, 2022 — totaling 106 verified questions) are permanently active across all views, metrics, and analytical computations.
- **Toggle Removed for Ultimate Minimalism**: The separate 2023 toggle switch has been completely removed from the UI. Users filter by year naturally via the standard `Year` filter pill buttons (`All`, `2025`, `2024`, `2023`, `2022`).
- **Clean, Clutter-Free Control Toolbar**: The search toolbar hosts solely the full-width responsive search box and the context-sensitive `Reset` action, eliminating toggle chrome and visual clutter.

---

## 9. Responsive Web App Architecture (Mobile & Tablet Experience)

- **Mobile Viewport & PWA Foundation**:
  - Viewport configured with `width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover`.
  - PWA tags enabled (`mobile-web-app-capable`, `apple-mobile-web-app-capable`, `apple-mobile-web-app-status-bar-style: default`).
  - Dynamic `#metaThemeColor` updates with theme toggle (`#fbfaf8` light, `#09090b` dark).
- **Native App-Style Mobile Bottom Navigation Bar**:
  - Fixed at viewport bottom on screens `<= 768px` with iOS safe area inset support (`env(safe-area-inset-bottom)`).
  - 3 primary destinations: **Checklist**, **Formulas**, and **Timetable**.
  - Synchronized in real time with `switchPageView(pageId)` and URL hash routing.
  - On desktop (`> 768px`), automatically hidden, displaying the top header navigation with centered tab navigation (`display: grid; grid-template-columns: 1fr auto 1fr;` placing navigation links perfectly in the center).
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

## 10. Calendar Current Date Tracking & Visual Indicators

- **Dedicated Blue Box Banner (`.cal-today-box`)**:
  - Located in the Calendar view (`src/components/timetable/timetable-view.tsx`).
  - Styled with semantic design tokens: `var(--pastel-sky-bg)`, `var(--pastel-sky-border)`, `var(--pastel-sky-foreground)`.
  - Displays the current date formatted (e.g. `Current Date: Monday, 16 November 2026`) and an automated countdown badge to the nearest upcoming exam paper (e.g. `18 Nov (Geo-2) • in 2 days`).
- **Calendar Grid Cell Blue Box (`.cal-cell.today` / `.cal-cell.current-date`)**:
  - Highlights today's date in the calendar grid with a blue background, border, and `<span class="cal-cell-tag">Today</span>` micro-tag, seamlessly matching the sage green (Regular) and peach (Old Syllabus) exam boxes.
  - Handles exam collision gracefully (`.cal-cell.today.exam-reg` / `.cal-cell.today.exam-old`) by preserving exam category fills with a dual blue focus ring.
- **Header Badges & Key Legend Integration**:
  - Includes `Today` key indicator in the notice bar: `<span class="badge badge-sky">Today</span> Current Date`.
  - November and December month headers display context-sensitive `Today: [Day] [Month]` pills when active.
- **Real-Time Client Synchronization**:
  - Client-side React detects `new Date()`, calculates day offsets to remaining schedule papers, marks matching cells, and handles fallbacks gracefully.

---

## 11. Modular Multi-Subject Architecture & Directory Governance

- **Modular Subject Hierarchy (`subjects/`)**:
  - Every academic subject lives self-contained under `subjects/<subject_id>/` (e.g. `subjects/geotech-2/`, `subjects/rcc/`, `subjects/dhs/`, `subjects/water/`, `subjects/sa-2/`).
  - **Required Subject Files**:
    1. `subject.json`: Course code, name, short name, storage prefix, and unit titles.
    2. `canonical_data.json`: Deduplicated topic clusters and frequency metadata.
    3. `compile_data.py`: Verified questions array containing verbatim paper questions, solutions, marks, and taxonomy.
    4. `master_formulas.json`: Governing equations, LaTeX strings, parameters, and engineering notes.
    5. `papers/`: High-resolution question paper scans and raw sources.
  - **Subject Registry (`subjects/registry.json`)**: Central catalog of all registered subjects, build status, and the `active_subject` pointer.
  - **Template Scaffold (`subjects/_template/`)**: Rapid onboarding scaffold for any new subject.
- **Timetable Policy & Local Storage Isolation**:
  - The examination timetable schedule is managed via `src/data/timetable.json` and client-side `localStorage` (`civil_exam_timetable_custom_v1`).
  - The default public repository schedule contains the 3 regular syllabus subjects (Geo-2, RCC, DHS).
  - User modifications, additions, and deletions persist in client-side localStorage without collision.
  - Local host environments automatically preserve the user's 7-paper backlog schedule, with quick preset toggles in the Edit Timetable modal.
  - Concluded papers adopt a calm muted green palette (`--pastel-done-bg`, `--pastel-done-border`, `--pastel-done-foreground`, and tag `✓ Done`) across calendar, table, and timeline views. Upcoming countdowns automatically skip completed papers.
- **Next.js App Router Architecture**:
  - React components reside in `src/components/`.
  - App Router routes reside in `src/app/`.
  - Strongly typed data resides in `src/data/` (compiled from Python subjects via `npm run export:data`).
- **Clean Workspace Rule**:
  - Build scripts reside in `scripts/`.
  - No loose scratch or test scripts in the root directory.

---

## 12. Personal Notes, Custom Answers & Study Scratchpad Engine

- **Overview & User Intent**:
  - Enables students to write, store, and toggle their own custom answers and personal study notes alongside verified solutions without leaking across cards or cluttering separate pages.
  - Guarantees zero data loss across browser sessions, device reboots, and dashboard regenerations.
- **Card-Level Quick Actions (`.note-action-btn`)**:
  - Placed directly in `.q-item-actions` (Question Bank) and `.checklist-card-actions` (PYQ Checklist).
  - Features an intuitive pen icon (`hgi-pencil-edit-01`).
  - Active visual feedback: When a question has a saved note, the pen button lights up with a subtle active fill and an indicator dot (`.note-indicator-dot`).
  - Smooth expansion: Clicking the pen button opens the question card solution, switches the view to the custom answer pane, and focuses the inline note editor.
- **In-Card Solution Segmented Toggle Switch (`.sol-view-switch-row`)**:
  - Located at the top of the solution area on question cards in both Question Bank and Checklist.
  - Recessed capsule track hosting two segmented tabs and quick action:
    - `Verified Solution`: The official step-by-step verified examination answer.
    - `My Answer ✍️`: The student's custom answer/notes for that exact question. Displays an indicator dot when notes exist.
    - `Edit My Answer`: Quick inline action button to update the saved answer.
  - **Zero-Clutter Visibility Policy (Hide When No Answer Provided)**:
    - When no personal answer is provided (`!hasNote`), all 3 elements in the row (`Verified Solution` pill, `My Answer` pill, and `Add My Answer` button) remain strictly **hidden** (`display: none`).
    - The verified solution renders cleanly and directly without top toolbar clutter.
    - Only when a personal answer is provided and saved by the student (via the card header's pen note button) does `.sol-view-switch-row` appear (`display: flex`), enabling fluid switching between the Verified Solution and My Answer.
    - If the user deletes their personal answer, the switch row with all 3 elements automatically hides again.
  - Isolated scoping: Toggling between "Verified Solution" and "My Answer" changes the view for that specific question card only, leaving all other questions unaffected.
  - **Default Tab Selection**: Questions that have a saved personal answer ("My Answer") automatically display the "My Answer" tab by default on both Question Bank and Checklist cards.
- **Full Markdown & Typographic Rendering (`renderUserAnswerHtml`)**:
  - Student notes and pasted ChatGPT answers are parsed and rendered with full Markdown support into project-standard editorial typography:
    - **Markdown Headings (`#`, `##`, `###`, `####`)**: Converted into styled editorial headers (`.my-answer-heading`) without literal `#` hashes or bracket artifacts.
    - **Markdown Pipe Tables (`| ... |`)**: Parsed and rendered as clean, responsive HTML tables (`.my-answer-table-wrapper` and `.my-answer-table`) with zebra striping, tonal headers, and horizontal scroll on mobile.
    - **Numbered Lists (`1.`, `1\.`, `1)`)**: Automatically strip backslash escapes (e.g. from ChatGPT `1\.`) and format into clean `.sol-item-row` rows with `.sol-item-num`.
    - **Bullet Lists (`-`, `*`, `•`, `+`)**: Formatted as vertical `.sol-item-row` list items.
    - **Note Callouts (`Note:`, `**Note:**`)**: Formatted with dedicated `.sol-note-box` containers and `.note-tag` micro-badges.
    - **Example Micro-Tags (`Example:`, `Eg:`)**: Formatted with `.sol-example` and `.example-tag`.
    - **Formatting**: Full support for bold (`**text**`), italic (`*text*`), inline code (` `code` `), and KaTeX mathematical formulas (`$...$`, `$$...$$`).
- **Navigation Architecture & In-Card Focus Policy**:
  - The desktop sticky header and mobile bottom navigation are strictly reserved for the 4 primary destinations: `Questions` / `Question Bank`, `Checklist` / `Unit Checklist`, `Formulas`, and `Timetable`.
  - The standalone `Notes` navigation tab and count badge are excluded from both desktop and mobile navigation bars to preserve maximum vertical and horizontal space and prevent clutter.
  - Personal custom answers and notes are managed directly in-place on individual question cards via `.note-action-btn` and the in-card solution switcher (`.sol-view-switch-row`).
- **Multi-Tier Zero-Data-Loss Persistence Guarantee**:
  1. **Tier 1 (Client Storage)**: Instant local persistence in `localStorage` under `<prefix>_user_notes` and `<prefix>_general_notes`.
  2. **Tier 2 (Disk Background Sync)**: Automatic asynchronous debounced sync to server endpoint `POST /api/progress`, persisted to `user_progress.json` via `core/progress.py`.
  3. **Tier 3 (Typed Seed Data)**: Statically exported into `src/data/user_progress.json` during build for initial hydration.
  4. **Tier 4 (Export / Import Backup Utility)**: One-click "Export JSON Backup" (`exportNotesJSON`) and "Import Backup" (`triggerImportNotes`) file picker on the Notes page, plus a "Copy All Notes" clipboard utility for offline archiving.

---

## 13. KaTeX Mathematical Typography & Numerical Parsing Standards (Zero Red Errors Policy)

- **The Problem**:
  - Raw HTML entities (`&lt;`, `&gt;`, `&amp;`, `&nbsp;`, `&mdash;`), unescaped comment delimiters (`%`), raw ampersands (`&`), and corrupted Unicode negative exponents (`10⁻³` becoming `10⁻^3`) cause KaTeX parser failure, rendering equations as raw unstyled red text (`.katex-error`).
- **The Standard**:
  - **Negative Exponents**: Always format negative exponents cleanly as `10^{-3}` or `x^{-n}` with curly braces. Never output bare `^-3` or corrupted `⁻^3`.
  - **HTML Entity Sanitization**: Never pass raw HTML entities inside math delimiters. `&lt;` must be `<`, `&gt;` must be `>`, `&amp;` must be `\&`, `&nbsp;` must be space, and `&mdash;` must be `\text{ --- }`.
  - **Percentage Escaping**: Always escape literal percentage signs in LaTeX math mode as `\%` (`100\%`, `80.0\%`) so they are not treated as LaTeX line comments that truncate the equation.
  - **Balanced Radicals & Nested Parentheses**: Ensure square roots with internal parentheses (e.g. Coulomb friction terms `\sqrt{...}`) enclose the full quotient without premature truncation.
  - **Pre-Process Sanitization Hook**: `MathRenderer` in `src/components/common/math-renderer.tsx` sanitizes all dynamic and server/client-rendered equations before KaTeX parsing occurs.
- **Verification Rule**: Every time numerical or formula code is modified, run `npm run build && npx tsc --noEmit` to ensure zero compilation or type errors.

---

## 15. Formula Parameter Breakdown & Clean Typography Standard (Zero Separate Bg & Font)

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

## 14. Star & Mark-for-Later Question Tracking Engine

- **Overview & User Intent**:
  - Allows students to star high-yield questions for fast revision and mark secondary or deferred questions as "Later".
  - **Zero Text Mandate**: Star and Later controls must be purely visual icon-only buttons ("notext just icon"), never rendering text labels inside the buttons.
- **Card-Level Quick Actions (`.icon-action-btn`)**:
  - Integrated directly in `.q-item-actions` (Question Bank) and `.checklist-card-actions` (PYQ Checklist), positioned immediately adjacent to Note, Mark Done, and accordion chevron controls.
  - Sized uniformly at `28px × 28px` with rounded pill curves (`var(--radius-full)`), subtle scale transitions (`scale(1.08)` hover, `scale(0.92)` active), and touch-friendly padding.
  - **Star Button (`.star-action-btn`)**: Features a crisp 5-point star SVG (`<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2">`). When active (`.is-starred`), fills with vibrant amber gold (`var(--pastel-amber-bg)` and `var(--pastel-amber-foreground)`).
  - **Later Button (`.later-action-btn`)**: Features a clean watch/clock SVG (`<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>`). When active (`.is-later`), highlights with soft lavender (`var(--pastel-lavender-bg)` and `var(--pastel-lavender-foreground)`).
  - **Card Dimming (`.q-item.is-later` / `.checklist-card.is-later`)**: When a question is postponed for later, its card adopts a subtle reduced opacity (`0.65`) that smoothly restores to `1.0` on hover, providing instant visual hierarchy.
  - **Accordion Shield**: Clicking either icon button stops event propagation (`event.stopPropagation()`) and never triggers card accordion expansion or collapse.
- **Strict Exclusion from Total Count (MANDATORY)**:
  - **Core Rule**: Questions marked as "Later" are strictly **excluded from total counts and completion denominators** across the entire application.
  - **Question Bank Denominator**: `totalSource = items.filter(q => !laterQuestions.has(q.id)).length`. Total matched and completion percentage (`doneCount / total Done (%)`) reflect only active questions.
  - **PYQ Checklist Metrics**: Overall completion meter (`checklistTotalCount`), percentage badge (`checklistTotalPct`), overline badge (`checklistOverlineCount`), and status counts (`checklistAllCount`, `checklistIncompleteCount`) exclude questions marked as "Later".
  - **Year & Unit Breakdown Denominators**: `yearTotal[y]` and `subheadTotal[yuKey]` tally only active questions, guaranteeing that postponed questions never distort syllabus mastery progress.
  - **Navbar Badges**: Desktop header and mobile navigation badges reflect the active non-later count (e.g. `76 PYQs` instead of `78 PYQs`).
- **One-Click Segmented Filtering**:
  - The Question Bank Control Panel and PYQ Checklist Toolbar include dedicated `Starred` and `Later` segmented status pills (`All`, `Incomplete`, `Completed`, `Starred`, `Later`).
  - Selecting `Starred` isolates only starred items. Selecting `Later` reviews all deferred items. Selecting `Incomplete` automatically excludes deferred items so students focus strictly on remaining active work.
- **Multi-Tier Persistence**:
  - Saved instantaneously to `localStorage` under `<prefix>_starred_questions` and `<prefix>_later_questions`.
  - Asynchronously synchronized to `user_progress.json` on disk via `POST /api/progress`.
  - Seed-injected during dashboard generation (`EMBEDDED_STARRED`, `EMBEDDED_LATER`) for instant zero-latency bootstrapping.

---

## 15. Minimal Favicon & Touch Icon Architecture

- **Minimalist Aesthetic & Brand Identity**:
  - Pure geometric "E" lettermark (Exam Intelligence & Engineering Precision) centered within a dark obsidian/zinc squircle (`#09090b` canvas, `rx=7` on 32×32 grid).
  - Subtle perimeter border (`rgba(255, 255, 255, 0.15)`) ensuring crisp edge contrast against both light and dark browser tab strips.
  - Crisp high-contrast white glyph (`#fcfcfd`) with mathematically balanced arm proportions (80% golden ratio middle arm).
- **Pixel-Perfect Integer Alignment (Zero Subpixel Blur)**:
  - Designed on a 32×32 grid with all vertices on even integer coordinates (`M8 6h16v4H12v4h9v4H12v4h12v4H8z`), scaling by 0.5 to 16×16 with exact 1-to-1 pixel alignment (2px stem, 2px arm thickness, 2px uniform gaps).
- **Multi-Tier Deployment Standard**:
  1. **Inline URL-Safe SVG Data URI**: Embedded directly in `<link rel="icon" type="image/svg+xml">` without literal `</style>` tags to ensure instant rendering when opened locally via `file://` offline and zero extra HTTP roundtrips.
  2. **Standalone Vector (`favicon.svg`)**: Root asset supporting `@media (prefers-color-scheme: light / dark)` theme adaptation and infinite retina scaling.
  3. **Multi-Resolution Windows/Legacy Icon (`favicon.ico`)**: Root asset containing 16×16, 32×32, and 48×48 downsampled bitmaps with Lanczos filtering.
  4. **High-DPI Touch Icon (`apple-touch-icon.png`)**: 180×180 PNG asset for iOS Safari homescreen shortcuts and macOS Safari bookmarks.
- **Next.js Metadata Integration**:
  - Declared in `src/app/layout.tsx` linking to icons hosted in `public/` (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`).

---

## 16. Unified Icon System Standard (MANDATORY)

- **Official Icon Architecture**: Clean, semantic React SVG icons consolidated in `src/components/ui/icons.tsx` based on Hugeicons Stroke-Rounded specifications.
- **Zero Sparkle Policy**: Sparkles, generative AI stars, and multi-point star icons are strictly prohibited.
- **Icon Sizing & Typography Proportions**:
  - Base `.icon`: `1.25rem` (20px)
  - `.icon-xs`: `1rem` (16px)
  - `.icon-sm`: `1.125rem` (18px)
  - `.icon-md`: `1.375rem` (22px)
  - `.icon-lg`: `1.75rem` (28px)
  - Mobile bottom nav icons (`.mobile-nav-icon`): `22px`
  - Floating back-to-top (`.scroll-to-top-btn i`): `24px`
- **Icon Mapping Catalog**:
  - **Question Bank**: `<i class="icon icon-sm hgi-stroke hgi-book-open-01"></i>`
  - **Unit Checklist**: `<i class="icon icon-sm hgi-stroke hgi-task-01"></i>`
  - **Formulas**: `<i class="icon icon-sm hgi-stroke hgi-function-of-x"></i>`
  - **Notes / Scratchpad**: `<i class="icon icon-sm hgi-stroke hgi-note-01"></i>`
  - **Timetable**: `<i class="icon icon-sm hgi-stroke hgi-calendar-03"></i>`
  - **Theme Toggle**: `<i class="icon hgi-stroke hgi-sun-01"></i>` (dark) / `<i class="icon hgi-stroke hgi-moon-02"></i>` (light)
  - **Search**: `<i class="icon icon-sm search-icon hgi-stroke hgi-search-01"></i>`
  - **Search Clear**: `<i class="icon icon-xs hgi-stroke hgi-cancel-01"></i>`
  - **Reset Filters**: `<i class="icon icon-xs hgi-stroke hgi-arrow-reload-horizontal"></i>`
  - **Clear Done**: `<i class="icon icon-xs hgi-stroke hgi-delete-02"></i>`
  - **Star Question**: `<i class="icon icon-xs star-icon hgi-stroke hgi-star"></i>`
  - **Later Question**: `<i class="icon icon-xs clock-icon hgi-stroke hgi-clock-01"></i>`
  - **Personal Note**: `<i class="icon icon-xs pen-icon hgi-stroke hgi-pencil-edit-01"></i>`
  - **Mark Done**: `<i class="icon icon-xs check-icon hgi-stroke hgi-checkmark-circle-02"></i>`
  - **Accordion Chevron**: `<i class="icon icon-sm chevron-icon hgi-stroke hgi-chevron-down"></i>` (rotates 180° when expanded)
  - **Checklist Tick**: `<i class="icon chk-svg hgi-stroke hgi-tick-01"></i>`
  - **Verified Solution Tab**: `<i class="icon icon-xs hgi-stroke hgi-checkmark-badge-01"></i>`
  - **Copy Action**: `<i class="icon icon-sm hgi-stroke hgi-copy-01"></i>`
  - **Scroll to Top**: `<i class="hgi-stroke hgi-arrow-up-01"></i>`
- **Zero Sparkle Rule Preserved**: Never use AI star glyphs, sparkles, or multi-point sparkles (`hgi-stars`, `hgi-sparkle`). Star questions strictly use standard 5-point star (`hgi-star`).

---

## 17. Layout ID Shared Sliding Pill Engine & Smooth Div Transitions (MANDATORY)

- **Layout ID Shared Pill Standard (Framer-Motion / Apple Style)**:
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


