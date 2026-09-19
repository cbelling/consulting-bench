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

    checks.append(all(tok in para for tok in ['more_cuts']))
    checks.append(any(tok in para for tok in ['319', '181']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'more_cuts')
    runrate_cost_billions = float(ans['runrate_cost_billions'])
    checks.append(8.21 <= runrate_cost_billions <= 8.25)
    runrate_profit_millions = float(ans['runrate_profit_millions'])
    checks.append(310.0 <= runrate_profit_millions <= 330.0)
    gap_to_500_millions = float(ans['gap_to_500_millions'])
    checks.append(170.0 <= gap_to_500_millions <= 190.0)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['hedge', 'labor']))
    checks.append(any(tok in body for tok in ['one-time', '31%']) if True else True)
    checks.append(any(tok in body for tok in ['steco', 'casm', '180', 'friday']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
