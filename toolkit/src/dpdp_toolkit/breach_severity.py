"""Breach severity engine.

Implements the ruleset documented in
`examples/breach-severity-decision-engine.md` (Rule 7(3) framework).
Given breach attributes, returns a severity score, tier (S1-S4), and the
DPBI / Data Principal / CERT-In notification decisions.
"""
from __future__ import annotations
from dataclasses import dataclass

# Point tables (mirror the markdown "Step 2: Severity Scoring")
_DATA_CATEGORY = {
    "biometric": 3, "health": 3, "children": 3, "special": 3,
    "financial": 2, "basic": 1,
}
_VOLUME = {">1M": 3, "100k-1M": 2, "1k-100k": 1, "<1k": 0}
_ENCRYPTION = {"plaintext": 2, "encrypted_keys_exposed": 1, "encrypted_keys_safe": 0}
_HARM = {"high": 3, "medium": 2, "low": 1, "none": 0}
_SENSITIVE = {"health", "biometric", "children", "special", "financial"}


@dataclass
class BreachInput:
    data_categories: str            # highest applicable category
    volume: str                     # one of _VOLUME keys
    encryption_state: str           # one of _ENCRYPTION keys
    harm_likelihood: str            # one of _HARM keys
    children_involved: bool = False
    cross_border: bool = False


@dataclass
class BreachResult:
    score: int
    tier: str                       # S1 | S2 | S3 | S4
    label: str
    notify_dpbi: bool
    dpbi_timeline_hours: int
    notify_data_principals: bool
    dp_rationale: str


def _tier(score: int) -> tuple[str, str]:
    if score >= 10:
        return "S1", "Critical"
    if score >= 7:
        return "S2", "High"
    if score >= 4:
        return "S3", "Moderate"
    return "S4", "Low"


def assess(inp: BreachInput) -> BreachResult:
    for name, table, val in (
        ("data_categories", _DATA_CATEGORY, inp.data_categories),
        ("volume", _VOLUME, inp.volume),
        ("encryption_state", _ENCRYPTION, inp.encryption_state),
        ("harm_likelihood", _HARM, inp.harm_likelihood),
    ):
        if val not in table:
            raise ValueError(f"invalid {name}={val!r}; expected one of {sorted(table)}")

    score = (
        _DATA_CATEGORY[inp.data_categories]
        + _VOLUME[inp.volume]
        + _ENCRYPTION[inp.encryption_state]
        + _HARM[inp.harm_likelihood]
        + (2 if inp.children_involved else 0)
        + (1 if inp.cross_border else 0)
    )
    tier, label = _tier(score)

    # Data Principal notification test (mirrors "Step 4")
    weak_enc = inp.encryption_state in ("plaintext", "encrypted_keys_exposed")
    notify_dp = (
        tier in ("S1", "S2")
        or inp.harm_likelihood in ("medium", "high")
        or (inp.data_categories in _SENSITIVE and weak_enc)
    )
    rationale = (
        "harm likely / sensitive exposure" if notify_dp
        else "low severity, no harm likely — document rationale"
    )

    # DPBI notification is ALWAYS required (Section 8(6) + Rule 7)
    return BreachResult(
        score=score,
        tier=tier,
        label=label,
        notify_dpbi=True,
        dpbi_timeline_hours=72,
        notify_data_principals=notify_dp,
        dp_rationale=rationale,
    )
