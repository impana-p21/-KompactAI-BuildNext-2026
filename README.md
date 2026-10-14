# -KompactAI-BuildNext-2026
Build Next 2026 AI Hackathon Project
🩺 MedProof AI — Build Next 2026

Evidence-Grounded Medical Information Assistant

MedProof AI is an AI-ready application designed to make medical information retrieval more transparent by presenting supporting evidence and source references.

🎯 Problem Statement

AI systems can generate misleading information when answers lack reliable supporting evidence. Users need a way to identify the sources behind information and recognize when available evidence is insufficient.

💡 Proposed Solution

MedProof AI retrieves relevant information from a curated knowledge base and displays supporting passages with their source references. When no relevant information is available, the application communicates that limitation instead of inventing an answer.

✨ Key Features

* 🔎 Evidence Retrieval: Finds relevant information from a curated knowledge base.
* 📚 Source Transparency: Displays supporting passages and source references.
* 🛡️ Evidence Awareness: Identifies when matching information is unavailable.
* 📋 Traceability: Associates retrieved information with document identifiers.
* 💻 Interactive Interface: Provides a simple, responsive web application.
* 🔌 Modular Architecture: Designed to support future AI inference integration.

🛠️ Technology Stack

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* JSON

⚙️ How It Works

1. The user submits a question.
2. The backend processes the question.
3. The retrieval module searches the knowledge base.
4. Relevant information and source references are collected.
5. The application displays the retrieved evidence.
6. If no matching evidence is found, the application reports that limitation.

🏗️ Project Architecture

KompactAI-BuildNext-2026/
├── app.py
├── requirements.txt
├── core/
│   ├── __init__.py
│   ├── retriever.py
│   └── evidence.py
├── data/
│   └── knowledge_base.json
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js

🚀 Getting Started

Prerequisites

* Python 3.10 or later
* pip

Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/KompactAI-BuildNext-2026.git

Navigate to the project directory:

cd KompactAI-BuildNext-2026

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open the local address displayed in your terminal to access the application.

🧠 Kompact AI Runtime Integration

The project is designed with a modular architecture to support potential integration with the Kompact AI Runtime.

Future development may explore AI-powered answer generation, improved retrieval, inference efficiency, and deployment security.

Runtime integration will depend on access to the official runtime and its documentation. The current prototype does not claim to use Kompact inference.

🔮 Future Enhancements

* Semantic search using embeddings
* Retrieval-Augmented Generation (RAG)
* AI-generated answers grounded in retrieved evidence
* Improved source validation
* Automated evaluation of answer relevance and evidence quality
* Performance benchmarking
* Kompact AI Runtime integration, subject to availability
* Enhanced privacy and security controls

🔐 Responsible AI

MedProof AI aims to improve transparency by showing retrieved information and its sources.

Source retrieval alone does not guarantee that information is correct or that a question has been answered completely. Further validation and evaluation are required.

⚠️ Disclaimer

This project is an educational prototype for general medical information. It is not intended to diagnose diseases, prescribe treatments, or replace qualified medical professionals.

👩‍💻 Hackathon

Developed as a project for Build Next 2026 — powered by Kompact AI, a national-level AI challenge organized by ZIROH LABS.

⸻

Project Status: Prototype under development.
