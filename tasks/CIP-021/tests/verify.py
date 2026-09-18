import re

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
            continue
        return c.lower()
    return chunks[0].lower() if chunks else ""

import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)

    lede_ok = any(w in para for w in ("exit", "wind down", "shut", "leave zone", "recommend exit"))
    contrib = float(ans["true_contribution_per_stop_usd"])
    band_ok = 1.2 <= contrib <= 1.6 and ans.get("decision") == "exit_zone_c"
    method_ok = "redeliver" in memo.lower() and any(
        k in memo.lower() for k in ("density", "stops/hour", "stops per hour", "18")
    )
    next_ok = any(
        k in memo.lower()
        for k in ("reassign", "re-route", "driver", "zone", "contract", "exit plan", "wind-down")
    ) and "monitor risks" not in memo.lower()

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
