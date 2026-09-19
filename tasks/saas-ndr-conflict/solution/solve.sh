#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend failing the growth plan until retention is fixed. Both CS and Finance views miss the 120% NDR hurdle: CS at 112.2% and Finance at 103.8%. Finance also misses the $12M net-ARR-from-existing hurdle by $8.2M.

## NDR bridge with churn-expansion
| View | Churn | Expansion | NDR | Net ARR | vs hurdles |
|------|------:|----------:|----:|--------:|:----------:|
| CS | 8% | 22% | **112.2%** | +$12.2M | NDR FAIL |
| Finance | 12% | 18% | **103.8%** | +$3.8M | BOTH FAIL |

Gap to 120% NDR: 7.8 pts (CS) / 16.2 pts (Finance).

## Next step
Launch a 90-day retention rescue workstream with CS and Finance on unified churn/expansion definitions before approving H2 growth spend.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "fail_fix_retention",
  "cs_ndr_pct": 112.2,
  "finance_ndr_pct": 103.8,
  "method": "NDR bridge with churn-expansion"
}
JSON_EOF
