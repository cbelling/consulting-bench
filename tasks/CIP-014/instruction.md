# CIP-014 — LeafMart Contribution Margin

Analyze LeafMart's category P&L in `/app/matter/leafmart_pl.csv`. Quantify contribution margin dollars and rate for Year 1 vs Year 2.

Write **`/app/output/answer.json`**:

```json
{
  "cm_dollars_y1_millions": <float>,
  "cm_dollars_y2_millions": <float>,
  "cm_pct_y1": <float>,
  "cm_pct_y2": <float>,
  "headline": "<string>"
}
```
