---
version: "1.7.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Intra-Group Transfer"
type: "skill"
---

# DPDP Intra-Group Transfer Skill

## Skill Identity

**Skill Name:** dpdp-intra-group-transfer
**Domain:** Group-Company Data Sharing, Intra-Group Agreements, Shared Services, Global HR
**Skill Type:** Operational, Legal, Regulatory
**Applicable To:** Group DPOs, Legal, Corporate Compliance, Multinationals

---

## Skill Purpose

Provide patterns for **personal data sharing between group companies** (parent, subsidiaries, affiliates) under the DPDP framework — intra-group agreements, shared-services processing, global HR data flows, and the interaction with the cross-border transfer rules (**Section 16**). Group sharing is **not automatically exempt**: each recipient is a separate legal person, so a lawful basis, purpose limitation, and (for overseas affiliates) transfer safeguards still apply.

> **Key principle:** There is no "group exemption" under the DPDP Act. A transfer to an affiliate is a transfer to a separate Data Fiduciary/Processor and must satisfy consent or a Section 7 legitimate use, purpose limitation, and \u2014 if the affiliate is overseas \u2014 the Section 16 transfer rules (pending the Rule 14 permissible-countries list).

---

## Skill Capabilities

---

### Capability 1: Intra-Group Data Flow Mapping

Map personal data flows between group entities: who shares what, with which affiliate, for what purpose, and across which borders.

---

### Capability 2: Lawful Basis for Group Sharing

Establish the basis for each intra-group flow (consent, S.7 legitimate use, or processor relationship) — never assume a group exemption.

---

### Capability 3: Intra-Group Agreement (IGA) Design

Design an intra-group data-sharing agreement / binding intra-group arrangement covering roles, purposes, security, sub-processing, and onward transfer.

---

### Capability 4: Controller vs Processor Mapping

Determine, for each affiliate, whether it acts as a Data Fiduciary (own purposes) or Processor (on instructions) \u2014 the roles drive the obligations.

---

### Capability 5: Cross-Border Overlay

Where affiliates are overseas, overlay the Section 16 transfer rules and interim contractual + technical safeguards (coordinate with Cross-Border and Localisation agents).

---

### Capability 6: Shared-Services & Global HR Flows

Handle common patterns \u2014 shared IT/HR/finance platforms, global employee directories \u2014 with proportionate controls and employee transparency.

---

### Capability 7: Group Accountability & Audit

Maintain group-level accountability: central register of intra-group flows, periodic audit, and consistent standards across entities.

---

## Quick Commands

| Command | Action |
|---|---|
| `/iga-flowmap` | Map personal data flows between group entities |
| `/iga-basis` | Establish lawful basis for each intra-group flow |
| `/iga-agreement` | Draft an intra-group data-sharing agreement |
| `/iga-roles` | Map controller vs processor roles per affiliate |
| `/iga-crossborder` | Overlay Section 16 transfer rules on overseas flows |
| `/iga-shared-services` | Handle shared-services and global HR flows |
| `/iga-audit` | Maintain group-level accountability and audit |

---

## Related Skills

- `dpdp-contract-clauses-skill.md` — Intra-group agreement clauses
- `dpdp-vendor-risk-skill.md` — Affiliate-as-processor risk
- `dpdp-international-comparison-skill.md` — Multi-jurisdiction group compliance

---

## Skill Guardrails

- **Never assume** a group exemption \u2014 each affiliate is a separate legal person under the Act.
- **Always establish** a lawful basis for every intra-group flow.
- **Always overlay** Section 16 transfer rules for overseas affiliates.
- **Always document** controller/processor roles per affiliate.
- **Never allow** onward transfer beyond the agreed group scope without a basis.

---

## References

- DPDP Act, 2023 — Section 16 (cross-border transfer), Sections 6, 7, 8
- MeITY DPDP Rules, 2025 — Rule 14 (transfer safeguards; permissible countries pending)
