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

    checks.append(all(tok in para for tok in ['keep_1p']))
    checks.append(any(tok in para for tok in ['30.72', '32.9']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'keep_1p')
    onep_contribution_millions = float(ans['onep_contribution_millions'])
    checks.append(30.0 <= onep_contribution_millions <= 31.5)
    threep_contribution_millions = float(ans['threep_contribution_millions'])
    checks.append(32.3 <= threep_contribution_millions <= 33.5)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['return', 'take-rate']))
    checks.append(any(tok in body for tok in ['fulfill', 'leakage', 'ads']) if True else True)
    checks.append(any(tok in body for tok in ['hold', '90-day', 'ads', 'test']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
