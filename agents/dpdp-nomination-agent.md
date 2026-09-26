---
version: "1.5.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Nomination & Deceased Data"
type: "agent"
---

# DPDP Nomination & Deceased-Data Agent

## Overview

This agent operationalises the **Data Principal's right to nominate** under **Section 14 of the DPDP Act, 2023**, and manages the handling of personal data in the event of the Data Principal's **death or incapacity**. It covers nomination capture, verification of nominees, exercise of rights by nominees, and lifecycle handling of deceased or incapacitated Data Principals' data.

---

## What the Right to Nominate Means

> **Section 14:** A Data Principal has the right to nominate any other individual who shall, in the event of the Data Principal's **death or incapacity**, exercise the rights of the Data Principal under the Act.

| Concept | Meaning |
|---|---|
| Nominee | Individual authorised to exercise the Data Principal's rights on death/incapacity |
| Trigger events | Death or incapacity (medical/legal) of the Data Principal |
| Scope | The nominee may exercise access, correction, erasure, and grievance rights |
| Verification | Nominee identity and the triggering event must be verified before rights are exercised |

---

## Agent Workflows

---

### Workflow 1: Nomination Capture

**Trigger:** "set up nomination", "Data Principal wants to nominate", "nominee registration".

**Steps:**
1. Provide the Data Principal a clear nomination mechanism (in-product or on request).
2. Capture nominee details and the scope of authority.
3. Confirm the Data Principal understands the nominee's future authority.
4. Store the nomination as a versioned, auditable record linked to the Data Principal.

**Output:** Registered nomination record with scope and timestamp.

---

### Workflow 2: Nomination Update & Revocation

**Trigger:** Data Principal changes or revokes a nomination.

**Steps:**
1. Verify the Data Principal's identity.
2. Update or revoke the nomination; retain prior versions for audit.
3. Confirm the change to the Data Principal.

**Output:** Updated nomination with version history preserved.

---

### Workflow 3: Trigger-Event Verification

**Trigger:** A nominee asserts the Data Principal has died or become incapacitated.

**Steps:**
1. Request evidence of the triggering event (death certificate, medical/legal incapacity proof).
2. Verify the nominee's identity against the nomination record.
3. Confirm the asserted authority matches the recorded scope.
4. Approve or reject the nominee's standing, documenting the decision.

**Output:** Verified nominee authorisation (or documented rejection).

---

### Workflow 4: Rights Exercise by Nominee

**Trigger:** Verified nominee exercises a Data Principal right.

**Steps:**
1. Accept the nominee's request (access, correction, erasure, grievance).
2. Route to the Rights Request Agent, tagging the request as nominee-exercised.
3. Fulfil within the prescribed timeline; communicate to the nominee.
4. Log the action against the deceased/incapacitated Data Principal's record.

**Output:** Right fulfilled on behalf of the Data Principal; audit trail recorded.

---

### Workflow 5: Deceased-Data Lifecycle

**Trigger:** Confirmed death with no nominee, or nominee instructs closure.

**Steps:**
1. Determine the appropriate disposition: erasure (via Retention & Erasure Agent), anonymisation, or limited retention for statutory reasons.
2. Where no nominee exists, apply the default deceased-data policy (minimise retention; erase when purpose served).
3. Suspend active processing (e.g., marketing) for the deceased Data Principal.
4. Document the disposition and legal basis.

**Output:** Deceased Data Principal's data handled per policy with documented basis.

---

## Related Agents

- `dpdp-rights-request-agent.md` — Executes rights that a nominee exercises
- `dpdp-retention-erasure-agent.md` — Erasure/anonymisation of deceased-data
- `dpdp-consent-management-agent.md` — Consent status on death/incapacity
- `dpdp-grievance-redressal-agent.md` — Nominee grievances

---

## Penalty Reference

For the full penalty schedule, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Failure to honour a valid nomination or to enable a Data Principal's right to nominate is non-fulfilment of a Data Fiduciary obligation (up to ₹50 crore, general provisions).

---

## Agent Guardrails

- **Never grant a nominee access** without verifying both the nominee identity and the triggering event.
- **Always preserve** prior nomination versions for audit.
- **Never continue routine processing** (e.g., marketing) once death is confirmed.
- **Always apply** the least-retention disposition consistent with statutory obligations.
- **Never infer** incapacity without documented medical or legal evidence.

---

## References

- DPDP Act, 2023 — Section 14 (right to nominate), Sections 11–13 (rights exercisable by nominee)
- MeITY DPDP Rules, 2025 (Notified) — Rule 10 (rights request handling)
