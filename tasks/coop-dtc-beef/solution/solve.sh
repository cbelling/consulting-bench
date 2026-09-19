#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend launch. Sellable retail pounds are 954,800. DTC contribution is $5.89M versus wholesale $3.92M — incremental $1.97M, above $1.5M. Exhibit A's 1.54M live-based pounds are wrong.

## Build
- Hanging: 2.2M × 62% = 1.364M lb
- Retail: 1.364M × 70% = **954,800 lb**
- DTC net $/lb: $8.40 × 0.96 − $1.90 = **$6.164**
- DTC: 954,800 × 6.164 = **$5.885M**
- Wholesale: 954,800 × $4.10 = **$3.915M**

## Next step
Pilot 8,000 boxes through the existing locker network this quarter and lock the $8.40 list.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "launch",
  "retail_lb": 954800.0,
  "dtc_contribution_millions": 5.885,
  "wholesale_contribution_millions": 3.915,
  "method": "live \u00d7 hang \u00d7 retail; DTC net price vs wholesale"
}
JSON_EOF
