import json
import re
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "knowledge_base.json"
)


def tokenize(text):
    return set(re.findall(r"\b[a-zA-Z]{3,}\b", text.lower()))


def retrieve_evidence(question):
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        documents = json.load(file)

    question_words = tokenize(question)
    results = []

    for document in documents:
        content_words = tokenize(
            document["topic"] + " " + document["content"]
        )

        matches = question_words & content_words

        if matches:
            results.append({
                **document,
                "match_count": len(matches)
            })

    results.sort(
        key=lambda item: item["match_count"],
        reverse=True
    )

    return results[:3]
