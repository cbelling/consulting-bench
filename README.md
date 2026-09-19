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
harbor run -p tasks/restinn-weekend-pricing -a oracle
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
bash scripts/verify_oracles_local.sh restinn-weekend-pricing hospital-outpatient-gap aerotread-tire-tam
```

CI runs the same oracle check plus `python3 scripts/validate_task_fields.py`.

## Difficulty mix

| Level | Count | What it asks |
|-------|-------|----------------|
| L1 | 5 | Single-exhibit arithmetic with a clear recommendation |
| L2 | 25 | Multi-exhibit math with one distractor number |
| L3 | 20 | Conflicting exhibits, arithmetic traps, or unit/timing issues |

Slugs: [tasks/README.md](tasks/README.md).

Target cheap-model pass rate is about 40–50% (DeepSeek V4.1 Flash).
DeepSeek V4.1 Flash / Modal / terminus-2 scoreboard:

| Set | Run | Pass | Mean | Cost |
|-----|-----|------|------|------|
| Pre-harden (31 stub graders) | Sequential n=1 | 43/50 | 0.86 | $1.04 |
| Pre-harden (31 stub graders) | Concurrent n=20 | 45/50 | 0.90 | $0.93 |
| **Hardened-v1 (all checkable)** | Concurrent n=20 | **26/50** | **0.52** | **$0.73** |

Hardened-v1: 0 errors; all 24 fails still have a passing local oracle.

## Catalog

| Slug | Level | Topic |
|------|-------|-------|
| [aerotread-tire-tam](tasks/aerotread-tire-tam) | L2 | AeroTread NB tire TAM (exclude cargo/spares) |
| [economy-hotel-revenue](tasks/economy-hotel-revenue) | L2 | US economy-hotel room revenue (exclude midscale) |
| [india-smartphone-sellout](tasks/india-smartphone-sellout) | L2 | India smartphone sell-out (exclude gray sell-in) |
| [piano-tunings-market](tasks/piano-tunings-market) | L3 | Piano tunings — unusual stock × frequency |
| [golf-balls-lost](tasks/golf-balls-lost) | L3 | Golf balls lost — conflicting exhibits |
| [hospital-outpatient-gap](tasks/hospital-outpatient-gap) | L3 | Hospital outpatient surgery profit gap |
| [saas-margin-compression](tasks/saas-margin-compression) | L2 | SaaS gross margin compression |
| [hotel-fb-mix](tasks/hotel-fb-mix) | L2 | Hotel F&B profit mix |
| [pharma-plant-oee](tasks/pharma-plant-oee) | L2 | Pharma plant utilization |
| [last-mile-zone-c](tasks/last-mile-zone-c) | L3 | Logistics last-mile Zone C contribution |
| [streaming-contribution](tasks/streaming-contribution) | L3 | Media streaming contribution layers |
| [urgent-care-adjacency](tasks/urgent-care-adjacency) | L3 | Hospital urgent-care adjacency |
| [airline-new-route](tasks/airline-new-route) | L2 | Airline new route |
| [battery-materials-entry](tasks/battery-materials-entry) | L3 | Battery materials entry — conflicting margins |
| [pet-insurance-adjacency](tasks/pet-insurance-adjacency) | L2 | Insurance pet adjacency |
| [marketplace-take-rate](tasks/marketplace-take-rate) | L2 | E-commerce 3P marketplace |
| [coop-dtc-beef](tasks/coop-dtc-beef) | L3 | Ag co-op DTC beef |
| [organic-cpg-acquisition](tasks/organic-cpg-acquisition) | L2 | CPG M&A organic brand |
| [hospital-asc-acquisition](tasks/hospital-asc-acquisition) | L2 | Hospital ASC acquisition |
| [saas-acqui-hire](tasks/saas-acqui-hire) | L2 | SaaS acqui-hire vs build |
| [distressed-store-four-wall](tasks/distressed-store-four-wall) | L3 | Retail distressed-store four-wall |
| [rare-disease-biotech-ev](tasks/rare-disease-biotech-ev) | L3 | Pharma rare-disease biotech EV |
| [airline-bag-fee](tasks/airline-bag-fee) | L3 | Airline bag-fee increase |
| [saas-seat-to-usage](tasks/saas-seat-to-usage) | L2 | SaaS pricing model |
| [restinn-weekend-pricing](tasks/restinn-weekend-pricing) | L1 | RestInn weekend dynamic pricing |
| [pharma-copay-paths](tasks/pharma-copay-paths) | L3 | Pharma co-pay assistance paths |
| [telecom-unlimited-reprice](tasks/telecom-unlimited-reprice) | L2 | Telecom unlimited repricing |
| [dim-weight-pricing](tasks/dim-weight-pricing) | L2 | Logistics dim-weight |
| [municipal-water-rates](tasks/municipal-water-rates) | L3 | Municipal water rates |
| [crunchora-whitespace](tasks/crunchora-whitespace) | L1 | Crunchora CPG distribution white space |
| [airline-loyalty-match](tasks/airline-loyalty-match) | L2 | Airline loyalty growth |
| [saas-ndr-conflict](tasks/saas-ndr-conflict) | L3 | SaaS NDR — CS vs Finance conflict |
| [grocery-fresh-deal](tasks/grocery-fresh-deal) | L2 | Grocery fresh growth |
| [streaming-ad-lite](tasks/streaming-ad-lite) | L3 | Media ad-tier growth |
| [greenpouch-go-nogo](tasks/greenpouch-go-nogo) | L1 | GreenPouch compostable bag go/no-go |
| [auto-feature-subscription](tasks/auto-feature-subscription) | L2 | Auto subscription feature |
| [bank-bnpl-feature](tasks/bank-bnpl-feature) | L2 | Bank BNPL feature |
| [pharma-diagnostic-kit](tasks/pharma-diagnostic-kit) | L3 | Pharma diagnostic kit |
| [industrial-iot-spin](tasks/industrial-iot-spin) | L2 | Industrial IoT spin |
| [retail-media-network](tasks/retail-media-network) | L2 | Retail media network |
| [community-solar-yield](tasks/community-solar-yield) | L3 | Energy community solar |
| [heroco-private-label](tasks/heroco-private-label) | L1 | HeroCo private-label response |
| [airline-fare-match](tasks/airline-fare-match) | L2 | Airline competitive response |
| [saas-freemium-match](tasks/saas-freemium-match) | L2 | SaaS freemium response |
| [ecomm-price-transparency](tasks/ecomm-price-transparency) | L3 | Retail e-comm price transparency |
| [airline-cost-turnaround](tasks/airline-cost-turnaround) | L3 | Airline cost turnaround |
| [retail-store-closures](tasks/retail-store-closures) | L2 | Retail store closures |
| [cloudsaas-path-to-profit](tasks/cloudsaas-path-to-profit) | L1 | CloudSaaS path to profitability |
| [hospital-service-line](tasks/hospital-service-line) | L3 | Hospital service-line turnaround |
| [nonprofit-program-cut](tasks/nonprofit-program-cut) | L2 | Nonprofit turnaround |

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
