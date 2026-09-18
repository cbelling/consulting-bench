import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    if abs(float(d["y1_four_wall_roi_pct"]) - 10) > 1:
        return False
    if abs(float(d["y2_four_wall_roi_pct"]) - 5) > 1:
        return False
    if d.get("meets_hurdle") is True:
        return False
    driver = d.get("primary_driver", "").lower()
    return "sales" in driver or "sqft" in driver

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
