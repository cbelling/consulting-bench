#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend renegotiate_hosting. Recurring GM is 69.0% after stripping the $2.52M one-time migration, and the hosting rate hike is a 2.0pp drag — above the 1.5pp trigger. Support mix is only 1.0pp.

## Bridge
- Reported GM: 1 − 28.56/84 = 66.0%
- Recurring COGS: 28.56 − 2.52 = **$26.04M** → recurring GM **69.0%**
- Hosting drag: 1.68 / 84 = **2.0pp**
- Support mix: 0.84 / 84 = 1.0pp

## Next step
Open the hosting renegotiation workstream this week and bring a 150-bps take-or-pay counter to Friday SteCo.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "renegotiate_hosting",
  "recurring_gm_pct": 69.0,
  "hosting_drag_pp": 2.0,
  "method": "reported COGS minus one-time; hosting hike / revenue"
}
JSON_EOF
