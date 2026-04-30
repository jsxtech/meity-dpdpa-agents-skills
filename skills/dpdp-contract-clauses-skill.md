---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Contract Clauses"
type: "skill"
---

# DPDP Contract Clauses Skill

## Skill Identity

**Skill Name:** dpdp-contract-clauses
**Domain:** DPDP-Compliant Contracts, Data Processing Agreements, Privacy Clauses
**Skill Type:** Legal, Contracts, Compliance
**Applicable To:** Legal Teams, Procurement, DPOs, Contract Managers, Commercial Teams

---

## Skill Purpose

Draft, review, and negotiate DPDP-compliant contract clauses — covering Data Processing Agreements (DPAs), privacy schedules, customer contracts, employment agreements, vendor terms, and intra-group data sharing agreements. Ensure every contract involving personal data protects the organisation's DPDP compliance position.

---

## Contract Types Covered

| Contract Type | When Used | Key DPDP Provisions |
|---|---|---|
| Data Processing Agreement (DPA) | With every processor handling personal data | Processing instructions, security, breach notification, rights assistance, deletion |
| Intra-Group Data Sharing Agreement | Between group companies sharing personal data | Transfer basis, purpose limitation, obligations flow-down |
| Customer / Terms of Service | Consumer-facing; basis for consent and service | Consent, notice, rights, grievance |
| Employment Agreement | HR data processing | Employment legitimate use, monitoring disclosure, data rights |
| Vendor / Supplier Agreement | Procurement involving personal data | DPA schedule, data minimisation, localisation |
| Research / Data Sharing Agreement | External data sharing | Purpose limitation, re-identification prohibition, deletion |
| SaaS / Cloud Service Agreement | Cloud and software services | Data residency, DPA, security standards, breach notification |

---

## Skill Capabilities

---

### Capability 1: Data Processing Agreement (DPA) Drafting

**Trigger:** "draft DPA", "data processing agreement", "vendor DPA", "processor agreement"

**DPA Mandatory Clauses Under DPDP Act:**

```
DATA PROCESSING AGREEMENT
Between: [Data Fiduciary] ("Controller") and [Processor] ("Processor")
Effective Date: [Date]

═══════════════════════════════════════════════════════════════════
CLAUSE 1: DEFINITIONS
  "Personal Data" — as defined in the DPDP Act, 2023
  "Processing" — as defined in the DPDP Act, 2023
  "Data Principal" — the individual to whom personal data relates
  "DPDP Act" — Digital Personal Data Protection Act, 2023
  "DPBI" — Data Protection Board of India

CLAUSE 2: APPOINTMENT AND SCOPE
  2.1 Controller appoints Processor to process Personal Data
      solely for the purposes set out in Schedule 1.
  2.2 Processor shall process Personal Data only on documented
      instructions of Controller, unless required by law.
  2.3 Processor shall promptly notify Controller if an instruction
      infringes the DPDP Act or applicable law.

CLAUSE 3: PURPOSE AND DATA MINIMISATION
  3.1 Processor shall process only the categories of Personal Data
      described in Schedule 1 for the purposes described therein.
  3.2 Processor shall not process Personal Data for its own
      purposes or any purpose other than those in Schedule 1.
  3.3 Processor shall collect and retain only data necessary
      for the specified purpose.

CLAUSE 4: CONFIDENTIALITY
  4.1 Processor shall ensure all personnel with access to Personal
      Data are bound by confidentiality obligations.
  4.2 Processor shall ensure such personnel process Personal Data
      only in accordance with Controller's instructions.
  4.3 Confidentiality obligations survive termination.

CLAUSE 5: SECURITY SAFEGUARDS
  5.1 Processor shall implement appropriate technical and
      organisational measures to protect Personal Data including:
      (a) Encryption of Personal Data at rest and in transit
      (b) Access controls limiting access to authorised personnel
      (c) Multi-factor authentication on systems holding Personal Data
      (d) Audit logging of access to Personal Data
      (e) Vulnerability management and patching programme
      (f) Incident detection and response capability
  5.2 Security measures shall be documented and provided to
      Controller on request.

CLAUSE 6: SUB-PROCESSING
  6.1 Processor shall not engage any sub-processor without prior
      written approval of Controller.
  6.2 Where approved, Processor shall impose equivalent obligations
      on the sub-processor as those in this Agreement.
  6.3 Processor shall maintain a current list of approved
      sub-processors and notify Controller of any changes.
  6.4 Processor remains fully responsible for acts of sub-processors.

CLAUSE 7: DATA PRINCIPAL RIGHTS
  7.1 Processor shall assist Controller in fulfilling its obligations
      to respond to Data Principal rights requests.
  7.2 Processor shall:
      (a) Notify Controller within 3 business days of receiving
          any rights request from a Data Principal
      (b) Not respond to the Data Principal directly without
          Controller's written authorisation
      (c) Provide all data and assistance needed for Controller
          to respond within the prescribed timeline
  7.3 Rights assistance includes: access, correction, erasure,
      grievance escalation, and nomination.

CLAUSE 8: PERSONAL DATA BREACH
  8.1 Processor shall notify Controller of any Personal Data Breach
      without undue delay and within 24 hours of becoming aware.
  8.2 Breach notification shall include:
      (a) Nature of the breach and data categories affected
      (b) Approximate number of Data Principals affected
      (c) Likely consequences of the breach
      (d) Measures taken or proposed to address the breach
  8.3 Processor shall provide all further information requested
      by Controller to enable DPBI and Data Principal notification.
  8.4 Processor shall cooperate fully in breach investigation
      and remediation.

CLAUSE 9: DATA RETENTION AND DELETION
  9.1 Processor shall retain Personal Data only for the duration
      necessary for the purposes set out in Schedule 1 or as
      instructed by Controller.
  9.2 Upon termination of this Agreement or Controller's instruction,
      Processor shall promptly (and in any event within 30 days):
      (a) Return all Personal Data to Controller in an agreed format, OR
      (b) Permanently and securely delete all Personal Data
  9.3 Processor shall confirm deletion in writing with a Deletion
      Certificate within 30 days of deletion.
  9.4 Processor shall instruct all sub-processors to comply with
      this clause.
  9.5 Processor may retain Personal Data required by applicable
      law, provided such retention and its basis are disclosed
      to Controller in writing.

CLAUSE 10: CROSS-BORDER TRANSFERS
  10.1 Processor shall not transfer Personal Data outside India
       except to countries notified as permissible under the
       DPDP Act or with Controller's prior written approval.
  10.2 Any approved cross-border transfer shall be subject to
       equivalent data protection obligations.

CLAUSE 11: AUDIT RIGHTS
  11.1 Processor shall provide Controller (or its nominated auditor)
       with all information necessary to demonstrate compliance
       with this Agreement.
  11.2 Controller may conduct audits of Processor's compliance,
       with reasonable notice, not more than once per year
       (unless a breach or non-compliance triggers an audit).
  11.3 Processor shall cooperate fully with audits.

CLAUSE 12: INDEMNIFICATION
  12.1 Processor shall indemnify Controller for any losses,
       penalties, or claims arising from Processor's failure
       to comply with this Agreement or the DPDP Act.
  12.2 Each party shall indemnify the other for losses arising
       from that party's breach of this Agreement.

CLAUSE 13: TERM AND TERMINATION
  13.1 This Agreement is effective from [date] and continues
       until the underlying services agreement terminates.
  13.2 Either party may terminate this Agreement immediately
       on written notice if the other commits a material breach.
  13.3 Controller may terminate immediately if Processor is
       subject to a DPBI enforcement action.

SCHEDULE 1: PROCESSING DETAILS
  Subject matter of processing:
  Duration of processing:
  Nature and purpose of processing:
  Categories of Personal Data:
  Categories of Data Principals:
  Sub-processors (approved):

SCHEDULE 2: SECURITY MEASURES
  [Specific technical and organisational measures]

SCHEDULE 3: SUB-PROCESSOR LIST
  [Approved sub-processors at date of agreement]
═══════════════════════════════════════════════════════════════════
```

**Output:** Full DPA draft; schedules completed; legal review recommended before execution.

---

### Capability 2: Privacy Schedule for Customer/User Agreements

**Trigger:** "privacy clause for T&C", "data clause customer agreement", "consumer privacy schedule"

**Privacy Schedule Template:**

```
PRIVACY SCHEDULE
To: [Agreement Name] between [Company] and [Customer/User]

1. DATA COLLECTION AND USE
   1.1 We collect the personal data described in our Privacy Policy
       for the purposes set out therein.
   1.2 We will use your personal data only for the purposes for
       which it was collected or which you have consented to.
   1.3 We will notify you if we wish to use your data for a new
       purpose and obtain your consent where required.

2. YOUR CONSENT
   2.1 By [action — registering/purchasing/subscribing], you provide
       your free, specific, informed, and unambiguous consent to
       the processing described in our Privacy Policy.
   2.2 You may withdraw consent at any time by [method].
       Withdrawal does not affect the lawfulness of processing
       prior to withdrawal.
   2.3 Withdrawal of consent may affect our ability to provide
       certain services to you.

3. YOUR RIGHTS
   3.1 Under the Digital Personal Data Protection Act, 2023, you have:
       (a) The right to access your personal data
       (b) The right to correct inaccurate data
       (c) The right to erasure of your personal data
       (d) The right to nominate another person to exercise your rights
       (e) The right to raise a grievance with us
       (f) The right to approach the Data Protection Board of India
   3.2 To exercise your rights: [contact details / portal link]
   3.3 We will respond within [30 days / prescribed period].

4. DATA SECURITY
   We implement appropriate technical and organisational measures
   to protect your personal data. In the event of a breach affecting
   your data, we will notify you as required by law.

5. CHANGES
   We may update this Privacy Schedule. Material changes will be
   notified to you. Continued use after notification constitutes
   acceptance of the updated terms.
```

**Output:** Privacy schedule; consumer-friendly language; legally grounded.

---

### Capability 3: Employment Agreement — Data Processing Clauses

**Trigger:** "employment data clause", "employee privacy clause", "HR data in employment contract"

**Employment Data Clauses:**

```
DATA PROCESSING CLAUSES FOR EMPLOYMENT AGREEMENTS
═══════════════════════════════════════════════════════════════
CLAUSE: PERSONAL DATA PROCESSING

1. DATA COLLECTION AND PROCESSING
   The Company will collect and process your personal data for
   purposes related to your employment including:
   • Payroll processing, tax filing, and statutory compliance
     (Income Tax Act, EPF, ESI, Labour Codes)
   • Performance management and appraisals
   • Training and development records
   • Background verification (as required for your role)
   • Access control and attendance management
   • Health and safety obligations
   • Compliance with legal and regulatory requirements

   The legal basis for such processing is the legitimate use of
   employment data under Section 7(f) of the Digital Personal Data
   Protection Act, 2023, and applicable labour laws.

2. MONITORING
   [Include only if monitoring is conducted:]
   The Company may monitor [specify: emails/device/internet/location]
   for the following purposes: [specify: security/productivity/compliance].
   Such monitoring is conducted proportionately and only to the
   extent necessary for the stated purpose.

3. YOUR RIGHTS
   You have the right under the DPDP Act to access, correct, and
   in limited circumstances, request erasure of your personal data.
   To exercise your rights, contact: [HR / DPO contact].
   Note: Some data must be retained for the periods required by law
   (e.g., payroll records for 7 years under the Income Tax Act).

4. DATA SHARING
   Your personal data may be shared with:
   • Payroll processor: [Name]
   • Background verification agency: [Name]
   • Insurance / benefits providers: [Name]
   • Statutory authorities (EPF, ESI, tax authorities) as required

5. RETENTION
   Your personal data will be retained during your employment and
   for [period] thereafter as required by applicable law.

6. GRIEVANCE
   Privacy concerns related to your employment data may be raised
   with: [DPO / HR contact].
═══════════════════════════════════════════════════════════════
```

**Output:** Employment data clauses; disclosure of monitoring; rights statement.

---

### Capability 4: Intra-Group Data Sharing Agreement

**Trigger:** "intra-group data sharing", "group company data sharing", "affiliate data agreement"

**Key Clauses:**

```
INTRA-GROUP DATA SHARING AGREEMENT
Between: [Indian Entity] ("Data Fiduciary") and [Overseas/Domestic Group Entity] ("Recipient")

1. PURPOSE AND SCOPE
   1.1 Data Fiduciary shares Personal Data with Recipient solely for:
       [Specific business purpose — e.g., consolidated group reporting,
       IT support services, shared HR platform]
   1.2 Recipient acts as a Data Processor on behalf of Data Fiduciary
       [OR: Recipient acts as an independent Data Fiduciary for its own
       processing — specify clearly]

2. OBLIGATIONS OF RECIPIENT
   2.1 Process Personal Data only for the purposes in Clause 1.1
   2.2 Implement security safeguards equivalent to DPDP Act requirements
   2.3 Not transfer Personal Data to any further entity without approval
   2.4 Notify Data Fiduciary of any breach within 24 hours
   2.5 Assist Data Fiduciary with Data Principal rights requests
   2.6 Delete Personal Data on instruction or upon purpose completion

3. CROSS-BORDER TRANSFER (if Recipient is overseas)
   3.1 Data Fiduciary confirms that the Recipient's country is on the
       Central Government's permissible country list [OR: transfer
       is subject to such listing and pending legal advice]
   3.2 Recipient confirms it will not further transfer data outside
       its country without Data Fiduciary's written approval

4. AUDIT RIGHTS
   Data Fiduciary retains the right to audit Recipient's compliance
   with this Agreement annually.

5. GOVERNING LAW
   This Agreement is governed by the laws of India.
   Any disputes shall be subject to [jurisdiction] courts.
```

**Output:** Intra-group data sharing agreement draft; transfer basis documented.

---

### Capability 5: SaaS / Cloud Service Privacy Addendum

**Trigger:** "SaaS DPA", "cloud provider data agreement", "privacy addendum for software"

**SaaS Privacy Addendum Negotiation Checklist:**

```
SAAS PRIVACY ADDENDUM — NEGOTIATION CHECKLIST
─────────────────────────────────────────────────────────────
MUST HAVE (non-negotiable):
□ Processing only on our instructions
□ No use of our data to train vendor's AI models
□ India data residency option available (or permissible country)
□ Breach notification within 24–48 hours
□ Deletion of our data on contract termination (within 30 days)
□ Deletion certificate provided
□ Sub-processor list disclosed and change notification
□ No sub-processor addition without our approval
□ Audit rights (annual, with notice)

SHOULD HAVE:
□ ISO 27001 / SOC 2 Type II certification
□ Penetration test reports available on request
□ Dedicated India-region data residency (not just DPA clause)
□ Data portability in standard format on exit
□ SLA for rights request assistance (3 business days)
□ Dedicated privacy/security contact

WATCH OUT FOR:
□ Vendor claiming right to use data for "service improvement"
   (= training AI models) → Remove or restrict explicitly
□ Sub-processor clauses that allow any affiliate access → Restrict
□ Data retention after termination "for legal purposes" → Define period
□ Audit rights limited to "certifications only" → Push for actual audit
□ Breach notification timeline > 72 hours → Push for 24–48 hours
□ Governing law: foreign law → Negotiate Indian law or neutral jurisdiction
```

**Output:** SaaS privacy addendum review; negotiation positions; red flags identified.

---

### Capability 6: Research / Data Sharing Agreement

**Trigger:** "research data agreement", "data sharing with external party", "partner data agreement"

**Key Clauses:**

```
RESEARCH / DATA SHARING AGREEMENT
─────────────────────────────────────────────────────────────
1. DATA AND PURPOSE
   Sharing Party provides [dataset description] to Recipient
   solely for the purpose of [specific research/analysis purpose].

2. ANONYMISATION STATUS
   □ Data is fully anonymised [describe method] and DPDP Act
     does not apply to this dataset.
   [OR]
   □ Data is pseudonymised and DPDP Act applies. Recipient
     shall treat data as personal data accordingly.

3. PROHIBITED USES
   Recipient shall NOT:
   (a) Attempt to re-identify any individual in the dataset
   (b) Link this dataset with any other dataset for identification
   (c) Use the data for any commercial purpose beyond the stated purpose
   (d) Share the data with any third party
   (e) Publish any findings that could identify individuals

4. SECURITY
   Recipient shall store data in a secured environment with
   access limited to the named research team: [names/roles].

5. RETENTION AND DELETION
   Recipient shall delete all data within [30/60/90] days of
   completion of the research purpose.
   Recipient shall provide a Deletion Certificate within 7 days.

6. INCIDENT NOTIFICATION
   If re-identification risk is detected or data is exposed,
   Recipient shall notify Sharing Party within 24 hours.

7. PUBLICATION
   Any publication arising from this data must be approved by
   Sharing Party before submission and must not identify individuals.
```

**Output:** Research data sharing agreement; anonymisation status confirmed; re-identification prohibition.

---

### Capability 7: DPDP Contract Clause Review

**Trigger:** "review contract for DPDP", "check privacy clauses", "DPDP contract audit"

**Contract Review Checklist:**

```
DPDP CONTRACT CLAUSE REVIEW
═══════════════════════════════════════════════════════════════
VENDOR / PROCESSOR CONTRACTS
□ Is there a DPA or privacy schedule attached?
□ Does it cover all mandatory DPDP processor obligations?
□ Are processing purposes and data categories clearly defined?
□ Is breach notification timeline specified (< 48 hours)?
□ Are sub-processor restrictions in place?
□ Are audit rights included?
□ Is deletion on termination addressed?
□ Is cross-border transfer addressed?

CUSTOMER / USER AGREEMENTS
□ Is consent mechanism referenced in the agreement?
□ Are Data Principal rights disclosed?
□ Is the grievance mechanism referenced?
□ Is the DPO / Grievance Officer contact included?
□ Is the Privacy Policy linked or incorporated?

EMPLOYMENT AGREEMENTS
□ Are employment data processing purposes disclosed?
□ Is monitoring (if any) disclosed?
□ Are Data Principal rights described?
□ Is data retention period stated?

RED FLAGS TO FLAG FOR LEGAL:
□ Vendor claims ownership of data generated from our data
□ Vendor has unlimited right to use our data for "improvements"
□ No breach notification obligation on vendor
□ No audit rights
□ Foreign law / forum with no India nexus
□ No deletion obligation on termination
□ Unlimited sub-processing rights
═══════════════════════════════════════════════════════════════
```

**Output:** Contract review report; gaps identified; negotiation positions recommended.

---

## Quick Commands

| Command | Action |
|---|---|
| `/contract-dpa` | Draft full Data Processing Agreement |
| `/contract-privacy-schedule` | Draft privacy schedule for customer/user agreement |
| `/contract-employment` | Draft employment data processing clauses |
| `/contract-intragroup` | Draft intra-group data sharing agreement |
| `/contract-saas` | Review / negotiate SaaS privacy addendum |
| `/contract-research` | Draft research data sharing agreement |
| `/contract-review` | Review any contract for DPDP compliance |

---

## Related Skills

- `dpdp-consent-manager-skill.md` — CM agreements
- `dpdp-international-comparison-skill.md` — Cross-border clauses
- `dpdp-penalty-enforcement-skill.md` — Liability clauses

---

## Skill Guardrails

- **Always have legal counsel review** any contract clause before execution — templates are starting points, not final drafts.
- **Never accept** vendor contracts that lack breach notification, audit rights, or deletion obligations.
- **Never weaken** DPDP-mandated protections during commercial negotiations.
- **Always ensure** contracts are governed by or compatible with Indian law for DPDP compliance.
- **Always version-control** contract templates and track clause changes across negotiations.

---

## References

- DPDP Act, 2023 — Sections 6–9; Data Processor obligations
- MeITY Draft DPDP Rules, 2025
- ISO/IEC 27701 — Privacy Information Management (processor clauses)
- ICO Data Processing Agreement Guidance (comparative)
- Indian Contract Act, 1872
- IT Act, 2000 — Section 43A (reasonable security practices)
