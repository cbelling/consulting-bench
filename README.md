# Consulting Bench

[![Docs](https://img.shields.io/badge/Harbor_docs-000000?style=for-the-badge&logo=mdbook&color=105864)](https://www.harborframework.com/docs)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge)](LICENSE)

[Consulting Bench](https://austinbellinger.com/consulting-bench.html) measures how well agents handle **partner-memo** work in
management consulting: market sizing, profitability, pricing, and investment
decisions. Each task is a partner email to an associate — read a synthetic
matter pack, write a one-page memo, and emit a checkable JSON sidecar.

It runs on [Harbor](https://www.harborframework.com/), the same evaluation
harness used by [Terminal-Bench](https://github.com/harbor-framework/terminal-bench-2-1).
Any Harbor-supported agent (Terminus, Claude Code, Codex, and others) can be
scored with one command.

This release is **50 partner-delegated tasks** (5 L1 / 25 L2 / 20 L3). Verifiers
are programmatic. There is no frozen JSON-L1 holdout set and no separate
design-brief track.

## Links

- Task gallery: [`tasks/`](tasks)
- Harbor task contract: [docs/task-format.md](docs/task-format.md)
- Recorded runs: [`evals/`](evals)

## Getting started

Install [Harbor](https://github.com/harbor-framework/harbor):

```shell
uv tool install harbor
```

or

```shell
pip install harbor
```

Copy [`.env.example`](.env.example) if you are running a model-backed agent.
Oracle checks do not need a model key.

## Run the dataset

From the repo root, run every oracle solution in local Docker containers:

```shell
harbor run -c configs/oracle.yaml
```

Run one task:

```shell
harbor run -p tasks/CIP-054 -a oracle
```

Or a model-backed agent (Terminus-2 + DeepSeek V4.1 Flash):

```shell
export OPENROUTER_API_KEY=<YOUR-KEY>
harbor run -c configs/terminus-2.deepseek-v4.1-flash.yaml
```

A 3-task smoke slice (L1 pricing, L1 P&L, L3 cash EBITDA):

```shell
harbor run -c configs/dry-run.yaml
```

The same jobs can run on Modal sandboxes with `-e modal` after
`uv tool install "harbor[modal]"` and Modal credentials. Helper wrappers for
those recorded jobs live in `scripts/` (`run_dry_run.sh`,
`run_full_bench_concurrent.sh`, `run_hardened_bench_concurrent.sh`).

## Local verification (no Harbor required)

All 50 partner-memo oracles:

```bash
bash scripts/verify_oracles_local.sh
```

A subset or a single task:

```bash
bash scripts/verify_oracles_local.sh CIP-054 CIP-015 CIP-003
```

CI runs the same oracle check plus `python3 scripts/validate_task_fields.py`.

## Difficulty mix

| Level | Count | What it asks |
|-------|-------|----------------|
| L1 | 5 | Single-exhibit arithmetic with a clear recommendation |
| L2 | 25 | Multi-exhibit math with one distractor number |
| L3 | 20 | Conflicting exhibits, arithmetic traps, or unit/timing issues |

IDs: [tasks/README.md](tasks/README.md).

Target cheap-model pass rate is about 40–50% (DeepSeek V4.1 Flash).
DeepSeek V4.1 Flash / Modal / terminus-2 scoreboard:

| Set | Run | Pass | Mean | Cost |
|-----|-----|------|------|------|
| Pre-harden (31 stub graders) | Sequential n=1 | 43/50 | 0.86 | $1.04 |
| Pre-harden (31 stub graders) | Concurrent n=20 | 45/50 | 0.90 | $0.93 |
| **Hardened-v1 (all checkable)** | Concurrent n=20 | **26/50** | **0.52** | **$0.73** |

Hardened-v1: 0 errors; all 24 fails still have a passing local oracle.

## Catalog

| ID | Level | Topic |
|----|-------|-------|
| [CIP-003](tasks/CIP-003) | L2 | AeroTread NB tire TAM (exclude cargo/spares) |
| [CIP-005](tasks/CIP-005) | L2 | US economy-hotel room revenue (exclude midscale) |
| [CIP-006](tasks/CIP-006) | L2 | India smartphone sell-out (exclude gray sell-in) |
| [CIP-010](tasks/CIP-010) | L3 | Piano tunings — unusual stock × frequency |
| [CIP-012](tasks/CIP-012) | L3 | Golf balls lost — conflicting exhibits |
| [CIP-015](tasks/CIP-015) | L3 | Hospital outpatient surgery profit gap |
| [CIP-016](tasks/CIP-016) | L2 | SaaS gross margin compression |
| [CIP-018](tasks/CIP-018) | L2 | Hotel F&B profit mix |
| [CIP-019](tasks/CIP-019) | L2 | Pharma plant utilization |
| [CIP-021](tasks/CIP-021) | L3 | Logistics last-mile Zone C contribution |
| [CIP-025](tasks/CIP-025) | L3 | Media streaming contribution layers |
| [CIP-028](tasks/CIP-028) | L3 | Hospital urgent-care adjacency |
| [CIP-030](tasks/CIP-030) | L2 | Airline new route |
| [CIP-032](tasks/CIP-032) | L3 | Battery materials entry — conflicting margins |
| [CIP-033](tasks/CIP-033) | L2 | Insurance pet adjacency |
| [CIP-034](tasks/CIP-034) | L2 | E-commerce 3P marketplace |
| [CIP-038](tasks/CIP-038) | L3 | Ag co-op DTC beef |
| [CIP-040](tasks/CIP-040) | L2 | CPG M&A organic brand |
| [CIP-041](tasks/CIP-041) | L2 | Hospital ASC acquisition |
| [CIP-043](tasks/CIP-043) | L2 | SaaS acqui-hire vs build |
| [CIP-044](tasks/CIP-044) | L3 | Retail distressed-store four-wall |
| [CIP-050](tasks/CIP-050) | L3 | Pharma rare-disease biotech EV |
| [CIP-052](tasks/CIP-052) | L3 | Airline bag-fee increase |
| [CIP-053](tasks/CIP-053) | L2 | SaaS pricing model |
| [CIP-054](tasks/CIP-054) | L1 | RestInn weekend dynamic pricing |
| [CIP-055](tasks/CIP-055) | L3 | Pharma co-pay assistance paths |
| [CIP-057](tasks/CIP-057) | L2 | Telecom unlimited repricing |
| [CIP-059](tasks/CIP-059) | L2 | Logistics dim-weight |
| [CIP-062](tasks/CIP-062) | L3 | Municipal water rates |
| [CIP-063](tasks/CIP-063) | L1 | Crunchora CPG distribution white space |
| [CIP-064](tasks/CIP-064) | L2 | Airline loyalty growth |
| [CIP-066](tasks/CIP-066) | L3 | SaaS NDR — CS vs Finance conflict |
| [CIP-067](tasks/CIP-067) | L2 | Grocery fresh growth |
| [CIP-070](tasks/CIP-070) | L3 | Media ad-tier growth |
| [CIP-075](tasks/CIP-075) | L1 | GreenPouch compostable bag go/no-go |
| [CIP-076](tasks/CIP-076) | L2 | Auto subscription feature |
| [CIP-077](tasks/CIP-077) | L2 | Bank BNPL feature |
| [CIP-079](tasks/CIP-079) | L3 | Pharma diagnostic kit |
| [CIP-084](tasks/CIP-084) | L2 | Industrial IoT spin |
| [CIP-085](tasks/CIP-085) | L2 | Retail media network |
| [CIP-087](tasks/CIP-087) | L3 | Energy community solar |
| [CIP-089](tasks/CIP-089) | L1 | HeroCo private-label response |
| [CIP-090](tasks/CIP-090) | L2 | Airline competitive response |
| [CIP-091](tasks/CIP-091) | L2 | SaaS freemium response |
| [CIP-093](tasks/CIP-093) | L3 | Retail e-comm price transparency |
| [CIP-096](tasks/CIP-096) | L3 | Airline cost turnaround |
| [CIP-097](tasks/CIP-097) | L2 | Retail store closures |
| [CIP-098](tasks/CIP-098) | L1 | CloudSaaS path to profitability |
| [CIP-099](tasks/CIP-099) | L3 | Hospital service-line turnaround |
| [CIP-100](tasks/CIP-100) | L2 | Nonprofit turnaround |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Task-field checks and oracle smoke
tests run on every pull request.

## Citing Consulting Bench

If you use this benchmark, please cite the repository. GitHub’s cite button
reads [CITATION.cff](CITATION.cff).

```bibtex
@software{consulting_bench_2026,
  title        = {Consulting Bench},
  author       = {{Consulting Bench Authors}},
  year         = {2026},
  url          = {https://github.com/cbelling/consulting-bench}
}
```

## License

Apache-2.0. See [LICENSE](LICENSE).
