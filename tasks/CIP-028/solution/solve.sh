#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on Lakeside urgent-care entry unless ED cannibalization stays at or below ~6%. At the CFO's 5% assumption the system yields +$5.76M (passes the $5M hurdle), but at the strategy deck's 15% rate the system delivers only +$1.92M—below the $5M hurdle—and the breakeven cannibalization rate is ~6%.

## System contribution with cannibalization
- Captured visits: 1.2M × 8% = 96,000
- UC profit before cannibal (incl. payer steerage, 6 × $2.5M fixed): **+$7.68M**
- ED contribution lost per cannibalized visit: $400

| Cannibal rate | ED drag | System incremental | vs $5M hurdle |
|--------------|--------:|-------------------:|:-------------:|
| 5% | $1.92M | **+$5.76M** | PASS |
| 15% | $5.76M | **+$1.92M** | FAIL |
| Breakeven | ~6% | +$5.0M | threshold |

## Next step
Commission a two-site ED diversion diligence pilot before the land-use vote to validate cannibalization ≤6%.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "system_incremental_millions_at_5pct_cannibal": 5.76,
  "system_incremental_millions_at_15pct_cannibal": 1.92,
  "cannibal_breakeven_pct": 6.0,
  "method": "system contribution with cannibalization"
}
JSON_EOF
