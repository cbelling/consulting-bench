import json
import re
import sys


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

def main() -> bool:
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path, encoding="utf-8").read()
    ans = json.load(open(answer_path, encoding="utf-8"))
    para = first_paragraph(memo)
    body = memo.lower()
    checks = []

    checks.append(all(tok in para for tok in ['match']))
    checks.append(any(tok in para for tok in ['4.38', '4.381', '8.03']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'match')
    match_arr_hit_millions = float(ans['match_arr_hit_millions'])
    checks.append(4.2 <= match_arr_hit_millions <= 4.6)
    hold_arr_hit_millions = float(ans['hold_arr_hit_millions'])
    checks.append(7.8 <= hold_arr_hit_millions <= 8.3)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['downgrade', 'churn']))
    checks.append(any(tok in body for tok in ['conversion', 'free']) if True else True)
    checks.append(any(tok in body for tok in ['ship', 'friday', 'sku', 'cap']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
