import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    return d.get("dominant_driver") == "ticket_and_parts_margin"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
