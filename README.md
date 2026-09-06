# Management Consulting Bench

A benchmark for evaluating AI agents on **management consulting workflows**—specifically the analytical reasoning, information synthesis, and structured deliverable production used in commercial diligence, investment analysis, and strategic assessment.

## Status

**Design Phase** — Design brief complete (COD-53)  
**Implementation** — Deferred to COD-52

## Overview

This bench evaluates agent capabilities on realistic **management consulting** tasks:

- **Multi-document synthesis**: Analyze 10–50 page document bundles (financial models, market reports, contracts)
- **Structured reasoning**: Follow domain-specific analyst workflows (inventory → extract → challenge → synthesize)
- **Professional deliverables**: Produce investment memos, diligence reports, strategic assessments
- **Rigorous scoring**: Harvey-style all-pass rubrics (agents must meet all quality criteria)

### Methodological Influences

- **Mercor Apex / Harbor**: Task isolation, reproducible trials, programmatic verification
- **Harvey LAB**: Matter-centric document bundles, multi-criteria rubrics, analyst workflow patterns (Harvey is legal-domain; we adopt their **method** for **management consulting**)

### First Task Family

**Buy-side diligence memos** for private equity / growth equity investments:
- Analyze target company materials (CIM, financials, contracts, market research)
- Produce investment committee memo with recommendation
- Scored on analytical accuracy, risk identification, citation quality, professional structure

The immediate roadmap focuses on designing, scaffolding, and implementing this **one consulting environment** with a seed task and rubric before expanding scope.

## Documentation

See [`DESIGN.md`](DESIGN.md) for complete specification:
1. Task schema and directory structure
2. Scoring methodology (Harvey-style rubrics)
3. First task family design (buy-side diligence)
4. Non-goals and scope boundaries
5. Proposed repository layout

## Key Principles

- **Synthetic data only**: All tasks use fictional companies and placeholder content (no proprietary materials)
- **All-pass scoring**: Agents must meet all rubric criteria (professional work has high multi-dimensional standards)
- **Domain realism**: Tasks reflect actual management consulting workflows, not simplified proxies
- **Self-contained tasks**: Each task is a hermetically-sealed directory (instruction + documents + verifier)
- **Management consulting focus**: Single domain (not a multi-practice professional services bench)

## Next Steps

- **COD-52**: Implement repository scaffold, task harness, and first seed task
- **First environment**: Complete buy-side diligence environment (synthetic documents, rubric, verifier) before expanding scope

## License

TBD (MIT or Apache 2.0)

---

**Issue**: [COD-53](https://linear.app/filterab/issue/COD-53/1-design-brief-apex-harvey-shaped-consulting-bench)
