#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend pass on BOS–LIS. Year-3 contribution is $2.76M after the incentive cliff, below the $4.0M launch hurdle. Year-1 $6.5M incentive and the 8.6¢ reported CASM are not steady-state.

## Year-3 build
- Revenue: 420M ASMs × $0.114 = **$47.88M**
- Cash cost: 420M × $0.101 = **$42.42M**
- Crew premium $1.8M + spill $0.9M
- Contribution: 47.88 − 42.42 − 1.8 − 0.9 = **$2.76M**

## Next step
Decline the slot request this week and keep LIS coverage via the MAD connect instead of a BOS launch.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "pass",
  "year3_contribution_millions": 2.76,
  "incentive_year1_millions": 6.5,
  "method": "RASM \u00d7 ASMs \u2212 cash CASM \u2212 crew premium \u2212 spill"
}
JSON_EOF
