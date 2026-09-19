#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend Path B for HelixPharma co-pay assistance. Path B delivers $473M net revenue versus $400M for Path A, driven by broader access volume (11,000 vs 8,000 patients).

## Co-pay net revenue comparison
| Path | Net price | Volume | Net revenue |
|------|----------:|-------:|------------:|
| A | $55 − $5 = $50 | 8,000 | **$400M** |
| B | $48 − $5 = $43 | 11,000 | **$473M** |

Path B wins on access volume (+$73M).

## Next step
Present Path B to the access committee Friday and pre-negotiate payer contracts assuming 11k patient ramp.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "path_b",
  "path_b_net_revenue_millions": 473.0,
  "method": "co-pay net revenue comparison"
}
JSON_EOF
