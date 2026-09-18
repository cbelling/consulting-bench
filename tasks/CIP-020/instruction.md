# CIP-020 — MeshWave SaaS Leak

MeshWave's CAC looks stable, but growth is stalling. Read `/app/matter/meshwave_metrics.txt` and identify the primary leak.

Write **`/app/output/answer.json`**:

```json
{
  "primary_leak": "<churn|cac|pricing|sales_headcount>",
  "monthly_churn_pct": <float>,
  "rationale": "<string>"
}
```
