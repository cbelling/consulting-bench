#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend hold. Gross take from 400 joiners is $21.12M but contribution is $4.02M after traffic, serving, and $8.0M guarantees — below the $7.0M build bar. The $63.36M 1,200-banner TAM is not year 1.

## Build
- Gross take: 400 × $0.24M × 22% = **$21.12M**
- Minus 6.0 + 3.1 + 8.0 = **$17.1M**
- Contribution: **$4.02M**

## Next step
Renegotiate top-10 guarantees below $4M or delay the network until 700 joiners are signed.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "hold",
  "gross_take_millions": 21.12,
  "contribution_millions": 4.02,
  "method": "joiners \u00d7 ad GMV \u00d7 take \u2212 traffic \u2212 serving \u2212 guarantees"
}
JSON_EOF
