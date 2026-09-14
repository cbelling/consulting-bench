import json, sys

def close(a, b, tol=2.0):
    return abs(float(a) - float(b)) <= tol

def main():
    with open(sys.argv[1]) as f:
        d = json.load(f)
    return (
        close(d["cm_dollars_y1_millions"], 112)
        and close(d["cm_dollars_y2_millions"], 97)
        and close(d["cm_pct_y1"], 28, 1)
        and close(d["cm_pct_y2"], 22, 1)
    )

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
