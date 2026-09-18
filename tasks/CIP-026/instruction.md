# CIP-026 — Chemora Night Shift Decision

Chemora is debating a night production shift. Use **incremental** economics from `/app/matter/chemora_night_shift.csv`. Do **not** allocate fixed plant overhead to the night shift.

Write **`/app/output/answer.json`**:

```json
{
  "incremental_profit_millions": <float>,
  "decision": "<go|no-go|cut_nights>",
  "rationale": "<string>"
}
```
