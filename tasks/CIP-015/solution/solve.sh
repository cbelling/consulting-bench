#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend no-go on Meridian outpatient surgery expansion. After reconciling the $12M vs $4M implant under-accrual conflict to the true $8M adjustment and applying 8% uncollected receivables ($16M), both capacity scenarios fail the 15% cash EBITDA margin hurdle: C-Low at 7.5% and C-High at 7.8%.

## Cash EBITDA bridge
- Reported EBITDA: $40.0M on $200.0M (20%)
- True implant under-accrual (reconciled): −$8.0M
- Uncollected receivables (8%): −$16.0M
- **Base cash EBITDA: $16.0M (8.0%)**

| Scenario | Revenue | Cash EBITDA | Margin | vs 15% hurdle |
|----------|--------:|------------:|-------:|:-------------:|
| C-Low | $220M | $16.4M | **7.5%** | FAIL |
| C-High | $240M | $18.8M | **7.8%** | FAIL |

## Next step
Commission a 30-day implant accrual and collections diligence workstream with external audit support before revisiting any C-scenario capital request.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "scenario_c_low_cash_ebitda_margin_pct": 7.5,
  "scenario_c_high_cash_ebitda_margin_pct": 7.8,
  "method": "cash EBITDA bridge"
}
JSON_EOF
