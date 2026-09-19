#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend exiting Zone C after sizing true contribution. Zone C delivers only $1.40/stop after redelivery, below the $1.50 hurdle—despite headline $5.20/stop revenue that ignores failed-first-attempt costs and actual 18 stops/hour density.

## Contribution per stop after redelivery
- Revenue/stop: $5.20
- Driver cost: $36/hr ÷ 18 stops/hr = $2.00/stop
- Redelivery (35% × $4.00): $1.40/stop
- **True contribution: $5.20 − $2.00 − $1.40 = $1.40/stop** (FAIL vs $1.50 hurdle)

## Next step
Reassign Zone C routes to adjacent Zone A density corridors by month-end and notify the anchor shipper of 60-day wind-down.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "exit_zone_c",
  "true_contribution_per_stop_usd": 1.4,
  "method": "contribution per stop after redelivery"
}
JSON_EOF
