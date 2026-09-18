import re

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

import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("no-go", "no go", "do not expand", "reject", "decline"))
    low = float(ans["scenario_c_low_cash_ebitda_margin_pct"])
    high = float(ans["scenario_c_high_cash_ebitda_margin_pct"])
    lede_ok = lede_ok and ("7.5" in para or "7.8" in para)
    band_ok = (
        7.3 <= low <= 7.7
        and 7.6 <= high <= 8.0
        and ans.get("decision") == "no-go"
    )
    method_ok = "ebitda" in memo.lower() and any(
        k in memo.lower() for k in ("accrual", "uncollected", "cash")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("collections", "implant", "audit", "reconcile", "diligence", "receivable", "accrual review")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
