import json
import re
import compile_data
import formula_showcase

# Load canonical topics
with open("canonical_data.json", "r", encoding="utf-8") as f:
    canonical_topics = json.load(f)

raw_questions = compile_data.questions

def clean_num(raw):
    if not raw:
        return ""
    if raw == "&bull;":
        return "&bull;"
    return re.sub(r"[\.\)]+$", "", raw) + "."

def format_solution(html):
    if not html:
        return ""
    html = formula_showcase.enhance_solution_math(html)
    html = html.replace("•", "&bull;").replace("·", "&bull;")
    html = html.replace("<br>\n<br>", "<br>").replace("<br><br>", "<br>")
    
    split_pattern = r'<br>\s*(?=(?:<strong>|\d+\.\s*|[a-zA-Z]\)\s*|[a-zA-Z]\.\s*|&bull;\s*|\(\d+\)\s*|\([a-zA-Z]\)\s*))'
    parts = re.split(split_pattern, html)
    formatted = []
    
    for p in parts:
        p = p.strip()
        if not p:
            continue
            
        m_num_outer = re.match(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", p)
        m_num_inner = re.match(r"^<strong>(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", p)
        
        num_str = ""
        if m_num_outer:
            num_str = clean_num(m_num_outer.group(1))
        elif m_num_inner:
            num_str = clean_num(m_num_inner.group(1))
            
        m_title_desc = re.match(r"^(?:(?:\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*)?<strong>(.*?)</strong>:?\s*(.*)$", p, re.DOTALL)
        m_num_only = re.match(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s+(.+)$", p, re.DOTALL)
        
        if m_title_desc:
            raw_title = m_title_desc.group(1).strip()
            raw_desc = m_title_desc.group(2).strip()
            
            title_clean = re.sub(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", "", raw_title).rstrip(":")
            desc_clean = re.sub(r"^(?:<br\s*/?>|\s)+", "", raw_desc)
            
            example_html = ""
            m_ex = re.search(r'(?:<br\s*/?>|\s)*<em>Example:?</em>\s*(.*?)(?=(?:<br\s*/?>\s*<strong>|<br\s*/?>\s*&bull;|$))', desc_clean, flags=re.IGNORECASE | re.DOTALL)
            if m_ex:
                desc_clean = desc_clean[:m_ex.start()].strip()
                example_text = m_ex.group(1).strip()
                example_html = f'<div class="sol-item-example"><span class="example-label">Example:</span> {example_text}</div>'
            else:
                desc_clean = re.sub(r'<em>Example:?</em>', '<span class="example-label">Example:</span>', desc_clean, flags=re.IGNORECASE)

            if not desc_clean and not example_html:
                if num_str and num_str != "&bull;" and not title_clean.startswith(num_str):
                    heading_text = f"{num_str} {title_clean}:"
                else:
                    heading_text = f"{title_clean}:"
                formatted.append(f'<div class="sol-heading">{heading_text}</div>')
            elif not num_str and len(title_clean) > 30:
                formatted.append(f'<div class="sol-heading">{title_clean}:</div><div class="sol-body-text">{desc_clean}{example_html}</div>')
            elif not num_str and raw_desc.startswith("<br>"):
                formatted.append(f'<div class="sol-heading">{title_clean}:</div><div class="sol-body-text">{desc_clean}{example_html}</div>')
            else:
                num_html = f'<span class="sol-item-num">{num_str}</span>' if num_str else ""
                formatted.append(f"""<div class="sol-item-row">
    {num_html}
    <div class="sol-item-content">
        <span class="sol-item-title">{title_clean}:</span> 
        <span class="sol-item-text">{desc_clean}</span>
        {example_html}
    </div>
</div>""")
        elif m_num_only and m_num_only.group(2).strip():
            num = clean_num(m_num_only.group(1))
            desc_clean = re.sub(r"^(?:<br\s*/?>|\s)+", "", m_num_only.group(2).strip())
            
            example_html = ""
            m_ex = re.search(r'(?:<br\s*/?>|\s)*<em>Example:?</em>\s*(.*?)(?=(?:<br\s*/?>\s*<strong>|<br\s*/?>\s*&bull;|$))', desc_clean, flags=re.IGNORECASE | re.DOTALL)
            if m_ex:
                desc_clean = desc_clean[:m_ex.start()].strip()
                example_text = m_ex.group(1).strip()
                example_html = f'<div class="sol-item-example"><span class="example-label">Example:</span> {example_text}</div>'
            else:
                desc_clean = re.sub(r'<em>Example:?</em>', '<span class="example-label">Example:</span>', desc_clean, flags=re.IGNORECASE)

            formatted.append(f"""<div class="sol-item-row">
    <span class="sol-item-num">{num}</span>
    <div class="sol-item-content">
        <span class="sol-item-text">{desc_clean}</span>
        {example_html}
    </div>
</div>""")
        else:
            p_clean = re.sub(r"^(\d+\.|[a-zA-Z]\)|[a-zA-Z]\.|\(\d+\)|\([a-zA-Z]\)|&bull;)\s*", r'<span class="sol-item-num">\1</span> ', p)
            formatted.append(f'<div class="sol-step">{p_clean}</div>')
            
    return "".join(formatted)

q_order = {q['id']: idx for idx, q in enumerate(raw_questions)}

cluster_first_seen = {}
for t in canonical_topics:
    q_ids = [q['id'] if isinstance(q, dict) else q for q in t.get('questions', [])]
    indices = [q_order[qid] for qid in q_ids if qid in q_order]
    cluster_first_seen[t['id']] = min(indices) if indices else 999

unit_titles = {
    1: 'Lateral Earth Pressure',
    2: 'Shear Strength & Slope Stability',
    3: 'Shallow Foundations',
    4: 'Deep Foundations (Piles)',
    5: 'Soil Exploration & Testing'
}

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
    q['formatted_solution'] = format_solution(q['solution'])
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
    c['formatted_solution'] = format_solution(c['master_solution'])

canonical_json_str = json.dumps(canonical_topics).replace("</script>", "<\\/script>")
raw_json_str = json.dumps(raw_questions).replace("</script>", "<\\/script>")

def build_unit_checklist_html(questions):
    unit_titles = {
        1: 'Lateral Earth Pressure',
        2: 'Shear Strength & Slope Stability',
        3: 'Shallow Foundations',
        4: 'Deep Foundations (Piles)',
        5: 'Soil Exploration & Testing'
    }

    from collections import defaultdict
    tree = defaultdict(lambda: defaultdict(list))
    for q in questions:
        tree[str(q['year'])][q['unit']].append(q)

    for y in tree:
        for u in tree[y]:
            tree[y][u].sort(key=lambda x: x.get('q_no', ''))

    years = sorted(tree.keys(), reverse=True)

    html = []
    html.append(f'''
        <!-- ====================================================
             PAGE VIEW 2: PYQ CHECKLIST (YEAR-WISE & UNIT-WISE)
             ==================================================== -->
        <div class="app-page-view" id="view-syllabus">
            <div class="page-header-row" style="margin-bottom: 1rem;">
                <span class="card-overline">Study Tracker &bull; <span id="checklistOverlineCount">{len(questions)} PYQs</span></span>
                <h1 class="page-title">PYQ Checklist</h1>
            </div>

            <!-- CHECKLIST GLOBAL PROGRESS CARD -->
            <div class="checklist-summary-card">
                <div class="checklist-summary-left">
                    <div class="checklist-summary-meta">
                        <span class="card-overline">Total Completion</span>
                        <span class="checklist-stat-pct" id="checklistTotalPct">0%</span>
                    </div>
                    <div class="checklist-stat-count" id="checklistTotalCount">0 / {len(questions)} Completed</div>
                    <div class="checklist-progress-bar-bg">
                        <div class="checklist-progress-bar-fill" id="checklistTotalBar" style="width: 0%;"></div>
                    </div>
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
                    <button class="checklist-toggle-2022-pill" id="checklistToggle2022Btn" onclick="toggleHide2022()" title="Include 2022 Paper in checklist" style="display: none;">
                        + Include 2022 Paper (25 Qs)
                    </button>
                </div>
            </div>

            <!-- CHECKLIST CONTROLS & SEARCH TOOLBAR -->
            <div class="checklist-toolbar">
                <div class="checklist-status-filters" id="checklistStatusGroup">
                    <button class="checklist-status-pill active" data-status="all" onclick="setChecklistStatus('all')">
                        All <span class="nav-badge" id="checklistAllCount">{len(questions)}</span>
                    </button>
                    <button class="checklist-status-pill" data-status="incomplete" onclick="setChecklistStatus('incomplete')">
                        Incomplete <span class="nav-badge" id="checklistIncompleteCount">{len(questions)}</span>
                    </button>
                    <button class="checklist-status-pill" data-status="completed" onclick="setChecklistStatus('completed')">
                        Done <span class="nav-badge" id="checklistCompletedCount">0</span>
                    </button>
                </div>

                <div class="checklist-search-box">
                    <svg class="icon icon-sm checklist-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <input type="text" class="checklist-search-input" id="checklistSearchInput" placeholder="Filter questions..." aria-label="Filter questions">
                </div>
            </div>

            <!-- YEAR SECTIONS WITH UNITS INSIDE -->
            <div class="checklist-years-container">
    ''')

    for y in years:
        total_y = sum(len(tree[y][u]) for u in tree[y])
        html.append(f'''
                <section class="checklist-year-group" id="year-section-{y}">
                    <div class="checklist-year-header">
                        <div class="checklist-year-info">
                            <span class="badge badge-year-{y}">{y} Paper</span>
                            <span class="checklist-year-stat-text" id="yearStatText-{y}">0 / {total_y} Done (0%)</span>
                        </div>
                        <div class="checklist-year-mini-bar">
                            <div class="checklist-year-mini-bar-fill" id="yearMiniBar-{y}" style="width: 0%;"></div>
                        </div>
                    </div>

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
                safe_question = q['question']
                formatted_sol = q.get('formatted_solution', '')

                html.append(f'''
                                <div class="checklist-card" id="chk-card-{q['id']}" data-id="{q['id']}" data-year="{y}" data-unit="{u}" onclick="toggleChecklistSolution('{q['id']}', event)" title="Click to view answer">
                                    <div class="checklist-card-check" onclick="event.stopPropagation()">
                                        <button class="checklist-checkbox-btn" 
                                                id="chk-btn-{q['id']}"
                                                onclick="toggleCompleteQuestion('{q['id']}', event)"
                                                title="Toggle completed"
                                                aria-label="Toggle completion for {q['id']}">
                                            <svg class="icon chk-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                                <polyline points="20 6 9 17 4 12"></polyline>
                                            </svg>
                                        </button>
                                    </div>
                                    <div class="checklist-card-content">
                                        <div class="checklist-card-header-row">
                                            <div class="checklist-card-meta">
                                                <span class="badge badge-subtle font-mono">{q['q_no']}</span>
                                                <span class="badge badge-year-{y}">{y}</span>
                                                <span class="badge badge-subtle">{q['marks']}M</span>
                                                <span class="badge badge-subtle">{q['type']}</span>
                                                {rep_badge}
                                            </div>
                                            <div class="checklist-card-actions">
                                                <svg class="icon icon-sm chevron-icon chk-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                                    <polyline points="6 9 12 15 18 9"></polyline>
                                                </svg>
                                            </div>
                                        </div>
                                        <div class="checklist-card-title">{safe_question}</div>
                                        <div class="checklist-solution-content" id="chk-sol-{q['id']}">
                                            <div class="solution-body">
                                                {formatted_sol}
                                            </div>
                                            <div class="checklist-solution-footer">
                                                <button type="button" class="checklist-jump-link" onclick="jumpToQuestionBank('{q['id']}'); event.stopPropagation();" title="Open full view in Question Bank">
                                                    <span>Open in Question Bank &rarr;</span>
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

unit_checklist_html = build_unit_checklist_html(raw_questions)

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
    <title>Geotechnical Engineering - II (CE-41007) | PYQ Analysis &amp; High-Yield Solutions</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
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
            border: none !important;
            outline: none;
            -webkit-tap-highlight-color: transparent;
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

        .icon {{
            display: inline-block;
            width: 1.125rem;
            height: 1.125rem;
            stroke-width: 2;
            stroke: currentColor;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
            vertical-align: middle;
            flex-shrink: 0;
        }}

        .icon-sm {{ width: 0.875rem; height: 0.875rem; }}
        .icon-lg {{ width: 1.375rem; height: 1.375rem; }}

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
            background-color: var(--background);
            color: var(--muted-foreground);
            line-height: 1.2;
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
           2022 VISIBILITY TOGGLE (HEADER NAVBAR & CONTROL PANEL)
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
            background-color: var(--pastel-sand-foreground);
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

        .checklist-toggle-2022-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.75rem;
            background-color: var(--pastel-sand-bg);
            color: var(--pastel-sand-foreground);
            border-radius: var(--radius-full);
            border: 1px dashed var(--pastel-sand-foreground);
            cursor: pointer;
            font-size: 0.75rem;
            font-weight: 600;
            transition: background-color 0.2s ease, transform 0.15s ease;
        }}

        .checklist-toggle-2022-pill:hover {{
            background-color: var(--secondary-hover);
            transform: translateY(-1px);
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

        .nav-link-timetable {{
            background-color: var(--pastel-peach-bg) !important;
            color: var(--pastel-peach-foreground) !important;
            font-weight: 600 !important;
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
           COMPACT, SPACE-EFFICIENT CONTROL BAR
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

        /* TOP TOOLBAR: SEARCH & LIVE SESSION ACTIONS */
        .control-panel-toolbar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.85rem;
            flex-wrap: wrap;
            padding-bottom: 0.75rem;
            position: relative;
        }}

        .control-panel-toolbar::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 1px;
            background-color: var(--secondary);
        }}

        .search-box-wrapper {{
            position: relative;
            flex: 1;
            max-width: 440px;
            min-width: 240px;
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

        .control-panel-actions,
        .control-panel-meta {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            margin-left: auto;
            flex-wrap: wrap;
        }}

        .match-counter-badge {{
            display: inline-flex;
            align-items: center;
            font-size: 0.75rem;
            font-weight: 500;
            color: var(--muted-foreground);
            background-color: var(--secondary);
            padding: 0.25rem 0.6rem;
            border-radius: var(--radius-full);
            white-space: nowrap;
            height: 30px;
            box-sizing: border-box;
            line-height: 1;
        }}

        .progress-pill-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--pastel-sage-foreground);
            background-color: var(--pastel-sage-bg);
            padding: 0.25rem 0.65rem;
            border-radius: var(--radius-full);
            white-space: nowrap;
            cursor: pointer;
            user-select: none;
            height: 30px;
            box-sizing: border-box;
            line-height: 1;
            transition: opacity 0.15s ease, transform 0.1s ease;
        }}

        .progress-pill-badge:hover {{
            opacity: 0.85;
        }}

        .progress-pill-badge:active {{
            transform: scale(0.97);
        }}

        .clear-completed-btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            padding: 0.25rem 0.65rem;
            background-color: var(--pastel-rose-bg);
            color: var(--pastel-rose-foreground);
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 600;
            cursor: pointer;
            transition: opacity 0.15s ease, transform 0.1s ease;
            white-space: nowrap;
            height: 30px;
            box-sizing: border-box;
            line-height: 1;
        }}

        .clear-completed-btn:hover {{
            opacity: 0.85;
        }}

        .clear-completed-btn:active {{
            transform: scale(0.97);
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
            height: 30px;
            box-sizing: border-box;
            line-height: 1;
        }}

        .reset-filters-btn:hover {{
            background-color: var(--secondary-hover);
            color: var(--foreground);
        }}

        .reset-filters-btn:active {{
            transform: scale(0.97);
        }}

        /* FILTER ROWS & SEGMENTED CONTROLS */
        .control-panel-filters {{
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
        }}

        .control-panel-filter-row {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            flex-wrap: wrap;
        }}

        .filter-subgroup {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .filter-group-label {{
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
            margin-right: 0.15rem;
            user-select: none;
            white-space: nowrap;
        }}

        .filter-pills-row {{
            display: inline-flex;
            align-items: center;
            background-color: var(--secondary);
            padding: 2.5px;
            border-radius: var(--radius-full);
            gap: 2px;
        }}

        .filter-divider {{
            width: 1px;
            height: 16px;
            background-color: var(--secondary-hover);
            margin: 0 0.15rem;
            opacity: 0.6;
            flex-shrink: 0;
        }}

        .filter-pill-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.25rem;
            padding: 0.25rem 0.6rem;
            background: transparent;
            color: var(--muted-foreground);
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 500;
            cursor: pointer;
            transition: color 0.15s ease, background-color 0.15s ease, box-shadow 0.15s ease, transform 0.1s ease;
            white-space: nowrap;
            user-select: none;
            line-height: 1.25;
        }}

        .filter-pill-btn:hover {{
            color: var(--foreground);
            background-color: var(--secondary-hover);
        }}

        .filter-pill-btn:active {{
            transform: scale(0.97);
        }}

        .filter-pill-btn.active {{
            background-color: var(--filter-pill-active-bg);
            color: var(--filter-pill-active-fg);
            font-weight: 600;
            box-shadow: var(--filter-pill-active-shadow);
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
            background-color: var(--card);
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
        .checklist-summary-card {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }}

        @media (min-width: 960px) {{
            .checklist-summary-card {{
                flex-direction: row;
                align-items: center;
                justify-content: space-between;
                gap: 2rem;
            }}
        }}

        .checklist-summary-left {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            min-width: 260px;
        }}

        .checklist-summary-meta {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .checklist-stat-pct {{
            font-size: var(--font-size-stat);
            line-height: var(--line-height-stat);
            font-weight: 700;
            color: var(--pastel-sage-foreground);
            font-family: var(--font-family-mono);
        }}

        .checklist-stat-count {{
            font-size: 0.90625rem;
            color: var(--foreground-secondary, var(--foreground));
            font-weight: 500;
        }}

        .checklist-progress-bar-bg {{
            width: 100%;
            height: 8px;
            background-color: var(--secondary);
            border-radius: var(--radius-full);
            overflow: hidden;
            position: relative;
        }}

        .checklist-progress-bar-fill {{
            height: 100%;
            background-color: var(--pastel-sage-foreground);
            border-radius: var(--radius-full);
            transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        .checklist-summary-units {{
            display: flex;
            align-items: center;
            gap: 0.45rem;
            flex-wrap: wrap;
        }}

        .checklist-year-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.4rem 0.75rem;
            background-color: var(--secondary);
            border-radius: var(--radius-md);
            text-decoration: none;
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .checklist-year-pill:hover {{
            background-color: var(--secondary-hover);
            transform: translateY(-1px);
        }}

        .unit-pill-count {{
            font-size: 0.75rem;
            font-weight: 700;
            font-family: var(--font-family-mono);
            color: var(--foreground);
        }}

        /* CHECKLIST CONTROLS BAR */
        .checklist-toolbar {{
            background-color: var(--card);
            border-radius: var(--radius-lg);
            padding: 0.65rem 1rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-sm);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            flex-wrap: wrap;
        }}

        .checklist-status-filters {{
            display: inline-flex;
            gap: 0.25rem;
            background-color: var(--secondary);
            padding: 0.2rem;
            border-radius: var(--radius-md);
        }}

        .checklist-status-pill {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.75rem;
            background: transparent;
            color: var(--muted-foreground);
            font-size: 0.8125rem;
            font-weight: 500;
            border-radius: calc(var(--radius-md) - 2px);
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .checklist-status-pill:hover {{
            color: var(--foreground);
        }}

        .checklist-status-pill.active {{
            background-color: var(--card);
            color: var(--foreground);
            font-weight: 600;
            box-shadow: var(--shadow-sm);
        }}

        .checklist-search-box {{
            position: relative;
            flex: 1;
            max-width: 320px;
            min-width: 220px;
        }}

        .checklist-search-input {{
            width: 100%;
            background-color: var(--input-bg);
            border-radius: var(--radius-md);
            padding: 0.4rem 0.75rem 0.4rem 2.1rem;
            font-size: 0.8125rem;
            color: var(--foreground);
            height: 34px;
        }}

        .checklist-search-icon {{
            position: absolute;
            left: 0.65rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--muted-foreground);
            pointer-events: none;
        }}

        /* YEAR GROUPS & SUB-UNITS */
        .checklist-year-group {{
            margin-bottom: 2rem;
        }}

        .checklist-year-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 0.75rem 1.15rem;
            background-color: var(--secondary);
            border-radius: var(--radius-lg);
            margin-bottom: 0.85rem;
            flex-wrap: wrap;
        }}

        .checklist-year-info {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .checklist-year-stat-text {{
            font-size: 0.8125rem;
            font-weight: 600;
            color: var(--muted-foreground);
            font-family: var(--font-family-mono);
        }}

        .checklist-year-mini-bar {{
            width: 80px;
            height: 6px;
            background-color: var(--card);
            border-radius: var(--radius-full);
            overflow: hidden;
        }}

        .checklist-year-mini-bar-fill {{
            height: 100%;
            background-color: var(--pastel-sage-foreground);
            border-radius: var(--radius-full);
            transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
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
            box-shadow: var(--shadow-md);
            opacity: 1 !important;
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

            .match-counter-badge, .progress-pill-badge, .reset-filters-btn, .clear-completed-btn, .panel-year-toggle-btn {{
                font-size: 0.72rem;
                padding: 0.2rem 0.5rem;
                height: 28px;
            }}

            .checklist-summary-card {{
                padding: 1rem;
                gap: 0.85rem;
                border-radius: var(--radius-md);
            }}

            .checklist-summary-meta {{
                gap: 0.5rem;
            }}

            .checklist-summary-units {{
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: none;
                flex-wrap: nowrap;
                width: 100%;
                padding-bottom: 4px;
            }}

            .checklist-summary-units::-webkit-scrollbar {{
                display: none;
            }}

            .checklist-year-pill {{
                padding: 0.35rem 0.65rem;
                font-size: 0.75rem;
                flex-shrink: 0;
            }}

            .checklist-toolbar {{
                padding: 0.65rem 0.85rem;
                flex-direction: column;
                align-items: stretch;
                gap: 0.65rem;
                border-radius: var(--radius-md);
            }}

            .checklist-status-filters {{
                display: flex;
                width: 100%;
            }}

            .checklist-status-pill {{
                flex: 1;
                justify-content: center;
                text-align: center;
                padding: 0.35rem 0.5rem;
                font-size: 0.78rem;
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

            .checklist-year-header {{
                padding: 0.65rem 0.85rem;
                border-radius: var(--radius-md);
                gap: 0.5rem;
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

            .q-item-right-meta {{
                gap: 0.35rem;
                width: 100%;
                justify-content: space-between;
                margin-left: 0;
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
            <div class="brand" onclick="switchPageView('questions')" title="Geotechnical Engineering - II">
                <span class="brand-title">Geotechnical Engineering - II</span>
            </div>

            <!-- Nav links with badge view -->
            <ul class="nav-links">
                <li>
                    <button class="nav-link-btn active" data-view="questions" onclick="switchPageView('questions')">
                        <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
                        Question Bank
                        <span class="nav-badge" id="navQuestionsBadge">{len(raw_questions)} PYQs</span>
                    </button>
                </li>
                <li>
                    <button class="nav-link-btn" data-view="syllabus" onclick="switchPageView('syllabus')">
                        <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
                        Unit Checklist
                        <span class="nav-badge" id="navChecklistBadge">5 Units</span>
                    </button>
                </li>
                <li>
                    <button class="nav-link-btn" data-view="formulas" onclick="switchPageView('formulas')">
                        <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg>
                        Formulas
                    </button>
                </li>
                <li>
                    <a href="timetable.html" class="nav-link-btn nav-link-timetable" title="View Exam Timetable">
                        <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        Timetable
                    </a>
                </li>
            </ul>

            <div class="nav-actions">
                <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle Theme" title="Toggle Light/Dark Theme">
                    <svg class="icon" id="themeIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <circle cx="12" cy="12" r="5"></circle>
                        <line x1="12" y1="1" x2="12" y2="3"></line>
                        <line x1="12" y1="21" x2="12" y2="23"></line>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                        <line x1="1" y1="12" x2="3" y2="12"></line>
                        <line x1="21" y1="12" x2="23" y2="12"></line>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                    </svg>
                </button>
            </div>
        </div>
    </header>

    <div class="container">

        <!-- ====================================================
             PAGE VIEW 1: QUESTIONS & SOLUTIONS ENGINE (DEFAULT)
             ==================================================== -->
        <div class="app-page-view active" id="view-questions">
            <!-- Compact, Space-Efficient Control Panel (Refined Segmented Architecture) -->
            <div class="control-panel">
                <!-- TOP UTILITY & SEARCH TOOLBAR -->
                <div class="control-panel-toolbar">
                    <div class="search-box-wrapper">
                        <svg class="icon icon-sm search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        <input type="text" class="search-input" id="searchInput" placeholder="Search topics, questions, formulas..." aria-label="Search questions">
                        <kbd class="search-kbd-hint" aria-hidden="true">/</kbd>
                        <button class="search-clear-btn" id="searchClearBtn" title="Clear search" aria-label="Clear search" style="display: none;">
                            <svg class="icon icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                        </button>
                    </div>

                    <div class="control-panel-actions">
                        <button class="panel-year-toggle-btn is-active" id="panelToggle2022Btn" onclick="toggleHide2022()" title="Toggle 2022 exam questions (Click to show/hide 2022 questions)">
                            <span class="toggle-switch-track" aria-hidden="true">
                                <span class="toggle-switch-thumb"></span>
                            </span>
                            <span class="year-toggle-text" id="panelToggle2022Text">
                                <span class="badge badge-year-2022">2022</span> Shown
                            </span>
                        </button>

                        <span class="match-counter-badge" id="matchCounter">{len(raw_questions)} of {len(raw_questions)} matched</span>

                        <div class="progress-pill-badge" id="completionProgressBadge" title="Click to view completed questions">
                            <svg class="icon icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                            <span id="completedCounterText">0 / {len(raw_questions)} Done</span>
                        </div>

                        <button class="clear-completed-btn" id="clearCompletedBtn" title="Unmark all completed questions" style="display: none;">
                            <svg class="icon icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                            Clear Done
                        </button>

                        <button class="reset-filters-btn" id="resetFiltersBtn" title="Reset all filters to default" style="display: none;">
                            <svg class="icon icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="1 4 1 10 7 10"></polyline><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path></svg>
                            Reset
                        </button>
                    </div>
                </div>

                <!-- STRUCTURED FILTER ROWS (ZERO WRAPPING & PERFECT SYMMETRY) -->
                <div class="control-panel-filters">
                    <!-- ROW 1: YEAR, REPEAT, STATUS -->
                    <div class="control-panel-filter-row">
                        <div class="filter-subgroup">
                            <span class="filter-group-label">Year</span>
                            <div id="yearFilters" class="filter-pills-row">
                                <button class="filter-pill-btn active" data-year="all">All</button>
                                <button class="filter-pill-btn" data-year="2025">2025</button>
                                <button class="filter-pill-btn" data-year="2024">2024</button>
                                <button class="filter-pill-btn" data-year="2023">2023</button>
                                <button class="filter-pill-btn" data-year="2022" id="filterPill2022">2022</button>
                            </div>
                        </div>

                        <div class="filter-divider" aria-hidden="true"></div>

                        <div class="filter-subgroup">
                            <span class="filter-group-label">Repeated</span>
                            <div id="repeatFilters" class="filter-pills-row">
                                <button class="filter-pill-btn active" data-repeat="all">All</button>
                                <button class="filter-pill-btn" data-repeat="repeated" title="All Repeated Questions (4x, 3x, 2x)">Most Repeated</button>
                                <button class="filter-pill-btn" data-repeat="4x" title="Questions repeated across all 4 exam papers">4x</button>
                                <button class="filter-pill-btn" data-repeat="3x" title="Questions repeated across 3 exam papers">3x</button>
                                <button class="filter-pill-btn" data-repeat="2x" title="Questions repeated across 2 exam papers">2x</button>
                            </div>
                        </div>

                        <div class="filter-divider" aria-hidden="true"></div>

                        <div class="filter-subgroup">
                            <span class="filter-group-label">Status</span>
                            <div id="statusFilters" class="filter-pills-row">
                                <button class="filter-pill-btn active" data-status="all">All</button>
                                <button class="filter-pill-btn" data-status="incomplete" title="Hide completed questions">Incomplete</button>
                                <button class="filter-pill-btn" data-status="completed" title="Show only completed questions">Completed</button>
                            </div>
                        </div>
                    </div>

                    <!-- ROW 2: UNIT, TYPE, MARKS -->
                    <div class="control-panel-filter-row">
                        <div class="filter-subgroup">
                            <span class="filter-group-label">Unit</span>
                            <div id="unitFilters" class="filter-pills-row">
                                <button class="filter-pill-btn active" data-unit="all">All</button>
                                <button class="filter-pill-btn" data-unit="1">Unit 1</button>
                                <button class="filter-pill-btn" data-unit="2">Unit 2</button>
                                <button class="filter-pill-btn" data-unit="3">Unit 3</button>
                                <button class="filter-pill-btn" data-unit="4">Unit 4</button>
                                <button class="filter-pill-btn" data-unit="5">Unit 5</button>
                            </div>
                        </div>

                        <div class="filter-divider" aria-hidden="true"></div>

                        <div class="filter-subgroup">
                            <span class="filter-group-label">Type</span>
                            <div id="typeFilters" class="filter-pills-row">
                                <button class="filter-pill-btn active" data-type="all">All</button>
                                <button class="filter-pill-btn" data-type="Theory">Theory</button>
                                <button class="filter-pill-btn" data-type="Numerical">Numerical</button>
                                <button class="filter-pill-btn" data-type="Derivation">Derivation</button>
                            </div>
                        </div>

                        <div class="filter-divider" aria-hidden="true"></div>

                        <div class="filter-subgroup">
                            <span class="filter-group-label">Marks</span>
                            <div id="marksFilters" class="filter-pills-row">
                                <button class="filter-pill-btn active" data-marks="all">All</button>
                                <button class="filter-pill-btn" data-marks="2">2M</button>
                                <button class="filter-pill-btn" data-marks="3">3M</button>
                                <button class="filter-pill-btn" data-marks="7">7M / 6M</button>
                            </div>
                        </div>
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
            <div class="page-header-row">
                <span class="card-overline">Mathematical Cheat-Sheet &bull; 14 Governing Relations</span>
                <h1 class="page-title">Master Formulas &amp; Governing Equations</h1>
            </div>

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

    </div>

    <!-- Embedded High-Performance Data Arrays -->
    <script>
        const CANONICAL_TOPICS = {canonical_json_str};
        const RAW_QUESTIONS = {raw_json_str};

        const STORAGE_KEY_FILTERS = 'geotech_filters';
        const STORAGE_KEY_COMPLETED = 'geotech_completed_questions';
        const STORAGE_KEY_VIEW = 'geotech_active_view';
        const STORAGE_KEY_HIDE_2022 = 'geotech_hide_2022';

        let hide2022 = false;
        try {{
            const savedHide = localStorage.getItem(STORAGE_KEY_HIDE_2022);
            if (savedHide !== null) {{
                hide2022 = (savedHide === 'true');
            }}
        }} catch (e) {{
            console.error('Error loading hide2022 setting:', e);
        }}

        function setHide2022(val) {{
            hide2022 = Boolean(val);
            try {{
                localStorage.setItem(STORAGE_KEY_HIDE_2022, String(hide2022));
            }} catch (e) {{}}

            if (hide2022 && currentYear === '2022') {{
                currentYear = 'all';
                saveFilters();
                syncFilterUI();
            }}

            sync2022ToggleUI();
            renderQuestions();
            updateMetrics();
            syncChecklistUI();
        }}

        window.toggleHide2022 = function() {{
            setHide2022(!hide2022);
        }};

        function sync2022ToggleUI() {{
            const panelBtn = document.getElementById('panelToggle2022Btn');
            const panelText = document.getElementById('panelToggle2022Text');
            const filterPill2022 = document.getElementById('filterPill2022');
            const checklistToggleBtn = document.getElementById('checklistToggle2022Btn');
            const checklistPill2022 = document.getElementById('checklistYearPill-2022');
            const yearSection2022 = document.getElementById('year-section-2022');

            const isShown = !hide2022;

            if (panelBtn) {{
                panelBtn.classList.toggle('is-active', isShown);
                panelBtn.classList.toggle('is-hidden', !isShown);
                panelBtn.title = isShown ? '2022 PYQs are included (Click to hide 2022)' : '2022 PYQs are hidden (Click to include 2022)';
            }}
            if (panelText) {{
                panelText.innerHTML = isShown 
                    ? '<span class="badge badge-year-2022">2022</span> Shown'
                    : '<span class="badge badge-subtle">2022</span> Hidden';
            }}

            if (filterPill2022) {{
                filterPill2022.style.display = isShown ? 'inline-flex' : 'none';
            }}

            if (checklistToggleBtn) {{
                checklistToggleBtn.style.display = hide2022 ? 'inline-flex' : 'none';
            }}

            if (checklistPill2022) {{
                checklistPill2022.style.display = isShown ? 'inline-flex' : 'none';
            }}

            if (yearSection2022) {{
                yearSection2022.style.display = isShown ? 'block' : 'none';
            }}
        }}

        let currentYear = 'all';
        let currentUnit = 'all';
        let currentType = 'all';
        let currentMarks = 'all';
        let currentRepeat = 'all';
        let currentStatus = 'all';
        let searchQuery = '';

        let completedQuestions = new Set();
        try {{
            const savedDone = JSON.parse(localStorage.getItem(STORAGE_KEY_COMPLETED) || '[]');
            if (Array.isArray(savedDone)) {{
                completedQuestions = new Set(savedDone);
            }}
        }} catch (e) {{
            console.error('Error loading completed questions:', e);
        }}

        function saveCompleted() {{
            try {{
                localStorage.setItem(STORAGE_KEY_COMPLETED, JSON.stringify([...completedQuestions]));
            }} catch (e) {{
                console.error('Error saving completed questions:', e);
            }}
            updateMetrics();
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
            const visibleQuestions = RAW_QUESTIONS.filter(q => !hide2022 || String(q.year) !== '2022');
            const total = visibleQuestions.length;
            const doneCount = visibleQuestions.filter(q => completedQuestions.has(q.id)).length;
            const pct = total > 0 ? Math.round((doneCount / total) * 100) : 0;

            if (completedText) {{
                completedText.textContent = `${{doneCount}} / ${{total}} Done (${{pct}}%)`;
            }}
            if (clearBtn) {{
                clearBtn.style.display = doneCount > 0 ? 'inline-flex' : 'none';
                clearBtn.innerHTML = `<svg class="icon icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg> Clear Done (${{doneCount}})`;
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

        // UNIT CHECKLIST & SYNCHRONIZATION ENGINE (YEAR-WISE & UNIT-WISE)
        let currentChecklistStatus = 'all';
        let checklistSearchQuery = '';

        function syncChecklistUI() {{
            const visibleQuestions = RAW_QUESTIONS.filter(q => !hide2022 || String(q.year) !== '2022');
            const total = visibleQuestions.length;
            const completedCount = visibleQuestions.filter(q => completedQuestions.has(q.id)).length;
            const totalPct = total > 0 ? Math.round((completedCount / total) * 100) : 0;

            const totalPctEl = document.getElementById('checklistTotalPct');
            const totalCountEl = document.getElementById('checklistTotalCount');
            const totalBarEl = document.getElementById('checklistTotalBar');
            if (totalPctEl) totalPctEl.textContent = `${{totalPct}}%`;
            if (totalCountEl) totalCountEl.textContent = `${{completedCount}} / ${{total}} Completed`;
            if (totalBarEl) totalBarEl.style.width = `${{totalPct}}%`;

            const overlineEl = document.getElementById('checklistOverlineCount');
            if (overlineEl) overlineEl.textContent = `${{total}} PYQs`;

            const navBadge = document.getElementById('navChecklistBadge');
            if (navBadge) {{
                navBadge.textContent = `${{completedCount}}/${{total}} Done`;
            }}

            const navQBadge = document.getElementById('navQuestionsBadge');
            if (navQBadge) {{
                navQBadge.textContent = `${{total}} PYQs`;
            }}

            const allCountEl = document.getElementById('checklistAllCount');
            const incCountEl = document.getElementById('checklistIncompleteCount');
            const compCountEl = document.getElementById('checklistCompletedCount');
            if (allCountEl) allCountEl.textContent = total;
            if (incCountEl) incCountEl.textContent = total - completedCount;
            if (compCountEl) compCountEl.textContent = completedCount;

            const yearTotal = {{ '2025': 0, '2024': 0, '2023': 0, '2022': 0 }};
            const yearDone = {{ '2025': 0, '2024': 0, '2023': 0, '2022': 0 }};
            const subheadTotal = {{}};
            const subheadDone = {{}};

            RAW_QUESTIONS.forEach(item => {{
                const y = String(item.year);
                const u = String(item.unit);
                const yuKey = `${{y}}-${{u}}`;

                if (yearTotal[y] !== undefined) {{
                    yearTotal[y]++;
                    if (completedQuestions.has(item.id)) yearDone[y]++;
                }}
                subheadTotal[yuKey] = (subheadTotal[yuKey] || 0) + 1;
                if (completedQuestions.has(item.id)) {{
                    subheadDone[yuKey] = (subheadDone[yuKey] || 0) + 1;
                }}

                const isDone = completedQuestions.has(item.id);
                const cardEl = document.getElementById('chk-card-' + item.id);
                const btnEl = document.getElementById('chk-btn-' + item.id);

                if (cardEl) {{
                    cardEl.classList.toggle('is-completed', isDone);

                    let visible = true;
                    if (hide2022 && y === '2022') visible = false;
                    if (currentChecklistStatus === 'incomplete' && isDone) visible = false;
                    if (currentChecklistStatus === 'completed' && !isDone) visible = false;

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
            }});

            ['2025', '2024', '2023', '2022'].forEach(y => {{
                const yTot = yearTotal[y] || 0;
                const yDn = yearDone[y] || 0;
                const yPct = yTot > 0 ? Math.round((yDn / yTot) * 100) : 0;

                const pillCount = document.getElementById(`yearPillCount-${{y}}`);
                if (pillCount) pillCount.textContent = `${{yDn}}/${{yTot}}`;

                const statText = document.getElementById(`yearStatText-${{y}}`);
                if (statText) statText.textContent = `${{yDn}} / ${{yTot}} Done (${{yPct}}%)`;

                const miniBar = document.getElementById(`yearMiniBar-${{y}}`);
                if (miniBar) miniBar.style.width = `${{yPct}}%`;

                for (let u = 1; u <= 5; u++) {{
                    const yuKey = `${{y}}-${{u}}`;
                    const subCountEl = document.getElementById(`unitSubheadCount-${{y}}-${{u}}`);
                    if (subCountEl && subheadTotal[yuKey]) {{
                        subCountEl.textContent = `${{subheadDone[yuKey] || 0}}/${{subheadTotal[yuKey]}}`;
                    }}

                    const subGroup = document.getElementById(`unit-subgroup-${{y}}-${{u}}`);
                    if (subGroup) {{
                        if (hide2022 && y === '2022') {{
                            subGroup.style.display = 'none';
                        }} else {{
                            const visibleCards = subGroup.querySelectorAll('.checklist-card:not([style*="display: none"])');
                            subGroup.style.display = (visibleCards.length > 0 || (!checklistSearchQuery && currentChecklistStatus === 'all')) ? 'flex' : 'none';
                        }}
                    }}
                }}

                const yearGroup = document.getElementById(`year-section-${{y}}`);
                if (yearGroup) {{
                    if (hide2022 && y === '2022') {{
                        yearGroup.style.display = 'none';
                    }} else {{
                        const visibleInYear = yearGroup.querySelectorAll('.checklist-card:not([style*="display: none"])');
                        yearGroup.style.display = (visibleInYear.length > 0 || (!checklistSearchQuery && currentChecklistStatus === 'all')) ? 'block' : 'none';
                    }}
                }}
            }});

            const checklistPill2022 = document.getElementById('checklistYearPill-2022');
            if (checklistPill2022) {{
                checklistPill2022.style.display = hide2022 ? 'none' : 'inline-flex';
            }}
            const checklistToggleBtn = document.getElementById('checklistToggle2022Btn');
            if (checklistToggleBtn) {{
                checklistToggleBtn.style.display = hide2022 ? 'inline-flex' : 'none';
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
                group.querySelectorAll('.checklist-status-pill').forEach(btn => {{
                    btn.classList.toggle('active', btn.getAttribute('data-status') === status);
                }});
            }}
            syncChecklistUI();
        }};

        window.toggleChecklistSolution = function(id, event) {{
            if (event && event.target && (
                event.target.closest('.checklist-solution-content') || 
                event.target.closest('.checklist-card-check') || 
                event.target.closest('.checklist-checkbox-btn')
            )) {{
                return; // Do not collapse when selecting text inside answer or clicking checkbox!
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
                if (window.renderAllMath) {{
                    try {{ window.renderAllMath(); }} catch(e) {{}}
                }}
            }}
        }};

        window.jumpToQuestionBank = function(questionId) {{
            const qObj = RAW_QUESTIONS.find(q => q.id === questionId);
            if (!qObj) return;

            if (String(qObj.year) === '2022' && hide2022) {{
                setHide2022(false);
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
            }}

            window.scrollTo({{ top: 0, behavior: 'instant' }});
            const header = document.querySelector('.header');
            if (header) header.classList.remove('header-hidden');
        }};

        // Handle initial hash routing & restored state
        window.addEventListener('DOMContentLoaded', () => {{
            loadSavedFilters();
            syncFilterUI();
            sync2022ToggleUI();

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
            if (checklistSearchInput) {{
                let clTimeout;
                checklistSearchInput.addEventListener('input', (e) => {{
                    clearTimeout(clTimeout);
                    clTimeout = setTimeout(() => {{
                        checklistSearchQuery = e.target.value.trim().toLowerCase();
                        syncChecklistUI();
                    }}, 150);
                }});
            }}
            syncChecklistUI();
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
                themeIcon.innerHTML = `
                    <circle cx="12" cy="12" r="5"></circle>
                    <line x1="12" y1="1" x2="12" y2="3"></line>
                    <line x1="12" y1="21" x2="12" y2="23"></line>
                    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                    <line x1="1" y1="12" x2="3" y2="12"></line>
                    <line x1="21" y1="12" x2="23" y2="12"></line>
                    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                `;
            }} else {{
                themeIcon.innerHTML = `
                    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                `;
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

        // Render Engine for Questions (Click to open, constrained optimal line length)
        function renderQuestions() {{
            const container = document.getElementById('questionsContainer');
            const counterEl = document.getElementById('matchCounter');

            let items = RAW_QUESTIONS;
            if (hide2022) {{
                items = items.filter(q => String(q.year) !== '2022');
            }}
            let totalSource = items.length;

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
                    if (completedQuestions.has(item.id)) {{
                        return false;
                    }}
                }} else if (currentStatus === 'completed') {{
                    if (!completedQuestions.has(item.id)) {{
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
                counterEl.textContent = `${{filtered.length}} of ${{totalSource}} matched`;
            }}

            if (filtered.length === 0) {{
                const isAllDoneIncomplete = currentStatus === 'incomplete' && completedQuestions.size > 0 && completedQuestions.size === totalSource;
                container.innerHTML = `
                    <div class="empty-results">
                        <svg class="icon icon-lg" style="margin-bottom: 0.5rem; color: var(--muted-foreground);" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        <div class="empty-results-title">${{isAllDoneIncomplete ? 'All questions marked as completed!' : 'No matching questions found'}}</div>
                        <p class="text-body-small">${{isAllDoneIncomplete ? 'Great work! Switch status to "All" or "Completed" to review your work.' : 'Try clearing search filters or clicking Reset Filters.'}}</p>
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
                const unitBadgeClass = `badge-unit-${{item.unit}}`;
                const cardBadgeClass = repBadgeInfo.countStr === '4x' ? 'badge-repeat-4x' : (repBadgeInfo.countStr === '3x' ? 'badge-repeat-3x' : (repBadgeInfo.countStr === '2x' ? 'badge-repeat-2x' : 'badge-subtle'));

                htmlParts.push(`
                <div class="q-item ${{isCompleted ? 'is-completed' : ''}}" id="${{item.id}}" onclick="toggleSolution('${{item.id}}', event)">
                    <div class="q-item-header">
                        <div class="q-item-left-meta">
                            <span class="q-item-qno">${{item.q_no}}</span>
                        </div>

                        <div class="q-item-right-meta">
                            <div class="q-item-badges">
                                <span class="badge badge-year-${{item.year}}">${{item.year}}</span>
                                <span class="badge ${{unitBadgeClass}}">Unit ${{item.unit}}</span>
                                <span class="badge badge-subtle">${{item.type}}</span>
                                <span class="badge badge-subtle">${{item.marks}}M</span>
                                ${{repBadgeInfo.isRep && repBadgeInfo.countStr ? `<span class=\"badge ${{cardBadgeClass}}\" title=\"${{repBadgeInfo.freq}}\">${{repBadgeInfo.countStr}}</span>` : ''}}
                                ${{isCompleted ? `<span class="badge badge-completed"><svg class="icon icon-xs" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"></polyline></svg> Done</span>` : ''}}
                            </div>

                            <div class="q-item-actions">
                                <button class="complete-btn ${{isCompleted ? 'is-completed' : ''}}" 
                                        onclick="toggleCompleteQuestion('${{item.id}}', event)" 
                                        title="${{isCompleted ? 'Click to unmark as complete' : 'Click to mark as complete'}}"
                                        aria-label="${{isCompleted ? 'Mark incomplete' : 'Mark complete'}}">
                                    <svg class="icon icon-xs check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                        <polyline points="20 6 9 17 4 12"></polyline>
                                    </svg>
                                    <span>${{isCompleted ? 'Completed' : 'Mark Done'}}</span>
                                </button>
                                <svg class="icon icon-sm chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                    <polyline points="6 9 12 15 18 9"></polyline>
                                </svg>
                            </div>
                        </div>
                    </div>

                    <h3 class="q-item-title">${{item.question}}</h3>

                    <div class="q-solution-content" id="sol-${{item.id}}">
                        <div class="solution-body">
                            ${{item.formatted_solution}}
                        </div>
                    </div>
                </div>
                `);
            }});

            container.innerHTML = htmlParts.join('');
        }}

        // TOGGLE SOLUTION ON ENTIRE CARD CLICK
        window.toggleSolution = function(id, event) {{
            if (event && event.target && (event.target.closest('.q-solution-content') || event.target.closest('.complete-btn'))) {{
                return; // Do not collapse when clicking or selecting text inside answer or clicking complete button!
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

        const resetBtn = document.getElementById('resetFiltersBtn');
        if (resetBtn) {{
            resetBtn.addEventListener('click', () => {{
                currentYear = 'all';
                currentUnit = 'all';
                currentType = 'all';
                currentMarks = 'all';
                currentRepeat = 'all';
                currentStatus = 'all';
                searchQuery = '';
                saveFilters();
                syncFilterUI();
                renderQuestions();
            }});
        }}

        const clearDoneBtn = document.getElementById('clearCompletedBtn');
        if (clearDoneBtn) {{
            clearDoneBtn.addEventListener('click', () => {{
                const visibleDone = RAW_QUESTIONS.filter(q => (!hide2022 || String(q.year) !== '2022') && completedQuestions.has(q.id));
                if (visibleDone.length === 0) return;
                const promptMsg = hide2022
                    ? `Unmark ${{visibleDone.length}} completed questions in 2024 & 2023?`
                    : `Unmark all ${{completedQuestions.size}} completed questions?`;
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
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="19" x2="12" y2="5"></line>
            <polyline points="5 12 12 5 19 12"></polyline>
        </svg>
    </button>

    <!-- MOBILE BOTTOM APP NAVIGATION (iOS/Android Native App Style) -->
    <nav class="mobile-bottom-nav" aria-label="Mobile App Navigation">
        <button class="mobile-nav-item nav-link-btn active" data-view="questions" onclick="switchPageView('questions')" aria-label="Question Bank">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 14 14"></polyline>
            </svg>
            <span class="mobile-nav-label">Questions</span>
        </button>
        <button class="mobile-nav-item nav-link-btn" data-view="syllabus" onclick="switchPageView('syllabus')" aria-label="PYQ Checklist">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <polyline points="9 11 12 14 22 4"></polyline>
                <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>
            </svg>
            <span class="mobile-nav-label">Checklist</span>
        </button>
        <button class="mobile-nav-item nav-link-btn" data-view="formulas" onclick="switchPageView('formulas')" aria-label="Formulas">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <polyline points="4 7 4 4 20 4 20 7"></polyline>
                <line x1="9" y1="20" x2="15" y2="20"></line>
                <line x1="12" y1="4" x2="12" y2="20"></line>
            </svg>
            <span class="mobile-nav-label">Formulas</span>
        </button>
        <a href="timetable.html" class="mobile-nav-item nav-link-timetable" aria-label="Exam Timetable">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
            </svg>
            <span class="mobile-nav-label">Timetable</span>
        </a>
    </nav>
</body>
</html>"""

import formula_showcase
html_template = formula_showcase.enhance_html(html_template)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open("geotech_pyq_analysis.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Updated index.html & geotech_pyq_analysis.html: KaTeX mathematical formulas & formula showcase integrated successfully!")
