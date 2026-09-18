# CIP-045 — TPA Acquisition Pricing

Review `/app/matter/tpa_deal.txt`. At a $120M purchase price, does the deal clear a 12% IRR hurdle?

Write **`/app/output/answer.json`**:

```json
{
  "irr_pct": <float>,
  "max_price_millions": <float>,
  "offer_price_millions": 120,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
