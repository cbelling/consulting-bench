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

    checks.append(all(tok in para for tok in ['build']))
    checks.append(any(tok in para for tok in ['6.16', '14.9']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'build')
    acqui_hire_cash_24m_millions = float(ans['acqui_hire_cash_24m_millions'])
    checks.append(14.7 <= acqui_hire_cash_24m_millions <= 15.1)
    build_cash_24m_millions = float(ans['build_cash_24m_millions'])
    checks.append(6.0 <= build_cash_24m_millions <= 6.4)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['retention', 'dead-time']))
    checks.append(any(tok in body for tok in ['equity', 'option', 'loi']) if True else True)
    checks.append(any(tok in body for tok in ['requisition', 'withdraw', 'loi', 'friday']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
