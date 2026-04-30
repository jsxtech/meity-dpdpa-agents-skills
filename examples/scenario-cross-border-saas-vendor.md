# Scenario: Cross-Border SaaS Vendor Onboarding

## Context

An Indian insurance company wants to onboard a US-based SaaS vendor for claims processing. The vendor will process policyholder personal data (names, health records, claim amounts) on US-hosted infrastructure. The insurer is regulated by IRDAI.

## Agent Sequence

```
Step 1 → Vendor Processor Agent
         Vendor risk assessment: Tier 1 (health data, high volume)
         → Privacy questionnaire
         → Security assessment (SOC 2, ISO 27001)
         → Sub-processor inventory

Step 2 → Cross-Border Transfer Agent
         Transfer assessment:
         → Is US on permissible country list? (NOT YET PUBLISHED)
         → Apply precautionary restrictions
         → Document transfer safeguards (DPA, contractual clauses, encryption)

Step 3 → Data Localisation Agent
         IRDAI requirements:
         → Check IRDAI Information Security Guidelines
         → Health data residency requirements
         → Determine if mirroring/localisation needed

Step 4 → DPIA Agent
         High-risk processing: health data, cross-border,
         automated claims processing
         → Risk score and mitigation plan

Step 5 → Policy Document Generator Agent
         Generate DPA with:
         → Processing scope (claims data, health records)
         → 48-hour breach notification
         → Audit rights (annual for Tier 1)
         → Sub-processor restrictions
         → Deletion on termination
         → Cross-border transfer safeguards schedule

Step 6 → Consent Management Agent
         Review consent basis:
         → Is existing policyholder consent sufficient for
            cross-border processing by this vendor?
         → If not, obtain fresh consent with updated notice

Step 7 → Audit Compliance Agent
         Schedule: annual vendor audit (Tier 1)
         → Add to compliance calendar
         → Define audit scope and evidence requirements
```

## Key Decision Points

```
Q: Is the US on the permissible country list?
A: NOT YET PUBLISHED. Apply precautionary approach.

Q: Does IRDAI allow health data processing abroad?
A: Check latest IRDAI circular. May require data mirroring in India.

Q: Can we rely on existing policyholder consent?
A: Only if the consent notice disclosed cross-border processing
   to this specific category of processor. Otherwise, re-consent.
```

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| Transfer to non-permissible country | ₹250 crore | DPA + contractual safeguards + encryption + legal opinion |
| IRDAI data residency violation | IRDAI regulatory action | Mirror data in India; verify with IRDAI |
| Health data breach at vendor | ₹250 crore + ₹200 crore | DPA with 48hr notification; audit rights |
| No DPIA for cross-border health data | ₹150 crore (if SDF) | Complete DPIA before onboarding |

## Skills to Use

- `dpdp-contract-clauses-skill.md` — DPA drafting and negotiation
- `dpdp-sector-specific-skill.md` — IRDAI insurance requirements
- `dpdp-international-comparison-skill.md` — US privacy law comparison
- `dpdp-privacy-risk-management-skill.md` — Vendor risk in risk register
