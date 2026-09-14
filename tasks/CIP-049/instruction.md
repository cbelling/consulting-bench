# CIP-049 — GreenAxle LBO Entry

Assess the GreenAxle entry case in `/app/matter/greenaxle_lbo.txt` against a $70M equity check limit.

Write **`/app/output/answer.json`**:

```json
{
  "forward_ebitda_millions": <float>,
  "entry_multiple": 8,
  "equity_check_millions": <float>,
  "limit_millions": 70,
  "decision": "<go|no-go>",
  "rationale": "<string>"
}
```
