#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go. EBITDA is $1.58M (7.3% of $21.6M capex), below the 9% hurdle. The developer's $3.56M revenue uses desert yield and 100% offtake.

## Build
- Revenue: 18,000 × 1,450 × $0.11 × 0.88 = **$2.526M**
- Costs: 0.28 + 0.45 + 0.22 = **$0.95M**
- EBITDA: **$1.576M**
- 1.576 / 21.6 = **7.3%** < 9%

## Next step
Send the developer a no-bid and reopen only if capex is ≤ $17.5M or offtake is contracted at 98%.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "ebitda_millions": 1.576,
  "ebitda_over_capex_pct": 7.3,
  "method": "MW \u00d7 kWh/kW \u00d7 price \u00d7 offtake \u2212 O&M \u2212 lease \u2212 interconnection"
}
JSON_EOF
