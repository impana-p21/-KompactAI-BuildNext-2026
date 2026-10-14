from flask import Flask, render_template, request, jsonify
from core.retriever import retrieve_evidence
from core.evidence import check_evidence

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "Please enter a question."
        }), 400

    evidence = retrieve_evidence(question)
    result = check_evidence(evidence)

    return jsonify({
        "question": question,
        "status": result["status"],
        "answer": result["answer"],
        "sources": result["sources"]
    })


if __name__ == "__main__":
    app.run(debug=True)
