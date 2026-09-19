#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go. Year-1 net is −$0.38M after a $4.03M heavy-user step-down and $3.1M network opex, below the $2.0M hurdle. The $50.4M marketing figure is not incremental.

## Build
- Switchers: 0.28 × 2.4M = 672k; cannibal 672k × ($81 − $75) = **$4.032M**
- New joiners: 90k × $75 = **$6.75M**
- Network opex **$3.1M**
- Net: 6.75 − 4.032 − 3.1 = **−$0.382M**

## Next step
Kill the unlimited SKU and instead cap high-usage overage at a $70 safety-valve plan for a 90-day test.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "year1_net_millions": -0.382,
  "cannibal_millions": 4.032,
  "method": "new joiners \u2212 ARPU step-down \u2212 network opex"
}
JSON_EOF
