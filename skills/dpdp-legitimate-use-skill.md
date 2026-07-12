---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Legitimate Use"
type: "skill"
---

# DPDP Legitimate Use Skill

## Skill Identity

**Skill Name:** dpdp-legitimate-use
**Domain:** Section 7 Legitimate Uses — Consent-Free Processing
**Skill Type:** Legal, Compliance, Advisory
**Applicable To:** DPOs, Legal Teams, HR, Compliance, Government Entities, Healthcare, Financial Services

---

## Skill Purpose

Identify, assess, document, and apply the **Section 7 legitimate use categories** under the DPDP Act — the narrow, defined circumstances where processing personal data without consent is lawful. Prevent both over-reliance on legitimate use (replacing consent where consent is required) and under-use (seeking consent where a simpler legitimate use basis applies).

---

## The Legitimate Use Landscape

```
DPDP ACT — LAWFUL PROCESSING BASES
══════════════════════════════════════════════════════════════
BASIS 1: CONSENT (Section 6)
  Free, specific, informed, unconditional, unambiguous
  → Most common; use when individual can meaningfully choose

BASIS 2: LEGITIMATE USE (Section 7)
  Processing without consent is lawful ONLY in these categories:
  7(a) State / government function
  7(b) Compliance with court/tribunal order
  7(c) Medical emergency — threat to life or health
  7(d) Health services during epidemic / disaster
  7(e) Safety / assistance during disaster / public order breakdown
  7(f) Employment / HR processing
  7(g) Credit, debt, prescribed purposes (Rules pending)

IMPORTANT: No "legitimate interests" balancing test like GDPR.
           If the purpose doesn't fit a Section 7 category → consent needed.
══════════════════════════════════════════════════════════════
```

---

## Skill Capabilities

---

### Capability 1: Legitimate Use Category Selector

**Trigger:** "what is our legal basis", "do we need consent for this", "legitimate use or consent"

**Decision Tool:**

```
LEGAL BASIS DECISION TREE
─────────────────────────────────────────────────────────────────
Q1: Is the Data Principal an employee / contractor / applicant?
    YES → Section 7(f) Employment applies for HR purposes
          (Still need consent for non-HR purposes e.g. marketing)

Q2: Is there a court, tribunal, or government order requiring this processing?
    YES → Section 7(b) Legal compliance

Q3: Is this processing by a State entity for a sovereign / government function?
    YES → Section 7(a) State function

Q4: Is there an immediate threat to life or health?
    YES → Section 7(c) Medical emergency

Q5: Is this for health services during a declared epidemic / disaster?
    YES → Section 7(d) Health services

Q6: Is this for safety / assistance during a declared disaster or public order breakdown?
    YES → Section 7(e) Disaster / public order

Q7: Is this for credit scoring, debt collection, or a Rules-prescribed purpose?
    YES → Section 7(g) Credit / prescribed

Q8: None of the above?
    → CONSENT IS REQUIRED
─────────────────────────────────────────────────────────────────
```

**Output:** Legal basis determination; consent or legitimate use route identified.

---

### Capability 2: Employment Legitimate Use — Deep Dive

**Trigger:** "employment data legal basis", "can we process employee data without consent", "HR data DPDP"

**What Section 7(f) Covers:**

```
EMPLOYMENT LEGITIMATE USE — PERMITTED PROCESSING
══════════════════════════════════════════════════════════════
RECRUITMENT
  □ Processing application data for hiring decisions
  □ Background verification (proportionate to role)
  □ Reference checks
  □ Pre-employment screening (PAN, Aadhaar for KYC)

EMPLOYMENT ADMINISTRATION
  □ Payroll processing — salary, deductions, bank details
  □ Tax filing — TDS, Form 16, ITR filing assistance
  □ EPF / ESI administration
  □ Gratuity, leave, bonus management
  □ Contract management

PERFORMANCE & DEVELOPMENT
  □ Performance appraisals and records
  □ Training and development records
  □ Promotion and career records

ATTENDANCE & ACCESS
  □ Biometric attendance (if necessary and disclosed)
  □ Physical access control
  □ IT access provisioning and logging

HEALTH & SAFETY
  □ Occupational health records
  □ Medical fitness for role (limited — proportionate)
  □ Workplace accident records

COMPLIANCE
  □ Professional licence verification
  □ Conflict of interest declarations
  □ POSH complaint records (strict confidentiality)
  □ Whistleblower reports

MONITORING (requires disclosure in employment terms)
  □ Email and device monitoring (security purposes, proportionate)
  □ Internet use monitoring (policy compliance)
  □ Location tracking (field staff — proportionate)
══════════════════════════════════════════════════════════════

EMPLOYMENT LEGITIMATE USE DOES NOT COVER:
  ✗ Marketing to employees using their employment data
  ✗ Processing employee family members' data (need separate basis)
  ✗ Post-employment processing beyond legal retention requirements
  ✗ Surveillance disproportionate to role or purpose
  ✗ Sharing employee data with third parties beyond operational need
  ✗ Profiling employees for commercial purposes unrelated to employment
```

**Output:** Employment data processing assessment; what is and isn't covered.

---

### Capability 3: State Function Legitimate Use

**Trigger:** "government processing", "state function DPDP", "public authority data"

**Section 7(a) Scope:**

```
STATE FUNCTION LEGITIMATE USE
─────────────────────────────────────────────────────────────
WHO CAN USE THIS BASIS:
  □ Central and State Government Ministries
  □ Government Departments
  □ Local Authorities (Municipal Corporations, Panchayats)
  □ Statutory Authorities and Boards
  □ Public Sector Undertakings (limited — for state function activities)

WHAT QUALIFIES AS STATE FUNCTION:
  □ Welfare scheme administration (PM-Kisan, MGNREGA, Ayushman Bharat)
  □ Tax administration (Income Tax, GST)
  □ Law enforcement and national security
  □ Voter roll maintenance and election administration
  □ Judicial and quasi-judicial proceedings
  □ Public health programmes
  □ Regulatory licensing and enforcement
  □ Census and statistical surveys
  □ Land records and property registration

WHAT DOES NOT QUALIFY:
  ✗ Commercial activities of government entities (not sovereign in nature)
  ✗ Private companies claiming government contractor status
  ✗ Processing for political party activities
  ✗ Activities beyond the entity's mandated functions
─────────────────────────────────────────────────────────────
```

**Output:** State function assessment; qualifying and non-qualifying activities mapped.

---

### Capability 4: Emergency Legitimate Uses

**Trigger:** "emergency data processing", "medical emergency DPDP", "disaster data"

**Section 7(c), 7(d), 7(e) — Emergency Bases:**

```
EMERGENCY LEGITIMATE USES — DECISION AND DOCUMENTATION
════════════════════════════════════════════════════════════
SECTION 7(c) — MEDICAL EMERGENCY (individual)
Criteria:
  □ Immediate, credible threat to life or health
  □ Individual is incapacitated or unreachable
  □ Processing is necessary to address the emergency
  □ Processing is limited to what is necessary

Examples:
  ✓ Hospital sharing unconscious patient's blood type with trauma team
  ✓ Employer sharing employee's medical alert with ambulance crew
  ✗ Routine data sharing dressed up as an "emergency"

Documentation:
  □ Nature of emergency
  □ Why consent was impossible
  □ Data shared and recipient
  □ Time of emergency and resolution

SECTION 7(d) — EPIDEMIC / DISASTER HEALTH SERVICES
Criteria:
  □ Declared epidemic, pandemic, or disaster (official notification)
  □ Processing for providing medical treatment or health services
  □ Processing strictly necessary for that health service

Examples:
  ✓ Government contact tracing during notified epidemic
  ✓ Hospital sharing patient data under NDMA directions during disaster
  ✗ Post-epidemic retention of contact tracing data

Documentation:
  □ Official declaration / notification reference
  □ Health service being provided
  □ Data minimisation assessment

SECTION 7(e) — DISASTER / PUBLIC ORDER SAFETY
Criteria:
  □ Declared disaster or breakdown of public order
  □ Processing for safety, rescue, or assistance
  □ Processing by appropriate authority or emergency service

Examples:
  ✓ NDRF using location data of persons trapped in flood zone
  ✓ Police using communication data during notified public order breakdown
  ✗ Post-emergency retention of emergency response data
  ✗ Private companies using disaster as pretext for data collection
════════════════════════════════════════════════════════════
```

**Output:** Emergency basis assessment; documentation requirements; expiry trigger.

---

### Capability 5: Post-Emergency Data Handling

**Trigger:** "emergency data after emergency ends", "what to do with disaster data", "emergency processing expiry"

**Steps:**
1. Confirm the emergency has officially ended (government announcement / notification lapse).
2. Review all data collected under emergency basis:
   - Is continued processing necessary for a non-emergency purpose?
   - Is there a separate legal basis for continued processing?
3. If NO separate basis:
   - Issue data deletion instruction within 30 days of emergency end
   - Propagate deletion to all emergency response partners
   - Obtain deletion certificates from processors
4. If separate basis exists (e.g., aggregated health surveillance under state function):
   - Document the new basis
   - Anonymise where possible
   - Update privacy notice
5. Log all decisions with rationale.

**Output:** Post-emergency data review; deletion or re-based; documentation complete.

---

### Capability 6: Legitimate Use Documentation Register

**Trigger:** "document our legitimate uses", "legitimate use register", "legal basis register"

**Register Schema:**

```
LEGITIMATE USE REGISTER
═══════════════════════════════════════════════════════════════════
Entry ID          : LU-001
Processing Activity: [e.g., Employee payroll processing]
Section 7 Category : 7(f) — Employment
Category Basis     : Payroll processing for employees under employment contract

JUSTIFICATION
Purpose           : Payment of monthly salary; statutory deductions
Necessity         : Cannot fulfil employment obligation without processing
                    bank account details, PAN, salary structure
Proportionality   : Data limited to what payroll processor requires
Alternatives      : No privacy-neutral alternative for salary payment

DATA DETAILS
Categories        : Name, bank account, PAN, salary structure, tax data
Data Principals   : Active employees
Volume            : [n] employees

OBLIGATIONS APPLIED
Data Minimisation : Only data needed for payroll collected
Purpose Limitation: Used only for payroll; not for other HR functions
Security          : Payroll system — access limited to HR and Finance
Retention         : 7 years (Income Tax Act) → then deleted
Rights            : Access and correction rights available

TRANSPARENCY
Disclosed in      : Employment Agreement (Clause X)
Privacy Notice    : Employee Privacy Notice (Section Y)

DPO Review        : [Name] — [Date]
Legal Review      : [Name] — [Date]
Last Reviewed     : [Date]
Next Review       : [Date — annual]
═══════════════════════════════════════════════════════════════════
```

**Output:** Populated Legitimate Use Register; all legitimate use bases documented.

---

## Common Legitimate Use Mistakes

```
MISTAKE 1: "Legitimate Interest" does not exist under DPDP
The DPDP Act does not have a "legitimate interest" basis like GDPR Article 6(1)(f).
Do not use this term or concept in DPDP compliance documentation.
→ Use consent OR identify a specific Section 7 category.

MISTAKE 2: Employment basis doesn't cover everything employee-related
Section 7(f) covers necessary HR processing only.
Employee data used for marketing, research, or unrelated purposes still needs consent.

MISTAKE 3: Legitimate use doesn't mean no other obligations apply
Data minimisation, security, retention limits, Data Principal rights,
and breach notification ALL still apply under legitimate use.

MISTAKE 4: Section 7(g) is still pending
The additional prescribed purposes under Section 7(g) require DPDP Rules notification.
Do not rely on 7(g) for purposes beyond credit/debt until Rules are published.

MISTAKE 5: Emergency basis doesn't extend post-emergency
Once an emergency is resolved, the emergency basis expires.
Data must be deleted or re-based on a different lawful basis.
```

---

## Quick Commands

| Command | Action |
|---|---|
| `/legit-use-selector` | Determine consent vs legitimate use for a processing activity |
| `/legit-employment` | Assess employment data processing under Section 7(f) |
| `/legit-state` | Assess state function processing under Section 7(a) |
| `/legit-emergency` | Assess emergency processing under Sections 7(c)/(d)/(e) |
| `/legit-post-emergency` | Handle data after emergency basis expires |
| `/legit-register` | Build and maintain Legitimate Use Register |

---

## Related Skills

- `dpdp-consent-manager-skill.md` — Consent vs legitimate use
- `dpdp-contract-clauses-skill.md` — Employment clauses
- `dpdp-audit-checklist-skill.md` — Legitimate use audit

---

## Skill Guardrails

- **Never use** legitimate use as a blanket alternative to consent — each category has strict boundaries.
- **Always document** the legal basis before processing begins, not retrospectively.
- **Never extend** emergency processing beyond the duration of the emergency.
- **Always respect** Data Principal rights even when processing under legitimate use.
- **Always review** legitimate use assessments periodically — circumstances change.

---

## References

- DPDP Act, 2023 — Section 7 (Certain Legitimate Uses)
- MeITY DPDP Rules, 2025 (Notified)
- Labour Codes, 2019–2020
- NDMA Act, 2005 (disaster management)
- Epidemic Diseases Act, 1897 (as amended)
- Disaster Management Act, 2005
- Credit Information Companies (Regulation) Act, 2005
