---
version: "1.7.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "RoPA Generation"
type: "skill"
---

# DPDP RoPA Generator Skill

## Skill Identity

**Skill Name:** dpdp-ropa-generator
**Domain:** Records of Processing Activities, Processing Register, Data Inventory Output
**Skill Type:** Operational, Documentation, Regulatory
**Applicable To:** DPO, Privacy Analysts, IT, Compliance

---

## Skill Purpose

Provide a **structured method and template to generate a Records of Processing Activities (RoPA)** \u2014 the processing register a Data Fiduciary maintains to demonstrate accountability under **Section 8** of the DPDP Act, 2023. Where the Data Mapping & Inventory skill *discovers* data, this skill *produces the RoPA document* from that inventory in a consistent, auditable format.

> **Note:** The DPDP Act does not prescribe a fixed RoPA format, but a maintained processing register is essential to demonstrate compliance (accountability) and to answer DPBI inquiries. This skill produces a defensible, industry-standard RoPA.

---

## Skill Capabilities

---

### Capability 1: RoPA Field Schema

Define the RoPA record fields: activity, purpose, data categories, Data Principal categories, lawful basis, recipients, cross-border, retention, and security measures.

| Field | Example |
|---|---|
| Processing activity | User registration |
| Purpose | Account creation and service delivery |
| Data categories | Name, email, phone |
| Lawful basis | Consent (S.6) / Legitimate use (S.7) |
| Recipients | Payment processor (processor) |
| Cross-border | No / Country + safeguard |
| Retention | Until account closure + statutory period |
| Security measures | Encryption, access control |

---

### Capability 2: RoPA Generation from Inventory

Transform the data-mapping inventory into completed RoPA records, one per processing activity.

---

### Capability 3: Lawful-Basis Column Population

Populate the lawful basis for each activity (consent vs Section 7 grounds), consistent with the Legitimate Use and Consent skills.

---

### Capability 4: Cross-Border & Recipient Mapping

Record recipients (processors, affiliates, third parties) and any cross-border element with the applicable safeguard.

---

### Capability 5: Retention Linkage

Link each RoPA record to its retention period and erasure trigger (coordinate with the Retention Schedule skill).

---

### Capability 6: RoPA Review & Versioning

Version the RoPA, schedule periodic review, and track changes as processing evolves.

---

### Capability 7: DPBI-Ready RoPA Export

Produce a clean, exportable RoPA suitable for internal audit and DPBI inquiry response.

---

## Quick Commands

| Command | Action |
|---|---|
| `/ropa-schema` | Define the RoPA record field schema |
| `/ropa-generate` | Generate RoPA records from the data inventory |
| `/ropa-basis` | Populate the lawful-basis column per activity |
| `/ropa-recipients` | Map recipients and cross-border elements |
| `/ropa-retention` | Link retention periods and erasure triggers |
| `/ropa-review` | Version and schedule RoPA review |
| `/ropa-export` | Produce a DPBI-ready RoPA export |

---

## Related Skills

- `dpdp-data-mapping-inventory-skill.md` — Source inventory for the RoPA
- `dpdp-retention-schedule-skill.md` — Retention periods per activity
- `dpdp-legitimate-use-skill.md` — Lawful-basis determination

---

## Skill Guardrails

- **Always base** the RoPA on the actual data inventory, not assumptions.
- **Always record** a lawful basis for every processing activity.
- **Always version** the RoPA and review it as processing changes.
- **Never include** raw personal data in the RoPA \u2014 it describes processing, not the data itself.

---

## References

- DPDP Act, 2023 — Section 8 (accountability, obligations of Data Fiduciary)
- MeITY DPDP Rules, 2025 (Notified)
