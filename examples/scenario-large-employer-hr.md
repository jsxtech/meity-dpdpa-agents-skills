# Scenario: Large IT Employer — Employee Data Processing at Scale

## Context

An IT services company with 50,000 employees processes personal data across HR records, background verification, performance monitoring, payroll, and CCTV surveillance at office premises. Most employment-related processing falls under S.7(f) legitimate use (employment purpose). However, certain activities — wellness programmes, employee satisfaction surveys, social media monitoring — fall outside legitimate use and require explicit consent. The company uses third-party HRIS, payroll, and background check vendors as Data Processors.

## Agent Sequence

```
Step 1 → Legitimate Use Agent
         Map all employee data processing to legal basis:
         — S.7(f) legitimate use: HR records, payroll, background
           checks, performance reviews, CCTV (workplace safety)
         — Consent required (S.6): wellness programmes, surveys,
           social media monitoring, referral programmes
         Document boundary between legitimate use and consent.

Step 2 → Vendor Processor Agent
         Onboard processors: HRIS provider, payroll vendor,
         background check agency, CCTV managed services.
         Execute DPDP-compliant DPAs with each:
         — Purpose limitation, security obligations (S.8)
         — Breach notification flow, sub-processor controls
         — Data deletion on contract termination

Step 3 → Policy Document Generator Agent
         Generate: Employee Privacy Notice (S.5), HR Data
         Retention Schedule, CCTV Notice, Background Check
         Consent Form, Grievance Redressal Procedure.
         Distribute notice at onboarding and on policy update.

Step 4 → Consent Management Agent
         Design consent flows for non-legitimate-use processing:
         — Wellness programme enrolment
         — Employee satisfaction surveys
         — Social media background checks
         Ensure consent is freely given (no employment penalty
         for refusal), specific, informed, and withdrawable.
```

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| CCTV without notice or purpose limitation | ₹150 crore ⚠️ | Post CCTV notices; limit to safety/security purpose |
| Treating all HR processing as legitimate use | ₹200 crore ⚠️ | Map each activity; obtain consent where S.7(f) does not apply |
| Vendor DPAs missing DPDP terms | ₹150 crore ⚠️ | Audit and update all processor agreements |
| Employee data retained after exit | ₹250 crore ⚠️ | Enforce retention schedule; delete within defined period |
| Coerced consent (employment conditioned) | ₹200 crore ⚠️ | Ensure voluntary opt-in; no adverse action for refusal |

## Skills to Use

- `dpdp-contract-clauses-skill.md` — DPA templates for HRIS/payroll vendors
- `dpdp-privacy-by-design-skill.md` — Employee data architecture and access controls
- `dpdp-privacy-risk-management-skill.md` — Risk assessment for large-scale employee processing
- `dpdp-sector-specific-skill.md` — IT services and employment law intersection
