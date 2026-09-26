"""Tests asserting the engines reproduce the worked examples documented in the
markdown decision engines. If the docs and code diverge, these fail."""
import pytest

from dpdp_toolkit import breach_severity as bs
from dpdp_toolkit import scoring as sc


# --- Breach severity: worked examples from breach-severity-decision-engine.md ---

def test_breach_example_a_bucket_2m_plaintext():
    # basic(1)+>1M(3)+plaintext(2)+high(3) = 9 -> S2
    r = bs.assess(bs.BreachInput("basic", ">1M", "plaintext", "high"))
    assert r.score == 9
    assert r.tier == "S2"
    assert r.notify_dpbi is True
    assert r.dpbi_timeline_hours == 72
    assert r.notify_data_principals is True


def test_breach_example_b_lost_encrypted_laptop():
    # basic(1)+<1k(0)+keys_safe(0)+low(1) = 2 -> S4
    r = bs.assess(bs.BreachInput("basic", "<1k", "encrypted_keys_safe", "low"))
    assert r.score == 2
    assert r.tier == "S4"
    assert r.notify_dpbi is True          # always required
    assert r.notify_data_principals is False


def test_breach_example_c_health_minors_keys_exposed():
    # health(3)+1k-100k(1)+keys_exposed(1)+high(3)+children(+2) = 10 -> S1
    r = bs.assess(bs.BreachInput(
        "health", "1k-100k", "encrypted_keys_exposed", "high", children_involved=True))
    assert r.score == 10
    assert r.tier == "S1"
    assert r.notify_data_principals is True


def test_breach_dpbi_always_required_even_low():
    r = bs.assess(bs.BreachInput("basic", "<1k", "encrypted_keys_safe", "none"))
    assert r.score == 1
    assert r.tier == "S4"
    assert r.notify_dpbi is True          # key rule: never discretionary


def test_breach_invalid_input_raises():
    with pytest.raises(ValueError):
        bs.assess(bs.BreachInput("nonsense", "<1k", "plaintext", "high"))


# --- Compliance scoring: worked example from compliance-scoring-engine.md ---

WORKED_EXAMPLE = {
    "security_safeguards": 40,
    "breach_notification": 50,
    "childrens_data": 100,
    "lawful_basis_consent": 80,
    "data_principal_rights": 70,
    "sdf_obligations": 60,
    "notice_transparency": 80,
    "data_minimisation_retention": 70,
    "vendor_processor": 60,
    "cross_border_transfers": 100,
    "governance_accountability": 75,
    "training_awareness": 50,
    "enforcement_readiness": 50,
}


def test_scoring_weights_sum_to_100():
    assert sum(sc.DOMAIN_WEIGHTS.values()) == 100


def test_scoring_worked_example_is_66_7_defined():
    r = sc.score(WORKED_EXAMPLE)
    assert r.weighted_score == 66.7
    assert r.maturity == "Defined"


def test_scoring_critical_flag_on_weak_security():
    r = sc.score(WORKED_EXAMPLE)
    assert "security_safeguards" in r.critical_flags


def test_scoring_top_priorities_match_doc():
    r = sc.score(WORKED_EXAMPLE)
    top3 = r.priorities[:3]
    assert top3[0] == ("security_safeguards", 1080)
    assert top3[1] == ("breach_notification", 600)
    assert top3[2] == ("sdf_obligations", 320)


@pytest.mark.parametrize("s,band", [
    (95, "Optimised"), (80, "Managed"), (66.7, "Defined"),
    (45, "Developing"), (10, "Initial"),
])
def test_maturity_bands(s, band):
    assert sc.maturity_band(s) == band


def test_scoring_unknown_domain_raises():
    with pytest.raises(ValueError):
        sc.score({"not_a_domain": 50})
