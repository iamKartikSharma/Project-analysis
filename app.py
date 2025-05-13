from flask import Flask, request, jsonify
from kb_loader import load_knowledge_base
from utils import find_relevant_chunk

app = Flask(__name__)
kb = load_knowledge_base()

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    result = find_relevant_chunk(question, kb)
    if result:
        return jsonify({"response": result})
    else:
        return jsonify({"response": "Sorry, I couldn't find that info."})

if __name__ == "__main__":
    app.run(debug=True)
