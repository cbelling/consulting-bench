#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend keep_banquet_cut_outlets. Banquet true contribution is $2.08M, above the $1.8M keep-bar. Outlets are −$0.28M after a fair kitchen split.

## True contribution
- Banquet: 2.80 + 0.75 kitchen add-back − 1.275 fair kitchen (85% of $1.50M) − 0.20 hidden OT = **$2.075M**
- Outlets: −0.80 + 0.75 − 0.225 fair kitchen (15%) = **−$0.275M**
- Reject the GM draft that keeps outlets on the loaded −$0.80M / $2.80M pair.

## Next step
Close the two outlets at month-end, move kitchen allocation to 85/15, and shift $0.20M setup overtime onto the banquet payroll.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "keep_banquet_cut_outlets",
  "banquet_true_contribution_millions": 2.075,
  "outlet_true_contribution_millions": -0.275,
  "method": "dept profit + kitchen add-back \u2212 fair kitchen \u2212 hidden overtime"
}
JSON_EOF
