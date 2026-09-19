#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend keep_1p. 3P contribution is $32.9M vs 1P $30.72M — only a $2.18M beat, below the $8M flip hurdle. The $33.6M take-rate shortcut is not contribution.

## Build
- 1P: 240 × 28% = 67.2; return drag 240 × 14% × 55% = 18.48; minus $18.0M fulfill → **$30.72M**
- 3P: 240 × 14% = 33.6; plus ads 6.5; minus ops 4.0 and leakage 3.2 → **$32.9M**
- Gap $2.18M < $8M → keep 1P

## Next step
Hold the 3P flip and run a 90-day ads-density test on 1P home-goods instead.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "keep_1p",
  "onep_contribution_millions": 30.72,
  "threep_contribution_millions": 32.9,
  "method": "1P margin after returns/fulfill vs take-rate + ads \u2212 3P costs"
}
JSON_EOF
