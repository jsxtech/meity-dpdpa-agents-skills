# DPDP Compliance Guide — Fintech & Banking (RBI Regulated)

> Practical mini-guide for fintech/banking entities regulated by RBI, covering DPDP Act 2023 + RBI-specific mandates.

## Regulatory Overlap

| Requirement | Source | Impact |
|---|---|---|
| Payment data localisation | RBI circular (Apr 2018) | All payment system data stored only in India |
| IT governance framework | RBI Master Direction on IT Framework | Board-level data protection oversight |
| KYC/AML data processing | RBI KYC Directions + DPDP S.7 | Legitimate use — no consent needed for statutory KYC |
| Credit scoring / auto-decisions | DPDP S.6 + S.10 | DPIA mandatory; clear notice to Data Principals |
| UPI transaction data retention | NPCI guidelines + DPDP S.8 | Retain only as long as purpose served; purge thereafter |
| Breach notification | DPDP S.8(6) + RBI cyber framework | Notify DPBI *and* RBI CSITE; RBI expects 6-hour reporting |

## Recommended Agent Sequence

```
1. Data Localisation Agent      → Map data flows; confirm India-only storage for payment data
2. Consent Management Agent     → Implement granular consent (loans, marketing, analytics)
3. DPIA Agent                   → Assess credit scoring, fraud models, automated decisions
4. Vendor Processor Agent            → Evaluate payment gateways, BaaS providers, cloud infra
5. Audit Compliance Agent      → Generate RBI + DPBI audit artefacts
```

## Compliance Checklist

| # | Item | Status |
|---|---|---|
| 1 | Payment system data stored exclusively in India | ☐ |
| 2 | Data flow mapping covers all third-party processors | ☐ |
| 3 | Consent collected before non-KYC processing (marketing, analytics) | ☐ |
| 4 | KYC/AML processing documented as legitimate use (S.7) | ☐ |
| 5 | DPIA completed for credit scoring / automated lending | ☐ |
| 6 | Privacy notice served at account opening and loan origination | ☐ |
| 7 | UPI/payment data retention policy with auto-purge | ☐ |
| 8 | Vendor agreements include DPDP data processing clauses | ☐ |
| 9 | Payment gateway vendors assessed for localisation compliance | ☐ |
| 10 | Breach response plan covers both DPBI and RBI CSITE | ☐ |
| 11 | Board-level DPO / Grievance Officer appointed | ☐ |
| 12 | IT governance framework aligned with RBI Master Direction | ☐ |
| 13 | Customer data access / erasure request workflow operational | ☐ |
| 14 | Children's accounts (minor savings) handled per S.9 | ☐ |
| 15 | Annual compliance audit scheduled with artefact generation | ☐ |

## Key Penalty Risks

| Violation | DPDP Penalty (up to) | RBI Action |
|---|---|---|
| Failure to implement security safeguards (S.8(5)) | ₹250 Cr | Monetary penalty + directive |
| Data stored outside India (S.16) | ₹50 Cr | Licence review / restriction |
| Missing / invalid consent (S.6) | ₹50 Cr | — |
| Breach notification failure (S.8(6)) | ₹200 Cr | Monetary penalty + directive |
| Children's data mishandling (S.9) | ₹200 Cr | — |
| Non-compliance with data erasure (S.8(7)) | ₹50 Cr | — |

## Common Pitfalls

- **Treating KYC consent as blanket consent** — Statutory KYC under S.7 covers identity verification only; using KYC-collected data for marketing or credit scoring still requires separate, specific consent under S.6.
- **Ignoring UPI transaction data retention limits** — Many fintechs retain full transaction histories indefinitely for analytics. NPCI guidelines and DPDP S.8 require purging data once the stated purpose is served.
- **Payment gateway vendors assumed compliant** — Onboarding a PCI-DSS certified gateway does not satisfy DPDP processor obligations. Vendor agreements must include explicit data processing clauses, localisation commitments, and breach notification duties.
- **Delayed dual-track breach reporting** — RBI CSITE expects reporting within 6 hours of detection, while DPDP requires notification to DPBI. Teams often report to one and forget the other, or wait for internal investigation before notifying either.
- **Credit scoring models deployed without DPIA** — Automated lending decisions based on transaction patterns, app usage, or alternative data require a DPIA under S.10. Many fintechs skip this, treating models as internal tooling.
- **Minor savings accounts overlooked** — Banks offering minor/teen savings accounts or wallets must comply with S.9 children's data provisions, including verifiable parental consent and a ban on profiling — often missed in digital onboarding flows.

## Regulator-Specific Timelines

| Event / Obligation | RBI / CERT-In Timeline | DPDP Timeline | Notes |
|---|---|---|---|
| Cyber incident reporting | **6 hours** to CERT-In (CERT-In Directions, Apr 2022) | **72 hours** to DPBI (Rule 7, DPDP Rules 2025) | RBI-regulated entities must also report to RBI CSITE within 6 hours |
| Breach notification to Data Principals | — | Without unreasonable delay where harm is likely (Rule 7) | Notify with plain language explanation and recommended protective actions |
| Data localisation compliance | Immediate (RBI circular effective since Oct 2018) | N/A (DPDP does not mandate localisation; S.16 governs transfers) | Payment system data must be stored only in India per RBI |
| KYC periodic re-verification | Every 2 / 8 / 10 years (risk-based) per RBI KYC Directions | Consent refresh if purpose changes (S.6) | Re-KYC does not require fresh DPDP consent if purpose unchanged |
| IT governance audit | Annual (RBI Master Direction on IT Framework) | Annual for SDFs (Rule 13(3)) | Align DPDP audit cycle with RBI annual IT audit |
| Grievance redressal response | 30 days (RBI Integrated Ombudsman) | **30 days** (Rule 10) | Appoint a single officer covering both RBI and DPDP grievances |
| Data retention / purge | As per NPCI / RBI product-specific norms | Erase when purpose served or consent withdrawn (S.8(7)) | Whichever is shorter applies; document retention rationale |

---
*Based on DPDP Act 2023 (enacted) and DPDP Rules 2025 (gazetted November 2025). Cross-referenced with current RBI circulars.*
