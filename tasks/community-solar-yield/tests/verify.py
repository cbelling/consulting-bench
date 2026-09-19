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
    checks.append(any(tok in para for tok in ['1.58', '1.576', '7.3']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'no-go')
    ebitda_millions = float(ans['ebitda_millions'])
    checks.append(1.52 <= ebitda_millions <= 1.64)
    ebitda_over_capex_pct = float(ans['ebitda_over_capex_pct'])
    checks.append(7.0 <= ebitda_over_capex_pct <= 7.6)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['offtake', 'yield']))
    checks.append(any(tok in body for tok in ['desert', '1450', '1,450']) if True else True)
    checks.append(any(tok in body for tok in ['no-bid', 'capex', '17.5', 'reopen']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
