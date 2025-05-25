import json, os, re

def search_kb(question):
    kb_path = os.path.join("data", "kb.json")
    try:
        with open(kb_path, "r") as f:
            kb = json.load(f)
    except FileNotFoundError:
        return None

    question = re.sub(r"\s+", " ", question.strip().lower())
    for q, ans in kb.items():
        if q.lower() in question:
            return ans
    return None
