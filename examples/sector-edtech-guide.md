# DPDP Compliance Guide — Edtech & Education

> Practical mini-guide for edtech platforms, schools, and education institutions under DPDP Act 2023.

## Regulatory Overlap

| Requirement | Source | Impact |
|---|---|---|
| Children's data (primary concern) | DPDP S.9 | Verifiable parental consent for all under-18 users |
| No profiling / tracking of children | DPDP S.9(3) | Behavioural monitoring, targeted ads strictly prohibited |
| Age verification | DPDP S.9(1) | Platform must reliably verify user age before processing |
| Teacher/staff employment data | DPDP S.7(f) | Legitimate use — consent not required for employment purposes |
| School as Data Fiduciary | DPDP S.2(i) | Institution determines purpose/means; bears compliance burden |
| Breach notification | DPDP S.8(6) | Notify DPBI; child data breaches attract highest scrutiny |

## Recommended Agent Sequence

```
1. Children's Data Agent        → Age-gate, parental consent, profiling restrictions
2. Consent Management Agent     → Student/parent consent; teacher data notices
3. Privacy by Design Skill      → Embed data minimisation into platform architecture
4. Policy Document Generator Agent       → Generate privacy policy, terms, cookie/data notices
5. Audit Compliance Agent      → Periodic compliance checks and DPBI-ready reports
```

## Compliance Checklist

| # | Item | Status |
|---|---|---|
| 1 | Age verification mechanism implemented for all users | ☐ |
| 2 | Verifiable parental consent collected for under-18 students | ☐ |
| 3 | No behavioural tracking or profiling of children | ☐ |
| 4 | No targeted advertising served to student users | ☐ |
| 5 | Data collection minimised to educational purpose only | ☐ |
| 6 | Teacher/staff data processed under S.7(f) legitimate use | ☐ |
| 7 | School/institution identified as Data Fiduciary with compliance obligations assigned | ☐ |
| 8 | Privacy notice served at student registration (parent-facing) | ☐ |
| 9 | Privacy by Design review completed on platform architecture | ☐ |
| 10 | Third-party SDK/analytics tools audited for child data access | ☐ |
| 11 | Data retention limited to enrolment period + statutory minimum | ☐ |
| 12 | Parent/student data access and erasure workflow operational | ☐ |
| 13 | Breach response plan with child-data escalation path | ☐ |
| 14 | DPO / Grievance Officer appointed and listed on platform | ☐ |
| 15 | Annual compliance audit with artefact generation scheduled | ☐ |

## Key Penalty Risks

| Violation | DPDP Penalty (up to) | Sector Impact |
|---|---|---|
| Processing child data without parental consent (S.9) | ₹200 Cr | Platform ban risk; public backlash |
| Profiling or targeting ads to children (S.9(3)) | ₹200 Cr | MeITY / DPBI enforcement action |
| Missing age verification (S.9(1)) | ₹200 Cr | Deemed non-compliant by default |
| Breach notification failure (S.8(6)) | ₹200 Cr | Heightened scrutiny (child data) |
| Failure to honour erasure requests (S.8(7)) | ₹50 Cr | Parent complaints to DPBI |
| Failure to implement security safeguards (S.8(5)) | ₹250 Cr | Student data breach; trust collapse |

## Common Pitfalls

- **Age verification reduced to a checkbox** — A simple "I am 18+" tick box does not constitute reliable age verification under S.9(1). Platforms need a defensible mechanism (e.g., parent email verification, ID-based checks) to demonstrate compliance.
- **Third-party SDKs and analytics collecting child data silently** — Embedding Google Analytics, Facebook SDK, or ad-tech trackers in a student-facing app can result in behavioural tracking of children, directly violating S.9(3) even if the platform itself does not profile users.
- **Parental consent collected once and never refreshed** — Consent obtained at initial registration may not cover new features, data uses, or third-party integrations added later. Each new purpose requires fresh, specific parental consent.
- **Teacher and staff data treated as exempt from DPDP** — While employment-related processing falls under S.7(f) legitimate use, this does not cover all teacher data. Biometric attendance, performance analytics, or sharing data with third-party HR platforms requires separate consent or a documented lawful basis.
- **Student data retained long after enrolment ends** — Many platforms keep student profiles, learning history, and assessment data indefinitely for "product improvement." DPDP S.8 requires erasure once the educational purpose is served, unless a statutory retention period applies.
- **Schools unaware they are Data Fiduciaries** — Institutions often assume the edtech vendor bears all compliance responsibility. Under DPDP S.2(i), the school that determines the purpose and means of processing is the Data Fiduciary and carries the primary compliance burden.

## Regulator-Specific Timelines

| Event / Obligation | Education Sector Timeline | DPDP Timeline | Notes |
|---|---|---|---|
| Academic year data cycle | Annual (typically Apr–Mar or Jun–May) | Consent valid until withdrawn (S.6) | Align data retention reviews with end-of-academic-year; purge graduated student data |
| NCPCR complaint response | **30 days** (NCPCR / SCPCR complaint norms) | **30 days** (Rule 10, DPDP Rules 2025) | Child data complaints may be filed with both NCPCR and DPBI simultaneously |
| Breach notification | Report to CERT-In within **6 hours** (CERT-In Directions, Apr 2022) | **72 hours** to DPBI (Rule 7, DPDP Rules 2025) | Child data breaches attract the highest scrutiny; notify both bodies immediately |
| Student record retention (state norms) | **3–5 years** post-completion (varies by state education board) | Erase when purpose served (S.8(7)) | Retain per state board norms; erase thereafter unless legal obligation continues |
| Parental consent re-verification | At each new academic year or major platform change | Consent refresh if purpose changes (S.6) | Use academic year rollover as a natural consent refresh checkpoint |
| Grievance redressal | As per school/university grievance norms | **30 days** (Rule 10, DPDP Rules 2025) | Appoint a single Grievance Officer covering academic and data protection complaints |
| Third-party vendor audit | Before each academic year (recommended) | Annual for SDFs (Rule 13(3)); periodic for others | Audit edtech vendors, SDK integrations, and cloud providers before new session begins |

---
*Based on DPDP Act 2023 (enacted) and DPDP Rules 2025 (gazetted November 2025).*
