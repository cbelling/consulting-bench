**From:** Rachel Kim, Partner — Technology & Analytics
**To:** Associate case team
**Subject:** DataLoop NDR — CS and Finance numbers don't match
**Date:** Monday, 2:00 PM

Team,

DataLoop starts at **$100M ARR**. Customer Success and Finance sent conflicting churn/expansion assumptions in `/app/matter/`. Hurdles: **NDR ≥120%** and **≥$12M net ARR from existing customers**.

Reconcile both views, quantify the gap to each hurdle, and recommend.

Deliverables by **Tuesday 10 AM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<fail_fix_retention|pass>",
  "cs_ndr_pct": <float>,
  "finance_ndr_pct": <float>,
  "method": "<NDR bridge with churn-expansion>"
}
```

Show both CS and Finance NDR math. End with a concrete retention workstream next step.

Rachel
