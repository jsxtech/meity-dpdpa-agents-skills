# DPDP Rules Provision Tracker

Maps each pending DPDP Rules provision to the current assumption used in this suite and the files that need updating when the final Rules are notified by the Central Government.

---

## Provision Tracker

| Provision | Current Assumption | Source | Files to Update | Priority |
|---|---|---|---|---|
| Breach notification timeline | 72 hours from awareness | Act §15; Draft Rules | agents/dpdp-breach-notification-agent.md, skills/dpdp-incident-response-skill.md | High |
| Rights request response period | 30 days from receipt | Act §§11–14; Draft Rules | agents/dpdp-rights-request-agent.md, skills/meity-dpdp-privacy-skill.md | High |
| Consent notice format/template | Free-text with required elements per Act §6 | Act §6; Draft Rules | agents/dpdp-consent-management-agent.md, skills/dpdp-consent-manager-skill.md | High |
| SDF designation criteria and thresholds | Based on volume, sensitivity, and risk per Act §10 | Act §10; Draft Rules | agents/dpdp-sdf-compliance-agent.md, DECISION_TREE.md | High |
| Consent Manager registration requirements | Registration with DPBI assumed; interoperability TBD | Act §7; Draft Rules | agents/dpdp-consent-management-agent.md, skills/dpdp-consent-manager-skill.md | High |
| Permissible countries list for cross-border transfers | All countries except those restricted by Central Government notification | Act §16; Draft Rules | agents/dpdp-cross-border-transfer-agent.md, skills/dpdp-international-comparison-skill.md | High |
| DPBI constitution and procedural rules | DPBI established per Act §18; procedures TBD | Act §§18–28; Draft Rules | agents/dpdp-dpbi-complaint-response-agent.md, REGULATORY_CALENDAR.md | High |
| DPO qualifications and appointment requirements | Senior officer with adequate knowledge; specifics TBD | Act §10(2); Draft Rules | agents/dpdp-sdf-compliance-agent.md, skills/dpdp-dpo-skill.md | Medium |
| Data retention periods by category | Purpose-based retention; delete when purpose fulfilled | Act §8(7); Draft Rules | agents/dpdp-policy-document-generator-agent.md, skills/dpdp-data-mapping-inventory-skill.md | Medium |
| Children's age verification methods | Verifiable mechanism required; method TBD | Act §9; Draft Rules | agents/dpdp-children-data-agent.md, skills/dpdp-children-data-skill.md | High |
| Penalty calculation methodology | Up to ₹250 crore per Act §33; calculation criteria TBD | Act §33, Schedule; Draft Rules | agents/dpdp-dpbi-complaint-response-agent.md, skills/dpdp-penalty-enforcement-skill.md | Medium |
| Audit frequency and format requirements | Annual audit assumed for SDFs | Act §10(2); Draft Rules | agents/dpdp-audit-compliance-agent.md, skills/dpdp-audit-checklist-skill.md | Medium |
| DPIA format and submission requirements | DPIA required for SDFs; format TBD | Act §10(2); Draft Rules | agents/dpdp-dpia-agent.md, skills/dpdp-privacy-risk-management-skill.md | Medium |
| Grievance redressal timeline | 30 days assumed | Act §13; Draft Rules | agents/dpdp-rights-request-agent.md, skills/dpdp-dpo-skill.md | Medium |
| Transfer safeguard mechanisms | Contractual clauses and adequacy assumed; specifics TBD | Act §16; Draft Rules | agents/dpdp-cross-border-transfer-agent.md, examples/scenario-cross-border-saas-vendor.md | Medium |
| Exemptions for startups/small entities | No exemptions assumed unless notified | Act §17; Draft Rules | DECISION_TREE.md, agents/dpdp-compliance-roadmap-agent.md | Low |
| Government processing exemptions scope | Exemptions per Act §17(2); scope TBD | Act §17; Draft Rules | agents/dpdp-legitimate-use-agent.md, skills/dpdp-legitimate-use-skill.md | Low |
| Consent Manager interoperability standards | Interoperability required per Act §7; standards TBD | Act §7; Draft Rules | agents/dpdp-consent-management-agent.md, skills/dpdp-consent-manager-skill.md | Medium |
| Algorithm accountability requirements for SDFs | Accountability measures required; specifics TBD | Act §10; Draft Rules | agents/dpdp-sdf-compliance-agent.md, skills/dpdp-ai-ml-ethics-skill.md | Medium |
| Data breach severity classification | Classification by impact and scale assumed; criteria TBD | Act §15; Draft Rules | agents/dpdp-breach-notification-agent.md, skills/dpdp-incident-response-skill.md | High |
| Voluntary undertaking format and acceptance criteria | Concept per Act §32; format and terms TBD | Act §32; Draft Rules | agents/dpdp-dpbi-complaint-response-agent.md, skills/dpdp-penalty-enforcement-skill.md | Medium |
| TDSAT appeal timeline and procedures | Appeal to TDSAT assumed per Act §29; timeline and format TBD | Act §29; Draft Rules | agents/dpdp-dpbi-complaint-response-agent.md, skills/dpdp-penalty-enforcement-skill.md | Medium |
| Blocking access mechanism and criteria | Central Government may direct blocking per Act §§36–37; criteria TBD | Act §§36–37; Draft Rules | agents/dpdp-regulatory-monitoring-agent.md, skills/dpdp-penalty-enforcement-skill.md | Low |
| Data Principal duty enforcement mechanism | ₹10,000 penalty per Act §15 Schedule; enforcement process TBD | Act §15, §33 Schedule; Draft Rules | agents/dpdp-dpbi-complaint-response-agent.md, skills/meity-dpdp-privacy-skill.md | Low |

---

## How to Use This Tracker

1. **When Rules are gazetted**: Download the official notification from the MeITY/Gazette of India website.
2. **Compare each provision**: Check the "Current Assumption" column against the final Rule text.
3. **Update affected files**: Edit every file listed in the "Files to Update" column for that provision.
4. **Bump frontmatter version**: Increment the `version` field in the YAML frontmatter of each updated file.
5. **Add a CHANGELOG entry**: Record the provision, old assumption, new rule text, and affected files in [CHANGELOG.md](CHANGELOG.md).
6. **Re-run validation**: Use the [Audit Checklist Skill](skills/dpdp-audit-checklist-skill.md) to verify updated content is consistent across the suite.
7. **Notify stakeholders**: Flag high-priority changes for immediate review by compliance teams.
