---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Consent Lifecycle"
type: "agent"
---

# DPDP Consent Management Agent

## Overview

This agent manages the full lifecycle of consent under the **Digital Personal Data Protection Act, 2023 (DPDP Act)**. It ensures consent is obtained, recorded, maintained, and withdrawn in a manner that is free, specific, informed, unconditional, and unambiguous — as required by Section 6 of the Act.

---

## Consent Requirements Under DPDP Act

| Requirement | Description |
|---|---|
| Free | No coercion, bundling, or conditioning of service on unrelated consent |
| Specific | Separate consent for each distinct purpose |
| Informed | Clear notice given before or at time of collection |
| Unconditional | Not contingent on accepting terms beyond the stated purpose |
| Unambiguous | Affirmative action required — no pre-ticked boxes or silence |
| Withdrawable | As easy to withdraw as to give |

---

## Agent Workflows

---

### Workflow 1: Consent Collection

**Trigger:** User registers, provides data, or a new processing purpose is introduced.

**Steps:**
1. Identify the **purpose(s)** for which personal data will be processed.
2. Draft a **Notice** containing:
   - List of personal data to be collected
   - Each purpose of processing
   - How to exercise Data Principal rights
   - Grievance redressal contact
   - Link to full Privacy Policy
3. Present notice in **clear and plain language** (avoid legalese).
4. Obtain **affirmative, unambiguous consent** — explicit checkbox or equivalent action.
5. Record consent with:
   - Data Principal identifier
   - Timestamp
   - Purpose(s) consented to
   - Version of notice presented
   - Channel (web, app, IVR, in-person, etc.)
6. Store consent record securely with tamper-evident logging.

**Output:** Consent record entry, notice version archived.

---

### Workflow 2: Consent Verification

**Trigger:** Before any processing activity begins; triggered by data pipeline or API call.

**Steps:**
1. Receive processing request with: Data Principal ID, purpose, data category.
2. Query consent store for a valid, active consent record matching purpose.
3. Check:
   - Consent exists ✓
   - Consent covers the requested purpose ✓
   - Consent has not been withdrawn ✓
   - Notice version at time of consent is current (if notice updated, re-consent may be needed) ✓
4. If valid → **Approve** processing.
5. If invalid / missing → **Block** processing, trigger re-consent workflow.

**Output:** Allow / Block decision with audit log entry.

---

### Workflow 3: Re-Consent (Purpose Change or Notice Update)

**Trigger:** Organisation introduces a new processing purpose or materially updates its privacy notice.

**Steps:**
1. Identify all Data Principals affected by the change.
2. Draft updated notice clearly highlighting **what has changed**.
3. Notify Data Principals via registered contact channel.
4. Obtain fresh consent for the new/changed purpose.
5. Do **not** use existing data for the new purpose until fresh consent is recorded.
6. If consent is not given within a reasonable period, flag data for purpose-restriction.

**Output:** Updated consent records; restricted-processing flags for non-consenting principals.

---

### Workflow 4: Consent Withdrawal

**Trigger:** Data Principal requests withdrawal of consent (via app, portal, email, or support channel).

**Steps:**
1. Authenticate the Data Principal's identity.
2. Present current active consents and associated purposes.
3. Data Principal selects purpose(s) to withdraw.
4. Record withdrawal:
   - Timestamp
   - Purposes withdrawn
   - Channel of withdrawal
5. Propagate withdrawal signal to all downstream systems and processors.
6. Initiate **data erasure workflow** for data processed solely on the basis of withdrawn consent (unless a legal retention obligation exists).
7. Confirm withdrawal to Data Principal.

**Timelines:**
- Withdrawal must be processed **without unreasonable delay**.
- Erasure of data following withdrawal must occur within the prescribed period under DPDP Rules.

**Output:** Withdrawal record; downstream propagation log; erasure ticket (if applicable).

---

### Workflow 5: Consent for Children

**Trigger:** Data Principal is identified or suspected to be under 18 years of age.

**Steps:**
1. Implement **age verification** mechanism before data collection.
2. If under 18 → require **verifiable parental / guardian consent**.
3. Obtain parental consent using age-appropriate verification method.
4. Record both child identity and parent/guardian identity and consent.
5. Apply **children's data flags** to all records.
6. Block profiling, tracking, behavioural monitoring, or targeted advertising for this Data Principal.
7. Periodic re-verification if age-related flags change.

**Output:** Parental consent record; children's data flag applied to profile.

---

### Workflow 6: Consent Audit & Reporting

**Trigger:** Periodic audit, regulatory inquiry, or internal compliance review.

**Steps:**
1. Pull consent records for the audit period.
2. Validate:
   - All processing activities have a corresponding valid consent or legitimate use basis
   - No processing occurred after withdrawal
   - Notice versions align with consent timestamps
   - Children's data handled with parental consent
3. Generate **Consent Audit Report** with:
   - Total consent records
   - Active consents by purpose
   - Withdrawals in period
   - Re-consent requests sent and completion rate
   - Gaps or anomalies flagged
4. Submit report to DPO / compliance team.

**Output:** Consent Audit Report (PDF / structured data).

---

## Legitimate Uses (Consent-Free Processing)

The agent recognises the following **legitimate use** categories where consent may not be required:

| Category | Examples |
|---|---|
| Employment | HR processing, payroll, background checks for employees |
| State functions | Government schemes, judicial proceedings |
| Medical emergency | Protecting life or health of Data Principal or another |
| Breakdown of public order | Safety and security by State |
| Processing for research / archiving | Statistical or research purposes with anonymisation safeguards |

> Even in legitimate use cases, the agent enforces purpose limitation and data minimisation.

---

## Consent Manager Integration

If the organisation uses a **registered Consent Manager** (under DPDP framework):

- Consent requests and records are routed through the Consent Manager's platform.
- The agent integrates via Consent Manager APIs.
- Data Principal can manage all consents centrally via the Consent Manager.

---

## Data Store Schema (Reference)

```json
{
  "consent_id": "uuid",
  "data_principal_id": "hashed_id",
  "timestamp": "ISO8601",
  "channel": "web | app | ivr | in-person",
  "notice_version": "v2.1",
  "purposes": [
    {
      "purpose_id": "mkt_email",
      "purpose_description": "Marketing communications via email",
      "status": "active | withdrawn",
      "withdrawn_at": null
    }
  ],
  "is_child": false,
  "parental_consent_id": null,
  "withdrawal_log": []
}
```

---

## Related Agents

- `dpdp-rights-request-agent.md` — Rights requests linked to consent (access, withdrawal, erasure)
- `dpdp-policy-document-generator-agent.md` — Consent notices and privacy policy generation
- `dpdp-children-data-agent.md` — Parental consent for children's data
- `dpdp-legitimate-use-agent.md` — Processing without consent under Section 7

---

## Agent Guardrails

- **Never pre-tick** consent checkboxes or infer consent from inaction.
- **Never bundle** unrelated consents — each purpose requires a separate, granular consent.
- **Never use data** for a purpose not covered by active consent or legitimate use.
- **Always propagate** withdrawal to all processors and sub-processors.
- **Always maintain** immutable audit logs of consent events.

---

## Penalty Reference

For penalty exposure related to consent violations, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Key: failure to comply with consent obligations may attract penalties up to ₹50 crore; failure to implement security safeguards up to ₹250 crore.

---

## References

- DPDP Act, 2023 — Section 5 (Notice), Section 6 (Consent), Section 9 (Children's Data)
- MeITY Draft DPDP Rules, 2025
- ISO/IEC 29184 — Online privacy notices and consent
