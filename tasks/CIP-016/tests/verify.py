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

    checks.append(all(tok in para for tok in ['renegotiate']))
    checks.append(any(tok in para for tok in ['69', '2.0']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'renegotiate_hosting')
    recurring_gm_pct = float(ans['recurring_gm_pct'])
    checks.append(68.5 <= recurring_gm_pct <= 69.5)
    hosting_drag_pp = float(ans['hosting_drag_pp'])
    checks.append(1.9 <= hosting_drag_pp <= 2.1)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['one-time', 'hosting']))
    checks.append(any(tok in body for tok in ['migration', 'recurring']) if True else True)
    checks.append(any(tok in body for tok in ['renegotiat', 'steco', 'workstream', 'counter']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
