def first_paragraph(text: str) -> str:
    chunks = [c.strip() for c in text.replace("\r\n", "\n").strip().split("\n\n") if c.strip()]
    for c in chunks:
        first = c.split("\n", 1)[0].strip()
        fl = first.lstrip("*").strip().lower()
        if first.startswith("#"):
            continue
        if fl.startswith(("to:", "from:", "date:", "subject:")):
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("cvr", "no-go", "no go", "walk", "bear", "decline"))
    bull = float(ans["bull_ev_billions"])
    bear = float(ans["bear_ev_billions"])
    band_ok = (
        1.2 <= bull <= 1.5
        and 0.25 <= bear <= 0.35
        and ans.get("decision") in ("cvr_or_no-go", "no-go", "cvr")
    )
    method_ok = any(k in memo.lower() for k in ("dcf", "ev", "rnpv", "valuation"))
    method_ok = method_ok and "overhead" in memo.lower()
    next_ok = any(
        k in memo.lower()
        for k in ("cvr", "ic", "diligence", "phase iii", "readout", "term sheet", "walk away")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
