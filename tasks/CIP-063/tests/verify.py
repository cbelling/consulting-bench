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

    lede_ok = "distribution" in para and any(
        w in para for w in ("recommend", "first", "priorit", "lead", "sequence")
    )
    inc = float(ans["distribution_incremental_millions"])
    lede_ok = lede_ok and ("48" in para)
    band_ok = 47.5 <= inc <= 48.5 and ans.get("decision") == "distribution_first"
    method_ok = "option" in memo.lower() and "cannibal" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("pilot", "roll out", "retailer", "launch plan", "sign off", "workshop", "field team", "reset")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
