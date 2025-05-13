def find_relevant_chunk(question, kb):
    question = question.lower()
    for item in kb:
        if item["location"].lower() in question or item["category"].lower() in question:
            return item["content"]
    return None
