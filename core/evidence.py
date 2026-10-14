def check_evidence(evidence):
    if not evidence:
        return {
            "status": "Insufficient Evidence",
            "answer": (
                "The knowledge base does not contain enough "
                "matching information to answer this question."
            ),
            "sources": []
        }

    sources = [
        {
            "id": item["id"],
            "topic": item["topic"],
            "content": item["content"],
            "source": item["source"],
            "url": item["url"]
        }
        for item in evidence
    ]

    return {
        "status": "Evidence Retrieved",
        "answer": (
            "The following information was retrieved from "
            "the knowledge base. Review the supporting sources "
            "before relying on it."
        ),
        "sources": sources
    }
