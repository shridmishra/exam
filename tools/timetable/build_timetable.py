#!/usr/bin/env python3
"""
Civil Engineering Examination Timetable Generator.
Produces timetable.html with customizable timetable engine, client-side localStorage persistence,
dynamic month calendars, done (muted green) visual states, and official SGSITS defaults.
"""
from pathlib import Path

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
    <meta name="description" content="Civil Engineering Examination Timetable (Nov - Dec 2026). Customizable schedule stored in local storage with separated dynamic calendars, status tracking, and gap analysis.">
    <!-- Minimalist Favicon & Touch Icons -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%2309090b'/%3E%3Crect x='0.5' y='0.5' width='31' height='31' rx='6.5' fill='none' stroke='rgba(255,255,255,0.15)' stroke-width='1'/%3E%3Cpath d='M8 6h16v4H12v4h9v4H12v4h12v4H8z' fill='%23fcfcfd'/%3E%3C/svg%3E">
    <link rel="icon" type="image/svg+xml" href="favicon.svg">
    <link rel="alternate icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
    <!-- Hugeicons Font (CDN with offline local fallback) -->
    <link rel="stylesheet" href="https://use.hugeicons.com/font/icons.css" onerror="this.onerror=null;this.href='vendor/hugeicons/icons.css'">
    <link rel="stylesheet" href="vendor/hugeicons/icons.css">
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

            /* Muted Green Concluded / Done Palette ("Yes, this is done") */
            --pastel-done-bg: #edf7ee;
            --pastel-done-border: #b7e1be;
            --pastel-done-foreground: #205c36;
            --pastel-done-muted: #f4faf5;
            --pastel-done-tag-bg: #dcf0e0;

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

            /* Dark mode Muted Green Concluded Palette */
            --pastel-done-bg: rgba(52, 211, 153, 0.14);
            --pastel-done-border: rgba(52, 211, 153, 0.30);
            --pastel-done-foreground: #6ee7b7;
            --pastel-done-muted: rgba(52, 211, 153, 0.08);
            --pastel-done-tag-bg: rgba(52, 211, 153, 0.22);

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

        /* Hugeicons Tokens */
        .icon,
        .hgi-stroke.icon,
        i.hgi-stroke {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 1.25rem;
            height: 1.25rem;
            font-size: 1.25rem;
            line-height: 1;
            vertical-align: middle;
            flex-shrink: 0;
            font-style: normal;
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

        .scroll-to-top-btn i,
        .scroll-to-top-btn .icon {
            font-size: 24px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

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

        /* Floating Scroll to Top Button */
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

        @media (max-width: 640px) {
            .scroll-to-top-btn {
                bottom: 1.25rem !important;
                right: 1.25rem !important;
                width: 42px;
                height: 42px;
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
            gap: 4px;
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

        .badge-done {
            background: var(--pastel-done-bg);
            border-color: var(--pastel-done-border);
            color: var(--pastel-done-foreground);
            font-weight: 600;
        }

        .badge-subtle {
            background: var(--muted);
            border-color: var(--border);
            color: var(--muted-foreground);
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
            grid-template-columns: repeat(5, 1fr);
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

        .btn-action {
            background: var(--card);
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
            transition: background-color 0.15s ease, border-color 0.15s ease;
        }

        .btn-action:hover {
            background: var(--muted);
            border-color: var(--border-hover);
        }

        .edit-timetable-btn {
            background: var(--pastel-sage-bg);
            border-color: var(--pastel-sage-border);
            color: var(--pastel-sage-foreground);
        }

        .edit-timetable-btn:hover {
            background: var(--pastel-sage-border);
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
           DYNAMIC SEPARATED CALENDARS (November & December)
           ---------------------------------------------------- */
        .cal-separated-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
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
            padding: 2px;
            position: relative;
            transition: transform 0.1s ease, border-color 0.15s ease;
        }

        .cal-cell:hover:not(.empty) {
            border-color: var(--border-hover);
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

        /* Done Paper Cell Style: Muted Green "Yes, this is done" */
        .cal-cell.exam-done {
            background: var(--pastel-done-bg) !important;
            border-color: var(--pastel-done-border) !important;
            color: var(--pastel-done-foreground) !important;
            font-weight: 700;
            position: relative;
            box-shadow: 0 1px 3px rgba(32, 92, 54, 0.08);
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

        .cal-cell.today.exam-done,
        .cal-cell.current-date.exam-done {
            background: var(--pastel-done-bg) !important;
            border-color: var(--pastel-sky-foreground);
            color: var(--pastel-done-foreground);
            box-shadow: 0 0 0 2px var(--pastel-sky-border);
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
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 100%;
        }

        .cal-cell-tag.cal-cell-tag-done {
            background: var(--pastel-done-tag-bg);
            color: var(--pastel-done-foreground);
            padding: 1px 4px;
            border-radius: var(--radius-sm);
            font-size: 9px;
            font-weight: 700;
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

        tr.row-done td {
            background: var(--pastel-done-muted);
        }

        tr.row-done td:first-child {
            border-left: 3px solid var(--pastel-done-foreground);
        }

        .code-tag {
            font-family: var(--font-mono);
            font-size: var(--font-size-body-small);
            background: var(--muted);
            padding: 2px 6px;
            border-radius: var(--radius-sm);
            font-weight: 600;
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
            border: 1px solid var(--border);
            background: var(--muted);
            color: var(--muted-foreground);
            transition: all 0.15s ease;
        }

        .status-btn:hover {
            border-color: var(--border-hover);
            color: var(--foreground);
        }

        .status-btn-done {
            background: var(--pastel-done-bg);
            border-color: var(--pastel-done-border);
            color: var(--pastel-done-foreground);
        }

        .status-btn-done:hover {
            background: var(--pastel-done-tag-bg);
        }

        .btn-icon-action {
            background: transparent;
            border: 1px solid transparent;
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
            background: var(--muted);
            border-color: var(--border);
            color: var(--foreground);
        }

        .btn-icon-danger:hover {
            background: rgba(239, 68, 68, 0.12);
            border-color: rgba(239, 68, 68, 0.25);
            color: #ef4444;
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
        .timeline-card.done {
            background: var(--pastel-done-muted);
            border-left: 4px solid var(--pastel-done-foreground);
        }

        /* ----------------------------------------------------
           CUSTOMIZE TIMETABLE MODAL
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
        }

        .modal-card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            max-width: 660px;
            width: 100%;
            max-height: 88vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.28);
            overflow: hidden;
            animation: modalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes modalFadeIn {
            from { opacity: 0; transform: scale(0.96) translateY(8px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .modal-header {
            padding: 16px 20px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 12px;
        }

        .modal-title {
            font-size: 18px;
            font-weight: 700;
            line-height: 24px;
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
            background: var(--muted);
            color: var(--foreground);
        }

        .modal-body {
            padding: 16px 20px;
            overflow-y: auto;
            flex: 1;
        }

        .exam-form {
            background: var(--background);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 14px;
            margin-bottom: 18px;
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
            border: 1px solid var(--border);
            color: var(--foreground);
            font-size: var(--font-size-body-medium);
            font-family: var(--font-sans);
            padding: 6px 10px;
            border-radius: var(--radius-sm);
            outline: none;
        }

        .form-input:focus, .form-select:focus {
            border-color: var(--foreground);
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
            background: var(--muted);
            color: var(--foreground);
            border: 1px solid var(--border);
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            font-size: var(--font-size-button);
            font-weight: 500;
            cursor: pointer;
        }

        .btn-secondary:hover {
            background: var(--card);
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
            height: 1px;
            background: var(--border);
        }

        .modal-subject-list {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 16px;
        }

        .modal-subject-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding: 8px 12px;
            background: var(--background);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            transition: border-color 0.15s ease;
        }

        .modal-subject-item.is-done {
            background: var(--pastel-done-muted);
            border-color: var(--pastel-done-border);
        }

        .modal-presets {
            background: var(--background);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 10px 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
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
            border: 1px solid var(--border);
            color: var(--foreground);
            font-size: 11px;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: var(--radius-sm);
            cursor: pointer;
        }

        .btn-preset:hover {
            background: var(--muted);
        }

        .btn-preset-danger {
            color: #ef4444;
        }

        .btn-preset-danger:hover {
            background: rgba(239, 68, 68, 0.1);
            border-color: rgba(239, 68, 68, 0.3);
        }

        .modal-footer {
            padding: 12px 20px;
            border-top: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            background: var(--card);
        }

        .storage-notice {
            font-size: 12px;
            color: var(--muted-foreground);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .footer {
            border-top: 1px solid var(--border);
            padding: 16px 0;
            text-align: center;
            color: var(--muted-foreground);
            font-size: var(--font-size-body-small);
            margin-top: 20px;
        }

        /* Mobile Bottom Nav */
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
            .sort-btn, .edit-timetable-btn {
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

        @media print {
            .header, .controls-bar, .theme-toggle-btn, .footer, .modal-overlay, .scroll-to-top-btn { display: none !important; }
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
                    <i class="icon hgi-stroke hgi-moon-02" id="themeIcon"></i>
                </button>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-meta">
                <span class="badge badge-peach">Nov to Dec 2026</span>
                <span class="badge badge-sky" id="heroTodayBadge">Today: Current Date</span>
                <span class="badge badge-sky">Timing: 2:00 PM – 5:00 PM</span>
                <span class="badge badge-sage">Revised Timetable (SGSITS Indore)</span>
            </div>
            <h1 class="hero-title">Civil Engineering Examination Timetable</h1>

            <div class="notice-bar">
                <!-- Dynamically populated by updateNoticeBar() -->
            </div>
        </section>

        <!-- Stats Bar -->
        <section class="stats-bar">
            <div class="stat-box">
                <div class="stat-label">Total Papers</div>
                <div class="stat-value" id="statTotal">3</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Concluded / Done</div>
                <div class="stat-value" id="statDone" style="color: var(--pastel-done-foreground);">0</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Regular Papers</div>
                <div class="stat-value" id="statRegular" style="color: var(--pastel-sage-foreground);">3</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Old Syllabus</div>
                <div class="stat-value" id="statOld" style="color: var(--pastel-peach-foreground);">0</div>
            </div>
            <div class="stat-box">
                <div class="stat-label">Date Range</div>
                <div class="stat-value" id="statRange" style="font-size: 18px; line-height: 32px;">18 Nov – 12 Dec</div>
            </div>
        </section>

        <!-- Filter Controls & Edit Button -->
        <div class="controls-bar">
            <div class="filter-tabs">
                <button class="tab-btn active" data-filter="all" onclick="setFilter('all')">All (<span id="filterCountAll">3</span>)</button>
                <button class="tab-btn" data-filter="regular" onclick="setFilter('regular')">Regular (<span id="filterCountReg">3</span>)</button>
                <button class="tab-btn" data-filter="old" onclick="setFilter('old')">Old Syllabus (<span id="filterCountOld">0</span>)</button>
                <button class="tab-btn" data-filter="done" onclick="setFilter('done')">Done (<span id="filterCountDone">0</span>)</button>
            </div>

            <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <button class="btn-action edit-timetable-btn" id="btnOpenEditModal" onclick="openEditModal()" title="Customize timetable, add/edit papers, or load backlogs">
                    <i class="icon hgi-stroke hgi-pencil-edit-02"></i> Edit Timetable
                </button>

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

        <!-- VIEW 1: SEPARATED CALENDARS (Dynamic November & December Grids) -->
        <section id="calendar-view">
            <!-- Dedicated Blue Box with Current Date & Next Exam Status -->
            <div class="cal-today-box">
                <div class="cal-today-box-left">
                    <span class="badge badge-sky" style="font-size: 11px; text-transform: uppercase; font-weight: 700; letter-spacing: 0.04em;">Today</span>
                    <span class="cal-today-date-text" id="calTodayDateText">Current Date: Today</span>
                </div>
                <div class="cal-today-box-right" id="calTodayCountdownBox">
                    <span>Upcoming:</span>
                    <span class="cal-today-countdown">
                        <strong style="color: var(--pastel-sage-foreground);">Calculating...</strong>
                    </span>
                </div>
            </div>

            <!-- Dynamic separated months container -->
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
        <section id="timeline-view" class="timeline-list" style="display: none;"></section>
    </main>

    <!-- CUSTOMIZE TIMETABLE MODAL -->
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
                            <input type="text" id="formShortTag" class="form-input" placeholder="e.g. Geo-2 (shown on calendar)" maxlength="8" required>
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
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn-primary" id="formSubmitBtn">
                            <i class="icon hgi-stroke hgi-plus-sign"></i> <span id="formSubmitBtnText">Add Subject</span>
                        </button>
                        <button type="button" class="btn-secondary" id="formCancelBtn" onclick="resetExamForm()" style="display: none;">
                            Cancel Edit
                        </button>
                    </div>
                </form>

                <div class="modal-section-divider">
                    <span>Scheduled Papers (<span id="modalExamCount">3</span>)</span>
                </div>

                <!-- Subject List in Modal -->
                <div id="modalSubjectList" class="modal-subject-list"></div>

                <!-- Presets & Quick Resets -->
                <div class="modal-presets">
                    <span class="preset-label">Quick Presets:</span>
                    <div class="preset-buttons">
                        <button type="button" class="btn-preset" onclick="loadPreset('default')" title="Reset to standard 3 regular papers">
                            Reset to 3 Regular Papers
                        </button>
                        <button type="button" class="btn-preset" onclick="loadPreset('backlog')" title="Load full SGSITS timetable with 4 backlog subjects">
                            Load 7 SGSITS Papers (with Backlogs)
                        </button>
                        <button type="button" class="btn-preset btn-preset-danger" onclick="loadPreset('clear')" title="Clear all subjects">
                            Clear All
                        </button>
                    </div>
                </div>
            </div>

            <div class="modal-footer">
                <span class="storage-notice">
                    <i class="icon hgi-stroke hgi-database-01"></i> Stored locally in your browser
                </span>
                <button class="btn-primary" onclick="closeEditModal()">Done</button>
            </div>
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <p>Civil Engineering Exam Schedule • Nov – Dec 2026 • Verified with Official Revised Timetable (SGSITS)</p>
        </div>
    </footer>

    <script>
        // Default 3 regular subjects (Normal Syllabus) for public repo
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
            themeIcon.className = theme === 'dark' ? 'icon hgi-stroke hgi-sun-01' : 'icon hgi-stroke hgi-moon-02';
            themeIcon.innerHTML = '';
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

                // Calculate countdown to next UNCOMPLETED exam
                const countdownBox = document.getElementById('calTodayCountdownBox');
                if (countdownBox) {
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
                        countdownBox.innerHTML = `
                            <span>Upcoming:</span>
                            <span class="cal-today-countdown">
                                <strong style="color: ${nextExam.isOld ? 'var(--pastel-peach-foreground)' : 'var(--pastel-sage-foreground)'};">${nextExam.date.split(' ').slice(0, 2).join(' ')} (${codeDisplay})</strong> &bull; ${diffText}
                            </span>
                        `;
                    } else {
                        const totalPapers = schedule.length;
                        const allDone = totalPapers > 0 && schedule.every(s => s.completed);
                        countdownBox.innerHTML = `
                            <span class="cal-today-countdown" style="color: ${allDone ? 'var(--pastel-done-foreground)' : 'var(--muted-foreground)'};">
                                ${allDone ? '<i class="icon hgi-stroke hgi-tick-double-02"></i> All examinations concluded' : 'No upcoming papers scheduled'}
                            </span>
                        `;
                    }
                }
            } catch (err) {
                console.warn('Current date tracker initialized with fallback:', err);
            }
        }

        function setFilter(filter) {
            activeFilter = filter;
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.classList.toggle('active', b.getAttribute('data-filter') === filter);
            });
            renderAll();
        }

        function toggleDateSort() {
            sortAscending = !sortAscending;
            document.getElementById('sortDirectionLabel').textContent = sortAscending ? 'Sort Date: Ascending ▲' : 'Sort Date: Descending ▼';
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

        // Render Separated Calendar Grids
        function renderCalendar() {
            const container = document.getElementById('calSeparatedContainer');
            if (!container) return;

            // Collect all months to show: at least Nov 2026 and Dec 2026
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
                                    cellTitle += `: ${exam.subject} (Old Syllabus)`;
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
                            ${item.link ? `<a href="${item.link}" style="color: var(--pastel-sky-foreground); font-weight: 600; font-size: 12px; margin-right: 4px;">PYQs →</a>` : ''}
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
                        <span style="font-size: 12px; font-weight: 600; background: var(--muted); padding: 4px 10px; border-radius: var(--radius-full);">${item.gap}</span>
                        <button class="status-btn ${item.completed ? 'status-btn-done' : 'status-btn-pending'}" onclick="toggleExamDone(${item.id})">
                            ${item.completed ? '✓ Done' : 'Mark Done'}
                        </button>
                    </div>
                </div>
            `).join('');
        }

        function updateStats() {
            const total = schedule.length;
            const completedCount = schedule.filter(s => s.completed).length;
            const regCount = schedule.filter(s => !s.isOld).length;
            const oldCount = schedule.filter(s => s.isOld).length;

            const statTotal = document.getElementById('statTotal');
            if (statTotal) statTotal.textContent = total;

            const statDone = document.getElementById('statDone');
            if (statDone) statDone.textContent = `${completedCount} / ${total}`;

            const statReg = document.getElementById('statRegular');
            if (statReg) statReg.textContent = regCount;

            const statOld = document.getElementById('statOld');
            if (statOld) statOld.textContent = oldCount;

            const statRange = document.getElementById('statRange');
            if (statRange) {
                if (total === 0) {
                    statRange.textContent = '—';
                } else {
                    const first = schedule[0];
                    const last = schedule[schedule.length - 1];
                    statRange.textContent = `${first.date.split(' ').slice(0, 2).join(' ')} – ${last.date}`;
                }
            }

            // Filter button counters
            const fAll = document.getElementById('filterCountAll');
            if (fAll) fAll.textContent = total;
            const fReg = document.getElementById('filterCountReg');
            if (fReg) fReg.textContent = regCount;
            const fOld = document.getElementById('filterCountOld');
            if (fOld) fOld.textContent = oldCount;
            const fDone = document.getElementById('filterCountDone');
            if (fDone) fDone.textContent = completedCount;
        }

        function updateNoticeBar() {
            const noticeBar = document.querySelector('.notice-bar');
            if (!noticeBar) return;

            const regItems = schedule.filter(s => !s.isOld);
            const oldItems = schedule.filter(s => s.isOld);
            const doneCount = schedule.filter(s => s.completed).length;

            const regNames = regItems.map(s => s.shortTag || s.code.replace('CE ', '')).join(', ') || 'None';
            const oldNames = oldItems.map(s => s.shortTag || s.code.replace('CE ', '')).join(', ') || 'None';

            noticeBar.innerHTML = `
                <span><strong>Key:</strong></span>
                <span><span class="badge badge-sky" style="padding: 1px 7px;">Today</span> Current Date</span>
                <span><span class="badge badge-sage" style="padding: 1px 7px;">Regular</span> Normal Syllabus (${regNames})</span>
                <span><span class="badge badge-peach" style="padding: 1px 7px;">Old Syllabus</span> Backlog (${oldNames})</span>
                <span><span class="badge badge-done" style="padding: 1px 7px;">✓ Done</span> Concluded (${doneCount} finished)</span>
                <span style="margin-left: auto; color: var(--muted-foreground);"><i class="icon hgi-stroke hgi-database-01" style="font-size: 13px; vertical-align: middle;"></i> Saved Locally</span>
            `;
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
            updateStats();
            updateNoticeBar();
            initCurrentDateTracker();
        }

        // ----------------------------------------------------
        // EDIT TIMETABLE MODAL ENGINE
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
                // Edit existing
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
                // Add new
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

        renderAll();
    </script>

    <!-- Floating Back to Top Button -->
    <button id="scrollToTopBtn" class="scroll-to-top-btn" aria-label="Scroll to top" title="Scroll to top" onclick="scrollToTop()">
        <i class="hgi-stroke hgi-arrow-up-01"></i>
    </button>

    <!-- MOBILE BOTTOM APP NAVIGATION -->
    <nav class="mobile-bottom-nav" aria-label="Mobile App Navigation">
        <a href="index.html#questions" class="mobile-nav-item" aria-label="Question Bank">
            <i class="mobile-nav-icon hgi-stroke hgi-help-circle"></i>
            <span class="mobile-nav-label">Questions</span>
        </a>
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
    return html

if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent.parent
    out_file = root_dir / "timetable.html"
    content = generate_timetable_html()
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated {out_file} with customizable timetable and local persistence!")
