---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Incident Response"
type: "skill"
---

# DPDP Incident Response Skill

## Skill Identity

**Skill Name:** dpdp-incident-response
**Domain:** Personal Data Breach Response, Incident Management, Crisis Communication
**Skill Type:** Security, Operations, Legal, Communications
**Applicable To:** DPOs, CISO / Security Teams, Legal, Communications, Senior Management, Incident Response Teams

---

## Skill Purpose

Provide a structured, time-critical framework for detecting, classifying, containing, and recovering from personal data incidents — and meeting DPDP Act notification obligations to the DPBI and affected Data Principals within prescribed timelines.

---

## Incident Response Phases

```
DPDP INCIDENT RESPONSE LIFECYCLE
────────────────────────────────────────────────────────────
PHASE 1: DETECT & REPORT         (Hour 0–1)
PHASE 2: TRIAGE & CLASSIFY       (Hour 1–4)
PHASE 3: ESCALATE & CONTAIN      (Hour 4–24)
PHASE 4: ASSESS & NOTIFY         (Hour 24–72)
PHASE 5: ERADICATE & RECOVER     (Day 3–14)
PHASE 6: POST-INCIDENT REVIEW    (Day 14–30)
────────────────────────────────────────────────────────────
```

---

## Skill Capabilities

---

### Capability 1: Incident Detection Sources

**Trigger:** "how to detect a breach", "incident detection", "breach indicators", "security monitoring for DPDP"

**Detection Sources:**

| Source | Example Signal |
|---|---|
| SIEM / Security monitoring | Bulk data export outside business hours; anomalous access |
| Intrusion Detection System | Malware detected; lateral movement; C2 traffic |
| DLP system | Large file sent to personal email; USB data copy |
| Cloud security alerts | S3 bucket set to public; misconfigured storage |
| Employee self-report | "I sent the email to the wrong person" |
| Customer report | "I received someone else's data" |
| Vendor / processor notification | "We have experienced a security incident" |
| External researcher | Bug bounty or responsible disclosure report |
| Dark web monitoring | Organisation data appearing on dark web forums |
| Regulatory notification | CERT-In or DPBI alerts organisation |
| Media / social media | Reports of data exposure going public |

**Detection Checklist for SOC / Security Team:**
```
□ Real-time SIEM alerts enabled for personal data access anomalies
□ DLP rules configured for personal data exfiltration
□ Cloud storage misconfiguration alerts active
□ Vendor breach notification procedure defined in all DPAs
□ Employee reporting channel communicated to all staff (not just IT)
□ Dark web monitoring in place for organisation's data
□ Bug bounty / responsible disclosure programme active
```

**Output:** Detection source inventory; monitoring gaps identified.

---

### Capability 2: Incident Triage & Classification

**Trigger:** "classify this incident", "is this a DPDP breach", "incident triage"

**Triage Decision Tree:**

```
INCIDENT TRIAGE FLOWCHART
──────────────────────────────────────────────────────────────
STEP 1: Does the incident involve personal data?
  NO → Log as non-DPDP incident; handle under general security IR
  YES → Proceed to Step 2

STEP 2: What type of breach?
  CONFIDENTIALITY → Unauthorised disclosure / access
  INTEGRITY       → Data altered or corrupted
  AVAILABILITY    → Data lost, deleted, or inaccessible
  COMBINED        → More than one type

STEP 3: What personal data is affected?
  TIER 1 SENSITIVE (health, financial, biometric, children) → CRITICAL
  TIER 2 PERSONAL (name, contact, ID numbers) → HIGH
  TIER 3 PSEUDONYMISED → MEDIUM
  INTERNAL ONLY → LOW

STEP 4: Scale?
  >100,000 individuals → add one severity level
  <1,000 individuals → standard level
  Children affected → CRITICAL regardless of scale

STEP 5: Likely harm to Data Principals?
  Financial loss, identity theft, physical harm → CRITICAL
  Reputational damage, discrimination → HIGH
  Minimal / unlikely harm → MEDIUM or LOW
──────────────────────────────────────────────────────────────
```

**Severity Matrix:**

| Severity | Description | Response SLA |
|---|---|---|
| P1 CRITICAL | Large-scale, sensitive data, likely severe harm | Immediate — 24/7 response |
| P2 HIGH | Sensitive data or significant scale, harm possible | 4-hour response |
| P3 MEDIUM | Limited scope, low-sensitivity, harm unlikely | 24-hour response |
| P4 LOW | Internal only, no external exposure, no harm | 72-hour response |

**Output:** Incident classified with severity; response SLA triggered.

---

### Capability 3: Escalation Matrix

**Trigger:** "who to escalate to", "incident escalation", "notify about breach", "who needs to know"

**Escalation by Severity:**

```
P1 CRITICAL (immediate — within 1 hour)
  □ DPO
  □ CISO / Head of Security
  □ Legal Counsel (internal + external if needed)
  □ CEO / MD
  □ Board (if systemic or reputational)
  □ Head of Communications (media risk)
  □ Relevant BU Head

P2 HIGH (within 4 hours)
  □ DPO
  □ CISO / Head of Security
  □ Legal Counsel
  □ Senior Management

P3 MEDIUM (within 24 hours)
  □ DPO
  □ Security Team Lead
  □ Legal (advisory)

P4 LOW (within 72 hours)
  □ DPO (for awareness)
  □ Security Team Lead
```

**Escalation Communication Template:**

```
INCIDENT ESCALATION ALERT
─────────────────────────────────────────────────────
TO    : [Escalation contacts per matrix above]
FROM  : [Incident responder name]
TIME  : [Date/Time]

INCIDENT ID   : INC-XXXX
SEVERITY      : P[1/2/3/4]
SUMMARY       : [2-sentence description of what happened]
DATA AFFECTED : [Categories; estimated number of Data Principals]
CURRENT STATUS: [Contained / Ongoing / Unknown]
IMMEDIATE ACTION TAKEN: [Steps taken so far]
NEXT ACTION   : [What happens next; owner; timeline]
DPBI NOTIFICATION REQUIRED: [Y / N / Under assessment]
─────────────────────────────────────────────────────
```

**Output:** Escalation completed; all required parties notified.

---

### Capability 4: Containment Playbooks

**Trigger:** "contain the breach", "stop the leak", "containment steps", "breach containment"

**Playbook A — Unauthorised External Access (Hacking / Ransomware):**
```
IMMEDIATE (0–2 hours):
□ Isolate affected systems from network
□ Revoke all active sessions on compromised accounts
□ Block attacker's IP / access vectors at firewall
□ Preserve all logs — do NOT power off (forensic evidence)
□ Engage forensics team (internal or external)
□ Notify CERT-In (within 6 hours per CERT-In Directions)

SHORT-TERM (2–24 hours):
□ Identify full scope of compromise (lateral movement?)
□ Reset credentials on all potentially affected accounts
□ Assess whether data was exfiltrated (vs only encrypted)
□ Restore from clean backups (verify integrity before restore)
□ Patch the exploited vulnerability before reconnecting
```

**Playbook B — Accidental Disclosure (Wrong Recipient / Misconfiguration):**
```
IMMEDIATE (0–2 hours):
□ Identify recipient(s) of misdirected data
□ Contact recipient immediately and request deletion/return
□ Restrict access to the misconfigured resource (storage bucket, file share)
□ Document all exposed data and affected Data Principals
□ Preserve evidence (email logs, access logs)

SHORT-TERM (2–24 hours):
□ Obtain confirmation of deletion from recipient (written)
□ Assess whether data was further distributed
□ Identify configuration error and fix
□ Review similar configurations for the same issue
```

**Playbook C — Insider Threat (Employee Data Theft):**
```
IMMEDIATE (0–2 hours):
□ Revoke system access of suspected insider immediately
□ Preserve all access logs, email logs, device logs — DO NOT ALERT SUSPECT
□ Secure the employee's physical access (building, devices)
□ Involve HR and Legal before any communication with employee
□ Engage forensics — image device before alerting

SHORT-TERM (2–24 hours):
□ Scope the data exfiltrated (DLP logs, cloud upload logs)
□ Identify all affected Data Principals
□ Legal advice on employment action
□ Consider police report (if criminal exfiltration)
```

**Playbook D — Processor / Vendor Breach:**
```
IMMEDIATE (0–2 hours):
□ Receive breach notification from processor
□ Immediately escalate to DPO and Legal
□ Demand full incident details from processor per DPA obligations
□ Assess whether data shared with processor is affected
□ Consider temporarily suspending data transfer to processor

SHORT-TERM (2–24 hours):
□ Obtain processor's containment and investigation report
□ Independently assess scope and affected Data Principals
□ Initiate DPBI notification — Data Fiduciary remains responsible
□ Review DPA — hold processor accountable
□ Assess processor's ongoing reliability
```

**Output:** Containment playbook executed; steps logged with timestamps.

---

### Capability 5: DPDP Notification Decision

**Trigger:** "do we need to notify DPBI", "do we tell customers", "notification decision", "breach notification required"

**Notification Decision Framework:**

```
DPBI NOTIFICATION
─────────────────────────────────────────────────────────
Q: Is this a personal data breach?
   YES → DPBI notification is MANDATORY (no threshold)
   NO  → No DPDP notification required

Timeline: As prescribed by DPDP Rules (pending notification)
          Interim target: Within 72 hours of becoming aware
          If full information unavailable → notify with what is known;
          supplement later

DATA PRINCIPAL NOTIFICATION
─────────────────────────────────────────────────────────
Q: Is harm to Data Principals likely?
   LIKELY HARM → Notification MANDATORY
   HARM POSSIBLE → Notify (err on the side of notification)
   NO LIKELY HARM → May not be required; document decision

What constitutes "likely harm":
  □ Financial loss (bank details, card data exposed)
  □ Identity theft risk (Aadhaar, PAN, passport exposed)
  □ Physical safety risk (location data, domestic abuse victims)
  □ Reputational damage (sensitive personal info exposed)
  □ Loss of access to services (login credentials exposed)
  □ Discrimination risk (health, religion, caste exposed)
─────────────────────────────────────────────────────────
```

**Output:** Notification decision documented with reasoning; notifications prepared.

---

### Capability 6: DPBI Notification Drafting

**Trigger:** "draft DPBI notification", "notify data protection board", "DPBI breach report"

**DPBI Notification — Required Content:**

```
PERSONAL DATA BREACH NOTIFICATION
TO: Data Protection Board of India
─────────────────────────────────────────────────────────────────
1. DATA FIDUCIARY DETAILS
   Organisation Name    :
   Registered Address   :
   Industry / Sector    :
   DPO Name & Contact   :

2. INCIDENT DETAILS
   Incident ID          : INC-XXXX
   Date/Time Discovered :
   Date/Time Occurred   : (if known)
   Nature of Breach     : [Unauthorised access / Accidental disclosure /
                           Ransomware / Insider / Processor breach / Other]

3. PERSONAL DATA AFFECTED
   Categories           : [Name / Contact / Financial / Health / Biometric /
                           Children / National ID / Other]
   Approximate Volume   : [Number of Data Principals affected]
   Sensitivity          : [Sensitive / General personal data]

4. CIRCUMSTANCES
   How breach occurred  : [Brief factual description]
   How discovered       : [Security monitoring / Employee report / External /
                           Vendor notification]
   Duration of exposure : [Known / Unknown]

5. LIKELY CONSEQUENCES
   Potential harms      : [Financial / Identity theft / Reputational /
                           Physical / Discrimination]
   Assessed likelihood  : [High / Medium / Low]

6. CONTAINMENT MEASURES TAKEN
   Immediate steps      : [List actions taken]
   Systems affected     : [Isolated / Patched / Access revoked]

7. DATA PRINCIPAL NOTIFICATION
   Notified?            : [Y / N / In progress]
   Method               : [Email / SMS / In-app / Post / Public notice]
   Date notified        :

8. PROPOSED REMEDIATION
   Technical            :
   Organisational       :
   Timeline             :

9. FURTHER INFORMATION
   Full report expected by :
   Contact for queries     :
─────────────────────────────────────────────────────────────────
```

**Output:** DPBI notification drafted; filed; reference number recorded.

---

### Capability 7: Data Principal Notification Drafting

**Trigger:** "notify customers of breach", "data principal breach notification", "breach communication to users"

**Communication Principles:**
- **Plain language** — no jargon; comprehensible to a layperson
- **Factual** — accurate; not minimising; not catastrophising
- **Actionable** — tell them what they can do to protect themselves
- **Empathetic** — acknowledge the impact; do not be defensive
- **Complete** — include all required information in one communication

**Data Principal Notification Template:**

```
Subject: Important Security Notice — Your Personal Data

Dear [Name / Account Holder],

We are writing to inform you of a security incident that may have
affected your personal data held with [Organisation Name].

WHAT HAPPENED
[Plain language description — 2–3 sentences. When, how discovered.]

WHAT INFORMATION WAS INVOLVED
The following types of your personal data may have been affected:
• [Data type 1, e.g., Name and email address]
• [Data type 2, e.g., Phone number]
• [Data type 3 — if sensitive, be specific and empathetic]

[If no data confirmed affected for this individual:]
While we have no evidence that your specific data was accessed,
we are notifying you as a precaution because [reason].

WHAT WE ARE DOING
• [Step 1 — e.g., We have secured the affected systems]
• [Step 2 — e.g., We are investigating the full scope]
• [Step 3 — e.g., We have notified the Data Protection Board of India]
• [Step 4 — e.g., We have engaged cybersecurity experts]

WHAT YOU CAN DO
To protect yourself, we recommend:
• [Action 1 — e.g., Change your password for our service immediately]
• [Action 2 — e.g., Enable two-factor authentication]
• [Action 3 — e.g., Monitor your bank statements for unusual activity]
• [Action 4 — e.g., Be alert to phishing emails using your name]
• [Free credit monitoring — if financial data affected]

YOUR RIGHTS
Under the Digital Personal Data Protection Act, 2023, you have the
right to access, correct, and erase your personal data, and to raise
a grievance with us or the Data Protection Board of India.

CONTACT US
If you have questions or concerns, please contact:
  Grievance Officer: [Name]
  Email: [privacy@organisation.com]
  Phone: [number] | Available: [hours]

We sincerely regret this incident and are committed to protecting
your personal data. We will provide updates as our investigation
progresses.

[Organisation Name]
[Date]
```

**Output:** Data Principal notification drafted; approved; sent; delivery logged.

---

### Capability 8: Post-Incident Review

**Trigger:** "post-incident review", "lessons learned breach", "incident retrospective", "prevent recurrence"

**Steps:**
1. Schedule review within **14 days** of incident closure.
2. Attendees: DPO, CISO, Legal, affected BU Head, Incident Lead.
3. Review agenda:

   ```
   POST-INCIDENT REVIEW AGENDA
   ──────────────────────────────────────────────────────────
   1. TIMELINE RECONSTRUCTION
      Walk through the incident minute by minute.
      When did it start? When detected? When contained?

   2. ROOT CAUSE ANALYSIS
      5-Whys or fishbone analysis.
      Technical cause + organisational cause.

   3. RESPONSE ASSESSMENT
      What worked well in the response?
      What did not work / was delayed?
      Were DPBI and Data Principal notifications timely?

   4. CONTROL GAPS
      What control failed to prevent the breach?
      What monitoring failed to detect it earlier?
      What process failed to contain it faster?

   5. REMEDIATION REVIEW
      Are all remediation actions completed?
      Are they effective?
      Any residual risk?

   6. SYSTEMIC IMPROVEMENTS
      Are similar vulnerabilities present elsewhere?
      Policy / procedure updates needed?
      Training updates needed?

   7. ACTIONS
      Owner and deadline for each improvement action.
   ──────────────────────────────────────────────────────────
   ```

4. Produce **Post-Incident Review Report**.
5. Update **Breach Register** with final details.
6. Communicate lessons learned (anonymised) to all staff.
7. Update Incident Response Plan based on findings.
8. Report to Board within 30 days of incident closure.

**Output:** Post-incident review report; improvement actions; Board report.

---

## Incident Severity SLA Summary

| Phase | P1 Critical | P2 High | P3 Medium | P4 Low |
|---|---|---|---|---|
| Escalate to DPO | 30 minutes | 2 hours | 8 hours | 24 hours |
| Containment initiated | 1 hour | 4 hours | 24 hours | 72 hours |
| DPBI notification | 72 hours | 72 hours | 72 hours | 72 hours |
| Data Principal notification | 24–48 hours | 48–72 hours | As needed | N/A |
| Post-incident review | 14 days | 14 days | 30 days | 30 days |
| Board report | 7 days | 14 days | 30 days | Quarterly |

---

## Related Skills

- `dpdp-penalty-enforcement-skill.md` — Breach penalty exposure
- `dpdp-training-awareness-skill.md` — Breach drills
- `dpdp-privacy-risk-management-skill.md` — Incident risk

---

## Skill Guardrails

- **Never delay** DPBI notification to gather all facts — notify with what is known; supplement later.
- **Never destroy** logs or evidence after a breach is discovered.
- **Always treat** a processor breach with the same urgency as an internal breach.
- **Never allow** communications about a breach to go public without Legal review.
- **Always notify** Data Principals where harm is likely — err on the side of transparency.

---

## Quick Commands

| Command | Action |
|---|---|
| `/ir-detect` | Identify and configure incident detection sources |
| `/ir-triage` | Triage and classify an incident |
| `/ir-escalate` | Execute escalation matrix |
| `/ir-contain` | Run containment playbook for incident type |
| `/ir-notify-decision` | Make DPBI / Data Principal notification decision |
| `/ir-dpbi-draft` | Draft DPBI breach notification |
| `/ir-dp-draft` | Draft Data Principal breach notification |
| `/ir-review` | Run post-incident review |

---

## References

- DPDP Act, 2023 — Sections 8(5) and 8(6) (Security and Breach Notification)
- CERT-In Cyber Incident Reporting Directions, 2022 (6-hour notification)
- NIST SP 800-61 — Computer Security Incident Handling Guide
- ISO/IEC 27035 — Information Security Incident Management
- ISO/IEC 27001 — Annex A.16 (Incident Management)
