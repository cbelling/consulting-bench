#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend raising the bag fee to $40 only if elasticity is closer to −0.4 with ≤0.5% spill. The optimistic case yields +$39.6M incremental profit; the pessimistic case (−1.0 elasticity, 1.2% spill) loses −$20.4M.

## Bag-fee elasticity and spill model
| Scenario | ε | New bags | Bag Δ profit | Spill cost | Net incremental |
|----------|--:|---------:|-------------:|-----------:|----------------:|
| Optimistic | −0.4 | 6.93M | +$43.6M | $4.0M | **+$39.6M** |
| Pessimistic | −1.0 | 5.33M | −$10.8M | $9.6M | **−$20.4M** |

VC/bag $6; 20M passengers at $40 contribution each.

## Next step
Run a 60-day A/B pricing pilot on three routes to validate ε near −0.4 and spill ≤0.5% before system-wide rollout.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "raise",
  "incremental_profit_millions_optimistic": 39.6,
  "incremental_profit_millions_pessimistic": -20.4,
  "method": "bag-fee elasticity and spill model"
}
JSON_EOF
