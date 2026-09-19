#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend match. The year-1 ARR hit if we match is $4.38M (under the $5.0M cap) versus an $8.03M hit if we hold. 210k × $480 is not a forecast.

## Build
- Match conversion: 210k × 4% × $480 = **+$4.032M**
- Match downgrade: 82k × 9% × $1,140 = **−$8.413M**
- Match hit: **$4.381M**
- Hold extra churn: 82k × 0.7% × 12 × 0.5 × $1,140 = **$3.926M**
- Hold lost logos: 12k × 30% × $1,140 = **$4.104M**
- Hold hit: **$8.030M**

## Next step
Ship the free tier on the existing SKU tree Friday and cap conversion campaigns at the $480 ARPU pack.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "match",
  "match_arr_hit_millions": 4.381,
  "hold_arr_hit_millions": 8.03,
  "method": "free conversion \u2212 paid downgrade vs extra churn + lost logos"
}
JSON_EOF
