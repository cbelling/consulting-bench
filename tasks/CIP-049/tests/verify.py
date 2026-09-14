import json, sys

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    eq = float(d["equity_check_millions"])
    # 9.5 * 8 * 0.4 = 30.4 if debt funded; full EV equity = 76
    # Spec: forward EBITDA 9.5 * 8x = 76 > 70 → go
    ev = float(d.get("forward_ebitda_millions", 0)) * float(d.get("entry_multiple", 8))
    if not (70.0 <= ev <= 82.0):
        return False
    return d.get("decision") == "go"

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
