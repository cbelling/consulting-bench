import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    npv = float(d["npv_millions"])
    if not (-11.0 <= npv <= -8.0):
        return False
    return d.get("decision") == "no-go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
