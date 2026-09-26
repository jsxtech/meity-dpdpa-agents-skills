---
version: "1.5.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Data Retention Schedule"
type: "skill"
---

# DPDP Data Retention Schedule Skill

## Skill Identity

**Skill Name:** dpdp-retention-schedule
**Domain:** Retention Periods, Deletion Workflows, Legal Hold, Data Lifecycle
**Skill Type:** Operational, Regulatory
**Applicable To:** DPO, IT, Data Engineers, Records Management, Legal

---

## Skill Purpose

Provide the operational building blocks for **purpose-based data retention** under **Section 8 of the DPDP Act, 2023** and **Rule 8** of the DPDP Rules 2025 — retention-period templates by data category and sector, deletion-workflow patterns, legal-hold handling, and backup/replica erasure planning. This skill supplies the templates the Data Retention & Erasure Agent executes.

> **Rule 8 note:** The Rules confirm **purpose-based** retention and do not prescribe fixed sector-agnostic periods. Periods below are derived from purpose plus sector statutes (tax, RBI, labour, etc.) and must be validated against the organisation's own legal obligations.

---

## Skill Capabilities

---

### Capability 1: Retention Period Mapping

Map each processing purpose to a retention driver and period.

| Data / Purpose | Typical Driver | Indicative Period |
|---|---|---|
| Account/profile data | Duration of relationship | Until account closure + buffer |
| Transaction/financial records | Tax / statutory | As per applicable tax law |
| Marketing consent data | Consent validity | Until withdrawal or expiry |
| Employee records | Labour / statutory | As per labour law |
| Support tickets | Business need | Defined business period |

> Periods are indicative — validate against sector statutes before adoption.

---

### Capability 2: Retention Schedule Template

Produce a documented, per-purpose retention schedule (purpose, data categories, driver, period, erasure trigger, exceptions).

---

### Capability 3: Deletion Workflow Patterns

Define patterns for time-based and event-based deletion, including primary stores, replicas, caches, logs, and analytics copies.

---

### Capability 4: Legal Hold Handling

Establish legal-hold placement, scope, preservation, and release, overriding the normal erasure schedule.

---

### Capability 5: Backup & Replica Erasure Planning

Address erasure in immutable/rolling backups: scheduled backup expiry, crypto-shredding, or documented anonymisation where deletion is infeasible.

---

### Capability 6: Anonymisation-in-Lieu-of-Erasure

Decide when to anonymise instead of delete (e.g., analytics retention), coordinating with the Anonymisation Agent.

---

### Capability 7: Retention Evidence & Reporting

Maintain erasure logs (system, timestamp, record count) and produce retention-compliance evidence for audit and DPBI.

---

## Quick Commands

| Command | Action |
|---|---|
| `/retention-map` | Map processing purposes to retention drivers and periods |
| `/retention-schedule` | Generate a documented per-purpose retention schedule |
| `/retention-delete-flow` | Design a deletion workflow across all data stores |
| `/retention-legal-hold` | Place, track, or release a legal hold |
| `/retention-backups` | Plan erasure/anonymisation for backups and replicas |
| `/retention-anonymise` | Decide anonymisation-in-lieu-of-erasure |
| `/retention-evidence` | Produce retention-compliance evidence and logs |

---

## Related Skills

- `dpdp-data-mapping-inventory-skill.md` — Source of purposes and data categories
- `dpdp-audit-checklist-skill.md` — Retention & deletion audit domain
- `dpdp-sector-specific-skill.md` — Sector statutory retention periods

---

## Skill Guardrails

- **Never delete** data under active legal hold or statutory retention.
- **Always document** the driver and legal basis for each retention period.
- **Always plan for backups** — do not leave replicas out of erasure scope.
- **Always retain erasure evidence**, never the erased data itself.

---

## References

- DPDP Act, 2023 — Section 8 (erasure when purpose served)
- MeITY DPDP Rules, 2025 — Rule 8 (purpose-based retention)
- ISO/IEC 27001 — Annex A (secure disposal, information lifecycle)
