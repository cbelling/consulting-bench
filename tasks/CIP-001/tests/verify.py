import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    est = float(d["estimate_millions"])
    return 32.0 <= est <= 48.0

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
