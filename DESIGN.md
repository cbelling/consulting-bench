# Management Consulting Bench — Design Brief

**Issue**: COD-53  
**Status**: Design phase (implementation in COD-52)  
**Version**: 1.0

---

## Overview

The Management Consulting Bench evaluates AI agent capabilities in **management consulting workflows**—specifically, the analytical and reasoning patterns used when conducting commercial diligence, preparing investment memos, and synthesizing complex business information for strategic decision-making.

This bench draws architectural inspiration from **Mercor Apex/Harbor** (task isolation, reproducible trials, programmatic verification) and evaluation methodology from **Harvey LAB** (matter-centric document bundles, multi-criteria rubric scoring, all-pass thresholds). Harvey LAB is a legal-domain benchmark; we adopt their **method** (document bundles, rubrics, analyst workflows) while applying it to **management consulting** as the domain.

Unlike query-response benchmarks, this bench tests:
- **Information synthesis** across multi-document datasets
- **Structured reasoning** following domain-specific methodologies
- **Deliverable production** matching professional standards
- **Iterative refinement** patterns (inventory → analyze → challenge → synthesize)

---

## 1. Task Schema

Each task represents a **consulting engagement** or **diligence project**. Tasks are self-contained directories with standardized structure:

```
tasks/
  {task-id}/
    instruction.md          # Engagement brief and deliverable spec
    matter/                 # Source document bundle
      cim.pdf              # Confidential Information Memorandum
      financials.xlsx      # Historical financials
      mgmt-presentation.pdf
      market-report.pdf
      contracts/           # Sample customer contracts
      ...
    reference/             # Optional reference materials
      rubric.json          # Scoring criteria (Harvey-style)
      exemplar.md          # Optional gold-standard deliverable
    env.json               # Task-specific environment config (optional)
    tests/
      verifier.py          # Programmatic scoring logic
```

### Task Metadata (`instruction.md` frontmatter)

```yaml
---
task_id: "consulting-001-saas-diligence"
family: "buy-side-diligence"
domain: "software-saas"
difficulty: "intermediate"
estimated_time_minutes: 180
document_count: 12
document_pages: 87
requires_tools: ["pdf_reader", "spreadsheet", "web_search"]
deliverable_format: "markdown"
---
```

### Instruction Structure

Each `instruction.md` follows this template:

1. **Engagement Context**: Who the client is, what they're evaluating
2. **Objective**: What question needs answering (e.g., "Assess growth sustainability")
3. **Available Materials**: List of documents in `matter/`
4. **Deliverable Specification**: Format, sections, length, tone
5. **Success Criteria**: High-level expectations (detailed rubric in `reference/rubric.json`)

### Design Rationale — Harbor Alignment

This schema mirrors **Mercor Apex/Harbor**:
- **Task directories** are self-contained trial environments
- **`instruction.md`** = Harbor's task specification
- **`matter/`** = environment state (documents instead of web apps)
- **`tests/verifier.py`** = Harbor's programmatic verifier
- **Trial execution** = `start → agent.run(instruction) → verify → teardown`

Key differences:
- Harbor tasks target live web environments; ours use static document bundles
- Harbor emphasizes tool use (browser, terminal); ours emphasizes reasoning and synthesis
- Harbor runs headless; ours may involve multi-step workflows with intermediate artifacts

---

## 2. Scoring (Harvey-Style Rubric with All-Pass)

### Scoring Philosophy

Inspired by **Harvey LAB**, each task uses a **multi-criteria rubric** where:
- Each criterion is **binary** (pass/fail)
- The agent must pass **all criteria** to pass the task
- Criteria cover **substance** (accuracy, completeness) and **form** (structure, professionalism)

This differs from partial-credit benchmarks: professional deliverables must clear multiple quality bars simultaneously. A memo with correct analysis but poor structure, or perfect formatting with factual errors, both fail to meet professional standards.

### Rubric Structure

Rubrics are stored as JSON in `reference/rubric.json`:

```json
{
  "task_id": "consulting-001-saas-diligence",
  "rubric_version": "1.0",
  "all_pass_required": true,
  "criteria": [
    {
      "id": "substance-revenue-analysis",
      "category": "substance",
      "weight": "critical",
      "description": "Correctly identifies revenue growth drivers from financials and CIM",
      "verification": "automated",
      "verifier_function": "check_revenue_metrics"
    },
    {
      "id": "substance-risk-identification",
      "category": "substance",
      "weight": "critical",
      "description": "Identifies at least 3 material risks with evidence citations",
      "verification": "automated",
      "verifier_function": "check_risk_count_and_citations"
    },
    {
      "id": "form-executive-summary",
      "category": "form",
      "weight": "major",
      "description": "Includes executive summary with investment recommendation",
      "verification": "automated",
      "verifier_function": "check_structure_has_exec_summary"
    },
    {
      "id": "form-citation-quality",
      "category": "form",
      "weight": "major",
      "description": "All factual claims cite specific documents with page numbers",
      "verification": "automated",
      "verifier_function": "validate_citations"
    },
    {
      "id": "reasoning-coherence",
      "category": "reasoning",
      "weight": "major",
      "description": "Conclusions follow logically from presented evidence",
      "verification": "llm-as-judge",
      "verifier_function": "assess_logical_coherence"
    }
  ]
}
```

### Verification Methods

1. **Automated checks** (preferred):
   - Structural validation (sections present, length requirements)
   - Entity extraction and fact verification
   - Citation format and referential integrity
   - Quantitative accuracy (calculations, percentages)

2. **LLM-as-judge** (when necessary):
   - Reasoning coherence
   - Tone appropriateness
   - Argumentation quality
   - Used sparingly; prefer deterministic checks

3. **Human review** (fallback):
   - Reserved for ambiguous cases
   - Not part of automated benchmark runs

### Scoring Output

```json
{
  "task_id": "consulting-001-saas-diligence",
  "agent_id": "gpt-4-turbo-2024-04",
  "timestamp": "2026-09-06T16:30:00Z",
  "overall_pass": false,
  "criteria_results": [
    {"id": "substance-revenue-analysis", "pass": true, "evidence": "Found 4/4 key metrics"},
    {"id": "substance-risk-identification", "pass": false, "evidence": "Only 2 risks identified, requires 3"},
    {"id": "form-executive-summary", "pass": true},
    {"id": "form-citation-quality", "pass": true},
    {"id": "reasoning-coherence", "pass": true, "judge_score": 0.87}
  ],
  "execution_time_seconds": 423,
  "token_usage": {"input": 45231, "output": 3421}
}
```

### Connection to Harvey LAB

Harvey's evaluation framework (legal domain) emphasizes methodological principles we adapt:
- **Matter realism**: Complex, multi-document matters with realistic document bundles
- **All-pass rubrics**: Professional work requires meeting all quality standards simultaneously
- **Process fidelity**: Analysts follow multi-step workflows (inventory docs → extract facts → challenge assumptions → synthesize memo)

We adopt Harvey's **evaluation method** (document bundles, rubric structure, workflow patterns) while applying it to **management consulting** as the domain. This is not a multi-practice professional services bench—it focuses on management consulting only.

---

## 3. First Task Family: Buy-Side Diligence Memos

### Task Family Overview

**Domain**: Private equity / growth equity buy-side commercial diligence  
**Deliverable**: Investment committee memo (5–10 pages)  
**Workflow**: Multi-step analyst process with iterative refinement  

### Representative Task: SaaS Company Acquisition

**Scenario** (synthetic placeholder):

> **Client**: MidMarket Growth Partners (PE firm)  
> **Target**: "CloudMetrics Inc." (B2B SaaS analytics platform)  
> **Ask**: Assess commercial attractiveness for $150M Series D / growth equity investment  
> **Materials**: CIM, 3 years financials, product demo deck, 5 customer contracts, market sizing report, competitor analysis  
> **Deliverable**: Investment memo with recommendation (Pass / Pass with conditions / No-go)

**Matter Bundle** (`matter/`):
```
cim-cloudmetrics-2026.pdf               # 32 pages, seller-prepared
financials-2023-2025.xlsx               # Income statement, balance sheet, cash flow
product-overview-deck.pdf               # 18 slides
customer-contracts/                     # 5 sample contracts (anonymized)
  enterprise-contract-1.pdf
  mid-market-contract-1.pdf
  ...
market-report-saas-analytics-2026.pdf   # Third-party market research
competitor-landscape.pdf                # Competitive positioning analysis
cap-table.xlsx                          # Current ownership structure
management-bios.pdf                     # Executive team backgrounds
```

**Deliverable Specification**:

Produce a markdown memo (`deliverable.md`) with these sections:

1. **Executive Summary** (0.5 pages)
   - Investment thesis in 3–4 sentences
   - Recommendation: Pass / Pass with conditions / No-go
   - Key supporting points (3–4 bullets)

2. **Business Overview** (1 page)
   - Product description and value proposition
   - Target customers and go-to-market strategy
   - Competitive positioning

3. **Financial Analysis** (2 pages)
   - Revenue growth trajectory and drivers
   - Unit economics (CAC, LTV, payback period)
   - Profitability and cash flow trends
   - Key metrics (ARR, net retention, gross margins)

4. **Market Opportunity** (1 page)
   - TAM/SAM/SOM sizing
   - Market growth drivers
   - Competitive dynamics

5. **Risk Assessment** (1.5 pages)
   - Customer concentration risk
   - Product/technology risks
   - Market/competitive risks
   - Execution risks
   - Each risk with severity assessment and evidence

6. **Investment Considerations** (1 page)
   - Valuation context (if comparable data available)
   - Key diligence areas for next phase
   - Conditions or mitigants for proceed decision

**Scoring Rubric** (all-pass):
- ✅ Executive summary includes clear recommendation with rationale
- ✅ Revenue growth analysis cites specific figures from financials
- ✅ Unit economics calculations are arithmetically correct
- ✅ Identifies at least 4 material risks with evidence
- ✅ Customer concentration risk explicitly addressed (top 3 customer % from contracts)
- ✅ All factual claims cite source documents with page numbers
- ✅ Sections follow specified structure
- ✅ Memo is 5–10 pages (as markdown word count equivalent)
- ✅ Tone is professional and analytical (LLM judge)

### Analyst Workflow Pattern

Inspired by Harvey LAB's **analyst moves**, the expected process:

1. **Inventory Phase**
   - Catalog available documents
   - Identify information gaps
   - Prioritize review order

2. **Extraction Phase**
   - Pull key financial metrics from Excel
   - Extract claims from CIM (treat as marketing document, verify where possible)
   - Analyze contract terms for red flags
   - Note market sizing assumptions

3. **Challenge Phase**
   - Cross-reference CIM claims against financials
   - Recalculate unit economics from first principles
   - Identify unrealistic assumptions in projections
   - Challenge add-backs or non-recurring items

4. **Synthesis Phase**
   - Build investment narrative
   - Structure memo following template
   - Ensure all claims are cited
   - Draft recommendation with supporting logic

Agents should demonstrate this multi-step reasoning rather than direct-to-memo generation.

### Synthetic Placeholder Principle

**Critical constraint**: All task content must be **synthetic**.

- Do NOT use real company names, financials, or confidential materials
- Do NOT copy Harvard Business School cases or proprietary datasets
- Create plausible but fictional scenarios with realistic complexity
- Use placeholder names: "CloudMetrics Inc.", "MidMarket Growth Partners"
- Generate synthetic financials with realistic patterns (growth rates, margins, burn)

**Example Synthetic Data**:
- Revenue: $12M → $18M → $27M (50% CAGR, plausible for growth SaaS)
- Gross margin: 78% (typical for software)
- Top 3 customers: 18%, 12%, 9% of revenue (concentration risk)
- CAC payback: 14 months (good but requires verification)
- Net retention: 115% (strong, indicates expansion revenue)

### Scope: One Task Family First

For COD-53, we specify **only** the buy-side diligence family. The immediate roadmap focuses on designing, scaffolding, and implementing this **one consulting environment** with a seed task and rubric. Additional task families (if any) are deferred until the first environment is complete and validated.

---

## 4. Non-Goals

### What This Bench Is NOT

1. **Not a query-answering benchmark**
   - Not MMLU-style multiple choice
   - Not single-document QA (e.g., "What was Q3 revenue?")
   - Evaluates synthesis and reasoning, not information retrieval alone

2. **Not a coding benchmark**
   - Agents may use tools (PDF parsing, spreadsheet analysis) but tasks are not programming challenges
   - Not generating or debugging code (that's SWE-Bench, APPS, etc.)

3. **Not a web agent benchmark**
   - Harbor/WebArena evaluate live web navigation and tool use
   - Our tasks use static document bundles (no APIs, no websites to navigate)
   - No state mutations or side effects (read-only environment)

4. **Not Harvey's actual benchmark**
   - Harvey LAB is proprietary and legal-domain specific
   - We adopt their scoring methodology (all-pass rubrics, document bundles, analyst workflows) but not their tasks or content
   - This bench is open-source and **management consulting domain only**—not a multi-practice professional services benchmark

5. **Not rapid-fire scale testing**
   - Tasks take 1–3 hours of agent time (not seconds)
   - Emphasis on quality over quantity (10–50 curated tasks, not thousands)
   - Deep evaluation of reasoning, not statistical sampling

6. **Not end-user application evaluation**
   - This is a research benchmark for model capabilities
   - Not testing deployed assistant UX, latency, or safety guardrails
   - Not customer-facing readiness testing

### Out of Scope for Initial Version

- **Human-in-the-loop workflows**: Tasks assume autonomous completion
- **Multi-turn conversations**: One instruction, one deliverable (no iterative user feedback)
- **Proprietary data**: All content must be synthetic or public-domain
- **Subjective creativity**: Focus on analytical reasoning over creative writing
- **Real-time information**: No web search required; all data in task bundle

---

## 5. Proposed Repo Layout

**Note**: Full scaffold implementation deferred to COD-52. This section proposes structure only.

```
management-consulting-bench/
│
├── README.md                    # Overview, quickstart, links to design doc
├── DESIGN.md                    # This document
├── LICENSE                      # Open-source license (TBD: MIT or Apache 2.0)
│
├── tasks/                       # Task definitions (the benchmark itself)
│   ├── consulting-001-saas-diligence/
│   │   ├── instruction.md
│   │   ├── matter/
│   │   │   ├── cim.pdf
│   │   │   ├── financials.xlsx
│   │   │   └── ...
│   │   ├── reference/
│   │   │   ├── rubric.json
│   │   │   └── exemplar.md      # Optional gold-standard deliverable
│   │   └── tests/
│   │       └── verifier.py
│   │
│   └── families.json            # Task family metadata (initially: buy-side diligence only)
│
├── harness/                     # Execution framework (Harbor-inspired)
│   ├── runner.py                # Trial orchestration: start → run → verify → teardown
│   ├── verifier_base.py         # Base class for verifiers
│   ├── scoring.py               # Rubric evaluation logic
│   ├── llm_judge.py             # LLM-as-judge helpers (for reasoning coherence checks)
│   └── utils/
│       ├── pdf_parser.py
│       ├── spreadsheet_parser.py
│       └── citation_validator.py
│
├── agents/                      # Agent adapters (make any LLM API compatible)
│   ├── base_agent.py            # Abstract agent interface
│   ├── openai_agent.py          # GPT-4, etc.
│   ├── anthropic_agent.py       # Claude
│   ├── local_agent.py           # For open models (vLLM, Ollama)
│   └── registry.py              # Agent configuration and discovery
│
├── docs/                        # Extended documentation
│   ├── task-authoring-guide.md  # How to create new tasks
│   ├── rubric-design.md         # Scoring principles and best practices
│   ├── synthetic-data-guide.md  # Generating realistic placeholder content
│   └── comparison-to-other-benchmarks.md
│
├── scripts/                     # Utilities
│   ├── run_benchmark.py         # Run full benchmark suite
│   ├── run_single_task.py       # Debug individual task
│   ├── validate_task.py         # Lint task structure and rubric
│   └── generate_report.py       # Aggregate results across tasks/agents
│
├── results/                     # Benchmark results (gitignored or separate repo)
│   └── .gitkeep
│
├── examples/                    # Sample outputs and walkthroughs
│   ├── sample-deliverable-pass.md
│   ├── sample-deliverable-fail.md
│   └── annotated-workflow.md    # Demonstrates ideal agent reasoning process
│
├── pyproject.toml               # Python project config (or setup.py)
├── requirements.txt             # Python dependencies
└── .github/
    └── workflows/
        └── ci.yml               # Validate task structure, run tests on new tasks
```

### Key Design Decisions

#### Task Directory Design (Harbor-inspired)
- **Self-contained**: Each task is a complete, hermetically-sealed environment
- **Instruction-driven**: `instruction.md` is the single source of truth for the agent
- **Verifiable**: Programmatic scoring via `tests/verifier.py` (no human loop required for benchmarking)
- **Reproducible**: Static assets (no external API calls, no time-dependent data)

#### Harness Architecture
- **`runner.py`** orchestrates trial lifecycle:
  ```python
  trial = Trial(task_id="consulting-001", agent=gpt4_agent)
  trial.start()              # Load task, prepare environment
  output = trial.run()        # Agent executes instruction → deliverable
  result = trial.verify()     # Run verifier, score rubric
  trial.teardown()           # Cleanup
  ```
- **Verifiers** extend `VerifierBase`:
  ```python
  class ConsultingVerifier(VerifierBase):
      def verify(self, deliverable_path: Path) -> VerificationResult:
          # Load rubric, run automated checks, return pass/fail per criterion
  ```
- **Scoring** aggregates criterion-level results into task-level pass/fail

#### Agent Adapter Pattern
- Abstract interface allows benchmark to run against any LLM or agent framework
- Agent receives `instruction.md` + access to `matter/` directory
- Agent produces `deliverable.md` (or specified format)
- Harness is agnostic to agent internals (prompting strategy, tool use, etc.)

#### Separation of Concerns
- **`tasks/`**: Benchmark content (can evolve independently)
- **`harness/`**: Execution infrastructure (stable API)
- **`agents/`**: Model/framework integrations (community-extensible)

### Comparison to Other Benchmark Repos

| Benchmark | Repo Structure | Task Format | Scoring |
|-----------|---------------|-------------|---------|
| **SWE-Bench** | GitHub issues as tasks | Natural language + repo context | Unit tests pass/fail |
| **GAIA** | JSON task definitions | Q&A pairs | Exact match |
| **WebArena** | Live web environments | Goal descriptions | Programmatic state checks |
| **Harbor** | Task dirs with env specs | `instruction.md` + environment | Verifier scripts |
| **This bench** | Task dirs (Harbor-style) | `instruction.md` + document bundle | Rubric verifier (Harvey-style) |

**Key difference**: We combine Harbor's task isolation model with Harvey's rubric-based scoring, applied to consulting/finance domain.

---

## Implementation Roadmap (Deferred to COD-52)

**COD-53 scope**: Design specification (this document)  
**COD-52 scope**: Repository scaffold and harness implementation

### Sequence: One Environment First

The immediate roadmap focuses on **one consulting environment** (buy-side diligence):

1. **Design** (COD-53, this document) — Task schema, scoring, first family specification
2. **Scaffold** (COD-52, held) — Repository structure, harness, verifier base classes
3. **First environment** (post-COD-52) — Seed task with synthetic documents, complete rubric, automated verifier, test with GPT-4 and Claude

### Scaffold Phases (for reference, not COD-53 deliverable)

1. **Phase 1: Core harness**
   - `runner.py` trial orchestration
   - Base verifier class
   - Rubric JSON schema and scorer
   - Basic agent interface

2. **Phase 2: First seed task**
   - Implement `consulting-001-saas-diligence` fully
   - Synthetic CIM, financials, contracts
   - Complete rubric and automated verifier
   - Test with GPT-4 and Claude

3. **Phase 3: Validation and refinement**
   - Validate rubric effectiveness on first task
   - Tune verifier thresholds based on agent runs
   - Document learnings for future task authoring

4. **Phase 4: Documentation and CI**
   - Task authoring guide (based on first task experience)
   - Benchmark runner scripts
   - CI validation for task format
   - Example results and walkthroughs

**Note**: Additional tasks within buy-side diligence or other consulting domains are deferred until the first environment is complete and validated. Priority is proving the approach works for **one environment** before expanding scope.

---

## Appendix: Influences and Prior Art

### Mercor Apex / Harbor

**Harbor** (https://github.com/harbor-ml) provides a framework for evaluating autonomous agents on web-based tasks:

- **Task specification**: `instruction.md` defines goal; environment provides tools and state
- **Trial lifecycle**: `start` (provision env) → `run` (agent acts) → `verify` (check success) → `teardown` (cleanup)
- **Programmatic verification**: Each task includes a verifier script that checks environment state
- **Tool use emphasis**: Tasks require browser automation, terminal commands, API calls

**SkyRL** (related work) explores RL in simulated environments; Harbor provides the task specification layer.

**Apex** is Mercor's internal benchmark suite; Harbor is the open-source task harness. Many Harbor-compatible tasks are in separate repos (Query Gym for search/QA tasks, etc.).

### Harvey LAB

**Harvey** (https://harvey.ai) builds AI for legal professionals. Their internal evaluation framework (not open-source) emphasizes:

- **Matter-centric design**: Tasks are realistic legal matters (e.g., contract review, due diligence memo)
- **Document bundles**: 10–50 documents per matter (contracts, emails, research memos)
- **Multi-step workflows**: Analysts inventory documents → extract key facts → build fact sheets → challenge assumptions → produce memo
- **Rubric scoring**: Each matter has 10–20 evaluation criteria; agent must pass all (all-pass) to succeed
- **Professional standards**: Deliverables judged against actual attorney work product

**Key insight**: Professional work has high standards on multiple dimensions (accuracy, completeness, structure, tone). Partial credit doesn't reflect real-world acceptance criteria.

### Query Gym

**Query Gym** (Harbor-compatible task set) focuses on search and question-answering tasks. Relevant for methodology (task isolation, verifiers) but different domain (information retrieval vs. synthesis).

### Adaptations for This Bench

- **From Harbor**: Task directory structure, verifier pattern, reproducible trials
- **From Harvey**: Evaluation methodology (all-pass rubrics), multi-document bundles, analyst workflow patterns
- **Method vs. domain**: Harvey LAB is legal-domain; we adopt their **method** and apply it to **management consulting** only
- **Static vs. dynamic**: Document bundles (static) instead of live web environments (Harbor)
- **Single domain focus**: Management consulting only, not a multi-practice professional services bench

---

## Glossary

- **CIM**: Confidential Information Memorandum (seller-prepared marketing document in M&A process)
- **Diligence**: Due diligence process where buyer evaluates target company before investment/acquisition
- **Buy-side**: Investor/acquirer perspective (vs. sell-side = seller/advisor perspective)
- **Rubric**: Evaluation criteria set; each criterion is pass/fail
- **All-pass scoring**: Agent must pass every rubric criterion to pass the task (no partial credit)
- **Matter**: Case or project (legal/consulting term); here, a collection of documents for one engagement
- **Deliverable**: Work product (memo, report, analysis) produced by consultant/analyst
- **Trial**: Single execution of an agent on a task (Harbor terminology)
- **Verifier**: Script that programmatically checks deliverable against rubric
- **Harvey-style**: Referring to Harvey LAB's evaluation philosophy (multi-criteria, all-pass, domain-realistic)
- **Harbor-style**: Referring to Harbor's task structure (instruction, environment, verifier, trial lifecycle)

---

## Questions for Future Resolution

1. **LLM-as-judge calibration**: How to ensure consistent scoring for subjective criteria (reasoning coherence, tone)?
2. **Synthetic data realism**: What level of complexity/realism is sufficient? How to generate at scale?
3. **Task difficulty calibration**: How to establish difficulty levels (junior analyst, senior analyst, principal)?
4. **Tool use vs. reasoning**: Should tasks require agents to use tools (spreadsheet calc) or focus purely on synthesis?
5. **Time limits**: Should tasks have time/token budgets? How to enforce in benchmark runs?
6. **Versioning**: How to version tasks as rubrics/verifiers improve? Retro-apply to old results?

These will be addressed during COD-52 implementation based on empirical testing.

---

**End of Design Brief**
