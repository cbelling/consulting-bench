#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend distribution expansion first for Crunchora. It yields ~+$48M incremental revenue in 24 months, ahead of a new SKU net +$18M (after 40% cannibalization) and a price move worth only ~+$2M.

## Growth option tree
| Option | Incremental revenue | Notes |
|--------|--------------------:|-------|
| A — Distribution +15% (80% ramp) | **+$48M** | Same velocity, white-space ACV |
| B — New SKU | +$18M net | $30M gross, 40% cannibalized |
| C — Price +3% (ε=−0.8) | ~+$2M | Volume −2.4% |

## Next step
Book a retailer reset workshop with the top-4 accounts in the week of the 18th to lock distribution targets before SKU design spend.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "distribution_first",
  "distribution_incremental_millions": 48.0,
  "method": "growth option tree with cannibalization"
}
JSON_EOF
