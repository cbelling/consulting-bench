#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend reject. Net is $1.76M after a $1.60M shrink hit on the $80M subset, below the $2.5M accept bar. The $3.36M buyer model ignores shrink; the $8.4M model over-scopes it.

## Build
- GM uplift: $420M × 0.80% = **$3.36M**
- Shrink hit: $80M × 2.0% = **$1.60M**
- Net: **$1.76M**

## Next step
Counter the vendor for 80bps plus shrink-sharing on the $80M subset, or walk.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "reject",
  "gm_uplift_millions": 3.36,
  "shrink_hit_millions": 1.6,
  "net_millions": 1.76,
  "method": "category sales \u00d7 bps \u2212 subset sales \u00d7 extra shrink"
}
JSON_EOF
