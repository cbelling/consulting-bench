import json, sys

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

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = ("s&m" in para or "sm" in para or "sales" in para) and any(
        w in para for w in ("recommend", "cut", "reduce", "choose")
    )
    q4 = float(ans["q4_operating_profit_millions"])
    band_ok = -0.5 <= q4 <= 1.0 and ans.get("decision") in ("sm_cut", "s_m_cut")
    method_ok = "breakeven" in memo.lower() or "break-even" in memo.lower()
    method_ok = method_ok and any(k in memo.lower() for k in ("quarter", "q4", "four-quarter"))
    next_ok = any(
        k in memo.lower()
        for k in ("board", "approve", "sign off", "implement", "reforecast", "headcount", "plan")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
