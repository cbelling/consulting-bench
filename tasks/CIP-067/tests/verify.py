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

    checks.append(all(tok in para for tok in ['reject']))
    checks.append(any(tok in para for tok in ['1.76']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'reject')
    gm_uplift_millions = float(ans['gm_uplift_millions'])
    checks.append(3.3 <= gm_uplift_millions <= 3.42)
    shrink_hit_millions = float(ans['shrink_hit_millions'])
    checks.append(1.55 <= shrink_hit_millions <= 1.65)
    net_millions = float(ans['net_millions'])
    checks.append(1.7 <= net_millions <= 1.82)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['shrink', 'bps']))
    checks.append(any(tok in body for tok in ['subset', '80']) if True else True)
    checks.append(any(tok in body for tok in ['counter', 'walk', 'vendor', 'sharing']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
