#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on GreenPouch. Year-2 incremental operating profit is −$6.4M, well below the $2M hurdle.

## Incremental contribution formula
- Unit contribution: $0.20 premium − $0.12 incremental VC = **$0.08**
- Gross contribution: 20M × $0.08 = **$1.6M**
- Cannibalization: 40% × 20M × $0.50 hero margin = **−$4.0M**
- Launch opex: **−$4.0M**
- **Incremental profit: −$6.4M**

## Next step
Deprioritize GreenPouch at Friday SteCo and redirect packaging R&D budget to the proven hero SKU cost-down initiative.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "incremental_profit_millions_y2": -6.4,
  "method": "incremental contribution formula"
}
JSON_EOF
