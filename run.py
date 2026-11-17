#!/usr/bin/env python3
"""
Exam Intelligence & PYQ Platform Launcher.
Usage:
  ./run            (rebuilds if needed, starts server & opens browser)
  ./run 8080       (runs on custom port 8080)
  ./run --no-open  (starts server without launching browser)
"""

import sys
import os
import socket
import webbrowser
import threading
import argparse
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

REPO_ROOT = Path(__file__).resolve().parent

def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    """Checks if a port is actively in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

def find_available_port(start_port: int = 3000, max_attempts: int = 30) -> int:
    """Finds first available port starting from start_port."""
    for port in range(start_port, start_port + max_attempts):
        if not is_port_in_use(port):
            return port
    return start_port

def run_build(subject: str = None) -> bool:
    """Rebuilds active subject dashboard before serving."""
    try:
        from generate_dashboard import build_dashboard_for_subject
        build_dashboard_for_subject(subject_id=subject, write_index=True)
        return True
    except Exception as e:
        print(f"Notice: build check encountered {e}", file=sys.stderr)
        return False

class CustomHandler(SimpleHTTPRequestHandler):
    """Custom request handler with progress API support and clean terminal output."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REPO_ROOT), **kwargs)

    def do_OPTIONS(self):
        if self.path.startswith("/api/"):
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()
        else:
            super().do_OPTIONS()

    def do_GET(self):
        if self.path.startswith("/api/progress"):
            import json
            from core.progress import load_all_progress
            data = load_all_progress()
            payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/progress"):
            import json
            from core.progress import save_subject_progress
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                payload = json.loads(body.decode("utf-8"))
                subject_id = payload.get("subject", "geotech-2")
                completed = payload.get("completed_questions")
                filters = payload.get("filters")
                active_view = payload.get("active_view")
                hide_2023 = payload.get("hide_2023")
                if hide_2023 is None:
                    hide_2023 = payload.get("hide_2022")
                notes = payload.get("notes")
                general_notes = payload.get("general_notes")
                
                updated = save_subject_progress(
                    subject_id=subject_id,
                    completed_questions=completed,
                    filters=filters,
                    active_view=active_view,
                    hide_2023=hide_2023,
                    notes=notes,
                    general_notes=general_notes
                )
                
                resp_data = json.dumps({
                    "success": True,
                    "subject": subject_id,
                    "completed_count": len(updated.get("completed_questions", []))
                }).encode("utf-8")
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(resp_data)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(resp_data)
                return
            except Exception as e:
                err_data = json.dumps({"success": False, "error": str(e)}).encode("utf-8")
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(err_data)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(err_data)
                return
        super().do_POST()
        
    def log_message(self, format, *args):
        # Only log 4xx and 5xx errors to keep the terminal clean
        code = args[1] if len(args) > 1 else ""
        if str(code).startswith(("4", "5")):
            super().log_message(format, *args)

def main():
    parser = argparse.ArgumentParser(description="Exam Platform Local Server")
    parser.add_argument("port", nargs="?", type=int, default=None, help="Port to run on (default: 3000 or next available)")
    parser.add_argument("--no-open", action="store_true", help="Do not open browser automatically")
    parser.add_argument("--no-build", action="store_true", help="Skip rebuilding dashboard")
    parser.add_argument("--subject", default=None, help="Subject to build (default: active subject)")
    args = parser.parse_args()

    os.chdir(str(REPO_ROOT))

    print("\n" + "=" * 60)
    print("  EXAM INTELLIGENCE & PYQ ANALYSIS PLATFORM")
    print("=" * 60)

    if not args.no_build:
        print("Compiling dashboard & verifying question bank...")
        run_build(args.subject)

    preferred_port = args.port or 3000
    port = find_available_port(preferred_port) if args.port is None else args.port

    server_url = f"http://localhost:{port}/"

    print("\nApp is live at:")
    print(f"  * Question Bank:   {server_url}")
    print(f"  * PYQ Checklist:   {server_url}#syllabus")
    print(f"  * Formula Hub:     {server_url}#formulas")
    if (REPO_ROOT / "timetable.html").exists():
        print(f"  * Exam Timetable:  {server_url}timetable.html")
    print("\nPress Ctrl+C to stop the server.\n" + "-" * 60 + "\n")

    if not args.no_open:
        threading.Timer(0.5, lambda: webbrowser.open(server_url)).start()

    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), CustomHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. Have a great study session!")
        sys.exit(0)

if __name__ == "__main__":
    main()
