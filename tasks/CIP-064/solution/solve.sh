#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend reject. True-new members are 0.54M and net ancillary is $2.74M after the $6.2M campaign cost, below the $4.0M hurdle. The $20.8M marketing gross uses duplicates and the base trip rate.

## Build
- True new: 0.90M × 60% = **0.54M**
- Gross ancillary: 0.54M × 0.8 × 1,150 × $0.018 = **$8.942M**
- Net: 8.942 − 6.2 = **$2.742M**

## Next step
Cancel the mass status-match and run a 50k-member controlled match with proof-of-non-member filters.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "reject",
  "true_new_members_millions": 0.54,
  "net_ancillary_millions": 2.742,
  "method": "true-new \u00d7 y1 trips \u00d7 miles \u00d7 ancillary \u2212 cost"
}
JSON_EOF
