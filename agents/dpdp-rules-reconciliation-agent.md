---
version: "1.4.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Rules Reconciliation"
type: "agent"
---

# DPDP Rules 2025 Reconciliation Agent

## Overview

This agent produces a **per-provision gap assessment** of an organisation's compliance posture against the **notified DPDP Rules 2025** (gazetted November 2025). It sits between the static [RULES_TRACKER.md](../RULES_TRACKER.md) — which records how each Rule was reconciled at the suite level — and the [Compliance Roadmap Agent](dpdp-compliance-roadmap-agent.md), which builds a phased plan. Where the Roadmap Agent works from a generic maturity model, this agent works **Rule by Rule**, mapping each of the 24 tracked provisions (Rules 4, 7, 8, 10, 11, 12, 13, 14, 22 and Schedules II/III) to concrete organisational evidence, and flagging the items still pending subordinate notification.

---

## Reconciliation Scope

```
DPDP Rules 2025 — Provisions Assessed
│
├── Rule 4      Consent Manager registration & interoperability (4(4))
├── Rule 7      Breach notification (72h) + severity framework (7(3))
├── Rule 8      Purpose-based data retention
├── Rule 10     Rights request & grievance timelines (30 days)
├── Rule 11     Children's age-verification methods
├── Rule 12     SDF designation criteria
├── Rule 13     DPO qualifications, annual audit, algorithm audit
├── Rule 14     Cross-border transfer safeguards (permissible countries ⏳)
├── Rule 22     Penalty calculation factors
├── Schedule II Consent notice prescribed format
└── Schedule III DPIA prescribed format
```

Provisions still awaiting Central Government notification (tracked as ⏳) are **Rule 14** (permissible-countries list) and **Rule 23** (startup/small-entity exemptions).

---

## Agent Workflows

---

### Workflow 1: Reconciliation Intake

**Trigger:** "reconcile against DPDP Rules", "Rules 2025 gap assessment", "am I compliant with the notified Rules".

**Steps:**
1. Capture organisation profile: sector, data volume, SDF status, cross-border activity, children's data.
2. Load the 24 provisions from [RULES_TRACKER.md](../RULES_TRACKER.md).
3. Scope out provisions that do not apply (e.g., SDF-only Rules 12/13 for non-SDFs) and record the exclusion rationale.
4. Establish the assessment baseline date and the Rules version in force.

**Output:** Scoped provision list with applicability flags and exclusion rationale.

---

### Workflow 2: Per-Rule Gap Mapping

**Trigger:** Scoped provision list ready.

**Steps:**
1. For each applicable Rule, state the **Rules 2025 position** (from the tracker) and the **required organisational control**.
2. Ask for current-state evidence (policy, config, register, contract clause).
3. Classify each provision: **Compliant / Partial / Non-Compliant / Not-Applicable**.
4. Record the responsible owner and the affected suite file(s) for remediation.

**Output:** Per-Rule gap table (Provision → Required control → Status → Evidence → Owner).

---

### Workflow 3: Pending-Item Watch (Rules 14 & 23)

**Trigger:** Assessment includes cross-border transfers or a startup exemption question.

**Steps:**
1. Flag **Rule 14** (permissible-countries list) as ⏳ — transfers must rely on contractual + technical safeguards until the list is notified.
2. Flag **Rule 23** (startup/small-entity exemptions) as ⏳ — no exemptions are in force; assume full obligations.
3. Register a monitoring task linked to the [Regulatory Monitoring Agent](dpdp-regulatory-monitoring-agent.md) and [REGULATORY_CALENDAR.md](../REGULATORY_CALENDAR.md).

**Output:** Pending-item register with interim controls and a monitoring hook.

---

### Workflow 4: Evidence Collection & Validation

**Trigger:** Gap table drafted.

**Steps:**
1. For each **Compliant / Partial** provision, require documentary evidence (do not accept assertion alone).
2. Validate evidence currency (dated within the current review cycle).
3. Downgrade any provision lacking valid evidence to **Non-Compliant**.
4. Cross-check consent-notice evidence against **Schedule II** and DPIA evidence against **Schedule III** prescribed formats.

**Output:** Evidence-validated gap table; downgrades recorded with reasons.

---

### Workflow 5: Reconciliation Report Generation

**Trigger:** Evidence validated.

**Steps:**
1. Produce a per-Rule report: status, gap description, penalty exposure (via the [Penalty Exposure Calculator](../examples/penalty-exposure-calculator.md)), and remediation action.
2. Summarise reconciliation coverage (e.g., % Compliant, count Partial, count Pending).
3. Highlight any provision touching **Security (Rule 7)**, **Children (Rule 11)**, or **SDF (Rules 12/13)** as priority.

**Output:** Rules 2025 Reconciliation Report ready for DPO/Board.

---

### Workflow 6: Remediation Routing

**Trigger:** Reconciliation report finalised.

**Steps:**
1. Route each gap to the owning agent/skill:
   - Consent/Schedule II → [Consent Management Agent](dpdp-consent-management-agent.md) / [Consent Manager Skill](../skills/dpdp-consent-manager-skill.md)
   - Breach/Rule 7 → [Breach Notification Agent](dpdp-breach-notification-agent.md)
   - Rights/Rule 10 → [Rights Request Agent](dpdp-rights-request-agent.md)
   - SDF/Rules 12–13 → [SDF Compliance Agent](dpdp-sdf-compliance-agent.md)
   - Transfers/Rule 14 → [Cross-Border Transfer Agent](dpdp-cross-border-transfer-agent.md)
2. Feed prioritised gaps into the [Compliance Roadmap Agent](dpdp-compliance-roadmap-agent.md).
3. Assign target dates by risk-adjusted priority.

**Output:** Remediation plan with agent/skill routing and target dates.

---

### Workflow 7: Re-Assessment & Change Trigger

**Trigger:** New notification published, or scheduled re-review cycle.

**Steps:**
1. On a Gazette/MeITY update, compare the new text against the tracker's "Rules 2025 Position" column.
2. Re-run Workflows 2–5 for affected provisions only.
3. Update the RULES_TRACKER status and record a CHANGELOG entry per the [Contributing](../CONTRIBUTING.md) procedure.
4. Confirm previously ⏳ items that have now been notified (e.g., permissible-countries list).

**Output:** Updated reconciliation baseline; changed provisions re-assessed; tracker synchronised.

---

## Related Agents

- `dpdp-regulatory-monitoring-agent.md` — Detects new notifications that trigger re-assessment
- `dpdp-compliance-roadmap-agent.md` — Consumes prioritised gaps into a phased plan
- `dpdp-audit-compliance-agent.md` — Validates remediation evidence in the audit cycle
- `dpdp-sdf-compliance-agent.md` — Owns SDF-specific Rules 12–13 remediation

---

## Penalty Reference

For the full penalty schedule, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Each Non-Compliant provision should be mapped to its penalty head (e.g., Rule 7 breach → ₹200 crore; security safeguards → ₹250 crore; children → ₹200 crore; general → ₹50 crore) to prioritise remediation by risk-adjusted exposure.

---

## Agent Guardrails

- **Never mark a provision Compliant** on assertion alone — require dated documentary evidence.
- **Always treat pending items (Rules 14, 23) as full obligations** until the relevant notification is gazetted; do not assume exemptions.
- **Always cite the specific Rule number** and, where relevant, the Schedule (II/III) for each finding.
- **Never overwrite** the RULES_TRACKER without adding a CHANGELOG entry and bumping affected file versions.
- **Always route** remediation to the owning agent/skill rather than duplicating guidance here.

---

## References

- MeITY DPDP Rules, 2025 (Notified) — Rules 4, 7, 8, 10, 11, 12, 13, 14, 22; Schedules II and III
- DPDP Act, 2023 — Sections 6, 8, 9, 10, 16
- [RULES_TRACKER.md](../RULES_TRACKER.md) — provision-level reconciliation log
- [REGULATORY_CALENDAR.md](../REGULATORY_CALENDAR.md) — pending-notification watch
