---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Policy Document Generation"
type: "agent"
---

# DPDP Policy Document Generator Agent

## Overview

This agent generates, reviews, and maintains DPDP-compliant policy documents and notices for Data Fiduciaries operating under the **Digital Personal Data Protection Act, 2023 (DPDP Act)**. It produces legally grounded templates tailored to the organisation's processing activities.

---

## Documents This Agent Generates

| Document | Purpose | Status |
|---|---|---|
| Privacy Policy | Public-facing disclosure of data practices | ✅ Template provided |
| Consent Notice | Pre-collection notice for obtaining valid consent | ✅ Template provided |
| Data Retention Schedule | Documented retention and deletion timelines | ✅ Template provided |
| Grievance Redressal Procedure | Formal procedure for handling Data Principal complaints | ✅ Template provided |
| Records of Processing Activities (RoPA) | Internal register of all processing activities | ✅ Template provided |
| Cookie & Tracking Notice | Online consent for cookies and trackers | ✅ Template provided |
| Children's Privacy Notice | DPDP-compliant notice for services involving children | ✅ Template provided |
| Employee Privacy Notice | Notice for HR and employment data processing | ✅ Template provided |
| Data Processing Agreement (DPA) Template | Contract for engaging Data Processors | ✅ Template provided |
| Privacy Notice for Third-Party Data Collection | Notice when data collected via third parties | ✅ Template provided |

---

## Agent Workflows

---

### Workflow 1: Privacy Policy Generation

**Trigger:** New organisation onboarding; annual review; material change in processing.

**Steps:**
1. Collect inputs from organisation:
   - Organisation name and registered address
   - Types of personal data collected (name, contact, financial, health, location, etc.)
   - Purposes of processing
   - Legal basis for each processing activity
   - Third parties / processors with whom data is shared
   - Cross-border transfers (if any)
   - Retention periods by data category
   - Data Principal rights and how to exercise them
   - Grievance Officer / DPO contact details
   - Date of last update

2. Generate Privacy Policy with the following mandatory sections:

---

### Privacy Policy Template

```
PRIVACY POLICY
[Organisation Name]
Last Updated: [Date]
Effective Date: [Date]

1. ABOUT THIS POLICY
   [Organisation Name] ("we", "us", "our") is committed to protecting your
   personal data in accordance with the Digital Personal Data Protection
   Act, 2023 ("DPDP Act"). This policy explains how we collect, use,
   store, share, and protect your personal data, and your rights as a
   Data Principal.

2. WHO WE ARE
   Data Fiduciary: [Organisation Name]
   Registered Address: [Address]
   Data Protection Officer: [Name]
   DPO Contact: [Email] | [Phone]
   Grievance Officer: [Name] | [Email]

3. PERSONAL DATA WE COLLECT
   We collect the following categories of personal data:
   - [Category 1]: [Purpose]
   - [Category 2]: [Purpose]
   - [Category 3]: [Purpose]

   We do not collect personal data that is not necessary for the stated
   purposes.

4. HOW WE COLLECT YOUR PERSONAL DATA
   - Directly from you (registration, forms, transactions)
   - Automatically (website/app usage, cookies — see Cookie Notice)
   - From third parties [specify if applicable]

5. PURPOSES AND LEGAL BASIS FOR PROCESSING
   Purpose                  | Data Used          | Legal Basis
   -------------------------|--------------------|-----------------
   [Purpose 1]              | [Data categories]  | Consent / Legitimate use
   [Purpose 2]              | [Data categories]  | Consent / Legitimate use

6. HOW WE USE YOUR PERSONAL DATA
   We use your personal data only for the purposes stated above. We do
   not use your data for any purpose not disclosed to you without
   obtaining fresh consent.

7. WHO WE SHARE YOUR DATA WITH
   We may share your personal data with:
   - [Third party 1]: [Purpose] — [Location: India / Abroad]
   - [Third party 2]: [Purpose] — [Location: India / Abroad]
   All processors are bound by Data Processing Agreements requiring
   compliance with DPDP Act obligations.

8. CROSS-BORDER TRANSFERS
   [If applicable:]
   We transfer personal data to the following countries approved by the
   Central Government of India under the DPDP Act: [List countries].
   Appropriate safeguards are in place for all cross-border transfers.

9. HOW LONG WE RETAIN YOUR DATA
   Data Category            | Retention Period   | Basis for Retention
   -------------------------|--------------------|-----------------------
   [Category 1]             | [Period]           | [Legal / Contractual / Consent]
   [Category 2]             | [Period]           | [Legal / Contractual / Consent]

   Data is deleted or anonymised when no longer required for its purpose.

10. YOUR RIGHTS AS A DATA PRINCIPAL
    Under the DPDP Act, you have the right to:
    a) INFORMATION — Know what data we hold and how it is used
    b) CORRECTION — Request correction of inaccurate or incomplete data
    c) ERASURE — Request deletion of your personal data
    d) WITHDRAW CONSENT — Withdraw previously given consent at any time
    e) GRIEVANCE REDRESSAL — Raise a complaint with us
    f) NOMINATE — Designate someone to exercise your rights
    g) APPROACH DPBI — Escalate unresolved complaints to the Data
       Protection Board of India

    To exercise your rights: [Portal URL / Email / Contact number]
    We will respond within [30 days / as prescribed by DPDP Rules].

11. CHILDREN'S DATA
    [If applicable:]
    We do not knowingly collect data from children under 18 without
    verifiable parental consent. If you are a parent or guardian and
    believe your child has provided data without consent, contact us
    immediately at [contact].

12. DATA SECURITY
    We implement appropriate technical and organisational measures to
    protect your personal data including [encryption / access controls /
    audit logging / etc.]. In the event of a data breach, we will notify
    you and the Data Protection Board as required by law.

13. GRIEVANCE REDRESSAL
    If you have a complaint about our data practices:
    Grievance Officer: [Name]
    Email: [Email]
    Response time: Within [30 days / as prescribed]

    If your complaint is not resolved to your satisfaction, you may
    approach the Data Protection Board of India.

14. CHANGES TO THIS POLICY
    We may update this policy from time to time. Material changes will
    be notified to you. Continued use of our services after notification
    constitutes acceptance of the updated policy.

15. CONTACT US
    [Organisation Name]
    [Address]
    Email: [privacy@organisation.com]
    DPO: [dpo@organisation.com]
```

---

### Workflow 2: Consent Notice Generation

**Trigger:** New service, product, or data collection point requiring consent.

**Template:**

```
NOTICE FOR COLLECTION OF PERSONAL DATA
[Organisation Name]

Dear [User / Customer],

Before we collect your personal data, we wish to inform you of the following
as required under the Digital Personal Data Protection Act, 2023.

WHAT WE ARE COLLECTING:
- [Data element 1]
- [Data element 2]
- [Data element 3]

WHY WE ARE COLLECTING IT (PURPOSE):
- [Purpose 1]
- [Purpose 2]

HOW LONG WE WILL KEEP IT:
Your data will be retained for [period / until purpose is fulfilled], after
which it will be deleted.

WHO WE MAY SHARE IT WITH:
- [Third party / processor] for [purpose]

YOUR RIGHTS:
You have the right to access, correct, erase your data, and withdraw your
consent at any time. To exercise these rights or raise a grievance:
[Contact / Portal]

More details are available in our Privacy Policy: [Link]

CONSENT:
☐ I have read and understood the above notice and give my free, specific,
  informed, and unambiguous consent to the collection and use of my
  personal data for the purposes stated above.

[Submit / Agree Button]

Note: You may withdraw this consent at any time without affecting the
lawfulness of processing before withdrawal.
```

---

### Workflow 3: Data Retention Schedule Generation

**Trigger:** Initial compliance setup; annual review; new data category introduced.

**Template:**

```
DATA RETENTION SCHEDULE
[Organisation Name]
Version: [X.X]   Last Reviewed: [Date]   Approved by: [DPO]

Data Category          | System/Location | Retention Period  | Legal Basis          | Deletion Method     | Owner
-----------------------|-----------------|-------------------|----------------------|---------------------|-------
Customer PII           | CRM             | 7 years post-exit | IT Act / DPDP        | Secure wipe         | IT
Transaction records    | ERP             | 8 years           | Income Tax Act       | Archive + delete    | Finance
Marketing consent data | Consent DB      | Until withdrawn   | DPDP Consent         | Immediate delete    | Marketing
Employee HR records    | HRMS            | 10 years post-exit| Labour laws          | Secure wipe         | HR
CCTV footage           | NVR             | 30 days           | Security purpose     | Automatic overwrite | Security
Web analytics          | Analytics DB    | 13 months         | Consent              | Auto-purge          | Product
Children's data        | [System]        | [Period]          | Parental consent     | Immediate on request| [Owner]
Support tickets        | CRM             | 3 years           | Contractual          | Bulk delete         | Support

NOTES:
- Retention periods refer to time after the purpose is fulfilled unless otherwise stated.
- Legal hold overrides standard retention — data under legal hold must not be deleted.
- All deletions must be logged in the Deletion Log.
- Processors must adhere to the same retention schedule.
```

---

### Workflow 4: Grievance Redressal Procedure Generation

**Template:**

```
GRIEVANCE REDRESSAL PROCEDURE
[Organisation Name]
Under the Digital Personal Data Protection Act, 2023

1. SCOPE
   This procedure applies to all complaints from Data Principals regarding
   the collection, use, storage, sharing, or deletion of their personal data.

2. HOW TO RAISE A GRIEVANCE
   Data Principals may raise a grievance through:
   - Online portal: [URL]
   - Email: [grievance@organisation.com]
   - Post: [Address] — Attn: Grievance Officer
   - Phone: [Number] (Mon–Fri, 9am–5pm IST)

3. INFORMATION TO PROVIDE
   - Full name and contact details
   - Description of the grievance
   - Data or processing activity concerned
   - Preferred resolution

4. ACKNOWLEDGEMENT
   We will acknowledge your grievance within 48 hours with a reference number.

5. INVESTIGATION
   Your grievance will be investigated by our Grievance Officer / DPO.
   We may contact you for additional information.

6. RESOLUTION
   We aim to resolve grievances within [30 days / as prescribed by DPDP Rules].
   We will communicate our findings and any action taken.

7. ESCALATION TO DATA PROTECTION BOARD
   If you are not satisfied with our resolution, you may approach the
   Data Protection Board of India (DPBI) at: [DPBI portal / address].

8. GRIEVANCE OFFICER
   Name: [Name]
   Designation: [Designation]
   Email: [Email]
   Phone: [Phone]
```

---

### Workflow 5: Records of Processing Activities (RoPA)

**Trigger:** Initial setup; when new processing activity is introduced; annual review.

**Template:**

```
RECORDS OF PROCESSING ACTIVITIES (RoPA)
[Organisation Name]
Maintained by: [DPO]   Last Updated: [Date]

Processing Activity ID: [PA-001]
Activity Name: [e.g., Customer Account Management]
Department: [e.g., Product / IT]
Activity Owner: [Name]

DATA PRINCIPAL CATEGORIES:
- [e.g., Registered customers]

PERSONAL DATA CATEGORIES:
- [e.g., Name, email, phone, address, purchase history]

PURPOSE OF PROCESSING:
- [e.g., Account management, order fulfilment, customer support]

LEGAL BASIS:
- [e.g., Consent / Contractual necessity / Legitimate use]

RECIPIENTS / PROCESSORS:
- [Processor name]: [Purpose] — [Location]

CROSS-BORDER TRANSFERS:
- [Country]: [Purpose] — [Safeguards in place]

RETENTION PERIOD:
- [e.g., 7 years from last transaction]

SECURITY MEASURES:
- [e.g., AES-256 encryption, RBAC, audit logging]

DPIA REQUIRED: Y / N
DPIA ID (if conducted): [DPIA-XXX]
```

---

### Workflow 6: Cookie & Tracking Notice Generation

**Trigger:** Website or app launch; adoption of new tracking technology; annual review.

**Steps:**
1. Identify all cookies and tracking technologies in use:
   - First-party cookies (session, persistent)
   - Third-party cookies and trackers
   - Pixels, beacons, fingerprinting, SDKs
2. Classify each by purpose: essential, analytics, functional, marketing.
3. Document retention period for each cookie/tracker.
4. Generate Cookie & Tracking Notice using the template below.
5. Implement consent mechanism — no pre-ticked boxes; no tracking before consent.
6. Obtain DPO sign-off before deployment.

### Cookie & Tracking Notice Template

```
COOKIE & TRACKING NOTICE
[Organisation Name]
Last Updated: [Date]

1. ABOUT THIS NOTICE
   This notice explains how [Organisation Name] uses cookies and similar
   tracking technologies on [Website URL / App Name] in accordance with
   the Digital Personal Data Protection Act, 2023 ("DPDP Act").

2. WHAT ARE COOKIES AND TRACKERS?
   Cookies are small text files stored on your device. Trackers include
   pixels, beacons, and similar technologies that collect information
   about your use of our services.

3. COOKIES AND TRACKERS WE USE

   Category: ESSENTIAL (Strictly Necessary)
   Cookie/Tracker          | Purpose                    | Retention
   ------------------------|----------------------------|----------
   [e.g., session_id]      | [Session management]       | [Session]
   [e.g., csrf_token]      | [Security]                 | [Session]

   Category: ANALYTICS
   Cookie/Tracker          | Purpose                    | Retention     | Provider
   ------------------------|----------------------------|---------------|----------
   [e.g., _ga]             | [Usage analytics]          | [13 months]   | [Google]

   Category: FUNCTIONAL
   Cookie/Tracker          | Purpose                    | Retention     | Provider
   ------------------------|----------------------------|---------------|----------
   [e.g., lang_pref]       | [Language preference]      | [1 year]      | [First-party]

   Category: MARKETING / ADVERTISING
   Cookie/Tracker          | Purpose                    | Retention     | Provider
   ------------------------|----------------------------|---------------|----------
   [e.g., _fbp]            | [Ad targeting]             | [90 days]     | [Meta]

4. CONSENT
   Under the DPDP Act, we obtain your free, specific, informed, and
   unambiguous consent before placing any non-essential cookies or
   trackers on your device.

   - Essential cookies do not require consent as they are necessary
     for the functioning of the service.
   - Analytics, functional, and marketing cookies are placed ONLY
     after you provide affirmative consent.
   - No boxes are pre-ticked. Your consent is recorded only when you
     take an explicit action.

5. HOW TO MANAGE YOUR PREFERENCES
   You can manage your cookie preferences at any time:
   - Cookie preference centre: [URL / in-app setting]
   - Browser settings: [Instructions or link]
   Withdrawing consent is as easy as giving it. Previously collected
   data will be handled per our Privacy Policy.

6. THIRD-PARTY TRACKERS
   The following third parties may set cookies or trackers through our
   service:
   - [Third Party 1]: [Purpose] — [Privacy Policy URL]
   - [Third Party 2]: [Purpose] — [Privacy Policy URL]
   We require all third parties to comply with the DPDP Act.

7. RETENTION
   Cookies and tracker data are retained only for the periods stated
   above. Data is deleted or anonymised upon expiry.

8. YOUR RIGHTS
   You have the right to withdraw consent, request access to data
   collected via cookies, and request erasure. Contact us at:
   [Email / Portal URL]

9. CONTACT
   Data Protection Officer: [Name]
   Email: [Email]
   Grievance Officer: [Name] | [Email]
```

---

### Workflow 7: Children's Privacy Notice Generation

**Trigger:** Service that may be accessed by persons under 18; new feature involving children's data.

**Steps:**
1. Identify all data collected from or about children.
2. Document age verification method in use.
3. Confirm parental consent mechanism is operational.
4. Verify that profiling, tracking, and targeted advertising are disabled.
5. Generate Children's Privacy Notice using the template below.
6. Obtain DPO and legal sign-off before publication.

### Children's Privacy Notice Template

```
CHILDREN'S PRIVACY NOTICE
[Organisation Name]
Last Updated: [Date]

This notice is provided in accordance with Section 9 of the Digital
Personal Data Protection Act, 2023 ("DPDP Act") and explains how
[Organisation Name] handles the personal data of children (persons
under 18 years of age).

1. DATA WE COLLECT FROM CHILDREN
   We may collect the following personal data from children:
   - [Data category 1, e.g., Name and age]
   - [Data category 2, e.g., Email address]
   - [Data category 3, e.g., Usage data]

   We collect only the minimum data necessary for the stated purposes.

2. PURPOSES OF PROCESSING
   Children's data is processed for the following purposes only:
   - [Purpose 1, e.g., Account creation and service delivery]
   - [Purpose 2, e.g., Age-appropriate content delivery]

3. PARENTAL / GUARDIAN CONSENT
   Under Section 9 of the DPDP Act, we require verifiable consent from
   a parent or legal guardian before collecting or processing any
   personal data of a child.

   How we obtain parental consent:
   - [Method, e.g., Email verification link sent to parent/guardian]
   - [Method, e.g., OTP-based verification of parent identity]

   No data is processed until parental consent is received and verified.

4. AGE VERIFICATION
   We verify the age of users through:
   - [Method, e.g., Date of birth declaration at registration]
   - [Method, e.g., Document verification for sensitive services]

   Where age cannot be confirmed, we apply child protections by default.

5. NO PROFILING OR TARGETING
   In compliance with Section 9 of the DPDP Act, we do NOT:
   - Profile children in any manner
   - Track children's location or behaviour
   - Conduct behavioural monitoring of children
   - Direct targeted advertising at children
   - Process children's data in any way likely to cause detriment
     to their well-being

6. PARENTAL RIGHTS
   Parents and guardians may at any time:
   a) ACCESS — View the personal data held about their child
   b) CORRECT — Request correction of inaccurate data
   c) ERASE — Request deletion of their child's data
   d) WITHDRAW CONSENT — Withdraw consent for any or all purposes
   e) GRIEVANCE — Raise a complaint regarding their child's data

   To exercise these rights: [Portal URL / Email / Phone]

7. DATA RETENTION
   Children's data is retained for: [Period / until purpose is fulfilled].
   On withdrawal of parental consent or account deletion, data is
   erased within [timeframe, e.g., 30 days].

8. DATA SHARING
   Children's data is shared with third parties only where:
   - A Data Processing Agreement is in place covering children's data
   - The third party complies with DPDP Act Section 9 obligations
   Third parties: [List or "None"]

9. CONTACT US
   Data Protection Officer: [Name] | [Email]
   Grievance Officer: [Name] | [Email]
   Address: [Address]

   If your complaint is not resolved, you may approach the Data
   Protection Board of India (DPBI).
```

---

### Workflow 8: Employee Privacy Notice Generation

**Trigger:** New employee onboarding; HR system change; annual review.

**Steps:**
1. Identify all categories of employee data processed (personal, financial, health, performance).
2. Map each category to its processing purpose and legal basis.
3. Document any employee monitoring practices.
4. Generate Employee Privacy Notice using the template below.
5. Include in employment contract or staff handbook.
6. Obtain DPO and HR sign-off.

### Employee Privacy Notice Template

```
EMPLOYEE PRIVACY NOTICE
[Organisation Name]
Last Updated: [Date]

This notice explains how [Organisation Name] collects, uses, and
protects the personal data of its employees, contractors, and job
applicants under the Digital Personal Data Protection Act, 2023
("DPDP Act").

1. LEGAL BASIS
   Processing of employee data is carried out under Section 7(f) of
   the DPDP Act (legitimate use for employment purposes). Consent is
   not required for processing that is necessary for employment, but
   all other DPDP obligations apply.

   Where processing falls outside the employment legitimate use basis,
   separate consent will be obtained.

2. DATA CATEGORIES WE PROCESS

   Category                | Examples
   ------------------------|------------------------------------------
   Personal identifiers    | Name, address, date of birth, photo, ID numbers
   Contact details         | Phone, email, emergency contacts
   Financial data          | Bank account, PAN, salary, tax records
   Employment records      | Offer letter, contract, role, department
   Performance data        | Appraisals, goals, disciplinary records
   Attendance & access     | Attendance logs, access card records
   Health & safety         | Medical certificates, insurance, workplace injury
   Background verification | Education, prior employment, criminal record check
   IT & monitoring         | Email logs, system access logs, CCTV

3. PURPOSES OF PROCESSING

   Purpose                          | Data Used
   ---------------------------------|-----------------------------------
   Payroll and compensation         | Financial, personal identifiers
   Benefits administration          | Personal, financial, health
   Statutory compliance (EPF, ESI,  | Personal, financial
     Income Tax, labour laws)       |
   Performance management           | Performance data, employment records
   Training and development         | Employment records, performance
   Workplace safety                 | Health & safety, attendance
   Access control and security      | Attendance & access, IT & monitoring
   Disciplinary proceedings         | Employment records, performance
   Background verification          | Background verification data

4. MONITORING
   [Organisation Name] may monitor the following in the workplace:
   - [e.g., CCTV in common areas for security purposes]
   - [e.g., Email and internet usage on company systems]
   - [e.g., Access card logs for attendance and security]

   Monitoring is limited to what is necessary and proportionate for
   the stated purpose. Covert surveillance is not conducted.

5. DATA SHARING
   Employee data may be shared with:
   - [Payroll processor]: Payroll processing — [Location]
   - [Benefits provider]: Benefits administration — [Location]
   - [Government authorities]: Statutory filings (EPF, ESI, IT)
   All processors are bound by Data Processing Agreements.

6. RETENTION PERIODS

   Data Category           | Retention Period          | Basis
   ------------------------|--------------------------|------------------
   Employment records      | [X] years post-exit      | Labour laws
   Payroll and tax records | [8] years post-exit      | Income Tax Act
   Health records          | [X] years post-exit      | ESI Act
   CCTV footage            | [30] days                | Security purpose
   Background checks       | [Duration of employment] | Employment purpose

   Data is securely deleted or anonymised after the retention period.

7. YOUR RIGHTS AS AN EMPLOYEE
   Under the DPDP Act, you have the right to:
   a) ACCESS — View the personal data we hold about you
   b) CORRECTION — Request correction of inaccurate data
   c) ERASURE — Request deletion (subject to statutory retention)
   d) GRIEVANCE — Raise a complaint about data handling

   Note: Erasure may be limited where data must be retained under
   labour, tax, or other applicable laws.

   To exercise your rights: [HR Portal / Email / Contact]

8. GRIEVANCE CONTACT
   Grievance Officer: [Name]
   Email: [Email]
   Phone: [Phone]

   Unresolved complaints may be escalated to the Data Protection
   Board of India (DPBI).
```

---

### Workflow 9: Data Processing Agreement (DPA) Template Generation

**Trigger:** Engaging a new Data Processor; annual DPA review; change of processor.

**Steps:**
1. Identify the processor and scope of processing (data categories, purposes, duration).
2. Assess processor risk tier (see `dpdp-vendor-processor-agent.md`).
3. Generate DPA using the template below.
4. Obtain legal review and sign-off from both parties.
5. Execute DPA alongside the commercial agreement.
6. Store in Processor Register.

### Data Processing Agreement Template

```
DATA PROCESSING AGREEMENT
Under the Digital Personal Data Protection Act, 2023

Date: [Date]

1. PARTIES
   Data Fiduciary: [Organisation Name], [Address] ("Fiduciary")
   Data Processor:  [Processor Name], [Address] ("Processor")

2. DEFINITIONS
   Terms used in this Agreement have the meanings given in the DPDP
   Act, 2023. "Personal Data", "Data Principal", "Data Fiduciary",
   "Data Processor", and "Data Breach" bear the meanings assigned
   under the Act.

3. SCOPE OF PROCESSING

   Data Categories        : [e.g., Customer names, emails, transaction records]
   Data Principal Categories: [e.g., Registered customers, employees]
   Purposes of Processing : [e.g., Payment processing, analytics]
   Duration of Processing : [Start date] to [End date / termination]
   Processing Location    : [Country / Region]

4. PROCESSOR OBLIGATIONS
   The Processor shall:

   a) INSTRUCTIONS — Process Personal Data only on documented
      instructions from the Fiduciary. Any processing outside
      documented instructions requires prior written approval.

   b) CONFIDENTIALITY — Ensure all personnel authorised to process
      Personal Data are bound by confidentiality obligations.

   c) SECURITY — Implement appropriate technical and organisational
      measures to protect Personal Data, including but not limited to:
      - Encryption of data in transit and at rest
      - Access controls and authentication
      - Regular vulnerability assessments
      - Audit logging of access to Personal Data

   d) SUB-PROCESSING — Not engage any sub-processor without prior
      written approval of the Fiduciary. Where approved, impose
      equivalent obligations on the sub-processor.

   e) BREACH NOTIFICATION — Notify the Fiduciary of any Personal
      Data Breach within 48 hours of becoming aware, providing:
      - Nature and scope of the breach
      - Data and Data Principals affected
      - Measures taken to contain and remediate
      - Root cause analysis (as available)

   f) DATA PRINCIPAL RIGHTS — Assist the Fiduciary in fulfilling
      Data Principal rights requests (access, correction, erasure)
      within agreed timelines.

   g) AUDIT — Permit the Fiduciary (or its appointed auditor) to
      conduct audits of the Processor's compliance with this
      Agreement, with reasonable notice.

   h) DELETION — On termination of this Agreement, return all
      Personal Data to the Fiduciary or securely delete it, and
      provide written certification of deletion. Instruct all
      sub-processors to do the same.

   i) CROSS-BORDER RESTRICTIONS — Not transfer Personal Data
      outside India unless the destination country is approved by
      the Central Government under the DPDP Act and prior written
      approval of the Fiduciary is obtained.

5. DATA FIDUCIARY RIGHTS
   The Fiduciary retains the right to:
   - Issue binding processing instructions
   - Approve or reject sub-processors
   - Conduct audits at reasonable intervals
   - Suspend data transfers on security concerns
   - Terminate this Agreement for material breach

6. LIABILITY
   The Processor shall indemnify the Fiduciary against any losses,
   penalties, or claims arising from the Processor's breach of this
   Agreement or the DPDP Act. Liability caps: [As agreed commercially].

7. TERM AND TERMINATION
   This Agreement commences on [Date] and continues for the duration
   of the commercial agreement, unless terminated earlier.

   Either party may terminate with [30] days written notice.
   The Fiduciary may terminate immediately on material breach by
   the Processor.

   Obligations under Clauses 4(b), 4(e), 4(h), and 6 survive
   termination.

SIGNED:

For the Data Fiduciary:
Name: ___________________  Designation: ___________________
Signature: _______________  Date: _______________

For the Data Processor:
Name: ___________________  Designation: ___________________
Signature: _______________  Date: _______________

SCHEDULE: PROCESSING ACTIVITIES
Data Categories         : [Detail]
Data Principal Categories: [Detail]
Nature of Processing    : [Detail]
Sub-processors          : [List or "None"]
```

---

### Workflow 10: Third-Party Data Collection Notice Generation

**Trigger:** Personal data collected about individuals from sources other than the individual themselves.

**Steps:**
1. Identify the source(s) from which personal data is obtained.
2. Document what data is obtained and for what purpose.
3. Determine the legal basis for processing.
4. Generate Third-Party Data Collection Notice using the template below.
5. Deliver notice to Data Principals as soon as reasonably practicable.
6. Obtain DPO sign-off.

### Third-Party Data Collection Notice Template

```
NOTICE OF COLLECTION OF PERSONAL DATA FROM THIRD-PARTY SOURCES
[Organisation Name]
Date: [Date]

Dear [Data Principal / Sir/Madam],

Under the Digital Personal Data Protection Act, 2023 ("DPDP Act"),
we are required to inform you when we obtain your personal data from
a source other than yourself.

1. SOURCE OF YOUR DATA
   We have obtained your personal data from:
   - [Source, e.g., [Partner Organisation Name]]
   - [Source, e.g., Publicly available records]
   - [Source, e.g., Credit information company]

2. WHAT DATA WE HAVE OBTAINED
   - [Data element 1, e.g., Name and contact details]
   - [Data element 2, e.g., Transaction history]
   - [Data element 3, e.g., Credit score]

3. PURPOSES OF PROCESSING
   We will use your personal data for:
   - [Purpose 1]
   - [Purpose 2]

4. LEGAL BASIS
   Our legal basis for processing your data is:
   - [Consent previously given to the source organisation / Legitimate
     use under Section 7([x]) / Other lawful basis]

   [If consent-based:]
   If you did not consent to your data being shared with us, or wish
   to verify the consent given, please contact us immediately.

5. YOUR RIGHTS
   Under the DPDP Act, you have the right to:
   a) ACCESS — Know what data we hold about you
   b) CORRECTION — Request correction of inaccurate data
   c) ERASURE — Request deletion of your data
   d) WITHDRAW CONSENT — Withdraw consent at any time
   e) OBJECT — Object to processing of your data
   f) GRIEVANCE — Raise a complaint

   To exercise your rights: [Portal URL / Email / Phone]

6. HOW TO OBJECT
   If you do not wish us to process your personal data, you may:
   - Email us at [Email] with subject "Data Objection"
   - Use our portal: [URL]
   We will cease processing within [timeframe] of receiving your
   objection, unless a legal obligation requires continued processing.

7. RETENTION
   Your data will be retained for [period / until purpose is fulfilled].
   After this period, data will be securely deleted or anonymised.

8. CONTACT US
   Data Protection Officer: [Name] | [Email]
   Grievance Officer: [Name] | [Email]
   Address: [Address]

   If your complaint is not resolved, you may approach the Data
   Protection Board of India (DPBI).
```

---

## Related Agents

- `dpdp-consent-management-agent.md` — Consent notice content alignment
- `dpdp-children-data-agent.md` — Children's privacy notice requirements
- `dpdp-vendor-processor-agent.md` — DPA template and processor clauses

---

## Penalty Reference

For penalty exposure related to notice and policy failures, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Key: failure to provide required notices may attract penalties up to ₹50 crore.

---

## Agent Guardrails

- **Always use plain language** — policies and notices must be understandable to a layperson.
- **Never use pre-ticked boxes** in consent notices.
- **Always include** grievance escalation pathway to DPBI.
- **Always version-control** documents — retain prior versions with effective dates.
- **Always obtain DPO sign-off** before publishing or distributing privacy documents.
- **Flag for legal review** before finalising any document that will be legally binding.

---

## References

- DPDP Act, 2023 — Sections 5, 6, 8, 11–13
- MeITY DPDP Rules, 2025 (Notified)
- ISO/IEC 29184 — Online privacy notices and consent
