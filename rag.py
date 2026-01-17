def load_law_context(issue_type):
    file_map = {
        "Consumer": "data/consumer.txt",
        "Employment": "data/employment.txt",
        "Traffic": "data/traffic.txt",
        "Civil": "data/civil.txt"
    }

    file_path = file_map.get(issue_type, "data/civil.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
