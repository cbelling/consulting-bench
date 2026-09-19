#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go. BNPL contribution is $12.6M but year-1 net is $5.4M after credit loss, opex, and $7.2M revolving NII cannibal, below the $8M hurdle. The $61.2M take-rate slide is not profit.

## Build
- Spread: 3.4% − 2.1% − 0.6% = **0.7%**
- Contribution: $1.8B × 0.7% = **$12.6M**
- Cannibal: 18% × $40M = **$7.2M**
- Net: **$5.4M**

## Next step
Hold BNPL and instead raise revolving interchange-plus APR on the same checkout cohort.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "bnpl_contribution_millions": 12.6,
  "year1_net_millions": 5.4,
  "method": "GMV \u00d7 spread \u2212 revolving cannibal"
}
JSON_EOF
