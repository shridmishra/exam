#!/usr/bin/env python3
"""
Local Timetable Builder Runner.
Delegates to tools/timetable/build_timetable.py
"""
import subprocess
import sys
from pathlib import Path

script = Path(__file__).resolve().parent / "tools" / "timetable" / "build_timetable.py"
if script.exists():
    result = subprocess.run([sys.executable, str(script)], check=True)
    sys.exit(result.returncode)
else:
    print(f"Error: {script} not found.", file=sys.stderr)
    sys.exit(1)
