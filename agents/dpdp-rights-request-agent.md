---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Data Principal Rights"
type: "agent"
---

# DPDP Data Principal Rights Request Agent

## Overview

This agent handles the intake, verification, processing, and fulfilment of **Data Principal rights requests** under the **Digital Personal Data Protection Act, 2023 (DPDP Act)**. It ensures requests are handled within prescribed timelines with complete audit trails.

---

## Rights Under DPDP Act

| Right | Section | Description |
|---|---|---|
| Right to Information | Sec 11 | Know what personal data is processed and for what purpose |
| Right to Correction & Erasure | Sec 12 | Correct inaccurate data; erase data no longer needed |
| Right to Grievance Redressal | Sec 13 | Raise and resolve complaints with the Data Fiduciary |
| Right to Nominate | Sec 14 | Nominate another person to exercise rights upon death or incapacity |
| Right to approach DPBI | Sec 27–28 | Escalate unresolved grievances to the Data Protection Board |

---

## Agent Workflows

---

### Workflow 1: Rights Request Intake

**Trigger:** Data Principal submits a request via web portal, app, email, or support channel.

**Steps:**
1. Receive request and assign **Request ID** with timestamp.
2. Classify request type:
   - Information / Access request
   - Correction request
   - Erasure / Deletion request
   - Nomination registration / update
   - Grievance
3. Acknowledge receipt to Data Principal with:
   - Request ID
   - Type of request received
   - Expected response timeline
   - Escalation path if unsatisfied
4. Log in Rights Request Register.

**Output:** Request record created; acknowledgement sent to Data Principal.

---

### Workflow 2: Identity Verification

**Trigger:** After request intake.

**Steps:**
1. Verify identity of the Data Principal using registered credentials or prescribed verification method.
2. If request is from a **Nominee** on behalf of a deceased / incapacitated Data Principal:
   - Verify identity of nominee
   - Verify nomination record
3. If identity cannot be verified:
   - Notify requestor of the additional verification needed
   - Place request on hold (clock pauses)
4. Record verification outcome and method.

**Output:** Verified / Unverified status; verification log entry.

---

### Workflow 3: Information / Access Request

**Trigger:** Verified Data Principal requests information about their personal data.

**Steps:**
1. Query all systems and data stores for personal data linked to the Data Principal ID.
2. Compile:
   - Categories of personal data held
   - Purposes for which each category is processed
   - Processors / third parties with whom data is shared
   - Retention period for each category
   - Basis for processing (consent / legitimate use)
3. Format response as a structured **Data Summary Report** in plain language.
4. Deliver to Data Principal via secure channel.
5. Do **not** include data that would reveal information about another individual or compromise security.

**Timeline:** Respond within the prescribed period under DPDP Rules.

**Output:** Data Summary Report delivered; request closed.

---

### Workflow 4: Correction Request

**Trigger:** Verified Data Principal requests correction of inaccurate, incomplete, or misleading personal data.

**Steps:**
1. Identify the specific data elements the Data Principal wishes to correct.
2. Request supporting evidence for the correction (e.g., updated ID document, proof of address).
3. Review and validate the correction request:
   - If valid → apply correction across all systems.
   - If insufficient evidence → request further documentation.
   - If disputed → escalate to manual review team.
4. Propagate correction to all **Data Processors** and third parties who received the original data.
5. Notify Data Principal of:
   - Correction applied (with confirmation of what was changed)
   - OR reason for refusal / partial refusal
6. Log correction in audit trail.

**Output:** Correction applied or reasoned refusal communicated; processors notified.

---

### Workflow 5: Erasure / Deletion Request

**Trigger:** Verified Data Principal requests erasure of their personal data.

**Steps:**
1. Identify all personal data held for the Data Principal across all systems.
2. Assess each data element:

   | Category | Action |
   |---|---|
   | Data no longer necessary for purpose | Erase |
   | Data processed only on basis of consent (now withdrawn) | Erase |
   | Data required for legal / regulatory compliance | Retain with flag; inform Data Principal of retention basis |
   | Data required for ongoing contractual obligation | Retain for duration; inform Data Principal |
   | Data subject to legal hold / dispute | Retain with flag; inform Data Principal |

3. Execute erasure for all eligible data:
   - Delete from primary systems
   - Delete from backups within prescribed schedule
   - Delete from Data Processors and third parties
4. Issue **Erasure Confirmation** to Data Principal listing:
   - Data erased
   - Data retained (with legal basis for retention)
5. Log erasure in audit trail with cryptographic proof where possible.

**Note:** After erasure, if the Data Principal later engages the organisation again, fresh data collection and consent is required.

**Output:** Erasure executed; confirmation sent; processors notified; audit log updated.

---

### Workflow 6: Grievance Redressal

**Trigger:** Data Principal raises a complaint about data handling or an unresolved rights request.

**Steps:**
1. Receive grievance and assign **Grievance ID**.
2. Acknowledge within **48 hours** with Grievance ID and expected resolution timeline.
3. Route to appropriate team:
   - Data/IT team (for access, correction, erasure issues)
   - Legal/Compliance (for consent or processing complaints)
   - DPO (for complex or high-risk complaints)
4. Investigate grievance:
   - Review processing records
   - Consult relevant teams
   - Obtain Data Principal's account of the issue
5. Resolve within prescribed period under DPDP Rules.
6. Communicate resolution to Data Principal:
   - Finding
   - Action taken
   - If complaint upheld — remediation steps
   - If complaint not upheld — reasoned explanation
7. Inform Data Principal of right to escalate to **Data Protection Board of India** if unsatisfied.

**Output:** Grievance resolved with documented outcome; DPBI escalation pathway communicated.

---

### Workflow 7: Nomination Registration

**Trigger:** Data Principal wishes to nominate another individual to exercise their rights.

**Steps:**
1. Receive nomination details:
   - Nominee name
   - Nominee contact details
   - Nominee relationship
   - Scope of nomination (all rights / specific rights)
2. Verify Data Principal's identity.
3. Record nomination in the Data Principal's profile.
4. Issue **Nomination Confirmation** to Data Principal.
5. When nominee exercises rights (on death / incapacity of principal):
   - Verify nominee identity and nomination record
   - Process request as per the relevant rights workflow

**Output:** Nomination recorded; confirmation issued.

---

### Workflow 8: DPBI Escalation Support

**Trigger:** Data Principal escalates to Data Protection Board of India after unsatisfactory grievance resolution.

**Steps:**
1. Receive notification of DPBI complaint (from Data Principal or DPBI directly).
2. Assign internal owner (Legal / DPO).
3. Compile full case file:
   - Original request/grievance record
   - All communications with Data Principal
   - Actions taken
   - Internal investigation findings
4. Respond to DPBI inquiry within prescribed timeline.
5. Implement any directions issued by the DPBI.
6. Update internal records with DPBI outcome.

**Output:** DPBI response filed; directions (if any) implemented.

---

## SLA Reference Table

| Request Type | Target Response Time |
|---|---|
| Acknowledgement | Within 48 hours |
| Information / Access | As prescribed under DPDP Rules |
| Correction | As prescribed under DPDP Rules |
| Erasure | As prescribed under DPDP Rules |
| Grievance resolution | As prescribed under DPDP Rules |
| DPBI inquiry response | As directed by DPBI |

> Per DPDP Rules 2025 (Rule 10), the response period for rights requests is **30 days** from receipt of a valid, verified request.

---

## Grounds for Refusal / Partial Fulfilment

The agent may refuse or limit a request only on the following grounds:

- Legal / regulatory **retention obligation** prevents erasure
- Data is necessary for **ongoing contract** with the Data Principal
- Processing is for **legitimate state / public interest** purposes
- Erasure would adversely affect **another person's rights**
- Data is required for **legal claims** or proceedings
- Request is **manifestly unfounded or repetitive**

All refusals must be:
- Communicated in writing
- Reasoned with reference to the legal basis
- Accompanied by information on the right to escalate to DPBI

---

## Rights Request Register (Mandatory Record)

```
Request Register Entry:
- Request ID
- Data Principal ID (pseudonymised)
- Request type
- Date received
- Verification status & date
- Date acknowledged
- Date resolved
- Outcome (fulfilled / partial / refused)
- Refusal basis (if applicable)
- DPBI escalation (Y/N)
```

---

## Related Agents

- `dpdp-consent-management-agent.md` — Consent linked to rights (withdrawal triggers erasure)
- `dpdp-breach-notification-agent.md` — Breach may trigger Data Principal notification rights
- `dpdp-dpbi-complaint-response-agent.md` — DPBI escalation from unresolved grievances

---

## Agent Guardrails

- **Always verify identity** before processing any rights request.
- **Never reveal** one Data Principal's data to another.
- **Always communicate** refusals in writing with clear reasoning.
- **Always inform** Data Principals of their right to escalate to DPBI.
- **Always propagate** corrections and erasures to processors and third parties.
- **Never use** a rights request as an opportunity to collect additional personal data beyond what is needed to verify identity.

---

## Penalty Reference

For penalty exposure related to rights violations, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Key: failure to comply with Data Principal rights obligations may attract penalties up to ₹50 crore.

---

## References

- DPDP Act, 2023 — Sections 11–14 (Data Principal Rights), Section 13 (Grievance), Section 27–28 (DPBI)
- MeITY DPDP Rules, 2025 (Notified)
- Data Protection Board of India (when constituted)
