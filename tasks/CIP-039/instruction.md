# CIP-039 — HopLite Acquisition

Build a simple EV view from `/app/matter/hoplite_deal.txt` and compare to the seller ask.

Write **`/app/output/answer.json`**:

```json
{
  "enterprise_value_millions": <float>,
  "seller_ask_millions": 400,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
