import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    ev = float(d["enterprise_value_millions"])
    if not (520.0 <= ev <= 600.0):
        return False
    return d.get("decision") == "go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
