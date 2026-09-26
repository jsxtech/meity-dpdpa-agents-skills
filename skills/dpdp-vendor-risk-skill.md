---
version: "1.5.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Vendor Risk Assessment"
type: "skill"
---

# DPDP Vendor Risk Assessment Skill

## Skill Identity

**Skill Name:** dpdp-vendor-risk
**Domain:** Processor Due Diligence, Vendor Risk Scoring, Sub-Processor Management
**Skill Type:** Operational, Risk, Regulatory
**Applicable To:** Procurement, DPO, Security, Vendor Management, Legal

---

## Skill Purpose

Provide the **risk-assessment toolkit** for engaging Data Processors under **Section 8 of the DPDP Act, 2023** — due-diligence questionnaires, a vendor risk-scoring rubric, sub-processor tiering, and ongoing monitoring. The Vendor & Processor Agent runs the engagement process; this skill supplies the scoring and diligence instruments.

---

## Skill Capabilities

---

### Capability 1: Vendor Risk Tiering

Classify vendors by risk based on data sensitivity, volume, cross-border exposure, and criticality.

| Tier | Criteria | Diligence Depth |
|---|---|---|
| Critical | Sensitive data, large volume, or cross-border | Full assessment + audit rights |
| High | Personal data, moderate volume | Full questionnaire + evidence |
| Medium | Limited personal data | Standard questionnaire |
| Low | No/negligible personal data | Lightweight screening |

---

### Capability 2: Due-Diligence Questionnaire

Structured questionnaire covering security controls, sub-processors, breach history, cross-border processing, certifications (ISO 27001, SOC 2), and DPDP-specific obligations.

---

### Capability 3: Vendor Risk Scoring Rubric

Score each vendor across security, compliance, data-handling, and resilience dimensions to a composite risk rating that drives approval and controls.

---

### Capability 4: Sub-Processor Assessment

Assess and register sub-processors, require flow-down of DPDP obligations, and control changes to the sub-processor chain.

---

### Capability 5: Contractual Control Mapping

Map identified risks to required DPA clauses (coordinate with Contract Clauses Skill): security, breach notification, audit rights, deletion, sub-processing, cross-border.

---

### Capability 6: Ongoing Vendor Monitoring

Define reassessment cadence, evidence refresh, breach-notification obligations, and trigger-based re-review (incident, ownership change, new sub-processor).

---

### Capability 7: Vendor Offboarding Risk

Ensure secure data return/deletion, access revocation, and deletion confirmation at contract end.

---

## Quick Commands

| Command | Action |
|---|---|
| `/vendor-tier` | Classify a vendor into a risk tier |
| `/vendor-questionnaire` | Generate a due-diligence questionnaire |
| `/vendor-score` | Score a vendor against the risk rubric |
| `/vendor-subprocessor` | Assess and register sub-processors |
| `/vendor-controls` | Map risks to required DPA clauses |
| `/vendor-monitor` | Define ongoing monitoring and reassessment |
| `/vendor-offboard` | Run vendor offboarding risk checks |

---

## Related Skills

- `dpdp-contract-clauses-skill.md` — DPA clauses that mitigate identified risks
- `dpdp-privacy-risk-management-skill.md` — Feeds vendor risk into the register
- `dpdp-audit-checklist-skill.md` — Vendor & processor audit domain

---

## Skill Guardrails

- **Never onboard** a Critical-tier vendor without a completed full assessment.
- **Always require** sub-processor flow-down of DPDP obligations.
- **Always obtain deletion confirmation** at offboarding.
- **Never accept** self-attestation alone for Critical vendors — require evidence.

---

## References

- DPDP Act, 2023 — Section 8 (Data Fiduciary responsible for processor compliance)
- MeITY DPDP Rules, 2025 (Notified)
- ISO/IEC 27036 — Supplier relationship security
