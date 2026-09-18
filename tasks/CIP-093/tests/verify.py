def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\r\n", "\n").strip().split("\n\n") if c.strip()]
    for c in chunks:
        first = c.split("\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = "selective" in para and any(
        w in para for w in ("recommend", "choose", "best", "maxim", "prefer")
    )
    gm = float(ans["gross_margin_millions"])
    band_ok = 440.0 <= gm <= 450.0 and ans.get("decision") == "selective_match"
    method_ok = "match" in memo.lower() and any(
        k in memo.lower() for k in ("electronics", "apparel", "gm", "gross margin")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("roll out", "deploy", "electronics", "pricing", "pilot", "implement", "sign off")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
