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

    lede_ok = "path b" in para or "path_b" in para or (
        "b" in para and any(w in para for w in ("recommend", "prefer", "choose", "select"))
    )
    rev = float(ans["path_b_net_revenue_millions"])
    band_ok = 465.0 <= rev <= 480.0 and ans.get("decision") == "path_b"
    method_ok = "co-pay" in memo.lower() or "copay" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("473", "400", "volume", "access"))
    next_ok = any(
        k in memo.lower()
        for k in ("access committee", "payer", "launch", "contract", "formulary", "sign off")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
