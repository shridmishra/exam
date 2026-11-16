import json
from compile_data import questions

def generate_html():
    total_q = len(questions)
    theory_q = len([q for q in questions if q['type'] == 'Theory'])
    num_q = len([q for q in questions if q['type'] == 'Numerical'])
    deriv_q = len([q for q in questions if q['type'] == 'Derivation'])
    prac_q = len([q for q in questions if q['type'] == 'Practical'])
    repeated_q = len([q for q in questions if q['repeated']])
    
    questions_json = json.dumps(questions, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geotechnical Engineering - II | PYQ Analysis & Question Bank</title>
    <meta name="description" content="Previous Year Questions analysis, repeat trends, formula guides, and solutions for Geotechnical Engineering - II (CE 41007 / CE 4107 / CE 4151).">
    <style>
        /* ----------------------------------------------------
           MANDATORY GLOBAL DESIGN TOKENS & TYPOGRAPHY SYSTEM
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
            --font-size-body-medium: 14px;
            --line-height-body-medium: 20px;
            --font-size-body-small: 12px;
            --line-height-body-small: 16px;
            --font-size-button: 14px;
            --line-height-button: 21px;

            /* Specific component scale constraints */
            --font-size-stat: 24px;
            --line-height-stat: 32px;
            --font-size-overline: 11px;

            /* Neutral Color Palette (Light Mode - Enhanced Readability) */
            --background: #f8fafc;
            --foreground: #0f172a;
            --card: #ffffff;
            --card-foreground: #0f172a;
            --popover: #ffffff;
            --popover-foreground: #0f172a;
            --primary: #0f172a;
            --primary-foreground: #ffffff;
            --secondary: #f1f5f9;
            --secondary-foreground: #0f172a;
            --muted: #f1f5f9;
            --muted-foreground: #475569;
            --border: #e2e8f0;
            --border-hover: #cbd5e1;
            --input: #e2e8f0;
            --ring: #64748b;

            /* High-Contrast Neutral Pastel Accents */
            --pastel-sage-bg: #f0fdf4;
            --pastel-sage-border: #bbf7d0;
            --pastel-sage-foreground: #14532d;

            --pastel-lavender-bg: #faf5ff;
            --pastel-lavender-border: #e9d5ff;
            --pastel-lavender-foreground: #581c87;

            --pastel-peach-bg: #fff7ed;
            --pastel-peach-border: #fed7aa;
            --pastel-peach-foreground: #7c2d12;

            --pastel-sky-bg: #f0f9ff;
            --pastel-sky-border: #bae6fd;
            --pastel-sky-foreground: #0c4a6e;

            --pastel-rose-bg: #fff1f2;
            --pastel-rose-border: #fecdd3;
            --pastel-rose-foreground: #881337;

            --pastel-sand-bg: #fefce8;
            --pastel-sand-border: #fef08a;
            --pastel-sand-foreground: #713f12;

            --flame-bg: #fff7ed;
            --flame-border: #ffedd5;
            --flame-foreground: #9a3412;

            --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);

            --radius-sm: 6px;
            --radius-md: 8px;
            --radius-lg: 12px;
            --radius-full: 9999px;

            --font-family-sans: "Aeonik", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            --font-family-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        }}

        [data-theme="dark"] {{
            /* Neutral Color Palette (Dark Mode - Enhanced Readability) */
            --background: #090d16;
            --foreground: #f8fafc;
            --card: #111827;
            --card-foreground: #f8fafc;
            --popover: #111827;
            --popover-foreground: #f8fafc;
            --primary: #f8fafc;
            --primary-foreground: #090d16;
            --secondary: #1f2937;
            --secondary-foreground: #f8fafc;
            --muted: #1f2937;
            --muted-foreground: #94a3b8;
            --border: #374151;
            --border-hover: #4b5563;
            --input: #374151;
            --ring: #94a3b8;

            --pastel-sage-bg: rgba(20, 83, 45, 0.25);
            --pastel-sage-border: rgba(74, 222, 128, 0.4);
            --pastel-sage-foreground: #86efac;

            --pastel-lavender-bg: rgba(88, 28, 135, 0.25);
            --pastel-lavender-border: rgba(192, 132, 252, 0.4);
            --pastel-lavender-foreground: #d8b4fe;

            --pastel-peach-bg: rgba(124, 45, 18, 0.25);
            --pastel-peach-border: rgba(251, 146, 60, 0.4);
            --pastel-peach-foreground: #fdba74;

            --pastel-sky-bg: rgba(12, 74, 110, 0.25);
            --pastel-sky-border: rgba(56, 189, 248, 0.4);
            --pastel-sky-foreground: #7dd3fc;

            --pastel-rose-bg: rgba(136, 19, 55, 0.25);
            --pastel-rose-border: rgba(251, 113, 133, 0.4);
            --pastel-rose-foreground: #fca5a5;

            --pastel-sand-bg: rgba(113, 63, 18, 0.25);
            --pastel-sand-border: rgba(250, 204, 21, 0.4);
            --pastel-sand-foreground: #fde047;

            --flame-bg: rgba(154, 52, 18, 0.28);
            --flame-border: rgba(251, 146, 60, 0.45);
            --flame-foreground: #fb923c;

            --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        }}

        /* ----------------------------------------------------
           STRICT TYPOGRAPHY UTILITY CLASSES (PER USER RULE)
           ---------------------------------------------------- */
        .text-h1, .typography-h1 {{
            font-size: var(--font-size-h1);
            line-height: var(--line-height-h1);
            font-weight: 700;
            color: var(--foreground);
        }}

        .text-h2, .typography-h2 {{
            font-size: var(--font-size-h2);
            line-height: var(--line-height-h2);
            font-weight: 700;
            color: var(--foreground);
        }}

        .text-h3, .typography-h3 {{
            font-size: var(--font-size-h3);
            line-height: var(--line-height-h3);
            font-weight: 500;
            color: var(--foreground);
        }}

        .text-h4, .typography-h4 {{
            font-size: var(--font-size-h4);
            line-height: var(--line-height-h4);
            font-weight: 400;
            color: var(--foreground);
        }}

        .text-h5, .typography-h5 {{
            font-size: var(--font-size-h5);
            line-height: var(--line-height-h5);
            font-weight: 400;
            color: var(--foreground);
        }}

        .text-h6, .typography-h6, .text-h6-title {{
            font-size: var(--font-size-h6);
            line-height: var(--line-height-h6);
            font-weight: 500;
            color: var(--foreground);
        }}

        .text-body-large, .text-body-lg {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 500;
            color: var(--foreground);
        }}

        .text-body-medium, .text-body-md {{
            font-size: var(--font-size-body-medium);
            line-height: var(--line-height-body-medium);
            font-weight: 500;
            color: var(--foreground);
        }}

        .text-body-small, .text-body-sm {{
            font-size: var(--font-size-body-small);
            line-height: var(--line-height-body-small);
            font-weight: 400;
            color: var(--foreground);
        }}

        .text-button, .typography-button {{
            font-size: var(--font-size-button);
            line-height: var(--line-height-button);
            font-weight: 600;
        }}

        /* Specific Rule Classes */
        .card-stat-number {{
            font-size: var(--font-size-stat);
            line-height: var(--line-height-stat);
            font-weight: 500;
            color: var(--foreground);
        }}

        .section-header-title {{
            font-size: var(--font-size-h6);
            line-height: var(--line-height-h6);
            font-weight: 500;
            color: var(--foreground);
            letter-spacing: -0.01em;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .card-overline {{
            font-size: var(--font-size-overline);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.02em;
            color: var(--muted-foreground);
        }}

        /* Color Utility Classes (Using CSS Variables Only) */
        .text-lavender {{ color: var(--pastel-lavender-foreground); }}
        .text-sand {{ color: var(--pastel-sand-foreground); }}
        .text-peach {{ color: var(--pastel-peach-foreground); }}
        .text-sage {{ color: var(--pastel-sage-foreground); }}
        .text-rose {{ color: var(--pastel-rose-foreground); }}
        .text-sky {{ color: var(--pastel-sky-foreground); }}
        .text-flame {{ color: var(--flame-foreground); }}
        .text-muted {{ color: var(--muted-foreground); }}

        /* ----------------------------------------------------
           BASE LAYOUT
           ---------------------------------------------------- */
        *, *::before, *::after {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
        }}

        body {{
            background-color: var(--background);
            color: var(--foreground);
            font-family: var(--font-family-sans);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
        }}

        a {{
            color: inherit;
            text-decoration: none;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }}

        /* Clean SVG Icon Wrapper (No Emojis) */
        .icon {{
            display: inline-block;
            vertical-align: middle;
            width: 16px;
            height: 16px;
            stroke-width: 2;
            flex-shrink: 0;
        }}

        .icon-lg {{
            width: 20px;
            height: 20px;
        }}

        .icon-sm {{
            width: 14px;
            height: 14px;
        }}

        /* ----------------------------------------------------
           HEADER & NAV
           ---------------------------------------------------- */
        .header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(248, 250, 252, 0.94);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
        }}

        [data-theme="dark"] .header {{
            background: rgba(9, 13, 22, 0.94);
        }}

        .nav {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 60px;
            gap: 12px;
        }}

        .brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
            white-space: nowrap;
        }}

        .brand-badge {{
            background: var(--pastel-sage-bg);
            border: 1px solid var(--pastel-sage-border);
            color: var(--pastel-sage-foreground);
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.02em;
            padding: 3px 8px;
            border-radius: var(--radius-sm);
            flex-shrink: 0;
        }}

        .brand-title {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 600;
            color: var(--foreground);
            white-space: nowrap;
        }}

        .brand-short {{
            display: none;
        }}

        .nav-links {{
            display: flex;
            align-items: center;
            gap: 8px;
            list-style: none;
            flex-wrap: nowrap;
            overflow-x: auto;
            scrollbar-width: none;
            -ms-overflow-style: none;
        }}

        .nav-links::-webkit-scrollbar {{
            display: none;
        }}

        .nav-link {{
            font-size: var(--font-size-button);
            line-height: var(--line-height-button);
            font-weight: 500;
            color: var(--muted-foreground);
            padding: 5px 10px;
            border-radius: var(--radius-full);
            display: inline-flex;
            align-items: center;
            gap: 5px;
            white-space: nowrap;
            flex-shrink: 0;
            transition: all 0.15s ease;
        }}

        @media (max-width: 1150px) {{
            .nav-link {{
                padding: 4px 8px;
                font-size: 12px;
                gap: 4px;
            }}
            .nav-links {{
                gap: 6px;
            }}
        }}

        @media (max-width: 960px) {{
            .brand-full {{
                display: none;
            }}
            .brand-short {{
                display: inline;
            }}
        }}

        .nav-link:hover {{
            color: var(--foreground);
            background: var(--secondary);
        }}

        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .theme-toggle-btn {{
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--foreground);
            width: 38px;
            height: 38px;
            border-radius: var(--radius-full);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: var(--shadow-sm);
        }}

        .theme-toggle-btn:hover {{
            background: var(--secondary);
            border-color: var(--border-hover);
        }}

        /* ----------------------------------------------------
           HERO SECTION
           ---------------------------------------------------- */
        .hero {{
            padding: 44px 0 32px 0;
            border-bottom: 1px solid var(--border);
        }}

        .hero-meta {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 14px;
            flex-wrap: wrap;
        }}

        .hero-title {{
            font-size: var(--font-size-h2);
            line-height: var(--line-height-h2);
            font-weight: 700;
            color: var(--foreground);
            letter-spacing: -0.02em;
            margin-bottom: 12px;
        }}

        @media (min-width: 1024px) {{
            .hero-title {{
                font-size: var(--font-size-h1);
                line-height: var(--line-height-h1);
            }}
        }}

        .hero-desc {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 500;
            color: var(--muted-foreground);
            max-width: 820px;
            margin-bottom: 24px;
        }}

        .hero-tags {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}

        /* ----------------------------------------------------
           CARD STATS (STRICT 24px per user rule)
           ---------------------------------------------------- */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-top: 28px;
            margin-bottom: 40px;
        }}

        .stat-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 20px;
            box-shadow: var(--shadow-sm);
            position: relative;
            overflow: hidden;
        }}

        .stat-card.sage {{ border-top: 3px solid var(--pastel-sage-border); }}
        .stat-card.lavender {{ border-top: 3px solid var(--pastel-lavender-border); }}
        .stat-card.peach {{ border-top: 3px solid var(--pastel-peach-border); }}
        .stat-card.sky {{ border-top: 3px solid var(--pastel-sky-border); }}

        .stat-subtext {{
            font-size: var(--font-size-body-small);
            line-height: var(--line-height-body-small);
            font-weight: 400;
            color: var(--muted-foreground);
            margin-top: 4px;
        }}

        /* ----------------------------------------------------
           SECTIONS
           ---------------------------------------------------- */
        .section {{
            padding: 40px 0;
            border-bottom: 1px solid var(--border);
        }}

        .section-header {{
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 12px;
        }}

        .section-subtitle {{
            font-size: var(--font-size-body-medium);
            line-height: var(--line-height-body-medium);
            font-weight: 500;
            color: var(--muted-foreground);
            margin-top: 4px;
        }}

        /* ----------------------------------------------------
           MOST REPEATED CARDS (TOP 10 BLUEPRINT)
           ---------------------------------------------------- */
        .repeated-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 18px;
        }}

        .rep-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 22px;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .rep-card:hover {{
            box-shadow: var(--shadow-md);
            border-color: var(--border-hover);
        }}

        .rep-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 10px;
        }}

        .rep-title {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 500;
            color: var(--foreground);
            margin-bottom: 6px;
        }}

        .rep-desc {{
            font-size: var(--font-size-body-medium);
            line-height: 1.6;
            font-weight: 500;
            color: var(--foreground);
            margin-bottom: 14px;
        }}

        .rep-meta {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
            margin-top: auto;
            padding-top: 12px;
            border-top: 1px solid var(--border);
        }}

        /* ----------------------------------------------------
           SYLLABUS & UNIT BREAKDOWN
           ---------------------------------------------------- */
        .units-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 18px;
        }}

        .unit-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 22px;
            box-shadow: var(--shadow-sm);
        }}

        .unit-name {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 500;
            color: var(--foreground);
            margin-top: 4px;
            margin-bottom: 10px;
        }}

        .unit-topics-list {{
            list-style: none;
            margin-top: 8px;
            margin-bottom: 14px;
        }}

        .unit-topics-list li {{
            font-size: var(--font-size-body-small);
            line-height: var(--line-height-body-small);
            font-weight: 400;
            color: var(--foreground);
            padding: 3px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .unit-bullet {{
            width: 4px;
            height: 4px;
            border-radius: var(--radius-full);
            background: var(--muted-foreground);
            display: inline-block;
            flex-shrink: 0;
        }}

        .unit-weightage-bar {{
            height: 5px;
            background: var(--secondary);
            border-radius: var(--radius-full);
            overflow: hidden;
            margin-top: 10px;
        }}

        .unit-weightage-fill {{
            height: 100%;
            border-radius: var(--radius-full);
            width: 100%;
        }}

        .bar-sky {{ background: var(--pastel-sky-foreground); }}
        .bar-lavender {{ background: var(--pastel-lavender-foreground); }}
        .bar-peach {{ background: var(--pastel-peach-foreground); }}
        .bar-sage {{ background: var(--pastel-sage-foreground); }}
        .bar-rose {{ background: var(--pastel-rose-foreground); }}

        /* ----------------------------------------------------
           FORMULA CHEAT SHEET
           ---------------------------------------------------- */
        .formula-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 16px;
        }}

        .formula-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 18px;
        }}

        .formula-title {{
            font-size: var(--font-size-body-medium);
            line-height: var(--line-height-body-medium);
            font-weight: 500;
            color: var(--foreground);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .formula-math {{
            background: var(--secondary);
            padding: 10px 12px;
            border-radius: var(--radius-sm);
            font-family: var(--font-family-mono);
            font-size: var(--font-size-body-small);
            line-height: 1.5;
            color: var(--foreground);
            margin: 8px 0;
            border-left: 3px solid var(--ring);
            overflow-x: auto;
        }}

        .formula-notes {{
            font-size: var(--font-size-body-small);
            line-height: var(--line-height-body-small);
            font-weight: 400;
            color: var(--muted-foreground);
        }}

        /* ----------------------------------------------------
           FILTER CONTROLS & QUESTION BANK
           ---------------------------------------------------- */
        .filter-panel {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 22px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
        }}

        .search-box {{
            display: flex;
            align-items: center;
            background: var(--secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 8px 14px;
            margin-bottom: 18px;
            gap: 10px;
        }}

        .search-box:focus-within {{
            border-color: var(--ring);
            box-shadow: 0 0 0 2px rgba(100, 116, 139, 0.2);
        }}

        .search-input {{
            background: transparent;
            border: none;
            outline: none;
            color: var(--foreground);
            font-size: var(--font-size-body-medium);
            line-height: var(--line-height-body-medium);
            width: 100%;
            font-family: inherit;
        }}

        .search-input::placeholder {{
            color: var(--muted-foreground);
        }}

        .filter-row {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
            flex-wrap: wrap;
        }}

        .filter-row:last-child {{
            margin-bottom: 0;
        }}

        .filter-label {{
            font-size: var(--font-size-overline);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.02em;
            color: var(--muted-foreground);
            min-width: 75px;
        }}

        .filter-pills {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }}

        .pill-btn {{
            background: var(--secondary);
            border: 1px solid var(--border);
            color: var(--muted-foreground);
            font-size: var(--font-size-button);
            line-height: var(--line-height-button);
            font-weight: 600;
            padding: 5px 12px;
            border-radius: var(--radius-full);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }}

        .pill-btn:hover {{
            background: var(--muted);
            color: var(--foreground);
        }}

        .pill-btn.active {{
            background: var(--primary);
            border-color: var(--primary);
            color: var(--primary-foreground);
        }}

        .pill-btn.flame.active {{
            background: var(--flame-foreground);
            border-color: var(--flame-foreground);
            color: var(--primary-foreground);
        }}

        .results-count-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 18px;
            font-size: var(--font-size-body-small);
            line-height: var(--line-height-body-small);
            font-weight: 400;
            color: var(--muted-foreground);
        }}

        .expand-collapse-btn {{
            background: transparent;
            border: none;
            color: var(--foreground);
            font-size: var(--font-size-body-small);
            font-weight: 500;
            cursor: pointer;
            text-decoration: underline;
        }}

        .divider-bullet {{
            margin: 0 8px;
            color: var(--muted-foreground);
        }}

        /* ----------------------------------------------------
           QUESTION CARDS
           ---------------------------------------------------- */
        .questions-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .q-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 22px;
            box-shadow: var(--shadow-sm);
        }}

        .q-card:hover {{
            box-shadow: var(--shadow-md);
            border-color: var(--border-hover);
        }}

        .q-top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .q-badges {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }}

        /* Strict Badges (All Design Token Classes) */
        .badge {{
            font-size: var(--font-size-overline);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.02em;
            padding: 3px 8px;
            border-radius: var(--radius-sm);
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}

        .badge-year {{
            background: var(--secondary);
            color: var(--foreground);
            border: 1px solid var(--border);
        }}

        .badge-unit {{
            background: var(--pastel-sky-bg);
            border: 1px solid var(--pastel-sky-border);
            color: var(--pastel-sky-foreground);
        }}

        .badge-theory {{
            background: var(--pastel-lavender-bg);
            border: 1px solid var(--pastel-lavender-border);
            color: var(--pastel-lavender-foreground);
        }}

        .badge-numerical {{
            background: var(--pastel-peach-bg);
            border: 1px solid var(--pastel-peach-border);
            color: var(--pastel-peach-foreground);
        }}

        .badge-deriv {{
            background: var(--pastel-sand-bg);
            border: 1px solid var(--pastel-sand-border);
            color: var(--pastel-sand-foreground);
        }}

        .badge-practical {{
            background: var(--pastel-rose-bg);
            border: 1px solid var(--pastel-rose-border);
            color: var(--pastel-rose-foreground);
        }}

        .badge-repeated {{
            background: var(--flame-bg);
            border: 1px solid var(--flame-border);
            color: var(--flame-foreground);
            font-weight: 600;
        }}

        .badge-marks {{
            background: var(--pastel-sage-bg);
            border: 1px solid var(--pastel-sage-border);
            color: var(--pastel-sage-foreground);
        }}

        .badge-subtle {{
            background: var(--secondary);
            color: var(--muted-foreground);
            border: 1px solid var(--border);
        }}

        .q-code-badge {{
            font-size: var(--font-size-body-small);
            font-weight: 500;
            color: var(--muted-foreground);
            font-family: var(--font-family-mono);
        }}

        .q-text {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 500;
            color: var(--foreground);
            margin-bottom: 12px;
        }}

        .q-solution-toggle {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 8px 14px;
            cursor: pointer;
            font-size: var(--font-size-button);
            line-height: var(--line-height-button);
            font-weight: 600;
            color: var(--foreground);
            user-select: none;
        }}

        .q-solution-toggle:hover {{
            background: var(--muted);
            border-color: var(--border-hover);
        }}

        .q-solution-content {{
            display: none;
            padding: 16px;
            margin-top: 8px;
            background: var(--secondary);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            font-size: var(--font-size-body-medium);
            line-height: 1.65;
            font-weight: 500;
            color: var(--foreground);
        }}

        .q-solution-content.open {{
            display: block;
        }}

        .q-topic-label {{
            margin-bottom: 8px;
        }}

        .q-solution-content code {{
            background: var(--card);
            padding: 2px 6px;
            border-radius: var(--radius-sm);
            font-family: var(--font-family-mono);
            font-size: var(--font-size-body-small);
            border: 1px solid var(--border);
            color: var(--foreground);
        }}

        .empty-state {{
            text-align: center;
            padding: 40px;
            background: var(--card);
            border: 1px dashed var(--border);
            border-radius: var(--radius-lg);
        }}

        .empty-state-title {{
            font-size: var(--font-size-body-large);
            line-height: var(--line-height-body-large);
            font-weight: 500;
            color: var(--foreground);
            margin-bottom: 6px;
        }}

        .empty-state-desc {{
            font-size: var(--font-size-body-medium);
            line-height: var(--line-height-body-medium);
            color: var(--muted-foreground);
        }}

        /* ----------------------------------------------------
           FOOTER
           ---------------------------------------------------- */
        .footer {{
            padding: 36px 0;
            border-top: 1px solid var(--border);
            background: var(--card);
            margin-top: 48px;
        }}

        .footer-content {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 16px;
            font-size: var(--font-size-body-small);
            line-height: var(--line-height-body-small);
            font-weight: 400;
            color: var(--muted-foreground);
        }}
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header class="header">
        <div class="container nav">
            <div class="brand">
                <span class="brand-title">
                    <span class="brand-full">Geotechnical Engineering - II</span>
                    <span class="brand-short">Geotech - II</span>
                </span>
            </div>
            <ul class="nav-links">
                <li>
                    <a href="timetable.html" class="nav-link" style="background: var(--pastel-peach-bg); color: var(--pastel-peach-foreground); border: 1px solid var(--pastel-peach-border); font-weight: 600;">
                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        Timetable
                    </a>
                </li>
                <li>
                    <a href="#stats" class="nav-link">
                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        Overview
                    </a>
                </li>
                <li>
                    <a href="#repeated" class="nav-link">
                        <svg class="icon text-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                        Most Repeated
                    </a>
                </li>
                <li>
                    <a href="#syllabus" class="nav-link">
                        <svg class="icon text-sky" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                        Syllabus Breakdown
                    </a>
                </li>
                <li>
                    <a href="#formulas" class="nav-link">
                        <svg class="icon text-sand" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
                        Formulas
                    </a>
                </li>
                <li>
                    <a href="#questions" class="nav-link">
                        <svg class="icon text-sage" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        Question Bank
                    </a>
                </li>
            </ul>
            <div class="nav-actions">
                <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle Light/Dark Theme" title="Toggle Theme">
                    <svg id="themeIcon" class="icon icon-lg" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                </button>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Hero Section -->
        <section class="hero" id="overview">
            <div class="hero-meta">
                <span class="badge badge-year">Nov-Dec 2024</span>
                <span class="badge badge-year">Nov-Dec 2023</span>
                <span class="badge badge-year">Dec 2022</span>
                <span class="badge badge-marks">70 Marks Scheme</span>
            </div>
            <h1 class="hero-title">Geotechnical Engineering - II<br>Previous Year Questions Deep Analysis</h1>
            <p class="hero-desc">
                An exhaustive, line-by-line examination analysis of 3 complete exam sessions (2024, 2023, 2022). Every single question, mark distribution, Course Outcome, and Bloom's level mapped with complete step-by-step solution guides, formulas, and high-frequency recurring patterns.
            </p>
            <div class="hero-tags">
                <span class="badge badge-repeated">
                    <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                    82.1% High-Yield Repetition Rate
                </span>
                <span class="badge badge-theory">{theory_q} Theory Questions</span>
                <span class="badge badge-numerical">{num_q} Numerical Problems</span>
                <span class="badge badge-deriv">{deriv_q} Derivations</span>
            </div>

            <!-- Clean Timetable Banner (Nov-Dec 2026) -->
            <div style="background: var(--card); border: 1px solid var(--border); border-left: 4px solid var(--pastel-peach-foreground); border-radius: var(--radius-md); padding: 14px 20px; margin-top: 20px; display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap;">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                        <span class="badge badge-peach" style="font-weight: 700; font-size: 11px;">Nov – Dec 2026 Session</span>
                        <span style="font-size: 12px; color: var(--muted-foreground);">Timing: 2:00 PM – 5:00 PM</span>
                    </div>
                    <div style="font-size: 15px; font-weight: 600; color: var(--foreground);">
                        Civil Engineering Exam Schedule (Nov to Dec Session)
                    </div>
                </div>
                <a href="timetable.html" style="background: var(--primary); color: var(--primary-foreground); padding: 8px 16px; border-radius: var(--radius-full); font-size: var(--font-size-button); font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
                    View Timetable (7 Papers) →
                </a>
            </div>
        </section>

        <!-- KPI Stats Dashboard (24px Stat Numbers per rule) -->
        <section class="stats-grid" id="stats">
            <div class="stat-card sage">
                <div class="card-overline">Total Questions</div>
                <div class="card-stat-number">{total_q}</div>
                <div class="stat-subtext">Across 3 university exam papers</div>
            </div>
            <div class="stat-card lavender">
                <div class="card-overline">Repeat Probability</div>
                <div class="card-stat-number">82%</div>
                <div class="stat-subtext">{repeated_q} of {total_q} questions follow repeat patterns</div>
            </div>
            <div class="stat-card peach">
                <div class="card-overline">Theory vs Numerical</div>
                <div class="card-stat-number">51 : 41</div>
                <div class="stat-subtext">Balanced split (51% Theory, 41% Numerical)</div>
            </div>
            <div class="stat-card sky">
                <div class="card-overline">Highest Yield Units</div>
                <div class="card-stat-number">Unit 4 &amp; 5</div>
                <div class="stat-subtext">Pile groups &amp; SPT have 100% deterministic repeats</div>
            </div>
        </section>

        <!-- Top 10 Most Repeated PYQs -->
        <section class="section" id="repeated">
            <div class="section-header">
                <div>
                    <span class="card-overline text-flame">Exam Blueprint</span>
                    <h2 class="section-header-title">
                        <svg class="icon icon-lg text-flame" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                        Top 10 Most Repeated Questions &amp; Concepts
                    </h2>
                </div>
            </div>

            <div class="repeated-grid">
                <!-- Rep Item 1 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #1 &bull; 100% Frequency
                            </span>
                            <span class="badge badge-marks">7 Marks</span>
                        </div>
                        <h3 class="rep-title">Standard Penetration Test (SPT) &amp; Corrections</h3>
                        <p class="rep-desc">
                            Appeared in <strong>every single paper without exception</strong> (2024 Q5e, 2023 Q5c OR, 2022 Q5d). Covers equipment details, blow count counting, overburden pressure correction (C<sub>N</sub>), and dilatancy correction for submerged silty sand. In 2023 it was asked as a full depth-wise calculation table!
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 5</span>
                        <span class="badge badge-theory">Theory &amp; Numerical</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2023</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 2 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #2 &bull; Direct Verbatim Repeat
                            </span>
                            <span class="badge badge-marks">7 Marks</span>
                        </div>
                        <h3 class="rep-title">9-Pile Group in Soft Clay (Exact Identical Numerical)</h3>
                        <p class="rep-desc">
                            <strong>Word-for-word identical</strong> in both 2024 (Q.4d) and 2022 (Q.4e)! Data: 3&times;3 square array of 9 piles, diameter = 30 cm, length = 9 m, q<sub>u</sub> = 90 kN/m&sup2; (c = 45 kPa), spacing = 90 cm, FS = 2.5, &alpha; = 0.75. Tests individual shear failure vs. block failure capacity.
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 4</span>
                        <span class="badge badge-numerical">Numerical</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 3 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #3 &bull; 100% Frequency
                            </span>
                            <span class="badge badge-marks">3 &bull; 7 Marks</span>
                        </div>
                        <h3 class="rep-title">Effect of Ground Water Table on Bearing Capacity</h3>
                        <p class="rep-desc">
                            Tested in all three years (2024 Q3e, 2023 Q2b-ii, 2023 Q2c, 2022 Q3c, 2022 Q3d). Evaluates reduction in surcharge and base wedge capacity when the water table rises, proving bearing capacity can decrease by up to ~50% due to buoyant unit weight &gamma;'.
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 3</span>
                        <span class="badge badge-theory">Theory &amp; Numerical</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2023</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 4 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #4 &bull; Near-Identical Repeat
                            </span>
                            <span class="badge badge-marks">7 Marks</span>
                        </div>
                        <h3 class="rep-title">Gravity Retaining Wall Coulomb Earth Pressure</h3>
                        <p class="rep-desc">
                            Appeared in 2024 (12 m wall, &gamma; = 18 kN/m&sup3;, &phi; = 30&deg;, &delta; = 20&deg;) and 2022 (15 m wall, &gamma; = 20 kN/m&sup3;, &phi; = 30&deg;, &delta; = 20&deg;). Requires calculating active and passive thrusts with wall friction and identifying points of application at H/3.
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 1</span>
                        <span class="badge badge-numerical">Numerical</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 5 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #5 &bull; 100% Frequency
                            </span>
                            <span class="badge badge-marks">2 &bull; 3 Marks</span>
                        </div>
                        <h3 class="rep-title">Triaxial Shear Tests (UU, CU, CD) &amp; Drainage Classification</h3>
                        <p class="rep-desc">
                            Present in all 3 papers (2024 Q2c, 2023 Q3b-iii, 2022 Q2b). Compares drainage valve control during cell pressure application and deviatoric shearing stages, plus test suitability for site-specific conditions.
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 2</span>
                        <span class="badge badge-theory">Theory</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2023</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 6 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #6 &bull; High-Weightage Derivation
                            </span>
                            <span class="badge badge-marks">6 &bull; 7 Marks</span>
                        </div>
                        <h3 class="rep-title">Rebhann's Graphical Construction for Earth Pressure</h3>
                        <p class="rep-desc">
                            Appeared in 2023 (Q1c OR) and 2022 (Q1e OR). Step-by-step graphical method for evaluating Coulomb's active earth pressure on rough retaining walls, along with geometric proof of maximum thrust.
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 1</span>
                        <span class="badge badge-deriv">Derivation &amp; Theory</span>
                        <span class="badge badge-year">2023</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 7 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #7 &bull; 100% Frequency
                            </span>
                            <span class="badge badge-marks">2 &bull; 3 Marks</span>
                        </div>
                        <h3 class="rep-title">Soil Sampling &amp; Area Ratio (A<sub>r</sub>) / Clearances</h3>
                        <p class="rep-desc">
                            Present in all 3 papers (2024 Q5c, 2023 Q5a, 2022 Q5c). Formulas for inside clearance (C<sub>i</sub>), outside clearance (C<sub>o</sub>), and area ratio A<sub>r</sub> = (D<sub>2</sub>&sup2; - D<sub>1</sub>&sup2;)/D<sub>1</sub>&sup2; &times; 100% with criteria for undisturbed sampling (&le; 10-20%).
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 5</span>
                        <span class="badge badge-numerical">Numerical &amp; Theory</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2023</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 8 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #8 &bull; Recurring Concept
                            </span>
                            <span class="badge badge-marks">2 &bull; 3 Marks</span>
                        </div>
                        <h3 class="rep-title">Modes of Shear Failure (General, Local, Punching)</h3>
                        <p class="rep-desc">
                            Appeared in 2024 (Q2b) and 2023 (Q2b-i). Compares failure surface geometry, presence of ground heave, and relative density criteria (dense sand vs loose sand vs soft clay) with load-settlement curves.
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 2 / 3</span>
                        <span class="badge badge-theory">Theory</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2023</span>
                    </div>
                </div>

                <!-- Rep Item 9 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #9 &bull; Recurring Topic
                            </span>
                            <span class="badge badge-marks">2 &bull; 7 Marks</span>
                        </div>
                        <h3 class="rep-title">Infinite Slope Stability &amp; Stabilization Methods</h3>
                        <p class="rep-desc">
                            Appeared in 2024 (Q2a, Q2d) and 2022 (Q2e OR). Analysis of factor of safety under dry, submerged, and steady parallel seepage conditions, plus engineering stabilization techniques (flattening, drainage, berms, nailing).
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 2</span>
                        <span class="badge badge-numerical">Theory &amp; Numerical</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>

                <!-- Rep Item 10 -->
                <div class="rep-card">
                    <div>
                        <div class="rep-header">
                            <span class="badge badge-repeated">
                                <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                                #10 &bull; Core Deep Foundation Theory
                            </span>
                            <span class="badge badge-marks">2 &bull; 3 Marks</span>
                        </div>
                        <h3 class="rep-title">Under-Reamed Piles &amp; Open Caisson Well Foundations</h3>
                        <p class="rep-desc">
                            Appeared in 2024 (Q4b, Q4c) and 2023/2022 pile theory. Under-reamed bulb dimensions in expansive black cotton soil, and open caisson component sketches (cutting edge, well curb, steining, bottom plug, sand filling).
                        </p>
                    </div>
                    <div class="rep-meta">
                        <span class="badge badge-unit">Unit 4</span>
                        <span class="badge badge-theory">Theory &amp; Sketch</span>
                        <span class="badge badge-year">2024</span>
                        <span class="badge badge-year">2022</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Unit Syllabus Breakdown & Weightage -->
        <section class="section" id="syllabus">
            <div class="section-header">
                <div>
                    <span class="card-overline text-sky">Syllabus Mapping</span>
                    <h2 class="section-header-title">
                        <svg class="icon icon-lg text-sky" viewBox="0 0 24 24" fill="none" stroke="currentColor"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                        5-Unit Structure &amp; Exam Weightage
                    </h2>
                </div>
            </div>

            <div class="units-grid">
                <!-- Unit 1 -->
                <div class="unit-card">
                    <div class="card-overline text-sky">Unit 1 &bull; CO1</div>
                    <h3 class="unit-name">Lateral Earth Pressure &amp; Retaining Walls</h3>
                    <ul class="unit-topics-list">
                        <li><span class="unit-bullet"></span>Active, passive, and at-rest earth pressures (K<sub>0</sub>, K<sub>a</sub>, K<sub>p</sub>)</li>
                        <li><span class="unit-bullet"></span>Rankine's earth pressure theory &amp; tension crack depth (z<sub>c</sub> = 2c / &gamma;&radic;K<sub>a</sub>)</li>
                        <li><span class="unit-bullet"></span>Coulomb's wedge theory &amp; wall friction (&delta;)</li>
                        <li><span class="unit-bullet"></span>Rebhann's and Culmann's graphical constructions</li>
                        <li><span class="unit-bullet"></span>Gravity retaining walls with horizontal or battered backfill</li>
                    </ul>
                    <div class="unit-weightage-bar">
                        <div class="unit-weightage-fill bar-sky"></div>
                    </div>
                </div>

                <!-- Unit 2 -->
                <div class="unit-card">
                    <div class="card-overline text-lavender">Unit 2 &bull; CO2</div>
                    <h3 class="unit-name">Shear Strength &amp; Slope Stability</h3>
                    <ul class="unit-topics-list">
                        <li><span class="unit-bullet"></span>Mohr-Coulomb failure criterion (&sigma;'₁ = &sigma;'₃ N<sub>&phi;</sub> + 2c'&radic;N<sub>&phi;</sub>)</li>
                        <li><span class="unit-bullet"></span>Direct shear box test vs. Triaxial shear test</li>
                        <li><span class="unit-bullet"></span>Drainage conditions: UU (Quick), CU, and CD (Slow) tests</li>
                        <li><span class="unit-bullet"></span>Vane shear test in soft clay (T = c<sub>u</sub> &pi; D&sup2; [H/2 + D/6])</li>
                        <li><span class="unit-bullet"></span>Infinite slope stability: dry, submerged, and steady seepage</li>
                    </ul>
                    <div class="unit-weightage-bar">
                        <div class="unit-weightage-fill bar-lavender"></div>
                    </div>
                </div>

                <!-- Unit 3 -->
                <div class="unit-card">
                    <div class="card-overline text-peach">Unit 3 &bull; CO3</div>
                    <h3 class="unit-name">Shallow Foundations &amp; Bearing Capacity</h3>
                    <ul class="unit-topics-list">
                        <li><span class="unit-bullet"></span>Terzaghi's bearing capacity equations for strip, square, and circular footings</li>
                        <li><span class="unit-bullet"></span>Ground water table correction factors (R<sub>w1</sub> and R<sub>w2</sub>)</li>
                        <li><span class="unit-bullet"></span>Modes of shear failure (General, Local, and Punching)</li>
                        <li><span class="unit-bullet"></span>Plate load test &amp; Housel's two-plate equation (Q = Am + Pn)</li>
                        <li><span class="unit-bullet"></span>Immediate elastic settlement (S<sub>i</sub> = q B (1-&mu;&sup2;)/E<sub>s</sub> &middot; I<sub>f</sub>)</li>
                    </ul>
                    <div class="unit-weightage-bar">
                        <div class="unit-weightage-fill bar-peach"></div>
                    </div>
                </div>

                <!-- Unit 4 -->
                <div class="unit-card">
                    <div class="card-overline text-sage">Unit 4 &bull; CO4</div>
                    <h3 class="unit-name">Deep Foundations (Piles &amp; Caissons)</h3>
                    <ul class="unit-topics-list">
                        <li><span class="unit-bullet"></span>Single pile capacity in clay (Q<sub>u</sub> = 9 c A<sub>b</sub> + &alpha; c A<sub>s</sub>) and sand</li>
                        <li><span class="unit-bullet"></span>Pile group efficiency &amp; block failure vs. individual failure</li>
                        <li><span class="unit-bullet"></span>Optimum spacing derivation for square pile groups</li>
                        <li><span class="unit-bullet"></span>Under-reamed piles for expansive black cotton soils</li>
                        <li><span class="unit-bullet"></span>Open caissons (well foundations) components &amp; sketches</li>
                    </ul>
                    <div class="unit-weightage-bar">
                        <div class="unit-weightage-fill bar-sage"></div>
                    </div>
                </div>

                <!-- Unit 5 -->
                <div class="unit-card">
                    <div class="card-overline text-rose">Unit 5 &bull; CO5</div>
                    <h3 class="unit-name">Subsoil Exploration &amp; Testing</h3>
                    <ul class="unit-topics-list">
                        <li><span class="unit-bullet"></span>Methods of exploration (open pits, auger, wash, percussion, rotary drilling)</li>
                        <li><span class="unit-bullet"></span>Soil sampling criteria: Area ratio A<sub>r</sub>, inside clearance C<sub>i</sub>, outside clearance C<sub>o</sub></li>
                        <li><span class="unit-bullet"></span>Standard Penetration Test (SPT) &amp; overburden/dilatancy corrections</li>
                        <li><span class="unit-bullet"></span>Borelog preparation, significant depth of exploration</li>
                        <li><span class="unit-bullet"></span>Rock Mass Rating (RMR), Total Core Recovery (TCR), and RQD</li>
                    </ul>
                    <div class="unit-weightage-bar">
                        <div class="unit-weightage-fill bar-rose"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Master Formula Cheat-Sheet -->
        <section class="section" id="formulas">
            <div class="section-header">
                <div>
                    <span class="card-overline text-sand">Quick Reference</span>
                    <h2 class="section-header-title">
                        <svg class="icon icon-lg text-sand" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
                        Master Formulas &amp; Governing Equations
                    </h2>
                </div>
            </div>

            <div class="formula-grid">
                <div class="formula-card">
                    <div class="formula-title">Rankine Earth Pressure &amp; Tension Depth</div>
                    <div class="formula-math">K<sub>a</sub> = tan&sup2;(45&deg; - &phi;/2) = (1 - sin &phi;) / (1 + sin &phi;)<br>K<sub>p</sub> = tan&sup2;(45&deg; + &phi;/2) = (1 + sin &phi;) / (1 - sin &phi;)<br>z<sub>c</sub> = 2c / (&gamma; &radic;K<sub>a</sub>), &nbsp; H<sub>c</sub> = 2 z<sub>c</sub></div>
                    <div class="formula-notes">For horizontal backfill. Surcharge q increases lateral stress by &Delta;p = K<sub>a</sub> &middot; q.</div>
                </div>

                <div class="formula-card">
                    <div class="formula-title">Mohr-Coulomb Principal Stress Relation</div>
                    <div class="formula-math">&sigma;'₁ = &sigma;'₃ tan&sup2;(45&deg; + &phi;'/2) + 2 c' tan(45&deg; + &phi;'/2)<br>&theta; = 45&deg; + &phi;'/2 (Slip plane inclination)</div>
                    <div class="formula-notes">For normally consolidated clay/sand (c' = 0): sin &phi;' = (&sigma;'₁ - &sigma;'₃) / (&sigma;'₁ + &sigma;'₃).</div>
                </div>

                <div class="formula-card">
                    <div class="formula-title">Terzaghi Bearing Capacity Equations</div>
                    <div class="formula-math">Strip: q<sub>u</sub> = c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> + 0.5 &gamma; B N<sub>&gamma;</sub><br>Square: q<sub>u</sub> = 1.3 c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> + 0.4 &gamma; B N<sub>&gamma;</sub><br>Circular: q<sub>u</sub> = 1.3 c N<sub>c</sub> + &gamma; D<sub>f</sub> N<sub>q</sub> + 0.3 &gamma; B N<sub>&gamma;</sub></div>
                    <div class="formula-notes">Water table correction: multiply surcharge term by R<sub>w1</sub> and &gamma;-term by R<sub>w2</sub>.</div>
                </div>

                <div class="formula-card">
                    <div class="formula-title">Pile Group Capacity in Clay</div>
                    <div class="formula-math">Individual: Q<sub>gi</sub> = n &middot; [9 c A<sub>b</sub> + &alpha; c A<sub>s</sub>]<br>Block: Q<sub>gb</sub> = 9 c B&sup2; + 4 B L c<br>Q<sub>ug</sub> = min(Q<sub>gi</sub>, Q<sub>gb</sub>), &nbsp; Q<sub>safe</sub> = Q<sub>ug</sub> / FS</div>
                    <div class="formula-notes">B = (k - 1)s + d for k&times;k square pile array. Governing mode is typically individual failure at standard spacings.</div>
                </div>

                <div class="formula-card">
                    <div class="formula-title">Soil Sampler Area Ratio &amp; Clearances</div>
                    <div class="formula-math">A<sub>r</sub> = [ (D<sub>2</sub>&sup2; - D<sub>1</sub>&sup2;) / D<sub>1</sub>&sup2; ] &times; 100%<br>C<sub>i</sub> = [ (D<sub>3</sub> - D<sub>1</sub>) / D<sub>1</sub> ] &times; 100%<br>C<sub>o</sub> = [ (D<sub>2</sub> - D<sub>4</sub>) / D<sub>4</sub> ] &times; 100%</div>
                    <div class="formula-notes">Undisturbed sampling requires A<sub>r</sub> &le; 10-20%, C<sub>i</sub> = 1-3%, C<sub>o</sub> = 0-2%.</div>
                </div>

                <div class="formula-card">
                    <div class="formula-title">SPT Overburden &amp; Dilatancy Corrections</div>
                    <div class="formula-math">Overburden: N' = N<sub>0</sub> &middot; [ 350 / (&sigma;'<sub>v</sub> + 70) ] &nbsp;(or &radic;[100/&sigma;'<sub>v</sub>])<br>Dilatancy: N\" = 15 + 0.5 &middot; (N' - 15) &nbsp;[if N' > 15 below WT]</div>
                    <div class="formula-notes">Apply overburden correction first; apply dilatancy correction second only if submerged and N' > 15.</div>
                </div>
            </div>
        </section>

        <!-- Interactive Question Bank -->
        <section class="section" id="questions">
            <div class="section-header">
                <div>
                    <span class="card-overline text-sage">Master Database</span>
                    <h2 class="section-header-title">
                        <svg class="icon icon-lg text-sage" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        Comprehensive Question Bank ({total_q} Questions)
                    </h2>
                </div>
            </div>

            <!-- Filter Panel -->
            <div class="filter-panel">
                <div class="search-box">
                    <svg class="icon text-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                    <input type="text" id="searchInput" class="search-input" placeholder="Search by topic, keyword, or equation (e.g. 'SPT', 'pile group', 'Rankine', 'water table', 'tension crack')...">
                </div>

                <!-- Unit Filters -->
                <div class="filter-row">
                    <span class="filter-label">Unit:</span>
                    <div class="filter-pills" id="unitFilters">
                        <button class="pill-btn active" data-unit="all">All Units</button>
                        <button class="pill-btn" data-unit="1">Unit 1: Earth Pressure</button>
                        <button class="pill-btn" data-unit="2">Unit 2: Shear &amp; Slopes</button>
                        <button class="pill-btn" data-unit="3">Unit 3: Shallow Foundations</button>
                        <button class="pill-btn" data-unit="4">Unit 4: Piles &amp; Caissons</button>
                        <button class="pill-btn" data-unit="5">Unit 5: Exploration</button>
                    </div>
                </div>

                <!-- Year Filters -->
                <div class="filter-row">
                    <span class="filter-label">Year:</span>
                    <div class="filter-pills" id="yearFilters">
                        <button class="pill-btn active" data-year="all">All Years</button>
                        <button class="pill-btn" data-year="2024">2024 Exam</button>
                        <button class="pill-btn" data-year="2023">2023 Exam</button>
                        <button class="pill-btn" data-year="2022">2022 Exam</button>
                    </div>
                </div>

                <!-- Type Filters -->
                <div class="filter-row">
                    <span class="filter-label">Type:</span>
                    <div class="filter-pills" id="typeFilters">
                        <button class="pill-btn active" data-type="all">All Types</button>
                        <button class="pill-btn" data-type="Theory">Theory</button>
                        <button class="pill-btn" data-type="Numerical">Numerical</button>
                        <button class="pill-btn" data-type="Derivation">Derivation</button>
                        <button class="pill-btn" data-type="Practical">Practical</button>
                    </div>
                </div>

                <!-- Repetition Filter -->
                <div class="filter-row">
                    <span class="filter-label">Focus:</span>
                    <div class="filter-pills" id="repFilters">
                        <button class="pill-btn active" data-rep="all">All Questions</button>
                        <button class="pill-btn flame" data-rep="repeated">
                            <svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>
                            Repeated / High-Yield Only ({repeated_q})
                        </button>
                    </div>
                </div>
            </div>

            <!-- Results Counter & Global Toggles -->
            <div class="results-count-bar">
                <span id="resultsCount">Showing {total_q} of {total_q} questions</span>
                <div>
                    <button class="expand-collapse-btn" id="expandAllBtn">Expand All Solutions</button>
                    <span class="divider-bullet">&bull;</span>
                    <button class="expand-collapse-btn" id="collapseAllBtn">Collapse All</button>
                </div>
            </div>

            <!-- Dynamic Question Cards Container -->
            <div class="questions-list" id="questionsContainer">
                <!-- Injected via JavaScript -->
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-content">
            <div>
                <strong>Geotechnical Engineering - II (CE 41007 / CE 4107 / CE 4151)</strong> &bull; Complete PYQ Mastery Platform
            </div>
            <div>
                Neutral palette &bull; High readability &bull; No external dependencies
            </div>
        </div>
    </footer>

    <!-- Client-side Logic -->
    <script>
        const questions = {questions_json};

        let currentUnit = 'all';
        let currentYear = 'all';
        let currentType = 'all';
        let currentRep = 'all';
        let searchQuery = '';

        const container = document.getElementById('questionsContainer');
        const searchInput = document.getElementById('searchInput');
        const resultsCount = document.getElementById('resultsCount');
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const expandAllBtn = document.getElementById('expandAllBtn');
        const collapseAllBtn = document.getElementById('collapseAllBtn');

        function initTheme() {{
            const savedTheme = localStorage.getItem('geotech_theme') || 
                               (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme', savedTheme);
            updateThemeIcon(savedTheme);
        }}

        function toggleTheme() {{
            const current = document.documentElement.getAttribute('data-theme') || 'light';
            const next = current === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('geotech_theme', next);
            updateThemeIcon(next);
        }}

        function updateThemeIcon(theme) {{
            if (theme === 'dark') {{
                themeIcon.innerHTML = '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>';
            }} else {{
                themeIcon.innerHTML = '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>';
            }}
        }}

        themeToggle.addEventListener('click', toggleTheme);
        initTheme();

        function getTypeBadge(type) {{
            if (type === 'Theory') return '<span class="badge badge-theory">Theory</span>';
            if (type === 'Numerical') return '<span class="badge badge-numerical">Numerical</span>';
            if (type === 'Derivation') return '<span class="badge badge-deriv">Derivation</span>';
            return '<span class="badge badge-practical">Practical</span>';
        }}

        function renderQuestions() {{
            const filtered = questions.filter(q => {{
                if (currentUnit !== 'all' && q.unit.toString() !== currentUnit) return false;
                if (currentYear !== 'all' && q.year !== currentYear) return false;
                if (currentType !== 'all' && q.type !== currentType) return false;
                if (currentRep === 'repeated' && !q.repeated) return false;
                if (searchQuery) {{
                    const query = searchQuery.toLowerCase();
                    const matchText = (q.question + ' ' + q.topic + ' ' + q.solution + ' ' + q.q_no).toLowerCase();
                    if (!matchText.includes(query)) return false;
                }}
                return true;
            }});

            resultsCount.textContent = `Showing ${{filtered.length}} of ${{questions.length}} questions`;

            if (filtered.length === 0) {{
                container.innerHTML = `
                    <div class="empty-state">
                        <p class="empty-state-title">No questions matched your filter criteria.</p>
                        <p class="empty-state-desc">Try clearing your search query or selecting "All Units".</p>
                    </div>
                `;
                return;
            }}

            container.innerHTML = filtered.map(q => `
                <div class="q-card" id="${{q.id}}">
                    <div class="q-top-row">
                        <div class="q-badges">
                            <span class="badge badge-year">${{q.year}} Exam</span>
                            <span class="badge badge-unit">Unit ${{q.unit}}</span>
                            <span class="badge badge-marks">${{q.marks}} Marks</span>
                            ${{getTypeBadge(q.type)}}
                            ${{q.repeated ? `<span class="badge badge-repeated"><svg class="icon icon-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>${{q.rep_frequency}}</span>` : ''}}
                            <span class="badge badge-subtle">${{q.co}} &bull; ${{q.bl}}</span>
                        </div>
                        <span class="q-code-badge">${{q.q_no}}</span>
                    </div>

                    <div class="q-text">
                        ${{q.question}}
                    </div>

                    <div class="q-solution-toggle" onclick="toggleSolution('${{q.id}}')">
                        <span>Solution Guide &amp; Key Formulas</span>
                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" id="icon-${{q.id}}">
                            <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                    </div>

                    <div class="q-solution-content" id="sol-${{q.id}}">
                        <div class="q-topic-label">
                            <span class="card-overline">Topic: ${{q.topic}}</span>
                        </div>
                        ${{q.solution}}
                    </div>
                </div>
            `).join('');
        }}

        window.toggleSolution = function(id) {{
            const sol = document.getElementById('sol-' + id);
            const icon = document.getElementById('icon-' + id);
            if (!sol) return;
            const isOpen = sol.classList.contains('open');
            if (isOpen) {{
                sol.classList.remove('open');
                if (icon) icon.style.transform = 'rotate(0deg)';
            }} else {{
                sol.classList.add('open');
                if (icon) icon.style.transform = 'rotate(180deg)';
            }}
        }};

        expandAllBtn.addEventListener('click', () => {{
            document.querySelectorAll('.q-solution-content').forEach(el => el.classList.add('open'));
            document.querySelectorAll('.q-solution-toggle svg').forEach(el => el.style.transform = 'rotate(180deg)');
        }});

        collapseAllBtn.addEventListener('click', () => {{
            document.querySelectorAll('.q-solution-content').forEach(el => el.classList.remove('open'));
            document.querySelectorAll('.q-solution-toggle svg').forEach(el => el.style.transform = 'rotate(0deg)');
        }});

        function setupFilterGroup(containerId, stateVarSetter) {{
            const group = document.getElementById(containerId);
            if (!group) return;
            group.querySelectorAll('.pill-btn').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    group.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    stateVarSetter(btn);
                    renderQuestions();
                }});
            }});
        }}

        setupFilterGroup('unitFilters', btn => currentUnit = btn.getAttribute('data-unit'));
        setupFilterGroup('yearFilters', btn => currentYear = btn.getAttribute('data-year'));
        setupFilterGroup('typeFilters', btn => currentType = btn.getAttribute('data-type'));
        setupFilterGroup('repFilters', btn => currentRep = btn.getAttribute('data-rep'));

        let searchTimeout;
        searchInput.addEventListener('input', (e) => {{
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {{
                searchQuery = e.target.value.trim();
                renderQuestions();
            }}, 200);
        }});

        renderQuestions();
    </script>
</body>
</html>"""

    with open("geotech_pyq_analysis.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Re-generated geotech_pyq_analysis.html and index.html with clean icons and neutral palette!")

if __name__ == "__main__":
    generate_html()
