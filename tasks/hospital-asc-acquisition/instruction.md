**From:** Amara Osei, Partner — Healthcare Services
**To:** Associate case team
**Subject:** Riverside Health — ASC bid after physician leakage
**Date:** Tuesday, 3:05 PM

Team,

Riverside can buy MetroASC for $42M. Build **year-2 cash EBITDA** after physician-owner leakage and a billing under-code add-back that compliance will not let us keep.

Bid only if year-2 cash EBITDA / EV ≥ **18%**.

The CIM's $11.2M EBITDA is reported, not cash, and assumes all five surgeon-owners stay.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<bid|walk>",
  "year2_cash_ebitda_millions": <float>,
  "cash_ebitda_over_ev_pct": <float>,
  "method": "<reported EBITDA − leakage − disallowed coding + rent-norm>"
}
```

Start from reported EBITDA. Subtract departing-surgeon contribution. Remove the coding add-back compliance disallows. Normalize related-party rent.
End with a concrete client next step—not generic risk monitoring.

Amara
