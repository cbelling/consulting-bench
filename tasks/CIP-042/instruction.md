# CIP-042 — Cell Tower Portfolio Bid

Value the tower portfolio in `/app/matter/towers_valuation.csv` and compare to a $180M bid.

Write **`/app/output/answer.json`**:

```json
{
  "implied_value_millions": <float>,
  "bid_millions": 180,
  "decision": "<go|no-go|marginal>",
  "rationale": "<string>"
}
```
