import compile_data
from scratch.test_2025_questions import questions_2025

# Read compile_data.py source
with open("compile_data.py", "r", encoding="utf-8") as f:
    src = f.read()

# Replace header comment
src = src.replace(
    "# Derived from 3 examination papers: Nov-Dec 2024, Nov-Dec 2023, Dec 2022",
    "# Derived from 4 examination papers: Nov-Dec 2025, Nov-Dec 2024, Nov-Dec 2023, Dec 2022"
)

# Format questions_2025 as Python code
import pprint

q2025_code = "questions = [\n"
for q in questions_2025:
    q2025_code += f"    {{\n"
    q2025_code += f"        \"id\": {repr(q['id'])},\n"
    q2025_code += f"        \"year\": {repr(q['year'])},\n"
    q2025_code += f"        \"unit\": {q['unit']},\n"
    q2025_code += f"        \"unit_name\": {repr(q['unit_name'])},\n"
    q2025_code += f"        \"q_no\": {repr(q['q_no'])},\n"
    q2025_code += f"        \"marks\": {q['marks']},\n"
    q2025_code += f"        \"type\": {repr(q['type'])},\n"
    q2025_code += f"        \"co\": {repr(q['co'])},\n"
    q2025_code += f"        \"bl\": {repr(q['bl'])},\n"
    q2025_code += f"        \"pi\": {repr(q['pi'])},\n"
    q2025_code += f"        \"topic\": {repr(q['topic'])},\n"
    q2025_code += f"        \"repeated\": {q['repeated']},\n"
    q2025_code += f"        \"rep_frequency\": {repr(q['rep_frequency'])},\n"
    q2025_code += f"        \"question\": r\"\"\"{q['question']}\"\"\",\n"
    q2025_code += f"        \"solution\": r\"\"\"{q['solution']}\"\"\"\n"
    q2025_code += f"    }},\n"

# Replace "questions = [" with the 2025 questions + existing questions
src = src.replace("questions = [\n", q2025_code, 1)

with open("compile_data.py", "w", encoding="utf-8") as f:
    f.write(src)

print("Updated compile_data.py successfully!")
