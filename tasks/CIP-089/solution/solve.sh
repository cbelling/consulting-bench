#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend the innovate response to HeroCo's private-label attack. It maximizes operating profit at $39.5M, beating no-response ($36.0M), promo ($26.4M), and full price match ($20.0M).

## Scenario P&L comparison
| Option | Operating profit ($M) |
|--------|----------------------:|
| No response (−20% vol) | 36.0 |
| Match PL price (−25%) | 20.0 |
| Promo (−15% price, −12% vol) | 26.4 |
| **Innovate (+5% price, −5% vol, $8M spend)** | **39.5** |

Private-label defense math: innovate = 0.95M units × ($105 − $55) − $8M = $39.5M.

## Next step
Approve the $8M innovation workstream at Thursday's exec session and assign a GM to ship reformulation by Q3.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "innovate",
  "operating_profit_millions": 39.5,
  "method": "scenario P&L comparison"
}
JSON_EOF
