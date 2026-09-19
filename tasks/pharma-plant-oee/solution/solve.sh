#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend add_shift. Saturday true OEE is 64.1% and incremental weekly contribution is $59.0k, above the $42k hurdle. The weekday 71% OEE and the double-counted 88% quality restatement are rejected.

## OEE and contribution
- Availability: 9.0 / 12 = 75.0%
- Performance: 6,480 / (9.0 × 800) = 90.0%
- Quality: 6,156 / 6,480 = 95.0%
- True OEE: 0.75 × 0.90 × 0.95 = **64.125%**
- Saleable kg: 12 × 800 × 0.64125 = **6,156**
- Contribution: 6,156 × $12.50 − $18,000 = **$58,950**

## Next step
Approve the Saturday crew roster at Wednesday ops and lock raw-material inbound for a 6-week pilot.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "add_shift",
  "true_oee_pct": 64.125,
  "incremental_weekly_contribution_k": 58.95,
  "method": "OEE \u00d7 hours \u00d7 rate \u00d7 yield \u00d7 margin \u2212 Saturday labor"
}
JSON_EOF
