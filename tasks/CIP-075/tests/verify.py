import json, sys

def first_paragraph(text: str) -> str:
    return text.strip().split("\n\n")[0].lower()

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("no-go", "no go", "do not launch", "decline", "reject"))
    profit = float(ans["incremental_profit_millions_y2"])
    band_ok = -7.0 <= profit <= -5.8 and ans.get("decision") == "no-go"
    method_ok = "contribution" in memo.lower() and "cannibal" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("deprioritize", "kill", "pause", "redirect", "reallocate", "steerco", "sign off", "halt")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
