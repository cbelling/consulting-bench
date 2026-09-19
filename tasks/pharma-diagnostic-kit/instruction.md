**From:** Priya Nair, Partner — Healthcare & Life Sciences
**To:** Associate case team
**Subject:** HelixDx kit — field FP cost vs $2M hurdle
**Date:** Wednesday, 11:20 AM

Team,

HelixDx wants to launch a kit (220k tests). Lab quotes a 0.8% **analytical** false-positive rate. Field follow-up runs at **3.2%**. Each FP follow-up costs $210.

Launch only if contribution after FP, launch opex, and cannibal ≥ **$2.0M**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|no-go>",
  "unit_contribution_millions": <float>,
  "fp_cost_millions": <float>,
  "net_millions": <float>,
  "method": "<(ASP−COGS)×tests − field FP − opex − cannibal>"
}
```

Use 3.2% field FP, not 0.8% analytical. Cannibal $1.2M. Launch opex $3.8M.
End with a concrete client next step—not generic risk monitoring.

Priya
