#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend more_cuts. Run-rate profit is $319M, $181M short of the $500M board ask. Strip the $180M hedge loss and add 4% only on the 31% labor share.

## Build
- Labor base: 0.31 × 8.308 = **$2.575B**; +4% = **+$0.103B**
- Run-rate cost: 8.308 − 0.180 + 0.103 = **$8.231B**
- Profit: 8.550 − 8.231 = **$0.319B ($319M)**
- Gap to $500M: **$181M**

## Next step
Bring a $180M non-labor CASM program to Friday SteCo; do not claim the hedge roll-off closes the gap.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "more_cuts",
  "runrate_cost_billions": 8.231,
  "runrate_profit_millions": 319.0,
  "gap_to_500_millions": 181.0,
  "method": "reported cost \u2212 hedge + labor step; vs revenue"
}
JSON_EOF
