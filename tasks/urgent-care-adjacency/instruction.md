**From:** Dr. Amara Osei, Partner — Healthcare Services
**To:** Associate case team
**Subject:** Lakeside Health — urgent-care adjacency before land-use vote
**Date:** Thursday, 1:00 PM

Team,

Lakeside is weighing **6 urgent-care clinics** in a 1.2M-visit trade area. Marketing assumes **8% capture**; finance sent conflicting ED cannibalization rates (**15%** in the strategy deck vs **5%** in the CFO model). Economics per visit: **$140 net contribution**, **$60 variable cost**, **$2.5M fixed cost per clinic**. Each cannibalized ED visit costs **$400** contribution.

Hurdle: **≥+$5M system incremental profit**. Model both cannibalization assumptions and recommend whether to enter.

Deliverables by **Friday 10 AM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "system_incremental_millions_at_5pct_cannibal": <float>,
  "system_incremental_millions_at_15pct_cannibal": <float>,
  "cannibal_breakeven_pct": <float>,
  "method": "<system contribution with cannibalization>"
}
```

Show both cannibal scenarios. End with a concrete diligence next step on ED diversion rates.

Amara
