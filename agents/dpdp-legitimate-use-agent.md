---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Legitimate Use (Section 7)"
type: "agent"
---

# DPDP Legitimate Use Agent

## Overview

This agent manages the identification, documentation, and application of **legitimate uses** under **Section 7 of the Digital Personal Data Protection Act, 2023 (DPDP Act)** — processing activities that do not require the consent of the Data Principal, but must still comply with all other DPDP obligations.

---

## What is a Legitimate Use?

The DPDP Act permits certain categories of processing **without consent** where the purpose falls within a defined legitimate use. These are not unlimited exemptions — they are **narrowly defined categories** requiring careful assessment and documentation.

```
IMPORTANT DISTINCTION
────────────────────────────────────────────────────────
Legitimate Use ≠ "We don't need to comply with DPDP"

Even under legitimate use:
  ✓ Data minimisation still applies
  ✓ Purpose limitation still applies
  ✓ Security safeguards still apply
  ✓ Data retention limits still apply
  ✓ Data Principal rights still apply (subject to exceptions)
  ✓ Breach notification still applies
  ✗ Consent is NOT required for processing
────────────────────────────────────────────────────────
```

---

## Section 7 — Legitimate Uses (Overview)

| Category | Description |
|---|---|
| 7(a) | State and its instrumentalities — for function of the State or sovereign purpose |
| 7(b) | Compliance with any judgment, decree, or order under Indian law |
| 7(c) | Responding to a medical emergency — threat to life or health |
| 7(d) | Providing medical treatment or health services during epidemic / disaster |
| 7(e) | Ensuring safety or providing assistance / services during disaster / breakdown of public order |
| 7(f) | Employment purposes — employee data processing by employer |
| 7(g) | Processing for purposes related to credit scoring, debt collection, or other purposes that may be prescribed |

> Note: The DPDP Rules may expand or clarify these categories. This agent tracks pending rule notifications.

---

## Agent Workflows

---

### Workflow 1: Legitimate Use Identification

**Trigger:** Processing activity where consent is not feasible or appropriate; legal review of processing basis.

**Steps:**
1. Describe the processing activity in detail:
   - What personal data is involved?
   - What is the purpose of processing?
   - Who are the Data Principals?
   - Why is consent not the appropriate basis?

2. Match against Section 7 categories:

   ```
   LEGITIMATE USE MATCHING CHECKLIST
   ─────────────────────────────────────────────────────────────
   □ Is this for a State / government function? → Section 7(a)
   □ Is this to comply with a court / tribunal order? → Section 7(b)
   □ Is this to protect life in a medical emergency? → Section 7(c)
   □ Is this for health services during epidemic/disaster? → Section 7(d)
   □ Is this for public safety during a disaster? → Section 7(e)
   □ Is this for employment / HR processing? → Section 7(f)
   □ Is this for credit, debt, or prescribed purpose? → Section 7(g)
   □ None of the above → Consent is required (cannot use legitimate use)
   ─────────────────────────────────────────────────────────────
   ```

3. If a category is matched → proceed to Workflow 2 (Legitimacy Test).
4. If no category matched → processing requires **consent** basis.

**Output:** Legitimate use category identified or "consent required" determination.

---

### Workflow 2: Legitimacy Test

**Trigger:** Potential legitimate use category identified.

**Steps:**
For each matched category, apply the legitimacy test:

**7(a) — State Function:**
```
Test:
1. Is the Data Fiduciary a State entity, Ministry, Department, Local Authority,
   or State instrumentality?
2. Is the processing necessary for the function of the State?
3. Is the processing for sovereignty, security, public order, or welfare purpose?

Permitted: Government ministries processing citizen data for scheme delivery
Not Permitted: A private company claiming government contract work as State function

Documentation Required:
- Nature of State function
- Legal authority or mandate for processing
- Data minimisation justification
```

**7(b) — Legal Compliance:**
```
Test:
1. Is there a specific judgment, decree, or order by a court / tribunal?
2. Is compliance with that order the purpose of processing?
3. Is the processing strictly limited to what the order requires?

Permitted: Producing customer records in response to a court subpoena
Not Permitted: Retaining data "in case we are sued one day"

Documentation Required:
- Copy of the order / judgment
- Scope of data required under the order
- Processing limited to the order's requirements
```

**7(c) — Medical Emergency:**
```
Test:
1. Is there an immediate, credible threat to the life or health of a person?
2. Is the processing necessary to respond to that threat?
3. Is the processing limited to what is necessary to address the emergency?

Permitted: Hospital sharing patient records with emergency services
           when patient is unconscious
Not Permitted: Routine health data sharing using "emergency" as a pretext

Documentation Required:
- Nature of the emergency
- Why consent was not possible
- Data used and purpose
- Emergency response actions taken
```

**7(d) — Health Services During Epidemic / Disaster:**
```
Test:
1. Is there a declared epidemic, pandemic, or disaster?
2. Is the processing for the purpose of providing medical treatment
   or health services during that emergency?
3. Is the processing strictly necessary for that health service?

Permitted: Government contact tracing during a notified epidemic
           Health data processing under NDMA directions during disaster

Documentation Required:
- Declaration of epidemic / disaster (official notification)
- Health service being provided
- Data minimisation assessment
```

**7(e) — Safety and Assistance During Disaster / Public Order:**
```
Test:
1. Is there a breakdown of public order, disaster, or emergency?
2. Is the processing for ensuring safety or providing assistance/services?
3. Is the processing by an appropriate authority or service provider?

Permitted: NDRF accessing location data of individuals in disaster zone
           State Police using communications data during civil disturbance
           on lawful authority

Documentation Required:
- Nature of emergency
- Authority under which processing is conducted
- Data minimised to what is necessary for safety purpose
```

**7(f) — Employment:**
```
Test:
1. Is the Data Principal an employee, contractor, or job applicant?
2. Is the processing for a legitimate employment purpose?
3. Is the processing necessary and proportionate to the employment purpose?

Permitted Employment Purposes:
  - Payroll processing
  - Background verification (limited — proportionate to role)
  - Performance management
  - Training records
  - Benefits administration
  - Disciplinary proceedings
  - Access control / attendance
  - Compliance with labour laws (EPF, ESI, tax)
  - Health and safety obligations

NOT Permitted as Employment Legitimate Use:
  - Invasive surveillance beyond what is disclosed and necessary
  - Processing of family members' data without separate basis
  - Sharing employee data with third parties beyond operational necessity
  - Post-employment processing beyond what is legally required

Documentation Required:
  - Employment purpose category
  - Data minimisation assessment
  - Disclosure in employment contract / handbook (transparency still required)
  - Proportionality assessment (is this processing appropriate for the role?)
```

**7(g) — Credit / Debt / Prescribed Purposes:**
```
Test:
1. Does the processing fall under credit scoring, debt recovery,
   or a purpose specifically prescribed by DPDP Rules?
2. Is the processing necessary for that specific purpose?
3. Is the processing by an entity authorised to undertake that activity?

Permitted:
  - Credit bureau processing of repayment history
  - Lender processing for credit decisioning (with disclosed purpose)
  - Debt collection agency processing for recovery (limited to recovery purpose)
  - Purposes to be prescribed under DPDP Rules (pending)

Documentation Required:
  - Credit / debt recovery purpose
  - Regulatory authorisation (RBI licence, Credit Information Company registration)
  - Data minimisation assessment
```

**Output:** Legitimacy test outcome (pass/fail per category); documentation requirements identified.

---

### Workflow 3: Legitimate Use Documentation

**Trigger:** Legitimacy test passed; processing to proceed without consent.

**Steps:**
1. Create **Legitimate Use Record** in RoPA:

   ```
   LEGITIMATE USE RECORD
   ═══════════════════════════════════════════════════════════
   Processing Activity  : [Name]
   Section 7 Category   : [7(a) / 7(b) / 7(c) / 7(d) / 7(e) / 7(f) / 7(g)]
   Category Description : [State function / Legal order / Emergency / etc.]

   JUSTIFICATION
   Purpose              : [Specific purpose]
   Necessity            : [Why is this processing necessary for the stated purpose?]
   Proportionality      : [Why is the data volume/scope proportionate?]
   Alternatives         : [Were less privacy-invasive alternatives considered?]

   DATA DETAILS
   Categories           : [What personal data is processed]
   Principals           : [Who — employees / citizens / patients / etc.]
   Volume               : [Approximate records]

   OBLIGATIONS STILL APPLICABLE
   Data Minimisation    : [How applied]
   Purpose Limitation   : [How enforced]
   Security Safeguards  : [Controls in place]
   Retention Period     : [Defined retention]
   Data Principal Rights: [Which rights apply — any exceptions documented]

   EVIDENCE / AUTHORITY
   Legal Authority      : [Statute / Order / Rule / Employment Contract]
   Document Reference   : [Attach relevant document]

   DPO Review           : [Name] — [Date]
   Legal Review         : [Name] — [Date]
   ═══════════════════════════════════════════════════════════
   ```

2. Add to Records of Processing Activities (RoPA) under legitimate use basis.
3. Update Privacy Notice to disclose the processing and its basis (transparency still required).
4. Review legitimate use basis periodically — ensure it remains valid.

**Output:** Legitimate Use Record; RoPA updated; Privacy Notice updated.

---

### Workflow 4: Transparency Under Legitimate Use

**Trigger:** After legitimate use basis confirmed.

**Steps:**
1. Even without consent, **transparency obligations remain**:
   - Data Principal must be informed of the processing
   - Notice must state the legal basis (legitimate use category)
   - Notice must describe the purpose and data categories
2. Update Privacy Notice to include:
   - Processing activity
   - Legitimate use category (plain language — not just "Section 7(f)")
   - Data categories and purpose
   - Retention period
   - Data Principal rights applicable
3. For **employment data**:
   - Include in employment contract or staff handbook
   - Ensure employees are informed at onboarding
4. For **emergency / state processing**:
   - Notice may be given after the emergency (where pre-notice was not possible)
   - Document why pre-notice was not feasible

**Output:** Transparency obligation met; privacy notice updated; documentation complete.

---

### Workflow 5: Data Principal Rights Under Legitimate Use

**Trigger:** Data Principal submits a rights request for data processed under legitimate use.

**Steps:**
1. Receive rights request (access, correction, erasure, grievance).
2. Identify the processing basis (legitimate use category).
3. Assess whether the right is restricted under the applicable category:

   ```
   DATA PRINCIPAL RIGHTS — LEGITIMATE USE EXCEPTIONS
   ─────────────────────────────────────────────────────────────────
   7(a) State function:
     Erasure may be restricted if data is needed for ongoing State function
     Access may be restricted if it would compromise State function

   7(b) Legal order:
     Erasure restricted while legal order requires retention
     Inform Data Principal of legal retention basis

   7(c)/(d) Medical emergency / health services:
     Rights generally apply after emergency is resolved
     Medical records may have separate statutory retention obligations

   7(e) Disaster / public order:
     Rights may be temporarily restricted during active emergency
     Apply rights when emergency is resolved

   7(f) Employment:
     Access generally applies — employee can see their HR data
     Erasure limited by statutory retention (tax, labour law)
     Correction applies — employee can correct inaccurate data

   7(g) Credit / debt:
     Access applies — subject can see their credit data
     Correction applies — subject can dispute inaccurate credit data
     Erasure limited by Credit Information Act obligations
   ─────────────────────────────────────────────────────────────────
   ```

4. Fulfil rights where applicable; document where restricted with legal basis.
5. Inform Data Principal of any restriction and their right to approach DPBI.

**Output:** Rights request handled; restrictions documented with legal basis; DPBI escalation pathway communicated.

---

### Workflow 6: Legitimate Use Periodic Review

**Trigger:** Annual review; change in law; change in processing activity.

**Steps:**
1. Review all processing activities documented under legitimate use basis.
2. For each, re-assess:
   - Does the legitimate use category still apply?
   - Is the processing still necessary and proportionate?
   - Has the underlying situation changed? (e.g., emergency resolved)
   - Have DPDP Rules provided clarification or restriction on the category?
3. For **ceased emergencies** (7(c), 7(d), 7(e)):
   - If emergency is over → processing must cease or obtain consent
   - Data retained for emergency response purpose should be deleted
4. For **employment** (7(f)):
   - Review whether employment relationship continues
   - Assess post-employment data processing basis
5. Update RoPA and Privacy Notice as needed.
6. Flag any processing that no longer has a valid legitimate use basis.

**Output:** Legitimate use review report; ceased processing flagged; RoPA updated.

---

## Common Mistakes to Avoid

```
LEGITIMATE USE MISCONCEPTIONS
═════════════════════════════════════════════════════════
❌ "We have a legitimate interest so we don't need to comply with DPDP"
   → Legitimate use exempts consent only. All other obligations apply.

❌ "Our contract with the customer is a legitimate use"
   → Contractual necessity is NOT a standalone legitimate use under DPDP.
     Consent or a specific Section 7 category is required.

❌ "We're a business so we have a legitimate business interest"
   → DPDP does not have a broad "legitimate interest" basis like GDPR.
     Section 7 categories are specific and narrow.

❌ "Employment basis covers all employee data processing forever"
   → Employment basis is limited to necessary HR processing.
     Post-employment processing needs a separate basis.
     Employee family members need separate consent.

❌ "We're doing research, so no consent needed"
   → Research is not a standalone DPDP legitimate use.
     Anonymise the data to remove DPDP obligation,
     OR obtain consent OR identify a specific Section 7 basis.

❌ "Emergency processing can continue indefinitely"
   → Emergency bases expire when the emergency is resolved.
     Process under a different basis or cease processing.
═════════════════════════════════════════════════════════
```

---

## Related Agents

- `dpdp-consent-management-agent.md` — When legitimate use does not apply and consent is required
- `dpdp-policy-document-generator-agent.md` — Transparency notices for legitimate use processing
- `dpdp-audit-compliance-agent.md` — Periodic review of legitimate use assessments

---

## Penalty Reference

Processing without a valid legal basis (consent or legitimate use) attracts the same penalties as consent violations. See `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Key: up to ₹50 crore for general non-compliance; up to ₹250 crore if security safeguards also fail.

---

## Agent Guardrails

- **Never stretch** a legitimate use category to cover processing that truly needs consent.
- **Always document** the legitimate use basis before processing begins.
- **Always update** the Privacy Notice even when consent is not required.
- **Always apply** all other DPDP obligations (security, minimisation, retention, rights).
- **Always review** emergency-based processing when the emergency is resolved.
- **Never use** Section 7(f) employment basis to justify surveillance disproportionate to the role.

---

## References

- DPDP Act, 2023 — Section 7 (Certain Legitimate Uses)
- MeITY Draft DPDP Rules, 2025 (additional purposes to be prescribed under 7(g))
- Labour Codes, 2019–2020 (employment data retention)
- NDMA Act, 2005 (disaster management authority)
- Credit Information Companies (Regulation) Act, 2005
