# DPDP Compliance Guide — Healthtech & Healthcare

> Practical mini-guide for healthtech platforms, hospitals, and digital health providers under DPDP Act 2023.

## Regulatory Overlap

| Requirement | Source | Impact |
|---|---|---|
| Health data as personal data | DPDP S.4, S.6 | Free, specific, informed consent for all health data processing |
| Telemedicine data handling | Telemedicine Guidelines 2020 + DPDP | Consent + secure storage for teleconsultation records |
| ABDM integration | ABDM Health Data Mgmt Policy | ABHA-linked records follow ABDM consent framework |
| Clinical trial exemptions | DPDP S.17(2) + ICMR guidelines | Anonymised data may be exempt; raw data needs consent |
| Patient data sharing | DPDP S.6 + S.7 | Sharing with labs/pharmacies needs purpose-specific consent |
| Breach notification | DPDP S.8(6) | Notify DPBI; health breaches carry reputational + legal risk |

## Recommended Agent Sequence

```
1. Consent Management Agent     → Patient consent for diagnosis, treatment, sharing
2. DPIA Agent                   → Assess telemedicine, AI diagnostics, health analytics
3. Children's Data Agent        → Paediatric records: parental consent, no profiling
4. Anonymisation & Pseudonymisation Agent          → De-identify data for research / public health use
5. Vendor Processor Agent            → Labs, pharmacies, cloud/EHR vendors, ABDM gateways
```

## Compliance Checklist

| # | Item | Status |
|---|---|---|
| 1 | Free, specific, informed consent obtained before processing health data | ☐ |
| 2 | Consent granular per purpose (treatment, insurance, research) | ☐ |
| 3 | ABDM consent artefacts integrated where ABHA IDs used | ☐ |
| 4 | DPIA completed for AI diagnostics / telemedicine platforms | ☐ |
| 5 | Paediatric data processed only with verifiable parental consent | ☐ |
| 6 | No behavioural tracking or ad targeting on patient data | ☐ |
| 7 | Clinical trial data anonymised before secondary research use | ☐ |
| 8 | Research exemption documented with ICMR ethics approval | ☐ |
| 9 | EHR/EMR vendor agreements include DPDP processing clauses | ☐ |
| 10 | Lab and pharmacy data-sharing limited to stated purpose | ☐ |
| 11 | Patient right to access and erasure workflow operational | ☐ |
| 12 | Breach response plan with health-sector escalation path | ☐ |
| 13 | Data retention aligned with clinical record norms | ☐ |
| 14 | Privacy notice displayed at registration and teleconsultation | ☐ |
| 15 | DPO / Grievance Officer appointed and contactable | ☐ |

## Key Penalty Risks

| Violation | DPDP Penalty (up to) | Sector Impact |
|---|---|---|
| Failure to implement security safeguards (S.8(5)) | ₹250 Cr | Patient data breach; trust collapse |
| Processing health data without consent (S.6) | ₹50 Cr | Trust erosion |
| Children's health data mishandling (S.9) | ₹200 Cr | Regulatory scrutiny |
| Breach notification failure (S.8(6)) | ₹200 Cr | Complaints to DPBI; reputational risk |
| Non-anonymised research data sharing | ₹50 Cr | Ethics board action |
| Failure to honour erasure requests (S.8(7)) | ₹50 Cr | Complaints to DPBI |

## Common Pitfalls

- **Conflating treatment consent with data processing consent** — A patient consenting to a medical procedure does not automatically consent to digital processing of their health records. DPDP S.6 requires a separate, specific data processing notice and consent.
- **ABDM consent artefacts treated as DPDP-sufficient** — ABDM's Health Information User (HIU) consent flow covers data sharing within the ABDM ecosystem, but does not satisfy DPDP consent requirements for purposes outside ABDM (e.g., marketing, insurance analytics).
- **Retaining clinical records beyond necessity without legal basis** — Many platforms retain patient data indefinitely "just in case." DPDP S.8 requires erasure once the purpose is served, unless a specific statute (e.g., MCI record retention norms) mandates longer retention.
- **Third-party lab and pharmacy integrations lacking processor agreements** — Sharing patient data with diagnostic labs or pharmacies for order fulfilment without DPDP-compliant data processing agreements exposes the fiduciary to penalty.
- **AI diagnostic models trained on non-anonymised patient data** — Using identifiable patient records to train or fine-tune AI models without explicit consent or proper anonymisation violates both DPDP and ICMR ethics guidelines.
- **Paediatric health data handled identically to adult data** — Hospitals and healthtech apps processing children's health records must obtain verifiable parental consent under S.9 and must not profile minors — often missed in unified patient registration flows.

## Regulator-Specific Timelines

| Event / Obligation | Health Sector / ABDM Timeline | DPDP Timeline | Notes |
|---|---|---|---|
| ABDM consent artefact validity | Defined per consent request (typically 1 hour to 30 days) | Consent valid until withdrawn (S.6) | ABDM consent expiry does not auto-revoke DPDP consent; manage separately |
| Clinical record retention (MCI) | **3 years** minimum (Indian Medical Council regulations) | Erase when purpose served or consent withdrawn (S.8) | Retain for 3 years per MCI; erase thereafter unless another lawful basis exists |
| Breach notification | Report to CERT-In within **6 hours** (CERT-In Directions, Apr 2022) | **72 hours** to DPBI (Rule 7, DPDP Rules 2025) | Health data breaches attract heightened scrutiny; notify both bodies promptly |
| Telemedicine record retention | Retain teleconsultation records for **3 years** (Telemedicine Guidelines 2020) | Erase when purpose served (S.8(7)) | Align with 3-year telemedicine norm; purge after unless ongoing treatment |
| ICMR ethics approval for research | Before data collection (ICMR National Ethical Guidelines) | Consent or anonymisation required (S.17(2), S.6) | Ethics approval does not replace DPDP consent for identifiable data |
| Patient grievance redressal | As per Clinical Establishment Act / state norms | **30 days** (Rule 10, DPDP Rules 2025) | Appoint a single Grievance Officer covering clinical and data complaints |
| ABHA-linked data access request | Real-time via ABDM PHR app | Right to access under S.11; **30 days** response (Rule 10) | Ensure non-ABDM records are also accessible on request |

---
*Based on DPDP Act 2023 (enacted), DPDP Rules 2025 (gazetted November 2025), and ABDM policies.*
