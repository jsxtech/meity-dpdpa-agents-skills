---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Privacy Risk Management"
type: "skill"
---

# DPDP Privacy Risk Management Skill

## Skill Identity

**Skill Name:** dpdp-privacy-risk-management
**Domain:** Privacy Risk Identification, Assessment, Treatment, Monitoring
**Skill Type:** Risk Management, Governance, Compliance
**Applicable To:** DPOs, Risk Managers, CISOs, Compliance Officers, Board / Audit Committees

---

## Skill Purpose

Provide a structured approach to identifying, assessing, treating, and monitoring **privacy risks** across the organisation under the DPDP Act. Integrate privacy risk into the enterprise risk management (ERM) framework and maintain a live Privacy Risk Register.

---

## Privacy Risk Framework

```
PRIVACY RISK = Likelihood of a DPDP violation or privacy harm
               × Severity of impact on Data Principals and the organisation

RISK CATEGORIES
────────────────────────────────────────────────────────────
1. REGULATORY RISK      — DPDP violation leading to DPBI inquiry / penalty
2. OPERATIONAL RISK     — Process failure leading to breach or rights failure
3. TECHNOLOGY RISK      — System failure, misconfiguration, vulnerability
4. THIRD-PARTY RISK     — Processor / vendor breach or non-compliance
5. PEOPLE RISK          — Insider threat, staff error, lack of awareness
6. STRATEGIC RISK       — New business initiative with unassessed privacy impact
7. REPUTATIONAL RISK    — Privacy failure causing public trust damage
8. CHILDREN'S DATA RISK — Elevated risk for processing data of minors
```

---

## Risk Rating Matrix

```
LIKELIHOOD                    IMPACT ON DATA PRINCIPALS / ORGANISATION
            │ Negligible(1) │ Minor(2)  │ Moderate(3) │ Major(4)  │ Critical(5)
────────────┼───────────────┼───────────┼─────────────┼───────────┼────────────
Almost      │      5        │    10     │     15      │    20     │    25
Certain (5) │    MEDIUM     │   HIGH    │   CRITICAL  │ CRITICAL  │  CRITICAL
────────────┼───────────────┼───────────┼─────────────┼───────────┼────────────
Likely (4)  │      4        │     8     │     12      │    16     │    20
            │     LOW       │  MEDIUM   │    HIGH     │  CRITICAL │  CRITICAL
────────────┼───────────────┼───────────┼─────────────┼───────────┼────────────
Possible(3) │      3        │     6     │      9      │    12     │    15
            │     LOW       │  MEDIUM   │    MEDIUM   │   HIGH    │  CRITICAL
────────────┼───────────────┼───────────┼─────────────┼───────────┼────────────
Unlikely(2) │      2        │     4     │      6      │     8     │    10
            │     LOW       │   LOW     │    MEDIUM   │  MEDIUM   │   HIGH
────────────┼───────────────┼───────────┼─────────────┼───────────┼────────────
Rare (1)    │      1        │     2     │      3      │     4     │     5
            │     LOW       │   LOW     │    LOW      │   LOW     │  MEDIUM
────────────┴───────────────┴───────────┴─────────────┴───────────┴────────────

CRITICAL (15–25): Immediate escalation; treatment within 72 hours
HIGH     (8–12) : Escalate to DPO; treatment within 30 days
MEDIUM   (4–6)  : Treatment within 90 days
LOW      (1–3)  : Monitor; treat within 6 months
```

---

## Skill Capabilities

---

### Capability 1: Privacy Risk Identification

**Trigger:** "identify privacy risks", "what are our DPDP risks", "privacy risk discovery"

**Risk Identification Sources:**

```
INTERNAL SOURCES
□ Records of Processing Activities (RoPA) review
□ Data flow mapping — each transfer point is a risk
□ Prior audit findings
□ Near-miss incidents
□ Staff-reported concerns
□ System change log — new systems = new risks
□ Vendor / processor list — each processor = a third-party risk

EXTERNAL SOURCES
□ DPBI orders against other organisations (sector benchmarking)
□ Data breach news — what are others getting wrong?
□ MeITY guidance and consultations
□ CERT-In threat intelligence
□ OWASP / security advisories
□ Regulatory changes (new DPDP Rules, sector regulations)
```

**Risk Identification Workshops:**
1. Facilitate risk identification workshops by domain:
   - Workshop 1: Data collection and consent risks
   - Workshop 2: Data storage and security risks
   - Workshop 3: Data sharing and vendor risks
   - Workshop 4: Data Principal rights risks
   - Workshop 5: Regulatory and governance risks
2. Use scenario prompts: "What could go wrong when...?"
3. Document all identified risks — no filtering at identification stage.
4. Categorise into the 8 risk categories.

**Output:** Raw risk log; categorised risk inventory.

---

### Capability 2: Privacy Risk Assessment

**Trigger:** "assess privacy risk", "rate our DPDP risks", "risk scoring"

**Steps:**
1. For each identified risk, assess:

   **Likelihood (1–5):**
   - 5 Almost Certain: Has happened recently / happening now
   - 4 Likely: Happened in the past year; expected to occur
   - 3 Possible: Could occur; happened in similar organisations
   - 2 Unlikely: Could occur but no recent evidence
   - 1 Rare: Only under exceptional circumstances

   **Impact on Data Principals (1–5):**
   - 5 Critical: Severe financial loss, physical harm, identity theft
   - 4 Major: Significant financial / reputational harm, discrimination
   - 3 Moderate: Moderate inconvenience, limited financial impact
   - 2 Minor: Minimal impact; easily remediated
   - 1 Negligible: No meaningful impact on Data Principals

   **Impact on Organisation (1–5):**
   - 5 Critical: DPBI penalty > ₹100 crore; regulatory action; severe reputational damage
   - 4 Major: DPBI investigation; penalty ₹10–100 crore; significant reputational harm
   - 3 Moderate: DPBI complaint; penalty < ₹10 crore; moderate reputational damage
   - 2 Minor: Regulatory correspondence; minor reputational impact
   - 1 Negligible: Internal issue; minimal external impact

2. Calculate composite impact = max(Data Principal impact, Org impact).
3. Calculate Risk Score = Likelihood × Impact.
4. Assign Risk Rating (Critical / High / Medium / Low).
5. Identify existing controls and their effectiveness:
   - Strong: Reduces likelihood/impact by 2 levels
   - Adequate: Reduces by 1 level
   - Weak: Minimal reduction
   - Absent: No reduction

**Output:** Risk assessment with scores; control effectiveness rating.

---

### Capability 3: Privacy Risk Register

**Trigger:** "build privacy risk register", "risk register DPDP", "maintain risk register"

**Privacy Risk Register Schema:**

```
PRIVACY RISK REGISTER
═══════════════════════════════════════════════════════════════════════════
Risk ID        : PR-001
Risk Category  : Technology Risk
Risk Title     : Unencrypted personal data in legacy database
Description    : [System X] stores customer records without encryption at rest.
                 Successful DB compromise would expose all customer PII.

ASSESSMENT (GROSS / INHERENT RISK — before controls)
Likelihood     : 3 (Possible)
DP Impact      : 4 (Major — financial data exposed)
Org Impact     : 5 (Critical — DPBI penalty, breach notification)
Risk Score     : 15 → CRITICAL

EXISTING CONTROLS
Control 1      : Network segmentation (limits external access) — ADEQUATE
Control 2      : Access logging (detects but doesn't prevent) — ADEQUATE
Control Effectiveness: Reduces likelihood by 1 level

ASSESSMENT (NET / RESIDUAL RISK — after controls)
Likelihood     : 2 (Unlikely)
Impact         : 5 (unchanged)
Residual Score : 10 → HIGH

TREATMENT
Treatment Plan : Migrate [System X] to encrypted database by Q3 2025
Owner          : CTO
Target Date    : 30 September 2025
Status         : In Progress

MONITORING
Review Frequency: Monthly (HIGH risk)
Last Reviewed  : 2025-03-01
Next Review    : 2025-04-01

DPBI PENALTY EXPOSURE
Max Penalty    : ₹250 crore (failure of security safeguards)
Exposure Note  : [Legacy system — documented treatment plan]
═══════════════════════════════════════════════════════════════════════════
```

**Output:** Populated Privacy Risk Register; export to Board / DPO report.

---

### Capability 4: Risk Treatment Planning

**Trigger:** "treat privacy risk", "risk mitigation plan", "reduce DPDP risk"

**Treatment Options:**

```
RISK TREATMENT STRATEGIES
──────────────────────────────────────────────────────────────
AVOID    : Stop the processing activity that creates the risk
           Best for: High-risk processing with no business necessity

MITIGATE : Implement controls to reduce likelihood or impact
           Best for: Necessary processing; risk can be reduced to acceptable level

TRANSFER : Transfer risk to third party (insurance, contractual indemnity)
           Note: DPDP liability cannot be fully transferred — Data Fiduciary remains responsible
           Best for: Residual financial risk beyond what controls address

ACCEPT   : Accept the risk with Board approval
           Best for: Low residual risk after mitigation; cost of control > risk value
           Requires: Documented Board acceptance; DPO review
──────────────────────────────────────────────────────────────
```

**Risk Treatment Plan Template:**

```
RISK TREATMENT PLAN
Risk ID     : PR-001
Risk Title  : [Title]
Rating      : [Critical / High / Medium / Low]

TREATMENT STRATEGY: [Avoid / Mitigate / Transfer / Accept]

MITIGATION ACTIONS:
Action 1   : [Specific action]
  Owner    : [Name / Team]
  Deadline : [Date]
  Resources: [Budget / Systems required]
  KPI      : [How will we know it's done?]

Action 2   : [Specific action]
  Owner    : [Name / Team]
  Deadline : [Date]

TARGET RESIDUAL RISK POST-TREATMENT:
  Likelihood  : [target]
  Impact      : [target]
  Target Score: [target rating]

ESCALATION:
  Escalate to DPO if not on track by: [Date]
  Escalate to Board if Critical unresolved by: [Date]
```

**Output:** Risk treatment plans for all Critical and High risks; owner-assigned actions.

---

### Capability 5: Risk Monitoring & Reporting

**Trigger:** "monitor privacy risks", "risk reporting", "privacy risk dashboard", "KRI monitoring"

**Key Risk Indicators (KRIs):**

| KRI | Target | Trigger for Review |
|---|---|---|
| Open Critical privacy risks | 0 | Any Critical risk open > 72 hours |
| Open High risks unresolved > 30 days | 0 | Any High risk overdue |
| Rights request SLA breach rate | < 2% | > 5% in any month |
| Consent withdrawal processing delay | < 24 hours | Any delay > 48 hours |
| Processor audits overdue | 0 | Any Tier 1 audit > 12 months |
| Security patch latency (Critical CVEs) | < 48 hours | Any Critical patch > 48 hours |
| Staff training completion rate | 100% | Any drop below 90% |
| Breach detection to notification time | < 72 hours | Any breach exceeding timeline |
| DPIA completion for new high-risk processing | 100% | Any launch without DPIA |
| Consent audit anomaly rate | < 1% | > 2% anomalies in sample |

**Reporting Cadence:**

| Audience | Frequency | Content |
|---|---|---|
| DPO | Weekly | Open risks, KRI status, new risks identified |
| Senior Management | Monthly | Risk register summary, treatment progress |
| Board / Audit Committee | Quarterly | Top risks, KRIs, penalty exposure, trends |
| Independent Auditor (SDF) | Annual | Full risk register, treatment history |

**Output:** KRI dashboard; risk reporting pack; Board privacy risk report.

---

### Capability 6: Emerging Risk Assessment

**Trigger:** "new privacy risk", "emerging risk", "assess risk of new initiative", "privacy risk of new technology"

**Emerging Risk Triggers:**

```
TRIGGER                          ACTION
─────────────────────────────────────────────────────────
New product / feature launch  → Privacy risk pre-assessment + DPIA
New AI/ML system              → AI DPIA; bias audit; algorithmic risk
New third-party vendor        → Vendor privacy risk assessment
New geography (expansion)     → Cross-border transfer risk assessment
New regulation (DPDP Rules)   → Regulatory change impact assessment
Sector regulatory change      → Dual compliance re-assessment
Major system change           → Security risk re-assessment
Staff restructuring           → Access control risk review
M&A activity                  → Acquired entity data risk assessment
Public data breach at peer    → Assess same vulnerability in own systems
```

**Emerging Risk Fast Assessment (30 minutes):**
1. Describe the change / new initiative.
2. What personal data is involved?
3. What new risks does this introduce?
4. Do existing controls cover these risks?
5. What additional controls are needed?
6. Is a full DPIA required?
7. Risk rating of identified emerging risks?
8. Escalate to DPO immediately if Critical.

**Output:** Emerging risk assessment; DPIA triggered if needed; new risks added to Register.

---

### Capability 7: Privacy Risk Appetite Statement

**Trigger:** "risk appetite for privacy", "how much DPDP risk can we accept", "risk tolerance statement"

**Privacy Risk Appetite Framework:**

```
PRIVACY RISK APPETITE STATEMENT
[Organisation Name] — Approved by: Board | Date: ___________

ZERO TOLERANCE (will not accept under any circumstances):
  • Processing children's data without verifiable parental consent
  • Profiling or targeting children
  • Transferring personal data to non-permissible countries
  • Withholding or concealing a personal data breach
  • Ignoring or dismissing Data Principal rights requests
  • Processing personal data without any lawful basis

LOW TOLERANCE (accept only with Board approval and robust controls):
  • Processing sensitive personal data (health, financial, biometric)
  • Fully automated decisions without human review
  • Large-scale processing triggering SDF designation risk
  • Engaging processors with inadequate data protection standards

MODERATE TOLERANCE (accept with DPO approval and documented controls):
  • Processing personal data of large populations (>100,000 individuals)
  • Cross-border transfers to permissible countries
  • New AI/ML systems processing personal data (post-DPIA approval)
  • Processing personal data via third-party processors (post-DPA execution)

STANDARD TOLERANCE (manage within normal operations):
  • Processing personal data for core business purposes with valid consent
  • Minor technical gaps with documented and time-bound remediation plans
  • Low-risk processing activities with adequate controls
```

**Output:** Board-approved Privacy Risk Appetite Statement; embedded in ERM framework.

---

## Privacy Risk Register — Summary Dashboard

```
PRIVACY RISK SUMMARY DASHBOARD
As at: [Date]

RISK DISTRIBUTION
  Critical : [n] risks
  High     : [n] risks
  Medium   : [n] risks
  Low      : [n] risks

TOP 5 RISKS BY RESIDUAL SCORE
  1. [Risk Title] — PR-XXX — Score: XX — Owner: [Name] — Due: [Date]
  2. [Risk Title] — PR-XXX — Score: XX — Owner: [Name] — Due: [Date]
  3. [Risk Title] — PR-XXX — Score: XX — Owner: [Name] — Due: [Date]
  4. [Risk Title] — PR-XXX — Score: XX — Owner: [Name] — Due: [Date]
  5. [Risk Title] — PR-XXX — Score: XX — Owner: [Name] — Due: [Date]

TREATMENT STATUS
  On Track   : [n] risks
  At Risk    : [n] risks (treatment delayed)
  Overdue    : [n] risks (ESCALATE)

KRI ALERTS THIS PERIOD
  [KRI name] : [Status] — [Action required]

PENALTY EXPOSURE ESTIMATE
  Worst case : ₹[X] crore (if all Critical/High risks materialise)
  Likely case: ₹[X] crore (probability-weighted)
```

---

## Related Skills

- `dpdp-audit-checklist-skill.md` — Risk-based audit
- `dpdp-penalty-enforcement-skill.md` — Penalty as risk
- `dpdp-incident-response-skill.md` — Incident risk

---

## Skill Guardrails

- **Never accept** Critical privacy risks without Board sign-off and a time-bound treatment plan.
- **Always escalate** new Critical risks to DPO within 24 hours of identification.
- **Always distinguish** inherent risk (before controls) from residual risk (after controls).
- **Never use** risk acceptance as a substitute for unavailable controls.
- **Always link** Privacy Risk Register to DPIA Register and Breach Register.

---

## Quick Commands

| Command | Action |
|---|---|
| `/risk-identify` | Facilitate privacy risk identification |
| `/risk-assess` | Score and rate identified risks |
| `/risk-register` | Build or update Privacy Risk Register |
| `/risk-treat` | Create risk treatment plans |
| `/risk-monitor` | Set up KRIs and risk monitoring |
| `/risk-emerging` | Fast-assess emerging / new privacy risk |
| `/risk-appetite` | Draft Privacy Risk Appetite Statement |
| `/risk-dashboard` | Generate Privacy Risk Summary Dashboard |

---

## References

- DPDP Act, 2023 — Sections 8–10
- MeITY DPDP Rules, 2025 (Notified)
- ISO 31000 — Risk Management Guidelines
- ISO/IEC 27005 — Information Security Risk Management
- ISO/IEC 29134 — Privacy Impact Assessment Guidelines
- NIST Privacy Framework — Identify-P Function
