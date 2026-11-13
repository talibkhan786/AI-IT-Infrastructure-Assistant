import json
from pathlib import Path
from difflib import SequenceMatcher

KB_PATH = Path(__file__).with_name("knowledge_base.json")

def load_kb():
    with KB_PATH.open(encoding="utf-8") as f:
        return json.load(f)

def score(query, entry):
    terms = [entry["title"], entry["symptoms"], " ".join(entry["keywords"])]
    return max(SequenceMatcher(None, query.lower(), text.lower()).ratio() for text in terms)

def find_solution(query, kb):
    ranked = sorted(((score(query, item), item) for item in kb), key=lambda x: x[0], reverse=True)
    return ranked[0] if ranked else (0, None)

def main():
    kb = load_kb()
    print("\nAI IT Infrastructure Assistant — safe troubleshooting demo")
    print("Type a symptom (e.g. 'DNS not working') or 'exit'.\n")
    while True:
        query = input("You: ").strip()
        if query.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not query:
            continue
        confidence, item = find_solution(query, kb)
        if item and confidence >= 0.18:
            print(f"\nSuggested topic: {item['title']}")
            print(f"Summary: {item['summary']}")
            print("Suggested checks:")
            for step in item["steps"]:
                print(f"  - {step}")
            print(f"Escalate if: {item['escalate']}\n")
        else:
            print("\nNo close match found. Add this issue to the knowledge base or escalate to your IT team.\n")

if __name__ == "__main__":
    main()
