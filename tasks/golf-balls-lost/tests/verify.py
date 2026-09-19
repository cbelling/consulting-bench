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
    
    lede_ok = any(w in para for w in ("920", "900")) and any(
        w in para for w in ("million", "ball")
    )
    total = float(ans["golf_balls_lost_annually_millions"])
    course = float(ans["course_loss_millions"])
    range_c = float(ans["range_consumption_millions"])
    
    band_ok = (
        900 <= total <= 940
        and 340 <= course <= 380
        and 540 <= range_c <= 580
    )
    
    method_ok = any(
        k in memo.lower() for k in ("course", "range", "loss rate", "consumption", "survey")
    ) and "conflict" in memo.lower()
    
    next_ok = any(
        k in memo.lower()
        for k in ("validate", "survey", "diary", "loss rate", "field study", "reconcile")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
