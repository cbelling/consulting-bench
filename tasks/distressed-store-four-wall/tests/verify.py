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

    lede_ok = any(w in para for w in ("reject", "renegotiat", "lease", "unless", "no-go", "decline"))
    margin = float(ans["store_b_four_wall_margin_pct"])
    lede_ok = lede_ok and ("56" in para)
    band_ok = -57.0 <= margin <= -55.0 and ans.get("decision") in (
        "reject", "proceed_with_lease_renegotiation"
    )
    method_ok = "four-wall" in memo.lower() or "four wall" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("rent", "lease", "sqft"))
    next_ok = any(
        k in memo.lower()
        for k in ("renegotiat", "lease", "landlord", "rent", "loi", "diligence", "walk away")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
