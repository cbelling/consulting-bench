import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    return 6.0 <= float(d["estimate_millions"]) <= 12.0

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
