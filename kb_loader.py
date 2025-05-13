import json

def load_knowledge_base():
    with open("knowledge_base.json", "r") as f:
        return json.load(f)
