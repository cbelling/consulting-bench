#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend cutting S&M by 30% at CloudSaaS. After the FP&A corrections (G&A $15M → $9M run-rate and gross margin true-up to 88%), the S&M-cut path reaches −$0.02M Q4 operating profit (~breakeven) while the R&D-cut path remains at −$1.39M.

## Four-quarter breakeven P&L (Q4 run-rate)
| Scenario | Q4 ARR | Q4 GP | Q4 Opex | Q4 Op profit |
|----------|-------:|------:|--------:|-------------:|
| A — S&M −30%, 5% growth | $84M | $18.48M | $18.50M | **−$0.02M** |
| B — R&D −20%, 10% growth | $88M | $19.36M | $20.75M | −$1.39M |

FP&A noted one correction bundle: duplicate HQ allocation removed from G&A and COGS reclassified (GM 70% → 88% run-rate).

## Next step
Ask the board Tuesday to approve the S&M reduction plan and reforecast hiring to match 5% growth.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "sm_cut",
  "q4_operating_profit_millions": -0.02,
  "method": "four-quarter breakeven P&L"
}
JSON_EOF
