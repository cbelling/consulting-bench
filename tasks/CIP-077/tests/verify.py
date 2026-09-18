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
    checks.append(any(tok in para for tok in ['5.4', '12.6']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'no-go')
    bnpl_contribution_millions = float(ans['bnpl_contribution_millions'])
    checks.append(12.3 <= bnpl_contribution_millions <= 12.9)
    year1_net_millions = float(ans['year1_net_millions'])
    checks.append(5.2 <= year1_net_millions <= 5.6)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['cannibal', 'loss']))
    checks.append(any(tok in body for tok in ['take-rate', 'spread', 'nii']) if True else True)
    checks.append(any(tok in body for tok in ['hold', 'revolving', 'apr', 'checkout']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
