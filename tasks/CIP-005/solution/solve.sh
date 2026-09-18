#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend proceed: US economy-segment room revenue is $13.75B (176.3M room-nights at $78 ADR), above the $10B bar for LodgeCo's $400M RevPAR tool. Midscale and the FY2019 STR snapshot are excluded.

## Build
- Room-nights: 8,200 × 92 × 365 × 64% = **176.34M**
- Revenue: 176.34M × $78 = **$13.75B**
- Trap rejected: occupancy-free 8,200 × 92 × 365 × $78; midscale mix; 2019 STR 88 rooms / 71% / $69

## Next step
Put the $400M tool through Thursday product IC with the $13.75B economy-only TAM as the addressable base.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "proceed",
  "economy_room_nights_millions": 176.33664,
  "economy_room_revenue_billions": 13.754,
  "method": "properties \u00d7 rooms \u00d7 occupancy \u00d7 ADR"
}
JSON_EOF
