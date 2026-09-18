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

    checks.append(all(tok in para for tok in ['delay']))
    checks.append(any(tok in para for tok in ['4.10', '4.099', '3.91']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'delay')
    incremental_revenue_millions = float(ans['incremental_revenue_millions'])
    checks.append(3.8 <= incremental_revenue_millions <= 4.05)
    treatment_save_millions = float(ans['treatment_save_millions'])
    checks.append(0.17 <= treatment_save_millions <= 0.21)
    total_vs_plant_millions = float(ans['total_vs_plant_millions'])
    checks.append(3.95 <= total_vs_plant_millions <= 4.2)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['elastic', 'treatment']))
    checks.append(any(tok in body for tok in ['kgal', '4.5']) if True else True)
    checks.append(any(tok in body for tok in ['council', 'delay', '5.25', 'phased']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
