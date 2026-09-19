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

    lede_ok = any(w in para for w in ("no-go", "no go", "do not enter", "not enter", "decline", "unless"))
    at5 = float(ans["system_incremental_millions_at_5pct_cannibal"])
    at15 = float(ans["system_incremental_millions_at_15pct_cannibal"])
    breakeven = float(ans["cannibal_breakeven_pct"])
    band_ok = (
        5.3 <= at5 <= 5.9
        and 1.4 <= at15 <= 2.0
        and 5.7 <= breakeven <= 6.3
        and ans.get("decision") == "no-go"
    )
    method_ok = "cannibal" in memo.lower() and any(
        k in memo.lower() for k in ("urgent", "ed", "clinic", "capture")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("diligence", "diversion", "cannibal", "ed volume", "pilot", "steerage", "land-use")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
