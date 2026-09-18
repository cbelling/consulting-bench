#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend rejecting the CornerMart package unless Store B's lease is renegotiated. Store A four-wall margin is ~10% (acceptable at broker $360/sqft vs our $280/sqft internal value), but Store B four-wall margin is −56% due to rent 38% above market—despite the broker teaser claiming both stores are cash-flow positive.

## Four-wall profitability analysis
| Store | Rent/sqft | Sales | Four-wall margin | Assessment |
|-------|----------:|------:|-----------------:|:----------:|
| A | $42 | $4.2M | **+10.2%** | OK with caution |
| B | $58 | $2.4M | **−56.0%** | FAIL |

Broker $360/sqft vs internal $280/sqft — proceed only if Store B rent resets to ≤$42/sqft.

## Next step
Reject the LOI deadline package unless the landlord agrees to renegotiate Store B to market rent within 30 days.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "proceed_with_lease_renegotiation",
  "store_b_four_wall_margin_pct": -56.0,
  "method": "four-wall profitability analysis"
}
JSON_EOF
