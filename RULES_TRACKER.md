# DPDP Rules 2025 — Provision Tracker & Reconciliation Log

Tracks each DPDP Rules 2025 provision against the assumptions originally used in this suite. The Rules were **notified on 13 November 2025** and **published in the Official Gazette on 14 November 2025**. This suite was reconciled against the gazetted text in v1.3.2 (July 2026).

---

## Status Key

| Symbol | Meaning |
|---|---|
| ✅ | Reconciled — assumption confirmed or corrected against gazetted Rules |
| ⏳ | Pending subordinate notification — Rules delegate to further Central Government notification |
| 🔄 | Partially reconciled — Rules provide framework but specifics await notification |

---

## Provision Tracker

| # | Provision | Original Assumption | Rules 2025 Position | Status | Files Updated |
|---|---|---|---|---|---|
| 1 | Breach notification timeline | 72 hours from awareness | **72 hours confirmed** (Rule 7) | ✅ | agents/dpdp-breach-notification-agent.md, skills/dpdp-incident-response-skill.md |
| 2 | Rights request response period | 30 days from receipt | **30 days confirmed** (Rule 10) | ✅ | agents/dpdp-rights-request-agent.md, skills/meity-dpdp-privacy-skill.md |
| 3 | Consent notice format | Free-text with required elements | **Prescribed format** in Schedule II of Rules | ✅ | agents/dpdp-consent-management-agent.md, skills/dpdp-consent-manager-skill.md |
| 4 | SDF designation criteria | Volume, sensitivity, and risk (Act §10) | **Criteria specified** (Rule 12): revenue, data volume, sensitivity | ✅ | agents/dpdp-sdf-compliance-agent.md, DECISION_TREE.md |
| 5 | Consent Manager registration | Registration with DPBI; interoperability TBD | **Registration framework specified** (Rule 4); interoperability standards prescribed | ✅ | agents/dpdp-consent-management-agent.md, skills/dpdp-consent-manager-skill.md |
| 6 | Permissible countries list | All except those restricted | **Delegated to Central Government notification** (Rule 14) — list not yet published | ⏳ | agents/dpdp-cross-border-transfer-agent.md, agents/dpdp-data-localisation-agent.md |
| 7 | DPBI constitution | DPBI established under Act §18 | **DPBI constituted** (November 2025); procedural rules published | ✅ | agents/dpdp-dpbi-complaint-response-agent.md, REGULATORY_CALENDAR.md |
| 8 | DPO qualifications | Senior officer with adequate knowledge | **KMP or equivalent; based in India** (Rule 13) | ✅ | agents/dpdp-sdf-compliance-agent.md, skills/dpdp-dpo-skill.md |
| 9 | Data retention periods | Purpose-based; delete when purpose fulfilled | **Purpose-based retention confirmed** (Rule 8); no sector-specific periods prescribed | ✅ | agents/dpdp-policy-document-generator-agent.md, skills/dpdp-data-mapping-inventory-skill.md |
| 10 | Children's age verification | Verifiable mechanism required; method TBD | **Multiple methods prescribed** (Rule 11): parent email, ID verification, token-based | ✅ | agents/dpdp-children-data-agent.md, skills/dpdp-children-data-skill.md |
| 11 | Penalty calculation methodology | Up to ₹250 crore per Schedule | **Factors specified** (Rule 22): nature, duration, type of data, mitigation, repetition | ✅ | agents/dpdp-dpbi-complaint-response-agent.md, skills/dpdp-penalty-enforcement-skill.md |
| 12 | Audit frequency (SDF) | Annual audit assumed | **Annual audit confirmed** for SDFs (Rule 13(3)) | ✅ | agents/dpdp-audit-compliance-agent.md, skills/dpdp-audit-checklist-skill.md |
| 13 | DPIA format (SDF) | DPIA required; format TBD | **Prescribed DPIA format** in Schedule III of Rules | ✅ | agents/dpdp-dpia-agent.md, skills/dpdp-privacy-risk-management-skill.md |
| 14 | Grievance redressal timeline | 30 days assumed | **30 days confirmed** (Rule 10(2)) | ✅ | agents/dpdp-rights-request-agent.md, skills/dpdp-dpo-skill.md |
| 15 | Transfer safeguard mechanisms | Contractual clauses and adequacy assumed | **Contractual safeguards + technical measures** required (Rule 14) | 🔄 | agents/dpdp-cross-border-transfer-agent.md, examples/scenario-cross-border-saas-vendor.md |
| 16 | Startup/small entity exemptions | No exemptions unless notified | **Delegated to Central Government notification** (Rule 23) — no exemptions notified yet | ⏳ | DECISION_TREE.md, agents/dpdp-compliance-roadmap-agent.md |
| 17 | Government processing exemptions scope | Per Act §17(2); scope TBD | **Scope parameters defined** (Rule 15): security of state, public order, research | ✅ | agents/dpdp-legitimate-use-agent.md, skills/dpdp-legitimate-use-skill.md |
| 18 | Consent Manager interoperability | Required per Act §7; standards TBD | **Technical standards specified** (Rule 4(4)); API-based interoperability | 🔄 | agents/dpdp-consent-management-agent.md, skills/dpdp-consent-manager-skill.md |
| 19 | Algorithm accountability (SDF) | Accountability measures required; specifics TBD | **Periodic algorithmic audit required** (Rule 13(5)) | ✅ | agents/dpdp-sdf-compliance-agent.md, skills/dpdp-ai-ml-ethics-skill.md |
| 20 | Data breach severity classification | Classification by impact and scale | **Severity framework prescribed** (Rule 7(3)): categories, thresholds, escalation criteria | ✅ | agents/dpdp-breach-notification-agent.md, skills/dpdp-incident-response-skill.md |
| 21 | Voluntary undertaking format | Concept per Act §32; format TBD | **Format and acceptance criteria specified** (Rule 20) | ✅ | agents/dpdp-dpbi-complaint-response-agent.md, skills/dpdp-penalty-enforcement-skill.md |
| 22 | TDSAT appeal timeline | Appeal to TDSAT per Act §29; timeline TBD | **60 days from DPBI order** (Rule 21) | ✅ | agents/dpdp-dpbi-complaint-response-agent.md, skills/dpdp-penalty-enforcement-skill.md |
| 23 | Blocking access mechanism | Per Act §§36–37; criteria TBD | **Procedure specified** (Rule 24): notice to DF, opportunity to respond, Central Govt direction | ✅ | agents/dpdp-regulatory-monitoring-agent.md, skills/dpdp-penalty-enforcement-skill.md |
| 24 | Data Principal duty enforcement | ₹10,000 penalty; enforcement process TBD | **Complaint-based enforcement** via DPBI (Rule 19); frivolous complaint penalty mechanism defined | ✅ | agents/dpdp-dpbi-complaint-response-agent.md, skills/meity-dpdp-privacy-skill.md |

---

## Reconciliation Summary

| Status | Count | Percentage |
|---|---|---|
| ✅ Reconciled | 20 | 83% |
| 🔄 Partially reconciled | 2 | 8% |
| ⏳ Pending subordinate notification | 2 | 8% |

**Pending items** (awaiting Central Government notification):
- **Permissible countries list** (Rule 14) — cross-border transfer whitelist not yet published
- **Startup/small entity exemptions** (Rule 23) — no exemptions notified

These items are tracked in [REGULATORY_CALENDAR.md](REGULATORY_CALENDAR.md).

---

## How to Use This Tracker

1. **For pending items (⏳)**: Monitor the Official Gazette and MeITY website for notifications.
2. **When a new notification is published**: Compare against the "Rules 2025 Position" column.
3. **Update affected files**: Edit every file listed in the "Files Updated" column.
4. **Bump version**: Increment `version` in YAML frontmatter of each updated file.
5. **Add CHANGELOG entry**: Record the notification, new position, and affected files.
6. **Re-run validation**: Use the [Audit Checklist Skill](skills/dpdp-audit-checklist-skill.md) to verify consistency.
