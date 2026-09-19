"""Terminal-Bench-style kebab-case slugs for Consulting Bench tasks.

Harbor task folders and `[task].name` suffixes use these written names.
The original CIP-XXX identifiers stay on `[metadata].legacy_id`.
"""

from __future__ import annotations

NAME_PREFIX = "consulting-bench/"

CIP_TO_SLUG: dict[str, str] = {
    "CIP-003": "aerotread-tire-tam",
    "CIP-005": "economy-hotel-revenue",
    "CIP-006": "india-smartphone-sellout",
    "CIP-010": "piano-tunings-market",
    "CIP-012": "golf-balls-lost",
    "CIP-015": "hospital-outpatient-gap",
    "CIP-016": "saas-margin-compression",
    "CIP-018": "hotel-fb-mix",
    "CIP-019": "pharma-plant-oee",
    "CIP-021": "last-mile-zone-c",
    "CIP-025": "streaming-contribution",
    "CIP-028": "urgent-care-adjacency",
    "CIP-030": "airline-new-route",
    "CIP-032": "battery-materials-entry",
    "CIP-033": "pet-insurance-adjacency",
    "CIP-034": "marketplace-take-rate",
    "CIP-038": "coop-dtc-beef",
    "CIP-040": "organic-cpg-acquisition",
    "CIP-041": "hospital-asc-acquisition",
    "CIP-043": "saas-acqui-hire",
    "CIP-044": "distressed-store-four-wall",
    "CIP-050": "rare-disease-biotech-ev",
    "CIP-052": "airline-bag-fee",
    "CIP-053": "saas-seat-to-usage",
    "CIP-054": "restinn-weekend-pricing",
    "CIP-055": "pharma-copay-paths",
    "CIP-057": "telecom-unlimited-reprice",
    "CIP-059": "dim-weight-pricing",
    "CIP-062": "municipal-water-rates",
    "CIP-063": "crunchora-whitespace",
    "CIP-064": "airline-loyalty-match",
    "CIP-066": "saas-ndr-conflict",
    "CIP-067": "grocery-fresh-deal",
    "CIP-070": "streaming-ad-lite",
    "CIP-075": "greenpouch-go-nogo",
    "CIP-076": "auto-feature-subscription",
    "CIP-077": "bank-bnpl-feature",
    "CIP-079": "pharma-diagnostic-kit",
    "CIP-084": "industrial-iot-spin",
    "CIP-085": "retail-media-network",
    "CIP-087": "community-solar-yield",
    "CIP-089": "heroco-private-label",
    "CIP-090": "airline-fare-match",
    "CIP-091": "saas-freemium-match",
    "CIP-093": "ecomm-price-transparency",
    "CIP-096": "airline-cost-turnaround",
    "CIP-097": "retail-store-closures",
    "CIP-098": "cloudsaas-path-to-profit",
    "CIP-099": "hospital-service-line",
    "CIP-100": "nonprofit-program-cut",
}

SLUG_TO_CIP: dict[str, str] = {slug: cip for cip, slug in CIP_TO_SLUG.items()}


def folder_slug(task_id: str) -> str:
    """Return the kebab-case folder name for a CIP id or slug."""
    if task_id in CIP_TO_SLUG:
        return CIP_TO_SLUG[task_id]
    if task_id in SLUG_TO_CIP:
        return task_id
    raise KeyError(f"unknown task id: {task_id}")


def legacy_cip(task_id: str) -> str:
    """Return the original CIP-XXX id for a CIP id or slug."""
    if task_id in CIP_TO_SLUG:
        return task_id
    return SLUG_TO_CIP[task_id]


def harbor_name(task_id: str) -> str:
    return f"{NAME_PREFIX}{folder_slug(task_id)}"
