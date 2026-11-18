import sys
import json
import re
import argparse
from pathlib import Path

# Add repo root to sys.path
repo_root = Path(__file__).resolve().parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from core.subjects import (
    load_subject,
    list_subjects,
    get_active_subject_id,
    scaffold_new_subject,
)
from core.formatter import format_solution, clean_num

def build_unit_checklist_html(questions, unit_titles=None):
    if not unit_titles:
        unit_titles = {}

    from collections import defaultdict
    tree = defaultdict(lambda: defaultdict(list))
    for q in questions:
        tree[str(q['year'])][q['unit']].append(q)

    for y in tree:
        for u in tree[y]:
            tree[y][u].sort(key=lambda x: x.get('q_no', ''))

    years = sorted(tree.keys(), reverse=True)

    distinct_units = sorted(list(set(int(q['unit']) for q in questions if q.get('unit'))))
    unit_buttons = ['<button type="button" class="filter-pill-btn active" data-unit="all" onclick="setChecklistUnit(\'all\', this)">All</button>']
    for u in distinct_units:
        unit_buttons.append(f'<button type="button" class="filter-pill-btn" data-unit="{u}" onclick="setChecklistUnit(\'{u}\', this)">Unit {u}</button>')
    unit_pills_html = "".join(unit_buttons)

    html = []
    html.append(f'''
        <!-- ====================================================
             PAGE VIEW 2: PYQ CHECKLIST (YEAR-WISE & UNIT-WISE)
             ==================================================== -->
        <div class="app-page-view" id="view-syllabus">
            <div class="checklist-header-row">
                <h1 class="page-title">Checklist</h1>

                <div class="checklist-header-right">
                    <div class="checklist-progress-circle" id="checklistProgressWidget" onclick="toggleChecklistProgressFilter()" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' '){{event.preventDefault();toggleChecklistProgressFilter();}}" title="Overall Checklist Completion: 0% • Click to filter incomplete questions" aria-label="Overall Checklist Completion: 0%">
                        <svg class="checklist-progress-ring" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true">
                            <defs>
                                <linearGradient id="checklistRingGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" stop-color="var(--ring-grad-start)" />
                                    <stop offset="100%" stop-color="var(--ring-grad-end)" />
                                </linearGradient>
                            </defs>
                            <circle class="checklist-ring-bg" cx="21" cy="21" r="17.5" />
                            <circle class="checklist-ring-fill" id="checklistTotalRing" cx="21" cy="21" r="17.5" />
                        </svg>
                        <span class="checklist-stat-pct" id="checklistTotalPct">
                            <span class="pct-num" id="checklistPctVal">0</span><span class="pct-unit">%</span>
                        </span>
                    </div>

                    <div class="checklist-summary-units">
    ''')

    for y in years:
        total_y = sum(len(tree[y][u]) for u in tree[y])
        html.append(f'''
                    <a href="#year-section-{y}" class="checklist-year-pill" id="checklistYearPill-{y}" onclick="jumpToChecklistYear('{y}', event)" title="Jump to {y} Paper">
                        <span class="badge badge-year-{y}">{y}</span>
                        <span class="unit-pill-count" id="yearPillCount-{y}">0/{total_y}</span>
                    </a>
        ''')

    html.append(f'''
                    </div>
                </div>
            </div>

            <!-- CHECKLIST CONTROLS & SEARCH TOOLBAR (MINIMAL, ZERO BG SEPARATION) -->
            <div class="checklist-toolbar">
                <div class="checklist-toolbar-filters">
                    <!-- STATUS -->
                    <div id="checklistStatusGroup" class="filter-pill-group">
                        <button type="button" class="filter-pill-btn active" data-status="all" onclick="setChecklistStatus('all')">
                            All <span class="nav-badge" id="checklistAllCount">{len(questions)}</span>
                        </button>
                        <button type="button" class="filter-pill-btn" data-status="incomplete" onclick="setChecklistStatus('incomplete')">
                            Incomplete <span class="nav-badge" id="checklistIncompleteCount">{len(questions)}</span>
                        </button>
                        <button type="button" class="filter-pill-btn" data-status="completed" onclick="setChecklistStatus('completed')">
                            Done <span class="nav-badge" id="checklistCompletedCount">0</span>
                        </button>
                        <button type="button" class="filter-pill-btn" data-status="starred" onclick="setChecklistStatus('starred')">
                            Starred <span class="nav-badge" id="checklistStarredCount">0</span>
                        </button>
                        <button type="button" class="filter-pill-btn" data-status="later" onclick="setChecklistStatus('later')">
                            Later <span class="nav-badge" id="checklistLaterCount">0</span>
                        </button>
                    </div>

                    <div class="checklist-filter-divider" aria-hidden="true"></div>

                    <!-- UNIT -->
                    <div class="checklist-unit-group" id="checklistUnitGroup">
                        <span class="checklist-filter-label">Unit</span>
                        <div id="checklistUnitFilters" class="filter-pill-group">
                            {unit_pills_html}
                        </div>
                    </div>
                </div>

                <!-- MINIMAL COMPACT SEARCH BOX ON RIGHT -->
                <div class="checklist-search-box">
                    <i class="icon icon-sm checklist-search-icon hgi-stroke hgi-search-01"></i>
                    <input type="text" class="checklist-search-input" id="checklistSearchInput" placeholder="Filter questions..." aria-label="Filter questions">
                    <button type="button" class="checklist-search-clear-btn" id="checklistSearchClearBtn" title="Clear search" aria-label="Clear search" style="display: none;">
                        <i class="icon icon-xs hgi-stroke hgi-cancel-01"></i>
                    </button>
                </div>
            </div>

            <!-- YEAR SECTIONS WITH UNITS INSIDE -->
            <div class="checklist-years-container">
    ''')

    for y in years:
        html.append(f'''
                <section class="checklist-year-group" id="year-section-{y}">
                    <div class="checklist-year-units">
        ''')

        for u in sorted(tree[y].keys()):
            u_qs = tree[y][u]
            u_title = unit_titles.get(u, f'Unit {u}')
            html.append(f'''
                        <div class="checklist-unit-subgroup" id="unit-subgroup-{y}-{u}">
                            <div class="checklist-unit-subhead">
                                <span class="badge badge-unit-{u}">Unit {u}</span>
                                <span class="checklist-unit-subhead-title">{u_title}</span>
                                <span class="checklist-unit-subhead-count" id="unitSubheadCount-{y}-{u}">0/{len(u_qs)}</span>
                            </div>

                            <div class="checklist-unit-items">
            ''')

            for q in u_qs:
                b_class = f'badge-repeat-{q["repeat_count_str"]}' if q.get("repeat_count_str") in ['4x', '3x', '2x'] else 'badge-subtle'
                rep_badge = f'<span class="badge {b_class}">{q["repeat_count_str"]}</span>' if q.get("repeat_count_str") else ''
                safe_question = q.get('question', '')
                formatted_sol = q.get('formatted_solution', '')
                q_no_label = q.get('q_no') or q.get('qno', '')
                raw_marks = str(q.get('marks', ''))
                q_marks_label = (raw_marks + 'M') if raw_marks and not raw_marks.endswith('M') else (raw_marks or '2M')
                q_type = q.get('type', 'Theory')

                html.append(f'''
                                <div class="checklist-card" id="chk-card-{q['id']}" data-id="{q['id']}" data-year="{y}" data-unit="{u}" onclick="toggleChecklistSolution('{q['id']}', event)" title="Click to view answer">
                                    <div class="checklist-card-check" onclick="event.stopPropagation()">
                                        <button class="checklist-checkbox-btn" 
                                                id="chk-btn-{q['id']}"
                                                onclick="toggleCompleteQuestion('{q['id']}', event)"
                                                title="Toggle completed"
                                                aria-label="Toggle completion for {q['id']}">
                                            <i class="icon chk-svg hgi-stroke hgi-tick-01"></i>
                                        </button>
                                    </div>
                                    <div class="checklist-card-content">
                                        <div class="checklist-card-header-row">
                                            <div class="checklist-card-meta">
                                                <span class="badge badge-subtle font-mono">{q_no_label}</span>
                                                <span class="badge badge-year-{y}">{y}</span>
                                                <span class="badge badge-subtle">{q_marks_label}</span>
                                                <span class="badge badge-subtle">{q_type}</span>
                                                {rep_badge}
                                            </div>
                                            <div class="checklist-card-actions">
                                                <button class="icon-action-btn star-action-btn" id="chk-star-btn-{q['id']}" onclick="toggleStarQuestion('{q['id']}', event)" title="Star this question" aria-label="Star question">
                                                    <i class="icon icon-xs star-icon hgi-stroke hgi-star"></i>
                                                </button>
                                                <button class="icon-action-btn later-action-btn" id="chk-later-btn-{q['id']}" onclick="toggleLaterQuestion('{q['id']}', event)" title="Mark for later" aria-label="Mark for later">
                                                    <i class="icon icon-xs clock-icon hgi-stroke hgi-clock-01"></i>
                                                </button>
                                                <button class="icon-action-btn note-action-btn" id="chk-note-btn-{q['id']}" onclick="handleChecklistNoteClick('{q['id']}', event)" title="Personal Answer / Notes" aria-label="Personal Notes">
                                                    <i class="icon icon-xs pen-icon hgi-stroke hgi-pencil-edit-01"></i>
                                                </button>
                                                <i class="icon icon-sm chevron-icon chk-chevron hgi-stroke hgi-chevron-down"></i>
                                            </div>
                                        </div>
                                        <div class="checklist-card-title">{safe_question}</div>
                                        <div class="checklist-solution-content" id="chk-sol-{q['id']}">
                                            <div class="sol-view-switch-row" id="chk-switch-row-{q['id']}" style="display: none;" onclick="event.stopPropagation()">
                                                <div class="sol-view-pills">
                                                    <button type="button" class="sol-view-pill active" id="chk-tab-std-{q['id']}" onclick="switchSolutionTab('{q['id']}', 'standard', event, true)">
                                                        <i class="icon icon-xs hgi-stroke hgi-checkmark-badge-01"></i>
                                                        <span>Verified Solution</span>
                                                    </button>
                                                    <button type="button" class="sol-view-pill" id="chk-tab-mine-{q['id']}" onclick="switchSolutionTab('{q['id']}', 'mine', event, true)">
                                                        <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                                        <span>My Answer</span>
                                                        <span class="note-indicator-dot" id="chk-dot-{q['id']}" style="display:none;"></span>
                                                    </button>
                                                </div>
                                                <div class="sol-view-quick-actions">
                                                    <button type="button" class="sol-btn-edit-note" id="chk-btn-edit-{q['id']}" onclick="openNoteEditor('{q['id']}', event, true)" title="Edit or write your personal answer">
                                                        <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                                        <span id="chk-btn-edit-text-{q['id']}">Add My Answer</span>
                                                    </button>
                                                </div>
                                            </div>

                                            <div class="solution-pane" id="chk-pane-std-{q['id']}">
                                                <div class="solution-body">
                                                    {formatted_sol}
                                                </div>
                                            </div>

                                            <div class="solution-pane" id="chk-pane-mine-{q['id']}" style="display: none;">
                                                <div class="my-answer-container" id="chk-my-answer-box-{q['id']}">
                                                </div>
                                            </div>

                                            <div class="note-editor-container" id="chk-editor-{q['id']}" style="display: none;" onclick="event.stopPropagation()">
                                                <div class="note-editor-header">
                                                    <div class="note-editor-title">
                                                        <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                                        <span>Personal Answer / Custom Solution</span>
                                                    </div>
                                                    <span class="note-editor-meta">Saved in data &bull; Never lost</span>
                                                </div>
                                                <p class="note-editor-hint">Write your alternate explanation, textbook derivation steps, or revision notes. Supports line breaks, numbered points, and math ($...$).</p>
                                                <textarea class="note-editor-textarea" id="chk-note-input-{q['id']}" rows="7" placeholder="Write your own custom answer or notes for this question here..."></textarea>
                                                <div class="note-editor-footer">
                                                    <span class="note-editor-keys">Press <kbd>Ctrl</kbd> + <kbd>Enter</kbd> to save</span>
                                                    <div class="note-editor-buttons">
                                                        <button type="button" class="note-btn-cancel" onclick="cancelNoteEditor('{q['id']}', event, true)">Cancel</button>
                                                        <button type="button" class="note-btn-save" onclick="saveQuestionNote('{q['id']}', event, true)">
                                                            <i class="icon icon-xs hgi-stroke hgi-tick-01"></i>
                                                            <span>Save Answer</span>
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="checklist-solution-footer">
                                                <button type="button" class="checklist-jump-link" onclick="jumpToQuestionBank('{q['id']}'); event.stopPropagation();" title="Open question in Questions">
                                                    <span>Open in Questions &rarr;</span>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                ''')

            html.append('''
                            </div>
                        </div>
            ''')

        html.append('''
                    </div>
                </section>
        ''')

    html.append('''
            </div>
        </div>
    ''')
    return ''.join(html)

def build_dashboard_for_subject(subject_id=None, write_index=True):
    ctx = load_subject(subject_id)
    canonical_topics = ctx.canonical_topics
    raw_questions = ctx.raw_questions
    unit_titles = ctx.unit_titles or {
        1: 'Lateral Earth Pressure',
        2: 'Shear Strength & Slope Stability',
        3: 'Shallow Foundations',
        4: 'Deep Foundations (Piles)',
        5: 'Soil Exploration & Testing'
    }
    subject_name = ctx.name
    subject_code = ctx.code
    storage_prefix = ctx.storage_prefix

    math_enhancer = None
    if ctx.formula_module and hasattr(ctx.formula_module, "enhance_solution_math"):
        math_enhancer = ctx.formula_module.enhance_solution_math

    q_order = {q['id']: idx for idx, q in enumerate(raw_questions)}

    cluster_first_seen = {}
    for t in canonical_topics:
        q_ids = [q['id'] if isinstance(q, dict) else q for q in t.get('questions', [])]
        indices = [q_order[qid] for qid in q_ids if qid in q_order]
        cluster_first_seen[t['id']] = min(indices) if indices else 999

    cluster_map = {}
    for idx, t in enumerate(canonical_topics):
        q_items = t.get('questions', [])
        q_ids = [q['id'] if isinstance(q, dict) else q for q in q_items]
        years = sorted(list(set(str(raw_questions[q_order[qid]]['year']) for qid in q_ids if qid in q_order)), reverse=True)
        is_4x = len(years) >= 4
        is_3x = len(years) == 3
        is_2x = len(years) == 2
        rank = 1 if is_4x else (2 if is_3x else (3 if is_2x else 4))
        count_str = "4x" if is_4x else ("3x" if is_3x else ("2x" if is_2x else ""))
        first_idx = cluster_first_seen.get(t['id'], 999)
        for qid in q_ids:
            cluster_map[qid] = {
                'cluster_id': t['id'],
                'cluster_title': t['title'],
                'cluster_unit': t.get('unit', 1),
                'cluster_rep_frequency': t.get('rep_frequency', ''),
                'cluster_is_repeated': is_4x or is_3x or is_2x,
                'cluster_rank': rank,
                'cluster_order': first_idx,
                'repeat_count_str': count_str
            }

    for q in raw_questions:
        q['formatted_solution'] = format_solution(q['solution'], math_enhancer=math_enhancer)
        c_info = cluster_map.get(q['id'], {})
        q['cluster_id'] = c_info.get('cluster_id', '')
        q['cluster_title'] = c_info.get('cluster_title', q.get('topic', ''))
        q['cluster_unit'] = c_info.get('cluster_unit', q.get('unit', 1))
        q['unit'] = q['cluster_unit']
        q['cluster_rep_frequency'] = c_info.get('cluster_rep_frequency', q.get('rep_frequency', ''))
        q['cluster_is_repeated'] = c_info.get('cluster_is_repeated', False)
        q['cluster_rank'] = c_info.get('cluster_rank', 4)
        q['cluster_order'] = c_info.get('cluster_order', 999)
        q['repeat_count_str'] = c_info.get('repeat_count_str', '')
        q['unit_name'] = unit_titles.get(q['cluster_unit'], '')

    for c in canonical_topics:
        c['formatted_solution'] = format_solution(c.get('master_solution', ''), math_enhancer=math_enhancer)

    canonical_json_str = json.dumps(canonical_topics).replace("</script>", r"<\/script>")
    raw_json_str = json.dumps(raw_questions).replace("</script>", r"<\/script>")

    from core.progress import get_subject_progress
    sub_prog = get_subject_progress(ctx.id)
    embedded_completed_json = json.dumps(sub_prog.get("completed_questions", [])).replace("</script>", r"<\/script>")
    embedded_starred_json = json.dumps(sub_prog.get("starred_questions", [])).replace("</script>", r"<\/script>")
    embedded_later_json = json.dumps(sub_prog.get("later_questions", [])).replace("</script>", r"<\/script>")
    embedded_notes_json = json.dumps(sub_prog.get("notes", {})).replace("</script>", r"<\/script>")
    embedded_general_notes = json.dumps(sub_prog.get("general_notes", "")).replace("</script>", r"<\/script>")
    subject_id_str = ctx.id

    unit_checklist_html = build_unit_checklist_html(raw_questions, unit_titles)

    html_template = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="theme-color" id="metaThemeColor" content="#09090b">
    <meta name="format-detection" content="telephone=no">
    <title>{subject_name} ({subject_code}) | PYQ Analysis &amp; High-Yield Solutions</title>
    <!-- Minimalist Favicon & Touch Icons -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%2309090b'/%3E%3Crect x='0.5' y='0.5' width='31' height='31' rx='6.5' fill='none' stroke='rgba(255,255,255,0.15)' stroke-width='1'/%3E%3Cpath d='M8 6h16v4H12v4h9v4H12v4h12v4H8z' fill='%23fcfcfd'/%3E%3C/svg%3E">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="alternate icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- Hugeicons Font (CDN with offline local fallback) -->
    <link rel="stylesheet" href="https://use.hugeicons.com/font/icons.css" onerror="this.onerror=null;this.href='vendor/hugeicons/icons.css'">
    <link rel="stylesheet" href="vendor/hugeicons/icons.css">
    <style>
        /* ----------------------------------------------------
           STRICT DESIGN SYSTEM TOKENS & PURE BG SEPARATION
           (ZERO BORDERS THROUGHOUT ENTIRE APPLICATION)
           ---------------------------------------------------- */
        :root {{
            /* Strict Custom Typography System Tokens */
            --font-size-h1: 56px;
            --line-height-h1: 72px;
            --font-size-h2: 40px;
            --line-height-h2: 56px;
            --font-size-h3: 28px;
            --line-height-h3: 40px;
            --font-size-h4: 26px;
            --line-height-h4: 32px;
            --font-size-h5: 22px;
            --line-height-h5: 32px;
            --font-size-h6: 20px;
            --line-height-h6: 28px;
            --font-size-body-large: 16px;
            --line-height-body-large: 27px;
            --font-size-body-medium: 14.5px;
            --line-height-body-medium: 22px;
            --font-size-body-small: 13px;
            --line-height-body-small: 18px;
            --font-size-button: 14px;
            --line-height-button: 21px;

            /* Specific component scale constraints */
            --font-size-stat: 24px;
            --line-height-stat: 32px;
            --font-size-overline: 11px;

            /* Neutral Color Palette (Light Mode - Harmonized with Timetable warm canvas) */
            --background: #fbfaf8;
            --foreground: #1e293b;
            --card: #ffffff;
            --card-foreground: #1e293b;
            --popover: #ffffff;
            --popover-foreground: #1e293b;
            --primary: #2d3748;
            --primary-foreground: #ffffff;
            --secondary: #f3f1ec;
            --secondary-hover: #e8e5dc;
            --secondary-foreground: #1e293b;
            --muted: #f3f1ec;
            --muted-foreground: #64748b;
            --input-bg: #f3f1ec;
            --border: #e8e5dc;
            --border-hover: #d8d4c9;

            /* Filter Pill Segmented Active Tokens (Light Mode) */
            --filter-pill-active-bg: #ffffff;
            --filter-pill-active-fg: #1e293b;
            --filter-pill-active-shadow: 0 1px 3px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);

            /* Circular Progress Ring Gradient Tokens (Light Mode) */
            --ring-grad-start: #059669;
            --ring-grad-end: #10b981;

            /* Neutral Pastel Accents */
            --pastel-sage-bg: #eaf4ed;
            --pastel-sage-foreground: #205c36;

            --pastel-lavender-bg: #f4effc;
            --pastel-lavender-foreground: #581c87;

            --pastel-peach-bg: #fff1e8;
            --pastel-peach-foreground: #9a4318;

            --pastel-sky-bg: #ebf5fd;
            --pastel-sky-foreground: #1a5a90;

            --pastel-rose-bg: #fdf2f4;
            --pastel-rose-foreground: #881337;

            --pastel-sand-bg: #fdf8e8;
            --pastel-sand-foreground: #713f12;

            --pastel-amber-bg: #fef3c7;
            --pastel-amber-foreground: #92400e;

            --table-header-bg: #f3f1ec;
            --table-row-hover: #faf9f6;
            --table-row-alt: #fdfcfb;

            --solution-card-bg: #f8f7f4;
            --foreground-secondary: #334155;
            --math-display-bg: #f3f1ec;
            --math-copy-btn-bg: #e8e5dc;
            --math-copy-btn-hover: #d8d4c9;
            --math-param-pill-bg: #e8e5dc;

            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.03);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.06), 0 2px 4px -2px rgba(0, 0, 0, 0.03);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.06), 0 4px 6px -4px rgba(0, 0, 0, 0.03);

            --radius-sm: 6px;
            --radius-md: 8px;
            --radius-lg: 12px;
            --radius-full: 9999px;

            --font-family-sans: "Aeonik", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            --font-family-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        }}

        [data-theme="dark"] {{
            /* Neutral Color Palette (Dark Mode - Harmonized with Timetable zinc canvas) */
            --background: #09090b;
            --foreground: #fcfcfd;
            --card: #141416;
            --card-foreground: #fcfcfd;
            --popover: #141416;
            --popover-foreground: #fcfcfd;
            --primary: #fcfcfd;
            --primary-foreground: #09090b;
            --secondary: #1c1c1f;
            --secondary-hover: #27272a;
            --secondary-foreground: #fcfcfd;
            --muted: #1c1c1f;
            --muted-foreground: #a1a1aa;
            --input-bg: #1c1c1f;
            --border: #27272a;
            --border-hover: #3f3f46;

            /* Filter Pill Segmented Active Tokens (Dark Mode - Apple/Linear Elevated Zinc) */
            --filter-pill-active-bg: #27272a;
            --filter-pill-active-fg: #fcfcfd;
            --filter-pill-active-shadow: 0 1px 3px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.08);

            /* Circular Progress Ring Gradient Tokens (Dark Mode) */
            --ring-grad-start: #10b981;
            --ring-grad-end: #34d399;

            --pastel-sage-bg: rgba(52, 211, 153, 0.16);
            --pastel-sage-foreground: #34d399;

            --pastel-lavender-bg: rgba(168, 85, 247, 0.16);
            --pastel-lavender-foreground: #d8b4fe;

            --pastel-peach-bg: rgba(251, 146, 60, 0.16);
            --pastel-peach-foreground: #fb923c;

            --pastel-sky-bg: rgba(56, 189, 248, 0.16);
            --pastel-sky-foreground: #38bdf8;

            --pastel-rose-bg: rgba(244, 63, 94, 0.16);
            --pastel-rose-foreground: #fca5a5;

            --pastel-sand-bg: rgba(234, 179, 8, 0.16);
            --pastel-sand-foreground: #fde047;

            --pastel-amber-bg: rgba(245, 158, 11, 0.16);
            --pastel-amber-foreground: #fbbf24;

            --table-header-bg: #18181b;
            --table-row-hover: #1f1f23;
            --table-row-alt: #101012;

            --solution-card-bg: #18181b;
            --foreground-secondary: #d4d4d8;
            --math-display-bg: #111113;
            --math-copy-btn-bg: #1c1c1f;
            --math-copy-btn-hover: #27272a;
            --math-param-pill-bg: #1c1c1f;

            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.45);
            --shadow-lg: 0 10px 24px rgba(0, 0, 0, 0.55);
        }}

        /* ZERO BORDERS ENFORCEMENT & APP PERFORMANCE */
        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            outline: none;
            -webkit-tap-highlight-color: transparent;
        }}

        button, input, select, textarea {{
            border: none;
            outline: none;
        }}

        html, body {{
            overflow-x: hidden;
            width: 100%;
            -webkit-text-size-adjust: 100%;
        }}

        body {{
            font-family: var(--font-family-sans);
            background-color: var(--background);
            color: var(--foreground);
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            transition: background-color 0.2s ease, color 0.2s ease;
        }}

        button, a, input, select {{
            touch-action: manipulation;
        }}

        .container {{
            max-width: 1440px;
            width: 100%;
            margin: 0 auto;
            padding-left: max(1rem, env(safe-area-inset-left));
            padding-right: max(1rem, env(safe-area-inset-right));
            box-sizing: border-box;
        }}

        @media (min-width: 640px) {{
            .container {{
                padding-left: max(1.5rem, env(safe-area-inset-left));
                padding-right: max(1.5rem, env(safe-area-inset-right));
            }}
        }}

        @media (min-width: 1024px) {{
            .container {{
                padding-left: max(2.5rem, env(safe-area-inset-left));
                padding-right: max(2.5rem, env(safe-area-inset-right));
            }}
        }}

        @media (min-width: 1440px) {{
            .container {{
                padding-left: max(3.5rem, env(safe-area-inset-left));
                padding-right: max(3.5rem, env(safe-area-inset-right));
            }}
        }}

        @media (max-width: 640px) {{
            :root {{
                --font-size-h1: 32px;
                --line-height-h1: 42px;
                --font-size-h2: 24px;
                --line-height-h2: 32px;
                --font-size-h3: 20px;
                --line-height-h3: 28px;
                --font-size-h4: 18px;
                --line-height-h4: 24px;
                --font-size-h5: 16px;
                --line-height-h5: 22px;
                --font-size-h6: 15px;
                --line-height-h6: 20px;
                --font-size-body-large: 15px;
                --line-height-body-large: 23px;
                --font-size-body-medium: 14px;
                --line-height-body-medium: 21px;
                --font-size-body-small: 12px;
                --line-height-body-small: 16px;
                --font-size-button: 13px;
                --line-height-button: 19px;
                --font-size-stat: 20px;
                --line-height-stat: 28px;
            }}
        }}

        /* Typography */
        .text-h1 {{ font-size: var(--font-size-h1); line-height: var(--line-height-h1); font-weight: 700; color: var(--foreground); }}
        .text-h2 {{ font-size: var(--font-size-h2); line-height: var(--line-height-h2); font-weight: 700; color: var(--foreground); }}
        .text-h3 {{ font-size: var(--font-size-h3); line-height: var(--line-height-h3); font-weight: 500; color: var(--foreground); }}
        .text-body-large {{ font-size: var(--font-size-body-large); line-height: var(--line-height-body-large); font-weight: 500; color: var(--foreground); }}
        .text-body-medium {{ font-size: var(--font-size-body-medium); line-height: var(--line-height-body-medium); font-weight: 500; color: var(--foreground); }}
        .text-body-small {{ font-size: var(--font-size-body-small); line-height: var(--line-height-body-small); font-weight: 400; color: var(--muted-foreground); }}
        .card-stat-number {{ font-size: var(--font-size-stat); line-height: var(--line-height-stat); font-weight: 600; color: var(--foreground); }}
        .section-header-title {{ font-size: var(--font-size-h6); line-height: var(--line-height-h6); font-weight: 600; color: var(--foreground); display: flex; align-items: center; gap: 0.5rem; }}
        .card-overline {{ font-size: var(--font-size-overline); font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; color: var(--muted-foreground); display: inline-block; }}

        /* ----------------------------------------------------
           HUGEICONS SYSTEM & ENHANCED ICON TYPOGRAPHY TOKENS
           ---------------------------------------------------- */
        .icon,
        .hgi-stroke.icon,
        i.hgi-stroke {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 1.25rem;
            height: 1.25rem;
            font-size: 1.25rem;
            line-height: 1;
            stroke-width: 2;
            stroke: currentColor;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
            vertical-align: middle;
            flex-shrink: 0;
            font-style: normal;
        }}

        .icon-xs, .hgi-stroke.icon-xs {{ width: 1rem; height: 1rem; font-size: 1rem; }}
        .icon-sm, .hgi-stroke.icon-sm {{ width: 1.125rem; height: 1.125rem; font-size: 1.125rem; }}
        .icon-md, .hgi-stroke.icon-md {{ width: 1.375rem; height: 1.375rem; font-size: 1.375rem; }}
        .icon-lg, .hgi-stroke.icon-lg {{ width: 1.75rem; height: 1.75rem; font-size: 1.75rem; }}

        .mobile-nav-icon,
        .hgi-stroke.mobile-nav-icon {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            font-size: 22px;
            line-height: 1;
            transition: transform 0.15s ease;
            font-style: normal;
        }}

        .scroll-to-top-btn i,
        .scroll-to-top-btn .icon {{
            font-size: 24px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }}

        .q-item.is-open .chevron-icon,
        .checklist-card.is-open .chk-chevron {{
            transform: rotate(180deg);
        }}
        .chevron-icon,
        .chk-chevron {{
            transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        /* ----------------------------------------------------
           STICKY NAVBAR (AUTO-HIDE ON SCROLL DOWN, SHOW ON UPSCROLL)
           ---------------------------------------------------- */
        .header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background-color: var(--card);
            box-shadow: var(--shadow-sm);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, box-shadow 0.2s ease;
            will-change: transform;
            padding-top: env(safe-area-inset-top, 0px);
        }}

        .header.header-hidden {{
            transform: translateY(-100%);
            box-shadow: none;
            pointer-events: none;
        }}

        .nav {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 60px;
            gap: 1rem;
        }}

        @media (max-width: 768px) {{
            .nav {{
                height: 52px;
                gap: 0.5rem;
            }}
            .header .nav-links {{
                display: none !important;
            }}
            .brand-title {{
                font-size: 0.95rem;
                max-width: calc(100vw - 110px);
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }}
            .app-page-view {{
                padding: 1rem 0 2.5rem !important;
            }}
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-shrink: 0;
            white-space: nowrap;
            text-decoration: none;
            cursor: pointer;
        }}

        .brand-badge {{
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
            font-size: var(--font-size-overline);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 0.3rem 0.6rem;
            border-radius: var(--radius-sm);
            flex-shrink: 0;
        }}

        .brand-title {{
            font-size: 1.0625rem;
            font-weight: 700;
            color: var(--foreground);
            letter-spacing: -0.015em;
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 0.35rem;
            list-style: none;
            overflow-x: auto;
            scrollbar-width: none;
        }}

        .nav-links::-webkit-scrollbar {{
            display: none;
        }}

        .nav-link-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.5rem 0.85rem;
            background-color: transparent;
            color: var(--muted-foreground);
            font-size: 0.875rem;
            font-weight: 500;
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
            text-decoration: none;
        }}

        .nav-link-btn:hover {{
            color: var(--foreground);
            background-color: var(--secondary);
        }}

        .nav-link-btn.active {{
            background-color: var(--secondary);
            color: var(--foreground);
            font-weight: 600;
        }}

        .nav-badge {{
            font-size: 0.71875rem;
            font-weight: 600;
            padding: 0.15rem 0.45rem;
            border-radius: var(--radius-full);
            background-color: var(--secondary);
            color: var(--muted-foreground);
            line-height: 1.2;
            font-variant-numeric: tabular-nums;
        }}

        .nav-link-btn.active .nav-badge {{
            background-color: var(--card);
            color: var(--foreground);
        }}

        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-shrink: 0;
        }}

        .theme-toggle-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            background-color: var(--secondary);
            color: var(--foreground);
            border-radius: var(--radius-md);
            cursor: pointer;
            transition: background-color 0.15s ease;
        }}

        .theme-toggle-btn:hover {{
            background-color: var(--secondary-hover);
        }}

        /* ----------------------------------------------------
           2023 VISIBILITY TOGGLE (HEADER NAVBAR & CONTROL PANEL)
           ---------------------------------------------------- */
        .year-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            height: 38px;
            padding: 0 0.85rem;
            background-color: var(--secondary);
            color: var(--foreground);
            border: none;
            border-radius: var(--radius-full);
            cursor: pointer;
            font-size: var(--font-size-small);
            font-weight: 500;
            transition: background-color 0.2s ease, transform 0.15s ease;
            user-select: none;
            white-space: nowrap;
        }}

        .year-toggle-btn:hover {{
            background-color: var(--secondary-hover);
        }}

        .year-toggle-btn:active {{
            transform: scale(0.97);
        }}

        .panel-year-toggle-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.25rem 0.65rem;
            background-color: var(--secondary);
            color: var(--foreground);
            border: none;
            border-radius: var(--radius-full);
            cursor: pointer;
            font-size: 0.75rem;
            font-weight: 500;
            transition: background-color 0.15s ease, transform 0.1s ease;
            user-select: none;
            white-space: nowrap;
            height: 30px;
            box-sizing: border-box;
            line-height: 1;
        }}

        .panel-year-toggle-btn:hover {{
            background-color: var(--secondary-hover);
        }}

        .panel-year-toggle-btn:active {{
            transform: scale(0.97);
        }}

        .toggle-switch-track {{
            display: inline-flex;
            align-items: center;
            width: 24px;
            height: 14px;
            background-color: var(--muted-foreground);
            border-radius: var(--radius-full);
            padding: 2px;
            transition: background-color 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
            position: relative;
            opacity: 0.45;
            flex-shrink: 0;
            box-sizing: border-box;
        }}

        .year-toggle-btn.is-active .toggle-switch-track,
        .panel-year-toggle-btn.is-active .toggle-switch-track {{
            background-color: var(--pastel-lavender-foreground);
            opacity: 1;
        }}

        .toggle-switch-thumb {{
            display: block;
            width: 10px;
            height: 10px;
            background-color: var(--card);
            border-radius: var(--radius-full);
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
            transform: translateX(0);
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .year-toggle-btn.is-active .toggle-switch-thumb,
        .panel-year-toggle-btn.is-active .toggle-switch-thumb {{
            transform: translateX(10px);
        }}

        .year-toggle-text {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.75rem;
            line-height: 1;
        }}


        /* ----------------------------------------------------
           SCROLL TO TOP (FLOATING ACTION BUTTON)
           ---------------------------------------------------- */
        .scroll-to-top-btn {{
            position: fixed !important;
            bottom: 2rem !important;
            right: 2rem !important;
            z-index: 99999 !important;
            width: 48px;
            height: 48px;
            border-radius: var(--radius-full);
            background-color: var(--primary);
            color: var(--primary-foreground);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28);
            display: inline-flex !important;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0.95;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s ease, opacity 0.2s ease, box-shadow 0.2s ease;
        }}

        .scroll-to-top-btn:hover {{
            opacity: 1;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        }}

        .scroll-to-top-btn:active {{
            transform: translateY(0) scale(0.96);
        }}

        .scroll-to-top-btn svg {{
            width: 22px;
            height: 22px;
            stroke-width: 2.5;
            stroke: currentColor;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}

        @media (max-width: 768px) {{
            .scroll-to-top-btn {{
                bottom: calc(72px + env(safe-area-inset-bottom, 0px)) !important;
                right: 1.25rem !important;
                width: 42px !important;
                height: 42px !important;
            }}
            .scroll-to-top-btn svg {{
                width: 20px !important;
                height: 20px !important;
            }}
        }}

        .nav-link-timetable:hover {{
            background-color: var(--pastel-peach-bg);
            color: var(--pastel-peach-foreground);
        }}

        /* ----------------------------------------------------
           PAGE VIEWS (MULTI-VIEW TABBED APPLICATION)
           ---------------------------------------------------- */
        .app-page-view {{
            display: none;
            padding: 1.75rem 0 3rem;
        }}

        .app-page-view.active {{
            display: block;
        }}

        .page-header-row {{
            margin-bottom: 1.5rem;
        }}

        .page-title {{
            font-size: clamp(1.75rem, 2.8vw, 2.25rem);
            font-weight: 700;
            color: var(--foreground);
            letter-spacing: -0.02em;
            margin-bottom: 0;
        }}

        .page-subtitle {{
            font-size: 0.9375rem;
            line-height: 1.55;
            color: var(--muted-foreground);
            max-width: 900px;
        }}

        /* ----------------------------------------------------
           TABLES & STRUCTURED CONTAINERS
           ---------------------------------------------------- */
        .table-responsive-wrapper {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            overflow-x: auto;
            box-shadow: var(--shadow-sm);
        }}

        .master-data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.96875rem;
            line-height: 1.6;
            text-align: left;
        }}

        .master-data-table th {{
            background-color: var(--table-header-bg);
            color: var(--foreground);
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 0.875rem 1.25rem;
            white-space: nowrap;
        }}

        .master-data-table td {{
            padding: 1rem 1.25rem;
            color: var(--foreground);
            vertical-align: top;
            background-color: var(--card);
        }}

        .master-data-table tr:hover td {{
            background-color: var(--table-row-hover);
        }}

        .formula-chip {{
            display: inline-block;
            font-family: var(--font-family-mono);
            font-size: 0.8125rem;
            background-color: var(--secondary);
            color: var(--foreground);
            padding: 0.2rem 0.5rem;
            border-radius: var(--radius-sm);
            margin: 0.125rem 0.25rem 0.125rem 0;
            line-height: 1.4;
        }}

        /* ----------------------------------------------------
           STRUCTURED BULLETED LISTS FOR HIGH READABILITY
           (ZERO RUN-ON CONTINUOUS TEXT ACROSS TABLES & CARDS)
           ---------------------------------------------------- */
        .table-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
        }}

        .table-list li {{
            position: relative;
            padding-left: 1.15rem;
            font-size: 0.90625rem;
            line-height: 1.5;
            color: var(--foreground);
        }}

        .table-list li::before {{
            content: "•";
            position: absolute;
            left: 0.1rem;
            top: -0.05rem;
            color: var(--muted-foreground);
            font-size: 1.1rem;
            line-height: 1.5;
        }}

        .table-list-compact {{
            gap: 0.3rem;
        }}

        .table-list-compact li {{
            font-size: 0.84375rem;
            line-height: 1.4;
            white-space: nowrap;
        }}

        .formula-chip-sm {{
            display: inline-block;
            font-family: var(--font-family-mono);
            font-size: 0.8125rem;
            background-color: var(--secondary);
            color: var(--foreground);
            padding: 0.1rem 0.4rem;
            border-radius: var(--radius-sm);
            line-height: 1.35;
            vertical-align: middle;
        }}

        .note-highlight {{
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.15rem 0.5rem;
            border-radius: var(--radius-sm);
            background-color: var(--pastel-amber-bg);
            color: var(--pastel-amber-foreground);
            line-height: 1.3;
        }}

        .note-highlight-green {{
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
        }}

        

        .sol-item-num {{
            font-weight: 600;
            color: var(--foreground);
            display: inline-block;
            margin-right: 0.25rem;
        }}

        .sol-text-block {{
            margin-bottom: 0.35rem;
            line-height: 1.6;
        }}

        /* Clean badges */
        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.75rem;
            font-weight: 600;
            padding: 0.25rem 0.55rem;
            border-radius: var(--radius-full);
            white-space: nowrap;
            letter-spacing: 0.01em;
            line-height: 1.2;
            transition: background-color 0.2s ease, color 0.2s ease;
        }}

        .badge-unit-1 {{ background-color: var(--pastel-sky-bg); color: var(--pastel-sky-foreground); }}
        .badge-unit-2 {{ background-color: var(--pastel-lavender-bg); color: var(--pastel-lavender-foreground); }}
        .badge-unit-3 {{ background-color: var(--pastel-peach-bg); color: var(--pastel-peach-foreground); }}
        .badge-unit-4 {{ background-color: var(--pastel-sage-bg); color: var(--pastel-sage-foreground); }}
        .badge-unit-5 {{ background-color: var(--pastel-rose-bg); color: var(--pastel-rose-foreground); }}
        .badge-subtle {{ background-color: var(--secondary); color: var(--muted-foreground); }}
        .badge-year {{ background-color: var(--pastel-sand-bg); color: var(--pastel-sand-foreground); }}
        .badge-year-2025 {{ background-color: var(--pastel-sage-bg); color: var(--pastel-sage-foreground); }}
        .badge-year-2024 {{ background-color: var(--pastel-sky-bg); color: var(--pastel-sky-foreground); }}
        .badge-year-2023 {{ background-color: var(--pastel-lavender-bg); color: var(--pastel-lavender-foreground); }}
        .badge-year-2022 {{ background-color: var(--pastel-sand-bg); color: var(--pastel-sand-foreground); }}
        .badge-repeat-4x {{ background-color: var(--pastel-rose-bg); color: var(--pastel-rose-foreground); font-weight: 700; }}
        .badge-repeat-3x {{ background-color: var(--pastel-sky-bg); color: var(--pastel-sky-foreground); font-weight: 700; }}
        .badge-repeat-2x {{ background-color: var(--pastel-lavender-bg); color: var(--pastel-lavender-foreground); font-weight: 700; }}
        .badge-completed {{
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
        }}

        /* ----------------------------------------------------
           MINIMAL GRID-BASED CONTROL BAR
           ---------------------------------------------------- */
        .control-panel {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 0.85rem 1.15rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}

        /* TOP TOOLBAR: SEARCH & RESET */
        .control-panel-toolbar {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            width: 100%;
        }}

        .search-box-wrapper {{
            position: relative;
            flex: 1;
            min-width: 200px;
        }}

        .search-input {{
            width: 100%;
            background-color: var(--input-bg);
            border-radius: var(--radius-full);
            padding: 0.4rem 2.2rem 0.4rem 2.2rem;
            font-size: 0.8125rem;
            color: var(--foreground);
            height: 32px;
            box-sizing: border-box;
            transition: background-color 0.15s ease, box-shadow 0.15s ease;
        }}

        .search-input:focus {{
            background-color: var(--card);
            box-shadow: 0 0 0 2px var(--secondary-hover);
        }}

        .search-icon {{
            position: absolute;
            left: 0.75rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted-foreground);
            pointer-events: none;
        }}

        .search-kbd-hint {{
            position: absolute;
            right: 0.65rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 0.6875rem;
            font-family: var(--font-family-mono);
            color: var(--muted-foreground);
            background-color: var(--secondary);
            padding: 0.12rem 0.4rem;
            border-radius: var(--radius-sm);
            pointer-events: none;
            line-height: 1;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            transition: opacity 0.15s ease;
        }}

        .search-input:focus ~ .search-kbd-hint,
        .search-input:not(:placeholder-shown) ~ .search-kbd-hint {{
            opacity: 0;
            pointer-events: none;
        }}

        .search-clear-btn {{
            position: absolute;
            right: 0.5rem;
            top: 50%;
            transform: translateY(-50%);
            background: transparent;
            color: var(--muted-foreground);
            cursor: pointer;
            padding: 0.2rem;
            border-radius: var(--radius-full);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: color 0.15s ease, background-color 0.15s ease;
        }}

        .search-clear-btn:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        .reset-filters-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            padding: 0.25rem 0.65rem;
            background-color: var(--secondary);
            color: var(--muted-foreground);
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.15s ease, color 0.15s ease, transform 0.1s ease;
            white-space: nowrap;
            height: 32px;
            box-sizing: border-box;
            line-height: 1;
            flex-shrink: 0;
        }}

        .reset-filters-btn:hover {{
            background-color: var(--secondary-hover);
            color: var(--foreground);
        }}

        .reset-filters-btn:active {{
            transform: scale(0.97);
        }}

        .control-panel-actions {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            margin-left: auto;
            flex-wrap: wrap;
        }}

        .filter-pills-row {{
            display: inline-flex;
            align-items: center;
            gap: 2px;
        }}

        /* ----------------------------------------------------
           PROPER CSS GRID SYSTEM FOR FILTERS (RESPONSIVE)
           ---------------------------------------------------- */
        .control-panel-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.65rem 1.25rem;
            width: 100%;
        }}

        .filter-grid-cell {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            min-width: 0;
        }}

        .filter-grid-label {{
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
            user-select: none;
            white-space: nowrap;
            flex-shrink: 0;
            width: 62px;
        }}

        .filter-pill-group {{
            display: inline-flex;
            align-items: center;
            gap: 2px;
            background-color: var(--secondary);
            padding: 2.5px 3px;
            border-radius: var(--radius-full);
            min-width: 0;
            overflow-x: auto;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }}

        .filter-pill-group::-webkit-scrollbar {{
            display: none;
        }}

        .filter-pill-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.25rem;
            padding: 0.22rem 0.55rem;
            background: transparent;
            color: var(--muted-foreground);
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: color 0.15s ease, background-color 0.15s ease, transform 0.1s ease;
            white-space: nowrap;
            user-select: none;
            line-height: 1.25;
            box-sizing: border-box;
            flex-shrink: 0;
        }}

        .filter-pill-btn:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        .filter-pill-btn:active {{
            transform: scale(0.97);
        }}

        .filter-pill-btn.active {{
            background-color: #ffffff;
            color: var(--foreground);
            font-weight: 600;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
        }}

        [data-theme="dark"] .filter-pill-btn.active {{
            background-color: #27272a;
            color: #fcfcfd;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
        }}

        .filter-pill-btn .nav-badge {{
            font-size: 0.7rem;
            padding: 0.1rem 0.35rem;
            border-radius: var(--radius-full);
            background-color: var(--secondary);
            color: var(--muted-foreground);
            line-height: 1;
            font-variant-numeric: tabular-nums;
            margin-left: 0.15rem;
        }}

        .filter-pill-btn.active .nav-badge {{
            background-color: var(--card);
            color: var(--foreground);
        }}

        [data-theme="dark"] .filter-pill-btn.active .nav-badge {{
            background-color: #18181b;
            color: #fcfcfd;
        }}



        @media (max-width: 1100px) {{
            .control-panel-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 0.6rem 1rem;
            }}
        }}

        @media (max-width: 680px) {{
            .control-panel {{
                padding: 0.75rem 0.85rem;
                gap: 0.65rem;
            }}

            .control-panel-grid {{
                grid-template-columns: 1fr;
                gap: 0.5rem;
            }}

            .filter-grid-label {{
                width: 58px;
            }}
        }}

        .search-clear-btn:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        .complete-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.25rem 0.65rem;
            background-color: var(--secondary);
            color: var(--muted-foreground);
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            user-select: none;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}

        .complete-btn:hover {{
            background-color: var(--secondary-hover);
            color: var(--foreground);
        }}

        .complete-btn.is-completed {{
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
            font-weight: 600;
        }}

        .complete-btn .check-icon {{
            width: 13px;
            height: 13px;
            stroke-width: 2.5;
        }}

        .q-item.is-completed {{
            background-color: var(--card);
        }}

        .q-item.is-open .badge-completed {{
            background-color: var(--pastel-sage-bg) !important;
            color: var(--pastel-sage-foreground) !important;
        }}

        .icon-action-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
            padding: 0;
            background-color: var(--secondary);
            color: var(--muted-foreground);
            border-radius: var(--radius-full);
            cursor: pointer;
            user-select: none;
            transition: all 0.15s ease;
            flex-shrink: 0;
        }}

        .icon-action-btn:hover {{
            background-color: var(--secondary-hover);
            color: var(--foreground);
            transform: scale(1.08);
        }}

        .icon-action-btn:active {{
            transform: scale(0.92);
        }}

        .icon-action-btn.star-action-btn.is-starred {{
            background-color: var(--pastel-amber-bg);
            color: var(--pastel-amber-foreground);
        }}

        .icon-action-btn.star-action-btn.is-starred .star-icon {{
            fill: currentColor;
            stroke: currentColor;
        }}

        .icon-action-btn.later-action-btn.is-later {{
            background-color: var(--pastel-lavender-bg);
            color: var(--pastel-lavender-foreground);
        }}

        .icon-action-btn.later-action-btn.is-later .clock-icon {{
            stroke-width: 2.5;
        }}

        .q-item.is-later {{
            opacity: 0.65;
        }}

        .q-item.is-later:hover {{
            opacity: 1;
        }}

        .checklist-card.is-later {{
            opacity: 0.65;
        }}

        .checklist-card.is-later:hover {{
            opacity: 1;
        }}

        .note-action-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
            padding: 0;
            background-color: var(--secondary);
            color: var(--muted-foreground);
            border-radius: var(--radius-full);
            cursor: pointer;
            user-select: none;
            transition: all 0.15s ease;
            position: relative;
            flex-shrink: 0;
        }}

        .note-action-btn:hover {{
            background-color: var(--secondary-hover);
            color: var(--foreground);
            transform: scale(1.08);
        }}

        .note-action-btn:active {{
            transform: scale(0.92);
        }}

        .note-action-btn.has-note {{
            background-color: var(--pastel-sky-bg);
            color: var(--pastel-sky-foreground);
        }}

        .note-action-btn .pen-icon {{
            width: 13px;
            height: 13px;
            stroke-width: 2.2;
        }}

        .note-indicator-dot {{
            position: absolute;
            top: 2px;
            right: 2px;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background-color: currentColor;
            display: inline-block;
        }}

        /* ----------------------------------------------------
           QUESTIONS ENGINE: CLICK-TO-OPEN CARD (NO TOGGLE BUTTON)
           CONSTRAINED OPTIMAL READING MEASURE (NO RUNAWAY WIDE LINES)
           ---------------------------------------------------- */
        .questions-list-wrapper {{
            display: flex;
            flex-direction: column;
            gap: 0.875rem;
        }}

        /* SECTION DISTINCTION & SPACER FOR REPEATED QUESTION GROUPS */
        .q-section-spacer {{
            height: 2.5rem;
            width: 100%;
        }}

        .q-tier-section-divider {{
            margin-top: 3.5rem;
            margin-bottom: 1.25rem;
            padding-top: 0.5rem;
        }}

        .q-tier-section-divider.first-tier {{
            margin-top: 0.75rem;
        }}

        .q-tier-section-title {{
            display: inline-flex;
            align-items: center;
            gap: 0.85rem;
            background-color: var(--card);
            padding: 0.6rem 1.25rem;
            border-radius: var(--radius-pill);
            user-select: none;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}

        .q-tier-section-title .card-overline {{
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--foreground);
            letter-spacing: 0.02em;
        }}

        .q-unit-section-divider {{
            margin-top: 2rem;
            margin-bottom: 0.75rem;
            padding-top: 0.25rem;
        }}

        .q-unit-section-title {{
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            background-color: var(--secondary);
            padding: 0.45rem 1rem;
            border-radius: var(--radius-pill);
            user-select: none;
        }}

        .q-unit-section-title .card-overline {{
            font-size: 0.75rem;
            color: var(--muted-foreground);
        }}

        .q-topic-section-header {{
            margin-top: 2.25rem;
            margin-bottom: 0.5rem;
            padding: 0 0.25rem;
        }}

        .q-topic-section-header.first-section {{
            margin-top: 1rem;
        }}

        .q-topic-section-meta {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin-bottom: 0.35rem;
        }}

        .q-topic-section-title {{
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--foreground);
            line-height: 1.4;
            margin: 0;
        }}

        .q-item {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 1.6rem 2rem;
            box-shadow: var(--shadow-sm);
            cursor: pointer;
            user-select: none;
            transition: background-color 0.15s ease, box-shadow 0.15s ease;
        }}

        .q-item:hover {{
            box-shadow: var(--shadow-md);
        }}

        .q-item.is-open {{
            background-color: transparent;
            box-shadow: none;
        }}

        .q-item.is-open:hover {{
            background-color: transparent;
            box-shadow: none;
        }}

        .q-item-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            margin-bottom: 0.75rem;
            flex-wrap: wrap;
        }}

        .q-item-left-meta {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            row-gap: 0.35rem;
            flex-wrap: wrap;
            flex: 1;
            min-width: 0;
        }}

        .q-item-qno {{
            font-size: 0.8125rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            color: var(--muted-foreground);
            background-color: var(--secondary);
            padding: 0.22rem 0.65rem;
            border-radius: var(--radius-sm);
            line-height: 1.25;
            display: inline-flex;
            align-items: center;
        }}

        .q-item.is-open .q-item-qno {{
            background-color: var(--secondary);
            color: var(--foreground);
        }}

        .q-item-right-meta {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-left: auto;
            flex-wrap: wrap;
        }}

        .q-item-badges {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
            flex-wrap: wrap;
        }}

        .q-item-actions {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .chevron-icon {{
            transition: transform 0.2s ease;
            color: var(--muted-foreground);
        }}

        /* WHEN ANSWER IS OPEN:
           1. HIDE/MUTE BADGE COLORS
           2. ROTATE CHEVRON ICON
        */
        .q-item.is-open .badge {{
            background-color: var(--secondary) !important;
            color: var(--muted-foreground) !important;
        }}

        .q-item.is-open .chevron-icon {{
            transform: rotate(180deg);
            color: var(--foreground);
        }}

        .q-item-title {{
            font-size: 1.0625rem;
            font-weight: 600;
            color: var(--foreground);
            line-height: 1.55;
            margin-bottom: 0;
            max-width: 1040px; /* Constrained readable measure */
        }}

        .q-item.is-open .q-item-title {{
            margin-bottom: 0.65rem;
        }}

        .sol-header-banner {{
            margin-bottom: 0.85rem;
            padding-bottom: 0.4rem;
        }}

        /* READABLE, CONSTRAINED ANSWER UI (NO RUNAWAY WIDE LINES) */
        .q-solution-content {{
            display: none;
            padding-top: 1.25rem;
            margin-top: 1rem;
            cursor: default;
            user-select: text; /* Allow text selection inside open answer */
        }}

        .q-solution-content.open {{
            display: block;
        }}

        /* SOLUTION VIEW TOGGLE TOOLBAR (SWITCH BETWEEN VERIFIED SOLUTION & MY ANSWER) */
        .sol-view-switch-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--secondary);
            flex-wrap: wrap;
        }}

        .sol-view-pills {{
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            background-color: var(--secondary);
            padding: 3px;
            border-radius: var(--radius-full);
        }}

        .sol-view-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.28rem 0.75rem;
            font-size: 0.78rem;
            font-weight: 500;
            color: var(--muted-foreground);
            background: transparent;
            border: none;
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: all 0.15s ease;
            user-select: none;
        }}

        .sol-view-pill:hover {{
            color: var(--foreground);
        }}

        .sol-view-pill.active {{
            background-color: var(--filter-pill-active-bg);
            color: var(--filter-pill-active-fg);
            font-weight: 600;
            box-shadow: var(--filter-pill-active-shadow);
        }}

        .sol-view-quick-actions {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .sol-btn-edit-note {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.28rem 0.7rem;
            font-size: 0.76rem;
            font-weight: 500;
            color: var(--foreground);
            background-color: var(--secondary);
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: all 0.15s ease;
            user-select: none;
        }}

        .sol-btn-edit-note:hover {{
            background-color: var(--secondary-hover);
        }}

        /* USER CUSTOM ANSWER PANE (MINE) */
        .my-answer-container {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.5rem;
            position: relative;
        }}

        .my-answer-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.85rem;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        .my-answer-meta {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .my-answer-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 0.18rem 0.55rem;
            border-radius: var(--radius-full);
            background-color: var(--pastel-sky-bg);
            color: var(--pastel-sky-foreground);
        }}

        .my-answer-time {{
            font-size: 0.75rem;
            color: var(--muted-foreground);
        }}

        .my-answer-actions {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .my-answer-btn-action {{
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.2rem 0.55rem;
            font-size: 0.74rem;
            font-weight: 500;
            color: var(--muted-foreground);
            background-color: var(--secondary);
            border-radius: var(--radius-sm);
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .my-answer-btn-action:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        .my-answer-btn-action.btn-delete:hover {{
            color: #ef4444;
            background-color: rgba(239, 68, 68, 0.12);
        }}

        .my-answer-text {{
            font-size: var(--font-size-body-medium);
            line-height: 1.7;
            color: var(--foreground);
            word-break: break-word;
        }}

        .my-answer-text p,
        .my-answer-p {{
            margin-bottom: 0.85rem;
            line-height: 1.7;
            color: var(--foreground);
        }}

        .my-answer-text p:last-child,
        .my-answer-p:last-child {{
            margin-bottom: 0;
        }}

        .my-answer-heading {{
            font-weight: 700;
            color: var(--foreground);
            margin-top: 1.4rem;
            margin-bottom: 0.65rem;
            display: block;
            letter-spacing: -0.015em;
        }}

        .my-answer-heading:first-child {{
            margin-top: 0;
        }}

        .my-answer-heading.h1,
        .my-answer-heading.h2 {{
            font-size: 1.15rem;
            line-height: 1.45;
            color: var(--foreground);
            padding-bottom: 0.45rem;
            border-bottom: 1px solid var(--border);
        }}

        .my-answer-heading.h3 {{
            font-size: 1.05rem;
            line-height: 1.4;
            color: var(--foreground);
            margin-top: 1.35rem;
        }}

        .my-answer-heading.h4 {{
            font-size: 0.92rem;
            line-height: 1.4;
            color: var(--muted-foreground);
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }}

        /* TABLE CONTAINER & STYLING */
        .my-answer-table-wrapper {{
            width: 100%;
            overflow-x: auto;
            margin: 1rem 0 1.5rem;
            border-radius: var(--radius-md);
            background-color: var(--card);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
            border: 1px solid var(--border);
            -webkit-overflow-scrolling: touch;
        }}

        .my-answer-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.875rem;
            line-height: 1.6;
            text-align: left;
            table-layout: fixed;
        }}

        .my-answer-table thead tr {{
            background-color: var(--secondary);
            border-bottom: 1px solid var(--border);
        }}

        .my-answer-table th {{
            padding: 0.85rem 1.15rem;
            font-weight: 600;
            font-size: 0.8125rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
            border-bottom: 1px solid var(--border);
            word-wrap: break-word;
            overflow-wrap: break-word;
        }}

        .my-answer-table td {{
            padding: 0.85rem 1.15rem;
            color: var(--foreground);
            font-weight: 400;
            vertical-align: top;
            border-bottom: 1px solid var(--border);
            word-wrap: break-word;
            overflow-wrap: break-word;
        }}

        .my-answer-table tbody tr:last-child td {{
            border-bottom: none;
        }}

        .my-answer-table tbody tr:nth-child(even) {{
            background-color: var(--table-row-alt, var(--secondary));
        }}

        .my-answer-table tbody tr:hover {{
            background-color: var(--table-row-hover, var(--secondary-hover));
        }}

        .my-answer-table td strong {{
            color: var(--foreground);
            font-weight: 600;
        }}

        /* LIST ITEMS INSIDE MY ANSWER */
        .my-answer-text .sol-item-row {{
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            margin-bottom: 0.65rem;
            line-height: 1.65;
        }}

        .my-answer-text .sol-item-row:last-child {{
            margin-bottom: 0;
        }}

        .my-answer-text .sol-item-num {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 1.5rem;
            height: 1.5rem;
            border-radius: var(--radius-sm);
            background-color: var(--secondary);
            color: var(--foreground);
            font-weight: 700;
            font-size: 0.8rem;
            flex-shrink: 0;
            margin-top: 0.15rem;
            line-height: 1;
        }}

        .my-answer-text .sol-item-content {{
            flex: 1;
            min-width: 0;
            color: var(--foreground);
        }}

        .my-answer-text .sol-item-content strong {{
            color: var(--foreground);
            font-weight: 700;
        }}

        /* NOTE BOX CALLOUT */
        .sol-note-box {{
            margin: 1.25rem 0 0.5rem;
            padding: 0.85rem 1.1rem;
            border-radius: var(--radius-md);
            background-color: var(--pastel-peach-bg);
            border-left: 3px solid var(--pastel-peach-foreground);
            display: flex;
            gap: 0.75rem;
            align-items: flex-start;
        }}

        .sol-note-box .note-tag {{
            font-weight: 700;
            color: var(--pastel-peach-foreground);
            text-transform: uppercase;
            font-size: 0.72rem;
            letter-spacing: 0.05em;
            padding: 0.15rem 0.5rem;
            border-radius: var(--radius-sm);
            background-color: var(--card);
            flex-shrink: 0;
            margin-top: 0.1rem;
        }}

        .sol-note-box .sol-note-text {{
            flex: 1;
            color: var(--foreground);
            font-size: 0.875rem;
            line-height: 1.6;
        }}

        .my-answer-empty {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 2rem 1rem;
            background-color: var(--secondary);
            border-radius: var(--radius-lg);
            gap: 0.75rem;
        }}

        .my-answer-empty-title {{
            font-size: 1rem;
            font-weight: 600;
            color: var(--foreground);
        }}

        .my-answer-empty-desc {{
            font-size: 0.85rem;
            color: var(--muted-foreground);
            max-width: 480px;
            line-height: 1.5;
        }}

        .my-answer-empty-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.45rem 1rem;
            font-size: 0.82rem;
            font-weight: 600;
            background-color: var(--primary);
            color: var(--primary-foreground);
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: all 0.15s ease;
            margin-top: 0.25rem;
        }}

        .my-answer-empty-btn:hover {{
            transform: scale(1.02);
            opacity: 0.95;
        }}

        /* INLINE NOTE EDITOR */
        .note-editor-container {{
            background-color: var(--secondary);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.5rem;
            margin-top: 0.5rem;
        }}

        .note-editor-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        .note-editor-title {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--foreground);
        }}

        .note-editor-meta {{
            font-size: 0.75rem;
            color: var(--muted-foreground);
        }}

        .note-editor-hint {{
            font-size: 0.8rem;
            color: var(--muted-foreground);
            margin-bottom: 0.75rem;
            line-height: 1.45;
        }}

        .note-editor-textarea {{
            width: 100%;
            min-height: 160px;
            padding: 0.85rem 1rem;
            font-family: inherit;
            font-size: 0.92rem;
            line-height: 1.65;
            color: var(--foreground);
            background-color: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            resize: vertical;
            outline: none;
            transition: border-color 0.15s ease, box-shadow 0.15s ease;
            box-sizing: border-box;
        }}

        .note-editor-textarea:focus {{
            border-color: var(--foreground);
            box-shadow: 0 0 0 2px rgba(100, 116, 139, 0.2);
        }}

        .note-editor-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 0.75rem;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}

        .note-editor-keys {{
            font-size: 0.75rem;
            color: var(--muted-foreground);
        }}

        .note-editor-keys kbd {{
            background-color: var(--card);
            padding: 0.15rem 0.35rem;
            border-radius: 4px;
            font-size: 0.72rem;
            font-family: var(--font-family-mono);
            border: 1px solid var(--border);
        }}

        .note-editor-buttons {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            margin-left: auto;
        }}

        .note-btn-cancel {{
            padding: 0.4rem 0.85rem;
            font-size: 0.8rem;
            font-weight: 500;
            color: var(--muted-foreground);
            background-color: transparent;
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .note-btn-cancel:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        .note-btn-save {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.4rem 1rem;
            font-size: 0.8rem;
            font-weight: 600;
            background-color: var(--primary);
            color: var(--primary-foreground);
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .note-btn-save:hover {{
            transform: scale(1.02);
            opacity: 0.95;
        }}

        /* APP GLOBAL TOAST NOTIFICATION */
        .app-global-toast {{
            position: fixed;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%) translateY(100px);
            background-color: var(--foreground);
            color: var(--background);
            padding: 0.6rem 1.25rem;
            border-radius: var(--radius-full);
            font-size: 0.84rem;
            font-weight: 600;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
            z-index: 999999;
            pointer-events: none;
            opacity: 0;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .app-global-toast.visible {{
            transform: translateX(-50%) translateY(0);
            opacity: 1;
        }}

        /* ----------------------------------------------------
           PAGE VIEW: NOTES & CUSTOM ANSWERS ARCHIVE
           ---------------------------------------------------- */
        .general-scratchpad-card {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-sm);
        }}

        .scratchpad-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 0.85rem;
            flex-wrap: wrap;
        }}

        .scratchpad-title-wrap {{
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
        }}

        .scratchpad-title-wrap .icon {{
            color: var(--foreground);
            margin-top: 2px;
        }}

        .scratchpad-title {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--foreground);
            margin: 0 0 0.2rem 0;
        }}

        .scratchpad-subtitle {{
            font-size: 0.82rem;
            color: var(--muted-foreground);
            margin: 0;
            line-height: 1.45;
        }}

        .scratchpad-status {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.75rem;
            color: var(--muted-foreground);
            background-color: var(--secondary);
            padding: 0.2rem 0.6rem;
            border-radius: var(--radius-full);
            white-space: nowrap;
        }}

        .scratchpad-status .status-indicator {{
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background-color: #22c55e;
        }}

        .scratchpad-textarea {{
            width: 100%;
            min-height: 120px;
            padding: 0.85rem 1rem;
            font-family: inherit;
            font-size: 0.92rem;
            line-height: 1.65;
            color: var(--foreground);
            background-color: var(--secondary);
            border: 1px solid transparent;
            border-radius: var(--radius-md);
            resize: vertical;
            outline: none;
            transition: all 0.15s ease;
            box-sizing: border-box;
        }}

        .scratchpad-textarea:focus {{
            border-color: var(--foreground);
            background-color: var(--card);
            box-shadow: 0 0 0 2px rgba(100, 116, 139, 0.2);
        }}

        .notes-filter-toolbar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 1.25rem;
            flex-wrap: wrap;
        }}

        .notes-search-box {{
            position: relative;
            flex: 1;
            min-width: 260px;
            max-width: 420px;
        }}

        .notes-search-icon {{
            position: absolute;
            left: 0.85rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted-foreground);
            pointer-events: none;
        }}

        .notes-search-input {{
            width: 100%;
            height: 38px;
            padding: 0 1rem 0 2.4rem;
            border-radius: var(--radius-full);
            background-color: var(--secondary);
            color: var(--foreground);
            font-size: 0.85rem;
            border: 1px solid transparent;
            outline: none;
            transition: all 0.15s ease;
            box-sizing: border-box;
        }}

        .notes-search-input:focus {{
            background-color: var(--card);
            border-color: var(--foreground);
        }}

        .notes-unit-pills {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background-color: var(--secondary);
            padding: 3px;
            border-radius: var(--radius-full);
            overflow-x: auto;
            max-width: 100%;
        }}

        .saved-notes-list {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }}

        .saved-note-card {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.5rem;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.15s ease;
        }}

        .saved-note-card:hover {{
            box-shadow: var(--shadow-md);
        }}

        .saved-note-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            margin-bottom: 0.65rem;
            flex-wrap: wrap;
        }}

        .saved-note-meta {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            flex-wrap: wrap;
        }}

        .saved-note-actions {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .saved-note-qtitle {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--foreground);
            margin-bottom: 0.85rem;
            line-height: 1.5;
        }}

        .saved-note-content-box {{
            background-color: var(--secondary);
            border-radius: var(--radius-md);
            padding: 1rem 1.25rem;
            margin-bottom: 0.75rem;
            line-height: 1.7;
            font-size: 0.95rem;
            color: var(--foreground);
            white-space: pre-wrap;
            word-break: break-word;
        }}

        .saved-note-footer {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.5rem;
            font-size: 0.75rem;
            color: var(--muted-foreground);
            flex-wrap: wrap;
        }}

        .solution-body {{
            max-width: 1160px;
            font-size: 1rem;
            line-height: 1.75;
            color: var(--foreground-secondary);
        }}

        .sol-heading {{
            font-size: 1.0625rem;
            font-weight: 700;
            color: var(--foreground);
            margin-top: 0.85rem;
            margin-bottom: 0.65rem;
            line-height: 1.45;
            letter-spacing: -0.01em;
        }}

        .sol-heading:first-child {{
            margin-top: 0;
        }}

        .sol-body-text {{
            font-size: 0.96875rem;
            line-height: 1.75;
            color: var(--foreground-secondary);
            margin-bottom: 0.85rem;
        }}

        /* CLEAN LIST ROWS (NO CARDS, NO BORDER BOXES, NO SHADOWS) */
        .sol-item-row {{
            display: flex;
            align-items: flex-start;
            gap: 0.65rem;
            margin-bottom: 0.85rem;
            line-height: 1.75;
            font-size: 0.96875rem;
        }}

        .sol-item-row:last-child {{
            margin-bottom: 0;
        }}

        .sol-item-num {{
            display: inline-block;
            min-width: 1.4rem;
            font-weight: 600;
            color: var(--foreground);
            flex-shrink: 0;
            line-height: 1.75;
        }}

        .sol-item-content {{
            flex: 1;
            min-width: 0;
            color: var(--foreground-secondary);
        }}

        .sol-item-title {{
            font-weight: 600;
            color: var(--foreground);
            margin-right: 0.25rem;
        }}

        .sol-item-text {{
            color: var(--foreground-secondary);
        }}

        .sol-item-example {{
            margin-top: 0.25rem;
            font-size: 0.90625rem;
            line-height: 1.6;
            color: var(--muted-foreground);
        }}

        .sol-item-example .example-label {{
            font-style: italic;
            font-weight: 500;
            color: var(--foreground);
        }}

        .sol-step {{
            max-width: 1040px;
            margin-bottom: 0.75rem;
            line-height: 1.75;
            font-size: 0.96875rem;
            color: var(--foreground-secondary);
        }}

        .sol-step:last-child {{
            margin-bottom: 0;
        }}

        .sol-step strong {{
            font-weight: 600;
            color: var(--foreground);
        }}

        .sol-step code, .solution-body code {{
            background-color: var(--secondary);
            color: var(--foreground);
            padding: 0.18rem 0.45rem;
            border-radius: var(--radius-sm);
            font-family: var(--font-family-mono);
            font-size: 0.9em;
            line-height: 1.5;
            font-weight: 500;
        }}

        .example-tag {{
            display: inline-block;
            font-size: 0.6875rem;
            font-weight: 600;
            text-transform: none;
            letter-spacing: 0.02em;
            background-color: var(--secondary);
            color: var(--muted-foreground);
            padding: 0.12rem 0.38rem;
            border-radius: var(--radius-sm);
            margin: 0 0.35rem 0 0;
            vertical-align: middle;
            line-height: 1.2;
        }}

        /* SOLUTION DIAGRAMS & ILLUSTRATIONS (THEORY ANSWERS) */
        .sol-diagram-box {{
            margin: 0.85rem 0;
            padding: 1rem 1.15rem;
            background-color: var(--secondary);
            border-radius: var(--radius-md);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow-x: auto;
        }}

        .sol-diagram-title {{
            font-size: 0.78125rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
            margin-bottom: 0.65rem;
            align-self: flex-start;
        }}

        .sol-diagram-svg {{
            max-width: 100%;
            height: auto;
            display: block;
        }}

        /* COMPARISON TABLES IN SOLUTIONS */
        .sol-table-wrap {{
            margin: 0.85rem 0;
            overflow-x: auto;
            border-radius: var(--radius-md);
            background-color: var(--secondary);
        }}

        .sol-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.875rem;
            text-align: left;
        }}

        .sol-table th {{
            background-color: var(--muted);
            color: var(--foreground);
            font-weight: 700;
            padding: 0.65rem 0.85rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .sol-table td {{
            padding: 0.6rem 0.85rem;
            color: var(--foreground-secondary);
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            line-height: 1.5;
        }}

        .sol-table tr:last-child td {{
            border-bottom: none;
        }}

        .is-code-chip {{
            display: inline-flex;
            align-items: center;
            font-size: 0.71875rem;
            font-weight: 700;
            font-family: var(--font-family-mono);
            letter-spacing: 0.02em;
            background-color: var(--muted);
            color: var(--foreground);
            padding: 0.12rem 0.45rem;
            border-radius: var(--radius-sm);
            margin-right: 0.35rem;
            vertical-align: middle;
        }}

        .empty-results {{
            text-align: center;
            padding: 3.5rem 1.5rem;
            background-color: var(--card);
            border-radius: var(--radius-lg);
            color: var(--muted-foreground);
            box-shadow: var(--shadow-sm);
        }}

        /* ----------------------------------------------------
           UNIT-WISE PYQ CHECKLIST STYLING (PURE BACKGROUND SEPARATION)
           ---------------------------------------------------- */
        .checklist-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 1.25rem;
        }}

        .checklist-header-right {{
            display: inline-flex;
            align-items: center;
            gap: 0.65rem;
            flex-wrap: wrap;
        }}

        .checklist-progress-circle {{
            position: relative;
            width: 42px;
            height: 42px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: var(--radius-full);
            background-color: var(--card);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.18), inset 0 1px 0 rgba(255, 255, 255, 0.05);
            cursor: pointer;
            flex-shrink: 0;
            box-sizing: border-box;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease;
            user-select: none;
        }}

        [data-theme="light"] .checklist-progress-circle {{
            background-color: #ffffff;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 2px 6px rgba(0, 0, 0, 0.04);
        }}

        .checklist-progress-circle:hover {{
            transform: translateY(-1px) scale(1.04);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        }}

        [data-theme="light"] .checklist-progress-circle:hover {{
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
        }}

        .checklist-progress-circle:active {{
            transform: translateY(0) scale(0.98);
        }}

        .checklist-progress-ring {{
            position: absolute;
            top: 0;
            left: 0;
            width: 42px;
            height: 42px;
            transform: rotate(-90deg);
            pointer-events: none;
        }}

        .checklist-ring-bg {{
            fill: none;
            stroke: rgba(0, 0, 0, 0.06);
            stroke-width: 3;
        }}

        [data-theme="dark"] .checklist-ring-bg {{
            stroke: rgba(255, 255, 255, 0.08);
        }}

        .checklist-ring-fill {{
            fill: none;
            stroke: var(--pastel-sage-foreground);
            stroke: url(#checklistRingGrad);
            stroke-width: 3;
            stroke-linecap: round;
            stroke-dasharray: 109.96;
            stroke-dashoffset: 109.96;
            transition: stroke-dashoffset 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
        }}

        [data-theme="dark"] .checklist-ring-fill {{
            filter: drop-shadow(0 0 5px rgba(52, 211, 153, 0.45));
        }}

        .checklist-progress-circle.is-complete .checklist-ring-fill {{
            stroke-linecap: butt;
        }}

        [data-theme="dark"] .checklist-progress-circle.is-complete .checklist-ring-fill {{
            filter: drop-shadow(0 0 7px rgba(52, 211, 153, 0.6));
        }}

        .checklist-stat-pct {{
            position: relative;
            z-index: 1;
            display: inline-flex;
            align-items: baseline;
            justify-content: center;
            color: var(--muted-foreground);
            font-variant-numeric: tabular-nums;
            line-height: 1;
            letter-spacing: -0.02em;
            text-align: center;
            white-space: nowrap;
            pointer-events: none;
            transition: color 0.25s ease;
        }}

        .checklist-progress-circle.has-progress .checklist-stat-pct {{
            color: var(--pastel-sage-foreground);
        }}

        .checklist-stat-pct .pct-num {{
            font-size: 0.8125rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            font-family: inherit;
        }}

        .checklist-stat-pct .pct-unit {{
            font-size: 0.5rem;
            font-weight: 600;
            opacity: 0.75;
            margin-left: 0.75px;
            transform: translateY(-0.5px);
        }}

        .checklist-summary-units {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            flex-wrap: wrap;
        }}

        .checklist-year-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.3rem 0.65rem;
            background-color: var(--secondary);
            border-radius: var(--radius-full);
            text-decoration: none;
            cursor: pointer;
            transition: background-color 0.15s ease, transform 0.15s ease;
        }}

        .checklist-year-pill:hover {{
            background-color: var(--secondary-hover);
            transform: translateY(-1px);
        }}

        .unit-pill-count {{
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--foreground);
            font-variant-numeric: tabular-nums;
            line-height: 1;
        }}

        /* CHECKLIST CONTROLS BAR (ZERO BG SEPARATION, MINIMAL FLOW) */
        .checklist-toolbar {{
            background: transparent;
            border-radius: 0;
            padding: 0;
            margin-bottom: 1.5rem;
            box-shadow: none;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.85rem;
            flex-wrap: wrap;
        }}

        .checklist-toolbar-filters {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}

        .checklist-unit-group {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }}

        .checklist-filter-divider {{
            width: 1px;
            height: 18px;
            background-color: var(--border);
            opacity: 0.5;
            margin: 0 0.15rem;
            flex-shrink: 0;
        }}

        .checklist-filter-label {{
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--muted-foreground);
            margin-right: 0.2rem;
            user-select: none;
            white-space: nowrap;
            line-height: 1;
            display: inline-flex;
            align-items: center;
        }}

        .checklist-search-box {{
            position: relative;
            width: 220px;
            max-width: 240px;
            min-width: 180px;
            flex-shrink: 0;
        }}

        .checklist-search-input {{
            width: 100%;
            background-color: var(--input-bg);
            border: none;
            border-radius: var(--radius-full);
            padding: 0.35rem 1.8rem 0.35rem 2rem;
            font-size: 0.8125rem;
            color: var(--foreground);
            height: 32px;
            box-sizing: border-box;
            outline: none;
            transition: background-color 0.15s ease, box-shadow 0.15s ease;
        }}

        .checklist-search-input:focus {{
            background-color: var(--card);
            box-shadow: 0 0 0 2px var(--secondary-hover);
        }}

        .checklist-search-icon {{
            position: absolute;
            left: 0.65rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted-foreground);
            pointer-events: none;
            font-size: 13px;
        }}

        .checklist-search-clear-btn {{
            position: absolute;
            right: 0.45rem;
            top: 50%;
            transform: translateY(-50%);
            background: transparent;
            border: none;
            color: var(--muted-foreground);
            cursor: pointer;
            padding: 0.15rem;
            border-radius: var(--radius-full);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            transition: color 0.15s ease;
        }}

        .checklist-search-clear-btn:hover {{
            color: var(--foreground);
        }}

        /* YEAR GROUPS & SUB-UNITS */
        .checklist-year-group {{
            margin-bottom: 2rem;
        }}

        .checklist-year-units {{
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }}

        .checklist-unit-subgroup {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .checklist-unit-subhead {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            padding: 0.25rem 0.5rem 0.1rem;
        }}

        .checklist-unit-subhead-title {{
            font-size: 0.875rem;
            font-weight: 600;
            color: var(--foreground);
            letter-spacing: -0.01em;
        }}

        .checklist-unit-subhead-count {{
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--muted-foreground);
            font-family: var(--font-family-mono);
            margin-left: auto;
        }}

        .checklist-unit-items {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        /* INDIVIDUAL CHECKLIST ITEM CARD */
        .checklist-card {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 1rem 1.25rem;
            box-shadow: var(--shadow-sm);
            display: flex;
            align-items: flex-start;
            gap: 0.85rem;
            cursor: pointer;
            user-select: none;
            transition: background-color 0.15s ease, box-shadow 0.15s ease;
            position: relative;
        }}

        .checklist-card:hover {{
            box-shadow: var(--shadow-md);
        }}

        .checklist-card.is-open {{
            background-color: transparent;
            box-shadow: none;
            opacity: 1 !important;
        }}

        .checklist-card.is-open:hover {{
            background-color: transparent;
            box-shadow: none;
        }}

        .checklist-card.is-completed {{
            opacity: 0.82;
        }}

        .checklist-card.is-completed .checklist-card-title {{
            color: var(--muted-foreground);
        }}

        .checklist-card.is-completed.is-open {{
            opacity: 1;
        }}

        .checklist-card.is-completed.is-open .checklist-card-title {{
            color: var(--foreground);
        }}

        .checklist-card-check {{
            flex-shrink: 0;
            padding-top: 0.2rem;
        }}

        .checklist-checkbox-btn {{
            width: 22px;
            height: 22px;
            border-radius: var(--radius-sm);
            background-color: var(--secondary);
            color: transparent;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.15s ease;
            padding: 0;
        }}

        .checklist-checkbox-btn:hover {{
            background-color: var(--secondary-hover);
        }}

        .checklist-checkbox-btn.checked {{
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
        }}

        .checklist-checkbox-btn .chk-svg {{
            width: 14px;
            height: 14px;
            stroke-width: 3;
        }}

        .checklist-card-content {{
            flex: 1;
            min-width: 0;
        }}

        .checklist-card-header-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.5rem;
            margin-bottom: 0.4rem;
        }}

        .checklist-card-meta {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
            flex-wrap: wrap;
        }}

        .checklist-card-actions {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
            flex-shrink: 0;
        }}

        .chk-chevron {{
            transition: transform 0.2s ease;
            color: var(--muted-foreground);
        }}

        .checklist-card.is-open .chk-chevron {{
            transform: rotate(180deg);
            color: var(--foreground);
        }}

        .checklist-card-title {{
            font-size: 0.96875rem;
            font-weight: 500;
            line-height: 1.55;
            color: var(--foreground);
            max-width: 1040px;
            transition: color 0.15s ease;
            margin-bottom: 0;
        }}

        .checklist-card.is-open .checklist-card-title {{
            margin-bottom: 0.65rem;
        }}

        /* IN-PLACE SOLUTION CONTAINER */
        .checklist-solution-content {{
            display: none;
            padding-top: 1rem;
            margin-top: 0.75rem;
            cursor: default;
            user-select: text;
        }}

        .checklist-solution-content.open {{
            display: block;
        }}

        .checklist-solution-footer {{
            display: flex;
            justify-content: flex-end;
            margin-top: 1.25rem;
            padding-top: 0.75rem;
        }}

        .checklist-jump-link {{
            background-color: var(--secondary);
            color: var(--muted-foreground);
            border: none;
            padding: 0.35rem 0.75rem;
            font-size: 0.8125rem;
            font-weight: 500;
            border-radius: var(--radius-sm);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            transition: background-color 0.15s ease, color 0.15s ease;
        }}

        .checklist-jump-link:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        /* HIGHLIGHT TARGET WHEN JUMPING FROM CHECKLIST TO QUESTION BANK */
        .q-item.highlight-target {{
            box-shadow: 0 0 0 3px var(--pastel-sage-foreground), var(--shadow-lg) !important;
            transform: translateY(-2px);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        /* ----------------------------------------------------
           RESPONSIVE APP & MOBILE BOTTOM NAVIGATION SYSTEM
           ---------------------------------------------------- */
        .mobile-bottom-nav {{
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background-color: var(--card);
            border-top: 1px solid var(--secondary);
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
            padding-bottom: env(safe-area-inset-bottom, 0px);
            height: calc(56px + env(safe-area-inset-bottom, 0px));
            align-items: stretch;
            justify-content: space-around;
            transition: background-color 0.2s ease;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }}

        [data-theme="dark"] .mobile-bottom-nav {{
            box-shadow: 0 -2px 12px rgba(0, 0, 0, 0.5);
            border-top-color: var(--secondary-hover);
        }}

        .mobile-nav-item {{
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 3px;
            background: transparent;
            color: var(--muted-foreground);
            border: none;
            cursor: pointer;
            text-decoration: none;
            padding: 6px 0 4px;
            position: relative;
            user-select: none;
            transition: color 0.15s ease, transform 0.1s ease;
            touch-action: manipulation;
        }}

        .mobile-nav-item:active {{
            transform: scale(0.94);
        }}

        .mobile-nav-item.active {{
            color: var(--foreground);
            font-weight: 600;
        }}

        .mobile-nav-icon {{
            width: 20px;
            height: 20px;
            stroke-width: 2.2;
            stroke: currentColor;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
            transition: transform 0.15s ease;
        }}

        .mobile-nav-item.active .mobile-nav-icon {{
            stroke-width: 2.5;
            transform: translateY(-1px);
        }}

        .mobile-nav-label {{
            font-size: 11px;
            line-height: 1.2;
            letter-spacing: -0.01em;
        }}

        .mobile-nav-item.active .mobile-nav-label {{
            font-weight: 600;
        }}

        /* KATEX & MATHEMATICAL FORMULA OVERFLOW IMMUNITY */
        .katex-display {{
            overflow-x: auto !important;
            overflow-y: hidden !important;
            padding: 0.4rem 0 !important;
            -webkit-overflow-scrolling: touch !important;
            max-width: 100% !important;
        }}

        .katex {{
            font-size: 1.05em;
            max-width: 100%;
        }}

        /* KATEX FRACTION DIVIDING LINE & MATHEMATICAL BORDER ENFORCEMENT */
        .katex * {{
            border-color: currentColor;
        }}

        .katex .mfrac .frac-line {{
            display: inline-block !important;
            width: 100% !important;
            border-bottom-style: solid !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
            min-height: 1.2px !important;
        }}

        .katex .overline .overline-line,
        .katex .underline .underline-line {{
            border-bottom-style: solid !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
            min-height: 1.2px !important;
        }}

        .katex .hdashline {{
            border-bottom-style: dashed !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
        }}

        .katex .hline {{
            border-bottom-style: solid !important;
            border-bottom-width: 0.06em !important;
            border-bottom-width: max(1.2px, 0.05em) !important;
            border-bottom-color: currentColor !important;
        }}

        .katex .rule {{
            border-style: solid !important;
            border-color: currentColor !important;
        }}

        .table-responsive-wrapper {{
            -webkit-overflow-scrolling: touch;
        }}

        /* TABLET & MOBILE RESPONSIVE ADAPTATIONS */
        @media (max-width: 768px) {{
            .mobile-bottom-nav {{
                display: flex;
            }}

            body {{
                padding-bottom: calc(64px + env(safe-area-inset-bottom, 0px));
            }}

            .control-panel {{
                padding: 0.75rem 0.85rem;
                gap: 0.65rem;
                border-radius: var(--radius-md);
            }}

            .control-panel-toolbar {{
                flex-direction: column;
                align-items: stretch;
                gap: 0.65rem;
                padding-bottom: 0.65rem;
            }}

            .search-box-wrapper {{
                max-width: 100%;
                min-width: 100%;
                width: 100%;
            }}

            .search-input {{
                height: 38px;
                font-size: 0.875rem;
                padding-left: 2.25rem;
            }}

            .control-panel-actions,
            .control-panel-meta {{
                width: 100%;
                margin-left: 0;
                justify-content: space-between;
                gap: 0.35rem;
                flex-wrap: wrap;
            }}

            .control-panel-filters {{
                gap: 0.55rem;
            }}

            .control-panel-filter-row {{
                flex-direction: column;
                align-items: stretch;
                gap: 0.5rem;
                width: 100%;
            }}

            .filter-subgroup {{
                display: flex;
                align-items: center;
                gap: 0.45rem;
                width: 100%;
            }}

            .filter-group-label {{
                font-size: 0.6875rem;
                min-width: 52px;
                flex-shrink: 0;
            }}

            .filter-pills-row {{
                display: flex;
                gap: 0.25rem;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: none;
                flex: 1;
                white-space: nowrap;
                padding: 2.5px 3px;
            }}

            .filter-pills-row::-webkit-scrollbar {{
                display: none;
            }}

            .filter-divider {{
                display: none;
            }}

            .filter-pill-btn {{
                padding: 0.3rem 0.65rem;
                font-size: 0.75rem;
                min-height: 28px;
                flex-shrink: 0;
            }}

            .reset-filters-btn, .panel-year-toggle-btn {{
                font-size: 0.72rem;
                padding: 0.2rem 0.5rem;
                height: 28px;
            }}

            .checklist-header-row {{
                flex-direction: column;
                align-items: flex-start;
                gap: 0.75rem;
                margin-bottom: 1rem;
            }}

            .checklist-header-right {{
                width: 100%;
                justify-content: flex-start;
                gap: 0.5rem;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: none;
                padding-bottom: 3px;
                flex-wrap: nowrap;
            }}

            .checklist-header-right::-webkit-scrollbar {{
                display: none;
            }}

            .checklist-progress-circle {{
                flex-shrink: 0;
            }}

            .checklist-summary-units {{
                flex-shrink: 0;
                flex-wrap: nowrap;
            }}

            .checklist-year-pill {{
                padding: 0.28rem 0.55rem;
                font-size: 0.75rem;
                flex-shrink: 0;
            }}

            .checklist-toolbar {{
                padding: 0;
                flex-direction: column;
                align-items: stretch;
                gap: 0.65rem;
                background: transparent;
                box-shadow: none;
            }}

            .checklist-toolbar-filters {{
                display: flex;
                flex-direction: column;
                align-items: stretch;
                gap: 0.5rem;
                width: 100%;
            }}

            .checklist-filter-divider {{
                display: none;
            }}

            .checklist-unit-group {{
                display: flex;
                align-items: center;
                gap: 0.35rem;
                width: 100%;
            }}

            .checklist-search-box {{
                max-width: 100%;
                min-width: 100%;
                width: 100%;
            }}

            .checklist-card {{
                padding: 0.85rem 0.95rem;
                border-radius: var(--radius-md);
                gap: 0.65rem;
            }}

            .checklist-card-title {{
                font-size: 0.90625rem;
                line-height: 1.5;
            }}

            .checklist-card-meta {{
                gap: 0.3rem;
            }}

            .checklist-card-meta .badge {{
                font-size: 0.6875rem;
                padding: 0.18rem 0.4rem;
            }}
        }}

        @media (max-width: 640px) {{
            .q-item {{
                padding: 1rem 1rem;
                border-radius: var(--radius-md);
            }}

            .q-item-header {{
                gap: 0.45rem;
                margin-bottom: 0.5rem;
            }}

            .q-item-qno {{
                font-size: 0.75rem;
                padding: 0.2rem 0.5rem;
            }}

            .q-item-left-meta {{
                gap: 0.35rem;
                row-gap: 0.25rem;
                flex: 1;
                min-width: 0;
            }}

            .q-item-right-meta {{
                gap: 0.35rem;
                margin-left: auto;
                flex-shrink: 0;
            }}

            .q-item-badges {{
                gap: 0.25rem;
                flex-wrap: wrap;
            }}

            .q-item-badges .badge {{
                font-size: 0.6875rem;
                padding: 0.18rem 0.45rem;
            }}

            .complete-btn {{
                font-size: 0.72rem;
                padding: 0.25rem 0.55rem;
                min-height: 28px;
            }}

            .note-action-btn {{
                width: 28px;
                height: 28px;
                padding: 0;
            }}

            .sol-view-switch-row {{
                flex-direction: column;
                align-items: flex-start;
                gap: 0.5rem;
            }}

            .sol-view-pills {{
                width: 100%;
                justify-content: flex-start;
            }}

            .sol-view-quick-actions {{
                width: 100%;
                justify-content: flex-end;
            }}

            .my-answer-container, .note-editor-container {{
                padding: 0.85rem 1rem;
            }}

            .q-item-title {{
                font-size: clamp(0.9375rem, 3.5vw, 1.0625rem);
                line-height: 1.5;
            }}

            .q-solution-content {{
                padding-top: 0.85rem;
                margin-top: 0.65rem;
            }}

            .solution-body {{
                font-size: 0.9375rem;
                line-height: 1.65;
            }}

            .sol-heading {{
                font-size: 1rem;
                margin-top: 0.75rem;
                margin-bottom: 0.45rem;
            }}

            .sol-item-row {{
                gap: 0.45rem;
                margin-bottom: 0.65rem;
                font-size: 0.9375rem;
                line-height: 1.65;
            }}

            .sol-item-num {{
                min-width: 1.25rem;
                font-size: 0.9375rem;
            }}

            .sol-diagram-box {{
                padding: 0.65rem 0.4rem;
                margin: 0.65rem 0;
            }}

            .sol-table-wrap {{
                margin: 0.65rem 0;
            }}

            .sol-table th, .sol-table td {{
                padding: 0.5rem 0.65rem;
                font-size: 0.8125rem;
            }}

            .q-topic-section-header {{
                margin-top: 1.5rem;
                margin-bottom: 0.4rem;
            }}

            .q-topic-section-title {{
                font-size: 1.05rem;
            }}

            .q-tier-section-divider {{
                margin-top: 2rem;
                margin-bottom: 1rem;
            }}

            .q-unit-section-divider {{
                margin-top: 1.5rem;
                margin-bottom: 0.5rem;
            }}
        }}

    </style>
</head>
<body>

    <!-- STICKY HEADER NAVBAR (WITH TABS VIEW) -->
    <header class="header">
        <div class="container nav">
            <div class="brand" onclick="switchPageView('questions')" title="{subject_name}">
                <span class="brand-title">{subject_name}</span>
            </div>

            <!-- Nav links with badge view -->
            <ul class="nav-links">
                <li>
                    <button class="nav-link-btn active" data-view="questions" onclick="switchPageView('questions')">
                        <i class="icon icon-sm hgi-stroke hgi-help-circle"></i>
                        Questions
                        <span class="nav-badge" id="navQuestionsBadge">{len(raw_questions)}</span>
                    </button>
                </li>
                <li>
                    <button class="nav-link-btn" data-view="syllabus" onclick="switchPageView('syllabus')">
                        <i class="icon icon-sm hgi-stroke hgi-task-01"></i>
                        Checklist
                        <span class="nav-badge" id="navChecklistBadge">0/{len(raw_questions)}</span>
                    </button>
                </li>
                <li>
                    <button class="nav-link-btn" data-view="formulas" onclick="switchPageView('formulas')">
                        <i class="icon icon-sm hgi-stroke hgi-function-of-x"></i>
                        Formulas
                    </button>
                </li>
                <li>
                    <a href="timetable.html" class="nav-link-btn nav-link-timetable" title="View Exam Timetable">
                        <i class="icon icon-sm hgi-stroke hgi-calendar-03"></i>
                        Timetable
                    </a>
                </li>
            </ul>

            <div class="nav-actions">
                <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle Theme" title="Toggle Light/Dark Theme">
                    <i class="icon hgi-stroke hgi-sun-01" id="themeIcon"></i>
                </button>
            </div>
        </div>
    </header>

    <div class="container">

        <!-- ====================================================
             PAGE VIEW 1: QUESTIONS & SOLUTIONS ENGINE (DEFAULT)
             ==================================================== -->
        <div class="app-page-view active" id="view-questions">
            <!-- Compact, Space-Efficient Control Panel (Minimal Grid Architecture) -->
            <div class="control-panel">
                <!-- TOP UTILITY & SEARCH TOOLBAR -->
                <div class="control-panel-toolbar">
                    <div class="search-box-wrapper">
                        <i class="icon icon-sm search-icon hgi-stroke hgi-search-01"></i>
                        <input type="text" class="search-input" id="searchInput" placeholder="Search topics, questions, formulas..." aria-label="Search questions">
                        <kbd class="search-kbd-hint" aria-hidden="true">/</kbd>
                        <button class="search-clear-btn" id="searchClearBtn" title="Clear search" aria-label="Clear search" style="display: none;">
                            <i class="icon icon-xs hgi-stroke hgi-cancel-01"></i>
                        </button>
                    </div>

                    <button class="reset-filters-btn" id="resetFiltersBtn" title="Reset all filters to default" style="display: none;">
                        <i class="icon icon-xs hgi-stroke hgi-arrow-reload-horizontal"></i>
                        Reset
                    </button>
                </div>

                <!-- PROPER CSS GRID FOR ALL 6 FILTER DIMENSIONS -->
                <div class="control-panel-grid">
                    <!-- CELL 1: YEAR -->
                    <div class="filter-grid-cell">
                        <span class="filter-grid-label">Year</span>
                        <div id="yearFilters" class="filter-pill-group">
                            <button class="filter-pill-btn active" data-year="all">All</button>
                            <button class="filter-pill-btn" data-year="2025">2025</button>
                            <button class="filter-pill-btn" data-year="2024">2024</button>
                            <button class="filter-pill-btn" data-year="2023" id="filterPill2023">2023</button>
                            <button class="filter-pill-btn" data-year="2022">2022</button>
                        </div>
                    </div>

                    <!-- CELL 2: REPEATED -->
                    <div class="filter-grid-cell">
                        <span class="filter-grid-label">Repeated</span>
                        <div id="repeatFilters" class="filter-pill-group">
                            <button class="filter-pill-btn active" data-repeat="all">All</button>
                            <button class="filter-pill-btn" data-repeat="repeated" title="All Repeated Questions (4x, 3x, 2x)">Most Repeated</button>
                            <button class="filter-pill-btn" data-repeat="4x" title="Questions repeated across all 4 exam papers">4x</button>
                            <button class="filter-pill-btn" data-repeat="3x" title="Questions repeated across 3 exam papers">3x</button>
                            <button class="filter-pill-btn" data-repeat="2x" title="Questions repeated across 2 exam papers">2x</button>
                        </div>
                    </div>

                    <!-- CELL 3: STATUS -->
                    <div class="filter-grid-cell">
                        <span class="filter-grid-label">Status</span>
                        <div id="statusFilters" class="filter-pill-group">
                            <button class="filter-pill-btn active" data-status="all">All</button>
                            <button class="filter-pill-btn" data-status="incomplete" title="Hide completed questions">Incomplete</button>
                            <button class="filter-pill-btn" data-status="completed" title="Show only completed questions">Completed</button>
                            <button class="filter-pill-btn" data-status="starred" title="Show only starred questions">Starred</button>
                            <button class="filter-pill-btn" data-status="later" title="Show questions saved for later">Later</button>
                        </div>
                    </div>

                    <!-- CELL 4: UNIT -->
                    <div class="filter-grid-cell">
                        <span class="filter-grid-label">Unit</span>
                        <div id="unitFilters" class="filter-pill-group">
                            <button class="filter-pill-btn active" data-unit="all">All</button>
                            <button class="filter-pill-btn" data-unit="1">Unit 1</button>
                            <button class="filter-pill-btn" data-unit="2">Unit 2</button>
                            <button class="filter-pill-btn" data-unit="3">Unit 3</button>
                            <button class="filter-pill-btn" data-unit="4">Unit 4</button>
                            <button class="filter-pill-btn" data-unit="5">Unit 5</button>
                        </div>
                    </div>

                    <!-- CELL 5: TYPE -->
                    <div class="filter-grid-cell">
                        <span class="filter-grid-label">Type</span>
                        <div id="typeFilters" class="filter-pill-group">
                            <button class="filter-pill-btn active" data-type="all">All</button>
                            <button class="filter-pill-btn" data-type="Theory">Theory</button>
                            <button class="filter-pill-btn" data-type="Numerical">Numerical</button>
                            <button class="filter-pill-btn" data-type="Derivation">Derivation</button>
                        </div>
                    </div>

                    <!-- CELL 6: MARKS -->
                    <div class="filter-grid-cell">
                        <span class="filter-grid-label">Marks</span>
                        <div id="marksFilters" class="filter-pill-group">
                            <button class="filter-pill-btn active" data-marks="all">All</button>
                            <button class="filter-pill-btn" data-marks="2">2M</button>
                            <button class="filter-pill-btn" data-marks="3">3M</button>
                            <button class="filter-pill-btn" data-marks="7">7M / 6M</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Dynamic Question List Container -->
            <div class="questions-list-wrapper" id="questionsContainer">
                <!-- Rendered dynamically by JavaScript -->
            </div>
        </div>

        {unit_checklist_html}

        <!-- ====================================================
             PAGE VIEW 4: FORMULAS REFERENCE (CHEAT-SHEET)
             ==================================================== -->
        <div class="app-page-view" id="view-formulas">
            <div class="table-responsive-wrapper">
                <table class="master-data-table">
                    <thead>
                        <tr>
                            <th style="width: 130px;">Unit</th>
                            <th style="width: 220px;">Topic &amp; Application</th>
                            <th style="width: 380px;">Governing Equation</th>
                            <th>Parameter Definitions &amp; Units</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><span class="badge badge-unit-1">Unit 1</span></td>
                            <td>Rankine Active Pressure</td>
                            <td><span class="formula-chip">p<sub>a</sub> = K<sub>a</sub> &sigma;'<sub>v</sub> - 2c &radic;K<sub>a</sub></span></td>
                            <td>
                                <ul class="table-list">
                                    <li><span class="formula-chip-sm">K<sub>a</sub> = (1 - sin&phi;) / (1 + sin&phi;) = tan&sup2;(45&deg; - &phi;/2)</span></li>
                                    <li>Tension crack depth: <span class="formula-chip-sm">z<sub>c</sub> = 2c / (&gamma;&radic;K<sub>a</sub>)</span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-1">Unit 1</span></td>
                            <td>Coulomb Earth Thrust</td>
                            <td><span class="formula-chip">P<sub>a</sub> = 0.5 &gamma; H&sup2; K<sub>a</sub>, P<sub>p</sub> = 0.5 &gamma; H&sup2; K<sub>p</sub></span></td>
                            <td>
                                <ul class="table-list">
                                    <li>Acts at <span class="formula-chip-sm">H/3</span> above base of the retaining wall</li>
                                    <li>Inclined at wall friction angle <span class="formula-chip-sm">&delta;</span> to wall normal</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-2">Unit 2</span></td>
                            <td>Mohr-Coulomb Failure</td>
                            <td><span class="formula-chip">&sigma;'₁ = &sigma;'₃ tan&sup2;(45&deg; + &phi;'/2) + 2c' tan(45&deg; + &phi;'/2)</span></td>
                            <td>
                                <ul class="table-list">
                                    <li><span class="formula-chip-sm">&sigma;'₁</span> = Major effective principal stress at failure</li>
                                    <li><span class="formula-chip-sm">&sigma;'₃</span> = Minor effective principal stress (cell confining pressure)</li>
                                    <li>Failure plane inclination: <span class="formula-chip-sm">&theta;<sub>cr</sub> = 45&deg; + &phi;'/2</span> to horizontal</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-2">Unit 2</span></td>
                            <td>Triaxial Area Correction</td>
                            <td><span class="formula-chip">A = A<sub>0</sub> / (1 - &epsilon;)</span></td>
                            <td>
                                <ul class="table-list">
                                    <li><span class="formula-chip-sm">&epsilon; = &Delta;L / L<sub>0</sub></span> (axial strain at failure)</li>
                                    <li>Deviator stress: <span class="formula-chip-sm">&Delta;&sigma; = Failure Load / A</span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-2">Unit 2</span></td>
                            <td>Infinite Slope Seepage</td>
                            <td><span class="formula-chip">FS = (c' + &gamma;' z cos&sup2;&beta; tan&phi;') / (&gamma;<sub>sat</sub> z sin&beta; cos&beta;)</span></td>
                            <td>
                                <ul class="table-list">
                                    <li><span class="formula-chip-sm">&beta;</span> = slope angle; <span class="formula-chip-sm">z</span> = failure plane depth</li>
                                    <li>Submerged unit weight: <span class="formula-chip-sm">&gamma;' = &gamma;<sub>sat</sub> - &gamma;<sub>w</sub></span></li>
                                    <li>Submerged cohesionless slope: <span class="formula-chip-sm">FS = (&gamma;'/&gamma;<sub>sat</sub>)(tan&phi;'/tan&beta;)</span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-3">Unit 3</span></td>
                            <td>Terzaghi Bearing Capacity</td>
                            <td><span class="formula-chip">q<sub>ult</sub> = c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> R<sub>w1</sub> + 0.5 &gamma; B N<sub>&gamma;</sub> R<sub>w2</sub></span></td>
                            <td>
                                <ul class="table-list">
                                    <li><strong>Square Footing:</strong> <span class="formula-chip-sm">q<sub>ult</sub> = 1.3c N<sub>c</sub> + q N<sub>q</sub> + 0.4 &gamma; B N<sub>&gamma;</sub></span></li>
                                    <li><strong>Circular Footing:</strong> <span class="formula-chip-sm">q<sub>ult</sub> = 1.3c N<sub>c</sub> + q N<sub>q</sub> + 0.3 &gamma; B N<sub>&gamma;</sub></span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-3">Unit 3</span></td>
                            <td>Water Table Factors</td>
                            <td><span class="formula-chip">R<sub>w1</sub> = 0.5 [1 + (z<sub>w1</sub>/D<sub>f</sub>)], R<sub>w2</sub> = 0.5 [1 + (z<sub>w2</sub>/B)]</span></td>
                            <td>
                                <ul class="table-list">
                                    <li><span class="formula-chip-sm">z<sub>w1</sub>, z<sub>w2</sub></span>: Water table depths below ground and footing base</li>
                                    <li>When WT is at ground surface: <span class="formula-chip-sm">R<sub>w1</sub> = R<sub>w2</sub> = 0.5</span> (<span class="note-highlight">~50% reduction in q<sub>safe</sub></span>)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-3">Unit 3</span></td>
                            <td>Housel's Two-Plate Method</td>
                            <td><span class="formula-chip">Q<sub>1</sub> = A<sub>1</sub> m + P<sub>1</sub> n &emsp;|&emsp; Q<sub>2</sub> = A<sub>2</sub> m + P<sub>2</sub> n</span></td>
                            <td>
                                <ul class="table-list">
                                    <li><span class="formula-chip-sm">m</span> = Perimeter shear resistance factor (kN/m)</li>
                                    <li><span class="formula-chip-sm">n</span> = Direct bearing resistance factor (kN/m&sup2;)</li>
                                    <li>Prototype Footing: <span class="formula-chip-sm">Q<sub>F</sub> = A<sub>F</sub> &middot; m + P<sub>F</sub> &middot; n</span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-4">Unit 4</span></td>
                            <td>Single Pile Capacity</td>
                            <td><span class="formula-chip">Q<sub>u</sub> = 9 c<sub>u</sub> A<sub>b</sub> + &alpha; c<sub>u</sub> A<sub>s</sub></span></td>
                            <td>
                                <ul class="table-list">
                                    <li>Base area: <span class="formula-chip-sm">A<sub>b</sub> = &pi; d&sup2; / 4</span>; Shaft area: <span class="formula-chip-sm">A<sub>s</sub> = &pi; d L</span></li>
                                    <li><span class="formula-chip-sm">&alpha;</span> = Adhesion factor (<span class="formula-chip-sm">0.7 &ndash; 0.8</span> for soft clay)</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-4">Unit 4</span></td>
                            <td>Pile Group Block Failure</td>
                            <td><span class="formula-chip">Q<sub>ug</sub> = 9 c<sub>u</sub> B&sup2; + 4 B L c<sub>u</sub></span></td>
                            <td>
                                <ul class="table-list">
                                    <li>Group width: <span class="formula-chip-sm">B = (n - 1)s + d</span> for an <span class="formula-chip-sm">n &times; n</span> pile grid</li>
                                    <li>Safe group capacity: <span class="formula-chip-sm">Q<sub>safe</sub> = min(Q<sub>ug</sub>, n&middot;Q<sub>ui</sub>) / FS</span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-4">Unit 4</span></td>
                            <td>Optimum Pile Spacing</td>
                            <td><span class="formula-chip">s = d + (2 d / &pi; &alpha;)</span></td>
                            <td>
                                <ul class="table-list">
                                    <li>Derived by equating group block perimeter shear to sum of individual pile skin resistances</li>
                                    <li>Prevents redundant pile installation and block shear failure</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-5">Unit 5</span></td>
                            <td>SPT Overburden Correction</td>
                            <td><span class="formula-chip">N' = N &middot; [350 / (&sigma;'<sub>v</sub> + 70)]</span></td>
                            <td>
                                <ul class="table-list">
                                    <li>IS / Peck-Hanson-Thornburn formula; valid for <span class="formula-chip-sm">&sigma;'<sub>v</sub> &le; 280 kN/m&sup2;</span></li>
                                    <li>Liao &amp; Whitman alternative: <span class="formula-chip-sm">N' = N &middot; &radic;(100 / &sigma;'<sub>v</sub>)</span></li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-5">Unit 5</span></td>
                            <td>SPT Dilatancy Correction</td>
                            <td><span class="formula-chip">N'' = 15 + 0.5 (N' - 15)</span></td>
                            <td>
                                <ul class="table-list">
                                    <li>Applies strictly when <span class="formula-chip-sm">N' &gt; 15</span></li>
                                    <li>Applies in saturated fine sands or silty sands located below the water table</li>
                                    <li>Accounts for negative pore water pressure induced during dynamic hammer driving</li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td><span class="badge badge-unit-5">Unit 5</span></td>
                            <td>Sampler Area Ratio</td>
                            <td><span class="formula-chip">A<sub>r</sub> = [(D&sup2;<sub>ext</sub> - D&sup2;<sub>int</sub>) / D&sup2;<sub>int</sub>] &times; 100%</span></td>
                            <td>
                                <ul class="table-list">
                                    <li>Undisturbed sampling standard: <span class="formula-chip-sm">A<sub>r</sub> &le; 10&ndash;12%</span> (thin-walled Shelby tube)</li>
                                    <li>Inside clearance: <span class="formula-chip-sm">C<sub>i</sub> = 1&ndash;3%</span>; Outside clearance: <span class="formula-chip-sm">C<sub>o</sub> = 0&ndash;2%</span></li>
                                </ul>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- ====================================================
             PAGE VIEW: NOTES & CUSTOM ANSWERS ARCHIVE
             ==================================================== -->
        <div class="app-page-view" id="view-notes">
            <div class="page-header-row" style="margin-bottom: 1.25rem;">
                <div class="page-header-titles">
                    <span class="card-overline">Personal Study Archive &bull; <span id="notesCountStat">0 Answers Saved</span></span>
                    <h1 class="page-title">My Notes &amp; Custom Answers</h1>
                </div>
                <div class="page-header-actions" style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <button type="button" class="complete-btn" onclick="exportNotesJSON()" title="Download a JSON backup of all your notes and answers">
                        <i class="icon icon-xs hgi-stroke hgi-download-02"></i>
                        <span>Export Backup</span>
                    </button>
                    <button type="button" class="complete-btn" onclick="triggerImportNotes()" title="Restore notes from a JSON backup file">
                        <i class="icon icon-xs hgi-stroke hgi-upload-02"></i>
                        <span>Import</span>
                    </button>
                    <input type="file" id="notesImportFileInput" accept=".json" style="display:none;" onchange="handleImportFile(event)">
                    <button type="button" class="complete-btn" onclick="copyAllNotesToClipboard()" title="Copy all notes formatted to clipboard">
                        <i class="icon icon-xs hgi-stroke hgi-copy-01"></i>
                        <span>Copy All</span>
                    </button>
                </div>
            </div>

            <!-- GENERAL REVISION SCRATCHPAD / SUBJECT NOTES -->
            <div class="general-scratchpad-card">
                <div class="scratchpad-header">
                    <div class="scratchpad-title-wrap">
                        <i class="icon icon-sm hgi-stroke hgi-note-01"></i>
                        <div>
                            <h3 class="scratchpad-title">General Scratchpad &amp; Revision Notes</h3>
                            <p class="scratchpad-subtitle">Freeform notes, exam warnings, memory mnemonics, or formulas to remember for {subject_name}.</p>
                        </div>
                    </div>
                    <div class="scratchpad-status" id="scratchpadStatus">
                        <span class="status-indicator"></span>
                        <span id="scratchpadStatusText">Auto-saved</span>
                    </div>
                </div>
                <textarea class="scratchpad-textarea" id="generalNotesTextarea" rows="4" placeholder="Jot down quick reminders, high-priority exam tips, formulas to memorize, or general revision notes here..." oninput="handleGeneralNotesInput()"></textarea>
            </div>

            <!-- NOTES SEARCH & UNIT FILTER TOOLBAR -->
            <div class="notes-filter-toolbar">
                <div class="notes-search-box">
                    <i class="icon icon-xs notes-search-icon hgi-stroke hgi-search-01"></i>
                    <input type="text" class="notes-search-input" id="notesSearchInput" placeholder="Filter saved answers by question, keywords, or content..." oninput="filterNotesView()">
                </div>
                <div class="notes-unit-pills" id="notesUnitFilters">
                    <button type="button" class="filter-pill-btn active" data-unit="all" onclick="setNotesUnitFilter('all', this)">All Units</button>
                    <button type="button" class="filter-pill-btn" data-unit="1" onclick="setNotesUnitFilter('1', this)">Unit 1</button>
                    <button type="button" class="filter-pill-btn" data-unit="2" onclick="setNotesUnitFilter('2', this)">Unit 2</button>
                    <button type="button" class="filter-pill-btn" data-unit="3" onclick="setNotesUnitFilter('3', this)">Unit 3</button>
                    <button type="button" class="filter-pill-btn" data-unit="4" onclick="setNotesUnitFilter('4', this)">Unit 4</button>
                    <button type="button" class="filter-pill-btn" data-unit="5" onclick="setNotesUnitFilter('5', this)">Unit 5</button>
                </div>
            </div>

            <!-- SAVED QUESTION NOTES CONTAINER -->
            <div class="saved-notes-list" id="savedNotesContainer">
                <!-- Populated dynamically by JavaScript -->
            </div>
        </div>

    </div>

    <!-- Embedded High-Performance Data Arrays -->
    <script>
        const CANONICAL_TOPICS = {canonical_json_str};
        const RAW_QUESTIONS = {raw_json_str};

        const STORAGE_KEY_FILTERS = '{storage_prefix}_filters';
        const STORAGE_KEY_COMPLETED = '{storage_prefix}_completed_questions';
        const STORAGE_KEY_VIEW = '{storage_prefix}_active_view';
        const STORAGE_KEY_HIDE_2023 = '{storage_prefix}_hide_2023';
        const STORAGE_KEY_NOTES = '{storage_prefix}_user_notes';
        const STORAGE_KEY_GENERAL_NOTES = '{storage_prefix}_general_notes';
        const STORAGE_KEY_STARRED = '{storage_prefix}_starred_questions';
        const STORAGE_KEY_LATER = '{storage_prefix}_later_questions';

        const EMBEDDED_NOTES = {embedded_notes_json};
        const EMBEDDED_STARRED = {embedded_starred_json};
        const EMBEDDED_LATER = {embedded_later_json};
        const EMBEDDED_GEN_NOTES = {embedded_general_notes};

        let hide2023 = false;
        try {{
            localStorage.removeItem(STORAGE_KEY_HIDE_2023);
        }} catch (e) {{}}

        function setHide2023(val) {{
            hide2023 = false; // 2023 toggle removed per user directive; always visible
            try {{
                localStorage.removeItem(STORAGE_KEY_HIDE_2023);
            }} catch (e) {{}}

            sync2023ToggleUI();
            renderQuestions();
            updateMetrics();
            syncChecklistUI();
        }}

        window.toggleHide2023 = function() {{
            setHide2023(false);
        }};
        window.toggleHide2022 = window.toggleHide2023; // Alias for backward compatibility

        function sync2023ToggleUI() {{
            const panelBtn = document.getElementById('panelToggle2023Btn');
            const panelText = document.getElementById('panelToggle2023Text');
            const filterPill2023 = document.getElementById('filterPill2023');
            const checklistPill2023 = document.getElementById('checklistYearPill-2023');
            const yearSection2023 = document.getElementById('year-section-2023');

            const isShown = !hide2023;

            if (panelBtn) {{
                panelBtn.classList.toggle('is-active', isShown);
                panelBtn.classList.toggle('is-hidden', !isShown);
                panelBtn.title = isShown ? '2023 PYQs are included' : '2023 PYQs are hidden';
            }}
            if (panelText) {{
                panelText.innerHTML = isShown 
                    ? '<span class="badge badge-year-2023">2023</span> Shown'
                    : '<span class="badge badge-subtle">2023</span> Hidden';
            }}

            if (filterPill2023) {{
                filterPill2023.style.display = isShown ? 'inline-flex' : 'none';
            }}

            if (checklistPill2023) {{
                checklistPill2023.style.display = isShown ? 'inline-flex' : 'none';
            }}

            if (yearSection2023) {{
                yearSection2023.style.display = isShown ? 'block' : 'none';
            }}
        }}

        let currentYear = 'all';
        let currentUnit = 'all';
        let currentType = 'all';
        let currentMarks = 'all';
        let currentRepeat = 'all';
        let currentStatus = 'all';
        let searchQuery = '';

        const EMBEDDED_COMPLETED = {embedded_completed_json};
        const CURRENT_SUBJECT_ID = '{subject_id_str}';

        let completedQuestions = new Set();
        try {{
            if (Array.isArray(EMBEDDED_COMPLETED) && EMBEDDED_COMPLETED.length > 0) {{
                EMBEDDED_COMPLETED.forEach(qid => completedQuestions.add(qid));
            }}
            const savedDone = JSON.parse(localStorage.getItem(STORAGE_KEY_COMPLETED) || '[]');
            if (Array.isArray(savedDone)) {{
                savedDone.forEach(qid => completedQuestions.add(qid));
            }}
        }} catch (e) {{
            console.error('Error loading completed questions:', e);
        }}

        let starredQuestions = new Set();
        try {{
            if (Array.isArray(EMBEDDED_STARRED) && EMBEDDED_STARRED.length > 0) {{
                EMBEDDED_STARRED.forEach(qid => starredQuestions.add(qid));
            }}
            const savedStarred = JSON.parse(localStorage.getItem(STORAGE_KEY_STARRED) || '[]');
            if (Array.isArray(savedStarred)) {{
                savedStarred.forEach(qid => starredQuestions.add(qid));
            }}
        }} catch (e) {{
            console.error('Error loading starred questions:', e);
        }}

        let laterQuestions = new Set();
        try {{
            if (Array.isArray(EMBEDDED_LATER) && EMBEDDED_LATER.length > 0) {{
                EMBEDDED_LATER.forEach(qid => laterQuestions.add(qid));
            }}
            const savedLater = JSON.parse(localStorage.getItem(STORAGE_KEY_LATER) || '[]');
            if (Array.isArray(savedLater)) {{
                savedLater.forEach(qid => laterQuestions.add(qid));
            }}
        }} catch (e) {{
            console.error('Error loading later questions:', e);
        }}

        let userNotes = {{}};
        try {{
            const savedNotes = JSON.parse(localStorage.getItem(STORAGE_KEY_NOTES) || '{{}}');
            userNotes = Object.assign({{}}, EMBEDDED_NOTES, savedNotes);
        }} catch(e) {{
            userNotes = Object.assign({{}}, EMBEDDED_NOTES);
        }}

        let generalNotes = '';
        try {{
            const savedGen = localStorage.getItem(STORAGE_KEY_GENERAL_NOTES);
            generalNotes = (savedGen !== null ? savedGen : EMBEDDED_GEN_NOTES) || '';
        }} catch(e) {{
            generalNotes = EMBEDDED_GEN_NOTES || '';
        }}

        let activeSolutionTab = {{}};
        let notesUnitFilter = 'all';
        let notesSearchQuery = '';

        function setSyncStatus(state, msg) {{
            const badge = document.getElementById('syncStatusBadge');
            const txt = document.getElementById('syncStatusText');
            if (!badge || !txt) return;
            badge.className = 'sync-indicator-badge ' + state;
            txt.textContent = msg;
        }}

        let diskSyncTimeout = null;
        function saveCompleted() {{
            try {{
                localStorage.setItem(STORAGE_KEY_COMPLETED, JSON.stringify([...completedQuestions]));
            }} catch (e) {{
                console.error('Error saving completed questions to localStorage:', e);
            }}
            updateMetrics();
            setSyncStatus('saving', 'Saving...');
            if (diskSyncTimeout) clearTimeout(diskSyncTimeout);
            diskSyncTimeout = setTimeout(syncProgressToDisk, 300);
        }}

        function saveStarred() {{
            try {{
                localStorage.setItem(STORAGE_KEY_STARRED, JSON.stringify([...starredQuestions]));
            }} catch (e) {{
                console.error('Error saving starred questions to localStorage:', e);
            }}
            setSyncStatus('saving', 'Saving...');
            if (diskSyncTimeout) clearTimeout(diskSyncTimeout);
            diskSyncTimeout = setTimeout(syncProgressToDisk, 300);
        }}

        function saveLater() {{
            try {{
                localStorage.setItem(STORAGE_KEY_LATER, JSON.stringify([...laterQuestions]));
            }} catch (e) {{
                console.error('Error saving later questions to localStorage:', e);
            }}
            updateMetrics();
            setSyncStatus('saving', 'Saving...');
            if (diskSyncTimeout) clearTimeout(diskSyncTimeout);
            diskSyncTimeout = setTimeout(syncProgressToDisk, 300);
        }}

        async function syncProgressToDisk() {{
            try {{
                const payload = {{
                    subject: CURRENT_SUBJECT_ID,
                    completed_questions: [...completedQuestions],
                    starred_questions: [...starredQuestions],
                    later_questions: [...laterQuestions],
                    filters: {{
                        year: currentYear,
                        unit: currentUnit,
                        type: currentType,
                        marks: currentMarks,
                        repeat: currentRepeat,
                        status: currentStatus,
                        search: searchQuery
                    }},
                    active_view: (typeof activeView !== 'undefined' ? activeView : 'questions'),
                    hide_2023: hide2023,
                    notes: userNotes,
                    general_notes: generalNotes
                }};
                const res = await fetch('/api/progress', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
                if (res.ok) {{
                    setSyncStatus('saved', 'Saved to JSON');
                }} else {{
                    setSyncStatus('local', 'Local Storage');
                }}
            }} catch (err) {{
                setSyncStatus('local', 'Local Storage');
            }}
        }}

        async function initProgressSync() {{
            try {{
                const res = await fetch('/api/progress');
                if (res.ok) {{
                    const data = await res.json();
                    const subData = data.subjects && data.subjects[CURRENT_SUBJECT_ID];
                    if (subData) {{
                        if (Array.isArray(subData.completed_questions)) {{
                            const prevSize = completedQuestions.size;
                            subData.completed_questions.forEach(qid => completedQuestions.add(qid));
                            if (completedQuestions.size > subData.completed_questions.length) {{
                                syncProgressToDisk();
                            }}
                            if (completedQuestions.size !== prevSize) {{
                                try {{
                                    localStorage.setItem(STORAGE_KEY_COMPLETED, JSON.stringify([...completedQuestions]));
                                }} catch (e) {{}}
                                renderQuestions();
                                syncChecklistUI();
                                updateMetrics();
                            }}
                        }}

                        if (Array.isArray(subData.starred_questions)) {{
                            subData.starred_questions.forEach(qid => starredQuestions.add(qid));
                            try {{
                                localStorage.setItem(STORAGE_KEY_STARRED, JSON.stringify([...starredQuestions]));
                            }} catch (e) {{}}
                        }}

                        if (Array.isArray(subData.later_questions)) {{
                            subData.later_questions.forEach(qid => laterQuestions.add(qid));
                            try {{
                                localStorage.setItem(STORAGE_KEY_LATER, JSON.stringify([...laterQuestions]));
                            }} catch (e) {{}}
                        }}

                        if (subData.notes && typeof subData.notes === 'object') {{
                            let updated = false;
                            for (const qid in subData.notes) {{
                                if (!userNotes[qid]) {{
                                    userNotes[qid] = subData.notes[qid];
                                    updated = true;
                                }}
                            }}
                            if (updated) {{
                                try {{
                                    localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(userNotes));
                                }} catch(e) {{}}
                                renderQuestions();
                                renderNotesPage();
                                updateNavBadges();
                            }}
                        }}

                        if (subData.general_notes && !generalNotes) {{
                            generalNotes = subData.general_notes;
                            const ta = document.getElementById('generalNotesTextarea');
                            if (ta) ta.value = generalNotes;
                            try {{
                                localStorage.setItem(STORAGE_KEY_GENERAL_NOTES, generalNotes);
                            }} catch(e) {{}}
                        }}
                    }}
                    setSyncStatus('saved', 'Saved to JSON');
                }} else {{
                    setSyncStatus('local', 'Local Storage');
                }}
            }} catch (e) {{
                setSyncStatus('local', 'Local Storage');
            }}
        }}

        function loadSavedFilters() {{
            try {{
                const saved = JSON.parse(localStorage.getItem(STORAGE_KEY_FILTERS) || '{{}}');
                if (saved.year) currentYear = saved.year;
                if (saved.unit) currentUnit = saved.unit;
                if (saved.type) currentType = saved.type;
                if (saved.marks) currentMarks = saved.marks;
                if (saved.repeat) currentRepeat = saved.repeat;
                if (saved.status) currentStatus = saved.status;
                if (typeof saved.search === 'string') searchQuery = saved.search;
            }} catch (e) {{
                console.error('Error loading saved filters:', e);
            }}
        }}

        function saveFilters() {{
            try {{
                localStorage.setItem(STORAGE_KEY_FILTERS, JSON.stringify({{
                    year: currentYear,
                    unit: currentUnit,
                    type: currentType,
                    marks: currentMarks,
                    repeat: currentRepeat,
                    status: currentStatus,
                    search: searchQuery
                }}));
            }} catch (e) {{
                console.error('Error saving filters:', e);
            }}
            updateResetButton();
        }}

        function syncFilterUI() {{
            function setPillActive(containerId, attr, value) {{
                const container = document.getElementById(containerId);
                if (!container) return;
                container.querySelectorAll('.filter-pill-btn').forEach(btn => {{
                    btn.classList.toggle('active', btn.getAttribute(attr) === String(value));
                }});
            }}

            setPillActive('yearFilters', 'data-year', currentYear);
            setPillActive('repeatFilters', 'data-repeat', currentRepeat);
            setPillActive('statusFilters', 'data-status', currentStatus);
            setPillActive('unitFilters', 'data-unit', currentUnit);
            setPillActive('typeFilters', 'data-type', currentType);
            setPillActive('marksFilters', 'data-marks', currentMarks);

            const searchInput = document.getElementById('searchInput');
            const searchClearBtn = document.getElementById('searchClearBtn');
            if (searchInput) {{
                searchInput.value = searchQuery;
                if (searchClearBtn) {{
                    searchClearBtn.style.display = searchQuery ? 'inline-flex' : 'none';
                }}
            }}
            updateResetButton();
            updateMetrics();
        }}

        function updateResetButton() {{
            const resetBtn = document.getElementById('resetFiltersBtn');
            if (!resetBtn) return;
            const isCustom = (currentYear !== 'all' || currentUnit !== 'all' || currentType !== 'all' || currentMarks !== 'all' || currentRepeat !== 'all' || currentStatus !== 'all' || searchQuery !== '');
            resetBtn.style.display = isCustom ? 'inline-flex' : 'none';
        }}

        function updateMetrics() {{
            const completedText = document.getElementById('completedCounterText');
            const clearBtn = document.getElementById('clearCompletedBtn');
            const visibleQuestions = RAW_QUESTIONS.filter(q => !hide2023 || String(q.year) !== '2023');
            // Questions marked as later are excluded from total count!
            const activeQuestions = visibleQuestions.filter(q => !laterQuestions.has(q.id));
            const total = activeQuestions.length;
            const doneCount = activeQuestions.filter(q => completedQuestions.has(q.id)).length;
            const pct = total > 0 ? Math.round((doneCount / total) * 100) : 0;

            if (completedText) {{
                completedText.textContent = `${{doneCount}} / ${{total}} Done (${{pct}}%)`;
            }}
            if (clearBtn) {{
                clearBtn.style.display = doneCount > 0 ? 'inline-flex' : 'none';
                clearBtn.innerHTML = `<i class="icon icon-xs hgi-stroke hgi-delete-02"></i> Clear Done (${{doneCount}})`;
            }}
            syncChecklistUI();
        }}

        window.toggleCompleteQuestion = function(id, event) {{
            if (event) {{
                event.stopPropagation();
            }}
            if (completedQuestions.has(id)) {{
                completedQuestions.delete(id);
            }} else {{
                completedQuestions.add(id);
            }}
            saveCompleted();
            renderQuestions();
            syncChecklistUI();
        }};

        window.toggleStarQuestion = function(id, event) {{
            if (event) {{
                event.stopPropagation();
            }}
            if (starredQuestions.has(id)) {{
                starredQuestions.delete(id);
            }} else {{
                starredQuestions.add(id);
            }}
            saveStarred();
            renderQuestions();
            syncChecklistUI();
        }};

        window.toggleLaterQuestion = function(id, event) {{
            if (event) {{
                event.stopPropagation();
            }}
            if (laterQuestions.has(id)) {{
                laterQuestions.delete(id);
            }} else {{
                laterQuestions.add(id);
            }}
            saveLater();
            renderQuestions();
            syncChecklistUI();
        }};

        // UNIT CHECKLIST & SYNCHRONIZATION ENGINE (YEAR-WISE & UNIT-WISE)
        let currentChecklistStatus = 'all';
        let currentChecklistUnit = 'all';
        let checklistSearchQuery = '';

        window.setChecklistUnit = function(unit, btn) {{
            currentChecklistUnit = String(unit);
            const container = document.getElementById('checklistUnitFilters');
            if (container) {{
                container.querySelectorAll('.filter-pill-btn').forEach(b => {{
                    b.classList.toggle('active', b.getAttribute('data-unit') === String(unit));
                }});
            }}
            syncChecklistUI();
        }};

        function syncChecklistUI() {{
            const visibleQuestions = RAW_QUESTIONS.filter(q => !hide2023 || String(q.year) !== '2023');
            // Questions marked as later are excluded from total count!
            const activeQuestions = visibleQuestions.filter(q => !laterQuestions.has(q.id));
            const total = activeQuestions.length;
            const completedCount = activeQuestions.filter(q => completedQuestions.has(q.id)).length;
            const totalPct = total > 0 ? Math.round((completedCount / total) * 100) : 0;

            const totalPctEl = document.getElementById('checklistTotalPct');
            const pctValEl = document.getElementById('checklistPctVal');
            const totalCountEl = document.getElementById('checklistTotalCount');
            const totalBarEl = document.getElementById('checklistTotalBar');
            const totalRingEl = document.getElementById('checklistTotalRing');
            const widgetEl = document.getElementById('checklistProgressWidget');

            if (pctValEl) {{
                pctValEl.textContent = `${{totalPct}}`;
            }} else if (totalPctEl) {{
                totalPctEl.innerHTML = `<span class="pct-num" id="checklistPctVal">${{totalPct}}</span><span class="pct-unit">%</span>`;
            }}
            if (totalCountEl) totalCountEl.textContent = `${{completedCount}} / ${{total}} Completed`;
            if (totalBarEl) totalBarEl.style.width = `${{totalPct}}%`;

            if (totalRingEl) {{
                const circumference = 109.96;
                if (totalPct === 0) {{
                    totalRingEl.style.strokeDashoffset = circumference;
                    totalRingEl.style.opacity = '0';
                }} else {{
                    totalRingEl.style.opacity = '1';
                    const offset = circumference - (totalPct / 100) * circumference;
                    totalRingEl.style.strokeDashoffset = offset;
                }}
            }}
            if (widgetEl) {{
                const filterActionHint = (typeof currentChecklistStatus !== 'undefined' && currentChecklistStatus === 'incomplete')
                    ? 'Click to show all questions'
                    : 'Click to filter incomplete';
                widgetEl.title = `Overall Completion: ${{totalPct}}% (${{completedCount}} of ${{total}} Done) • ${{filterActionHint}}`;
                widgetEl.setAttribute('aria-label', `Overall Completion: ${{totalPct}}% (${{completedCount}} of ${{total}} Done)`);
                widgetEl.classList.toggle('has-progress', totalPct > 0);
                widgetEl.classList.toggle('is-complete', totalPct === 100);
            }}

            const overlineEl = document.getElementById('checklistOverlineCount');
            if (overlineEl) overlineEl.textContent = `${{total}} PYQs`;

            const navBadge = document.getElementById('navChecklistBadge');
            if (navBadge) {{
                navBadge.textContent = `${{completedCount}}/${{total}}`;
            }}

            const navQBadge = document.getElementById('navQuestionsBadge');
            if (navQBadge) {{
                navQBadge.textContent = `${{total}}`;
            }}

            const allCountEl = document.getElementById('checklistAllCount');
            const incCountEl = document.getElementById('checklistIncompleteCount');
            const compCountEl = document.getElementById('checklistCompletedCount');
            const starCountEl = document.getElementById('checklistStarredCount');
            const laterCountEl = document.getElementById('checklistLaterCount');
            if (allCountEl) allCountEl.textContent = total;
            if (incCountEl) incCountEl.textContent = total - completedCount;
            if (compCountEl) compCountEl.textContent = completedCount;
            if (starCountEl) starCountEl.textContent = visibleQuestions.filter(q => starredQuestions.has(q.id)).length;
            if (laterCountEl) laterCountEl.textContent = visibleQuestions.filter(q => laterQuestions.has(q.id)).length;

            const yearTotal = {{ '2025': 0, '2024': 0, '2023': 0, '2022': 0 }};
            const yearDone = {{ '2025': 0, '2024': 0, '2023': 0, '2022': 0 }};
            const subheadTotal = {{}};
            const subheadDone = {{}};

            RAW_QUESTIONS.forEach(item => {{
                const y = String(item.year);
                const u = String(item.unit);
                const yuKey = `${{y}}-${{u}}`;

                const isLater = laterQuestions.has(item.id);
                const isDone = completedQuestions.has(item.id);
                const isStarred = starredQuestions.has(item.id);

                if (!isLater) {{
                    if (yearTotal[y] !== undefined) {{
                        yearTotal[y]++;
                        if (isDone) yearDone[y]++;
                    }}
                    subheadTotal[yuKey] = (subheadTotal[yuKey] || 0) + 1;
                    if (isDone) {{
                        subheadDone[yuKey] = (subheadDone[yuKey] || 0) + 1;
                    }}
                }}

                const cardEl = document.getElementById('chk-card-' + item.id);
                const btnEl = document.getElementById('chk-btn-' + item.id);
                const starBtn = document.getElementById('chk-star-btn-' + item.id);
                const laterBtn = document.getElementById('chk-later-btn-' + item.id);

                if (cardEl) {{
                    cardEl.classList.toggle('is-completed', isDone);
                    cardEl.classList.toggle('is-later', isLater);

                    let visible = true;
                    if (hide2023 && y === '2023') visible = false;
                    if (currentChecklistUnit !== 'all' && u !== String(currentChecklistUnit)) visible = false;
                    if (currentChecklistStatus === 'incomplete' && (isDone || isLater)) visible = false;
                    if (currentChecklistStatus === 'completed' && !isDone) visible = false;
                    if (currentChecklistStatus === 'starred' && !isStarred) visible = false;
                    if (currentChecklistStatus === 'later' && !isLater) visible = false;

                    if (visible && checklistSearchQuery) {{
                        const qText = (item.question || '').toLowerCase();
                        const tText = (item.topic || '').toLowerCase();
                        const noText = (item.q_no || '').toLowerCase();
                        const yText = String(item.year || '');
                        const mText = `${{item.marks}}m ${{item.marks}} marks`;
                        const sText = (item.solution || '').toLowerCase();
                        if (!qText.includes(checklistSearchQuery) && !tText.includes(checklistSearchQuery) && !noText.includes(checklistSearchQuery) && !yText.includes(checklistSearchQuery) && !mText.includes(checklistSearchQuery) && !sText.includes(checklistSearchQuery)) {{
                            visible = false;
                        }}
                    }}

                    cardEl.style.display = visible ? 'flex' : 'none';
                }}

                if (btnEl) {{
                    btnEl.classList.toggle('checked', isDone);
                }}
                if (starBtn) {{
                    starBtn.classList.toggle('is-starred', isStarred);
                    const svgEl = starBtn.querySelector('.star-icon');
                    if (svgEl) svgEl.setAttribute('fill', isStarred ? 'currentColor' : 'none');
                }}
                if (laterBtn) {{
                    laterBtn.classList.toggle('is-later', isLater);
                }}
                updateNoteButtonsAndBadges(item.id);
            }});

            ['2025', '2024', '2023', '2022'].forEach(y => {{
                const yTot = yearTotal[y] || 0;
                const yDn = yearDone[y] || 0;
                const yPct = yTot > 0 ? Math.round((yDn / yTot) * 100) : 0;

                const pillCount = document.getElementById(`yearPillCount-${{y}}`);
                if (pillCount) pillCount.textContent = `${{yDn}}/${{yTot}}`;

                for (let u = 1; u <= 5; u++) {{
                    const yuKey = `${{y}}-${{u}}`;
                    const subCountEl = document.getElementById(`unitSubheadCount-${{y}}-${{u}}`);
                    if (subCountEl && subheadTotal[yuKey]) {{
                        subCountEl.textContent = `${{subheadDone[yuKey] || 0}}/${{subheadTotal[yuKey]}}`;
                    }}

                    const subGroup = document.getElementById(`unit-subgroup-${{y}}-${{u}}`);
                    if (subGroup) {{
                        if (hide2023 && y === '2023') {{
                            subGroup.style.display = 'none';
                        }} else if (currentChecklistUnit !== 'all' && String(u) !== String(currentChecklistUnit)) {{
                            subGroup.style.display = 'none';
                        }} else {{
                            const visibleCards = subGroup.querySelectorAll('.checklist-card:not([style*="display: none"])');
                            subGroup.style.display = (visibleCards.length > 0 || (!checklistSearchQuery && currentChecklistStatus === 'all' && currentChecklistUnit === 'all')) ? 'flex' : 'none';
                        }}
                    }}
                }}

                const yearGroup = document.getElementById(`year-section-${{y}}`);
                if (yearGroup) {{
                    if (hide2023 && y === '2023') {{
                        yearGroup.style.display = 'none';
                    }} else {{
                        const visibleInYear = yearGroup.querySelectorAll('.checklist-card:not([style*="display: none"])');
                        yearGroup.style.display = (visibleInYear.length > 0 || (!checklistSearchQuery && currentChecklistStatus === 'all' && currentChecklistUnit === 'all')) ? 'block' : 'none';
                    }}
                }}
            }});

            const checklistPill2023 = document.getElementById('checklistYearPill-2023');
            if (checklistPill2023) {{
                checklistPill2023.style.display = hide2023 ? 'none' : 'inline-flex';
            }}
        }}

        window.jumpToChecklistYear = function(year, event) {{
            if (event) event.preventDefault();
            const section = document.getElementById(`year-section-${{year}}`);
            if (section) {{
                section.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }};

        window.setChecklistStatus = function(status) {{
            currentChecklistStatus = status;
            const group = document.getElementById('checklistStatusGroup');
            if (group) {{
                group.querySelectorAll('.filter-pill-btn, .checklist-status-pill').forEach(btn => {{
                    btn.classList.toggle('active', btn.getAttribute('data-status') === status);
                }});
            }}
            syncChecklistUI();
        }};

        window.toggleChecklistProgressFilter = function() {{
            const nextStatus = (currentChecklistStatus === 'incomplete') ? 'all' : 'incomplete';
            window.setChecklistStatus(nextStatus);
        }};

        window.toggleChecklistSolution = function(id, event) {{
            if (event && event.target && (
                event.target.closest('.checklist-solution-content') || 
                event.target.closest('.checklist-card-check') || 
                event.target.closest('.checklist-checkbox-btn') ||
                event.target.closest('.note-action-btn') ||
                event.target.closest('.icon-action-btn')
            )) {{
                return; // Do not collapse when selecting text inside answer, clicking checkbox, or note button!
            }}
            const cardEl = document.getElementById('chk-card-' + id);
            const solEl = document.getElementById('chk-sol-' + id);
            if (!cardEl || !solEl) return;

            const isOpen = solEl.classList.contains('open');
            if (isOpen) {{
                solEl.classList.remove('open');
                cardEl.classList.remove('is-open');
            }} else {{
                solEl.classList.add('open');
                cardEl.classList.add('is-open');
                const box = document.getElementById('chk-my-answer-box-' + id);
                if (box) box.innerHTML = renderAnswerBoxInner(id, true);
                if (window.renderAllMath) {{
                    try {{ window.renderAllMath(); }} catch(e) {{}}
                }}
            }}
        }};

        window.jumpToQuestionBank = function(questionId) {{
            const qObj = RAW_QUESTIONS.find(q => q.id === questionId);
            if (!qObj) return;

            if (String(qObj.year) === '2023' && hide2023) {{
                setHide2023(false);
            }}

            let filtersNeedReset = false;
            if (currentYear !== 'all' && String(currentYear) !== String(qObj.year)) {{
                currentYear = 'all';
                filtersNeedReset = true;
            }}
            if (currentUnit !== 'all' && String(currentUnit) !== String(qObj.unit)) {{
                currentUnit = 'all';
                filtersNeedReset = true;
            }}
            if (currentType !== 'all' && !qObj.type.toLowerCase().includes(currentType.toLowerCase())) {{
                currentType = 'all';
                filtersNeedReset = true;
            }}
            if (currentMarks !== 'all') {{
                if (currentMarks === '7' && qObj.marks !== 7 && qObj.marks !== 6) {{
                    currentMarks = 'all';
                    filtersNeedReset = true;
                }} else if (String(currentMarks) !== String(qObj.marks)) {{
                    currentMarks = 'all';
                    filtersNeedReset = true;
                }}
            }}
            if (currentRepeat === 'repeated') {{
                const repInfo = getRepeatInfo(qObj, RAW_QUESTIONS);
                if (!repInfo.isRep) {{
                    currentRepeat = 'all';
                    filtersNeedReset = true;
                }}
            }} else if (currentRepeat === '4x' || currentRepeat === '3x' || currentRepeat === '2x') {{
                const repInfo = getRepeatInfo(qObj, RAW_QUESTIONS);
                if (repInfo.countStr !== currentRepeat) {{
                    currentRepeat = 'all';
                    filtersNeedReset = true;
                }}
            }}
            if (currentStatus === 'incomplete' && completedQuestions.has(questionId)) {{
                currentStatus = 'all';
                filtersNeedReset = true;
            }} else if (currentStatus === 'completed' && !completedQuestions.has(questionId)) {{
                currentStatus = 'all';
                filtersNeedReset = true;
            }}
            if (searchQuery) {{
                const q = searchQuery.toLowerCase();
                const matches = (qObj.question || '').toLowerCase().includes(q) ||
                                (qObj.topic || '').toLowerCase().includes(q) ||
                                (qObj.id || '').toLowerCase().includes(q);
                if (!matches) {{
                    searchQuery = '';
                    filtersNeedReset = true;
                }}
            }}

            if (filtersNeedReset) {{
                saveFilters();
                syncFilterUI();
            }}

            switchPageView('questions');
            renderQuestions();

            setTimeout(() => {{
                const targetEl = document.getElementById(questionId);
                if (targetEl) {{
                    const solEl = document.getElementById('sol-' + questionId);
                    if (solEl && !solEl.classList.contains('open')) {{
                        solEl.classList.add('open');
                        targetEl.classList.add('is-open');
                    }}
                    targetEl.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    targetEl.classList.add('highlight-target');
                    setTimeout(() => {{
                        targetEl.classList.remove('highlight-target');
                    }}, 2500);
                }}
            }}, 60);
        }};

        // PAGE VIEW SWITCHER LOGIC
        window.switchPageView = function(pageId) {{
            document.querySelectorAll('.app-page-view').forEach(p => {{
                p.classList.remove('active');
            }});

            const targetView = document.getElementById('view-' + pageId);
            if (targetView) {{
                targetView.classList.add('active');
            }}

            document.querySelectorAll('.nav-link-btn').forEach(btn => {{
                btn.classList.toggle('active', btn.getAttribute('data-view') === pageId);
            }});

            try {{
                localStorage.setItem(STORAGE_KEY_VIEW, pageId);
            }} catch (e) {{}}

            if (history.pushState) {{
                history.pushState(null, null, '#' + pageId);
            }} else {{
                location.hash = pageId;
            }}

            if (pageId === 'syllabus') {{
                syncChecklistUI();
            }} else if (pageId === 'notes') {{
                renderNotesPage();
            }}

            window.scrollTo({{ top: 0, behavior: 'instant' }});
            const header = document.querySelector('.header');
            if (header) header.classList.remove('header-hidden');
        }};

        // Handle initial hash routing & restored state
        window.addEventListener('DOMContentLoaded', () => {{
            loadSavedFilters();
            syncFilterUI();
            sync2023ToggleUI();
            initProgressSync();

            let hash = window.location.hash.replace('#', '');
            if (hash === 'checklist') hash = 'syllabus';
            const validViews = ['questions', 'syllabus', 'formulas'];
            const savedView = localStorage.getItem(STORAGE_KEY_VIEW);

            if (hash === 'repeated') {{
                switchPageView('questions');
                const repBtn = document.querySelector('#repeatFilters [data-repeat="repeated"]');
                if (repBtn) repBtn.click();
            }} else if (validViews.includes(hash)) {{
                switchPageView(hash);
            }} else if (savedView && validViews.includes(savedView)) {{
                switchPageView(savedView);
            }} else {{
                switchPageView('questions');
            }}

            const checklistSearchInput = document.getElementById('checklistSearchInput');
            const clClearBtn = document.getElementById('checklistSearchClearBtn');
            if (checklistSearchInput) {{
                let clTimeout;
                checklistSearchInput.addEventListener('input', (e) => {{
                    if (clClearBtn) clClearBtn.style.display = e.target.value ? 'inline-flex' : 'none';
                    clearTimeout(clTimeout);
                    clTimeout = setTimeout(() => {{
                        checklistSearchQuery = e.target.value.trim().toLowerCase();
                        syncChecklistUI();
                    }}, 150);
                }});
                if (clClearBtn) {{
                    clClearBtn.addEventListener('click', () => {{
                        checklistSearchInput.value = '';
                        clClearBtn.style.display = 'none';
                        checklistSearchQuery = '';
                        syncChecklistUI();
                        checklistSearchInput.focus();
                    }});
                }}
            }}
            syncChecklistUI();

            const genTextarea = document.getElementById('generalNotesTextarea');
            if (genTextarea) {{
                genTextarea.value = generalNotes;
            }}
            updateNavBadges();
            renderNotesPage();
        }});

        window.addEventListener('hashchange', () => {{
            let hash = window.location.hash.replace('#', '');
            if (hash === 'checklist') hash = 'syllabus';
            const validViews = ['questions', 'syllabus', 'formulas'];
            if (hash === 'repeated') {{
                switchPageView('questions');
                const repBtn = document.querySelector('#repeatFilters [data-repeat="repeated"]');
                if (repBtn) repBtn.click();
            }} else if (validViews.includes(hash)) {{
                switchPageView(hash);
            }}
        }});

        // Theme Toggle Logic
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const htmlEl = document.documentElement;

        function setTheme(theme) {{
            htmlEl.setAttribute('data-theme', theme);
            localStorage.setItem('geotech_theme', theme);
            const metaTheme = document.getElementById('metaThemeColor');
            if (metaTheme) {{
                metaTheme.setAttribute('content', theme === 'dark' ? '#09090b' : '#fbfaf8');
            }}
            if (theme === 'dark') {{
                themeIcon.className = 'icon hgi-stroke hgi-sun-01';
                themeIcon.innerHTML = '';
            }} else {{
                themeIcon.className = 'icon hgi-stroke hgi-moon-02';
                themeIcon.innerHTML = '';
            }}
        }}

        const savedTheme = localStorage.getItem('geotech_theme') || 'dark';
        setTheme(savedTheme);

        themeToggle.addEventListener('click', () => {{
            const current = htmlEl.getAttribute('data-theme') || 'dark';
            setTheme(current === 'dark' ? 'light' : 'dark');
        }});

        // Keyboard Shortcut: '/' to search
        window.addEventListener('keydown', (e) => {{
            if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {{
                e.preventDefault();
                switchPageView('questions');
                document.getElementById('searchInput').focus();
            }}
        }});

        // Compatibility stub
        window.switchViewMode = function(mode) {{}};

        function getRepeatInfo(item, items) {{
            if (!item.cluster_id) return {{ isRep: false, countStr: '', rank: 4, freq: '' }};
            const clusterItems = items.filter(q => q.cluster_id && q.cluster_id === item.cluster_id);
            const clusterYears = Array.from(new Set(clusterItems.map(q => String(q.year)))).sort().reverse();
            if (clusterYears.length >= 4) {{
                return {{ isRep: true, countStr: '4x', rank: 1, freq: `${{clusterYears.length}} Exam Papers (${{clusterYears.join(', ')}})` }};
            }} else if (clusterYears.length === 3) {{
                return {{ isRep: true, countStr: '3x', rank: 2, freq: `${{clusterYears.length}} Exam Papers (${{clusterYears.join(', ')}})` }};
            }} else if (clusterYears.length === 2) {{
                return {{ isRep: true, countStr: '2x', rank: 3, freq: `Both ${{clusterYears.join(' & ')}} Papers` }};
            }}
            return {{ isRep: false, countStr: '', rank: 4, freq: '' }};
        }}

        // ----------------------------------------------------
        // PERSONAL NOTES & CUSTOM ANSWERS PERSISTENCE ENGINE
        // ----------------------------------------------------
        function renderMath(latex, isDisplay) {{
            if (!latex) return '';
            let clean = latex.trim();
            clean = clean.replace(/\\\\_/g, '_');
            clean = clean.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
            if (typeof katex !== 'undefined' && typeof katex.renderToString === 'function') {{
                try {{
                    const rendered = katex.renderToString(clean, {{
                        displayMode: isDisplay,
                        throwOnError: false
                    }});
                    return isDisplay ? `<div class="sol-math-block">${{rendered}}</div>` : rendered;
                }} catch(e) {{
                    console.warn('KaTeX render error:', e);
                }}
            }}
            return isDisplay ? `<div class="sol-math-block">$$${{clean}}$$</div>` : `$${{clean}}$`;
        }}

        function renderUserAnswerHtml(raw) {{
            if (!raw) return '';

            // 1. Extract block display math first so internal newlines and pipes are protected
            const mathBlocks = [];
            let s = raw;

            // Matches $$...$$, display math brackets (including multiline)
            const displayMathRegex = /(\\$\\$[\\s\\S]*?\\$\\$|\\\\{{1,2}}[[](?:[\\s\\S]*?)\\\\{{1,2}}[\\]])/g;
            s = s.replace(displayMathRegex, function(match) {{
                let inner = match.trim();
                if (inner.startsWith('$$') && inner.endsWith('$$')) {{
                    inner = inner.slice(2, -2);
                }} else {{
                    if (inner.startsWith('\\\\\\\\[')) inner = inner.slice(3);
                    else if (inner.startsWith('\\\\[')) inner = inner.slice(2);
                    if (inner.endsWith('\\\\\\\\]')) inner = inner.slice(0, -3);
                    else if (inner.endsWith('\\\\]')) inner = inner.slice(0, -2);
                }}
                const token = `@@MATH_BLOCK_${{mathBlocks.length}}@@`;
                mathBlocks.push(renderMath(inner.trim(), true));
                return `\\n\\n${{token}}\\n\\n`;
            }});

            // 2. Escape basic HTML entities
            s = s
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');

            // 3. Helper to format inline elements (inline math, bold, italic, code)
            function formatInline(text) {{
                if (!text) return '';
                let t = text;

                // 3a. Stash inline math tokens
                const inlineMath = [];
                t = t.replace(/\\\\{{1,2}}[(]([\\s\\S]*?)\\\\{{1,2}}[)]/g, function(m, c) {{
                    const token = `@@INLINE_MATH_${{inlineMath.length}}@@`;
                    inlineMath.push(renderMath(c, false));
                    return token;
                }});
                t = t.replace(/(?<!\\$)\\$([^\\$\\n]+)\\$(?!\\$)/g, function(m, c) {{
                    const token = `@@INLINE_MATH_${{inlineMath.length}}@@`;
                    inlineMath.push(renderMath(c, false));
                    return token;
                }});

                // 3b. Markdown formatting
                t = t.replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
                t = t.replace(/__(.*?)__/g, '<strong>$1</strong>');
                t = t.replace(/(^|[^\\*])\\*([^\\*]+)\\*([^\\*]|$)/g, '$1<em>$2</em>$3');
                t = t.replace(/`([^`]+)`/g, '<code>$1</code>');

                // 3c. Restore inline math
                t = t.replace(/@@INLINE_MATH_(\\d+)@@/g, function(m, idx) {{
                    return inlineMath[parseInt(idx, 10)] || '';
                }});

                return t;
            }}

            // Normalize newlines and split lines
            const rawLines = s.replaceAll(String.fromCharCode(13), '').split(String.fromCharCode(10));
            const out = [];

            function isTableDelimiter(line) {{
                const trimmed = line.trim();
                if (!trimmed.includes('-')) return false;
                const cells = splitRow(trimmed);
                if (cells.length === 0) return false;
                return cells.every(c => /^\\s*:?-{{2,}}:?\\s*$/.test(c));
            }}

            function isTableRow(line) {{
                const trimmed = line.trim();
                return trimmed.includes('|') && !trimmed.startsWith('#');
            }}

            function splitRow(line) {{
                let t = line.trim();
                if (t.startsWith('|')) t = t.slice(1);
                if (t.endsWith('|')) t = t.slice(0, -1);
                return t.split('|').map(c => c.trim());
            }}

            let i = 0;
            while (i < rawLines.length) {{
                let line = rawLines[i];
                let trimmed = line.trim();

                if (!trimmed) {{
                    i++;
                    continue;
                }}

                // Check for display math placeholder
                const mbMatch = trimmed.match(/^@@MATH_BLOCK_(\\d+)@@$/);
                if (mbMatch) {{
                    const idx = parseInt(mbMatch[1], 10);
                    if (mathBlocks[idx]) {{
                        out.push(mathBlocks[idx]);
                    }}
                    i++;
                    continue;
                }}

                // 1. Headings: #, ##, ###, ####
                const headingMatch = trimmed.match(/^(#+)\\s+(.*)$/);
                if (headingMatch && headingMatch[1].length <= 6) {{
                    const level = headingMatch[1].length;
                    let title = headingMatch[2].trim();
                    title = title.replace(/^<strong>(.*)<\\/strong>$/i, '$1');
                    title = formatInline(title);
                    const hTag = level === 1 ? 'h3' : (level === 2 ? 'h4' : (level === 3 ? 'h5' : 'h6'));
                    const hClass = level === 1 ? 'my-answer-heading h1' : (level === 2 ? 'my-answer-heading h2' : (level === 3 ? 'my-answer-heading h3' : 'my-answer-heading h4'));
                    out.push(`<${{hTag}} class="${{hClass}}">${{title}}</${{hTag}}>`);
                    i++;
                    continue;
                }}

                // 2. Markdown Table Detection
                if (isTableRow(trimmed) && i + 1 < rawLines.length && isTableDelimiter(rawLines[i + 1])) {{
                    const headerCells = splitRow(trimmed);
                    const delimCells = splitRow(rawLines[i + 1]);
                    const aligns = delimCells.map(c => {{
                        const left = c.startsWith(':');
                        const right = c.endsWith(':');
                        if (left && right) return 'center';
                        if (right) return 'right';
                        return 'left';
                    }});

                    i += 2; // skip header & delimiter

                    const bodyRows = [];
                    while (i < rawLines.length) {{
                        const rowLine = rawLines[i].trim();
                        if (!rowLine || !isTableRow(rowLine) || isTableDelimiter(rowLine)) {{
                            break;
                        }}
                        bodyRows.push(splitRow(rowLine));
                        i++;
                    }}

                    const colCount = headerCells.length;
                    const colWidth = colCount > 0 ? (100 / colCount).toFixed(2) + '%' : 'auto';

                    let tableHtml = '<div class="my-answer-table-wrapper"><table class="my-answer-table"><thead><tr>';
                    headerCells.forEach((th, idx) => {{
                        const align = aligns[idx] || 'left';
                        tableHtml += `<th style="text-align: ${{align}}; width: ${{colWidth}};">${{formatInline(th)}}</th>`;
                    }});
                    tableHtml += '</tr></thead><tbody>';

                    bodyRows.forEach(row => {{
                        tableHtml += '<tr>';
                        row.forEach((td, idx) => {{
                            const align = aligns[idx] || 'left';
                            tableHtml += `<td style="text-align: ${{align}};">${{formatInline(td)}}</td>`;
                        }});
                        tableHtml += '</tr>';
                    }});

                    tableHtml += '</tbody></table></div>';
                    out.push(tableHtml);
                    continue;
                }}

                // 3. Examples
                const exampleMatch = trimmed.match(/^(?:(?:<strong>)?(?:Example|Eg):?(?:<\\/strong>)?)\\s*(.*)$/i);
                if (exampleMatch) {{
                    out.push(`<div class="sol-example"><span class="example-tag">Eg</span> <span class="sol-example-text">${{formatInline(exampleMatch[1])}}</span></div>`);
                    i++;
                    continue;
                }}

                // 4. Notes: Note: or **Note:**
                const noteMatch = trimmed.match(/^(?:(?:<strong>)?Note:?(?:<\\/strong>)?)\\s*(.*)$/i);
                if (noteMatch) {{
                    out.push(`<div class="sol-note-box"><span class="note-tag">Note</span><div class="sol-note-text">${{formatInline(noteMatch[1])}}</div></div>`);
                    i++;
                    continue;
                }}

                // 5. Numbered Lists: 1. or 1. or 1)
                const numMatch = trimmed.match(/^(\\d+)(?:\\.|\\)|\\\\\\\\\\.)\\s+(.*)$/);
                if (numMatch) {{
                    const num = numMatch[1];
                    let content = numMatch[2].trim();
                    out.push(`<div class="sol-item-row"><span class="sol-item-num">${{num}}.</span><div class="sol-item-content">${{formatInline(content)}}</div></div>`);
                    i++;
                    continue;
                }}

                // 6. Bullet lists
                const bulletMatch = trimmed.match(/^[-*•+]\\s+(.*)$/);
                if (bulletMatch) {{
                    out.push(`<div class="sol-item-row"><span class="sol-item-num">&bull;</span><div class="sol-item-content">${{formatInline(bulletMatch[1])}}</div></div>`);
                    i++;
                    continue;
                }}

                // 7. Regular paragraph
                out.push(`<p class="my-answer-p">${{formatInline(trimmed)}}</p>`);
                i++;
            }}

            return out.join('');
        }}

        function renderAnswerBoxInner(qid, isChecklist = false) {{
            const noteObj = userNotes[qid];
            const text = typeof noteObj === 'string' ? noteObj : (noteObj && noteObj.answer ? noteObj.answer : '');
            if (!text.trim()) {{
                return `
                    <div class="my-answer-empty">
                        <i class="icon icon-md hgi-stroke hgi-note-01" style="color: var(--muted-foreground);"></i>
                        <div class="my-answer-empty-title">No Personal Answer Yet</div>
                        <p class="my-answer-empty-desc">You can save your own alternate solution, summary points, formula steps, or mnemonics for this question. It is saved in your data so you never lose it.</p>
                        <button type="button" class="my-answer-empty-btn" onclick="openNoteEditor('${{qid}}', event, ${{isChecklist}})">
                            <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                            <span>Write Your Answer</span>
                        </button>
                    </div>
                `;
            }}

            const formatted = renderUserAnswerHtml(text);
            const dateStr = (noteObj && noteObj.updated_at) ? new Date(noteObj.updated_at).toLocaleDateString(undefined, {{ month: 'short', day: 'numeric' }}) : '';

            return `
                <div class="my-answer-header">
                    <div class="my-answer-meta">
                        <span class="my-answer-badge">
                            <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                            My Answer
                        </span>
                        ${{dateStr ? `<span class="my-answer-time">Updated ${{dateStr}}</span>` : ''}}
                    </div>
                    <div class="my-answer-actions">
                        <button type="button" class="my-answer-btn-action" onclick="openNoteEditor('${{qid}}', event, ${{isChecklist}})" title="Edit your answer">
                            <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                            <span>Edit</span>
                        </button>
                        <button type="button" class="my-answer-btn-action btn-delete" onclick="deleteQuestionNote('${{qid}}', event, ${{isChecklist}})" title="Delete your answer">
                            <i class="icon icon-xs hgi-stroke hgi-delete-02"></i>
                            <span>Delete</span>
                        </button>
                    </div>
                </div>
                <div class="my-answer-text">${{formatted}}</div>
            `;
        }}

        function updateNoteButtonsAndBadges(qid) {{
            const noteObj = userNotes[qid];
            const hasNote = Boolean(noteObj && (typeof noteObj === 'string' ? noteObj.trim() : (noteObj.answer && noteObj.answer.trim())));

            // Switch row in Question Bank (hide if no answer is provided)
            const switchRow = document.getElementById('sol-switch-row-' + qid);
            if (switchRow) {{
                switchRow.style.display = hasNote ? '' : 'none';
            }}

            // Switch row in Checklist (hide if no answer is provided)
            const chkSwitchRow = document.getElementById('chk-switch-row-' + qid);
            if (chkSwitchRow) {{
                chkSwitchRow.style.display = hasNote ? '' : 'none';
            }}

            // Question Bank button
            const btn = document.getElementById('note-btn-' + qid);
            if (btn) {{
                btn.classList.toggle('has-note', hasNote);
                btn.title = hasNote ? 'Personal Answer Saved (Click to view/edit)' : 'Add personal answer / custom notes';
                let dot = btn.querySelector('.note-indicator-dot');
                if (hasNote && !dot) {{
                    dot = document.createElement('span');
                    dot.className = 'note-indicator-dot';
                    btn.appendChild(dot);
                }} else if (!hasNote && dot) {{
                    dot.remove();
                }}
            }}

            // Question Bank toggle pill
            const pillMine = document.getElementById('tab-mine-' + qid);
            if (pillMine) {{
                pillMine.classList.toggle('has-note', hasNote);
                let dot = pillMine.querySelector('.note-indicator-dot');
                if (hasNote && !dot) {{
                    dot = document.createElement('span');
                    dot.className = 'note-indicator-dot';
                    pillMine.appendChild(dot);
                }} else if (!hasNote && dot) {{
                    dot.remove();
                }}
            }}

            const editLabel = document.getElementById('btn-edit-label-' + qid);
            if (editLabel) {{
                editLabel.textContent = hasNote ? 'Edit My Answer' : 'Add My Answer';
            }}

            // Checklist button
            const chkBtn = document.getElementById('chk-note-btn-' + qid);
            if (chkBtn) {{
                chkBtn.classList.toggle('has-note', hasNote);
                chkBtn.title = hasNote ? 'Personal Answer Saved (Click to view/edit)' : 'Personal Answer / Notes';
                let dot = chkBtn.querySelector('.note-indicator-dot');
                if (hasNote && !dot) {{
                    dot = document.createElement('span');
                    dot.className = 'note-indicator-dot';
                    chkBtn.appendChild(dot);
                }} else if (!hasNote && dot) {{
                    dot.remove();
                }}
            }}

            // Checklist toggle pill
            const chkPillMine = document.getElementById('chk-tab-mine-' + qid);
            if (chkPillMine) {{
                chkPillMine.classList.toggle('has-note', hasNote);
                const dot = document.getElementById('chk-dot-' + qid);
                if (dot) dot.style.display = hasNote ? 'inline-block' : 'none';
            }}

            const chkEditLabel = document.getElementById('chk-btn-edit-text-' + qid);
            if (chkEditLabel) {{
                chkEditLabel.textContent = hasNote ? 'Edit My Answer' : 'Add My Answer';
            }}
        }}

        function updateNavBadges() {{
            const count = Object.keys(userNotes).filter(id => {{
                const n = userNotes[id];
                return Boolean(n && (typeof n === 'string' ? n.trim() : (n.answer && n.answer.trim())));
            }}).length;
            const badge = document.getElementById('navNotesBadge');
            if (badge) {{
                badge.textContent = `${{count}} ${{count === 1 ? 'Note' : 'Notes'}}`;
            }}
            const stat = document.getElementById('notesCountStat');
            if (stat) {{
                stat.textContent = `${{count}} ${{count === 1 ? 'Answer' : 'Answers'}} Saved`;
            }}
        }}

        window.handleNoteButtonClick = function(qid, event) {{
            if (event) event.stopPropagation();
            const itemEl = document.getElementById(qid);
            const solEl = document.getElementById('sol-' + qid);
            if (!itemEl || !solEl) return;

            if (!solEl.classList.contains('open')) {{
                solEl.classList.add('open');
                itemEl.classList.add('is-open');
            }}

            const noteObj = userNotes[qid];
            const hasNote = Boolean(noteObj && (typeof noteObj === 'string' ? noteObj.trim() : (noteObj.answer && noteObj.answer.trim())));

            if (!hasNote) {{
                switchSolutionTab(qid, 'mine', event, false);
                openNoteEditor(qid, event, false);
            }} else {{
                switchSolutionTab(qid, 'mine', event, false);
            }}
        }};

        window.handleChecklistNoteClick = function(qid, event) {{
            if (event) event.stopPropagation();
            const cardEl = document.getElementById('chk-card-' + qid);
            const solEl = document.getElementById('chk-sol-' + qid);
            if (!cardEl || !solEl) return;

            if (!solEl.classList.contains('open')) {{
                solEl.classList.add('open');
                cardEl.classList.add('is-open');
            }}

            const noteObj = userNotes[qid];
            const hasNote = Boolean(noteObj && (typeof noteObj === 'string' ? noteObj.trim() : (noteObj.answer && noteObj.answer.trim())));

            if (!hasNote) {{
                switchSolutionTab(qid, 'mine', event, true);
                openNoteEditor(qid, event, true);
            }} else {{
                switchSolutionTab(qid, 'mine', event, true);
            }}
        }};

        window.switchSolutionTab = function(qid, tab, event, isChecklist = false) {{
            if (event) event.stopPropagation();
            activeSolutionTab[qid] = tab;

            const prefix = isChecklist ? 'chk-' : '';
            const stdBtn = document.getElementById(prefix + 'tab-std-' + qid);
            const mineBtn = document.getElementById(prefix + 'tab-mine-' + qid);
            const stdPane = document.getElementById(prefix + 'pane-std-' + qid);
            const minePane = document.getElementById(prefix + 'pane-mine-' + qid);
            const editor = document.getElementById(prefix + 'editor-' + qid);

            if (editor) editor.style.display = 'none';

            const noteObj = userNotes[qid];
            const hasNote = Boolean(noteObj && (typeof noteObj === 'string' ? noteObj.trim() : (noteObj.answer && noteObj.answer.trim())));
            const switchRow = document.getElementById(isChecklist ? ('chk-switch-row-' + qid) : ('sol-switch-row-' + qid));
            if (switchRow) switchRow.style.display = hasNote ? '' : 'none';

            if (tab === 'mine') {{
                if (stdBtn) stdBtn.classList.remove('active');
                if (mineBtn) mineBtn.classList.add('active');
                if (stdPane) stdPane.style.display = 'none';
                if (minePane) {{
                    minePane.style.display = 'block';
                    const box = document.getElementById(prefix + 'my-answer-box-' + qid);
                    if (box) box.innerHTML = renderAnswerBoxInner(qid, isChecklist);
                }}
            }} else {{
                if (mineBtn) mineBtn.classList.remove('active');
                if (stdBtn) stdBtn.classList.add('active');
                if (minePane) minePane.style.display = 'none';
                if (stdPane) stdPane.style.display = 'block';
            }}

            if (window.renderAllMath) {{
                try {{ window.renderAllMath(); }} catch(e) {{}}
            }}
        }};

        window.openNoteEditor = function(qid, event, isChecklist = false) {{
            if (event) event.stopPropagation();
            const prefix = isChecklist ? 'chk-' : '';
            const editor = document.getElementById(prefix + 'editor-' + qid);
            const stdPane = document.getElementById(prefix + 'pane-std-' + qid);
            const minePane = document.getElementById(prefix + 'pane-mine-' + qid);
            const textarea = document.getElementById(prefix + 'note-input-' + qid);
            const switchRow = document.getElementById(isChecklist ? ('chk-switch-row-' + qid) : ('sol-switch-row-' + qid));

            if (!editor || !textarea) return;

            const cardEl = document.getElementById(isChecklist ? ('chk-card-' + qid) : qid);
            const solEl = document.getElementById(isChecklist ? ('chk-sol-' + qid) : ('sol-' + qid));
            if (cardEl && solEl && !solEl.classList.contains('open')) {{
                solEl.classList.add('open');
                cardEl.classList.add('is-open');
            }}

            if (switchRow) switchRow.style.display = 'none';
            if (stdPane) stdPane.style.display = 'none';
            if (minePane) minePane.style.display = 'none';
            editor.style.display = 'block';

            const noteObj = userNotes[qid];
            const currentText = typeof noteObj === 'string' ? noteObj : (noteObj && noteObj.answer ? noteObj.answer : '');
            textarea.value = currentText;
            textarea.focus();

            textarea.onkeydown = function(e) {{
                if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {{
                    e.preventDefault();
                    saveQuestionNote(qid, e, isChecklist);
                }}
            }};
        }};

        window.cancelNoteEditor = function(qid, event, isChecklist = false) {{
            if (event) event.stopPropagation();
            const prefix = isChecklist ? 'chk-' : '';
            const editor = document.getElementById(prefix + 'editor-' + qid);
            if (editor) editor.style.display = 'none';

            const noteObj = userNotes[qid];
            const hasNote = Boolean(noteObj && (typeof noteObj === 'string' ? noteObj.trim() : (noteObj.answer && noteObj.answer.trim())));
            const switchRow = document.getElementById(isChecklist ? ('chk-switch-row-' + qid) : ('sol-switch-row-' + qid));
            if (switchRow) switchRow.style.display = hasNote ? '' : 'none';

            const tab = hasNote ? (activeSolutionTab[qid] || 'mine') : 'standard';
            switchSolutionTab(qid, tab, event, isChecklist);
        }};

        window.saveQuestionNote = function(qid, event, isChecklist = false) {{
            if (event) event.stopPropagation();
            const prefix = isChecklist ? 'chk-' : '';
            const textarea = document.getElementById(prefix + 'note-input-' + qid);
            if (!textarea) return;

            const text = textarea.value.trim();
            if (text) {{
                userNotes[qid] = {{
                    answer: text,
                    updated_at: new Date().toISOString()
                }};
            }} else {{
                delete userNotes[qid];
            }}

            try {{
                localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(userNotes));
            }} catch(e) {{
                console.error('Error saving notes to localStorage:', e);
            }}

            setSyncStatus('saving', 'Saving...');
            if (diskSyncTimeout) clearTimeout(diskSyncTimeout);
            diskSyncTimeout = setTimeout(syncProgressToDisk, 300);

            updateNoteButtonsAndBadges(qid);
            activeSolutionTab[qid] = text ? 'mine' : 'standard';
            switchSolutionTab(qid, activeSolutionTab[qid], null, isChecklist);
            updateNavBadges();
            renderNotesPage();
            showQuickToast(text ? 'Answer saved in your data!' : 'Answer removed');

            // Also synchronize the counterpart view if open
            const otherPrefix = isChecklist ? '' : 'chk-';
            const otherBox = document.getElementById(otherPrefix + 'my-answer-box-' + qid);
            if (otherBox) {{
                otherBox.innerHTML = renderAnswerBoxInner(qid, !isChecklist);
            }}
        }};

        window.deleteQuestionNote = function(qid, event, isChecklist = false) {{
            if (event) event.stopPropagation();
            if (!confirm('Are you sure you want to delete your personal answer for this question?')) {{
                return;
            }}

            delete userNotes[qid];
            try {{
                localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(userNotes));
            }} catch(e) {{}}

            setSyncStatus('saving', 'Saving...');
            if (diskSyncTimeout) clearTimeout(diskSyncTimeout);
            diskSyncTimeout = setTimeout(syncProgressToDisk, 300);

            updateNoteButtonsAndBadges(qid);
            activeSolutionTab[qid] = 'standard';
            switchSolutionTab(qid, 'standard', null, isChecklist);
            updateNavBadges();
            renderNotesPage();
            showQuickToast('Answer removed');
        }};

        let generalNotesTimeout = null;
        window.handleGeneralNotesInput = function() {{
            const ta = document.getElementById('generalNotesTextarea');
            const statusText = document.getElementById('scratchpadStatusText');
            if (!ta) return;

            generalNotes = ta.value;
            if (statusText) statusText.textContent = 'Saving...';

            try {{
                localStorage.setItem(STORAGE_KEY_GENERAL_NOTES, generalNotes);
            }} catch(e) {{}}

            if (generalNotesTimeout) clearTimeout(generalNotesTimeout);
            generalNotesTimeout = setTimeout(() => {{
                syncProgressToDisk();
                if (statusText) statusText.textContent = 'Auto-saved';
            }}, 500);
        }};

        window.setNotesUnitFilter = function(unit, btn) {{
            notesUnitFilter = String(unit);
            const parent = document.getElementById('notesUnitFilters');
            if (parent) {{
                parent.querySelectorAll('.filter-pill-btn').forEach(b => b.classList.remove('active'));
            }}
            if (btn) btn.classList.add('active');
            renderNotesPage();
        }};

        window.filterNotesView = function() {{
            const input = document.getElementById('notesSearchInput');
            notesSearchQuery = input ? input.value.trim() : '';
            renderNotesPage();
        }};

        function renderNotesPage() {{
            const container = document.getElementById('savedNotesContainer');
            const countStat = document.getElementById('notesCountStat');
            if (!container) return;

            const qIds = Object.keys(userNotes).filter(id => {{
                const n = userNotes[id];
                return Boolean(n && (typeof n === 'string' ? n.trim() : (n.answer && n.answer.trim())));
            }});

            if (countStat) {{
                countStat.textContent = `${{qIds.length}} ${{qIds.length === 1 ? 'Answer' : 'Answers'}} Saved`;
            }}

            let matched = qIds.map(id => {{
                const qObj = RAW_QUESTIONS.find(q => q.id === id);
                return {{
                    id: id,
                    qObj: qObj || {{ id: id, q_no: id, question: id, year: 'PYQ', unit: 1, marks: 0, type: 'Note' }},
                    note: userNotes[id]
                }};
            }});

            if (notesUnitFilter !== 'all') {{
                matched = matched.filter(m => String(m.qObj.unit) === String(notesUnitFilter));
            }}

            if (notesSearchQuery) {{
                const sq = notesSearchQuery.toLowerCase();
                matched = matched.filter(m => {{
                    const text = (typeof m.note === 'string' ? m.note : (m.note.answer || '')).toLowerCase();
                    const qTitle = (m.qObj.question || '').toLowerCase();
                    const qNo = (m.qObj.q_no || '').toLowerCase();
                    return text.includes(sq) || qTitle.includes(sq) || qNo.includes(sq);
                }});
            }}

            if (matched.length === 0) {{
                container.innerHTML = `
                    <div class="empty-results" style="padding: 3rem 1.5rem; text-align: center; background: var(--card); border-radius: var(--radius-lg);">
                        <i class="icon icon-lg hgi-stroke hgi-note-01" style="margin-bottom: 0.75rem; color: var(--muted-foreground);"></i>
                        <div class="empty-results-title">${{qIds.length === 0 ? 'No personal answers saved yet' : 'No matching answers found'}}</div>
                        <p class="text-body-small" style="max-width: 460px; margin: 0.5rem auto 1.25rem; color: var(--muted-foreground);">
                            ${{qIds.length === 0 
                                ? 'Click the ✍️ pen icon on any question card in Questions or Checklist to save your own answers and study notes.' 
                                : 'Try clearing your search query or switching the unit filter to All Units.'}}
                        </p>
                        ${{qIds.length === 0 ? `
                            <button type="button" class="complete-btn" style="padding: 0.5rem 1.25rem; font-size: 0.85rem;" onclick="switchPageView('questions')">
                                <span>Browse Questions &rarr;</span>
                            </button>
                        ` : ''}}
                    </div>
                `;
                return;
            }}

            matched.sort((a, b) => {{
                if (a.qObj.unit !== b.qObj.unit) return a.qObj.unit - b.qObj.unit;
                if (a.qObj.year !== b.qObj.year) return Number(b.qObj.year) - Number(a.qObj.year);
                return (a.qObj.q_no || '').localeCompare(b.qObj.q_no || '');
            }});

            const html = matched.map(m => {{
                const q = m.qObj;
                const text = typeof m.note === 'string' ? m.note : (m.note.answer || '');
                const dateStr = (m.note && m.note.updated_at) ? new Date(m.note.updated_at).toLocaleDateString(undefined, {{ month: 'short', day: 'numeric' }}) : '';
                const formattedAnswer = renderUserAnswerHtml(text);

                return `
                    <div class="saved-note-card" id="saved-note-card-${{q.id}}">
                        <div class="saved-note-header">
                            <div class="saved-note-meta">
                                <span class="badge badge-subtle font-mono" style="font-weight: 700;">${{q.q_no || q.id}}</span>
                                <span class="badge badge-year-${{q.year}}">${{q.year}}</span>
                                <span class="badge badge-unit-${{q.unit}}">Unit ${{q.unit}}</span>
                                <span class="badge badge-subtle">${{q.marks}}M</span>
                                <span class="badge badge-subtle">${{q.type}}</span>
                            </div>
                            <div class="saved-note-actions">
                                <button type="button" class="my-answer-btn-action" onclick="jumpFromNotesToQuestion('${{q.id}}')" title="Open question in Questions">
                                    <i class="icon icon-xs hgi-stroke hgi-view"></i>
                                    <span>View Question &rarr;</span>
                                </button>
                                <button type="button" class="my-answer-btn-action" onclick="jumpFromNotesToQuestion('${{q.id}}', true)" title="Edit your answer">
                                    <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                    <span>Edit</span>
                                </button>
                                <button type="button" class="my-answer-btn-action btn-delete" onclick="deleteQuestionNote('${{q.id}}')" title="Delete this answer">
                                    <i class="icon icon-xs hgi-stroke hgi-delete-02"></i>
                                    <span>Delete</span>
                                </button>
                            </div>
                        </div>

                        <div class="saved-note-qtitle">${{q.question}}</div>

                        <div class="saved-note-content-box">
                            <div class="my-answer-header" style="margin-bottom: 0.5rem;">
                                <span class="my-answer-badge">My Answer</span>
                                ${{dateStr ? `<span class=\"my-answer-time\">${{dateStr}}</span>` : ''}}
                            </div>
                            <div class="my-answer-text">${{formattedAnswer}}</div>
                        </div>
                    </div>
                `;
            }});

            container.innerHTML = html.join('');
            if (window.renderAllMath) {{
                try {{ window.renderAllMath(); }} catch(e) {{}}
            }}
        }}

        window.jumpFromNotesToQuestion = function(qid, openEdit = false) {{
            switchPageView('questions');
            const qObj = RAW_QUESTIONS.find(q => q.id === qid);
            if (qObj && String(qObj.year) === '2023' && hide2023) {{
                setHide2023(false);
            }}

            if (currentYear !== 'all' || currentUnit !== 'all' || currentType !== 'all' || currentMarks !== 'all' || currentRepeat !== 'all' || currentStatus !== 'all' || searchQuery) {{
                resetFilters();
            }}

            setTimeout(() => {{
                const el = document.getElementById(qid);
                const solEl = document.getElementById('sol-' + qid);
                if (el && solEl) {{
                    if (!solEl.classList.contains('open')) {{
                        solEl.classList.add('open');
                        el.classList.add('is-open');
                    }}
                    switchSolutionTab(qid, 'mine');
                    if (openEdit) {{
                        openNoteEditor(qid);
                    }}
                    el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    el.classList.add('highlight-target');
                    setTimeout(() => el.classList.remove('highlight-target'), 2500);
                }}
            }}, 120);
        }};

        window.exportNotesJSON = function() {{
            const data = {{
                subject: CURRENT_SUBJECT_ID,
                exported_at: new Date().toISOString(),
                general_notes: generalNotes,
                notes: userNotes
            }};
            const blob = new Blob([JSON.stringify(data, null, 2)], {{ type: 'application/json' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${{CURRENT_SUBJECT_ID}}_study_notes_${{new Date().toISOString().slice(0, 10)}}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showQuickToast('Notes exported successfully!');
        }};

        window.triggerImportNotes = function() {{
            const input = document.getElementById('notesImportFileInput');
            if (input) input.click();
        }};

        window.handleImportFile = function(e) {{
            const file = e.target.files && e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(evt) {{
                try {{
                    const data = JSON.parse(evt.target.result);
                    if (data && typeof data.notes === 'object') {{
                        Object.assign(userNotes, data.notes);
                        if (data.general_notes) {{
                            generalNotes = (generalNotes ? (generalNotes + '\\n\\n' + data.general_notes) : data.general_notes);
                            const ta = document.getElementById('generalNotesTextarea');
                            if (ta) ta.value = generalNotes;
                            localStorage.setItem(STORAGE_KEY_GENERAL_NOTES, generalNotes);
                        }}
                        localStorage.setItem(STORAGE_KEY_NOTES, JSON.stringify(userNotes));
                        syncProgressToDisk();
                        renderQuestions();
                        renderNotesPage();
                        updateNavBadges();
                        showQuickToast(`Imported ${{Object.keys(data.notes).length}} notes!`);
                    }} else {{
                        alert('Invalid backup file. Expected JSON with "notes" object.');
                    }}
                }} catch(err) {{
                    alert('Error reading backup file: ' + err.message);
                }}
            }};
            reader.readAsText(file);
            e.target.value = '';
        }};

        window.copyAllNotesToClipboard = function() {{
            const qIds = Object.keys(userNotes).filter(id => {{
                const n = userNotes[id];
                return Boolean(n && (typeof n === 'string' ? n.trim() : (n.answer && n.answer.trim())));
            }});

            if (qIds.length === 0 && !generalNotes.trim()) {{
                showQuickToast('No notes to copy.');
                return;
            }}

            let textParts = [];
            textParts.push(`# ${{document.title.split('|')[0].trim()}} - Study Notes\n`);

            if (generalNotes.trim()) {{
                textParts.push(`## General Scratchpad & Revision Notes\n${{generalNotes.trim()}}\n\n---\n`);
            }}

            textParts.push(`## Saved Question Answers (${{qIds.length}} PYQs)\n`);

            qIds.forEach(id => {{
                const qObj = RAW_QUESTIONS.find(q => q.id === id);
                const qNo = qObj ? qObj.q_no : id;
                const year = qObj ? qObj.year : '';
                const unit = qObj ? `Unit ${{qObj.unit}}` : '';
                const marks = qObj ? `${{qObj.marks}}M` : '';
                const qTitle = qObj ? qObj.question : id;
                const n = userNotes[id];
                const ans = typeof n === 'string' ? n : (n.answer || '');

                textParts.push(`### [${{qNo}}] (${{year}} - ${{unit}} - ${{marks}})\n${{qTitle}}\n\n**My Answer:**\n${{ans}}\n\n---\n`);
            }});

            navigator.clipboard.writeText(textParts.join('\\n')).then(() => {{
                showQuickToast('All notes copied to clipboard!');
            }}).catch(err => {{
                console.error('Clipboard copy failed:', err);
                alert('Could not copy notes to clipboard.');
            }});
        }};

        function showQuickToast(msg) {{
            let toast = document.getElementById('appGlobalToast');
            if (!toast) {{
                toast = document.createElement('div');
                toast.id = 'appGlobalToast';
                toast.className = 'app-global-toast';
                document.body.appendChild(toast);
            }}
            toast.textContent = msg;
            toast.classList.add('visible');
            setTimeout(() => {{
                toast.classList.remove('visible');
            }}, 2400);
        }}

        // Render Engine for Questions (Click to open, constrained optimal line length)
        function renderQuestions() {{
            const container = document.getElementById('questionsContainer');
            const counterEl = document.getElementById('matchCounter');

            let items = RAW_QUESTIONS;
            if (hide2023) {{
                items = items.filter(q => String(q.year) !== '2023');
            }}
            // Questions marked as later are not counted in total count!
            let totalSource = items.filter(q => !laterQuestions.has(q.id)).length;

            const filtered = items.filter(item => {{
                if (currentYear !== 'all' && String(item.year) !== String(currentYear)) {{
                    return false;
                }}

                if (currentUnit !== 'all' && String(item.unit) !== String(currentUnit)) {{
                    return false;
                }}

                if (currentType !== 'all') {{
                    const t = item.type || '';
                    if (!t.toLowerCase().includes(currentType.toLowerCase())) {{
                        return false;
                    }}
                }}

                if (currentMarks !== 'all') {{
                    if (currentMarks === '7') {{
                        if (item.marks !== 7 && item.marks !== 6) {{
                            return false;
                        }}
                    }} else if (String(item.marks) !== String(currentMarks)) {{
                        return false;
                    }}
                }}

                if (currentRepeat === 'repeated') {{
                    const repInfo = getRepeatInfo(item, items);
                    if (!repInfo.isRep) {{
                        return false;
                    }}
                }} else if (currentRepeat === '4x' || currentRepeat === '3x' || currentRepeat === '2x') {{
                    const repInfo = getRepeatInfo(item, items);
                    if (repInfo.countStr !== currentRepeat) {{
                        return false;
                    }}
                }}

                if (currentStatus === 'incomplete') {{
                    if (completedQuestions.has(item.id) || laterQuestions.has(item.id)) {{
                        return false;
                    }}
                }} else if (currentStatus === 'completed') {{
                    if (!completedQuestions.has(item.id)) {{
                        return false;
                    }}
                }} else if (currentStatus === 'starred') {{
                    if (!starredQuestions.has(item.id)) {{
                        return false;
                    }}
                }} else if (currentStatus === 'later') {{
                    if (!laterQuestions.has(item.id)) {{
                        return false;
                    }}
                }}

                if (searchQuery) {{
                    const q = searchQuery.toLowerCase();
                    const titleText = (item.title || item.topic || '').toLowerCase();
                    const questionText = (item.canonical_question || item.question || '').toLowerCase();
                    const solutionText = (item.master_solution || item.solution || '').toLowerCase();
                    const idText = (item.id || '').toLowerCase();
                    const yearText = String(item.year || '').toLowerCase();
                    const marksText = `${{item.marks}}m ${{item.marks}} marks`;
                    if (!titleText.includes(q) && !questionText.includes(q) && !solutionText.includes(q) && !idText.includes(q) && !yearText.includes(q) && !marksText.includes(q)) {{
                        return false;
                    }}
                }}

                return true;
            }});

            // SORTING: When repeat filter is selected (Most Repeated, 4x, 3x, 2x), group questions strictly by repeat tier (4x first, then 3x, then 2x), then unit, then cluster, then year
            if (currentRepeat === 'repeated' || currentRepeat === '4x' || currentRepeat === '3x' || currentRepeat === '2x') {{
                filtered.sort((a, b) => {{
                    const repA = getRepeatInfo(a, items);
                    const repB = getRepeatInfo(b, items);
                    if (repA.rank !== repB.rank) {{
                        return repA.rank - repB.rank;
                    }}
                    const unitA = a.cluster_unit || a.unit || 1;
                    const unitB = b.cluster_unit || b.unit || 1;
                    if (unitA !== unitB) {{
                        return unitA - unitB;
                    }}
                    if (a.cluster_id !== b.cluster_id) {{
                        return (a.cluster_order || 999) - (b.cluster_order || 999);
                    }}
                    if (a.year !== b.year) {{
                        return Number(b.year) - Number(a.year);
                    }}
                    return (a.q_no || '').localeCompare(b.q_no || '');
                }});
            }} else {{
                filtered.sort((a, b) => {{
                    if (a.year !== b.year) {{
                        return Number(b.year) - Number(a.year);
                    }}
                    if (a.unit !== b.unit) {{
                        return a.unit - b.unit;
                    }}
                    return (a.id || '').localeCompare(b.id || '');
                }});
            }}

            if (counterEl) {{
                if (currentStatus === 'later') {{
                    counterEl.textContent = `${{filtered.length}} marked for later`;
                }} else if (currentStatus === 'starred') {{
                    counterEl.textContent = `${{filtered.length}} of ${{totalSource}} starred`;
                }} else {{
                    const matchedActive = filtered.filter(q => !laterQuestions.has(q.id)).length;
                    counterEl.textContent = `${{matchedActive}} of ${{totalSource}} matched`;
                }}
            }}

            if (filtered.length === 0) {{
                const isAllDoneIncomplete = currentStatus === 'incomplete' && completedQuestions.size > 0 && completedQuestions.size === totalSource;
                container.innerHTML = `
                    <div class="empty-results">
                        <i class="icon icon-lg hgi-stroke hgi-search-01" style="margin-bottom: 0.5rem; color: var(--muted-foreground);"></i>
                        <div class="empty-results-title">${{isAllDoneIncomplete ? 'All questions marked as completed!' : 'No matching questions found'}}</div>
                        <p class="text-body-small">${{isAllDoneIncomplete ? 'Great work! Switch status to "All" or "Completed" to review your work.' : 'Your active filter combination has no matches.'}}</p>
                        <div style="margin-top: 1rem;">
                            <button type="button" class="reset-filters-btn" style="display: inline-flex;" onclick="window.resetAllFilters && window.resetAllFilters()">
                                <i class="icon icon-xs hgi-stroke hgi-arrow-reload-horizontal"></i>
                                <span>Reset All Filters</span>
                            </button>
                        </div>
                    </div>
                `;
                return;
            }}

            // RENDER INDIVIDUAL QUESTION CARDS
            const htmlParts = [];
            let prevRank = null;
            let prevClusterId = null;
            let prevUnit = null;

            const isRepeatMode = (currentRepeat === 'repeated' || currentRepeat === '4x' || currentRepeat === '3x' || currentRepeat === '2x');

            filtered.forEach((item, index) => {{
                const repBadgeInfo = getRepeatInfo(item, items);
                const itemUnit = item.cluster_unit || item.unit || 1;

                if (isRepeatMode) {{
                    if (repBadgeInfo.rank !== prevRank) {{
                        const tierMetaMap = {{
                            1: {{ label: '4x Repeated', bClass: 'badge-repeat-4x', desc: '100% Guaranteed Across All 4 Exam Papers (2025, 2024, 2023, 2022)' }},
                            2: {{ label: '3x Repeated', bClass: 'badge-repeat-3x', desc: '75% High Probability Across 3 Exam Papers' }},
                            3: {{ label: '2x Repeated', bClass: 'badge-repeat-2x', desc: '50% Medium Probability Across 2 Exam Papers' }}
                        }};
                        const tierMeta = tierMetaMap[repBadgeInfo.rank] || {{ label: 'Repeated', bClass: 'badge-subtle', desc: 'Recurring Topics' }};

                        htmlParts.push(`
                        <div class="q-tier-section-divider ${{index === 0 ? 'first-tier' : ''}}">
                            <div class="q-tier-section-title">
                                <span class="badge ${{tierMeta.bClass}}">${{tierMeta.label}}</span>
                                <span class="card-overline">${{tierMeta.desc}}</span>
                            </div>
                        </div>
                        `);
                        prevUnit = null;
                    }}

                    if (currentUnit === 'all' && itemUnit !== prevUnit) {{
                        htmlParts.push(`
                        <div class="q-unit-section-divider">
                            <div class="q-unit-section-title">
                                <span class="badge badge-unit-${{itemUnit}}">Unit ${{itemUnit}}</span>
                                <span class="card-overline">${{item.unit_name || ''}}</span>
                            </div>
                        </div>
                        `);
                    }}

                    if (item.cluster_id !== prevClusterId) {{
                        const bClass = repBadgeInfo.countStr === '4x' ? 'badge-repeat-4x' : (repBadgeInfo.countStr === '3x' ? 'badge-repeat-3x' : 'badge-repeat-2x');
                        htmlParts.push(`
                        <div class="q-topic-section-header">
                            <div class="q-topic-section-meta">
                                <span class="badge ${{bClass}}">${{repBadgeInfo.countStr || item.repeat_count_str || '2x'}}</span>
                                <span class="card-overline">Recurring Concept (${{repBadgeInfo.freq || item.cluster_rep_frequency || 'Multi-Year Repeat'}})</span>
                            </div>
                            <h4 class="q-topic-section-title">${{item.cluster_title}}</h4>
                        </div>
                        `);
                    }}

                    prevRank = repBadgeInfo.rank;
                    prevClusterId = item.cluster_id;
                    prevUnit = itemUnit;
                }}

                const isCompleted = completedQuestions.has(item.id);
                const isStarred = starredQuestions.has(item.id);
                const isLater = laterQuestions.has(item.id);
                const unitBadgeClass = `badge-unit-${{item.unit}}`;
                const cardBadgeClass = repBadgeInfo.countStr === '4x' ? 'badge-repeat-4x' : (repBadgeInfo.countStr === '3x' ? 'badge-repeat-3x' : (repBadgeInfo.countStr === '2x' ? 'badge-repeat-2x' : 'badge-subtle'));
                const userNoteObj = userNotes[item.id];
                const hasNote = Boolean(userNoteObj && (typeof userNoteObj === 'string' ? userNoteObj.trim() : (userNoteObj.answer && userNoteObj.answer.trim())));
                const activeTab = activeSolutionTab[item.id] || 'standard';

                htmlParts.push(`
                <div class="q-item ${{isCompleted ? 'is-completed' : ''}} ${{isLater ? 'is-later' : ''}}" id="${{item.id}}" onclick="toggleSolution('${{item.id}}', event)">
                    <div class="q-item-header">
                        <div class="q-item-left-meta">
                            <span class="q-item-qno">${{item.q_no}}</span>
                            <div class="q-item-badges">
                                <span class="badge badge-year-${{item.year}}">${{item.year}}</span>
                                <span class="badge ${{unitBadgeClass}}">Unit ${{item.unit}}</span>
                                <span class="badge badge-subtle">${{item.type}}</span>
                                <span class="badge badge-subtle">${{item.marks}}M</span>
                                ${{repBadgeInfo.isRep && repBadgeInfo.countStr ? `<span class=\"badge ${{cardBadgeClass}}\" title=\"${{repBadgeInfo.freq}}\">${{repBadgeInfo.countStr}}</span>` : ''}}
                            </div>
                        </div>

                        <div class="q-item-right-meta">
                            <div class="q-item-actions">
                                <button class="icon-action-btn star-action-btn ${{isStarred ? 'is-starred' : ''}}" 
                                        id="star-btn-${{item.id}}" 
                                        onclick="toggleStarQuestion('${{item.id}}', event)" 
                                        title="${{isStarred ? 'Starred (Click to unstar)' : 'Star this question'}}" 
                                        aria-label="${{isStarred ? 'Starred' : 'Star question'}}">
                                    <i class="icon icon-xs star-icon hgi-stroke hgi-star"></i>
                                </button>
                                <button class="icon-action-btn later-action-btn ${{isLater ? 'is-later' : ''}}" 
                                        id="later-btn-${{item.id}}" 
                                        onclick="toggleLaterQuestion('${{item.id}}', event)" 
                                        title="${{isLater ? 'Marked for later (Click to remove)' : 'Mark for later'}}" 
                                        aria-label="${{isLater ? 'Marked for later' : 'Mark for later'}}">
                                    <i class="icon icon-xs clock-icon hgi-stroke hgi-clock-01"></i>
                                </button>
                                <button class="icon-action-btn note-action-btn ${{hasNote ? 'has-note' : ''}}" 
                                        id="note-btn-${{item.id}}" 
                                        onclick="handleNoteButtonClick('${{item.id}}', event)" 
                                        title="${{hasNote ? 'Personal Answer Saved (Click to view/edit)' : 'Add personal answer / custom notes'}}"
                                        aria-label="Personal Notes">
                                    <i class="icon icon-xs pen-icon hgi-stroke hgi-pencil-edit-01"></i>
                                    ${{hasNote ? '<span class="note-indicator-dot"></span>' : ''}}
                                </button>
                                <button class="complete-btn ${{isCompleted ? 'is-completed' : ''}}" 
                                        onclick="toggleCompleteQuestion('${{item.id}}', event)" 
                                        title="${{isCompleted ? 'Click to unmark as complete' : 'Click to mark as complete'}}"
                                        aria-label="${{isCompleted ? 'Mark incomplete' : 'Mark complete'}}">
                                    <i class="icon icon-xs check-icon hgi-stroke hgi-checkmark-circle-02"></i>
                                    <span>${{isCompleted ? 'Completed' : 'Mark Done'}}</span>
                                </button>
                                <i class="icon icon-sm chevron-icon hgi-stroke hgi-chevron-down"></i>
                            </div>
                        </div>
                    </div>

                    <h3 class="q-item-title">${{item.question}}</h3>

                    <div class="q-solution-content" id="sol-${{item.id}}">
                        <div class="sol-view-switch-row" id="sol-switch-row-${{item.id}}" style="${{hasNote ? '' : 'display:none;'}}" onclick="event.stopPropagation()">
                            <div class="sol-view-pills">
                                <button type="button" class="sol-view-pill ${{activeTab === 'standard' ? 'active' : ''}}" id="tab-std-${{item.id}}" onclick="switchSolutionTab('${{item.id}}', 'standard', event)">
                                    <i class="icon icon-xs hgi-stroke hgi-checkmark-badge-01"></i>
                                    <span>Verified Solution</span>
                                </button>
                                <button type="button" class="sol-view-pill ${{activeTab === 'mine' ? 'active' : ''}} ${{hasNote ? 'has-note' : ''}}" id="tab-mine-${{item.id}}" onclick="switchSolutionTab('${{item.id}}', 'mine', event)">
                                    <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                    <span>My Answer</span>
                                    ${{hasNote ? '<span class="note-indicator-dot"></span>' : ''}}
                                </button>
                            </div>

                            <div class="sol-view-quick-actions">
                                <button type="button" class="sol-btn-edit-note" id="btn-edit-note-${{item.id}}" onclick="openNoteEditor('${{item.id}}', event)" title="Edit or write your personal answer">
                                    <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                    <span id="btn-edit-label-${{item.id}}">${{hasNote ? 'Edit My Answer' : 'Add My Answer'}}</span>
                                </button>
                            </div>
                        </div>

                        <div class="solution-pane" id="pane-std-${{item.id}}" style="${{activeTab === 'standard' ? '' : 'display:none;'}}">
                            <div class="solution-body">
                                ${{item.formatted_solution}}
                            </div>
                        </div>

                        <div class="solution-pane" id="pane-mine-${{item.id}}" style="${{activeTab === 'mine' ? '' : 'display:none;'}}">
                            <div class="my-answer-container" id="my-answer-box-${{item.id}}">
                                ${{renderAnswerBoxInner(item.id)}}
                            </div>
                        </div>

                        <div class="note-editor-container" id="editor-${{item.id}}" style="display: none;" onclick="event.stopPropagation()">
                            <div class="note-editor-header">
                                <div class="note-editor-title">
                                    <i class="icon icon-xs hgi-stroke hgi-pencil-edit-01"></i>
                                    <span>Personal Answer / Custom Solution</span>
                                </div>
                                <span class="note-editor-meta">Saved in data &bull; Never lost</span>
                            </div>
                            <p class="note-editor-hint">Write your alternate explanation, textbook derivation steps, or revision notes. Supports line breaks, numbered points, and math ($...$).</p>
                            <textarea class="note-editor-textarea" id="note-input-${{item.id}}" rows="7" placeholder="Write your own custom answer or notes for this question here..."></textarea>
                            <div class="note-editor-footer">
                                <span class="note-editor-keys">Press <kbd>Ctrl</kbd> + <kbd>Enter</kbd> to save</span>
                                <div class="note-editor-buttons">
                                    <button type="button" class="note-btn-cancel" onclick="cancelNoteEditor('${{item.id}}', event)">Cancel</button>
                                    <button type="button" class="note-btn-save" onclick="saveQuestionNote('${{item.id}}', event)">
                                        <i class="icon icon-xs hgi-stroke hgi-tick-01"></i>
                                        <span>Save Answer</span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                `);
            }});

            container.innerHTML = htmlParts.join('');
        }}

        // TOGGLE SOLUTION ON ENTIRE CARD CLICK
        window.toggleSolution = function(id, event) {{
            if (event && event.target && (
                event.target.closest('.q-solution-content') || 
                event.target.closest('.complete-btn') ||
                event.target.closest('.note-action-btn') ||
                event.target.closest('.icon-action-btn')
            )) {{
                return; // Do not collapse when clicking note button, complete button, or inside answer!
            }}
            const itemEl = document.getElementById(id);
            const solEl = document.getElementById('sol-' + id);
            if (!itemEl || !solEl) return;

            const isOpen = solEl.classList.contains('open');
            if (isOpen) {{
                solEl.classList.remove('open');
                itemEl.classList.remove('is-open');
            }} else {{
                solEl.classList.add('open');
                itemEl.classList.add('is-open');
                const box = document.getElementById('my-answer-box-' + id);
                if (box) box.innerHTML = renderAnswerBoxInner(id, false);
                if (window.renderAllMath) {{
                    try {{ window.renderAllMath(); }} catch(e) {{}}
                }}
            }}
        }};

        function setupFilterGroup(containerId, stateVarSetter) {{
            const group = document.getElementById(containerId);
            if (!group) return;
            group.querySelectorAll('.filter-pill-btn').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    group.querySelectorAll('.filter-pill-btn').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    stateVarSetter(btn);
                    saveFilters();
                    renderQuestions();
                }});
            }});
        }}

        setupFilterGroup('yearFilters', btn => currentYear = btn.getAttribute('data-year'));
        setupFilterGroup('repeatFilters', btn => {{
            currentRepeat = btn.getAttribute('data-repeat');
            if (currentRepeat !== 'all') {{
                currentYear = 'all';
                currentType = 'all';
                currentMarks = 'all';
                syncFilterUI();
            }}
        }});
        setupFilterGroup('statusFilters', btn => currentStatus = btn.getAttribute('data-status'));
        setupFilterGroup('unitFilters', btn => currentUnit = btn.getAttribute('data-unit'));
        setupFilterGroup('typeFilters', btn => currentType = btn.getAttribute('data-type'));
        setupFilterGroup('marksFilters', btn => currentMarks = btn.getAttribute('data-marks'));

        let searchTimeout;
        const searchInput = document.getElementById('searchInput');
        const searchClearBtn = document.getElementById('searchClearBtn');

        if (searchInput) {{
            searchInput.addEventListener('input', (e) => {{
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {{
                    searchQuery = e.target.value.trim();
                    if (searchClearBtn) {{
                        searchClearBtn.style.display = searchQuery ? 'inline-flex' : 'none';
                    }}
                    saveFilters();
                    renderQuestions();
                }}, 200);
            }});
        }}

        if (searchClearBtn && searchInput) {{
            searchClearBtn.addEventListener('click', () => {{
                searchInput.value = '';
                searchQuery = '';
                searchClearBtn.style.display = 'none';
                saveFilters();
                renderQuestions();
            }});
        }}

        window.resetAllFilters = function() {{
            currentYear = 'all';
            currentUnit = 'all';
            currentType = 'all';
            currentMarks = 'all';
            currentRepeat = 'all';
            currentStatus = 'all';
            searchQuery = '';
            const searchInput = document.getElementById('searchInput') || document.getElementById('searchBar');
            if (searchInput) searchInput.value = '';
            const searchClearBtn = document.getElementById('searchClearBtn');
            if (searchClearBtn) searchClearBtn.style.display = 'none';
            saveFilters();
            syncFilterUI();
            renderQuestions();
        }};

        const resetBtn = document.getElementById('resetFiltersBtn');
        if (resetBtn) {{
            resetBtn.addEventListener('click', () => {{
                window.resetAllFilters();
            }});
        }}

        const clearDoneBtn = document.getElementById('clearCompletedBtn');
        if (clearDoneBtn) {{
            clearDoneBtn.addEventListener('click', () => {{
                const visibleDone = RAW_QUESTIONS.filter(q => (!hide2023 || String(q.year) !== '2023') && completedQuestions.has(q.id));
                if (visibleDone.length === 0) return;
                const promptMsg = hide2023
                    ? ('Unmark ' + visibleDone.length + ' completed questions in 2025, 2024 & 2022?')
                    : ('Unmark all ' + completedQuestions.size + ' completed questions?');
                if (confirm(promptMsg)) {{
                    visibleDone.forEach(q => completedQuestions.delete(q.id));
                    saveCompleted();
                    renderQuestions();
                    syncChecklistUI();
                }}
            }});
        }}

        const completionBadge = document.getElementById('completionProgressBadge');
        if (completionBadge) {{
            completionBadge.addEventListener('click', () => {{
                currentStatus = currentStatus === 'completed' ? 'all' : 'completed';
                saveFilters();
                syncFilterUI();
                renderQuestions();
            }});
        }}

        // SCROLL TO TOP ENGINE
        window.scrollToTop = function() {{
            try {{
                window.scrollTo({{
                    top: 0,
                    behavior: 'smooth'
                }});
            }} catch(e) {{
                window.scrollTo(0, 0);
            }}
            try {{
                document.documentElement.scrollTo({{ top: 0, behavior: 'smooth' }});
                document.body.scrollTo({{ top: 0, behavior: 'smooth' }});
            }} catch(e) {{}}
            const header = document.querySelector('.header');
            if (header) header.classList.remove('header-hidden');
        }};

        // AUTO-HIDE NAVBAR ON SCROLL DOWN, REVEAL ON SCROLL UP
        (function() {{
            const header = document.querySelector('.header');
            if (!header) return;

            let lastScrollY = Math.max(0, window.pageYOffset || document.documentElement.scrollTop || 0);
            let ticking = false;
            const scrollThreshold = 8;
            const topThreshold = 64;

            function updateNavbar() {{
                const currentScrollY = Math.max(0, window.pageYOffset || document.documentElement.scrollTop || 0);
                const maxScrollY = (document.documentElement.scrollHeight || document.body.scrollHeight) - window.innerHeight;
                const scrollDelta = currentScrollY - lastScrollY;

                if (currentScrollY <= topThreshold) {{
                    header.classList.remove('header-hidden');
                }} else if (currentScrollY >= maxScrollY - 20) {{
                    // Near bottom bounce
                }} else if (Math.abs(scrollDelta) >= scrollThreshold) {{
                    if (scrollDelta > 0) {{
                        // Scrolling DOWN -> Hide navbar
                        header.classList.add('header-hidden');
                    }} else {{
                        // Scrolling UP -> Reveal navbar
                        header.classList.remove('header-hidden');
                    }}
                }}

                lastScrollY = currentScrollY;
                ticking = false;
            }}

            window.addEventListener('scroll', function() {{
                if (!ticking) {{
                    window.requestAnimationFrame(updateNavbar);
                    ticking = true;
                }}
            }}, {{ passive: true }});
        }})();

        renderQuestions();
    </script>

    <!-- Floating Back to Top Button (Always Visible in Bottom-Right Corner) -->
    <button id="scrollToTopBtn" class="scroll-to-top-btn" aria-label="Scroll to top" title="Scroll to top" onclick="scrollToTop()">
        <i class="hgi-stroke hgi-arrow-up-01"></i>
    </button>

    <!-- MOBILE BOTTOM APP NAVIGATION (iOS/Android Native App Style) -->
    <nav class="mobile-bottom-nav" aria-label="Mobile App Navigation">
        <button class="mobile-nav-item nav-link-btn active" data-view="questions" onclick="switchPageView('questions')" aria-label="Questions">
            <i class="mobile-nav-icon hgi-stroke hgi-help-circle"></i>
            <span class="mobile-nav-label">Questions</span>
        </button>
        <button class="mobile-nav-item nav-link-btn" data-view="syllabus" onclick="switchPageView('syllabus')" aria-label="Checklist">
            <i class="mobile-nav-icon hgi-stroke hgi-task-01"></i>
            <span class="mobile-nav-label">Checklist</span>
        </button>
        <button class="mobile-nav-item nav-link-btn" data-view="formulas" onclick="switchPageView('formulas')" aria-label="Formulas">
            <i class="mobile-nav-icon hgi-stroke hgi-function-of-x"></i>
            <span class="mobile-nav-label">Formulas</span>
        </button>
        <a href="timetable.html" class="mobile-nav-item nav-link-timetable" aria-label="Exam Timetable">
            <i class="mobile-nav-icon hgi-stroke hgi-calendar-03"></i>
            <span class="mobile-nav-label">Timetable</span>
        </a>
    </nav>
</body>
</html>"""

    if ctx.formula_module and hasattr(ctx.formula_module, "enhance_html"):
        html_template = ctx.formula_module.enhance_html(html_template)

    out_file = repo_root / ctx.output_filename
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_template)

    if write_index:
        with open(repo_root / "index.html", "w", encoding="utf-8") as f:
            f.write(html_template)
        print(f"Updated index.html & {ctx.output_filename}: {ctx.name} ({ctx.code}) dashboard generated successfully!")
    else:
        print(f"Updated {ctx.output_filename}: {ctx.name} ({ctx.code}) dashboard generated successfully!")

    return html_template

def main():
    parser = argparse.ArgumentParser(description="Exam Intelligence & PYQ Platform Dashboard Generator")
    parser.add_argument("subject", nargs="?", default=None, help="Subject ID to build (default: active subject from subjects/registry.json)")
    parser.add_argument("--list", action="store_true", help="List all registered subjects")
    parser.add_argument("--all", action="store_true", help="Build dashboards for all ready subjects")
    parser.add_argument("--new", nargs=3, metavar=("ID", "NAME", "CODE"), help="Scaffold a new subject (e.g. --new rcc 'Design of Reinforced Concrete Structures' 'CE 41001')")
    args = parser.parse_args()

    if args.list:
        subjects = list_subjects()
        print(f"{'ID':<15} {'CODE':<12} {'STATUS':<12} {'NAME'}")
        print("-" * 65)
        for s in subjects:
            print(f"{s.get('id', ''):<15} {s.get('code', ''):<12} {s.get('status', 'planned'):<12} {s.get('name', '')}")
        return

    if args.new:
        sub_id, name, code = args.new
        target = scaffold_new_subject(sub_id, name, code)
        print(f"Successfully scaffolded new subject '{sub_id}' at {target}")
        return

    if args.all:
        subjects = list_subjects()
        for s in subjects:
            if s.get("status") == "ready":
                is_default = s.get("is_default", False)
                build_dashboard_for_subject(s["id"], write_index=is_default)
        return

    # Default build
    build_dashboard_for_subject(args.subject, write_index=True)

if __name__ == "__main__":
    main()
