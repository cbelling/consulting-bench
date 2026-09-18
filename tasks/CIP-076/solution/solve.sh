#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go. Year-1 net is $2.51M after $1.43M cellular and $1.76M premium-trim churn, below the $3.5M hurdle. Gross subscriptions are $5.70M.

## Build
- Gross: 120k × 22% × $18 × 12 = **$5.702M**
- Cellular: 26,400 × $4.50 × 12 = **$1.426M**
- Trim churn: 28,000 × 1.5% × $4,200 = **$1.764M**
- Net: 5.702 − 1.426 − 1.764 = **$2.513M**

## Next step
Bundle the feature into premium trim instead of a stand-alone $18 SKU and re-forecast attach.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "gross_sub_millions": 5.702,
  "year1_net_millions": 2.513,
  "method": "attach \u00d7 price \u2212 cellular \u2212 trim churn"
}
JSON_EOF
