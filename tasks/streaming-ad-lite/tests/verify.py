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

    checks.append(all(tok in para for tok in ['hold']))
    checks.append(any(tok in para for tok in ['19.2', '19.19']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'hold')
    net_vs_base_millions = float(ans['net_vs_base_millions'])
    checks.append(18.8 <= net_vs_base_millions <= 19.7)
    ad_revenue_millions = float(ans['ad_revenue_millions'])
    checks.append(80.5 <= ad_revenue_millions <= 82.0)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['churn', 'ad']))
    checks.append(any(tok in body for tok in ['15.99', '12.99']) if True else True)
    checks.append(any(tok in body for tok in ['hold', '13.99', 'region', 'test']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
