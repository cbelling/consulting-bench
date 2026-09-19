#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go. Unit contribution is $6.82M but field FP cost is $1.48M; after $3.8M opex and $1.2M cannibal, net is $0.34M — below $2.0M. The 0.8% analytical FP is the wrong rate.

## Build
- Unit: 220k × ($48 − $17) = **$6.82M**
- FP: 220k × 3.2% × $210 = **$1.478M**
- Net: 6.82 − 1.478 − 3.8 − 1.2 = **$0.342M**

## Next step
Pause the launch and rerun the field study powered for a ≤1.5% confirmatory rate before SteCo.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "unit_contribution_millions": 6.82,
  "fp_cost_millions": 1.478,
  "net_millions": 0.342,
  "method": "(ASP\u2212COGS)\u00d7tests \u2212 field FP \u2212 opex \u2212 cannibal"
}
JSON_EOF
