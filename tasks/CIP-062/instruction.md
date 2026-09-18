**From:** Thomas Wright, Partner — Government
**To:** Associate case team
**Subject:** Cedar Falls — $5.10/kgal vs $4.5M plant need
**Date:** Tuesday, 8:15 AM

Team,

Cedar Falls proposed $5.10/kgal (from $4.20) on 82,000 accounts. Finance ignored elasticity. Public works ignored treatment-cost savings on lower volume.

Approve the rate if incremental revenue **plus** treatment save ≥ **$4.5M**. Otherwise delay the plant.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<approve|delay>",
  "incremental_revenue_millions": <float>,
  "treatment_save_millions": <float>,
  "total_vs_plant_millions": <float>,
  "method": "<accounts × months × kgal × rate with ε=−0.15>"
}
```

kgal/account/month now = 5.4. New volume = 5.4 × (1 + ε × %ΔP). Treatment save uses $1.10/kgal on the volume decline.
End with a concrete client next step—not generic risk monitoring.

Thomas
