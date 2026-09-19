#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend match. Matching cuts overlap yield 8% and costs $53.0M of overlap revenue versus $183.6M if we walk — a $130.6M save, above the $100M bar. Do not apply the cut to 70B system ASMs.

## Build
- Base overlap: 8.5B × $0.12 = **$1,020M**
- Match: 8.5B × 1.03 × $0.12 × 0.92 = $967.0M → **−$53.0M**
- No-match: $1,020M × 0.82 = $836.4M → **−$183.6M**
- Save vs walk: **$130.6M**

## Next step
File the matched fare in the overlap markets this weekend and hold system-wide prices.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "match",
  "match_revenue_delta_millions": -52.968,
  "no_match_revenue_delta_millions": -183.6,
  "savings_vs_walk_millions": 130.632,
  "method": "overlap ASMs \u00d7 RASM; match volume vs walk spill"
}
JSON_EOF
