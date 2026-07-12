# Scenario: Multinational SaaS Company Migrating from GDPR to DPDP

## Context

A multinational SaaS company headquartered in the EU has an established GDPR compliance programme. It is expanding to India and must comply with the DPDP Act for Indian users' personal data. The company needs to map existing GDPR controls to DPDP requirements, identify gaps, and build an India-specific compliance layer. Key gaps: no DPO requirement unless designated as Significant Data Fiduciary (SDF), no mandatory DPIAs unless SDF, consent model differs (no "legitimate interest" ground), and no Standard Contractual Clauses (SCCs) mechanism for cross-border transfers.

## Agent Sequence

```
Step 1 → Compliance Roadmap Agent
         Baseline: map existing GDPR controls to DPDP equivalents.
         Identify gaps:
         — Consent: GDPR legitimate interest ≠ DPDP S.7 legitimate use
         — DPO: not required unless SDF (S.10)
         — DPIA: not required unless SDF (S.10)
         — Cross-border: no SCCs; S.16 govt whitelist model
         — Data Principal rights: similar but not identical
         Build phased India compliance roadmap (3–6 months).

Step 2 → Cross-Border Transfer Agent
         Assess S.16 transfer restrictions:
         — Identify which countries Indian user data flows to
         — Check Central Government whitelist (pending notification)
         — Ensure no transfer to restricted jurisdictions
         — Document transfer mechanisms; no SCC equivalent exists
         — Plan data localisation if whitelist excludes key regions.

Step 3 → Audit Compliance Agent
         Gap audit: GDPR programme vs DPDP requirements.
         Verify: consent notices updated for DPDP (S.5–S.6),
         retention aligned with DPDP (S.8(7)),
         grievance redressal mechanism for Indian users (S.8(10)).
         Document: what GDPR controls carry over, what needs change.
```

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| Relying on GDPR legitimate interest in India | Up to ₹50 crore (S.6 consent — Other provisions) | Re-map to DPDP consent (S.6) or legitimate use (S.7) |
| Transfer to non-whitelisted country | Up to ₹50 crore (S.16 transfer — Other provisions) | Monitor S.16 whitelist; localise if needed |
| GDPR consent notice ≠ DPDP notice | Up to ₹50 crore (S.5 notice — Other provisions) | Generate India-specific S.5 notices |
| No grievance redressal for Indian users | Up to ₹50 crore (S.8(10) — Other provisions) | Appoint grievance officer; publish contact on platform |
| Assuming GDPR DPA = DPDP DPA | Up to ₹50 crore (S.8 obligations — Other provisions) | Review and update processor agreements for DPDP terms |

## Skills to Use

- `dpdp-international-comparison-skill.md` — GDPR-to-DPDP control mapping
- `dpdp-contract-clauses-skill.md` — Update DPAs for DPDP compliance
- `dpdp-sector-specific-skill.md` — SaaS/technology sector requirements
- `dpdp-privacy-risk-management-skill.md` — Gap analysis and risk scoring
