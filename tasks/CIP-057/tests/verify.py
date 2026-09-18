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
    checks.append(any(tok in para for tok in ['-0.38', '-0.382', '4.03']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'no-go')
    year1_net_millions = float(ans['year1_net_millions'])
    checks.append(-0.45 <= year1_net_millions <= -0.3)
    cannibal_millions = float(ans['cannibal_millions'])
    checks.append(3.9 <= cannibal_millions <= 4.2)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['cannibal', 'opex']))
    checks.append(any(tok in body for tok in ['heavy', 'step-down', 'arpu']) if True else True)
    checks.append(any(tok in body for tok in ['kill', 'safety-valve', '90-day', 'overage']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
