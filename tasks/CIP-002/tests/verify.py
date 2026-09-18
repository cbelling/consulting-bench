import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    est = float(d["estimate_millions_usd"])
    if not (150.0 <= est <= 230.0):
        return False
    hh = float(d.get("households_millions", 0))
    return 3.0 <= hh <= 4.0

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
