import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    val = float(d["implied_value_millions"])
    if not (170.0 <= val <= 185.0):
        return False
    return d.get("decision") == "marginal"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
