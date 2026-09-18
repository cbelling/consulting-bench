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

    checks.append(all(tok in para for tok in ['add_shift']))
    checks.append(any(tok in para for tok in ['64.1', '59', '58.9']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'add_shift')
    true_oee_pct = float(ans['true_oee_pct'])
    checks.append(63.5 <= true_oee_pct <= 64.8)
    incremental_weekly_contribution_k = float(ans['incremental_weekly_contribution_k'])
    checks.append(57.5 <= incremental_weekly_contribution_k <= 60.5)
    checks.append(abs(float(ans['incremental_weekly_contribution_k']) - 49.2) > 1e-6)
    checks.append(all(tok in body for tok in ['availability', 'quality']))
    checks.append(any(tok in body for tok in ['performance', 'oee']) if True else True)
    checks.append(any(tok in body for tok in ['roster', 'pilot', 'approve', 'ops']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
