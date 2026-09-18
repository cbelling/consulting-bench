import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    price = float(d["max_price_usd"])
    if abs(price - 2.79) > 0.05:
        return False
    share = float(d.get("min_share_pct", 35))
    return share >= 35

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
