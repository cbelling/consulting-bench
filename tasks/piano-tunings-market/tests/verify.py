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
        return c.lower()
    return chunks[0].lower() if chunks else ""

import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)
    
    lede_ok = ("9.3" in para or "9.30" in para) and any(
        w in para for w in ("million", "tuning")
    )
    total = float(ans["annual_us_piano_tunings_millions"])
    home = float(ans["home_tunings_millions"])
    inst = float(ans["institutional_tunings_millions"])
    
    band_ok = (
        9.1 <= total <= 9.5
        and 4.6 <= home <= 5.0
        and 4.3 <= inst <= 4.7
    )
    
    method_ok = any(
        k in memo.lower() for k in ("stock", "frequency", "home", "institutional", "segment")
    )
    
    next_ok = any(
        k in memo.lower()
        for k in ("survey", "validate", "technician", "guild", "sample", "verify frequency")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
