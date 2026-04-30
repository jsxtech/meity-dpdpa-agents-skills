# Scenario: Startup Launching a Consumer App

## Context

A fintech startup is launching a mobile app that collects user KYC data, processes payments, and uses an ML model for credit scoring. The app may be used by individuals under 18.

## Agent Sequence

```
Step 1 → Compliance Roadmap Agent
         Baseline assessment; Phase 1 compliance floor (3 months)

Step 2 → DPIA Agent
         High-risk processing: credit scoring (automated decisions),
         financial data, potential children's data

Step 3 → Consent Management Agent
         Design consent flows for: KYC collection, credit scoring,
         payment processing, marketing

Step 4 → Children's Data Agent
         Age verification gate; parental consent flow;
         block credit scoring for under-18s (profiling prohibited)

Step 5 → Policy Document Generator Agent
         Generate: Privacy Policy, Consent Notice, Children's Privacy
         Notice, Cookie & Tracking Notice, Data Retention Schedule

Step 6 → Vendor Processor Agent
         Onboard payment gateway, KYC provider, cloud hosting —
         execute DPAs with each

Step 7 → Data Localisation Agent
         RBI payment data must stay in India;
         verify cloud region configuration

Step 8 → Audit Compliance Agent
         Pre-launch privacy design review; schedule first audit
```

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| Credit scoring without DPIA | ₹150 crore ⚠️ (SDF penalty; DPIA recommended but not mandatory for non-SDFs) | Complete DPIA before launch (best practice) |
| Children's data without parental consent | ₹200 crore ⚠️ (maximum per Schedule) | Age gate + parental consent flow |
| Payment data outside India | RBI action + ₹250 crore ⚠️ (maximum per Schedule) | India-only cloud region |
| No privacy policy at launch | ₹50 crore ⚠️ (maximum per Schedule) | Generate via Policy Document Agent |

## Skills to Use

- `dpdp-privacy-by-design-skill.md` — Consent UX, security architecture
- `dpdp-sector-specific-skill.md` — Fintech/RBI requirements
- `dpdp-ai-ml-ethics-skill.md` — Credit scoring model compliance
- `dpdp-children-data-skill.md` — Age verification design
