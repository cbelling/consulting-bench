#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend selective electronics match with apparel non-match for ShopMart. It maximizes gross margin at $445M versus $420M do-nothing and $385M full match.

## Price-match scenario GM comparison
| Strategy | Electronics | Apparel | Gross margin |
|----------|:-----------:|:-------:|-------------:|
| Do nothing | No | No | $420M |
| Full match | Yes | Yes | $385M |
| **Selective match** | Yes | No | **$445M** |

## Next step
Roll out selective electronics price matching nationally by Q4 and hold apparel list prices.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "selective_match",
  "gross_margin_millions": 445.0,
  "method": "price-match scenario GM comparison"
}
JSON_EOF
