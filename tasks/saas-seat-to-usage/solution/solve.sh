#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend switch. Year-1 net ARR under usage is $36.71M, just above the $36.0M current book. Grandfathered ARR is $14.4M; the $43.2M deck is not a forecast.

## Build
- Current ARR: 450k × $80 = **$36.0M**
- Grandfather 40%: 0.40 × 36.0 = **$14.4M**
- Converted 60% at $96 with 0.93 volume: 270k × $96 × 0.93 = **$24.11M**
- Minus leakage $1.8M → year-1 net **$36.71M**
- Reject applying elasticity to the grandfathered 40%.

## Next step
Pilot usage on the newest 15% cohort, keep the 40% grandfather, and announce the switch after the first billed month.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "switch",
  "year1_net_arr_millions": 36.706,
  "grandfathered_arr_millions": 14.4,
  "method": "grandfather ARR + converted usage \u00d7 elasticity \u2212 leakage"
}
JSON_EOF
