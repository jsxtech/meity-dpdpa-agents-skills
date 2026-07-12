# Scenario: Data Breach at an E-Commerce Company

## Context

An e-commerce company discovers that a database containing customer names, email addresses, phone numbers, and order history was exposed due to a misconfigured cloud storage bucket. Approximately 500,000 Data Principals are affected.

## Agent Sequence

```
Step 1 → Breach Notification Agent (IMMEDIATE)
         Detect → Assess severity (Critical — 500K affected)
         → Internal escalation: DPO + CISO + Legal + CEO within 1 hour
         → Activate Incident Response Plan

Step 2 → Breach Notification Agent (within 72 hours)
         Prepare and submit DPBI notification:
         nature of breach, data categories, affected count,
         containment measures, proposed remediation

Step 3 → Children's Data Agent (PARALLEL)
         Check: were any affected accounts children's accounts?
         If yes → 24-hour parent notification (faster than standard)
         → Notify NCPCR if serious

Step 4 → Breach Notification Agent (Data Principal notification)
         Notify all 500K affected Data Principals:
         what happened, what data, what to do,
         DPO contact, right to complain to DPBI

Step 5 → Vendor Processor Agent
         Was the cloud provider (processor) responsible?
         → Review DPA breach notification clause
         → Obtain processor incident report
         → Assess DPA adequacy; update if gaps found

Step 6 → DPBI Complaint Response Agent (if complaints filed)
         Prepare case file; compile evidence of containment;
         document mitigation factors for penalty reduction

Step 7 → Audit Compliance Agent
         6-week post-incident review ⚠️ (best practice timeline)
         → Root cause analysis
         → Update security controls
         → Remediation tracking

Step 8 → Compliance Roadmap Agent
         Update roadmap with breach lessons learned;
         add security hardening to next phase
```

## Timeline

| Time | Action | Agent |
|---|---|---|
| T+0 | Breach discovered | Breach Notification |
| T+1hr | CEO/Board notified | Breach Notification |
| T+24hr | Parents notified (if children affected) | Children's Data |
| T+72hr | DPBI notified (72-hour statutory timeline per DPDP Rules 2025, Rule 7) | Breach Notification |
| T+72hr | Data Principals notified (where harm is likely; per DPDP Rules 2025, Rule 7) | Breach Notification |
| T+1wk | Processor incident report obtained | Vendor Processor |
| T+6wk | Post-incident review complete | Audit Compliance |

## Key Risks

| Risk | Penalty Exposure | Mitigation |
|---|---|---|
| Failure to notify DPBI | ₹200 crore | Notify within 72 hours |
| Inadequate security safeguards | ₹250 crore | Document controls; remediate |
| Children's data exposed | ₹200 crore | 24-hour parent notification |
| Delayed Data Principal notification | ₹200 crore | Notify immediately where harm likely |

## Skills to Use

- `dpdp-incident-response-skill.md` — Breach triage and containment playbooks
- `dpdp-penalty-enforcement-skill.md` — Penalty mitigation factors
- `dpdp-privacy-risk-management-skill.md` — Post-breach risk reassessment
- `dpdp-contract-clauses-skill.md` — DPA review for processor liability
