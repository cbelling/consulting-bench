#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend implement. Year-1 net is $11.42M after $1.68M small-shipper churn, above the $8M bar. Incremental billed pounds are 31.2M (2.6 lb × 12M), not 81.6M.

## Build
- Increment: 12M × (6.8 − 4.2) = **31.2M lb**
- Revenue: 31.2M × $0.42 = **$13.104M**
- Churn: 3.5% × $48M = **$1.68M**
- Net: **$11.424M**

## Next step
File the dim-weight tariff for the 1st-of-month cycle and stand up a small-shipper rebate desk before go-live.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "implement",
  "year1_net_millions": 11.424,
  "incremental_lb_billions": 0.0312,
  "method": "parcels \u00d7 (dim \u2212 actual) \u00d7 rate \u2212 churn"
}
JSON_EOF
