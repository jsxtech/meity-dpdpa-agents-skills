---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Sector-Specific Compliance"
type: "skill"
---

# DPDP Sector-Specific Compliance Skill

## Skill Identity

**Skill Name:** dpdp-sector-specific-compliance
**Domain:** Sector Compliance — Fintech, Healthtech, Edtech, E-commerce, HR/Employment, Telecom
**Skill Type:** Regulatory, Compliance, Legal
**Applicable To:** DPOs, Legal Teams, Compliance Officers, Product Teams in regulated sectors

---

## Skill Purpose

Apply the DPDP Act in combination with **sector-specific regulations** that impose additional or overlapping data protection requirements. Identify where sectoral rules are stricter, identify conflicts, and navigate dual compliance obligations.

---

## Regulatory Overlay Map

```
DPDP Act (Baseline)
│
├── Fintech / Banking / Payments
│       RBI Master Directions, Payment Aggregator Guidelines,
│       Account Aggregator Framework, PMLA, Credit Information Rules
│
├── Healthcare / Healthtech
│       IT Act (Sensitive Personal Data Rules), Clinical Establishments Act,
│       DISHA (Digital Health Data) — pending, NHA Digital Health Mission
│
├── Edtech / Education
│       UGC Regulations, NEP 2020 data norms, COPPA-equivalent (children)
│
├── E-commerce / Consumer Internet
│       Consumer Protection Act 2019, E-commerce Rules 2020,
│       IT (Intermediary Guidelines) Rules 2021
│
├── Telecom / ISPs
│       TRAI regulations, Unified Licence conditions,
│       DoT data localisation norms
│
├── Insurance
│       IRDAI data governance guidelines, Insurance Act
│
├── Capital Markets / Securities
│       SEBI data governance guidelines, SEBI Cyber Security Circular
│
└── HR / Employment
        Labour Codes, EPF & ESI Acts, Sexual Harassment (POSH) Act
```

---

## Sector Capabilities

---

### Capability 1: Fintech / Banking / Payments Compliance

**Trigger:** "fintech DPDP", "RBI data rules", "payments data compliance", "banking privacy"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| RBI Master Direction on IT | Data localisation for payment system data in India |
| Payment Aggregator Guidelines | Storage of card data — PCI DSS + RBI localisation |
| Account Aggregator Framework | Consent for financial data sharing via AA |
| PMLA / KYC Directions | Customer data retention — 5 years minimum post-relationship |
| Credit Information (Regulation) Act | Credit data — consent, accuracy, grievance rights |

**DPDP + Fintech Compliance Checklist:**
```
□ Payment data stored in India (RBI localisation mandate)
□ Card data — PCI DSS compliant; no full card number stored
□ KYC data retained for minimum 5 years (PMLA)
□ DPDP consent obtained for processing beyond KYC/AML obligation
□ Credit bureau data — separate consent; correction rights
□ Account Aggregator consent — FIP/FIU obligations met
□ Fraud detection — legitimate use; data minimisation applied
□ Cross-border transfer — RBI approval + DPDP permissibility
□ Customer grievance — RBI Banking Ombudsman + DPDP DPBI
□ Data breach — RBI CERT-In reporting + DPDP DPBI notification
```

**Conflict Resolution:**
- Where RBI mandates longer retention than DPDP purpose requires → RBI prevails (legal obligation basis)
- Where DPDP consent requirements are stricter than RBI minimum → apply DPDP standard
- Cross-border: RBI localisation takes precedence; DPDP permissibility applies additionally

**Output:** Fintech dual-compliance assessment; RBI + DPDP gap report.

---

### Capability 2: Healthcare / Healthtech Compliance

**Trigger:** "healthtech DPDP", "health data privacy", "medical data compliance", "patient data DPDP"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| IT Act — SPDI Rules 2011 | Health / medical data as sensitive personal data — consent required |
| NHA ABDM / ABHA | Digital health data — consent for sharing via HIP/HIU |
| Clinical Establishments Act | Medical record retention norms |
| DISHA (pending) | Specific digital health data protection framework |

**DPDP + Healthtech Compliance Checklist:**
```
□ Health data classified as Tier 1 Sensitive — enhanced controls
□ Separate, specific consent for each health data processing purpose
□ Patient data stored in India — no cross-border transfer without DPDP + regulatory clearance
□ ABHA / ABDM consent architecture integrated (for digital health ecosystem)
□ Medical records retained per Clinical Establishments Act norms
□ Research use of health data — anonymised; ethics committee approval
□ Telemedicine data — consent for recording; data minimisation
□ Wearable / IoT health data — continuous consent; data minimisation
□ Minor patients — parental consent (DPDP) + clinical consent norms
□ Data breach — CERT-In + DPDP DPBI notification
□ Staff access to patient data — need-to-know; audit logging
```

**Special Consideration — Research Exception:**
DPDP allows processing of personal data for research / statistical purposes without consent if:
- Data is anonymised (not re-identifiable)
- Purpose is genuine research
- Institutional review / ethics committee approval in place

**Output:** Healthtech dual-compliance assessment; patient data protection checklist.

---

### Capability 3: Edtech / Education Compliance

**Trigger:** "edtech DPDP", "student data privacy", "education data compliance", "children's data edtech"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| DPDP Act — Sec 9 | All students under 18 → parental consent mandatory |
| IT (Intermediary Guidelines) 2021 | Platform obligations for user data |
| UGC e-content guidelines | Student data in online learning |
| NEP 2020 | Student data for learning outcomes — anonymisation preferred |

**DPDP + Edtech Compliance Checklist:**
```
□ Age verification for all users before data collection
□ Users under 18 — verifiable parental consent obtained
□ No profiling of students under 18
□ No targeted advertising to students under 18
□ No behavioural tracking of students under 18
□ Learning analytics — anonymised or pseudonymised
□ Student performance data — access limited to educators and parents
□ Student data not shared with third-party advertisers
□ Parental dashboard — parents can view, correct, delete child's data
□ Data breach affecting students — notify parents + DPBI
□ Retention — student data deleted or anonymised after course completion
□ EdTech platform as Data Fiduciary for students; school as joint/separate fiduciary
```

**High-Risk Scenario — AI-Powered Adaptive Learning:**
- AI models trained on student performance data → DPIA required
- No automated decisions that materially affect student outcomes without human review
- Bias audits on AI learning recommendations

**Output:** Edtech compliance assessment; children's data protection plan.

---

### Capability 4: E-commerce & Consumer Internet Compliance

**Trigger:** "e-commerce DPDP", "consumer data compliance", "online platform privacy", "marketplace data"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| Consumer Protection Act 2019 | No unfair trade practices in data use |
| E-Commerce Rules 2020 | Disclosure of data collection; no manipulation |
| IT (Intermediary Guidelines) 2021 | Grievance officer; due diligence |
| Competition Act | Data-driven market dominance concerns |

**DPDP + E-commerce Compliance Checklist:**
```
□ Consent for personalisation / recommendation algorithms
□ Consent for marketing communications (separate from purchase consent)
□ No dark patterns in checkout or account creation
□ Purchase history — separate consent for use beyond order fulfilment
□ Location data — consent for precise tracking; minimise to city-level where possible
□ Third-party seller data sharing — DPA with each seller receiving customer data
□ Loyalty programme — clear disclosure of data use
□ Returns / refunds — data retention aligned with consumer protection timelines
□ Guest checkout option — do not force account creation (data minimisation)
□ Cookie consent — granular consent; no pre-ticked
□ Profiling — consent; right to object
□ Cross-border: customer data stays in India unless DPDP permissibility confirmed
□ Grievance Officer appointed (IT Rules) = also handles DPDP grievances
```

**Output:** E-commerce privacy compliance checklist; dark pattern audit.

---

### Capability 5: Telecom & ISP Compliance

**Trigger:** "telecom DPDP", "ISP data compliance", "telecom privacy", "subscriber data"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| TRAI Regulations | Customer data — consent for commercial communication |
| DoT Unified Licence | Subscriber data localisation; confidentiality |
| IT Act | Interception obligations; data retention for lawful intercept |
| TRAI DND Regulations | Opt-in/opt-out for commercial communications |

**DPDP + Telecom Compliance Checklist:**
```
□ Subscriber data localised in India (DoT + DPDP)
□ Consent for use of call/data patterns beyond service delivery
□ TRAI DND compliance — commercial comms only with consent
□ CDR (Call Detail Records) — retention per lawful intercept norms; not beyond
□ Network data (IP logs, traffic) — retention per law; not used for profiling without consent
□ Location data — consent for real-time location use beyond network routing
□ Lawful intercept — only on legal order; data minimisation
□ Data breach — CERT-In + TRAI + DPDP DPBI notification
□ Cross-border: DoT restrictions + DPDP permissibility
□ Customer grievance — TRAI Consumer Protection + DPDP grievance mechanism
```

**Output:** Telecom compliance matrix; subscriber data protection plan.

---

### Capability 6: HR / Employment Data Compliance

**Trigger:** "HR data DPDP", "employee privacy", "employment data compliance", "workforce data"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| Labour Codes (2019–2020) | Employee records retention |
| EPF & ESI Acts | Contribution and benefit data |
| POSH Act | Sexual harassment complaint data — confidentiality |
| Income Tax Act | Payroll and tax data retention (7 years) |

**DPDP + HR Compliance Checklist:**
```
□ Employee privacy notice issued at onboarding
□ Consent or legitimate use basis for each HR processing activity
□ Background verification — consent; data minimisation; no adverse action without notice
□ Payroll data — retained 7 years (Income Tax); access restricted to HR / Finance
□ Performance data — used only for stated HR purposes; no secondary use
□ Health data (sick leave, medical certificates) — Tier 1; strict access control
□ Biometric attendance data — Tier 1; consent; minimise retention
□ POSH complaint data — strict confidentiality; access limited to IC members
□ Monitoring (email, device, internet) — disclosed in employment contract; proportionate
□ Termination — data retained per legal obligation; non-essential data deleted
□ Cross-border: overseas payroll / HRIS providers — DPA + DPDP permissibility
□ Employee rights under DPDP — access, correction, erasure (within legal retention limits)
□ Third-party HR vendors (payroll, recruitment) — DPA required
```

**Special Note — Employee Monitoring:**
Monitoring employees (calls, emails, devices, location) is a processing activity requiring:
- Disclosure in employment contract / policy (transparency)
- Legitimate use basis (not consent — cannot be free if employment depends on it)
- Proportionality — monitoring only as extensive as necessary for the stated purpose
- No continuous surveillance beyond what is justified

**Output:** HR data compliance assessment; employee privacy notice template; monitoring policy review.

---

### Capability 7: Insurance Compliance

**Trigger:** "insurance DPDP", "IRDAI data compliance", "policyholder data privacy"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| IRDAI Guidelines on Information Security | Insurer data security, breach reporting |
| Insurance Act | Policy records retention |
| IRDAI (Protection of Policyholders' Interests) Regulations | Customer data disclosure; consent |

**DPDP + Insurance Compliance Checklist:**
```
□ Policyholder consent for data processing beyond policy issuance
□ Health / medical data (for health insurance) — Tier 1; enhanced controls
□ Underwriting algorithms — DPIA; bias audit; right to explanation
□ Claims data — access restricted to claims team; audit logged
□ Policy records — retained per Insurance Act norms
□ Third-party data (hospitals, garages) — DPA required
□ Fraud detection — legitimate use; data minimisation
□ Marketing using policyholder data — separate consent
□ Cross-border reinsurance — data transfer assessment
□ IRDAI breach reporting + DPDP DPBI notification
```

**Output:** Insurance compliance checklist; IRDAI + DPDP dual compliance assessment.

---

### Capability 8: Capital Markets / Securities Compliance

**Trigger:** "SEBI DPDP", "capital markets data compliance", "investor data privacy", "securities firm DPDP"

**Key Regulatory Obligations:**

| Regulation | Key Data Requirement |
|---|---|
| SEBI Cyber Security Circular | Data classification, localisation, breach reporting |
| SEBI (KYC Registration Agencies) Regulations | KYC data sharing and retention |
| PMLA | Investor identity and transaction records — 5 years |
| Depositories Act | Investor account data |

**DPDP + Securities Compliance Checklist:**
```
□ Investor data localised in India (SEBI + DPDP)
□ KYC data — consent for use beyond regulatory obligation
□ Transaction data — retained 5 years (PMLA); access restricted
□ Algorithmic trading data — not used for profiling investors without consent
□ Research reports — no personal investor data included
□ Third-party KRA / depository data sharing — DPA required
□ Cyber incident — SEBI CERT-In reporting + DPDP DPBI notification
□ Investor grievance — SEBI SCORES + DPDP grievance mechanism
□ Portfolio data — no sharing with affiliates without consent
```

**Output:** Securities compliance matrix; investor data protection checklist.

---

## Conflict Resolution Framework

When DPDP and sector regulation conflict:

```
CONFLICT RESOLUTION DECISION TREE
────────────────────────────────────────────────────────
1. Is the conflict on RETENTION?
   → Longer of the two periods applies (legal obligation basis)
   → Document the applicable regulation as legal basis in RoPA

2. Is the conflict on CONSENT?
   → Apply stricter of the two standards (DPDP is generally stricter)
   → Where sector regulation exempts consent → document as legitimate use

3. Is the conflict on LOCALISATION?
   → Apply stricter localisation requirement (RBI/DoT/SEBI localisation
     + DPDP permissibility)

4. Is the conflict on BREACH NOTIFICATION?
   → Comply with BOTH — notify all applicable regulators
   → CERT-In (6 hours), DPBI (prescribed timeline), sectoral regulator (as required)

5. Is the conflict on INDIVIDUAL RIGHTS?
   → Apply DPDP rights as minimum; sector regulation may provide additional rights
   → Where sector rules restrict erasure → document legal basis; inform Data Principal

6. Novel conflict not covered above?
   → Escalate to Legal; document analysis; apply precautionary approach
────────────────────────────────────────────────────────
```

---

## Quick Commands

| Command | Action |
|---|---|
| `/sector-fintech` | Run fintech dual-compliance assessment |
| `/sector-healthtech` | Run healthtech compliance checklist |
| `/sector-edtech` | Run edtech / children's data compliance |
| `/sector-ecommerce` | Run e-commerce privacy audit |
| `/sector-telecom` | Run telecom subscriber data assessment |
| `/sector-hr` | Run HR / employment data compliance |
| `/sector-insurance` | Run insurance compliance checklist |
| `/sector-securities` | Run capital markets compliance assessment |
| `/sector-conflict` | Resolve DPDP vs sector regulation conflict |

---

## Related Skills

- `dpdp-dpo-skill.md` — Sector DPO requirements
- `dpdp-penalty-enforcement-skill.md` — Sector penalty exposure
- `dpdp-international-comparison-skill.md` — Cross-jurisdiction

---

## Skill Guardrails

- **Always verify** sector-specific requirements against the latest regulator circulars — regulations change frequently.
- **When DPDP and sector rules conflict**, apply the stricter standard unless legal counsel advises otherwise.
- **Never assume** DPDP compliance alone satisfies sector-specific obligations.
- **Always document** the rationale when choosing one regulatory standard over another.
- **Always escalate** to legal counsel for novel or ambiguous cross-regulatory conflicts.

---

## References

- DPDP Act, 2023
- RBI Master Directions on IT Framework for NBFC / Banks
- IRDAI Information Security Guidelines
- SEBI Cyber Security and Cyber Resilience Circular
- TRAI Telecom Consumer Protection Regulations
- IT (Reasonable Security Practices and SPDI) Rules, 2011
- CERT-In Cyber Incident Reporting Directions, 2022
