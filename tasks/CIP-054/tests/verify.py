import re

import json, sys

def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\r\n", "\n").strip().split("\n\n") if c.strip()]
    for c in chunks:
        first = c.split("\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        if re.fullmatch(r"[-*_ ]{3,}", first):
            continue
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = ("6840" in para.replace(",", "") or "6,840" in para) and (
        "20" in para or "twenty" in para
    )
    profit = float(ans["weekend_contribution_profit_dollars"])
    band_ok = (
        6820.0 <= profit <= 6860.0
        and ans.get("decision") == "premium_20"
        and int(ans.get("optimal_premium_pct", 0)) == 20
    )
    method_ok = "contribution" in memo.lower() and any(
        k in memo.lower() for k in ("adr", "occupancy", "variable cost")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("pilot", "implement", "roll out", "deploy", "a/b", "test in", "schedule", "sign off")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
