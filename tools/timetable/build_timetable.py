#!/usr/bin/env python3
"""
Civil Engineering Examination Timetable Generator & Modular Component Provider.
Produces timetable.html and exposes modular components for index.html:
- get_timetable_styles()
- get_timetable_html_view()
- get_timetable_modal_html()
- get_timetable_script()
- generate_timetable_html()
"""
import sys
from pathlib import Path

# Ensure repo root is in sys.path
_repo_root = Path(__file__).resolve().parent.parent.parent
if str(_repo_root) not in sys.path:
    sys.path.insert(0, str(_repo_root))

_TIMETABLE_STYLES = """        /* ----------------------------------------------------
           TIMETABLE THEME TOKENS
           ---------------------------------------------------- */
        :root {
            --pastel-sage-count-bg: rgba(32, 92, 54, 0.12);
            --pastel-peach-count-bg: rgba(154, 67, 24, 0.12);
            --pastel-done-bg: #edf7ee;
            --pastel-done-foreground: #205c36;
            --pastel-done-muted: #f4faf5;
            --pastel-done-count-bg: rgba(32, 92, 54, 0.14);
        }

        [data-theme="dark"] {
            --pastel-sage-count-bg: rgba(52, 211, 153, 0.22);
            --pastel-peach-count-bg: rgba(251, 146, 60, 0.22);
            --pastel-done-bg: rgba(52, 211, 153, 0.14);
            --pastel-done-foreground: #6ee7b7;
            --pastel-done-muted: rgba(52, 211, 153, 0.08);
            --pastel-done-count-bg: rgba(52, 211, 153, 0.22);
        }

/* ----------------------------------------------------
           SUPER MINIMAL HEADER ROW (ZERO BORDERS)
           ---------------------------------------------------- */
        .timetable-header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 24px 0 14px 0;
            border: none;
            flex-wrap: wrap;
        }

        .timetable-header-left {
            display: flex;
            flex-direction: column;
            gap: 3px;
        }

        .timetable-title {
            font-size: var(--font-size-h2);
            line-height: var(--line-height-h2);
            font-weight: 700;
            letter-spacing: -0.02em;
            color: var(--foreground);
            margin: 0;
        }

        .timetable-subtitle {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: var(--font-size-body-small);
            color: var(--muted-foreground);
            flex-wrap: wrap;
        }

        .timetable-subtitle .sep {
            opacity: 0.4;
        }

        .timetable-subtle-badge {
            background: var(--secondary);
            color: var(--muted-foreground);
            padding: 1px 6px;
            border-radius: var(--radius-sm);
            font-size: 11px;
            font-weight: 600;
            border: none;
        }

        /* Sleek Live Status Pill (Zero Borders) */
        .live-status-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: var(--secondary);
            padding: 6px 14px;
            border-radius: var(--radius-full);
            font-size: var(--font-size-body-small);
            font-weight: 500;
            color: var(--foreground);
            border: none;
        }

        .status-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #38bdf8;
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
            flex-shrink: 0;
        }

        .status-dot.all-done {
            background: #22c55e;
            box-shadow: 0 0 0 2px rgba(34, 197, 94, 0.25);
        }

        /* ----------------------------------------------------
           DIRECTLY COLORED FILTERS (ZERO BORDERS, NO SEPARATE LEGEND)
           ---------------------------------------------------- */
        .controls-bar-minimal {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding: 8px 0 20px 0;
            border: none;
            flex-wrap: wrap;
        }

        .filter-tabs-minimal {
            position: relative;
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .filter-tabs-minimal .layout-pill-indicator {
            position: absolute;
            top: 0;
            left: 0;
            pointer-events: none;
            z-index: 1;
            background-color: var(--foreground);
            border-radius: var(--radius-full);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
            transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        width 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        height 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        background-color 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        opacity 0.2s ease;
            will-change: transform, width, height, background-color;
        }

        [data-theme="dark"] .filter-tabs-minimal .layout-pill-indicator {
            background-color: #27272a;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.45);
        }

        .tab-pill {
            position: relative;
            z-index: 2;
            border: none !important;
            font-size: var(--font-size-button);
            font-weight: 600;
            padding: 6px 13px;
            border-radius: var(--radius-full);
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            transition: color 0.18s ease, transform 0.1s ease;
            user-select: none;
        }

        .tab-pill:active {
            transform: scale(0.96);
        }

        .tab-pill.active {
            background-color: transparent !important;
            box-shadow: none !important;
        }

        .pill-count {
            font-size: 11px;
            padding: 1px 6px;
            border-radius: var(--radius-full);
            font-variant-numeric: tabular-nums;
            font-weight: 700;
            border: none;
        }

        /* 1. All Filter (Neutral) */
        .tab-pill-all {
            background-color: var(--secondary);
            color: var(--foreground);
        }
        .tab-pill-all .pill-count {
            background-color: var(--card);
            color: var(--foreground);
        }
        .tab-pill-all.active {
            background-color: var(--foreground);
            color: var(--background);
        }
        .tab-pill-all.active .pill-count {
            background-color: rgba(255, 255, 255, 0.2);
            color: var(--background);
        }
        [data-theme="dark"] .tab-pill-all.active .pill-count {
            background-color: rgba(0, 0, 0, 0.3);
            color: var(--background);
        }

        /* 2. Regular Filter (Sage Green Directly on Filter) */
        .tab-pill-regular {
            background-color: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
        }
        .tab-pill-regular .pill-count {
            background-color: var(--pastel-sage-count-bg);
            color: var(--pastel-sage-foreground);
        }
        .tab-pill-regular.active {
            background-color: #205c36;
            color: #ffffff;
        }
        [data-theme="dark"] .tab-pill-regular.active {
            background-color: #059669;
            color: #ffffff;
        }
        .tab-pill-regular.active .pill-count {
            background-color: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }

        /* 3. Backlog Filter (Peach / Orange Directly on Filter) */
        .tab-pill-old {
            background-color: var(--pastel-peach-bg);
            color: var(--pastel-peach-foreground);
        }
        .tab-pill-old .pill-count {
            background-color: var(--pastel-peach-count-bg);
            color: var(--pastel-peach-foreground);
        }
        .tab-pill-old.active {
            background-color: #9a4318;
            color: #ffffff;
        }
        [data-theme="dark"] .tab-pill-old.active {
            background-color: #ea580c;
            color: #ffffff;
        }
        .tab-pill-old.active .pill-count {
            background-color: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }

        /* 4. Done Filter (Muted Green Directly on Filter) */
        .tab-pill-done {
            background-color: var(--pastel-done-bg);
            color: var(--pastel-done-foreground);
        }
        .tab-pill-done .pill-count {
            background-color: var(--pastel-done-count-bg);
            color: var(--pastel-done-foreground);
        }
        .tab-pill-done.active {
            background-color: var(--pastel-done-foreground);
            color: #ffffff;
        }
        .tab-pill-done.active .pill-count {
            background-color: rgba(255, 255, 255, 0.25);
            color: #ffffff;
        }

        /* Controls Actions (Zero Borders) */
        .controls-right-minimal {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .btn-subtle-action {
            background: var(--secondary);
            color: var(--foreground);
            font-size: var(--font-size-button);
            font-weight: 500;
            padding: 6px 12px;
            border-radius: var(--radius-full);
            cursor: pointer;
            border: none;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.15s ease;
        }

        .btn-subtle-action:hover {
            background: var(--secondary-hover);
        }

        .view-switchers-minimal {
            position: relative;
            display: flex;
            background: var(--secondary);
            padding: 3px;
            border-radius: var(--radius-full);
            border: none;
        }

        .view-switchers-minimal .layout-pill-indicator {
            position: absolute;
            top: 0;
            left: 0;
            pointer-events: none;
            z-index: 1;
            background: var(--card);
            border-radius: var(--radius-full);
            box-shadow: var(--shadow-sm);
            transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        width 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        height 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        opacity 0.2s ease;
            will-change: transform, width, height;
        }

        [data-theme="dark"] .view-switchers-minimal .layout-pill-indicator {
            background: #27272a;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.45);
        }

        .view-pill {
            position: relative;
            z-index: 2;
            background: transparent !important;
            box-shadow: none !important;
            border: none;
            color: var(--muted-foreground);
            font-size: var(--font-size-body-small);
            font-weight: 500;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: color 0.18s ease, transform 0.1s ease;
        }

        .view-pill:hover:not(.active) {
            color: var(--foreground);
        }

        .view-pill:active {
            transform: scale(0.96);
        }

        .view-pill.active {
            background: transparent !important;
            box-shadow: none !important;
            color: var(--foreground) !important;
            font-weight: 600;
        }

        #calendar-view, #table-view, #timeline-view {
            animation: timetableViewEnter 0.26s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        @keyframes timetableViewEnter {
            0% {
                opacity: 0;
                transform: translateY(6px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* ----------------------------------------------------
           DYNAMIC SEPARATED CALENDARS (ZERO BORDERS)
           ---------------------------------------------------- */
        .cal-separated-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
            border: none;
        }

        .cal-box {
            background: var(--card);
            border-radius: var(--radius-md);
            padding: 18px;
            border: none;
            box-shadow: var(--shadow-sm);
        }

        .cal-box-header {
            font-size: var(--font-size-h6);
            font-weight: 600;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: none;
        }

        .cal-grid-vertical {
            display: grid;
            gap: 4px;
            align-items: center;
            border: none;
        }

        .cal-col-label {
            font-size: var(--font-size-overline);
            font-weight: 600;
            color: var(--muted-foreground);
            text-align: center;
            padding: 4px 0;
            text-transform: uppercase;
            border: none;
        }

        .cal-row-label {
            font-size: var(--font-size-body-small);
            font-weight: 700;
            color: var(--muted-foreground);
            text-align: left;
            padding: 6px 2px;
            border: none;
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
            background: var(--background);
            border: none !important;
            text-align: center;
            padding: 2px;
            position: relative;
            transition: transform 0.1s ease;
        }

        .cal-cell:hover:not(.empty) {
            background: var(--secondary-hover);
        }

        .cal-cell.empty {
            background: transparent;
            color: transparent;
            pointer-events: none;
            border: none !important;
        }

        .cal-cell.exam-reg {
            background: var(--pastel-sage-bg) !important;
            color: var(--pastel-sage-foreground) !important;
            font-weight: 700;
            cursor: pointer;
            border: none !important;
        }

        .cal-cell.exam-old {
            background: var(--pastel-peach-bg) !important;
            color: var(--pastel-peach-foreground) !important;
            font-weight: 700;
            cursor: pointer;
            border: none !important;
        }

        /* Done Paper Cell Style: Muted Green "Yes, this is done" (Zero Borders) */
        .cal-cell.exam-done {
            background: var(--pastel-done-bg) !important;
            color: var(--pastel-done-foreground) !important;
            font-weight: 700;
            position: relative;
            cursor: pointer;
            border: none !important;
        }

        .cal-cell.today,
        .cal-cell.current-date {
            background: var(--pastel-sky-bg) !important;
            color: var(--pastel-sky-foreground) !important;
            font-weight: 700;
            position: relative;
            cursor: pointer;
            border: none !important;
        }

        .cal-cell.today.exam-done,
        .cal-cell.current-date.exam-done {
            background: var(--pastel-done-bg) !important;
            color: var(--pastel-done-foreground) !important;
            border: none !important;
        }

        .cal-cell.today.exam-reg,
        .cal-cell.current-date.exam-reg {
            background: var(--pastel-sage-bg) !important;
            color: var(--pastel-sage-foreground) !important;
            border: none !important;
        }

        .cal-cell.today.exam-old,
        .cal-cell.current-date.exam-old {
            background: var(--pastel-peach-bg) !important;
            color: var(--pastel-peach-foreground) !important;
            border: none !important;
        }

        .cal-cell-tag {
            font-size: 10px;
            line-height: 12px;
            margin-top: 1px;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 100%;
            border: none;
        }

        .cal-cell-tag.cal-cell-tag-done {
            background: var(--pastel-done-count-bg);
            color: var(--pastel-done-foreground);
            padding: 1px 4px;
            border-radius: var(--radius-sm);
            font-size: 9px;
            font-weight: 700;
            border: none;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            font-size: var(--font-size-body-small);
            font-weight: 600;
            padding: 2px 8px;
            border-radius: var(--radius-full);
            text-decoration: none;
            gap: 4px;
            border: none !important;
        }

        .badge-sage {
            background: var(--pastel-sage-bg);
            color: var(--pastel-sage-foreground);
        }

        .badge-peach {
            background: var(--pastel-peach-bg);
            color: var(--pastel-peach-foreground);
        }

        .badge-sky {
            background: var(--pastel-sky-bg);
            color: var(--pastel-sky-foreground);
        }

        .badge-done {
            background: var(--pastel-done-bg);
            color: var(--pastel-done-foreground);
            font-weight: 600;
        }

        .badge-subtle {
            background: var(--secondary);
            color: var(--muted-foreground);
        }

        /* ----------------------------------------------------
           TABLE VIEW (ZERO BORDERS • PURE BG SEPARATION)
           ---------------------------------------------------- */
        .table-wrap {
            background: var(--card);
            border-radius: var(--radius-md);
            overflow-x: auto;
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
            border: none;
        }

        .table-wrap table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: var(--font-size-body-medium);
            border: none;
        }

        .table-wrap th {
            background: var(--secondary);
            color: var(--muted-foreground);
            font-size: var(--font-size-overline);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 10px 14px;
            cursor: pointer;
            user-select: none;
            border: none;
        }

        .table-wrap th:hover {
            color: var(--foreground);
        }

        .table-wrap td {
            padding: 11px 14px;
            vertical-align: middle;
            border: none;
        }

        .table-wrap tr:nth-child(even) td {
            background: rgba(0, 0, 0, 0.015);
        }

        [data-theme="dark"] .table-wrap tr:nth-child(even) td {
            background: rgba(255, 255, 255, 0.015);
        }

        .table-wrap tr:hover td {
            background: var(--secondary);
        }

        .table-wrap tr.row-done td {
            background: var(--pastel-done-muted) !important;
        }

        .code-tag {
            font-family: var(--font-mono);
            font-size: var(--font-size-body-small);
            background: var(--secondary);
            padding: 2px 6px;
            border-radius: var(--radius-sm);
            font-weight: 600;
            border: none;
        }

        .status-btn {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            font-size: 11.5px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: var(--radius-full);
            cursor: pointer;
            border: none;
            background: var(--secondary);
            color: var(--muted-foreground);
            transition: all 0.15s ease;
        }

        .status-btn:hover {
            background: var(--secondary-hover);
            color: var(--foreground);
        }

        .status-btn-done {
            background: var(--pastel-done-bg);
            color: var(--pastel-done-foreground);
        }

        .status-btn-done:hover {
            background: var(--pastel-done-count-bg);
        }

        .btn-icon-action {
            background: transparent;
            border: none;
            color: var(--muted-foreground);
            width: 28px;
            height: 28px;
            border-radius: var(--radius-sm);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .btn-icon-action:hover {
            background: var(--secondary);
            color: var(--foreground);
        }

        .btn-icon-danger:hover {
            background: rgba(239, 68, 68, 0.12);
            color: #ef4444;
        }

        /* ----------------------------------------------------
           TIMELINE VIEW (ZERO BORDERS)
           ---------------------------------------------------- */
        .timeline-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 24px;
            border: none;
        }

        .timeline-card {
            background: var(--card);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
            border: none;
            box-shadow: var(--shadow-sm);
        }

        .timeline-card.regular {
            background: var(--pastel-sage-bg);
        }

        .timeline-card.old {
            background: var(--pastel-peach-bg);
        }

        .timeline-card.done {
            background: var(--pastel-done-muted);
        }

        /* ----------------------------------------------------
           CUSTOMIZE TIMETABLE MODAL (ZERO BORDERS)
           ---------------------------------------------------- */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            z-index: 100000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
            box-sizing: border-box;
            border: none;
        }

        .modal-card {
            background: var(--card);
            border-radius: var(--radius-md);
            max-width: 640px;
            width: 100%;
            max-height: 88vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
            overflow: hidden;
            border: none;
            animation: modalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes modalFadeIn {
            from { opacity: 0; transform: scale(0.96) translateY(8px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .modal-header {
            padding: 18px 22px;
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
            border: none;
        }

        .modal-title {
            font-size: 17px;
            font-weight: 700;
            line-height: 22px;
            color: var(--foreground);
        }

        .modal-subtitle {
            font-size: 12px;
            color: var(--muted-foreground);
            margin-top: 2px;
        }

        .modal-close-btn {
            background: transparent;
            border: none;
            color: var(--muted-foreground);
            font-size: 18px;
            cursor: pointer;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: var(--radius-sm);
        }

        .modal-close-btn:hover {
            background: var(--secondary);
            color: var(--foreground);
        }

        .modal-body {
            padding: 0 22px 18px;
            overflow-y: auto;
            flex: 1;
            border: none;
        }

        .exam-form {
            background: var(--secondary);
            border-radius: var(--radius-sm);
            padding: 14px;
            margin-bottom: 16px;
            border: none;
        }

        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        .form-group-span2 {
            grid-column: span 2;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .form-label {
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
        }

        .form-input, .form-select {
            background: var(--card);
            color: var(--foreground);
            font-size: var(--font-size-body-medium);
            font-family: var(--font-sans);
            padding: 7px 10px;
            border-radius: var(--radius-sm);
            border: none;
            outline: none;
        }

        .form-input:focus, .form-select:focus {
            box-shadow: 0 0 0 2px var(--foreground);
        }

        .form-checkbox-group {
            display: flex;
            align-items: center;
            padding-top: 4px;
        }

        .checkbox-label {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            color: var(--foreground);
        }

        .form-actions {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 12px;
        }

        .btn-primary {
            background: var(--primary);
            color: var(--primary-foreground);
            border: none;
            padding: 6px 14px;
            border-radius: var(--radius-sm);
            font-size: var(--font-size-button);
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-primary:hover {
            opacity: 0.9;
        }

        .btn-secondary {
            background: var(--card);
            color: var(--foreground);
            border: none;
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            font-size: var(--font-size-button);
            font-weight: 500;
            cursor: pointer;
        }

        .btn-secondary:hover {
            background: var(--secondary-hover);
        }

        .modal-section-divider {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--muted-foreground);
            margin: 16px 0 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .modal-section-divider::after {
            content: '';
            flex: 1;
            height: 2px;
            background: var(--secondary);
            border-radius: var(--radius-full);
        }

        .modal-subject-list {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 16px;
            border: none;
        }

        .modal-subject-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding: 8px 12px;
            background: var(--secondary);
            border-radius: var(--radius-sm);
            border: none;
        }

        .modal-subject-item.is-done {
            background: var(--pastel-done-muted);
        }

        .modal-presets {
            background: var(--secondary);
            border-radius: var(--radius-sm);
            padding: 10px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
            border: none;
        }

        .preset-label {
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: var(--muted-foreground);
        }

        .preset-buttons {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .btn-preset {
            background: var(--card);
            color: var(--foreground);
            font-size: 11px;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: var(--radius-sm);
            cursor: pointer;
            border: none;
        }

        .btn-preset:hover {
            background: var(--secondary-hover);
        }

        .btn-preset-danger {
            color: #ef4444;
        }

        .btn-preset-danger:hover {
            background: rgba(239, 68, 68, 0.1);
        }

        .modal-footer {
            padding: 14px 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            background: var(--secondary);
            border: none;
        }

        .storage-notice {
            font-size: 12px;
            color: var(--muted-foreground);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        
        @media (max-width: 768px) {
            .timetable-header-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
                padding: 16px 0 10px 0;
            }
            .timetable-title {
                font-size: 20px !important;
                line-height: 26px !important;
            }
            .controls-bar-minimal {
                flex-direction: column;
                align-items: stretch;
                gap: 10px;
            }
            .filter-tabs-minimal {
                width: 100%;
                justify-content: flex-start;
                overflow-x: auto;
                padding-bottom: 2px;
            }
            .controls-right-minimal {
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
            .form-grid {
                grid-template-columns: 1fr;
            }
            .form-group-span2 {
                grid-column: span 1;
            }
        }
"""

_TIMETABLE_HTML_VIEW = """<!-- Super Minimal Header Row -->
        <div class="timetable-header-row">
            <div class="timetable-header-left">
                <h1 class="timetable-title">Examination Timetable</h1>
                <div class="timetable-subtitle">
                    <span>Civil Engineering</span>
                    <span class="sep">&bull;</span>
                    <span>Nov – Dec 2026</span>
                    <span class="sep">&bull;</span>
                    <span>2:00 – 5:00 PM</span>
                    <span class="sep">&bull;</span>
                    <span class="timetable-subtle-badge">SGSITS Indore</span>
                </div>
            </div>
            <div class="timetable-header-right">
                <div class="live-status-pill" id="liveStatusPill">
                    <span class="status-dot"></span>
                    <span id="liveStatusText">Loading upcoming exam...</span>
                </div>
            </div>
        </div>

        <!-- Super Minimal Controls & Directly Colored Filter Badges -->
        <div class="controls-bar-minimal">
            <div class="filter-tabs-minimal">
                <button class="tab-pill tab-pill-all active" data-filter="all" onclick="setFilter('all')">
                    All <span class="pill-count" id="filterCountAll">0</span>
                </button>
                <button class="tab-pill tab-pill-regular" data-filter="regular" onclick="setFilter('regular')">
                    Regular <span class="pill-count" id="filterCountReg">0</span>
                </button>
                <button class="tab-pill tab-pill-old" data-filter="old" onclick="setFilter('old')">
                    Backlog <span class="pill-count" id="filterCountOld">0</span>
                </button>
                <button class="tab-pill tab-pill-done" data-filter="done" onclick="setFilter('done')">
                    Done <span class="pill-count" id="filterCountDone">0</span>
                </button>
            </div>

            <div class="controls-right-minimal">
                <button class="btn-subtle-action" onclick="openEditModal()" title="Customize timetable">
                    <i class="icon hgi-stroke hgi-pencil-edit-02"></i>
                    <span>Edit</span>
                </button>

                <div class="view-switchers-minimal">
                    <button class="view-pill active" id="btnCalendar" onclick="showView('calendar')" title="Monthly calendars">Calendar</button>
                    <button class="view-pill" id="btnTable" onclick="showView('table')" title="Table view">Table</button>
                    <button class="view-pill" id="btnTimeline" onclick="showView('timeline')" title="Timeline view">Timeline</button>
                </div>
            </div>
        </div>

        <!-- VIEW 1: SEPARATED CALENDARS -->
        <section id="calendar-view">
            <div class="cal-separated-container" id="calSeparatedContainer"></div>
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
                        <th>Status</th>
                        <th>Prep Gap</th>
                        <th style="text-align: right;">Action</th>
                    </tr>
                </thead>
                <tbody id="tableBody"></tbody>
            </table>
        </section>

        <!-- VIEW 3: TIMELINE -->
        <section id="timeline-view" class="timeline-list" style="display: none;"></section>"""

_TIMETABLE_MODAL_HTML = """<!-- CUSTOMIZE TIMETABLE MODAL (ZERO BORDERS) -->
    <div id="editModal" class="modal-overlay" style="display: none;" onclick="handleModalOverlayClick(event)">
        <div class="modal-card" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
            <div class="modal-header">
                <div>
                    <h3 id="modalTitle" class="modal-title">Customize Exam Timetable</h3>
                    <p class="modal-subtitle">Saved privately to your browser's localStorage. Adjust dates, add papers, or mark exams done.</p>
                </div>
                <button class="modal-close-btn" onclick="closeEditModal()" aria-label="Close modal">✕</button>
            </div>

            <div class="modal-body">
                <!-- Add / Edit Form -->
                <form id="examForm" onsubmit="handleFormSubmit(event)" class="exam-form">
                    <input type="hidden" id="formExamId" value="">
                    <div class="form-grid">
                        <div class="form-group form-group-span2">
                            <label class="form-label" for="formSubject">Subject Name *</label>
                            <input type="text" id="formSubject" class="form-input" placeholder="e.g. Geotechnical Engineering - II" required>
                        </div>

                        <div class="form-group">
                            <label class="form-label" for="formCode">Subject Code</label>
                            <input type="text" id="formCode" class="form-input" placeholder="e.g. CE 41007">
                        </div>

                        <div class="form-group">
                            <label class="form-label" for="formShortTag">Calendar Tag *</label>
                            <input type="text" id="formShortTag" class="form-input" placeholder="e.g. Geo-2 (max 7 chars)" maxlength="8" required>
                        </div>

                        <div class="form-group">
                            <label class="form-label" for="formDate">Exam Date *</label>
                            <input type="date" id="formDate" class="form-input" required>
                        </div>

                        <div class="form-group">
                            <label class="form-label" for="formCategory">Category</label>
                            <select id="formCategory" class="form-select">
                                <option value="Regular">Regular (Normal Syllabus - Sage Green)</option>
                                <option value="Old Syllabus">Old Syllabus (Backlog - Peach)</option>
                            </select>
                        </div>

                        <div class="form-group form-group-span2">
                            <label class="form-label" for="formLink">PYQ Question Bank Link (Optional)</label>
                            <input type="text" id="formLink" class="form-input" placeholder="e.g. index.html or leave empty">
                        </div>

                        <div class="form-group form-group-span2 form-checkbox-group">
                            <label class="checkbox-label">
                                <input type="checkbox" id="formCompleted">
                                <span>Mark paper as concluded / completed (Muted Green ✓)</span>
                            </label>
                        </div>
                    </div>"""

_TIMETABLE_SCRIPT = """// Default 3 regular subjects (Normal Syllabus) for public repo
        const DEFAULT_SCHEDULE = [
            {
                id: 1,
                date: "18 Nov 2026",
                isoDate: "2026-11-18",
                day: "Wednesday",
                order: 18,
                code: "CE 41007",
                subject: "Geotechnical Engineering - II (Geo - 2)",
                shortTag: "Geo-2",
                tag: "Regular",
                isOld: false,
                gap: "First Exam",
                link: "index.html",
                completed: false
            },
            {
                id: 5,
                date: "09 Dec 2026",
                isoDate: "2026-12-09",
                day: "Wednesday",
                order: 39,
                code: "CE 41001",
                subject: "Design of Reinforced Concrete Structures (RCC)",
                shortTag: "RCC",
                tag: "Regular",
                isOld: false,
                gap: "4 Days Gap",
                link: null,
                completed: false
            },
            {
                id: 7,
                date: "12 Dec 2026",
                isoDate: "2026-12-12",
                day: "Saturday",
                order: 42,
                code: "CE 41006",
                subject: "Design of Hydraulic Structures (DHS)",
                shortTag: "DHS",
                tag: "Regular",
                isOld: false,
                gap: "1 Day Gap",
                link: null,
                completed: false
            }
        ];

        // Full SGSITS Timetable (Preserves author's 4 old syllabus backlog papers + 3 regular papers)
        const FULL_BACKLOG_SCHEDULE = [
            {
                id: 1,
                date: "18 Nov 2026",
                isoDate: "2026-11-18",
                day: "Wednesday",
                order: 18,
                code: "CE 41007",
                subject: "Geotechnical Engineering - II (Geo - 2)",
                shortTag: "Geo-2",
                tag: "Regular",
                isOld: false,
                gap: "First Exam",
                link: "index.html",
                completed: false
            },
            {
                id: 2,
                date: "26 Nov 2026",
                isoDate: "2026-11-26",
                day: "Thursday",
                order: 26,
                code: "CE 31505",
                subject: "Structural Analysis - II (SA-2)",
                shortTag: "SA-2",
                tag: "Old Syllabus",
                isOld: true,
                gap: "8 Days Gap",
                link: null,
                completed: false
            },
            {
                id: 3,
                date: "30 Nov 2026",
                isoDate: "2026-11-30",
                day: "Monday",
                order: 30,
                code: "CE 31007",
                subject: "Structural Analysis - I (SA-I)",
                shortTag: "SA-I",
                tag: "Old Syllabus",
                isOld: true,
                gap: "4 Days Gap",
                link: null,
                completed: false
            },
            {
                id: 4,
                date: "05 Dec 2026",
                isoDate: "2026-12-05",
                day: "Saturday",
                order: 35,
                code: "CE 31517",
                subject: "Geotechnical Engineering - I (Geo I)",
                shortTag: "Geo I",
                tag: "Old Syllabus",
                isOld: true,
                gap: "5 Days Gap",
                link: null,
                completed: false
            },
            {
                id: 5,
                date: "09 Dec 2026",
                isoDate: "2026-12-09",
                day: "Wednesday",
                order: 39,
                code: "CE 41001",
                subject: "Design of Reinforced Concrete Structures (RCC)",
                shortTag: "RCC",
                tag: "Regular",
                isOld: false,
                gap: "4 Days Gap",
                link: null,
                completed: false
            },
            {
                id: 6,
                date: "11 Dec 2026",
                isoDate: "2026-12-11",
                day: "Friday",
                order: 41,
                code: "CE 31713",
                subject: "Water Resources Engineering (Water)",
                shortTag: "Water",
                tag: "Old Syllabus",
                isOld: true,
                gap: "2 Days Gap",
                link: null,
                completed: false
            },
            {
                id: 7,
                date: "12 Dec 2026",
                isoDate: "2026-12-12",
                day: "Saturday",
                order: 42,
                code: "CE 41006",
                subject: "Design of Hydraulic Structures (DHS)",
                shortTag: "DHS",
                tag: "Regular",
                isOld: false,
                gap: "1 Day Gap",
                link: null,
                completed: false
            }
        ];

        const STORAGE_KEY = 'civil_exam_timetable_custom_v1';

        function isLocalEnvironment() {
            try {
                const p = window.location.protocol;
                const h = window.location.hostname;
                return p === 'file:' || h === 'localhost' || h === '127.0.0.1' || h === '' || h.startsWith('192.168.');
            } catch(e) {
                return false;
            }
        }

        function loadSchedule() {
            try {
                const saved = localStorage.getItem(STORAGE_KEY);
                if (saved) {
                    const parsed = JSON.parse(saved);
                    if (Array.isArray(parsed) && parsed.length > 0) {
                        return recalculateGaps(parsed);
                    }
                }
            } catch(e) {
                console.warn('Error reading from localStorage:', e);
            }

            // If running on local machine, preserve the author's 7 subjects (4 backlog + 3 regular)
            if (isLocalEnvironment()) {
                const fullList = JSON.parse(JSON.stringify(FULL_BACKLOG_SCHEDULE));
                saveSchedule(fullList);
                return recalculateGaps(fullList);
            }

            // Public default for everyone else:
            const def = JSON.parse(JSON.stringify(DEFAULT_SCHEDULE));
            saveSchedule(def);
            return recalculateGaps(def);
        }

        function saveSchedule(items) {
            try {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
            } catch(e) {
                console.error('Failed to save timetable to localStorage:', e);
            }
        }

        function recalculateGaps(items) {
            items.sort((a, b) => (a.isoDate || '').localeCompare(b.isoDate || ''));
            const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const baseDate = new Date('2026-11-01T00:00:00');

            for (let i = 0; i < items.length; i++) {
                const item = items[i];
                if (item.isoDate) {
                    const d = new Date(item.isoDate + 'T00:00:00');
                    if (!isNaN(d.getTime())) {
                        item.day = dayNames[d.getDay()];
                        item.date = `${String(d.getDate()).padStart(2, '0')} ${months[d.getMonth()]} ${d.getFullYear()}`;
                        item.order = Math.round((d.getTime() - baseDate.getTime()) / (1000 * 60 * 60 * 24)) + 1;
                    }
                }

                if (i === 0) {
                    item.gap = "First Exam";
                } else {
                    const prevD = new Date(items[i - 1].isoDate + 'T00:00:00');
                    const currD = new Date(item.isoDate + 'T00:00:00');
                    const diffDays = Math.round((currD.getTime() - prevD.getTime()) / (1000 * 60 * 60 * 24));
                    if (diffDays === 0) {
                        item.gap = "Same Day";
                    } else if (diffDays === 1) {
                        item.gap = "1 Day Gap";
                    } else {
                        item.gap = `${diffDays} Days Gap`;
                    }
                }
            }
            return items;
        }

        let schedule = loadSchedule();
        let activeFilter = 'all';
        let sortAscending = true;

        // Theme management (harmonized with index.html)
        const ttThemeToggle = document.getElementById('themeToggle');
        const ttThemeIcon = document.getElementById('themeIcon');

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
            if (!ttThemeIcon) return;
            ttThemeIcon.className = theme === 'dark' ? 'icon hgi-stroke hgi-sun-01' : 'icon hgi-stroke hgi-moon-02';
            ttThemeIcon.innerHTML = '';
            const metaTheme = document.getElementById('metaThemeColor');
            if (metaTheme) {
                metaTheme.setAttribute('content', theme === 'dark' ? '#09090b' : '#fbfaf8');
            }
        }

        if (!window.switchPageView) {
            if (ttThemeToggle) {
                ttThemeToggle.addEventListener('click', toggleTheme);
            }
            initTheme();
        }

        function initCurrentDateTracker() {
            try {
                const now = new Date();
                const y = now.getFullYear();
                const m = now.getMonth() + 1;
                const d = now.getDate();
                const todayMid = new Date(y, now.getMonth(), d);
                
                let nextExam = null;
                let daysDiff = 9999;

                for (const item of schedule) {
                    if (!item.isoDate || item.completed) continue;
                    const examDate = new Date(item.isoDate + 'T00:00:00');
                    const diffTime = examDate.getTime() - todayMid.getTime();
                    const diffDays = Math.round(diffTime / (1000 * 60 * 60 * 24));
                    if (diffDays >= 0 && diffDays < daysDiff) {
                        daysDiff = diffDays;
                        nextExam = item;
                    }
                }

                const liveText = document.getElementById('liveStatusText');
                const liveDot = document.querySelector('.live-status-pill .status-dot');

                if (liveText) {
                    if (nextExam) {
                        let diffText = '';
                        if (daysDiff === 0) {
                            diffText = '<span style="color: var(--pastel-sky-foreground); font-weight: 700;">Today!</span>';
                        } else if (daysDiff === 1) {
                            diffText = '<span style="color: var(--pastel-sky-foreground); font-weight: 700;">Tomorrow!</span>';
                        } else {
                            diffText = `in ${daysDiff} days`;
                        }

                        const codeDisplay = (nextExam.shortTag || nextExam.code.replace('CE ', ''));
                        liveText.innerHTML = `Next: <strong>${nextExam.date.split(' ').slice(0, 2).join(' ')}</strong> (${codeDisplay}) &bull; ${diffText}`;
                        if (liveDot) liveDot.className = 'status-dot';
                    } else {
                        const totalPapers = schedule.length;
                        const allDone = totalPapers > 0 && schedule.every(s => s.completed);
                        if (allDone) {
                            liveText.innerHTML = `<span style="color: var(--pastel-done-foreground); font-weight: 600;">✓ All examinations concluded</span>`;
                            if (liveDot) liveDot.className = 'status-dot all-done';
                        } else {
                            liveText.textContent = 'All scheduled papers concluded';
                            if (liveDot) liveDot.className = 'status-dot';
                        }
                    }
                }
            } catch (err) {
                console.warn('Current date tracker initialized with fallback:', err);
            }
        }

        /* ====================================================
           LAYOUT ID PILL ENGINE (APPLE / FRAMER-MOTION SMOOTH SLIDING PILLS)
           ==================================================== */
        if (!window.LayoutPillEngine) {
            const LayoutPillEngine = (function() {
            const SELECTORS = [
                '.filter-tabs-minimal',
                '.view-switchers-minimal',
                '.nav-links'
            ];

            function getContainers() {
                return document.querySelectorAll(SELECTORS.join(', '));
            }

            function updatePill(container, immediate = false) {
                if (!container || !container.isConnected) return;

                let indicator = container.querySelector(':scope > .layout-pill-indicator');
                if (!indicator) {
                    indicator = document.createElement('span');
                    indicator.className = 'layout-pill-indicator';
                    indicator.setAttribute('aria-hidden', 'true');
                    container.prepend(indicator);
                }

                const activeItem = container.querySelector(':scope > .active, :scope > * > .active, :scope > .tab-pill.active, :scope > .view-pill.active, :scope > .nav-link-btn.active');

                if (!activeItem || activeItem.offsetParent === null) {
                    indicator.style.opacity = '0';
                    return;
                }

                const cRect = container.getBoundingClientRect();
                const iRect = activeItem.getBoundingClientRect();

                const x = (iRect.left - cRect.left) + container.scrollLeft;
                const y = (iRect.top - cRect.top) + container.scrollTop;
                const w = iRect.width;
                const h = iRect.height;

                if (w === 0 || h === 0) {
                    indicator.style.opacity = '0';
                    return;
                }

                // Color-adaptive layout pill for filter-tabs-minimal
                if (container.classList.contains('filter-tabs-minimal')) {
                    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
                    if (activeItem.classList.contains('tab-pill-regular')) {
                        indicator.style.backgroundColor = isDark ? '#059669' : '#205c36';
                    } else if (activeItem.classList.contains('tab-pill-old')) {
                        indicator.style.backgroundColor = isDark ? '#ea580c' : '#9a4318';
                    } else if (activeItem.classList.contains('tab-pill-done')) {
                        indicator.style.backgroundColor = isDark ? '#059669' : '#205c36';
                    } else {
                        indicator.style.backgroundColor = isDark ? '#27272a' : 'var(--foreground)';
                    }
                }

                if (immediate || !indicator.dataset.initialized) {
                    indicator.style.transition = 'none';
                    indicator.style.transform = `translate3d(${x}px, ${y}px, 0)`;
                    indicator.style.width = `${w}px`;
                    indicator.style.height = `${h}px`;
                    indicator.style.opacity = '1';
                    indicator.dataset.initialized = 'true';
                    void indicator.offsetHeight;
                    indicator.style.transition = '';
                } else {
                    indicator.style.transform = `translate3d(${x}px, ${y}px, 0)`;
                    indicator.style.width = `${w}px`;
                    indicator.style.height = `${h}px`;
                    indicator.style.opacity = '1';
                }
            }

            function updateAll(immediate = false) {
                requestAnimationFrame(() => {
                    getContainers().forEach(c => updatePill(c, immediate));
                });
            }

            function init() {
                updateAll(true);
                setTimeout(() => updateAll(true), 60);

                document.addEventListener('click', (e) => {
                    const btn = e.target.closest('.tab-pill, .view-pill, .nav-link-btn');
                    if (btn) {
                        const container = btn.closest(SELECTORS.join(', '));
                        if (container) {
                            requestAnimationFrame(() => updatePill(container, false));
                        }
                    }
                }, true);

                let resizeTimer = null;
                window.addEventListener('resize', () => {
                    if (resizeTimer) cancelAnimationFrame(resizeTimer);
                    resizeTimer = requestAnimationFrame(() => {
                        getContainers().forEach(c => updatePill(c, true));
                    });
                }, { passive: true });
            }

            return {
                init,
                updatePill,
                updateAll
            };
        })();
        window.LayoutPillEngine = LayoutPillEngine;
        }

        function setFilter(filter) {
            activeFilter = filter;
            document.querySelectorAll('.tab-pill').forEach(b => {
                b.classList.toggle('active', b.getAttribute('data-filter') === filter);
            });
            if (window.LayoutPillEngine) {
                const tabs = document.querySelector('.filter-tabs-minimal');
                if (tabs) window.LayoutPillEngine.updatePill(tabs);
            }
            renderAll();
        }

        function toggleDateSort() {
            sortAscending = !sortAscending;
            const thIcon = document.getElementById('thSortIcon');
            if (thIcon) thIcon.textContent = sortAscending ? '▲' : '▼';
            renderAll();
        }

        function showView(view) {
            document.getElementById('calendar-view').style.display = view === 'calendar' ? 'block' : 'none';
            document.getElementById('table-view').style.display = view === 'table' ? 'block' : 'none';
            document.getElementById('timeline-view').style.display = view === 'timeline' ? 'flex' : 'none';

            document.getElementById('btnCalendar').classList.toggle('active', view === 'calendar');
            document.getElementById('btnTable').classList.toggle('active', view === 'table');
            document.getElementById('btnTimeline').classList.toggle('active', view === 'timeline');

            if (window.LayoutPillEngine) {
                const switchers = document.querySelector('.view-switchers-minimal');
                if (switchers) window.LayoutPillEngine.updatePill(switchers);
            }
        }

        function toggleExamDone(id) {
            const item = schedule.find(s => s.id === id);
            if (item) {
                item.completed = !item.completed;
                saveSchedule(schedule);
                renderAll();
                updateModalSubjectList();
            }
        }

        function deleteExam(id) {
            const item = schedule.find(s => s.id === id);
            const name = item ? (item.shortTag || item.subject) : 'this paper';
            if (confirm(`Remove "${name}" from your examination timetable?`)) {
                schedule = schedule.filter(s => s.id !== id);
                recalculateGaps(schedule);
                saveSchedule(schedule);
                renderAll();
                updateModalSubjectList();
            }
        }

        function loadPreset(type) {
            if (type === 'default') {
                if (confirm('Reset timetable to the 3 standard regular papers?')) {
                    schedule = JSON.parse(JSON.stringify(DEFAULT_SCHEDULE));
                    recalculateGaps(schedule);
                    saveSchedule(schedule);
                    renderAll();
                    updateModalSubjectList();
                }
            } else if (type === 'backlog') {
                if (confirm('Load the full 7-paper SGSITS timetable (including 4 old syllabus backlog subjects)?')) {
                    schedule = JSON.parse(JSON.stringify(FULL_BACKLOG_SCHEDULE));
                    recalculateGaps(schedule);
                    saveSchedule(schedule);
                    renderAll();
                    updateModalSubjectList();
                }
            } else if (type === 'clear') {
                if (confirm('Clear all subjects from your timetable?')) {
                    schedule = [];
                    saveSchedule(schedule);
                    renderAll();
                    updateModalSubjectList();
                }
            }
        }

        // Render Separated Calendar Grids (Zero Borders)
        function renderCalendar() {
            const container = document.getElementById('calSeparatedContainer');
            if (!container) return;

            const monthSet = new Set(['2026-11', '2026-12']);
            schedule.forEach(item => {
                if (item.isoDate && item.isoDate.length >= 7) {
                    monthSet.add(item.isoDate.substring(0, 7));
                }
            });

            const sortedMonths = Array.from(monthSet).sort();
            const now = new Date();
            const currentTodayIso = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;

            const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            const monthShorts = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
            const dayLabels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

            let html = '';

            sortedMonths.forEach(ym => {
                const [yearStr, monthStr] = ym.split('-');
                const year = parseInt(yearStr, 10);
                const month = parseInt(monthStr, 10) - 1;

                const daysInMonth = new Date(year, month + 1, 0).getDate();
                const firstDayOfWeek = new Date(year, month, 1).getDay();

                const monthExams = schedule.filter(item => item.isoDate && item.isoDate.startsWith(ym));
                const examCount = monthExams.length;

                let maxWeeks = 5;
                for (let d = 1; d <= daysInMonth; d++) {
                    const w = Math.floor((d + firstDayOfWeek - 1) / 7);
                    if (w >= maxWeeks) maxWeeks = w + 1;
                }

                const isCurrentMonth = (now.getFullYear() === year && now.getMonth() === month);

                html += `
                <div class="cal-box" data-month="${ym}">
                    <div class="cal-box-header">
                        <span>${monthNames[month]} ${year}</span>
                        <div style="display: flex; gap: 6px; align-items: center;">
                            ${isCurrentMonth ? `<span class="badge badge-sky" style="font-size: 11px;">Today: ${now.getDate()} ${monthShorts[month]}</span>` : ''}
                            <span class="badge ${examCount > 0 ? 'badge-sky' : 'badge-subtle'}" style="font-size: 11px;">
                                ${examCount} ${examCount === 1 ? 'Paper' : 'Papers'}
                            </span>
                        </div>
                    </div>
                    <div class="cal-grid-vertical" style="grid-template-columns: 46px repeat(${maxWeeks}, 1fr);">
                        <div class="cal-col-label">Day</div>
                `;

                for (let w = 1; w <= maxWeeks; w++) {
                    html += `<div class="cal-col-label">W${w}</div>`;
                }

                const gridMap = Array.from({ length: 7 }, () => Array(maxWeeks).fill(null));
                for (let d = 1; d <= daysInMonth; d++) {
                    const dayOfWeek = (firstDayOfWeek + d - 1) % 7;
                    const weekIndex = Math.floor((d + firstDayOfWeek - 1) / 7);
                    if (weekIndex < maxWeeks) {
                        gridMap[dayOfWeek][weekIndex] = d;
                    }
                }

                for (let dow = 0; dow < 7; dow++) {
                    html += `<div class="cal-row-label">${dayLabels[dow]}</div>`;

                    for (let w = 0; w < maxWeeks; w++) {
                        const dayNum = gridMap[dow][w];
                        if (dayNum === null) {
                            html += `<div class="cal-cell empty">—</div>`;
                        } else {
                            const dIso = `${year}-${String(month + 1).padStart(2, '0')}-${String(dayNum).padStart(2, '0')}`;
                            const isToday = (dIso === currentTodayIso);
                            const exam = schedule.find(item => item.isoDate === dIso);

                            let cellClasses = ['cal-cell'];
                            let cellContent = `<span>${dayNum}</span>`;
                            let cellTitle = `${dayNum} ${monthShorts[month]} ${year}`;

                            if (isToday) {
                                cellClasses.push('today', 'current-date');
                                cellTitle += ' (Today)';
                            }

                            if (exam) {
                                const tagText = exam.shortTag || exam.code.replace('CE ', '');
                                if (exam.completed) {
                                    cellClasses.push('exam-done');
                                    cellTitle += `: ${exam.subject} [✓ Concluded]`;
                                    cellContent += `<span class="cal-cell-tag cal-cell-tag-done" title="Concluded Paper">✓ ${tagText}</span>`;
                                } else if (exam.isOld) {
                                    cellClasses.push('exam-old');
                                    cellTitle += `: ${exam.subject} (Backlog)`;
                                    cellContent += `<span class="cal-cell-tag">${tagText}</span>`;
                                } else {
                                    cellClasses.push('exam-reg');
                                    cellTitle += `: ${exam.subject} (Regular)`;
                                    cellContent += `<span class="cal-cell-tag">${tagText}</span>`;
                                }
                            } else if (isToday) {
                                cellContent += `<span class="cal-cell-tag">Today</span>`;
                            }

                            const clickHandler = exam ? `onclick="handleExamCellClick(${exam.id})"` : `onclick="handleEmptyDateClick('${dIso}')"`;

                            html += `
                            <div class="${cellClasses.join(' ')}" data-date="${dIso}" title="${cellTitle}" ${clickHandler} style="cursor: pointer;">
                                ${cellContent}
                            </div>
                            `;
                        }
                    }
                }

                html += `
                    </div>
                </div>
                `;
            });

            container.innerHTML = html;
        }

        function handleExamCellClick(id) {
            openEditModal(id);
        }

        function handleEmptyDateClick(dateIso) {
            openEditModal();
            const dateInput = document.getElementById('formDate');
            if (dateInput) dateInput.value = dateIso;
        }

        function getPyqLink(item) {
            if (!item.link) return '';
            const isLocalIndex = (item.link === 'index.html' || item.link === 'index.html#syllabus' || item.link === '#syllabus');
            if (isLocalIndex) {
                if (window.switchPageView) {
                    return `<a href="#syllabus" onclick="window.switchPageView('syllabus');return false;" style="color: var(--pastel-sky-foreground); font-weight: 600; font-size: 12px; margin-right: 4px;">PYQs →</a>`;
                }
                return `<a href="index.html#syllabus" style="color: var(--pastel-sky-foreground); font-weight: 600; font-size: 12px; margin-right: 4px;">PYQs →</a>`;
            }
            return `<a href="${item.link}" style="color: var(--pastel-sky-foreground); font-weight: 600; font-size: 12px; margin-right: 4px;">PYQs →</a>`;
        }

        function renderTable(filtered) {
            const tbody = document.getElementById('tableBody');
            if (!tbody) return;

            if (filtered.length === 0) {
                tbody.innerHTML = `
                    <tr>
                        <td colspan="8" style="text-align: center; padding: 24px; color: var(--muted-foreground);">
                            No examination papers match the selected filter.
                        </td>
                    </tr>
                `;
                return;
            }

            tbody.innerHTML = filtered.map(item => `
                <tr class="${item.completed ? 'row-done' : ''}">
                    <td>
                        <strong>${item.date}</strong>
                        ${item.completed ? '<span style="color: var(--pastel-done-foreground); margin-left: 4px; font-weight: 700;">✓</span>' : ''}
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
                    <td>
                        <button class="status-btn ${item.completed ? 'status-btn-done' : 'status-btn-pending'}" onclick="toggleExamDone(${item.id})" title="${item.completed ? 'Mark as pending' : 'Mark as done'}">
                            <i class="icon hgi-stroke ${item.completed ? 'hgi-tick-01' : 'hgi-circle'}"></i>
                            ${item.completed ? 'Done' : 'Mark Done'}
                        </button>
                    </td>
                    <td style="font-size: 13px; font-weight: 500;">${item.gap}</td>
                    <td style="text-align: right; white-space: nowrap;">
                        <div style="display: inline-flex; align-items: center; gap: 6px;">
                            ${getPyqLink(item)}
                            <button class="btn-icon-action" onclick="openEditModal(${item.id})" title="Edit paper details">
                                <i class="icon hgi-stroke hgi-pencil-edit-02" style="font-size: 14px;"></i>
                            </button>
                            <button class="btn-icon-action btn-icon-danger" onclick="deleteExam(${item.id})" title="Remove paper">
                                <i class="icon hgi-stroke hgi-delete-02" style="font-size: 14px;"></i>
                            </button>
                        </div>
                    </td>
                </tr>
            `).join('');
        }

        function renderTimeline(filtered) {
            const tline = document.getElementById('timeline-view');
            if (!tline) return;

            if (filtered.length === 0) {
                tline.innerHTML = `
                    <div style="text-align: center; padding: 24px; color: var(--muted-foreground);">
                        No examination papers match the selected filter.
                    </div>
                `;
                return;
            }

            tline.innerHTML = filtered.map(item => `
                <div class="timeline-card ${item.completed ? 'done' : (item.isOld ? 'old' : 'regular')}">
                    <div style="min-width: 110px;">
                        <div style="font-size: 16px; font-weight: 700; display: flex; align-items: center; gap: 6px;">
                            ${item.date}
                            ${item.completed ? '<span style="color: var(--pastel-done-foreground);">✓</span>' : ''}
                        </div>
                        <div style="font-size: 11px; color: var(--muted-foreground);">${item.day}</div>
                    </div>
                    <div style="flex: 1;">
                        <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 2px;">
                            <span class="code-tag">${item.code}</span>
                            <span class="badge ${item.isOld ? 'badge-peach' : 'badge-sage'}">${item.tag}</span>
                            ${item.completed ? '<span class="badge badge-done">✓ Concluded</span>' : ''}
                        </div>
                        <div style="font-size: 14px; font-weight: 600;">${item.subject}</div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 12px; font-weight: 600; background: var(--secondary); padding: 4px 10px; border-radius: var(--radius-full);">${item.gap}</span>
                        <button class="status-btn ${item.completed ? 'status-btn-done' : 'status-btn-pending'}" onclick="toggleExamDone(${item.id})">
                            ${item.completed ? '✓ Done' : 'Mark Done'}
                        </button>
                    </div>
                </div>
            `).join('');
        }

        function renderAll() {
            let filtered = schedule.filter(item => {
                if (activeFilter === 'regular') return !item.isOld;
                if (activeFilter === 'old') return item.isOld;
                if (activeFilter === 'done') return item.completed;
                return true;
            });

            filtered.sort((a, b) => {
                const comp = (a.isoDate || '').localeCompare(b.isoDate || '');
                return sortAscending ? comp : -comp;
            });

            renderCalendar();
            renderTable(filtered);
            renderTimeline(filtered);

            // Update filter counts
            const total = schedule.length;
            const completedCount = schedule.filter(s => s.completed).length;
            const regCount = schedule.filter(s => !s.isOld).length;
            const oldCount = schedule.filter(s => s.isOld).length;

            const fAll = document.getElementById('filterCountAll');
            if (fAll) fAll.textContent = total;
            const fReg = document.getElementById('filterCountReg');
            if (fReg) fReg.textContent = regCount;
            const fOld = document.getElementById('filterCountOld');
            if (fOld) fOld.textContent = oldCount;
            const fDone = document.getElementById('filterCountDone');
            if (fDone) fDone.textContent = completedCount;

            initCurrentDateTracker();
        }

        // ----------------------------------------------------
        // EDIT TIMETABLE MODAL ENGINE (ZERO BORDERS)
        // ----------------------------------------------------
        const editModal = document.getElementById('editModal');

        function openEditModal(editId = null) {
            editModal.style.display = 'flex';
            document.body.style.overflow = 'hidden';
            updateModalSubjectList();

            if (editId) {
                populateFormForEdit(editId);
            } else {
                resetExamForm();
            }
        }

        function closeEditModal() {
            editModal.style.display = 'none';
            document.body.style.overflow = '';
            resetExamForm();
        }

        function handleModalOverlayClick(e) {
            if (e.target === editModal) {
                closeEditModal();
            }
        }

        function resetExamForm() {
            document.getElementById('formExamId').value = '';
            document.getElementById('formSubject').value = '';
            document.getElementById('formCode').value = '';
            document.getElementById('formShortTag').value = '';
            document.getElementById('formDate').value = '';
            document.getElementById('formCategory').value = 'Regular';
            document.getElementById('formLink').value = '';
            document.getElementById('formCompleted').checked = false;
            document.getElementById('formSubmitBtnText').textContent = 'Add Subject';
            document.getElementById('formCancelBtn').style.display = 'none';
        }

        function populateFormForEdit(id) {
            const item = schedule.find(s => s.id === id);
            if (!item) return;

            document.getElementById('formExamId').value = item.id;
            document.getElementById('formSubject').value = item.subject || '';
            document.getElementById('formCode').value = item.code || '';
            document.getElementById('formShortTag').value = item.shortTag || '';
            document.getElementById('formDate').value = item.isoDate || '';
            document.getElementById('formCategory').value = item.isOld ? 'Old Syllabus' : 'Regular';
            document.getElementById('formLink').value = item.link || '';
            document.getElementById('formCompleted').checked = !!item.completed;

            document.getElementById('formSubmitBtnText').textContent = 'Save Changes';
            document.getElementById('formCancelBtn').style.display = 'inline-flex';
            document.getElementById('formSubject').focus();
        }

        function handleFormSubmit(e) {
            e.preventDefault();
            const idVal = document.getElementById('formExamId').value;
            const subject = document.getElementById('formSubject').value.trim();
            const code = document.getElementById('formCode').value.trim() || 'CE-EXAM';
            const shortTag = document.getElementById('formShortTag').value.trim() || 'Exam';
            const isoDate = document.getElementById('formDate').value;
            const category = document.getElementById('formCategory').value;
            const link = document.getElementById('formLink').value.trim() || null;
            const completed = document.getElementById('formCompleted').checked;

            if (!subject || !isoDate) {
                alert('Please provide a subject name and examination date.');
                return;
            }

            const isOld = (category === 'Old Syllabus');

            if (idVal) {
                const existing = schedule.find(s => String(s.id) === String(idVal));
                if (existing) {
                    existing.subject = subject;
                    existing.code = code;
                    existing.shortTag = shortTag;
                    existing.isoDate = isoDate;
                    existing.tag = category;
                    existing.isOld = isOld;
                    existing.link = link;
                    existing.completed = completed;
                }
            } else {
                const newId = Date.now();
                schedule.push({
                    id: newId,
                    subject,
                    code,
                    shortTag,
                    isoDate,
                    tag: category,
                    isOld,
                    link,
                    completed
                });
            }

            recalculateGaps(schedule);
            saveSchedule(schedule);
            renderAll();
            updateModalSubjectList();
            resetExamForm();
        }

        function updateModalSubjectList() {
            const listEl = document.getElementById('modalSubjectList');
            const countEl = document.getElementById('modalExamCount');
            if (countEl) countEl.textContent = schedule.length;
            if (!listEl) return;

            if (schedule.length === 0) {
                listEl.innerHTML = `<div style="text-align: center; color: var(--muted-foreground); padding: 12px; font-size: 13px;">No subjects scheduled yet. Add one above or select a preset below.</div>`;
                return;
            }

            listEl.innerHTML = schedule.map(item => `
                <div class="modal-subject-item ${item.completed ? 'is-done' : ''}">
                    <div style="flex: 1; min-width: 0;">
                        <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 2px;">
                            <span style="font-weight: 700; font-size: 13px;">${item.date}</span>
                            <span class="code-tag" style="font-size: 11px;">${item.code}</span>
                            <span class="badge ${item.isOld ? 'badge-peach' : 'badge-sage'}" style="font-size: 10px; padding: 1px 6px;">${item.tag}</span>
                            ${item.completed ? '<span class="badge badge-done" style="font-size: 10px; padding: 1px 6px;">✓ Done</span>' : ''}
                        </div>
                        <div style="font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${item.subject}</div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <button type="button" class="status-btn ${item.completed ? 'status-btn-done' : 'status-btn-pending'}" onclick="toggleExamDone(${item.id})">
                            ${item.completed ? '✓ Done' : 'Mark Done'}
                        </button>
                        <button type="button" class="btn-icon-action" onclick="populateFormForEdit(${item.id})" title="Edit paper">
                            <i class="icon hgi-stroke hgi-pencil-edit-02" style="font-size: 14px;"></i>
                        </button>
                        <button type="button" class="btn-icon-action btn-icon-danger" onclick="deleteExam(${item.id})" title="Remove paper">
                            <i class="icon hgi-stroke hgi-delete-02" style="font-size: 14px;"></i>
                        </button>
                    </div>
                </div>
            `).join('');
        }

        // Scroll to Top
        window.scrollToTop = function() {
            try {
                window.scrollTo({ top: 0, behavior: 'smooth' });
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
        if (!window.switchPageView) {
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
        }

        renderAll();
        if (window.LayoutPillEngine) {
            window.LayoutPillEngine.init();
        }

        // Window Exports for Unified SPA & Inline Handlers
        window.renderTimetableAll = renderAll;
        window.renderAll = renderAll;
        window.setFilter = setFilter;
        window.showView = showView;
        window.toggleDateSort = toggleDateSort;
        window.toggleExamDone = toggleExamDone;
        window.deleteExam = deleteExam;
        window.loadPreset = loadPreset;
        window.openEditModal = openEditModal;
        window.closeEditModal = closeEditModal;
        window.handleModalOverlayClick = handleModalOverlayClick;
        window.resetExamForm = resetExamForm;
        window.populateFormForEdit = populateFormForEdit;
        window.handleFormSubmit = handleFormSubmit;
        window.handleExamCellClick = handleExamCellClick;
        window.handleEmptyDateClick = handleEmptyDateClick;
"""

_BASE_CSS = """:root {
            --font-size-h1: 28px;
            --line-height-h1: 36px;
            --font-size-h2: 22px;
            --line-height-h2: 28px;
            --font-size-h6: 15px;
            --line-height-h6: 20px;
            --font-size-body-large: 15px;
            --line-height-body-large: 22px;
            --font-size-body-medium: 13.5px;
            --line-height-body-medium: 19px;
            --font-size-body-small: 12px;
            --line-height-body-small: 16px;
            --font-size-button: 13px;
            --line-height-button: 18px;
            --font-size-stat: 22px;
            --line-height-stat: 28px;
            --font-size-overline: 11px;

            /* Neutral Color Palette (Light Mode - Warm Linen Paper) */
            --background: #fbfaf8;
            --foreground: #1e293b;
            --card: #ffffff;
            --card-foreground: #1e293b;
            --secondary: #f3f1ec;
            --secondary-hover: #e8e5dc;
            --secondary-foreground: #1e293b;
            --muted: #f3f1ec;
            --muted-foreground: #64748b;
            --primary: #2d3748;
            --primary-foreground: #ffffff;

            /* Category Tokens (Zero Harsh Borders) */
            --pastel-sage-bg: #eaf4ed;
            --pastel-sage-foreground: #205c36;
            --pastel-sage-count-bg: rgba(32, 92, 54, 0.12);

            --pastel-peach-bg: #fff1e8;
            --pastel-peach-foreground: #9a4318;
            --pastel-peach-count-bg: rgba(154, 67, 24, 0.12);

            --pastel-sky-bg: #ebf5fd;
            --pastel-sky-foreground: #1a5a90;

            --pastel-done-bg: #edf7ee;
            --pastel-done-foreground: #205c36;
            --pastel-done-muted: #f4faf5;
            --pastel-done-count-bg: rgba(32, 92, 54, 0.14);

            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-full: 9999px;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-mono: ui-monospace, Menlo, Monaco, Consolas, monospace;
        }

        [data-theme="dark"] {
            /* Neutral Color Palette (Dark Mode - Zinc 950 Canvas) */
            --background: #09090b;
            --foreground: #fcfcfd;
            --card: #141416;
            --card-foreground: #fcfcfd;
            --secondary: #1c1c1f;
            --secondary-hover: #27272a;
            --secondary-foreground: #fcfcfd;
            --muted: #1c1c1f;
            --muted-foreground: #a1a1aa;
            --primary: #fcfcfd;
            --primary-foreground: #09090b;

            --pastel-sage-bg: rgba(52, 211, 153, 0.16);
            --pastel-sage-foreground: #34d399;
            --pastel-sage-count-bg: rgba(52, 211, 153, 0.22);

            --pastel-peach-bg: rgba(251, 146, 60, 0.16);
            --pastel-peach-foreground: #fb923c;
            --pastel-peach-count-bg: rgba(251, 146, 60, 0.22);

            --pastel-sky-bg: rgba(56, 189, 248, 0.16);
            --pastel-sky-foreground: #38bdf8;

            --pastel-done-bg: rgba(52, 211, 153, 0.14);
            --pastel-done-foreground: #6ee7b7;
            --pastel-done-muted: rgba(52, 211, 153, 0.08);
            --pastel-done-count-bg: rgba(52, 211, 153, 0.22);

            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
        }

        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
            transition: background-color 0.15s ease, color 0.15s ease;
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
            border: none;
            outline: none;
        }

        a { color: inherit; text-decoration: none; }

        /* Hugeicons Tokens */
        .icon,
        .hgi-stroke.icon,
        i.hgi-stroke {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 1.15rem;
            height: 1.15rem;
            font-size: 1.15rem;
            line-height: 1;
            vertical-align: middle;
            flex-shrink: 0;
            font-style: normal;
        }

        .icon-sm {
            width: 1rem;
            height: 1rem;
            font-size: 1rem;
        }

        .mobile-nav-icon,
        .hgi-stroke.mobile-nav-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            font-size: 22px;
            line-height: 1;
            transition: transform 0.15s ease;
            font-style: normal;
        }

        .container {
            max-width: 1440px;
            width: 100%;
            margin: 0 auto;
            padding-left: max(1rem, env(safe-area-inset-left));
            padding-right: max(1rem, env(safe-area-inset-right));
            box-sizing: border-box;
        }

        @media (min-width: 640px) {
            .container {
                padding-left: max(1.5rem, env(safe-area-inset-left));
                padding-right: max(1.5rem, env(safe-area-inset-right));
            }
        }

        @media (min-width: 1024px) {
            .container {
                padding-left: max(2.5rem, env(safe-area-inset-left));
                padding-right: max(2.5rem, env(safe-area-inset-right));
            }
        }

        @media (min-width: 1440px) {
            .container {
                padding-left: max(3.5rem, env(safe-area-inset-left));
                padding-right: max(3.5rem, env(safe-area-inset-right));
            }
        }

        main.container {
            padding-bottom: 3.5rem;
        }

        /* ----------------------------------------------------
           STICKY HEADER NAVBAR (MATCHING INDEX.HTML EXACTLY)
           Zero Borders • Pure Background Separation
           ---------------------------------------------------- */
        .header {
            position: sticky;
            top: 0;
            z-index: 100;
            background-color: var(--card);
            box-shadow: var(--shadow-sm);
            border: none;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, box-shadow 0.2s ease;
            will-change: transform;
            padding-top: env(safe-area-inset-top, 0px);
        }

        .header.header-hidden {
            transform: translateY(-100%);
            box-shadow: none;
            pointer-events: none;
        }

        .nav {
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            height: 60px;
            gap: 1rem;
        }

        .brand {
            justify-self: start;
            min-width: 0;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-shrink: 0;
            white-space: nowrap;
            text-decoration: none;
            cursor: pointer;
        }

        .brand-title {
            font-size: 1.0625rem;
            font-weight: 700;
            color: var(--foreground);
            letter-spacing: -0.015em;
        }

        .nav-links {
            justify-self: center;
            display: flex;
            align-items: center;
            gap: 0.35rem;
            list-style: none;
            overflow-x: auto;
            scrollbar-width: none;
            position: relative;
        }

        .nav-links::-webkit-scrollbar { display: none; }

        .nav-links .layout-pill-indicator {
            position: absolute;
            top: 0;
            left: 0;
            pointer-events: none;
            z-index: 1;
            background-color: var(--secondary);
            border-radius: var(--radius-md);
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
            transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        width 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        height 0.28s cubic-bezier(0.16, 1, 0.3, 1),
                        opacity 0.2s ease;
            will-change: transform, width, height;
        }

        [data-theme="dark"] .nav-links .layout-pill-indicator {
            background-color: #27272a;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.35);
        }

        .nav-link-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.5rem 0.85rem;
            background-color: transparent !important;
            color: var(--muted-foreground);
            font-size: 0.875rem;
            font-weight: 500;
            border-radius: var(--radius-md);
            cursor: pointer;
            border: none;
            transition: color 0.18s ease, transform 0.1s ease;
            white-space: nowrap;
            text-decoration: none;
            position: relative;
            z-index: 2;
        }

        .nav-link-btn:hover:not(.active) {
            color: var(--foreground);
        }

        .nav-link-btn:active {
            transform: scale(0.96);
        }

        .nav-link-btn.active {
            background-color: transparent !important;
            box-shadow: none !important;
            color: var(--foreground) !important;
            font-weight: 600;
        }

        .nav-actions {
            justify-self: end;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-shrink: 0;
        }

        .theme-toggle-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            background-color: var(--secondary);
            color: var(--foreground);
            border-radius: var(--radius-md);
            border: none;
            cursor: pointer;
            transition: background-color 0.15s ease;
        }

        .theme-toggle-btn:hover {
            background-color: var(--secondary-hover);
        }"""

_EXTRA_CSS = """/* Floating Scroll to Top Button (Zero Borders) */
        .scroll-to-top-btn {
            position: fixed !important;
            bottom: 2rem !important;
            right: 2rem !important;
            z-index: 99999 !important;
            width: 44px;
            height: 44px;
            border-radius: var(--radius-full);
            background: var(--primary);
            color: var(--primary-foreground);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.28);
            border: none !important;
            display: inline-flex !important;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0.95;
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s ease, opacity 0.2s ease;
        }

        .scroll-to-top-btn:hover {
            opacity: 1;
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
        }

        /* Mobile Bottom Nav (Zero Borders) */
        .mobile-bottom-nav {
            display: none;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            background-color: var(--card);
            border: none;
            box-shadow: 0 -2px 12px rgba(0, 0, 0, 0.05);
            padding-bottom: env(safe-area-inset-bottom, 0px);
            height: calc(56px + env(safe-area-inset-bottom, 0px));
            align-items: stretch;
            justify-content: space-around;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }

        [data-theme="dark"] .mobile-bottom-nav {
            box-shadow: 0 -2px 14px rgba(0, 0, 0, 0.5);
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
                display: flex;
                justify-content: space-between;
                height: 52px;
                gap: 0.5rem;
            }
            .brand-title {
                font-size: 0.95rem;
                max-width: calc(100vw - 110px);
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
        }"""

def get_timetable_styles() -> str:
    """Returns CSS styles required for the examination timetable."""
    return _TIMETABLE_STYLES

def get_timetable_html_view() -> str:
    """Returns HTML content for the timetable page view container."""
    return _TIMETABLE_HTML_VIEW

def get_timetable_modal_html() -> str:
    """Returns HTML markup for the customize timetable modal."""
    return _TIMETABLE_MODAL_HTML

def get_timetable_script() -> str:
    """Returns JavaScript code controlling the timetable engine."""
    return _TIMETABLE_SCRIPT

def generate_timetable_html() -> str:
    """Generates the complete standalone timetable.html page."""
    styles = get_timetable_styles()
    view_html = get_timetable_html_view()
    modal_html = get_timetable_modal_html()
    script_js = get_timetable_script()

    template = """<!DOCTYPE html>
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
    <meta name="description" content="Civil Engineering Examination Timetable (Nov - Dec 2026). Seamless borderless schedule with colored filter badges, local storage persistence, and dynamic calendars.">
    <!-- Minimalist Favicon & Touch Icons -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%2309090b'/%3E%3Crect x='0.5' y='0.5' width='31' height='31' rx='6.5' fill='none' stroke='rgba(255,255,255,0.15)' stroke-width='1'/%3E%3Cpath d='M8 6h16v4H12v4h9v4H12v4h12v4H8z' fill='%23fcfcfd'/%3E%3C/svg%3E">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="alternate icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <!-- Hugeicons Font (CDN with offline local fallback) -->
    <link rel="stylesheet" href="https://use.hugeicons.com/font/icons.css" onerror="this.onerror=null;this.href='vendor/hugeicons/icons.css'">
    <link rel="stylesheet" href="vendor/hugeicons/icons.css">
    <style>
__STYLES_PLACEHOLDER__
    </style>
</head>
<body>

    <!-- STICKY HEADER NAVBAR (MATCHING INDEX.HTML EXACTLY) -->
    <header class="header">
        <div class="container nav">
            <a href="index.html#syllabus" class="brand" title="Geotechnical Engineering - II">
                <span class="brand-title">Geotechnical Engineering - II</span>
            </a>

            <!-- Nav links matching index.html navigation hierarchy -->
            <ul class="nav-links">
                <li>
                    <a href="index.html#syllabus" class="nav-link-btn" data-view="syllabus" title="PYQ Checklist">
                        <i class="icon icon-sm hgi-stroke hgi-task-01"></i>
                        Checklist
                    </a>
                </li>
                <li>
                    <a href="index.html#formulas" class="nav-link-btn" data-view="formulas" title="Master Formulas">
                        <i class="icon icon-sm hgi-stroke hgi-function-of-x"></i>
                        Formulas
                    </a>
                </li>
                <li>
                    <a href="timetable.html" class="nav-link-btn nav-link-timetable active" title="View Exam Timetable">
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

    <main class="container">
__VIEW_PLACEHOLDER__
    </main>

__MODAL_PLACEHOLDER__

    <script>
__SCRIPT_PLACEHOLDER__
    </script>

    <!-- Floating Back to Top Button -->
    <button id="scrollToTopBtn" class="scroll-to-top-btn" aria-label="Scroll to top" title="Scroll to top" onclick="scrollToTop()">
        <i class="hgi-stroke hgi-arrow-up-01"></i>
    </button>

    <!-- MOBILE BOTTOM APP NAVIGATION (MATCHING INDEX.HTML) -->
    <nav class="mobile-bottom-nav" aria-label="Mobile App Navigation">
        <a href="index.html#syllabus" class="mobile-nav-item" aria-label="PYQ Checklist">
            <i class="mobile-nav-icon hgi-stroke hgi-task-01"></i>
            <span class="mobile-nav-label">Checklist</span>
        </a>
        <a href="index.html#formulas" class="mobile-nav-item" aria-label="Formulas">
            <i class="mobile-nav-icon hgi-stroke hgi-function-of-x"></i>
            <span class="mobile-nav-label">Formulas</span>
        </a>
        <a href="timetable.html" class="mobile-nav-item active" aria-label="Exam Timetable">
            <i class="mobile-nav-icon hgi-stroke hgi-calendar-03"></i>
            <span class="mobile-nav-label">Timetable</span>
        </a>
    </nav>
</body>
</html>"""

    full_css = _BASE_CSS + "\n\n" + styles + "\n\n" + _EXTRA_CSS
    out = template.replace("__STYLES_PLACEHOLDER__", full_css)
    out = out.replace("__VIEW_PLACEHOLDER__", view_html)
    out = out.replace("__MODAL_PLACEHOLDER__", modal_html)
    out = out.replace("__SCRIPT_PLACEHOLDER__", script_js)
    return out

if __name__ == "__main__":
    out_file = _repo_root / "timetable.html"
    content = generate_timetable_html()
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated {out_file} with borderless design, colored filter badges, and unified navbar!")

    # Also rebuild index.html if generate_dashboard is available
    try:
        from generate_dashboard import build_dashboard_for_subject
        build_dashboard_for_subject(write_index=True)
    except Exception as e:
        print(f"Notice: automatic index update encountered: {e}")
