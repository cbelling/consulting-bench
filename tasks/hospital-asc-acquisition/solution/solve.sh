#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend walk. Year-2 cash EBITDA is $7.26M (17.3% of $42M EV), just under the 18% bid hurdle, after two surgeon-owners leave and rent is normalized. The $13.1M QoE and $1.4M coding upside are rejected.

## Cash EBITDA
- Leakage: 28% × 11.2 = **$3.136M**
- Rent normalize: **$0.8M**
- Cash EBITDA: 11.2 − 3.136 − 0.8 = **$7.264M**
- 7.264 / 42 = **17.3%** < 18%

## Next step
Walk from $42M and reopen only at EV ≤ $38M with signed employment for at least four of five owners.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "walk",
  "year2_cash_ebitda_millions": 7.264,
  "cash_ebitda_over_ev_pct": 17.3,
  "method": "reported EBITDA \u2212 leakage \u2212 rent-norm; no coding/QoE add-back"
}
JSON_EOF
