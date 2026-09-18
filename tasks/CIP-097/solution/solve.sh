#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend keep_open. Four-wall save is $3.2M but run-rate benefit is only $0.2M after $2.4M stranded leases and $0.6M halo — below the $1.5M close bar. Severance is one-time.

## Build
- Four-wall save: 40 × $80k = **$3.2M**
- Minus leases $2.4M and halo $0.6M → **$0.2M**
- Do not subtract $2.0M severance from run-rate.

## Next step
Keep the 40 boxes and renegotiate the 15 worst leases before any close vote.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "keep_open",
  "four_wall_save_millions": 3.2,
  "runrate_benefit_millions": 0.2,
  "method": "40 \u00d7 loss save \u2212 stranded leases \u2212 halo"
}
JSON_EOF
