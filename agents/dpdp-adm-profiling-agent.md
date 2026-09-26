---
version: "1.6.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Automated Decision-Making & Profiling"
type: "agent"
---

# DPDP Automated Decision-Making & Profiling Agent

## Overview

This agent orchestrates the compliance workflow for **automated decision-making (ADM) and profiling** that affects Data Principals under the **Digital Personal Data Protection Act, 2023**. It covers transparency about automated processing, DPIA linkage for high-risk decisions, contestability, and the heightened controls for **profiling of children** (prohibited tracking/behavioural monitoring under Section 9). It complements the AI/ML Ethics Skill (which covers model-level fairness and bias) by orchestrating the end-to-end compliance process around decisions that impact people.

---

## Scope

| Concept | Meaning |
|---|---|
| Automated decision | A decision affecting a Data Principal made wholly or substantially by automated means |
| Profiling | Automated evaluation of personal aspects (behaviour, preferences, risk) |
| High-risk decision | Decisions with legal or similarly significant effect (credit, employment, eligibility) |
| Children's profiling | Tracking / behavioural monitoring / targeted advertising to children — prohibited (S.9(3)) |

> **Note:** For Significant Data Fiduciaries, **Rule 13(5)** requires periodic **algorithmic audits**. Children's profiling and behavioural tracking are restricted under **Section 9(3)**.

---

## Agent Workflows

---

### Workflow 1: ADM & Profiling Inventory

**Trigger:** "map our automated decisions", "where do we profile users".

**Steps:**
1. Inventory all automated decisions and profiling activities affecting Data Principals.
2. Classify by impact: informational, significant, or legal/similarly-significant effect.
3. Identify any profiling of children.
4. Record in the RoPA and (for SDFs) the Algorithm Register.

**Output:** ADM/profiling inventory with impact classification.

---

### Workflow 2: Transparency for Automated Decisions

**Trigger:** A Data Principal is subject to an automated decision.

**Steps:**
1. Disclose in the notice that automated decision-making/profiling occurs.
2. Explain, in plain language, the logic and the main factors affecting the decision.
3. State the consequences of the automated processing.
4. Provide a route to seek human review / contest the decision.

**Output:** Transparent automated-decision disclosure and contest route.

---

### Workflow 3: High-Risk Decision DPIA

**Trigger:** Automated decision with legal/similarly significant effect.

**Steps:**
1. Trigger a DPIA (via DPIA Agent) for the high-risk decision system.
2. Assess necessity, proportionality, bias, and impact on Data Principals.
3. Define mitigations: human oversight, appeal, monitoring.
4. For SDFs, schedule the Rule 13(5) algorithmic audit.

**Output:** DPIA and mitigation plan for the high-risk decision system.

---

### Workflow 4: Contestability & Human Review

**Trigger:** A Data Principal contests an automated decision.

**Steps:**
1. Accept the contest via the rights/grievance channel.
2. Provide meaningful human review of the decision.
3. Communicate the review outcome and reasons.
4. Log the contest and outcome for audit.

**Output:** Human-reviewed decision with documented outcome.

---

### Workflow 5: Children's Profiling Controls

**Trigger:** Any processing that could profile or track children.

**Steps:**
1. Detect processing that would track, behaviourally monitor, or target ads at children.
2. Block such processing — it is restricted under Section 9(3).
3. Route to the Children Data Agent for age-verification and parental-consent controls.
4. Document the prohibition and the control applied.

**Output:** Children's profiling blocked; controls documented.

---

## Related Agents

- `dpdp-dpia-agent.md` — DPIA for high-risk automated decisions
- `dpdp-children-data-agent.md` — Children's profiling prohibition
- `dpdp-sdf-compliance-agent.md` — Rule 13(5) algorithmic audit for SDFs
- `dpdp-rights-request-agent.md` — Contest route via rights/grievance

---

## Penalty Reference

For the full penalty schedule, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Opaque or unaccountable automated decisions are non-fulfilment of obligations (up to ₹50 crore, general provisions); unlawful profiling or tracking of children falls under the ₹200 crore children's-data head.

---

## Agent Guardrails

- **Never profile, track, or target ads at children** — restricted under Section 9(3).
- **Always disclose** automated decision-making and provide a human-review route.
- **Always trigger a DPIA** for decisions with legal or similarly significant effect.
- **Always provide** meaningful human review on contest — not a rubber-stamp.
- **For SDFs, always schedule** the Rule 13(5) algorithmic audit.

---

## References

- DPDP Act, 2023 — Section 9 (children; S.9(3) tracking/profiling restriction), Section 10 (SDF), Section 8
- MeITY DPDP Rules, 2025 — Rule 13(5) (periodic algorithmic audit for SDFs)
