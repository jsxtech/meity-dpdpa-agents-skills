---
version: "1.5.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Breach Forensics & Evidence"
type: "skill"
---

# DPDP Data Breach Forensics & Evidence Skill

## Skill Identity

**Skill Name:** dpdp-breach-forensics
**Domain:** Digital Forensics, Evidence Preservation, Chain of Custody, Root-Cause Analysis
**Skill Type:** Technical, Security, Regulatory
**Applicable To:** CISO, Security/IR Teams, DPO, Legal

---

## Skill Purpose

Provide the **forensic and evidentiary discipline** that supports breach response under **Section 8(6) of the DPDP Act, 2023**. Where the Incident Response Skill covers containment and notification, this skill covers **preserving evidence, maintaining chain of custody, determining root cause, and building a defensible record** for the DPBI and any subsequent proceeding.

---

## Skill Capabilities

---

### Capability 1: Evidence Preservation

Preserve volatile and non-volatile evidence at incident detection: memory, logs, disk images, network captures — before remediation alters state.

---

### Capability 2: Chain of Custody

Maintain a documented chain of custody for every evidence item (who, what, when, where, how) so evidence is admissible and defensible.

---

### Capability 3: Scope & Impact Determination

Forensically establish which personal data was accessed, exfiltrated, altered, or destroyed, and the number of affected Data Principals — feeding the Breach Severity Decision Engine.

---

### Capability 4: Root-Cause Analysis

Determine the technical and process root cause (misconfiguration, credential compromise, insider, vulnerability) to drive remediation and prevent recurrence.

---

### Capability 5: Timeline Reconstruction

Reconstruct the incident timeline (initial access → dwell → exfiltration → detection) to support the 72-hour DPBI narrative and the awareness timestamp.

---

### Capability 6: Forensic Report for DPBI

Produce a defensible forensic report: scope, cause, timeline, affected data, containment, and remediation — aligned to the DPBI notification and any hearing.

---

### Capability 7: Post-Incident Hardening

Convert forensic findings into concrete control improvements and feed them to the Privacy Risk Management and Audit skills.

---

## Quick Commands

| Command | Action |
|---|---|
| `/forensics-preserve` | Preserve volatile and non-volatile evidence |
| `/forensics-custody` | Establish and maintain chain of custody |
| `/forensics-scope` | Determine data scope and affected Data Principals |
| `/forensics-rca` | Conduct root-cause analysis |
| `/forensics-timeline` | Reconstruct the incident timeline |
| `/forensics-report` | Produce a DPBI-ready forensic report |
| `/forensics-harden` | Convert findings into control improvements |

---

## Related Skills

- `dpdp-incident-response-skill.md` — Containment, notification, and the `/ir-severity` engine
- `dpdp-privacy-risk-management-skill.md` — Feeds findings into the risk register
- `dpdp-audit-checklist-skill.md` — Security safeguards audit domain

---

## Skill Guardrails

- **Never remediate** before preserving evidence where feasible — remediation can destroy proof.
- **Always maintain** an unbroken chain of custody for every evidence item.
- **Always establish** the awareness timestamp precisely — it starts the 72-hour DPBI clock.
- **Never overwrite** logs or images that may be evidence.
- **Always separate** forensic findings (facts) from legal conclusions.

---

## References

- DPDP Act, 2023 — Section 8(5) (security safeguards), Section 8(6) (breach notification)
- MeITY DPDP Rules, 2025 — Rule 7 (breach notification and severity)
- NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response
- ISO/IEC 27037 — Identification, collection, and preservation of digital evidence
