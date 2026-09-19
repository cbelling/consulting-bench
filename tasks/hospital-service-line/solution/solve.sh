#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend keeping cardiology, closing orthopedics, and pursuing the +$10M expansion. The allocation trap makes cardio look like −$20M allocated, but true contribution is +$15M; ortho true contribution is −$8M.

## True contribution vs allocated P&L
| Service line | Allocated P&L | True contribution | Action |
|--------------|-------------:|------------------:|:------:|
| Cardiology | −$20M | **+$15M** | KEEP |
| Orthopedics | −$35M | **−$8M** | CLOSE |

$50M fixed costs stick regardless. Closing ortho frees +$10M expansion capacity.

## Next step
Wind down orthopedics by Q2 and redeploy OR block time to the cardiology expansion program.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "keep_cardio_close_ortho_expand",
  "cardio_true_contribution_millions": 15.0,
  "ortho_true_contribution_millions": -8.0,
  "method": "true contribution vs allocated P&L"
}
JSON_EOF
