#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend cut_b. Surplus if we cut Program B is $2.2M, above the $0.5M bar. Unrestricted revenue lost is $1.6M; the $2.4M restricted book leaves with the program and was never deficit fuel.

## Build
- Unrestricted B revenue: 40% × $4.0M = **$1.6M**
- Improvement: $6.2M expenses saved − $1.6M = **$4.6M**
- Surplus: −$2.4M + $4.6M = **+$2.2M**

## Next step
Vote the Program B wind-down at Thursday board and reassign unrestricted donors to Program A.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "cut_b",
  "surplus_if_cut_millions": 2.2,
  "unrestricted_revenue_lost_millions": 1.6,
  "method": "current deficit + expense save \u2212 unrestricted revenue lost"
}
JSON_EOF
