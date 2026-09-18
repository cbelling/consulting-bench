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
        return c.lower()
    return chunks[0].lower() if chunks else ""

import json, sys

def main():
    memo_path, answer_path = sys.argv[1], sys.argv[2]
    memo = open(memo_path).read()
    ans = json.load(open(answer_path))
    para = first_paragraph(memo)
    
    lede_ok = any(w in para for w in ("price", "$14", "$15", "content", "cut", "both"))
    var_contrib = float(ans["variable_contribution_per_sub"])
    full_loaded = float(ans["full_loaded_margin_per_sub"])
    
    band_ok = (
        2.8 <= var_contrib <= 3.2
        and -3.0 <= full_loaded <= -2.5
    )
    
    method_ok = all(
        k in memo.lower() for k in ("contribution", "content", "fixed")
    ) and "bridge" in memo.lower()
    
    next_ok = ("price" in memo.lower() or "content" in memo.lower()) and \
              any(k in memo.lower() for k in ("$2", "$14", "$15", "20%", "15%", "18%", "cut $"))

    return lede_ok and band_ok and method_ok and next_ok

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
