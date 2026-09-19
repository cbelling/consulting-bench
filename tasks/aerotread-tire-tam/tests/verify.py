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

    checks.append(all(tok in para for tok in ['go']))
    checks.append(any(tok in para for tok in ['9,600', '9600', '23.04']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'go')
    annual_replacements = float(ans['annual_replacements'])
    checks.append(9500.0 <= annual_replacements <= 9700.0)
    tam_millions = float(ans['tam_millions'])
    checks.append(22.7 <= tam_millions <= 23.4)
    checks.append(abs(float(ans['annual_replacements']) - 11392.0) > 1e-6)
    checks.append(abs(float(ans['annual_replacements']) - 9816.0) > 1e-6)
    checks.append(all(tok in body for tok in ['cycle', 'landing']))
    checks.append(any(tok in body for tok in ['cargo', 'spare', 'exclu']) if True else True)
    checks.append(any(tok in body for tok in ['bid', 'committee', 'procurement', 'submit', 'lock']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
