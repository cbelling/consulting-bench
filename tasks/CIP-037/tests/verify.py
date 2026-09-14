import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if not (0.1 <= float(d["net_benefit_millions"]) <= 0.35):
        return False
    return d.get("decision") == "no-go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
