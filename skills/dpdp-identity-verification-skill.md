---
version: "1.6.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Identity Verification"
type: "skill"
---

# DPDP Data Subject Verification Skill

## Skill Identity

**Skill Name:** dpdp-identity-verification
**Domain:** Requester Verification, Anti-Fraud, Proportionate Verification, Nominee/Guardian Checks
**Skill Type:** Operational, Security, Regulatory
**Applicable To:** Rights/DSAR Teams, DPO, Security, Support

---

## Skill Purpose

Provide **proportionate identity-verification** methods for confirming that a person exercising a Data Principal right, a nomination, or a grievance is who they claim to be — under **Sections 11–14 of the DPDP Act, 2023** — without collecting excessive data during verification itself. Verification is referenced across the Rights, Nomination, and Grievance agents; this skill supplies the methods and anti-fraud controls.

---

## Skill Capabilities

---

### Capability 1: Proportionate Verification Levels

Match verification strength to request risk: low (view non-sensitive), medium (correction), high (erasure, sensitive data, nominee access).

| Request Type | Verification Level |
|---|---|
| Access to non-sensitive data | Low–Medium |
| Correction / update | Medium |
| Erasure / sensitive data | High |
| Nominee / guardian exercising rights | High + relationship proof |

---

### Capability 2: Verification Methods

Catalogue of methods (account authentication, OTP, existing-channel confirmation, document checks) chosen to be sufficient but not excessive.

---

### Capability 3: Data-Minimising Verification

Verify using data already held where possible; avoid collecting new identity documents unless strictly necessary, and delete verification data after use.

---

### Capability 4: Nominee & Guardian Verification

Verify a nominee (against the nomination record + trigger event) or a parent/guardian (for a child) before allowing rights exercise.

---

### Capability 5: Anti-Fraud & Impersonation Controls

Detect and prevent fraudulent requests (impersonation, social engineering, bulk automated requests) without over-burdening genuine Data Principals.

---

### Capability 6: Failed-Verification Handling

Define what happens when verification fails: additional proportionate steps, refusal with reasons, and logging — never silently ignoring the request.

---

### Capability 7: Verification Audit Trail

Record the verification performed for each request (method, level, outcome) as evidence, without retaining unnecessary identity data.

---

## Quick Commands

| Command | Action |
|---|---|
| `/idv-level` | Determine the proportionate verification level for a request |
| `/idv-methods` | Select sufficient, non-excessive verification methods |
| `/idv-minimise` | Design data-minimising verification using data already held |
| `/idv-nominee` | Verify a nominee or guardian before rights exercise |
| `/idv-antifraud` | Apply anti-fraud and anti-impersonation controls |
| `/idv-failed` | Handle a failed verification proportionately |
| `/idv-audit` | Produce a verification audit trail |

---

## Related Skills

- `dpdp-privacy-by-design-skill.md` — Verification UX and minimisation
- `dpdp-children-data-skill.md` — Parental/guardian verification
- `dpdp-incident-response-skill.md` — Fraudulent-request handling

---

## Skill Guardrails

- **Never collect more identity data** than necessary to verify a request.
- **Always match** verification strength to request risk — do not over-verify low-risk requests.
- **Always delete** verification data once the request is resolved (retain only the audit record).
- **Never refuse** a genuine request for lack of an unreasonable identity document.
- **Always verify** nominees and guardians against the underlying record and trigger event.

---

## References

- DPDP Act, 2023 — Sections 11–14 (Data Principal rights and nomination)
- MeITY DPDP Rules, 2025 — Rule 10 (rights request handling)
