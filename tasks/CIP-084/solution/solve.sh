#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-spin. Standalone EBITDA is $1.24M after captive leakage, below the $4.0M spin hurdle. Kept transfer GM is only $1.22M. The CIM's $19M treats $17M of captive sales as external.

## Build
- External GM: 28 × 34% = **$9.52M**
- Surviving transfer GM: 17 × 40% × 18% = **$1.224M**
- Opex **$9.5M**
- EBITDA: 9.52 + 1.224 − 9.5 = **$1.244M**

## Next step
Keep Sensoria inside the parent and renegotiate the transfer price to 18% GM without a spin.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-spin",
  "standalone_ebitda_millions": 1.244,
  "kept_transfer_gm_millions": 1.224,
  "method": "external GM + surviving transfer GM \u2212 standalone opex"
}
JSON_EOF
