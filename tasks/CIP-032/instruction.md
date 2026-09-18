**From:** Dr. James Park, Partner — Chemicals & Materials
**To:** Associate case team
**Subject:** Chemora US battery materials entry — conflicting economics
**Date:** Monday, 9:45 AM

Team,

Chemora is evaluating entry into US lithium processing for EV batteries. External consultant deck and internal engineering have wildly different margin assumptions, and both may miss the CapEx IRR hurdle. Board wants go/no-go by Wednesday.

Matter pack in `/app/matter/` has three conflicting exhibits on market size, achievable margin, and policy incentives. This is L3—reconcile all views and show whether ANY scenario hits the $150M annual EBITDA hurdle to justify $900M CapEx.

Deliverables by **Wednesday 6 PM**:
1. `/app/output/memo.md` — one-page memo with go/no-go recommendation in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "base_case_annual_ebitda_millions": <float>,
  "with_incentive_annual_ebitda_millions": <float>,
  "hurdle_annual_ebitda_millions": 150.0,
  "method": "<market × share × margin bridge>"
}
```

Show base case and incentive scenarios. Hurdle is firm: ≥$150M annual EBITDA for IRR target on $900M CapEx. End with specific partner/scale recommendation if no-go—not vague optimization.

James
