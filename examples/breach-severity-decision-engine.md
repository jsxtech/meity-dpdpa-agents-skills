---
version: "1.4.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Breach Severity & Notification"
type: "decision-engine"
---

# DPDP Breach Severity & Notification Decision Engine

A structured, deterministic decision engine that operationalises the **severity framework prescribed under Rule 7(3) of the DPDP Rules 2025** and the notification obligations under **Section 8(6) of the DPDP Act, 2023**. Given a small set of breach attributes, it produces reproducible outputs: a severity tier, whether and by when to notify the Data Protection Board of India (DPBI), whether a separate CERT-In report is required, and whether affected Data Principals must be notified.

> **Not legal advice.** This engine encodes the statutory decision logic to drive consistent triage. The Data Fiduciary remains responsible for the final determination; consult qualified Indian privacy counsel for binding decisions.

---

## How to Use

1. Collect the **input signals** for the incident (below).
2. Compute the **severity score** and map it to a **severity tier**.
3. Apply the **notification decision table** to derive required actions and timelines.
4. Record the determination using the **decision record template** for the incident file.

This engine is invoked by:
- `agents/dpdp-breach-notification-agent.md` — Workflow 2 (Breach Assessment & Classification)
- `skills/dpdp-incident-response-skill.md` — command `/ir-severity`

---

## Step 1: Input Signals

| Signal | Values | Notes |
|---|---|---|
| `data_categories` | basic / financial / health / biometric / children / special | Highest applicable category governs |
| `volume` | <1k / 1k–100k / 100k–1M / >1M | Number of affected Data Principals |
| `encryption_state` | encrypted_keys_safe / encrypted_keys_exposed / plaintext | Effective protection at time of breach |
| `breach_type` | confidentiality / integrity / availability | May be more than one |
| `harm_likelihood` | none / low / medium / high | Likelihood of harm to Data Principals |
| `children_involved` | yes / no | Any Data Principal under 18 |
| `cross_border` | yes / no | Data left India or foreign processor involved |
| `is_sdf` | yes / no | Fiduciary is a Significant Data Fiduciary |

---

## Step 2: Severity Scoring

Each signal contributes points. Sum the points, then map to a tier.

| Signal | Condition | Points |
|---|---|---|
| Data category | biometric / health / children / special | 3 |
| Data category | financial | 2 |
| Data category | basic | 1 |
| Volume | >1M | 3 |
| Volume | 100k–1M | 2 |
| Volume | 1k–100k | 1 |
| Volume | <1k | 0 |
| Encryption | plaintext | 2 |
| Encryption | encrypted_keys_exposed | 1 |
| Encryption | encrypted_keys_safe | 0 |
| Harm likelihood | high | 3 |
| Harm likelihood | medium | 2 |
| Harm likelihood | low | 1 |
| Harm likelihood | none | 0 |
| Children involved | yes | +2 (modifier) |
| Cross-border | yes | +1 (modifier) |

### Severity Tiers

| Total Score | Severity Tier | Meaning |
|---|---|---|
| 0–3 | **S4 — Low** | Contained, low harm, strong safeguards |
| 4–6 | **S3 — Moderate** | Real but limited exposure |
| 7–9 | **S2 — High** | Significant exposure or sensitive data |
| 10+ | **S1 — Critical** | Large-scale and/or highly sensitive; likely serious harm |

---

## Step 3: Notification Decision Table

| Severity Tier | Notify DPBI (Section 8(6)) | DPBI Timeline | Notify Data Principals | CERT-In 6-hour report |
|---|---|---|---|---|
| **S1 — Critical** | **Yes** | Within **72 hours** of awareness (Rule 7) | **Yes** — without unreasonable delay | **Yes** if a cyber incident under CERT-In Directions 2022 |
| **S2 — High** | **Yes** | Within **72 hours** of awareness (Rule 7) | **Yes** where harm is likely | **Yes** if a reportable cyber incident |
| **S3 — Moderate** | **Yes** | Within **72 hours** of awareness (Rule 7) | **Assess** — notify if harm likely | **Yes** if a reportable cyber incident |
| **S4 — Low** | **Yes** | Within **72 hours** of awareness (Rule 7) | **Usually not** — document rationale | **Yes** if a reportable cyber incident |

> **Key rule — DPBI notification is not discretionary.** Under Section 8(6) read with Rule 7, **every** personal data breach must be reported to the DPBI within 72 hours of the Data Fiduciary becoming aware of it, regardless of severity. Severity governs the **Data Principal** notification decision, the depth of the report, and internal escalation — not whether the DPBI is told.

> **CERT-In is a separate, parallel obligation.** The CERT-In Directions of April 2022 (issued under Section 70B of the IT Act, 2000) require reporting certain cyber incidents within **6 hours** of awareness. This runs independently of, and in addition to, the DPDP/DPBI obligation.

---

## Step 4: Data Principal Notification Test

Notify affected Data Principals where **any** of the following is true:
- Severity tier is **S1** or **S2**, or
- `harm_likelihood` is **medium** or **high**, or
- `data_categories` includes **financial, health, biometric, children, or special**, and data was **plaintext** or **keys exposed**.

Where notification is not made, record the documented rationale in the decision record.

---

## Machine-Readable Rule Set

```yaml
severity_engine:
  version: "1.0"
  legal_basis:
    dpdp_act: "Section 8(6)"
    dpdp_rules: "Rule 7, Rule 7(3)"
    certin: "IT Act 2000 Section 70B + CERT-In Directions 2022"
  scoring:
    data_category:
      biometric: 3
      health: 3
      children: 3
      special: 3
      financial: 2
      basic: 1
    volume:
      ">1M": 3
      "100k-1M": 2
      "1k-100k": 1
      "<1k": 0
    encryption_state:
      plaintext: 2
      encrypted_keys_exposed: 1
      encrypted_keys_safe: 0
    harm_likelihood:
      high: 3
      medium: 2
      low: 1
      none: 0
    modifiers:
      children_involved: 2
      cross_border: 1
  tiers:
    - { name: "S1", label: "Critical", min: 10 }
    - { name: "S2", label: "High", min: 7, max: 9 }
    - { name: "S3", label: "Moderate", min: 4, max: 6 }
    - { name: "S4", label: "Low", min: 0, max: 3 }
  decisions:
    notify_dpbi: always            # every breach, per Section 8(6) + Rule 7
    dpbi_timeline_hours: 72
    notify_data_principals_if:
      - "tier in [S1, S2]"
      - "harm_likelihood in [medium, high]"
      - "sensitive_category and weak_encryption"
    certin_6h_if: "reportable_cyber_incident"
```

---

## Worked Examples

### Example A — Misconfigured storage bucket, 2M user records, plaintext
- data_categories = basic (1), volume = >1M (3), encryption = plaintext (2), harm = high (3), children = no, cross_border = no
- **Score = 1+3+2+3 = 9 → S2 (High)**
- **Actions:** Notify DPBI within 72h; notify Data Principals (harm likely); file CERT-In 6h report (cyber incident).

### Example B — Laptop lost, full-disk encrypted, keys safe, 400 basic records
- data_categories = basic (1), volume = <1k (400 records → 0), encryption = encrypted_keys_safe (0), harm = low (1)
- **Score = 1+0+0+1 = 2 → S4 (Low)**
- **Actions:** Notify DPBI within 72h (still mandatory); Data Principal notice usually not required — document rationale; assess CERT-In applicability.

### Example C — Health records of 50,000 patients incl. minors, keys exposed
- data_categories = health (3), volume = 1k–100k (1), encryption = encrypted_keys_exposed (1), harm = high (3), children = yes (+2)
- **Score = 3+1+1+3+2 = 10 → S1 (Critical)**
- **Actions:** Notify DPBI within 72h; notify Data Principals without unreasonable delay; file CERT-In 6h report; invoke children's-data escalation (Children Data Agent).

---

## Decision Record Template

```
BREACH SEVERITY DECISION RECORD
Incident ID        : INC-XXXX
Assessed by        : [Name, Role]
Assessed at        : [Timestamp]
Inputs             : data_categories=__, volume=__, encryption=__,
                     harm=__, children=__, cross_border=__, is_sdf=__
Severity score     : __ → Tier __ (S_)
DPBI notification  : YES — due by [awareness + 72h = timestamp]
Data Principal     : [YES / NO] — rationale: ____________
CERT-In 6-hour     : [YES / NO] — rationale: ____________
Escalation invoked : [DPO / Legal / Children Agent / CISO]
```

---

## Related

- [Breach Notification Agent](../agents/dpdp-breach-notification-agent.md) — executes the notification workflows
- [Incident Response Skill](../skills/dpdp-incident-response-skill.md) — containment and drafting (`/ir-severity`, `/ir-notify-decision`)
- [Children Data Agent](../agents/dpdp-children-data-agent.md) — invoked when `children_involved = yes`
- [Penalty Exposure Calculator](penalty-exposure-calculator.md) — exposure if obligations are missed

## References

- DPDP Act, 2023 — Section 8(5) (Security Safeguards), Section 8(6) (Breach Notification)
- MeITY DPDP Rules, 2025 — Rule 7 (breach notification), Rule 7(3) (severity framework)
- CERT-In Cyber Incident Reporting Directions, 2022 (issued under IT Act 2000, Section 70B) — 6-hour reporting
- ISO/IEC 27035 — Information Security Incident Management
