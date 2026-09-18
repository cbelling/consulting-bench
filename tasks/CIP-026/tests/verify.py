import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if abs(float(d["incremental_profit_millions"]) + 3) > 0.5:
        return False
    return d.get("decision") in ("cut_nights", "no-go")

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
