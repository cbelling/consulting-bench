import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if not (-1.5 <= float(d["value_created_millions"]) <= -0.2):
        return False
    return d.get("decision") == "no-go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
