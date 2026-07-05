# ==========================================================
# app.py
# Flask API for RAG Pipeline
# ==========================================================


import os

print("=" * 60)
print("Running file:", __file__)
print("Current working directory:", os.getcwd())
print("=" * 60)

# ==========================================================
# Import Required Libraries
# ==========================================================

import logging

from flask import Flask, request, jsonify
from flask_cors import CORS

# Import the RAG pipeline from rag_pipeline.py
from rag_pipeline import rag_chain


# ==========================================================
# Create Flask App
# ==========================================================

app = Flask(__name__)

# Enable CORS
CORS(app)

# Hide Flask startup logs
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)


# ==========================================================
# Helper Function
# ==========================================================

def clean_qwen_response(response):
    """
    Cleans the generated response.
    """

    if response.startswith("Answer:"):
        response = response.replace("Answer:", "", 1)

    return response.strip()


# ==========================================================
# Home Route
# ==========================================================

@app.route("/")
def home():

    return jsonify({
        "message": "RAG Server Running Successfully!"
    })


# ==========================================================
# RAG API Route
# ==========================================================

@app.route("/rag_query", methods=["POST"])
def rag_query():

    try:

        # Read JSON data
        data = request.get_json()

        if not data:

            return jsonify({
                "error": "No JSON data received."
            }), 400


        question = data.get("question", "").strip()

        if question == "":

            return jsonify({
                "error": "Question cannot be empty."
            }), 400


        # Invoke RAG Pipeline
        result = rag_chain.invoke(question)


        # Clean Answer
        answer = clean_qwen_response(
            result["answer"]
        )


        # Retrieved Context
        sources = []

        for doc in result["context"]:

            sources.append(doc.page_content)


        # Return JSON Response
        return jsonify({

            "question": question,

            "answer": answer,

            "sources": sources

        })


    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================================
# Run Flask App
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🚀 Starting Flask RAG Server...")
    print("Server URL : http://127.0.0.1:5000")
    print("=" * 60)

    print("\nRegistered Routes:")
    for rule in app.url_map.iter_rules():
        print(rule)

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False,
        use_reloader=False
    )