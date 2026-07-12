# Scenario: Bank Designated as Significant Data Fiduciary

## Context

A large private-sector bank has been designated as a Significant Data Fiduciary (SDF) by the Central Government under Section 10 of the DPDP Act. The bank already has basic privacy practices but must now meet heightened SDF obligations.

## Agent Sequence

```
Step 1 → SDF Compliance Agent
         Gap assessment against SDF obligations:
         DPO appointment, independent auditor, DPIA programme,
         algorithmic accountability, annual compliance report

Step 2 → Compliance Roadmap Agent
         SDF-specific roadmap; Phase 1 priorities:
         DPO as Key Managerial Person, auditor empanelment

Step 3 → DPIA Agent
         Mandatory DPIA programme for all high-risk processing:
         credit scoring, fraud detection, AML/KYC, marketing profiling

Step 4 → Anonymisation & Pseudonymisation Agent
         Anonymise data used for analytics and model training;
         re-identification risk testing

Step 5 → Audit Compliance Agent
         Appoint independent auditor; schedule annual DPDP audit;
         establish compliance metrics dashboard

Step 6 → Data Localisation Agent
         RBI payment data localisation; SEBI securities data;
         IRDAI insurance data (if applicable)

Step 7 → Regulatory Monitoring Agent
         Track DPBI orders, MeITY notifications, RBI circulars;
         set up regulatory intelligence feed

Step 8 → Policy Document Generator Agent
         Update Privacy Policy for SDF disclosures;
         generate annual compliance report template
```

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| No DPO appointed | ₹150 crore ⚠️ (maximum per Schedule) | Appoint as KMP promptly (30 days per DPDP Rules 2025, Rule 13) |
| No independent auditor | ₹150 crore ⚠️ (maximum per Schedule) | Empanel auditor promptly (60 days per DPDP Rules 2025, Rule 13(3)) |
| No DPIA programme | ₹150 crore ⚠️ (maximum per Schedule) | Establish programme in Phase 1 |
| Algorithm accountability gap | ₹150 crore ⚠️ (maximum per Schedule) | Algorithm Register + bias audits |

## Skills to Use

- `dpdp-dpo-skill.md` — DPO governance and advisory
- `dpdp-audit-checklist-skill.md` — 159-control audit framework
- `dpdp-sector-specific-skill.md` — Banking/RBI requirements
- `dpdp-ai-ml-ethics-skill.md` — Algorithm accountability
- `dpdp-privacy-programme-management-skill.md` — Programme operating model
