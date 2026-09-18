#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend CVR structure or no-go on RareDx at the $1.2B ask. Bull-case EV is ~$1.37B (go), but bear-case EV is only ~$0.31B after the $80M overhead PV—far below ask.

## Bull-bear DCF with overhead
| Case | rNPV ops | Less overhead PV | EV | vs $1.2B ask |
|------|--------:|-----------------:|---:|:------------:|
| Bull (70% PoS) | $1.45B | $80M | **$1.37B** | GO |
| Bear (25% PoS) | $0.39B | $80M | **$0.31B** | NO-GO |

## Next step
Bring a CVR term sheet to Tuesday IC tying ≥50% of premium above $1.0B to Phase III readout; walk away if management rejects.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "cvr_or_no-go",
  "bull_ev_billions": 1.37,
  "bear_ev_billions": 0.31,
  "method": "bull-bear DCF with overhead"
}
JSON_EOF
