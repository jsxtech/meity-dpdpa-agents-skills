---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Master DPDP Skill"
type: "skill"
---

# MEITY DPDP Privacy Skill

## Skill Identity

**Skill Name:** meity-dpdp-privacy
**Domain:** Digital Personal Data Protection Act, 2023 (DPDP Act)
**Ministry:** MeITY — Ministry of Electronics and Information Technology, Government of India
**Skill Type:** Compliance, Legal, Privacy, Regulatory
**Applicable To:** Data Fiduciaries, Significant Data Fiduciaries, Data Processors, Legal & Compliance Teams, DPOs, Product & Engineering Teams

---

## Skill Purpose

This skill enables an agent or practitioner to:

1. **Understand** the full framework of India's Digital Personal Data Protection Act, 2023
2. **Assess** an organisation's compliance posture against DPDP obligations
3. **Execute** compliance workflows — consent, rights, breach, vendor, audit, transfers
4. **Generate** DPDP-compliant documents — policies, notices, agreements, reports
5. **Respond** to regulatory proceedings before the Data Protection Board of India (DPBI)
6. **Advise** product and engineering teams on privacy-by-design under DPDP

---

## Knowledge Base

### Act Overview

| Attribute | Detail |
|---|---|
| Full Title | Digital Personal Data Protection Act, 2023 |
| Short Title | DPDP Act |
| Act Number | No. 22 of 2023 |
| Date of Assent | 11 August 2023 |
| Administered by | MeITY |
| Regulator | Data Protection Board of India (DPBI) |
| Rules | DPDP Rules, 2025 (gazetted November 2025) |

---

### Core Definitions

| Term | Definition |
|---|---|
| Personal Data | Any data about an identifiable individual |
| Data Principal | Individual to whom personal data relates; parent/guardian for children under 18 |
| Data Fiduciary | Entity that determines purpose and means of processing personal data |
| Significant Data Fiduciary (SDF) | Data Fiduciary designated by Central Government based on risk, volume, or sensitivity |
| Data Processor | Entity processing personal data on behalf of and under instructions of a Data Fiduciary |
| Consent Manager | Registered entity enabling Data Principals to manage consent centrally |
| Processing | Any operation on personal data — collection, storage, use, sharing, deletion, etc. |
| Personal Data Breach | Unauthorised or accidental breach of confidentiality, integrity, or availability of personal data |

---

### Lawful Bases for Processing

```
1. CONSENT — Free, specific, informed, unconditional, unambiguous, withdrawable
2. LEGITIMATE USE (no consent required):
   a. Employment / HR processing
   b. State / government functions
   c. Medical emergency
   d. Breakdown of public order / safety
   e. Research / archiving with appropriate safeguards
```

---

### Data Fiduciary Core Obligations

```
Section 4  — Process only for lawful purpose
Section 5  — Give clear notice before or at time of data collection
Section 6  — Obtain valid consent; enable easy withdrawal
Section 7  — Recognise legitimate uses
Section 8  — Security safeguards; breach notification; data accuracy
Section 9  — Children's data — parental consent; no profiling/targeting
Section 10 — SDF additional obligations
```

---

### Data Principal Rights

```
Section 11 — Right to Information (what data, what purpose)
Section 12 — Right to Correction and Erasure
Section 13 — Right to Grievance Redressal
Section 14 — Right to Nominate
             + Right to approach DPBI (Sections 27–28)
```

---

### Penalty Schedule

| Violation | Maximum Penalty |
|---|---|
| Failure to implement security safeguards | ₹250 crore |
| Failure to notify breach to DPBI / Data Principals | ₹200 crore |
| Children's data obligations breach | ₹200 crore |
| SDF additional obligations breach | ₹150 crore |
| Other DPDP Act violations | ₹50 crore |
| Data Principal duties breach | ₹10,000 |

---

## Skill Capabilities

### Capability 1: Compliance Gap Assessment

**Trigger phrase:** "assess our DPDP compliance", "are we compliant with DPDP", "DPDP gap analysis"

**Execution:**
1. Gather organisation profile (sector, scale, data types, processing activities).
2. Run through the 10-domain DPDP compliance checklist:
   - Governance & Accountability
   - Data Inventory & Mapping
   - Lawful Basis Management
   - Data Principal Rights Fulfilment
   - Security & Breach Management
   - Vendor / Processor Management
   - DPIA Programme
   - Cross-Border Transfer Controls
   - Children's Data Protections
   - Regulatory Engagement (DPBI / SDF)
3. Identify gaps — classify as Critical / High / Medium / Low.
4. Generate Gap Assessment Report with prioritised remediation plan.

**Output:** Gap Assessment Report; remediation tracker.

---

### Capability 2: Consent Flow Review

**Trigger phrase:** "review our consent", "is our consent DPDP compliant", "check consent notice"

**Execution:**
1. Review consent notice for mandatory elements:
   - Data categories collected ✓
   - Purposes of processing ✓
   - Rights and how to exercise them ✓
   - Grievance contact ✓
   - Plain language ✓
2. Review consent mechanism:
   - No pre-ticked boxes ✓
   - No bundled consents ✓
   - Affirmative action required ✓
   - Withdrawal as easy as consent ✓
3. Check consent record structure (timestamp, version, purpose mapping).
4. Flag any dark patterns or DPDP violations.

**Output:** Consent review report with specific findings and fixes.

---

### Capability 3: Privacy Notice / Policy Drafting

**Trigger phrase:** "draft privacy policy", "write consent notice", "create privacy notice", "update our privacy policy"

**Execution:**
1. Collect organisation inputs (name, data types, purposes, processors, retention, DPO).
2. Generate DPDP-compliant document using the appropriate template:
   - Privacy Policy (public-facing)
   - Consent Notice (pre-collection)
   - Cookie / Tracking Notice
   - Children's Privacy Notice
   - Employee Privacy Notice
3. Flag sections requiring legal review.
4. Version-stamp with date.

**Output:** Draft document; checklist of mandatory elements included.

---

### Capability 4: Data Principal Rights Request Handling

**Trigger phrase:** "handle a rights request", "data erasure request", "access request received", "deletion request"

**Execution:**
1. Classify request type (access / correction / erasure / nomination / grievance).
2. Guide through identity verification.
3. Execute the appropriate rights fulfilment workflow.
4. Generate response communication to Data Principal.
5. Update Rights Request Register.
6. Flag refusal grounds if applicable with legal basis.

**Output:** Rights request processed; Data Principal communication drafted; register updated.

---

### Capability 5: Personal Data Breach Response

**Trigger phrase:** "data breach", "security incident", "breach notification", "data leak"

**Execution:**
1. Intake and classify the breach (type, scope, severity).
2. Escalate to DPO, Legal, Management.
3. Draft DPBI notification.
4. Draft Data Principal notification (where harm likely).
5. Issue containment and remediation checklist.
6. Update Breach Register.

**Output:** Breach classified; notifications drafted; remediation checklist; register updated.

---

### Capability 6: Vendor / Processor Due Diligence

**Trigger phrase:** "onboard a vendor", "vendor DPA", "processor compliance", "third party data sharing"

**Execution:**
1. Run vendor privacy assessment.
2. Assign vendor risk tier (1/2/3).
3. Generate or review Data Processing Agreement (DPA).
4. Assess cross-border transfer (if overseas vendor).
5. Add to Processor Register.

**Output:** Vendor risk assessment; DPA checklist; Processor Register entry.

---

### Capability 7: DPIA Execution

**Trigger phrase:** "conduct a DPIA", "data protection impact assessment", "privacy risk assessment", "is a DPIA needed"

**Execution:**
1. Run DPIA pre-screening questionnaire.
2. If DPIA required — guide through full 7-step DPIA process.
3. Identify risks, assign scores, recommend mitigations.
4. Generate DPIA Report with DPO sign-off checklist.
5. Add to DPIA Register.

**Output:** DPIA pre-screening result; full DPIA report (if required); DPIA Register entry.

---

### Capability 8: Cross-Border Transfer Assessment

**Trigger phrase:** "can we transfer data overseas", "data transfer to [country]", "cross-border data", "cloud provider overseas"

**Execution:**
1. Identify transfer destination and data category.
2. Check against permissible country list (or flag pending publication).
3. Assess DPA coverage and safeguards.
4. Approve / block / escalate.
5. Update Transfer Register.

**Output:** Transfer assessment decision; safeguards checklist; Transfer Register updated.

---

### Capability 9: SDF Compliance Readiness

**Trigger phrase:** "are we an SDF", "significant data fiduciary", "SDF obligations", "SDF readiness"

**Execution:**
1. Assess likelihood of SDF designation based on volume, sensitivity, sector.
2. Identify SDF-specific gaps (DPO, auditor, algorithmic accountability, children's safeguards).
3. Generate SDF readiness report.
4. Create SDF compliance roadmap.

**Output:** SDF likelihood assessment; readiness gap report; compliance roadmap.

---

### Capability 10: DPBI Complaint Response

**Trigger phrase:** "DPBI complaint", "data protection board notice", "respond to DPBI", "regulatory inquiry"

**Execution:**
1. Register matter with litigation hold.
2. Compile case file and factual chronology.
3. Draft written submission to DPBI.
4. Prepare hearing brief.
5. Track DPBI order compliance.
6. Assess appeal grounds (TDSAT) if required.

**Output:** Matter file; DPBI response drafted; hearing brief; compliance tracker.

---

### Capability 11: Privacy by Design Review

**Trigger phrase:** "privacy review", "privacy by design", "new product DPDP review", "feature privacy check"

**Execution:**
1. Review proposed product / feature against DPDP principles.
2. Check data minimisation, consent design, rights mechanisms, security, retention.
3. Trigger DPIA if pre-screening warrants.
4. Issue Privacy Design Sign-off or flag required changes.

**Output:** Privacy design review report; sign-off or remediation list.

---

### Capability 12: Staff Training & Awareness

**Trigger phrase:** "DPDP training", "privacy awareness", "staff training on DPDP", "educate team on data protection"

**Execution:**
1. Identify target audience and role-specific needs.
2. Deliver training content appropriate to role:
   - All staff: DPDP basics, Data Principal rights, breach reporting
   - IT/Engineering: Data security, privacy by design
   - Legal/Compliance: Full DPDP Act obligations
   - Customer Support: Rights request handling
   - HR: Employee data obligations
3. Assess comprehension.
4. Record completion.

**Output:** Training delivered; completion certificates; training log updated.

---

## Skill Interaction Guidelines

### Tone & Approach
- Use **plain language** — avoid legal jargon when communicating with non-legal stakeholders.
- Use **precise legal language** in formal documents (policies, DPAs, DPBI submissions).
- Be **risk-calibrated** — flag Critical issues urgently; provide context for Medium/Low findings.
- Be **constructive** — always pair a finding with a recommended remediation.

### Escalation Protocol
| Situation | Escalate To |
|---|---|
| Critical compliance gap | DPO + Legal immediately |
| Personal data breach | DPO + Legal + Senior Management |
| DPBI complaint / inquiry | DPO + Legal + Board |
| Children's data risk | DPO + Legal + Product immediately |
| SDF designation notification | DPO + Legal + CEO |

### Limitations
- This skill provides **compliance guidance**, not legal advice.
- For complex, high-stakes, or novel matters → always recommend engagement of qualified Indian privacy legal counsel.
- DPDP Rules 2025 have been gazetted — verify provisions against the notified text and cite specific Rule numbers.
- Sectoral regulations (RBI, SEBI, IRDAI, TRAI) may impose **additional requirements** beyond the DPDP Act — cross-check accordingly.

---

## Pending Regulatory Developments (as of 2026)

| Item | Status | Skill Action |
|---|---|---|
| DPDP Rules (final) | Notified November 2025 | Reconcile all provisions against gazetted text |
| Permissible country list (cross-border transfers) | Not yet published | Apply precautionary restrictions |
| SDF designation criteria / list | Not yet published | Proactive readiness assessment recommended |
| Consent Manager registration framework | Under development | Monitor MeITY updates |
| DPBI constitution and portal | Pending | Prepare filings in advance |
| Interplay with sectoral regulators | Guidance pending | Cross-check with RBI/SEBI/IRDAI as applicable |

---

## Connected Agents

This skill works in conjunction with the following specialised agents in the `/agents` folder:

| Agent | File |
|---|---|
| Master DPDP Overview | `meity-dpdp-privacy-agent.md` |
| Consent Management | `dpdp-consent-management-agent.md` |
| Breach Notification | `dpdp-breach-notification-agent.md` |
| Rights Request Handling | `dpdp-rights-request-agent.md` |
| DPIA | `dpdp-dpia-agent.md` |
| Vendor & Processor Management | `dpdp-vendor-processor-agent.md` |
| Policy Document Generator | `dpdp-policy-document-generator-agent.md` |
| SDF Compliance | `dpdp-sdf-compliance-agent.md` |
| DPBI Complaint Response | `dpdp-dpbi-complaint-response-agent.md` |
| Internal Audit & Compliance | `dpdp-audit-compliance-agent.md` |
| Cross-Border Transfers | `dpdp-cross-border-transfer-agent.md` |
| Children's Data Protection | `dpdp-children-data-agent.md` |
| Anonymisation & Pseudonymisation | `dpdp-anonymisation-pseudonymisation-agent.md` |
| Legitimate Use | `dpdp-legitimate-use-agent.md` |
| Regulatory Monitoring | `dpdp-regulatory-monitoring-agent.md` |
| Compliance Roadmap | `dpdp-compliance-roadmap-agent.md` |
| Data Localisation | `dpdp-data-localisation-agent.md` |

---

## Quick Commands

| Command / Trigger | Capability Invoked |
|---|---|
| `/dpdp-gap-assessment` | Compliance Gap Assessment |
| `/dpdp-consent-review` | Consent Flow Review |
| `/dpdp-draft-policy` | Privacy Notice / Policy Drafting |
| `/dpdp-rights-request` | Rights Request Handling |
| `/dpdp-breach-response` | Breach Response |
| `/dpdp-vendor-check` | Vendor Due Diligence |
| `/dpdp-dpia` | DPIA Execution |
| `/dpdp-transfer-check` | Cross-Border Transfer Assessment |
| `/dpdp-sdf-readiness` | SDF Compliance Readiness |
| `/dpdp-dpbi-response` | DPBI Complaint Response |
| `/dpdp-privacy-review` | Privacy by Design Review |
| `/dpdp-training` | Staff Training & Awareness |

---

## Related Skills

- `dpdp-data-mapping-inventory-skill.md` — Data discovery
- `dpdp-privacy-programme-management-skill.md` — Programme operations
- `dpdp-audit-checklist-skill.md` — Compliance audit

---

## Skill Guardrails

- **Always consult legal counsel** before making binding compliance decisions — this skill provides guidance, not legal advice.
- **Always verify** provisions against the gazetted DPDP Rules 2025 — do not rely on earlier draft versions.
- **Never minimise** penalty exposure or compliance gaps.
- **Always maintain** an audit trail of compliance assessments and decisions.
- **Always escalate** to the DPO or legal team when uncertainty exists on a compliance question.

---

## References

- Digital Personal Data Protection Act, 2023 — No. 22 of 2023
- MeITY DPDP Rules, 2025 (Notified)
- Data Protection Board of India (when constituted)
- MeITY Official Website: meity.gov.in
- ISO/IEC 27701 — Privacy Information Management System
- ISO/IEC 29134 — Privacy Impact Assessment Guidelines
- ISO/IEC 29184 — Online Privacy Notices and Consent
