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

    lede_ok = "cardio" in para and any(
        w in para for w in ("keep", "close", "ortho", "expand")
    )
    cardio = float(ans["cardio_true_contribution_millions"])
    ortho = float(ans["ortho_true_contribution_millions"])
    band_ok = (
        13.0 <= cardio <= 17.0
        and -10.0 <= ortho <= -6.0
        and ans.get("decision") == "keep_cardio_close_ortho_expand"
    )
    method_ok = "allocat" in memo.lower() and "true" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("cardio", "ortho"))
    next_ok = any(
        k in memo.lower()
        for k in ("close", "ortho", "expand", "capacity", "turnaround", "wind-down", "redeploy")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
