import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if abs(float(d["delta_profit_millions"]) + 86) > 2:
        return False
    fuel_pct = float(d["fuel_share_of_decline_pct"])
    if not (60.0 <= fuel_pct <= 80.0):
        return False
    return "fuel" in d.get("primary_driver", "").lower()

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
