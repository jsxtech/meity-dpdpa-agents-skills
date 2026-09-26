---
version: "1.4.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Compliance Scoring"
type: "decision-engine"
---

# DPDP Compliance Scoring Engine

A deterministic, weighted scoring model that unifies the two assessment instruments in this suite — the 60-question [Self-Assessment](../SELF_ASSESSMENT.md) (120 points, 13 domains) and the 159-control [Audit Checklist](../skills/dpdp-audit-checklist-skill.md) (12 domains) — into a single, reproducible compliance score, maturity level, and remediation-priority ranking.

The engine is designed so that an LLM assistant or an application can compute the same score from the same inputs every time, and so that self-assessment results and formal audit results are expressed on a comparable 0–100 scale.

> **Not legal advice.** The score is a management indicator, not a legal determination of compliance. Use it to prioritise remediation and report to the Board; consult qualified Indian privacy counsel for binding decisions.

---

## 1. Normalised Scoring Model

Both instruments are converted to a **0–100 normalised score**:

```
normalised_score = (points_achieved / points_possible) × 100
```

- **Self-Assessment:** each question scores Y = 2, P = 1, N = 0; `points_possible = 120`.
- **Audit Checklist:** each control scores Compliant = 1, Partial = 0.5, Non-Compliant = 0; `points_possible = 159`.

---

## 2. Domain Weights

Domains are weighted by statutory risk exposure (penalty magnitude under the DPDP Schedule) so that a weak high-risk domain lowers the score more than a weak low-risk one. Weights sum to 100.

| # | Domain | Weight | Rationale (penalty head) |
|---|---|---|---|
| 1 | Security Safeguards | 18 | ₹250 cr — highest statutory cap (S.8(5)) |
| 2 | Breach Notification | 12 | ₹200 cr — breach reporting (S.8(6)) |
| 3 | Children's Data | 12 | ₹200 cr — children (S.9) |
| 4 | Lawful Basis & Consent | 10 | Core lawfulness (S.4, 5, 6) |
| 5 | Data Principal Rights | 9 | Rights fulfilment (S.11–14) |
| 6 | SDF Obligations | 8 | ₹150 cr for SDFs (S.10) |
| 7 | Notice & Transparency | 7 | Notice adequacy (S.5) |
| 8 | Data Minimisation & Retention | 6 | Purpose limitation, erasure (S.6, 8) |
| 9 | Vendor & Processor Management | 6 | Processor obligations (S.8) |
| 10 | Cross-Border Transfers | 4 | Transfer restrictions (S.16) |
| 11 | Governance & Accountability | 4 | RoPA, DPO, oversight |
| 12 | Training & Awareness | 2 | Staff readiness |
| 13 | Enforcement Readiness & Exemptions | 2 | DPBI-readiness, S.17 exemptions |

> The 13 Self-Assessment domains map 1:1 to the weights above. The 12 Audit domains map by name; "Data Quality & Accuracy" folds into **Data Minimisation & Retention**, and Audit has no separate Training/Enforcement domain (those weights are redistributed proportionally when scoring an audit-only run — see the schema `audit_domain_map`).

### Weighted score

```
weighted_score = Σ ( domain_normalised_score × domain_weight ) / 100
```

---

## 3. Maturity Levels

The weighted score maps to the 5-level maturity model used by the [Compliance Roadmap Agent](../agents/dpdp-compliance-roadmap-agent.md):

| Weighted Score | Maturity Level | Meaning |
|---|---|---|
| 90–100 | **Optimised** | Controls embedded, monitored, continuously improved |
| 75–89 | **Managed** | Controls operating and measured; targeted gaps |
| 60–74 | **Defined** | Controls documented and largely implemented |
| 30–59 | **Developing** | Foundational controls partial or inconsistent |
| 0–29 | **Initial** | Ad-hoc or absent; urgent programme required |

---

## 4. Remediation Priority

Each domain gets a priority rank so remediation effort targets the biggest risk-adjusted gaps first:

```
priority_score = (100 − domain_normalised_score) × domain_weight
```

Rank domains by descending `priority_score`. The highest values are weak, high-weight domains — remediate these first. Domains scoring `< 50` in the **Security Safeguards**, **Breach Notification**, or **Children's Data** domains are flagged **Critical** regardless of overall score.

---

## 5. Machine-Readable Schema

```yaml
compliance_scoring_engine:
  version: "1.0"
  instruments:
    self_assessment:
      source: "SELF_ASSESSMENT.md"
      answer_scale: { Y: 2, P: 1, N: 0 }
      points_possible: 120
      domains: 13
    audit_checklist:
      source: "skills/dpdp-audit-checklist-skill.md"
      answer_scale: { Compliant: 1.0, Partial: 0.5, NonCompliant: 0.0 }
      controls: 159
      domains: 12
  domain_weights:
    security_safeguards: 18
    breach_notification: 12
    childrens_data: 12
    lawful_basis_consent: 10
    data_principal_rights: 9
    sdf_obligations: 8
    notice_transparency: 7
    data_minimisation_retention: 6
    vendor_processor: 6
    cross_border_transfers: 4
    governance_accountability: 4
    training_awareness: 2
    enforcement_readiness: 2
  audit_domain_map:
    data_quality_accuracy: data_minimisation_retention   # fold into retention
    # audit has no training/enforcement domains -> redistribute proportionally
  formulas:
    normalised_score: "(points_achieved / points_possible) * 100"
    weighted_score: "sum(domain_normalised * weight) / 100"
    priority_score: "(100 - domain_normalised) * weight"
  maturity_bands:
    - { level: "Optimised",  min: 90 }
    - { level: "Managed",    min: 75, max: 89 }
    - { level: "Defined",    min: 60, max: 74 }
    - { level: "Developing", min: 30, max: 59 }
    - { level: "Initial",    min: 0,  max: 29 }
  critical_flags:
    rule: "domain_normalised < 50 in [security_safeguards, breach_notification, childrens_data]"
```

---

## 6. Worked Example (Self-Assessment)

An organisation scores as follows (normalised per domain):

| Domain | Normalised | Weight | Weighted contribution | Priority score |
|---|---|---|---|---|
| Security Safeguards | 40 | 18 | 7.2 | 1080 (**Critical**) |
| Breach Notification | 50 | 12 | 6.0 | 600 |
| Children's Data | 100 | 12 | 12.0 | 0 |
| Lawful Basis & Consent | 80 | 10 | 8.0 | 200 |
| Data Principal Rights | 70 | 9 | 6.3 | 270 |
| SDF Obligations | 60 | 8 | 4.8 | 320 |
| Notice & Transparency | 80 | 7 | 5.6 | 140 |
| Data Minimisation & Retention | 70 | 6 | 4.2 | 180 |
| Vendor & Processor | 60 | 6 | 3.6 | 240 |
| Cross-Border Transfers | 100 | 4 | 4.0 | 0 |
| Governance & Accountability | 75 | 4 | 3.0 | 100 |
| Training & Awareness | 50 | 2 | 1.0 | 100 |
| Enforcement Readiness | 50 | 2 | 1.0 | 100 |
| **TOTAL** | — | **100** | **66.7** | — |

- **Weighted score = 66.7 → Maturity: Defined**
- **Critical flag:** Security Safeguards (40 < 50) — remediate first
- **Top remediation priorities:** Security Safeguards (1080), Breach Notification (600), SDF Obligations (320)

---

## 7. Scorecard Output Template

```
DPDP COMPLIANCE SCORE
Organisation : ___________________   Date : __________
Instrument   : [Self-Assessment | Audit Checklist]

Weighted Score : ____ / 100
Maturity Level : [Initial | Developing | Defined | Managed | Optimised]

Critical Flags :
  - ____________________
Top 3 Remediation Priorities (risk-adjusted):
  1. ____________  (priority score ____)
  2. ____________  (priority score ____)
  3. ____________  (priority score ____)

Recommended next step: [Compliance Roadmap Agent | Privacy Risk Management Skill]
```

---

## Related

- [Self-Assessment](../SELF_ASSESSMENT.md) — the 60-question input instrument
- [Audit Checklist Skill](../skills/dpdp-audit-checklist-skill.md) — the 159-control input instrument (`/audit-score`)
- [Compliance Roadmap Agent](../agents/dpdp-compliance-roadmap-agent.md) — consumes the maturity level and priorities
- [Privacy Risk Management Skill](../skills/dpdp-privacy-risk-management-skill.md) — turns priorities into a risk register

## References

- DPDP Act, 2023 — Schedule (penalty heads informing domain weights); Sections 4, 5, 6, 8, 9, 10, 11–14, 16
- MeITY DPDP Rules, 2025 — Rule 12 (SDF criteria), Rule 13 (SDF obligations)
