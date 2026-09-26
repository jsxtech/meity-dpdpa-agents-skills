"""Compliance scoring engine.

Implements the weighted scoring model documented in
`examples/compliance-scoring-engine.md`: per-domain normalised scores (0-100)
combined with statutory-risk weights (summing to 100) into a weighted 0-100
score, mapped to a 5-level maturity band, with risk-adjusted remediation
priorities and critical flags.
"""
from __future__ import annotations
from dataclasses import dataclass, field

# Domain weights (mirror the markdown "Section 2: Domain Weights"); sum = 100
DOMAIN_WEIGHTS: dict[str, int] = {
    "security_safeguards": 18,
    "breach_notification": 12,
    "childrens_data": 12,
    "lawful_basis_consent": 10,
    "data_principal_rights": 9,
    "sdf_obligations": 8,
    "notice_transparency": 7,
    "data_minimisation_retention": 6,
    "vendor_processor": 6,
    "cross_border_transfers": 4,
    "governance_accountability": 4,
    "training_awareness": 2,
    "enforcement_readiness": 2,
}

# Domains where a weak score is flagged Critical regardless of overall score
_CRITICAL_DOMAINS = {"security_safeguards", "breach_notification", "childrens_data"}

_MATURITY = [
    (90, "Optimised"),
    (75, "Managed"),
    (60, "Defined"),
    (30, "Developing"),
    (0, "Initial"),
]


@dataclass
class ScoringResult:
    weighted_score: float
    maturity: str
    critical_flags: list[str] = field(default_factory=list)
    priorities: list[tuple[str, int]] = field(default_factory=list)  # (domain, priority_score)


def maturity_band(score: float) -> str:
    for threshold, label in _MATURITY:
        if score >= threshold:
            return label
    return "Initial"


def score(domain_normalised: dict[str, float]) -> ScoringResult:
    """domain_normalised: {domain_key: 0-100 normalised score}."""
    unknown = set(domain_normalised) - set(DOMAIN_WEIGHTS)
    if unknown:
        raise ValueError(f"unknown domain(s): {sorted(unknown)}")

    weighted = sum(
        domain_normalised.get(d, 0.0) * w for d, w in DOMAIN_WEIGHTS.items()
    ) / 100.0
    weighted = round(weighted, 1)

    critical = [
        d for d in _CRITICAL_DOMAINS
        if domain_normalised.get(d, 0.0) < 50
    ]

    priorities = sorted(
        ((d, int((100 - domain_normalised.get(d, 0.0)) * w))
         for d, w in DOMAIN_WEIGHTS.items()),
        key=lambda t: t[1],
        reverse=True,
    )

    return ScoringResult(
        weighted_score=weighted,
        maturity=maturity_band(weighted),
        critical_flags=critical,
        priorities=priorities,
    )
