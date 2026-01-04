import json

FILE = "data/memory.json"

def read_memory():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def write_memory(entry):
    data = read_memory()
    data.append(entry)
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
