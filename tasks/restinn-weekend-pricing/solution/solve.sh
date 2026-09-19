#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend the +20% weekend ADR premium for RestInn. It delivers the highest weekend contribution profit ($6,840) versus base ($6,375) and +10% ($6,800) on 100 rooms.

## Contribution margin tree
- Base: 100 rooms × 85% occupancy × ($100 ADR − $25 variable cost) = **$6,375**
- +10% premium: 100 × 80% × ($110 − $25) = **$6,800**
- +20% premium: 100 × 72% × ($120 − $25) = **$6,840** ← optimal

## Next step
Schedule a 6-week A/B test on two comparable properties before portfolio roll-out; Elena to sign off on test design Friday.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "premium_20",
  "optimal_premium_pct": 20,
  "weekend_contribution_profit_dollars": 6840.0,
  "method": "contribution margin tree"
}
JSON_EOF
