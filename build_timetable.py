import json

def generate_timetable_html():
    html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="theme-color" id="metaThemeColor" content="#fbfaf8">
    <meta name="format-detection" content="telephone=no">
    <title>Civil Engineering Exam Timetable | Nov – Dec 2026</title>
    <meta name="description" content="Civil Engineering Examination Timetable (Nov - Dec 2026) updated per the official Revised Examination Timetable for 7 paper subjects.">
    <style>
        :root {
            --font-size-h1: 32px;
            --line-height-h1: 42px;
            --font-size-h2: 22px;
            --line-height-h2: 30px;
            --font-size-h6: 16px;
            --line-height-h6: 22px;
            --font-size-body-large: 15px;
            --line-height-body-large: 22px;
            --font-size-body-medium: 14px;
            --line-height-body-medium: 20px;
            --font-size-body-small: 12px;
            --line-height-body-small: 16px;
            --font-size-button: 13px;
            --line-height-button: 18px;
            --font-size-stat: 24px;
            --line-height-stat: 32px;
            --font-size-overline: 11px;

            --background: #fbfaf8;
            --foreground: #1e293b;
            --card: #ffffff;
            --card-foreground: #1e293b;
            --muted: #f3f1ec;
            --muted-foreground: #64748b;
            --border: #e8e5dc;
            --border-hover: #d8d4c9;
            --primary: #2d3748;
            --primary-foreground: #ffffff;

            --pastel-sage-bg: #eaf4ed;
            --pastel-sage-border: #c4e5ce;
            --pastel-sage-foreground: #205c36;

            --pastel-peach-bg: #fff1e8;
            --pastel-peach-border: #fed5c0;
            --pastel-peach-foreground: #9a4318;

            --pastel-sky-bg: #ebf5fd;
            --pastel-sky-border: #c1e0fa;
            --pastel-sky-foreground: #1a5a90;

            --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-full: 9999px;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: ui-monospace, Menlo, Monaco, Consolas, monospace;
        }

        [data-theme="dark"] {
            --background: #09090b;
            --foreground: #fcfcfd;
            --card: #141416;
            --card-foreground: #fcfcfd;
            --muted: #1c1c1f;
            --muted-foreground: #a1a1aa;
            --border: #27272a;
            --border-hover: #3f3f46;
            --primary: #fcfcfd;
            --primary-foreground: #09090b;

            --pastel-sage-bg: rgba(52, 211, 153, 0.16);
            --pastel-sage-border: rgba(52, 211, 153, 0.35);
            --pastel-sage-foreground: #34d399;

            --pastel-peach-bg: rgba(251, 146, 60, 0.16);
            --pastel-peach-border: rgba(251, 146, 60, 0.35);
            --pastel-peach-foreground: #fb923c;

            --pastel-sky-bg: rgba(56, 189, 248, 0.16);
            --pastel-sky-border: rgba(56, 189, 248, 0.35);
            --pastel-sky-foreground: #38bdf8;

            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
        }

        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
            transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
        }

        html, body {
            overflow-x: hidden;
            width: 100%;
            -webkit-text-size-adjust: 100%;
        }

        body {
            background-color: var(--background);
            color: var(--foreground);
            font-family: var(--font-sans);
            font-size: var(--font-size-body-medium);
            line-height: var(--line-height-body-medium);
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
        }

        button, a, input, select {
            touch-action: manipulation;
        }

        a { color: inherit; text-decoration: none; }

        .container {
            max-width: 1040px;
            margin: 0 auto;
            padding-left: max(16px, env(safe-area-inset-left));
            padding-right: max(16px, env(safe-area-inset-right));
            box-sizing: border-box;
        }

        .header {
            position: sticky;
            top: 0;
            z-index: 50;
            background: var(--background);
            border-bottom: 1px solid var(--border);
            backdrop-filter: blur(8px);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease;
            will-change: transform;
        }

        .header.header-hidden {
            transform: translateY(-100%);
            box-shadow: none;
            pointer-events: none;
        }

        .nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 56px;
            gap: 12px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
            white-space: nowrap;
        }

        .brand-badge {
            background: var(--pastel-peach-bg);
            border: 1px solid var(--pastel-peach-border);
            color: var(--pastel-peach-foreground);
            font-size: var(--font-size-overline);
            font-weight: 700;
            padding: 2px 7px;
            border-radius: var(--radius-sm);
            text-transform: uppercase;
            flex-shrink: 0;
        }

        .brand-title {
            font-size: var(--font-size-body-large);
            font-weight: 600;
            white-space: nowrap;
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 8px;
            list-style: none;
            flex-wrap: nowrap;
            overflow-x: auto;
            scrollbar-width: none;
        }

        .nav-links::-webkit-scrollbar { display: none; }

        .nav-link {
            font-size: var(--font-size-button);
            color: var(--muted-foreground);
            padding: 4px 10px;
            border-radius: var(--radius-full);
            cursor: pointer;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .nav-link:hover, .nav-link.active {
            color: var(--foreground);
            background: var(--muted);
        }

        .theme-toggle-btn {
            background: var(--card);
            border: 1px solid var(--border);
            color: var(--foreground);
            width: 34px;
            height: 34px;
            border-radius: var(--radius-full);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
        }

        /* Scroll to Top Button (Always Visible in Bottom-Right Corner) */
        .scroll-to-top-btn {
            position: fixed !important;
            bottom: 2rem !important;
            right: 2rem !important;
            z-index: 99999 !important;
            width: 48px;
            height: 48px;
            border-radius: var(--radius-full);
            background: var(--primary);
            color: var(--primary-foreground);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28);
            display: inline-flex !important;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0.95;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s ease, opacity 0.2s ease, box-shadow 0.2s ease;
        }

        .scroll-to-top-btn:hover {
            opacity: 1;
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        }

        .scroll-to-top-btn:active {
            transform: translateY(0) scale(0.96);
        }

        .scroll-to-top-btn svg {
            width: 22px;
            height: 22px;
            stroke-width: 2.5;
            stroke: currentColor;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        @media (max-width: 640px) {
            .scroll-to-top-btn {
                bottom: 1.25rem !important;
                right: 1.25rem !important;
                width: 42px;
                height: 42px;
            }
            .scroll-to-top-btn svg {
                width: 20px;
                height: 20px;
            }
        }

        .hero {
            padding: 20px 0 14px 0;
            border-bottom: 1px solid var(--border);
        }

        .hero-meta {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
            flex-wrap: wrap;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            font-size: var(--font-size-body-small);
            font-weight: 600;
            padding: 2px 8px;
            border-radius: var(--radius-full);
            border: 1px solid transparent;
            text-decoration: none;
        }

        .badge-sage {
            background: var(--pastel-sage-bg);
            border-color: var(--pastel-sage-border);
            color: var(--pastel-sage-foreground);
        }

        .badge-peach {
            background: var(--pastel-peach-bg);
            border-color: var(--pastel-peach-border);
            color: var(--pastel-peach-foreground);
        }

        .badge-sky {
            background: var(--pastel-sky-bg);
            border-color: var(--pastel-sky-border);
            color: var(--pastel-sky-foreground);
        }

        .hero-title {
            font-size: var(--font-size-h1);
            line-height: var(--line-height-h1);
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 4px;
        }

        .notice-bar {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 8px 14px;
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            font-size: var(--font-size-body-small);
            margin-top: 10px;
            flex-wrap: wrap;
        }

        .stats-bar {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 16px 0;
        }

        .stat-box {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 10px 14px;
        }

        .stat-label {
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            color: var(--muted-foreground);
            margin-bottom: 2px;
        }

        .stat-value {
            font-size: var(--font-size-stat);
            line-height: var(--line-height-stat);
            font-weight: 700;
        }

        .controls-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 16px;
            flex-wrap: wrap;
        }

        .filter-tabs {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .tab-btn {
            background: var(--muted);
            border: 1px solid var(--border);
            color: var(--muted-foreground);
            font-size: var(--font-size-button);
            font-weight: 500;
            padding: 5px 12px;
            border-radius: var(--radius-full);
            cursor: pointer;
        }

        .tab-btn.active {
            background: var(--primary);
            border-color: var(--primary);
            color: var(--primary-foreground);
            font-weight: 600;
        }

        .sort-btn {
            background: var(--muted);
            border: 1px solid var(--border);
            color: var(--foreground);
            font-size: var(--font-size-button);
            font-weight: 600;
            padding: 5px 12px;
            border-radius: var(--radius-full);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .sort-btn:hover {
            background: var(--card);
            border-color: var(--border-hover);
        }

        .view-switchers {
            display: flex;
            background: var(--muted);
            padding: 2px;
            border-radius: var(--radius-full);
            border: 1px solid var(--border);
        }

        .view-btn {
            background: transparent;
            border: none;
            color: var(--muted-foreground);
            font-size: var(--font-size-body-small);
            font-weight: 500;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            cursor: pointer;
        }

        .view-btn.active {
            background: var(--card);
            color: var(--foreground);
            font-weight: 600;
        }

        /* ----------------------------------------------------
           SEPARATED CALENDARS (November & December)
           Weekdays arranged vertically as rows
           ---------------------------------------------------- */
        .cal-separated-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 24px;
        }

        .cal-box {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 16px;
        }

        .cal-box-header {
            font-size: var(--font-size-h6);
            font-weight: 600;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .cal-grid-vertical {
            display: grid;
            grid-template-columns: 46px repeat(5, 1fr);
            gap: 4px;
            align-items: center;
        }

        .cal-col-label {
            font-size: var(--font-size-overline);
            font-weight: 600;
            color: var(--muted-foreground);
            text-align: center;
            padding: 4px 0;
            text-transform: uppercase;
        }

        .cal-row-label {
            font-size: var(--font-size-body-small);
            font-weight: 700;
            color: var(--muted-foreground);
            text-align: left;
            padding: 6px 2px;
        }

        .cal-cell {
            min-height: 44px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-radius: var(--radius-sm);
            font-size: var(--font-size-body-small);
            font-weight: 500;
            border: 1px solid transparent;
            background: var(--background);
            text-align: center;
        }

        .cal-cell.empty {
            background: transparent;
            color: transparent;
            pointer-events: none;
            border-color: transparent;
        }

        .cal-cell.exam-reg {
            background: var(--pastel-sage-bg);
            border-color: var(--pastel-sage-border);
            color: var(--pastel-sage-foreground);
            font-weight: 700;
            cursor: pointer;
        }

        .cal-cell.exam-old {
            background: var(--pastel-peach-bg);
            border-color: var(--pastel-peach-border);
            color: var(--pastel-peach-foreground);
            font-weight: 700;
            cursor: pointer;
        }

        .cal-cell.today,
        .cal-cell.current-date {
            background: var(--pastel-sky-bg);
            border-color: var(--pastel-sky-border);
            color: var(--pastel-sky-foreground);
            font-weight: 700;
            position: relative;
            box-shadow: 0 0 0 1px var(--pastel-sky-border);
            cursor: pointer;
        }

        .cal-cell.today:hover,
        .cal-cell.current-date:hover {
            border-color: var(--pastel-sky-foreground);
            box-shadow: 0 2px 8px rgba(56, 189, 248, 0.25);
        }

        .cal-cell.today.exam-reg,
        .cal-cell.current-date.exam-reg {
            background: var(--pastel-sage-bg);
            border-color: var(--pastel-sky-foreground);
            color: var(--pastel-sage-foreground);
            box-shadow: 0 0 0 2px var(--pastel-sky-border);
        }

        .cal-cell.today.exam-old,
        .cal-cell.current-date.exam-old {
            background: var(--pastel-peach-bg);
            border-color: var(--pastel-sky-foreground);
            color: var(--pastel-peach-foreground);
            box-shadow: 0 0 0 2px var(--pastel-sky-border);
        }

        /* Dedicated blue box for current date inside the calendar view */
        .cal-today-box {
            background: var(--pastel-sky-bg);
            border: 1px solid var(--pastel-sky-border);
            color: var(--pastel-sky-foreground);
            border-radius: var(--radius-md);
            padding: 12px 16px;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
        }

        .cal-today-box-left {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .cal-today-box-right {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: var(--font-size-body-small);
        }

        .cal-today-date-text {
            font-size: var(--font-size-body-medium);
            font-weight: 600;
        }

        .cal-today-countdown {
            background: var(--card);
            color: var(--foreground);
            padding: 3px 10px;
            border-radius: var(--radius-full);
            font-weight: 600;
            border: 1px solid var(--border);
            font-size: var(--font-size-body-small);
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .cal-cell-tag {
            font-size: 10px;
            line-height: 12px;
            margin-top: 1px;
            font-weight: 600;
        }

        /* Table */
        .table-wrap {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            overflow-x: auto;
            margin-bottom: 24px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: var(--font-size-body-medium);
        }

        th {
            background: var(--muted);
            color: var(--muted-foreground);
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 10px 14px;
            border-bottom: 1px solid var(--border);
            cursor: pointer;
            user-select: none;
        }

        th:hover {
            color: var(--foreground);
        }

        td {
            padding: 12px 14px;
            border-bottom: 1px solid var(--border);
            vertical-align: middle;
        }

        tr:last-child td { border-bottom: none; }
        tr:hover td { background: var(--muted); }

        .code-tag {
            font-family: var(--font-mono);
            font-size: var(--font-size-body-small);
            background: var(--muted);
            padding: 2px 6px;
            border-radius: var(--radius-sm);
            font-weight: 600;
        }

        /* Timeline */
        .timeline-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 24px;
        }

        .timeline-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 12px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }

        .timeline-card.regular { border-left: 4px solid var(--pastel-sage-foreground); }
        .timeline-card.old { border-left: 4px solid var(--pastel-peach-foreground); }

        .footer {
            border-top: 1px solid var(--border);
            padding: 16px 0;
            text-align: center;
            color: var(--muted-foreground);
            font-size: var(--font-size-body-small);
            margin-top: 20px;
        }

        /* ----------------------------------------------------
           RESPONSIVE APP & MOBILE BOTTOM NAVIGATION SYSTEM
           ---------------------------------------------------- */
        .mobile-bottom-nav {
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background-color: var(--card);
            border-top: 1px solid var(--border);
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
            padding-bottom: env(safe-area-inset-bottom, 0px);
            height: calc(56px + env(safe-area-inset-bottom, 0px));
            align-items: stretch;
            justify-content: space-around;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }

        [data-theme="dark"] .mobile-bottom-nav {
            box-shadow: 0 -2px 12px rgba(0, 0, 0, 0.5);
            border-top-color: var(--border);
        }

        .mobile-nav-item {
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
        }

        .mobile-nav-item:active {
            transform: scale(0.94);
        }

        .mobile-nav-item.active {
            color: var(--foreground);
            font-weight: 600;
        }

        .mobile-nav-icon {
            width: 20px;
            height: 20px;
            stroke-width: 2.2;
            stroke: currentColor;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
            transition: transform 0.15s ease;
        }

        .mobile-nav-item.active .mobile-nav-icon {
            stroke-width: 2.5;
            transform: translateY(-1px);
        }

        .mobile-nav-label {
            font-size: 11px;
            line-height: 1.2;
            letter-spacing: -0.01em;
        }

        .mobile-nav-item.active .mobile-nav-label {
            font-weight: 600;
        }

        @media (max-width: 768px) {
            .mobile-bottom-nav {
                display: flex;
            }
            body {
                padding-bottom: calc(64px + env(safe-area-inset-bottom, 0px));
            }
            .header .nav-links {
                display: none !important;
            }
            .nav {
                height: 52px;
            }
            .brand-title {
                font-size: 0.95rem;
                max-width: calc(100vw - 120px);
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
            .scroll-to-top-btn {
                bottom: calc(72px + env(safe-area-inset-bottom, 0px)) !important;
                right: 1.25rem !important;
                width: 42px !important;
                height: 42px !important;
            }
            .scroll-to-top-btn svg {
                width: 20px !important;
                height: 20px !important;
            }
            .hero-title {
                font-size: 22px !important;
                line-height: 28px !important;
            }
            .hero-meta {
                flex-wrap: wrap;
                gap: 6px;
            }
            .notice-bar {
                flex-direction: column;
                align-items: flex-start;
                gap: 6px;
            }
            .controls-bar {
                flex-direction: column;
                align-items: stretch;
                gap: 10px;
            }
            .filter-tabs {
                width: 100%;
                display: flex;
            }
            .tab-btn {
                flex: 1;
                text-align: center;
                padding: 6px 8px;
                font-size: 12px;
            }
            .controls-bar > div:last-child {
                width: 100%;
                flex-direction: column;
                gap: 8px !important;
            }
            .sort-btn {
                width: 100%;
                justify-content: center;
            }
            .view-switchers {
                width: 100%;
                display: flex;
            }
            .view-btn {
                flex: 1;
                text-align: center;
                padding: 6px 4px;
                font-size: 11px;
            }
            .stats-bar {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
            }
            .stat-box {
                padding: 10px;
            }
            .stat-value {
                font-size: 20px;
                line-height: 26px;
            }
            .cal-today-box {
                padding: 10px 12px;
                gap: 8px;
            }
            .cal-today-box-left {
                width: 100%;
                justify-content: space-between;
            }
            .cal-today-box-right {
                width: 100%;
                justify-content: space-between;
            }
            .cal-separated-container {
                grid-template-columns: 1fr;
                gap: 14px;
            }
            .cal-box {
                padding: 12px 8px;
            }
            .cal-grid-vertical {
                grid-template-columns: 36px repeat(5, 1fr);
                gap: 2px;
            }
            .cal-cell {
                min-height: 38px;
                font-size: 11px;
                padding: 2px;
            }
            .cal-row-label {
                font-size: 11px;
            }
            .cal-col-label {
                font-size: 10px;
            }
            .table-wrap {
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
            }
        }

        @media print {
            .header, .controls-bar, .theme-toggle-btn, .footer { display: none !important; }
            body { background: #fff !important; color: #000 !important; }
            .table-wrap, .stat-box, .cal-box { border: 1px solid #ccc !important; box-shadow: none !important; }
        }
    </style>
</head>
<body>

    <header class="header">
        <div class="container nav">
            <div class="brand">
                <span class="brand-badge">Nov – Dec</span>
                <span class="brand-title">Civil Engineering Timetable</span>
            </div>
            <ul class="nav-links">
                <li><a href="index.html" class="nav-link">← PYQ Master</a></li>
                <li><a class="nav-link active" onclick="showView('calendar')">Separated Calendars</a></li>
                <li><a class="nav-link" onclick="showView('table')">Table</a></li>
                <li><a class="nav-link" onclick="showView('timeline')">Timeline</a></li>
            </ul>
            <div style="display: flex; gap: 8px;">
                <button class="theme-toggle-btn" id="themeToggle" aria-label="Toggle Theme" title="Toggle Theme">
                    <svg id="themeIcon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                </button>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-meta">
                <span class="badge badge-peach">Nov to Dec 2026</span>
                <span class="badge badge-sky" id="heroTodayBadge">Today: 16 Nov 2026</span>
                <span class="badge badge-sky">Timing: 2:00 PM – 5:00 PM</span>
                <span class="badge badge-sage">Revised Timetable (SGSITS Indore)</span>
            </div>
            <h1 class="hero-title">Civil Engineering Examination Timetable</h1>

            <div class="notice-bar">
                <span><strong>Key:</strong></span>
                <span><span class="badge badge-sky" style="padding: 1px 7px;">Today</span> Current Date (16 Nov)</span>
                <span><span class="badge badge-sage" style="padding: 1px 7px;">Regular</span> Plain in note (Geo-2, DHS, RCC)</span>
                <span><span class="badge badge-peach" style="padding: 1px 7px;">Old Syllabus</span> Tagged Old in note (SA-2, SA-I, Geo I, Water)</span>
                <span style="margin-left: auto; color: var(--muted-foreground);">Dates matched to Official Revised PDF</span>
            </div>
        </section>

        <!-- Stats Bar -->
        <section class="stats-bar">
            <div class="stat-box">
                <div class="stat-label">Total Papers</div>
                <div class="stat-value">7</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Regular Papers</div>
                <div class="stat-value" style="color: var(--pastel-sage-foreground);">3</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Old Syllabus</div>
                <div class="stat-value" style="color: var(--pastel-peach-foreground);">4</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Date Range</div>
                <div class="stat-value" style="font-size: 18px; line-height: 32px;">18 Nov – 12 Dec</div>
            </div>
        </section>

        <!-- Filter Controls & Date Sort -->
        <div class="controls-bar">
            <div class="filter-tabs">
                <button class="tab-btn active" data-filter="all" onclick="setFilter('all')">All (7)</button>
                <button class="tab-btn" data-filter="regular" onclick="setFilter('regular')">Regular (3)</button>
                <button class="tab-btn" data-filter="old" onclick="setFilter('old')">Old Syllabus (4)</button>
            </div>

            <div style="display: flex; align-items: center; gap: 8px;">
                <button class="sort-btn" id="sortDateBtn" onclick="toggleDateSort()">
                    <span id="sortDirectionLabel">Sort Date: Ascending ▲</span>
                </button>

                <div class="view-switchers">
                    <button class="view-btn active" id="btnCalendar" onclick="showView('calendar')">Separated Calendars</button>
                    <button class="view-btn" id="btnTable" onclick="showView('table')">Table</button>
                    <button class="view-btn" id="btnTimeline" onclick="showView('timeline')">Timeline</button>
                </div>
            </div>
        </div>

        <!-- VIEW 1: SEPARATED CALENDARS (November & December side-by-side) -->
        <section id="calendar-view">
            <!-- Dedicated Blue Box with Current Date & Next Exam Status -->
            <div class="cal-today-box">
                <div class="cal-today-box-left">
                    <span class="badge badge-sky" style="font-size: 11px; text-transform: uppercase; font-weight: 700; letter-spacing: 0.04em;">Today</span>
                    <span class="cal-today-date-text" id="calTodayDateText">Current Date: Monday, 16 November 2026</span>
                </div>
                <div class="cal-today-box-right" id="calTodayCountdownBox">
                    <span>Upcoming:</span>
                    <span class="cal-today-countdown">
                        <strong style="color: var(--pastel-sage-foreground);">18 Nov (Geo-2)</strong> &bull; in 2 days
                    </span>
                </div>
            </div>

            <div class="cal-separated-container">
                <!-- November 2026 -->
                <div class="cal-box">
                    <div class="cal-box-header">
                        <span>November 2026</span>
                        <div style="display: flex; gap: 6px; align-items: center;">
                            <span class="badge badge-sky" id="novTodayBadge" style="font-size: 11px;">Today: 16 Nov</span>
                            <span class="badge badge-peach" style="font-size: 11px;">3 Papers</span>
                        </div>
                    </div>
                    <div class="cal-grid-vertical">
                        <div class="cal-col-label">Day</div>
                        <div class="cal-col-label">W1</div>
                        <div class="cal-col-label">W2</div>
                        <div class="cal-col-label">W3</div>
                        <div class="cal-col-label">W4</div>
                        <div class="cal-col-label">W5</div>

                        <!-- Sun -->
                        <div class="cal-row-label">Sun</div>
                        <div class="cal-cell" data-date="2026-11-01">1</div>
                        <div class="cal-cell" data-date="2026-11-08">8</div>
                        <div class="cal-cell" data-date="2026-11-15">15</div>
                        <div class="cal-cell" data-date="2026-11-22">22</div>
                        <div class="cal-cell" data-date="2026-11-29">29</div>

                        <!-- Mon -->
                        <div class="cal-row-label">Mon</div>
                        <div class="cal-cell" data-date="2026-11-02">2</div>
                        <div class="cal-cell" data-date="2026-11-09">9</div>
                        <div class="cal-cell today current-date" data-date="2026-11-16" title="Today: 16 Nov 2026 (Current Date)">
                            <span>16</span>
                            <span class="cal-cell-tag">Today</span>
                        </div>
                        <div class="cal-cell" data-date="2026-11-23">23</div>
                        <div class="cal-cell exam-old" data-date="2026-11-30" title="30 Nov: Structural Analysis - I (Old Syllabus)">
                            <span>30</span>
                            <span class="cal-cell-tag">SA-I</span>
                        </div>

                        <!-- Tue -->
                        <div class="cal-row-label">Tue</div>
                        <div class="cal-cell" data-date="2026-11-03">3</div>
                        <div class="cal-cell" data-date="2026-11-10">10</div>
                        <div class="cal-cell" data-date="2026-11-17">17</div>
                        <div class="cal-cell" data-date="2026-11-24">24</div>
                        <div class="cal-cell empty">—</div>

                        <!-- Wed -->
                        <div class="cal-row-label">Wed</div>
                        <div class="cal-cell" data-date="2026-11-04">4</div>
                        <div class="cal-cell" data-date="2026-11-11">11</div>
                        <div class="cal-cell exam-reg" data-date="2026-11-18" title="18 Nov: Geotechnical Engineering - II (Regular)">
                            <span>18</span>
                            <span class="cal-cell-tag">Geo-2</span>
                        </div>
                        <div class="cal-cell" data-date="2026-11-25">25</div>
                        <div class="cal-cell empty">—</div>

                        <!-- Thu -->
                        <div class="cal-row-label">Thu</div>
                        <div class="cal-cell" data-date="2026-11-05">5</div>
                        <div class="cal-cell" data-date="2026-11-12">12</div>
                        <div class="cal-cell" data-date="2026-11-19">19</div>
                        <div class="cal-cell exam-old" data-date="2026-11-26" title="26 Nov: Structural Analysis - II (Old Syllabus)">
                            <span>26</span>
                            <span class="cal-cell-tag">SA-2</span>
                        </div>
                        <div class="cal-cell empty">—</div>

                        <!-- Fri -->
                        <div class="cal-row-label">Fri</div>
                        <div class="cal-cell" data-date="2026-11-06">6</div>
                        <div class="cal-cell" data-date="2026-11-13">13</div>
                        <div class="cal-cell" data-date="2026-11-20">20</div>
                        <div class="cal-cell" data-date="2026-11-27">27</div>
                        <div class="cal-cell empty">—</div>

                        <!-- Sat -->
                        <div class="cal-row-label">Sat</div>
                        <div class="cal-cell" data-date="2026-11-07">7</div>
                        <div class="cal-cell" data-date="2026-11-14">14</div>
                        <div class="cal-cell" data-date="2026-11-21">21</div>
                        <div class="cal-cell" data-date="2026-11-28">28</div>
                        <div class="cal-cell empty">—</div>
                    </div>
                </div>

                <!-- December 2026 -->
                <div class="cal-box">
                    <div class="cal-box-header">
                        <span>December 2026</span>
                        <div style="display: flex; gap: 6px; align-items: center;">
                            <span class="badge badge-sky" id="decTodayBadge" style="font-size: 11px; display: none;">Today</span>
                            <span class="badge badge-sky" style="font-size: 11px;">4 Papers</span>
                        </div>
                    </div>
                    <div class="cal-grid-vertical">
                        <div class="cal-col-label">Day</div>
                        <div class="cal-col-label">W1</div>
                        <div class="cal-col-label">W2</div>
                        <div class="cal-col-label">W3</div>
                        <div class="cal-col-label">W4</div>
                        <div class="cal-col-label">W5</div>

                        <!-- Sun -->
                        <div class="cal-row-label">Sun</div>
                        <div class="cal-cell empty">—</div>
                        <div class="cal-cell" data-date="2026-12-06">6</div>
                        <div class="cal-cell" data-date="2026-12-13">13</div>
                        <div class="cal-cell" data-date="2026-12-20">20</div>
                        <div class="cal-cell" data-date="2026-12-27">27</div>

                        <!-- Mon -->
                        <div class="cal-row-label">Mon</div>
                        <div class="cal-cell empty">—</div>
                        <div class="cal-cell" data-date="2026-12-07">7</div>
                        <div class="cal-cell" data-date="2026-12-14">14</div>
                        <div class="cal-cell" data-date="2026-12-21">21</div>
                        <div class="cal-cell" data-date="2026-12-28">28</div>

                        <!-- Tue -->
                        <div class="cal-row-label">Tue</div>
                        <div class="cal-cell" data-date="2026-12-01">1</div>
                        <div class="cal-cell" data-date="2026-12-08">8</div>
                        <div class="cal-cell" data-date="2026-12-15">15</div>
                        <div class="cal-cell" data-date="2026-12-22">22</div>
                        <div class="cal-cell" data-date="2026-12-29">29</div>

                        <!-- Wed -->
                        <div class="cal-row-label">Wed</div>
                        <div class="cal-cell" data-date="2026-12-02">2</div>
                        <div class="cal-cell exam-reg" data-date="2026-12-09" title="09 Dec: Design of RCC / Advanced RCC (Regular)">
                            <span>9</span>
                            <span class="cal-cell-tag">RCC</span>
                        </div>
                        <div class="cal-cell" data-date="2026-12-16">16</div>
                        <div class="cal-cell" data-date="2026-12-23">23</div>
                        <div class="cal-cell" data-date="2026-12-30">30</div>

                        <!-- Thu -->
                        <div class="cal-row-label">Thu</div>
                        <div class="cal-cell" data-date="2026-12-03">3</div>
                        <div class="cal-cell" data-date="2026-12-10">10</div>
                        <div class="cal-cell" data-date="2026-12-17">17</div>
                        <div class="cal-cell" data-date="2026-12-24">24</div>
                        <div class="cal-cell" data-date="2026-12-31">31</div>

                        <!-- Fri -->
                        <div class="cal-row-label">Fri</div>
                        <div class="cal-cell" data-date="2026-12-04">4</div>
                        <div class="cal-cell exam-old" data-date="2026-12-11" title="11 Dec: Water Resources Engineering (Old Syllabus)">
                            <span>11</span>
                            <span class="cal-cell-tag">Water</span>
                        </div>
                        <div class="cal-cell" data-date="2026-12-18">18</div>
                        <div class="cal-cell" data-date="2026-12-25">25</div>
                        <div class="cal-cell empty">—</div>

                        <!-- Sat -->
                        <div class="cal-row-label">Sat</div>
                        <div class="cal-cell exam-old" data-date="2026-12-05" title="05 Dec: Geotechnical Engineering - I (Old Syllabus)">
                            <span>5</span>
                            <span class="cal-cell-tag">Geo I</span>
                        </div>
                        <div class="cal-cell exam-reg" data-date="2026-12-12" title="12 Dec: Design of Hydraulic Structures (Regular)">
                            <span>12</span>
                            <span class="cal-cell-tag">DHS</span>
                        </div>
                        <div class="cal-cell" data-date="2026-12-19">19</div>
                        <div class="cal-cell" data-date="2026-12-26">26</div>
                        <div class="cal-cell empty">—</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- VIEW 2: TABLE (Sortable by Date) -->
        <section id="table-view" class="table-wrap" style="display: none;">
            <table>
                <thead>
                    <tr>
                        <th onclick="toggleDateSort()" title="Click to sort by date">
                            Exam Date <span id="thSortIcon">▲</span>
                        </th>
                        <th>Day</th>
                        <th>Code</th>
                        <th>Subject Name</th>
                        <th>Category</th>
                        <th>Prep Gap</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody id="tableBody"></tbody>
            </table>
        </section>

        <!-- VIEW 3: TIMELINE -->
        <section id="timeline-view" class="timeline-list" style="display: none;"></section>
    </main>

    <footer class="footer">
        <div class="container">
            <p>Civil Engineering Exam Schedule • Nov – Dec 2026 • Verified with Official Revised Timetable (SGSITS)</p>
        </div>
    </footer>

    <script>
        const schedule = [
            {
                id: 1,
                date: "18 Nov 2026",
                isoDate: "2026-11-18",
                day: "Wednesday",
                order: 18,
                code: "CE 41007",
                subject: "Geotechnical Engineering - II (Geo - 2)",
                tag: "Regular",
                isOld: false,
                gap: "First Exam",
                link: "index.html"
            },
            {
                id: 2,
                date: "26 Nov 2026",
                isoDate: "2026-11-26",
                day: "Thursday",
                order: 26,
                code: "CE 31505",
                subject: "Structural Analysis - II (SA-2)",
                tag: "Old Syllabus",
                isOld: true,
                gap: "8 Days Gap",
                link: null
            },
            {
                id: 3,
                date: "30 Nov 2026",
                isoDate: "2026-11-30",
                day: "Monday",
                order: 30,
                code: "CE 31007",
                subject: "Structural Analysis - I (SA-I)",
                tag: "Old Syllabus",
                isOld: true,
                gap: "4 Days Gap",
                link: null
            },
            {
                id: 4,
                date: "05 Dec 2026",
                isoDate: "2026-12-05",
                day: "Saturday",
                order: 35,
                code: "CE 31517",
                subject: "Geotechnical Engineering - I (Geo I)",
                tag: "Old Syllabus",
                isOld: true,
                gap: "5 Days Gap",
                link: null
            },
            {
                id: 5,
                date: "09 Dec 2026",
                isoDate: "2026-12-09",
                day: "Wednesday",
                order: 39,
                code: "CE 41001",
                subject: "Design of Reinforced Concrete Structures (RCC)",
                tag: "Regular",
                isOld: false,
                gap: "4 Days Gap",
                link: null
            },
            {
                id: 6,
                date: "11 Dec 2026",
                isoDate: "2026-12-11",
                day: "Friday",
                order: 41,
                code: "CE 31713",
                subject: "Water Resources Engineering (Water)",
                tag: "Old Syllabus",
                isOld: true,
                gap: "2 Days Gap",
                link: null
            },
            {
                id: 7,
                date: "12 Dec 2026",
                isoDate: "2026-12-12",
                day: "Saturday",
                order: 42,
                code: "CE 41006",
                subject: "Design of Hydraulic Structures (DHS)",
                tag: "Regular",
                isOld: false,
                gap: "1 Day Gap",
                link: null
            }
        ];

        let activeFilter = 'all';
        let sortAscending = true;

        // Theme management
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');

        function initTheme() {
            const saved = localStorage.getItem('geotech_theme') || 
                          (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme', saved);
            updateIcon(saved);
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme') || 'light';
            const next = cur === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('geotech_theme', next);
            updateIcon(next);
        }

        function updateIcon(theme) {
            themeIcon.innerHTML = theme === 'dark' 
                ? '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>'
                : '<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>';
            const metaTheme = document.getElementById('metaThemeColor');
            if (metaTheme) {
                metaTheme.setAttribute('content', theme === 'dark' ? '#09090b' : '#fbfaf8');
            }
        }

        themeToggle.addEventListener('click', toggleTheme);
        initTheme();

        function initCurrentDateTracker() {
            try {
                const now = new Date();
                const y = now.getFullYear();
                const m = now.getMonth() + 1;
                const d = now.getDate();
                const todayIso = `${y}-${String(m).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
                
                const weekdayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
                const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
                const monthShortNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                
                const dayName = weekdayNames[now.getDay()];
                const monthName = monthNames[now.getMonth()];
                const monthShort = monthShortNames[now.getMonth()];
                
                const formattedDate = `${dayName}, ${d} ${monthName} ${y}`;
                
                const calDateTextEl = document.getElementById('calTodayDateText');
                if (calDateTextEl) {
                    calDateTextEl.textContent = `Current Date: ${formattedDate}`;
                }

                const heroBadge = document.getElementById('heroTodayBadge');
                if (heroBadge) {
                    heroBadge.textContent = `Today: ${d} ${monthShort} ${y}`;
                }

                // Month header badges
                const novBadge = document.getElementById('novTodayBadge');
                if (novBadge) {
                    if (y === 2026 && m === 11) {
                        novBadge.textContent = `Today: ${d} Nov`;
                        novBadge.style.display = 'inline-flex';
                    } else if (y === 2026 && m === 12) {
                        novBadge.style.display = 'none';
                    }
                }
                const decBadge = document.getElementById('decTodayBadge');
                if (decBadge) {
                    if (y === 2026 && m === 12) {
                        decBadge.textContent = `Today: ${d} Dec`;
                        decBadge.style.display = 'inline-flex';
                    } else {
                        decBadge.style.display = 'none';
                    }
                }

                // Mark current date in calendar if present in this session
                const matchingCell = document.querySelector(`.cal-cell[data-date="${todayIso}"]`);
                if (matchingCell) {
                    // Remove today from pre-rendered cells if different
                    document.querySelectorAll('.cal-cell.today').forEach(cell => {
                        if (cell !== matchingCell && !cell.classList.contains('exam-reg') && !cell.classList.contains('exam-old')) {
                            cell.classList.remove('today', 'current-date');
                            const tag = cell.querySelector('.cal-cell-tag');
                            if (tag && tag.textContent === 'Today') tag.remove();
                        }
                    });

                    matchingCell.classList.add('today', 'current-date');
                    matchingCell.setAttribute('title', `Today: ${d} ${monthShort} ${y} (Current Date)`);
                    if (!matchingCell.querySelector('.cal-cell-tag')) {
                        const tag = document.createElement('span');
                        tag.className = 'cal-cell-tag';
                        tag.textContent = 'Today';
                        matchingCell.appendChild(tag);
                    }
                }

                // Calculate countdown to next exam
                const countdownBox = document.getElementById('calTodayCountdownBox');
                if (countdownBox) {
                    const todayMid = new Date(y, now.getMonth(), d);
                    let nextExam = null;
                    let daysDiff = 9999;

                    for (const item of schedule) {
                        if (!item.isoDate) continue;
                        const examDate = new Date(item.isoDate + 'T00:00:00');
                        const diffTime = examDate.getTime() - todayMid.getTime();
                        const diffDays = Math.round(diffTime / (1000 * 60 * 60 * 24));
                        if (diffDays >= 0 && diffDays < daysDiff) {
                            daysDiff = diffDays;
                            nextExam = item;
                        }
                    }

                    if (nextExam) {
                        let diffText = '';
                        if (daysDiff === 0) {
                            diffText = '<span style="color: var(--pastel-sky-foreground); font-weight: 700;">Today!</span>';
                        } else if (daysDiff === 1) {
                            diffText = '<span style="color: var(--pastel-sky-foreground); font-weight: 700;">Tomorrow!</span>';
                        } else {
                            diffText = `in ${daysDiff} days`;
                        }

                        countdownBox.innerHTML = `
                            <span>Upcoming:</span>
                            <span class="cal-today-countdown">
                                <strong style="color: ${nextExam.isOld ? 'var(--pastel-peach-foreground)' : 'var(--pastel-sage-foreground)'};">${nextExam.date.split(' ').slice(0, 2).join(' ')} (${nextExam.code.replace('CE ', '')})</strong> &bull; ${diffText}
                            </span>
                        `;
                    } else {
                        countdownBox.innerHTML = `
                            <span class="cal-today-countdown" style="color: var(--muted-foreground);">All examinations concluded</span>
                        `;
                    }
                }
            } catch (err) {
                console.warn('Current date tracker initialized with static fallback:', err);
            }
        }

        initCurrentDateTracker();

        function setFilter(filter) {
            activeFilter = filter;
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.classList.toggle('active', b.getAttribute('data-filter') === filter);
            });
            render();
        }

        function toggleDateSort() {
            sortAscending = !sortAscending;
            document.getElementById('sortDirectionLabel').textContent = sortAscending ? 'Sort Date: Ascending ▲' : 'Sort Date: Descending ▼';
            document.getElementById('thSortIcon').textContent = sortAscending ? '▲' : '▼';
            render();
        }

        function showView(view) {
            document.getElementById('calendar-view').style.display = view === 'calendar' ? 'block' : 'none';
            document.getElementById('table-view').style.display = view === 'table' ? 'block' : 'none';
            document.getElementById('timeline-view').style.display = view === 'timeline' ? 'flex' : 'none';

            document.getElementById('btnCalendar').classList.toggle('active', view === 'calendar');
            document.getElementById('btnTable').classList.toggle('active', view === 'table');
            document.getElementById('btnTimeline').classList.toggle('active', view === 'timeline');
        }

        function render() {
            let filtered = schedule.filter(item => {
                if (activeFilter === 'regular') return !item.isOld;
                if (activeFilter === 'old') return item.isOld;
                return true;
            });

            // Sort by Date
            filtered.sort((a, b) => {
                return sortAscending ? (a.order - b.order) : (b.order - a.order);
            });

            // Table
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = filtered.map(item => `
                <tr>
                    <td>
                        <strong>${item.date}</strong>
                    </td>
                    <td style="font-size: 13px; color: var(--muted-foreground);">${item.day}</td>
                    <td><span class="code-tag">${item.code}</span></td>
                    <td>
                        <strong>${item.subject}</strong>
                    </td>
                    <td>
                        <span class="badge ${item.isOld ? 'badge-peach' : 'badge-sage'}">
                            ${item.tag}
                        </span>
                    </td>
                    <td style="font-size: 13px; font-weight: 500;">${item.gap}</td>
                    <td>
                        ${item.link ? `<a href="${item.link}" style="color: var(--pastel-sky-foreground); font-weight: 600; font-size: 12px;">PYQs →</a>` : '<span style="color: var(--muted-foreground); font-size: 12px;">—</span>'}
                    </td>
                </tr>
            `).join('');

            // Timeline
            const tline = document.getElementById('timeline-view');
            tline.innerHTML = filtered.map(item => `
                <div class="timeline-card ${item.isOld ? 'old' : 'regular'}">
                    <div style="min-width: 110px;">
                        <div style="font-size: 16px; font-weight: 700;">${item.date}</div>
                        <div style="font-size: 11px; color: var(--muted-foreground);">${item.day}</div>
                    </div>
                    <div style="flex: 1;">
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 2px;">
                            <span class="code-tag">${item.code}</span>
                            <span class="badge ${item.isOld ? 'badge-peach' : 'badge-sage'}">${item.tag}</span>
                        </div>
                        <div style="font-size: 14px; font-weight: 600;">${item.subject}</div>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-size: 12px; font-weight: 600; background: var(--muted); padding: 4px 10px; border-radius: var(--radius-full);">${item.gap}</span>
                    </div>
                </div>
            `).join('');
        }

        // Scroll to Top
        window.scrollToTop = function() {
            try {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            } catch(e) {
                window.scrollTo(0, 0);
            }
            try {
                document.documentElement.scrollTo({ top: 0, behavior: 'smooth' });
                document.body.scrollTo({ top: 0, behavior: 'smooth' });
            } catch(e) {}
            const header = document.querySelector('.header');
            if (header) header.classList.remove('header-hidden');
        };

        // Auto-hide navbar on scroll down, reveal on upscroll
        (function() {
            const header = document.querySelector('.header');
            if (!header) return;

            let lastScrollY = Math.max(0, window.pageYOffset || document.documentElement.scrollTop || 0);
            let ticking = false;
            const scrollThreshold = 8;
            const topThreshold = 56;

            function updateNavbar() {
                const currentScrollY = Math.max(0, window.pageYOffset || document.documentElement.scrollTop || 0);
                const maxScrollY = (document.documentElement.scrollHeight || document.body.scrollHeight) - window.innerHeight;
                const scrollDelta = currentScrollY - lastScrollY;

                if (currentScrollY <= topThreshold) {
                    header.classList.remove('header-hidden');
                } else if (currentScrollY >= maxScrollY - 20) {
                    // bottom bounce
                } else if (Math.abs(scrollDelta) >= scrollThreshold) {
                    if (scrollDelta > 0) {
                        header.classList.add('header-hidden');
                    } else {
                        header.classList.remove('header-hidden');
                    }
                }

                lastScrollY = currentScrollY;
                ticking = false;
            }

            window.addEventListener('scroll', function() {
                if (!ticking) {
                    window.requestAnimationFrame(updateNavbar);
                    ticking = true;
                }
            }, { passive: true });
        })();

        render();
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
        <a href="index.html#questions" class="mobile-nav-item" aria-label="Question Bank">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 14 14"></polyline>
            </svg>
            <span class="mobile-nav-label">Questions</span>
        </a>
        <a href="index.html#syllabus" class="mobile-nav-item" aria-label="PYQ Checklist">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <polyline points="9 11 12 14 22 4"></polyline>
                <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>
            </svg>
            <span class="mobile-nav-label">Checklist</span>
        </a>
        <a href="index.html#formulas" class="mobile-nav-item" aria-label="Formulas">
            <svg class="mobile-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <polyline points="4 7 4 4 20 4 20 7"></polyline>
                <line x1="9" y1="20" x2="15" y2="20"></line>
                <line x1="12" y1="4" x2="12" y2="20"></line>
            </svg>
            <span class="mobile-nav-label">Formulas</span>
        </a>
        <a href="timetable.html" class="mobile-nav-item active" aria-label="Exam Timetable">
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
    return html

if __name__ == "__main__":
    content = generate_timetable_html()
    with open("timetable.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully generated timetable.html with separated calendars and revised PDF dates!")
