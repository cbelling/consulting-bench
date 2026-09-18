#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend hold. Net vs base is $19.2M after 4% ad-lite churn, below the $25M hurdle. Finance's +$31.8M skips churn; product skips $81.3M of remaining ad revenue.

## Build
- Base: 4.2M × $15.99 × 12 = **$805.896M**
- Ad-lite after churn: 1.47M × 96% = 1.4112M
- Ad-lite sub+ad: 1.4112M × ($12.99+$4.80) × 12 = **$301.263M**
- Stay: 2.73M × $15.99 × 12 = **$523.832M**
- New total $825.095M; net vs base **$19.199M**
- Remaining ad revenue: 1.4112M × $4.80 × 12 = **$81.285M**

## Next step
Hold the ad-lite launch and test a $13.99 price with a 2% churn cap in one region.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "hold",
  "net_vs_base_millions": 19.199,
  "ad_revenue_millions": 81.285,
  "method": "mix of prices + ad ARPU \u2212 4% ad-lite churn"
}
JSON_EOF
