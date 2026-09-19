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

    checks.append(all(tok in para for tok in ['cut_b']))
    checks.append(any(tok in para for tok in ['2.2']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'cut_b')
    surplus_if_cut_millions = float(ans['surplus_if_cut_millions'])
    checks.append(2.1 <= surplus_if_cut_millions <= 2.3)
    unrestricted_revenue_lost_millions = float(ans['unrestricted_revenue_lost_millions'])
    checks.append(1.55 <= unrestricted_revenue_lost_millions <= 1.65)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['restricted', 'unrestricted']))
    checks.append(any(tok in body for tok in ['deficit', 'expense']) if True else True)
    checks.append(any(tok in body for tok in ['vote', 'board', 'wind-down', 'reassign']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
