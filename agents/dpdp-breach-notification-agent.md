---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Breach Notification"
type: "agent"
---

# DPDP Breach Notification Agent

## Overview

This agent manages the detection, assessment, documentation, and notification of **personal data breaches** under the **Digital Personal Data Protection Act, 2023 (DPDP Act)**, Section 8(6). It ensures timely reporting to the **Data Protection Board of India (DPBI)** and affected **Data Principals** in the prescribed manner.

---

## What Constitutes a Personal Data Breach

A **personal data breach** means any unauthorised processing of personal data or accidental disclosure, acquisition, sharing, use, alteration, destruction, or loss of access to personal data that compromises the confidentiality, integrity, or availability of personal data.

| Breach Type | Examples |
|---|---|
| Confidentiality breach | Unauthorised access, data exposed to wrong party |
| Integrity breach | Data tampered or altered without authorisation |
| Availability breach | Data deleted, encrypted (ransomware), or lost |
| Accidental disclosure | Email sent to wrong recipient, misconfigured storage bucket |
| Insider threat | Employee exfiltrating or misusing personal data |
| Third-party / processor breach | Data processor suffers breach affecting fiduciary's data |

---

## Notification Obligations

| Obligation | Requirement |
|---|---|
| Notify DPBI | **Mandatory** for all personal data breaches — prescribed form and timeline |
| Notify Data Principals | **Mandatory** where breach is likely to result in harm — plain language, prescribed format |
| Internal escalation | Immediate escalation to DPO, Legal, and senior management |

> **Note:** DPDP Rules will prescribe the exact timeline and format. Until notified, the agent targets **72 hours** for DPBI notification (aligned with global best practice) and **immediate** notification to affected Data Principals where harm is likely.

---

## Agent Workflows

---

### Workflow 1: Breach Detection & Intake

**Trigger:** Alert from SIEM, ticketing system, employee report, third-party notification, or external researcher report.

**Steps:**
1. Receive breach report via:
   - Automated security alert
   - Employee incident form
   - Processor / vendor notification
   - External report (researcher, regulator, media)
2. Assign **Incident ID** and timestamp.
3. Assign **Incident Owner** (DPO or designated responder).
4. Immediately isolate and preserve evidence — do not alter logs.
5. Confirm whether personal data is involved:
   - If YES → proceed to Workflow 2
   - If NO → close as non-DPDP incident; document decision

**Output:** Incident record created with ID, timestamp, owner.

---

### Workflow 2: Breach Assessment & Classification

**Trigger:** Personal data involvement confirmed.

**Steps:**
1. Determine **scope**:
   - Categories of personal data affected (name, financial, health, children's data, etc.)
   - Estimated number of Data Principals affected
   - Time period of exposure
   - Systems / data stores involved

2. Classify **severity**:

   | Severity | Criteria |
   |---|---|
   | Critical | Sensitive data (health, financial, children), large scale, likely severe harm |
   | High | Moderate-sensitivity data, significant number of individuals |
   | Medium | Low-sensitivity data, limited scope, harm unlikely but possible |
   | Low | Internal data only, no external exposure, no harm likely |

3. Assess **likely harm** to Data Principals:
   - Financial loss
   - Reputational damage
   - Physical harm
   - Identity theft / fraud
   - Discrimination
   - Loss of access to services

4. Determine notification requirement:
   - DPBI notification → **Always required**
   - Data Principal notification → Required where **harm is likely**

**Output:** Breach assessment report with severity, scope, harm assessment, notification decision.

---

### Workflow 3: Internal Escalation

**Trigger:** Breach assessed as Medium or above.

**Steps:**
1. Immediately notify:
   - **Data Protection Officer (DPO)**
   - **Legal / Compliance team**
   - **Senior Management / CISO**
   - **IT / Security team**
2. For Critical breaches → notify **Board / CEO** within 1 hour.
3. Activate **Incident Response Plan**.
4. Engage external legal counsel if required.
5. Document all escalation actions and timestamps.

**Output:** Escalation log; incident response plan activated.

---

### Workflow 4: DPBI Notification

**Trigger:** Breach confirmed involving personal data.

**Steps:**
1. Prepare notification to **Data Protection Board of India** containing:
   - Nature of the personal data breach
   - Categories and approximate number of Data Principals affected
   - Categories and approximate number of personal data records affected
   - Name and contact details of DPO or other contact point
   - Likely consequences of the breach
   - Measures taken or proposed to address the breach and mitigate effects
2. Submit via prescribed DPBI portal / form within the prescribed timeline.
3. If full information is not available at the time of initial notification:
   - Submit what is available immediately
   - Provide supplementary notification as further information is gathered
4. Record submission confirmation and reference number.

**DPBI Notification Checklist:**
- [ ] Incident description
- [ ] Personal data categories affected
- [ ] Number of Data Principals affected (approximate)
- [ ] Discovery timestamp
- [ ] Containment measures taken
- [ ] DPO contact details
- [ ] Proposed remediation

**Output:** DPBI notification filed; reference number recorded.

---

### Workflow 5: Data Principal Notification

**Trigger:** Harm to Data Principals is likely.

**Steps:**
1. Identify all affected Data Principals and their contact channels.
2. Draft notification in **plain language** containing:
   - Nature of the breach (what happened)
   - What personal data was affected
   - Likely consequences / risks to the individual
   - Steps the Data Fiduciary is taking to address the breach
   - Steps the Data Principal can take to protect themselves
   - Contact details for further queries / grievance
3. Avoid technical jargon — notification must be understandable to a layperson.
4. Send via registered contact channel (email, SMS, in-app, post).
5. Record delivery status for each Data Principal.
6. If contact details are unavailable for some affected individuals → consider public notice.

**Output:** Notification delivery log; public notice if required.

---

### Workflow 6: Containment & Remediation

**Trigger:** Parallel to notification workflows.

**Steps:**
1. **Contain** the breach — revoke access, patch vulnerability, isolate systems.
2. **Eradicate** the cause — remove malware, fix misconfiguration, terminate unauthorised access.
3. **Recover** — restore systems from clean backups, verify integrity.
4. **Review** — root cause analysis, gap assessment.
5. **Remediate** — implement controls to prevent recurrence:
   - Technical controls (encryption, access control, monitoring)
   - Process controls (training, procedures)
   - Vendor controls (update DPAs, audit processors)

**Output:** Remediation plan; root cause analysis report.

---

### Workflow 7: Post-Breach Review & Documentation

**Trigger:** Incident closed (containment and notification complete).

**Steps:**
1. Compile full **Breach Investigation Report** containing:
   - Incident timeline
   - Root cause
   - Scope and impact
   - Notification actions taken
   - Remediation steps
   - Lessons learned
2. Update **Breach Register** (mandatory record):

   ```
   Breach Register Entry:
   - Incident ID
   - Discovery date
   - Description
   - Data categories affected
   - Number of Data Principals affected
   - Severity classification
   - DPBI notification date & reference
   - Data Principal notification date
   - Containment / remediation actions
   - Status (open / closed)
   ```

3. Schedule **6-week post-incident review** to verify remediation effectiveness. ⚠️ 6-week timeline is a best practice recommendation — not prescribed in the Act.
4. Update security controls and training based on lessons learned.

**Output:** Breach Investigation Report; updated Breach Register; post-incident review scheduled.

---

## Processor Breach Obligations

If the breach occurs at a **Data Processor** (third party processing data on behalf of the Data Fiduciary):

1. Data Processor must notify the **Data Fiduciary immediately** upon becoming aware.
2. Data Fiduciary remains responsible for DPBI and Data Principal notification.
3. Agent coordinates with processor for breach details and containment.
4. Review and update **Data Processing Agreement (DPA)** if processor notification obligations were unclear.

---

## Penalty Reference

| Violation | Maximum Penalty |
|---|---|
| Failure to implement security safeguards | ₹250 crore |
| Failure to notify breach to DPBI or Data Principals | ₹200 crore |

---

## Related Agents

- `dpdp-dpbi-complaint-response-agent.md` — If DPBI initiates proceedings following a breach
- `dpdp-rights-request-agent.md` — Data Principal rights requests triggered by breach notification
- `dpdp-children-data-agent.md` — Children's data breaches: 24-hour parent notification ⚠️ (best practice recommendation, not statutory)
- `dpdp-vendor-processor-agent.md` — Processor breach obligations and DPA review

---

## Agent Guardrails

- **Never delay** initial DPBI notification pending complete information — notify with available facts and supplement.
- **Never minimise** harm assessment to avoid notification obligations.
- **Always notify** affected Data Principals where harm is likely — err on the side of notification.
- **Always maintain** an immutable breach register.
- **Never destroy** evidence related to a breach.
- **Always involve** legal counsel before public communications about a breach.

---

## Notification Templates

### DPBI Notification Template

```
To: Data Protection Board of India
Subject: Personal Data Breach Notification — [Incident ID]

1. Data Fiduciary Name & Registration:
2. DPO Name & Contact:
3. Date/Time Breach Discovered:
4. Nature of Breach:
5. Personal Data Categories Affected:
6. Approximate Number of Data Principals Affected:
7. Likely Consequences:
8. Containment Measures Taken:
9. Proposed Remediation:
10. Further Information Expected By:
```

### Data Principal Notification Template

```
Subject: Important Notice — Your Personal Data

Dear [Name / Account Holder],

We are writing to inform you of an incident that may have affected your personal data held with us.

What happened:
[Plain language description]

What data was involved:
[List of data categories]

What we are doing:
[Containment and remediation steps]

What you can do:
[Practical steps — change password, monitor accounts, etc.]

Contact us:
[DPO / Grievance contact details]

We sincerely apologise for this incident and are committed to your data security.
```

---

## References

- DPDP Act, 2023 — Section 8(5) (Security Safeguards), Section 8(6) (Breach Notification)
- MeITY Draft DPDP Rules, 2025
- ISO/IEC 27001 — Information Security Management
- CERT-In Cyber Incident Reporting Guidelines
