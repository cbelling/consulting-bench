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

    checks.append(all(tok in para for tok in ['no-go']))
    checks.append(any(tok in para for tok in ['0.34', '0.342', '1.48']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'no-go')
    unit_contribution_millions = float(ans['unit_contribution_millions'])
    checks.append(6.7 <= unit_contribution_millions <= 6.95)
    fp_cost_millions = float(ans['fp_cost_millions'])
    checks.append(1.4 <= fp_cost_millions <= 1.55)
    net_millions = float(ans['net_millions'])
    checks.append(0.28 <= net_millions <= 0.4)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['field', 'cannibal']))
    checks.append(any(tok in body for tok in ['0.8', 'analytical', '3.2']) if True else True)
    checks.append(any(tok in body for tok in ['pause', 'field', 'steco', 'study']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
