#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on PawSure standalone pet. Year-2 combined ratio is 107%, above the 92% ceiling, and the launch would still shave $0.43M of HO-rider profit.

## Combined ratio
- Loss 81% + selection 9% + LAE 6% + opex 11% = **107%**
- Cannibalized rider profit: 12% × $3.6M = **$0.432M**
- Reject $60M GWP and the 98% draft that drops selection.

## Next step
Kill the standalone filing and instead reprice the HO pet rider with the 9pp selection load.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "year2_combined_ratio_pct": 107.0,
  "cannibalized_rider_profit_millions": 0.432,
  "method": "(loss + LAE + opex + selection) / GWP"
}
JSON_EOF
