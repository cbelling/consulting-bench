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

    lede_ok = "innov" in para and any(
        w in para for w in ("recommend", "choose", "select", "maxim", "best", "win")
    )
    profit = float(ans["operating_profit_millions"])
    lede_ok = lede_ok and ("39.5" in para or "39.50" in para)
    band_ok = 39.2 <= profit <= 39.8 and ans.get("decision") == "innovate"
    method_ok = "p&l" in memo.lower() or "profit" in memo.lower()
    method_ok = method_ok and ("private label" in memo.lower() or "private-label" in memo.lower())
    next_ok = any(
        k in memo.lower()
        for k in ("approve", "fund", "launch", "pilot", "exec session", "sign off", "allocate", "workstream")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
