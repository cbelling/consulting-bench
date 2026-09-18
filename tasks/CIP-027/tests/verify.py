import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if abs(float(d["y3_operating_profit_millions"]) - 3) > 1:
        return False
    return d.get("decision") == "no-go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
