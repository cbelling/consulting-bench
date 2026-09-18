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

    lede_ok = any(w in para for w in ("fail", "fix", "retention", "miss", "below", "not meet"))
    cs = float(ans["cs_ndr_pct"])
    fin = float(ans["finance_ndr_pct"])
    band_ok = (
        110.0 <= cs <= 115.0
        and 102.0 <= fin <= 106.0
        and ans.get("decision") == "fail_fix_retention"
    )
    method_ok = "ndr" in memo.lower() and any(
        k in memo.lower() for k in ("churn", "expansion", "retention")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("retention", "churn", "cs", "customer success", "playbook", "workstream", "rescue")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
