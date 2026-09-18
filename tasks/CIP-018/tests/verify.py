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

    checks.append(all(tok in para for tok in ['keep_banquet']))
    checks.append(any(tok in para for tok in ['2.08', '2.075', '-0.28', '-0.275']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'keep_banquet_cut_outlets')
    banquet_true_contribution_millions = float(ans['banquet_true_contribution_millions'])
    checks.append(2.0 <= banquet_true_contribution_millions <= 2.15)
    outlet_true_contribution_millions = float(ans['outlet_true_contribution_millions'])
    checks.append(-0.32 <= outlet_true_contribution_millions <= -0.23)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['kitchen', 'overtime']))
    checks.append(any(tok in body for tok in ['85%', '0.20', '0.2']) if True else True)
    checks.append(any(tok in body for tok in ['close', 'month-end', 'payroll', 'shift']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
