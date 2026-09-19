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

    checks.append(all(tok in para for tok in ['walk']))
    checks.append(any(tok in para for tok in ['10.5', '10.47']))
    checks.append("monitor risks" not in body)
    checks.append(str(ans.get('decision', '')).lower() == 'walk')
    year3_roic_pct = float(ans['year3_roic_pct'])
    checks.append(10.2 <= year3_roic_pct <= 10.8)
    after_tax_synergies_millions = float(ans['after_tax_synergies_millions'])
    checks.append(5.8 <= after_tax_synergies_millions <= 6.2)
    # no trap-value rejects
    checks.append(all(tok in body for tok in ['nopat', 'syn']))
    checks.append(any(tok in body for tok in ['banker', 'revenue']) if True else True)
    checks.append(any(tok in body for tok in ['bid', '145', 'banker', 'reopen']))
    return all(checks)

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
