# CIP-051 — Protein Bar Shelf Price

HopScotch Foods needs the maximum shelf price that preserves contribution per bar while holding **at least 35% market share** in the segment. Use `/app/matter/protein_bar_economics.csv`.

Write **`/app/output/answer.json`**:

```json
{
  "max_price_usd": <float>,
  "min_share_pct": 35,
  "contribution_per_bar_usd": <float>,
  "rationale": "<string>"
}
```
