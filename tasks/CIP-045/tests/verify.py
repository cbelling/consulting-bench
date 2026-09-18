import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if abs(float(d["irr_pct"]) - 7.5) > 1:
        return False
    if abs(float(d["max_price_millions"]) - 75) > 5:
        return False
    return d.get("decision") == "no-go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
