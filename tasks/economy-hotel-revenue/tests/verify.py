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

    checks.append(all(tok in para for tok in ['proceed']))
    checks.append(any(tok in para for tok in ['13.75', '13.8', '13.7']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'proceed')
    economy_room_nights_millions = float(ans['economy_room_nights_millions'])
    checks.append(174.0 <= economy_room_nights_millions <= 179.0)
    economy_room_revenue_billions = float(ans['economy_room_revenue_billions'])
    checks.append(13.5 <= economy_room_revenue_billions <= 14.0)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['occupancy', 'adr']))
    checks.append(any(tok in body for tok in ['midscale', 'str', 'exclu']) if True else True)
    checks.append(any(tok in body for tok in ['ic', 'product', 'thursday', 'approve', 'pilot']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
