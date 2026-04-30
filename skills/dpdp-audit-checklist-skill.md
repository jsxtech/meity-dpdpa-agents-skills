---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Audit Checklist"
type: "skill"
---

# DPDP Audit Checklist Skill

## Skill Identity

**Skill Name:** dpdp-audit-checklist
**Domain:** DPDP Compliance Audit, Assurance, Gap Assessment
**Skill Type:** Audit, Compliance, Assurance
**Applicable To:** Internal Auditors, External Auditors, DPOs, Compliance Officers, Independent Data Auditors (SDF)

---

## Skill Purpose

Provide a comprehensive, domain-by-domain audit checklist for assessing an organisation's compliance with the **Digital Personal Data Protection Act, 2023**. Suitable for internal audits, independent audits (required for SDFs), regulatory inspections, and self-assessments.

---

## Audit Framework Overview

```
DPDP AUDIT FRAMEWORK
12 Domains — 159 Control Points

Domain 1  : Governance & Accountability
Domain 2  : Legal Basis & Consent Management
Domain 3  : Notice & Transparency
Domain 4  : Purpose Limitation & Data Minimisation
Domain 5  : Data Quality & Accuracy
Domain 6  : Data Retention & Deletion
Domain 7  : Security Safeguards
Domain 8  : Data Principal Rights
Domain 9  : Children's Data Protection
Domain 10 : Vendor & Processor Management
Domain 11 : Cross-Border Data Transfers
Domain 12 : Significant Data Fiduciary Obligations
```

---

## Audit Rating Scale

| Rating | Symbol | Meaning |
|---|---|---|
| Compliant | ✅ | Control fully implemented and effective |
| Partially Compliant | 🟡 | Control exists but has gaps; medium risk |
| Non-Compliant | ❌ | Control absent or ineffective; immediate remediation |
| Not Applicable | N/A | Control does not apply to this organisation |
| Not Assessed | — | Outside current audit scope |

---

## Domain 1: Governance & Accountability

```
1.1  DPDP Act obligations are documented and assigned to owners          [ ]
1.2  A Data Protection Officer (DPO) or Privacy Officer is designated   [ ]
1.3  DPO has appropriate qualifications and independence                 [ ]
1.4  DPO contact details are published (website, privacy notice)         [ ]
1.5  DPO has direct reporting line to Board / Senior Management          [ ]
1.6  Privacy governance structure is documented and operational          [ ]
1.7  Board receives regular DPO compliance reports (min. quarterly)      [ ]
1.8  Privacy policy is approved by senior management                     [ ]
1.9  Internal data protection policies are documented and current        [ ]
1.10 Roles and responsibilities for privacy are clearly assigned         [ ]
1.11 Privacy budget and resources are adequate for the programme         [ ]
1.12 Third-party / independent audits conducted (SDFs — mandatory)       [ ]
```

---

## Domain 2: Legal Basis & Consent Management

```
2.1  All processing activities have an identified and documented legal basis  [ ]
2.2  Legal basis is documented in the Records of Processing Activities (RoPA) [ ]
2.3  Consent is obtained before or at time of personal data collection        [ ]
2.4  Consent notices are in clear and plain language                          [ ]
2.5  Consent notices include all mandatory elements (data, purpose, rights)   [ ]
2.6  Consent is obtained through affirmative action (no pre-ticked boxes)     [ ]
2.7  Consent is specific per purpose (not bundled)                            [ ]
2.8  Withdrawal mechanism is as easy to use as consent mechanism              [ ]
2.9  Withdrawal is processed without unreasonable delay                       [ ]
2.10 Consent records are maintained with timestamp, version, and purpose      [ ]
2.11 Re-consent is obtained when purpose changes materially                   [ ]
2.12 Legitimate use cases are documented with appropriate legal basis         [ ]
2.13 No processing occurs after consent withdrawal (except legal obligation)  [ ]
2.14 Dark patterns are absent from consent flows                              [ ]
2.15 Consent audit trails are tamper-evident and retained                     [ ]
```

---

## Domain 3: Notice & Transparency

```
3.1  Privacy notice / policy is publicly accessible                       [ ]
3.2  Privacy notice is in plain language (tested for readability)         [ ]
3.3  Notice discloses: data categories collected                          [ ]
3.4  Notice discloses: purposes of processing                             [ ]
3.5  Notice discloses: legal basis for each processing activity           [ ]
3.6  Notice discloses: third parties / processors with whom data is shared[ ]
3.7  Notice discloses: cross-border transfers and destination countries   [ ]
3.8  Notice discloses: retention periods by data category                 [ ]
3.9  Notice discloses: Data Principal rights and how to exercise them     [ ]
3.10 Notice discloses: grievance redressal mechanism                      [ ]
3.11 Notice discloses: DPO / Grievance Officer contact details            [ ]
3.12 Notice is versioned — prior versions archived with effective dates   [ ]
3.13 Notice is updated when processing activities change materially       [ ]
3.14 Separate notices exist for distinct audiences (employees, customers) [ ]
3.15 Children's privacy notice is age-appropriate (if applicable)         [ ]
```

---

## Domain 4: Purpose Limitation & Data Minimisation

```
4.1  Personal data is used only for the purposes stated in the notice        [ ]
4.2  No secondary use of data without fresh consent or legitimate basis      [ ]
4.3  Technical controls enforce purpose limitation (access by purpose)       [ ]
4.4  Data collection is limited to what is necessary for the stated purpose  [ ]
4.5  Unused data fields have been identified and removed                      [ ]
4.6  Anonymisation / pseudonymisation applied where full PII is not needed   [ ]
4.7  Data minimisation is reviewed when new processing activities are added  [ ]
4.8  Analytics / reporting uses anonymised or aggregated data where possible [ ]
4.9  Marketing data use is limited to consented purposes                     [ ]
4.10 Data sharing with third parties is limited to stated purposes           [ ]
```

---

## Domain 5: Data Quality & Accuracy

```
5.1  Reasonable steps are taken to ensure personal data is accurate        [ ]
5.2  Data validation is applied at point of collection                     [ ]
5.3  Process exists to update data that becomes inaccurate                 [ ]
5.4  Data used for decisions about individuals is verified for accuracy    [ ]
5.5  Correction requests from Data Principals are acted upon promptly      [ ]
5.6  Corrections are propagated to processors and third parties            [ ]
5.7  Data quality is monitored for key datasets                            [ ]
```

---

## Domain 6: Data Retention & Deletion

```
6.1  A Data Retention Schedule is documented and approved                    [ ]
6.2  Retention periods are defined for all personal data categories         [ ]
6.3  Retention periods are linked to legal / contractual / consent basis     [ ]
6.4  Automated deletion is implemented for all systems where possible        [ ]
6.5  Manual deletion procedures exist where automation is not feasible       [ ]
6.6  Deletion mechanisms have been tested and verified                       [ ]
6.7  Backups are included in the retention and deletion schedule             [ ]
6.8  Legal hold process is in place (pauses deletion during disputes)        [ ]
6.9  Deletion is propagated to processors and third parties on termination   [ ]
6.10 Deletion certificates are obtained from processors on offboarding       [ ]
6.11 Deletion is logged with timestamp, data category, and method            [ ]
6.12 Expired data (beyond retention period) has been identified and deleted  [ ]
```

---

## Domain 7: Security Safeguards

```
7.1  Personal data is encrypted at rest (AES-256 or equivalent)              [ ]
7.2  Personal data is encrypted in transit (TLS 1.2+ on all connections)     [ ]
7.3  Encryption key management is separate from data                         [ ]
7.4  Role-Based Access Control (RBAC) is implemented on all data systems     [ ]
7.5  Principle of least privilege is enforced                                [ ]
7.6  Multi-Factor Authentication (MFA) is required for personal data access  [ ]
7.7  Access rights are reviewed quarterly                                    [ ]
7.8  Joiners / movers / leavers process revokes access promptly              [ ]
7.9  All access to personal data is audit logged                             [ ]
7.10 Audit logs are tamper-evident and retained for minimum 1 year           [ ]
7.11 Vulnerability management programme is active (patching SLA defined)     [ ]
7.12 Penetration testing is conducted annually                               [ ]
7.13 Security monitoring / SIEM is in place for personal data systems        [ ]
7.14 Incident response plan is documented and tested                         [ ]
7.15 Breach detection alerts are configured and tested                       [ ]
7.16 DLP controls are in place to prevent unauthorised exfiltration          [ ]
7.17 Physical security controls protect paper / physical personal data       [ ]
7.18 Remote access to personal data systems is secured (VPN / Zero Trust)   [ ]
7.19 Security controls are reviewed after significant changes to systems     [ ]
7.20 Staff are trained on security responsibilities for personal data        [ ]
```

---

## Domain 8: Data Principal Rights

```
8.1  Rights request intake mechanism is operational and accessible          [ ]
8.2  Identity verification procedure is in place before processing requests [ ]
8.3  Rights requests are acknowledged within 48 hours                       [ ]
8.4  Information / access requests are fulfilled within prescribed SLA      [ ]
8.5  Correction requests are fulfilled within prescribed SLA                [ ]
8.6  Erasure requests are fulfilled within prescribed SLA                   [ ]
8.7  Nomination mechanism is in place and operational                       [ ]
8.8  Grievance mechanism is accessible via multiple channels                [ ]
8.9  Grievances are acknowledged within 48 hours                            [ ]
8.10 Grievances are resolved within prescribed SLA                          [ ]
8.11 Data Principals are informed of right to escalate to DPBI              [ ]
8.12 Refusals of rights requests are reasoned and documented                [ ]
8.13 Rights request register is maintained                                  [ ]
8.14 Corrections and erasures are propagated to processors / third parties  [ ]
8.15 Rights fulfilment SLA compliance is monitored and reported             [ ]
```

---

## Domain 9: Children's Data Protection

```
9.1  Age verification mechanism is implemented before data collection       [ ]
9.2  Parental / guardian consent is obtained for users under 18             [ ]
9.3  Parental consent verification is robust (not self-declaration only)    [ ]
9.4  Parental consent records are maintained                                [ ]
9.5  Children's data is flagged in all systems                              [ ]
9.6  Profiling of children is disabled                                      [ ]
9.7  Targeted / behavioural advertising to children is blocked              [ ]
9.8  Behavioural tracking of children is disabled                           [ ]
9.9  Parental dashboard / controls are available                            [ ]
9.10 Children's privacy notice is published in age-appropriate language     [ ]
9.11 Staff who handle children's data receive enhanced training             [ ]
9.12 Children's data handling is audited separately                         [ ]
```

---

## Domain 10: Vendor & Processor Management

```
10.1  All third-party processors are identified in a Processor Register     [ ]
10.2  Risk tiers are assigned to all processors (Tier 1/2/3)                [ ]
10.3  Data Processing Agreements (DPAs) are executed with all processors    [ ]
10.4  DPAs include all DPDP-mandatory clauses                               [ ]
10.5  Sub-processor approval process is in place                            [ ]
10.6  All sub-processors are documented                                      [ ]
10.7  Vendor privacy assessments are conducted before onboarding            [ ]
10.8  Annual audits are conducted for Tier 1 processors                     [ ]
10.9  Bi-annual reviews are conducted for Tier 2 processors                 [ ]
10.10 Corrective actions from vendor audits are tracked to closure          [ ]
10.11 Processor breach notification obligations are defined in DPAs         [ ]
10.12 Data return / deletion on offboarding is confirmed in writing         [ ]
10.13 DPA renewal dates are tracked and renewed before expiry               [ ]
10.14 Processors handling children's data are subject to enhanced review    [ ]
```

---

## Domain 11: Cross-Border Data Transfers

```
11.1  All cross-border data transfers are identified in Transfer Register   [ ]
11.2  Transfer destinations are assessed against permissible country list   [ ]
11.3  Transfers to non-permissible countries are blocked                    [ ]
11.4  DPAs cover cross-border transfer obligations                          [ ]
11.5  End-to-end encryption is applied to all cross-border transfers        [ ]
11.6  Cloud provider data residency settings are configured correctly       [ ]
11.7  Intra-group transfers are governed by intra-group DPAs                [ ]
11.8  Overseas employee / contractor access is assessed as a transfer       [ ]
11.9  Transfer Register is reviewed quarterly                               [ ]
11.10 MeITY permissible country list updates are monitored                  [ ]
```

---

## Domain 12: Significant Data Fiduciary Obligations

```
12.1  SDF designation status is assessed and monitored                      [ ]
12.2  DPO is appointed — based in India, KMP level                          [ ]
12.3  DPO has no conflicts of interest                                      [ ]
12.4  DPO is registered with DPBI                                           [ ]
12.5  Independent Data Auditor is appointed                                 [ ]
12.6  Auditor is independent (no conflict of interest)                      [ ]
12.7  Annual independent audit is completed                                 [ ]
12.8  Audit findings are acted upon and tracked                             [ ]
12.9  Periodic DPIAs are conducted for all high-risk processing activities  [ ]
12.10 DPIA Register is maintained and current                               [ ]
12.11 Algorithm Register is maintained for all AI/ML systems                [ ]
12.12 Automated decision bias audits are conducted annually                 [ ]
12.13 Human review mechanism is in place for significant automated decisions[ ]
12.14 Enhanced children's data safeguards are implemented                   [ ]
12.15 Age verification is robust (beyond self-declaration)                  [ ]
12.16 SDF Annual Compliance Report is submitted to DPBI                     [ ]
12.17 DPBI registration is current                                          [ ]
```

---

## Audit Scoring Template

```
DPDP COMPLIANCE AUDIT SCORE CARD
Organisation: ___________________   Date: ___________________
Auditor: ________________________   Period: _________________

Domain                          | Controls | Compliant | Partial | Non-Compliant | Score
─────────────────────────────────────────────────────────────────────────────────────────
1. Governance & Accountability  |    12    |           |         |               |  /12
2. Legal Basis & Consent        |    15    |           |         |               |  /15
3. Notice & Transparency        |    15    |           |         |               |  /15
4. Purpose & Minimisation       |    10    |           |         |               |  /10
5. Data Quality & Accuracy      |     7    |           |         |               |   /7
6. Retention & Deletion         |    12    |           |         |               |  /12
7. Security Safeguards          |    20    |           |         |               |  /20
8. Data Principal Rights        |    15    |           |         |               |  /15
9. Children's Data              |    12    |           |         |               |  /12
10. Vendor & Processor          |    14    |           |         |               |  /14
11. Cross-Border Transfers      |    10    |           |         |               |  /10
12. SDF Obligations             |    17    |           |         |               |  /17
─────────────────────────────────────────────────────────────────────────────────────────
TOTAL                           |   159    |           |         |               | /159

OVERALL COMPLIANCE SCORE: _____ %

RATING:
  90–100%: Strong compliance
  75–89% : Adequate — targeted improvements needed
  60–74% : Developing — significant gaps to address
  <60%   : Non-compliant — urgent remediation required

CRITICAL NON-COMPLIANCES (must remediate immediately):
1.
2.
3.
```

---

## Related Skills

- `dpdp-privacy-risk-management-skill.md` — Risk-based audit
- `dpdp-dpo-skill.md` — DPO audit role
- `dpdp-data-mapping-inventory-skill.md` — Audit evidence from inventory

---

## Skill Guardrails

- **Never rate** a control as Compliant based on policy alone — verify implementation evidence.
- **Always sample** actual records (consent logs, rights requests, deletion logs) to validate controls.
- **Always flag** Critical non-compliances immediately — do not wait for the final report.
- **Never accept** management representations without corroborating evidence.
- **Always test** technical controls (attempt data deletion, test withdrawal mechanism, verify encryption).

---

## Quick Commands

| Command | Action |
|---|---|
| `/audit-governance` | Run Domain 1 — Governance audit |
| `/audit-consent` | Run Domain 2 — Legal basis and consent audit |
| `/audit-notice` | Run Domain 3 — Notice and transparency audit |
| `/audit-minimisation` | Run Domain 4 — Purpose limitation audit |
| `/audit-retention` | Run Domain 6 — Retention and deletion audit |
| `/audit-security` | Run Domain 7 — Security safeguards audit |
| `/audit-rights` | Run Domain 8 — Data Principal rights audit |
| `/audit-children` | Run Domain 9 — Children's data audit |
| `/audit-vendors` | Run Domain 10 — Vendor management audit |
| `/audit-transfers` | Run Domain 11 — Cross-border transfers audit |
| `/audit-sdf` | Run Domain 12 — SDF obligations audit |
| `/audit-full` | Run full 12-domain audit with scorecard |
| `/audit-scorecard` | Generate compliance scorecard and gap report |

---

## References

- DPDP Act, 2023 — All sections
- MeITY Draft DPDP Rules, 2025
- ISO/IEC 27701 — Privacy Information Management (audit framework)
- ISO 19011 — Guidelines for Auditing Management Systems
- ISO/IEC 29151 — PII Protection Code of Practice
