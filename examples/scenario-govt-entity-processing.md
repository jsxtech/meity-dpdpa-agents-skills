# Scenario: State Government Department Digitising Citizen Services

## Context

A state government department is digitising welfare scheme delivery and citizen services. The platform links Aadhaar numbers to beneficiary records, processes caste/income certificates, and disburses subsidies. Processing is under S.7 legitimate use (performance of state function). Approximately 20 million citizens are on the platform. Exemptions under S.17 (state security, public order) may apply to certain datasets.

## Agent Sequence

```
Step 1 → Legitimate Use Agent
         Map all processing activities to S.7(a) — state function.
         Confirm: no consent required for subsidy disbursal,
         certificate issuance, identity verification.
         Flag any processing that falls OUTSIDE legitimate use
         (e.g., citizen satisfaction surveys → needs consent).

Step 2 → Policy Document Generator Agent
         Generate S.5 notice for each service:
         purpose, data categories, retention period, rights.
         Notice is mandatory even when consent is not required.
         Generate: Privacy Policy, Data Retention Schedule,
         Grievance Redressal Procedure.

Step 3 → Audit Compliance Agent
         Verify S.8 security safeguards are in place:
         encryption at rest/transit, access controls, audit logs.
         Assess S.17 exemption applicability — document
         which datasets qualify and which do not.
         Schedule annual compliance audit.
```

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| No S.5 notice despite legitimate use | ₹50 crore ⚠️ | Generate and publish notice for every service |
| Inadequate security safeguards (S.8) | ₹250 crore ⚠️ | Encryption, access controls, audit logging |
| Over-reliance on S.17 exemptions | ₹150 crore ⚠️ | Document exemption basis per dataset; narrow scope |
| Aadhaar data breach (20M records) | ₹250 crore ⚠️ | Data minimisation; tokenise Aadhaar; segment access |
| Processing beyond stated purpose | ₹200 crore ⚠️ | Strict purpose limitation; no secondary use without consent |

## Skills to Use

- `dpdp-sector-specific-skill.md` — Government/public sector requirements
- `dpdp-privacy-by-design-skill.md` — Security architecture for citizen data
- `dpdp-privacy-risk-management-skill.md` — Risk assessment for large-scale state processing
- `dpdp-penalty-enforcement-skill.md` — Penalty exposure for government Data Fiduciaries
