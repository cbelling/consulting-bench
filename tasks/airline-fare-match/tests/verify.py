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
    checks.append(any(tok in para for tok in ['130', '53']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'match')
    match_revenue_delta_millions = float(ans['match_revenue_delta_millions'])
    checks.append(-55.0 <= match_revenue_delta_millions <= -50.0)
    no_match_revenue_delta_millions = float(ans['no_match_revenue_delta_millions'])
    checks.append(-186.0 <= no_match_revenue_delta_millions <= -180.0)
    savings_vs_walk_millions = float(ans['savings_vs_walk_millions'])
    checks.append(128.0 <= savings_vs_walk_millions <= 134.0)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['overlap', 'yield']))
    checks.append(any(tok in body for tok in ['18%', 'system']) if True else True)
    checks.append(any(tok in body for tok in ['file', 'weekend', 'overlap', 'hold']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
