---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Consent Manager"
type: "skill"
---

# DPDP Consent Manager Skill

## Skill Identity

**Skill Name:** dpdp-consent-manager
**Domain:** Consent Manager Framework, Consent Lifecycle, Consent Architecture
**Skill Type:** Technical, Regulatory, Operations
**Applicable To:** Consent Manager Entities, Data Fiduciaries integrating with Consent Managers, Technology Teams, DPOs

---

## Skill Purpose

Operationalise the **Consent Manager** framework under the DPDP Act — enabling centralised, interoperable consent management for Data Principals across multiple Data Fiduciaries. Covers both the Consent Manager entity obligations and the Data Fiduciary integration requirements.

---

## What is a Consent Manager?

Under the DPDP Act, a **Consent Manager** is a registered entity that:
- Acts as a **single point of contact** for Data Principals to give, manage, review, and withdraw consent
- Provides an interoperable platform accessible to all registered Data Fiduciaries
- Maintains **consent artefacts** in a standardised, machine-readable format
- Enables Data Principals to exercise consent rights across multiple organisations from one interface

```
DATA PRINCIPAL
      │
      │ gives / manages / withdraws consent
      ▼
CONSENT MANAGER (registered entity)
      │
      ├──► Data Fiduciary A (consent signal)
      ├──► Data Fiduciary B (consent signal)
      └──► Data Fiduciary C (consent signal)
```

> **Regulatory Status (2025):** The Consent Manager registration framework has not yet been finalised under DPDP Rules. This skill anticipates the framework based on the Account Aggregator model (RBI) and the draft DPDP Rules.

---

## Skill Capabilities

---

### Capability 1: Consent Manager Registration & Setup

**Trigger:** "register as consent manager", "set up consent manager", "become a consent manager under DPDP"

**Steps:**
1. Assess eligibility:
   - Entity must be registered in India
   - Must meet prescribed technical, financial, and governance standards (to be notified)
   - Must be free from conflicts of interest with Data Fiduciaries

2. Prepare **Registration Application** for DPBI / MeITY containing:
   - Entity details and incorporation documents
   - Technical architecture description
   - Security certifications (ISO 27001, SOC 2)
   - Privacy policy and grievance mechanism
   - Financial viability evidence
   - Governance and ownership structure
   - Proposed fee structure
   - Interoperability standards compliance

3. Post-registration:
   - Publish registered Consent Manager status publicly
   - Integrate with DPBI Consent Manager registry
   - Onboard Data Fiduciaries to the platform
   - Launch Data Principal app / portal

**Output:** Registration application; post-registration setup checklist.

---

### Capability 2: Consent Artefact Architecture

**Trigger:** "consent artefact design", "consent token", "machine-readable consent", "consent data model"

**Steps:**
1. Design the **Consent Artefact** — a standardised, digitally signed consent record:

```json
{
  "consent_id": "uuid-v4",
  "version": "1.0",
  "issued_at": "2025-06-15T10:30:00Z",
  "data_principal": {
    "id": "dp_hashed_identifier",
    "verification_method": "aadhaar_otp | mobile_otp | email_otp"
  },
  "data_fiduciary": {
    "id": "df_registered_id",
    "name": "Organisation Name",
    "dpbi_registration": "DF-XXXX"
  },
  "consent_manager": {
    "id": "cm_registered_id",
    "name": "Consent Manager Name",
    "dpbi_registration": "CM-XXXX"
  },
  "purposes": [
    {
      "purpose_id": "p001",
      "description": "Marketing communications via email",
      "data_categories": ["email_address", "purchase_history"],
      "frequency": "ongoing",
      "expiry": "2026-06-15T00:00:00Z",
      "status": "active"
    }
  ],
  "consent_mode": "explicit",
  "notice_version": "v2.3",
  "notice_url": "https://df.example/privacy-notice-v2.3",
  "signature": {
    "algorithm": "RS256",
    "value": "digital_signature_of_artefact"
  },
  "withdrawal": {
    "withdrawn_at": null,
    "withdrawal_channel": null
  }
}
```

2. Implement **digital signing** of consent artefacts — tamper-evident.
3. Design **consent artefact registry** — immutable log of all consent events.
4. Implement consent artefact **versioning** — track changes over time.
5. Expose consent artefacts via **standardised API** to Data Fiduciaries.

**Output:** Consent artefact schema; signing mechanism; registry design; API specification.

---

### Capability 3: Data Principal Consent Portal

**Trigger:** "consent portal design", "Data Principal consent dashboard", "consent app", "manage my consents"

**Steps:**
1. Design **Data Principal Consent Dashboard** with:

   ```
   CONSENT DASHBOARD FEATURES
   ─────────────────────────────────────────────────
   □ Unified login (Aadhaar / DigiLocker / mobile OTP)
   □ List of all Data Fiduciaries with active consents
   □ Per-fiduciary consent detail:
       - Purposes consented to
       - Data categories covered
       - Consent date and expiry
       - Status (active / withdrawn / expired)
   □ Withdraw consent (per purpose or all)
   □ View consent history (full audit trail)
   □ New consent requests from Data Fiduciaries
   □ Nomination management
   □ Grievance filing
   □ Notification preferences
   ─────────────────────────────────────────────────
   ```

2. Design for **accessibility** — support for multiple languages, low-bandwidth, feature phones.
3. Implement **plain language** for all consent descriptions — no legalese.
4. Provide **visual consent status indicators** (active / withdrawn / expired).
5. Implement push / SMS / email **consent event notifications** to Data Principal.

**Output:** Consent portal design specification; accessibility plan; notification design.

---

### Capability 4: Data Fiduciary Integration

**Trigger:** "integrate with consent manager", "connect to consent manager API", "consent manager integration for our app"

**Steps:**
1. Register Data Fiduciary on the Consent Manager platform.
2. Integrate via **Consent Manager API**:

   ```
   CONSENT MANAGER API (reference design)
   ────────────────────────────────────────────────────────
   POST /consent/request
        Body: {data_principal_id, purposes[], notice_url, expiry}
        Response: {consent_request_id, redirect_url_to_CM_portal}

   GET  /consent/status/{consent_request_id}
        Response: {status: pending|approved|rejected, consent_artefact}

   POST /consent/verify
        Body: {consent_artefact, purpose_id, data_categories[]}
        Response: {valid: true|false, reason}

   POST /consent/withdrawal-notification (webhook)
        Body: {consent_id, withdrawn_purposes[], timestamp}

   GET  /consent/history/{data_principal_id}
        Response: {consent_events[]}
   ────────────────────────────────────────────────────────
   ```

3. Implement **consent verification gate** — check consent artefact validity before any processing.
4. Subscribe to **withdrawal webhooks** — propagate withdrawal to all downstream systems immediately.
5. Store consent artefact reference (not full PII) locally for audit purposes.
6. Test integration with Consent Manager sandbox environment.

**Output:** API integration; consent verification gate; withdrawal webhook handler; test results.

---

### Capability 5: Consent Withdrawal Propagation

**Trigger:** "process consent withdrawal", "withdrawal notification received", "propagate withdrawal"

**Steps:**
1. Receive withdrawal event from Consent Manager (webhook or polling).
2. Identify all systems processing data under the withdrawn consent.
3. Immediately halt processing in all affected systems.
4. Propagate withdrawal to all processors / sub-processors with access.
5. Initiate **data erasure workflow** for data processed solely on withdrawn consent.
6. Confirm withdrawal processing to Consent Manager (acknowledgement event).
7. Log withdrawal and downstream actions in audit trail.
8. Notify Data Principal of withdrawal completion via Consent Manager.

**SLA:** Withdrawal processing must be immediate — no unreasonable delay.

**Output:** Withdrawal processed; downstream systems updated; erasure initiated; acknowledgement sent.

---

### Capability 6: Consent Manager Audit & Compliance

**Trigger:** "consent manager audit", "CM compliance", "consent platform audit", "DPBI consent manager review"

**Steps:**
1. Conduct periodic **platform audit** covering:
   - Consent artefact integrity (tamper-evident logs)
   - Data Principal authentication security
   - Withdrawal propagation accuracy and timeliness
   - Data Fiduciary onboarding KYC and compliance
   - Platform security (ISO 27001 / SOC 2)
   - Availability and uptime (SLA compliance)
   - Grievance resolution rate and timeliness
   - Staff access controls and training

2. Generate **Consent Manager Compliance Report**:
   - Total Data Principals on platform
   - Total Data Fiduciaries registered
   - Consent events in period (given / withdrawn / expired)
   - Withdrawal propagation SLA compliance
   - Grievances received and resolved
   - Security incidents (if any)
   - Audit findings and remediation

3. Submit to DPBI as required.

**Output:** CM Compliance Report; DPBI submission.

---

### Capability 7: Grievance Handling for Consent Manager

**Trigger:** "consent manager grievance", "Data Principal complaint about consent", "CM grievance procedure"

**Steps:**
1. Receive grievance from Data Principal via CM portal / support channel.
2. Classify:
   - Consent not reflected correctly → CM issue
   - Withdrawal not processed by Data Fiduciary → escalate to DF
   - Data Fiduciary not honouring consent → escalate to DF and flag to DPBI
   - CM platform issue → CM resolves directly
3. Acknowledge within 48 hours.
4. Resolve within prescribed period.
5. If issue is with the Data Fiduciary:
   - Formally notify the DF of the grievance
   - Track DF response
   - If DF does not resolve → report to DPBI
6. Communicate resolution to Data Principal.
7. Inform Data Principal of right to approach DPBI.

**Output:** Grievance resolved; DF escalation documented; DPBI referral if warranted.

---

## Consent Manager Obligations Summary

```
CONSENT MANAGER OBLIGATIONS
══════════════════════════════════════════════════════
□ Registered with DPBI / MeITY
□ Platform technically interoperable with all registered DFs
□ Data Principal authentication — secure, accessible
□ Consent artefacts — digitally signed, tamper-evident
□ Withdrawal propagation — immediate, complete
□ Grievance mechanism — accessible, 48-hour acknowledgement
□ Security — ISO 27001 or equivalent
□ Audit — periodic platform audit; report to DPBI
□ DF onboarding — KYC of Data Fiduciaries before registration
□ Independence — no conflict of interest with registered DFs
□ Transparency — published fees, terms, and privacy policy
□ Data minimisation — CM stores only what is needed for consent management
□ No processing of DP data beyond consent management purpose
══════════════════════════════════════════════════════
```

---

## Related Skills

- `dpdp-privacy-by-design-skill.md` — Consent UX design
- `dpdp-contract-clauses-skill.md` — Consent Manager agreements
- `dpdp-children-data-skill.md` — Parental consent

---

## Skill Guardrails

- **Never process** Data Principal personal data for any purpose beyond consent management.
- **Always propagate** withdrawal within prescribed SLA — no delays.
- **Always maintain** consent artefact integrity — no modifications after signing.
- **Never onboard** a Data Fiduciary without proper registration verification.
- **Always inform** Data Principals of their right to approach DPBI.

---

## Quick Commands

| Command | Action |
|---|---|
| `/cm-registration` | Prepare Consent Manager registration application |
| `/cm-artefact-design` | Design consent artefact schema |
| `/cm-portal-design` | Design Data Principal consent portal |
| `/cm-df-integration` | Integrate Data Fiduciary with Consent Manager |
| `/cm-withdrawal` | Process consent withdrawal and propagation |
| `/cm-audit` | Conduct Consent Manager compliance audit |
| `/cm-grievance` | Handle Data Principal grievance on CM platform |

---

## References

- DPDP Act, 2023 — Section 2(7) (Consent Manager), Section 6 (Consent)
- MeITY Draft DPDP Rules, 2025
- RBI Account Aggregator Framework (analogous architecture)
- DEPA — Data Empowerment and Protection Architecture (India Stack)
- ISO/IEC 29184 — Online Privacy Notices and Consent
