#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend walk. Year-3 syn-adjusted ROIC is 10.5%, below the 13% bid hurdle. After-tax confirmed synergies are $6.0M; the banker's $22M revenue synergy is excluded.

## ROIC
- NOPAT: 18.0 × (1 − 0.25) = **$13.5M**
- After-tax syn: 8.0 × 0.75 = **$6.0M**
- After-tax stranded HQ: 1.6 × 0.75 = **$1.2M**
- Numerator: 13.5 + 6.0 − 1.2 = **$18.3M**
- Denominator: 180 + 12 = **$192M**
- ROIC: 18.3 / 192 = **10.47%**

## Next step
Tell the banker we will not mark a bid and reopen only if EV ≤ $145M or confirmed cost syn reach $14M pre-tax.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "walk",
  "year3_roic_pct": 10.47,
  "after_tax_synergies_millions": 6.0,
  "method": "(NOPAT + after-tax syn \u2212 stranded) / (EV + integration cash)"
}
JSON_EOF
