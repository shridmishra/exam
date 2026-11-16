import json
import compile_data

with open("canonical_data.json", "r", encoding="utf-8") as f:
    canonical_topics = json.load(f)

raw_questions = compile_data.questions

print(f"Loaded {len(canonical_topics)} canonical topics and {len(raw_questions)} raw questions.")
