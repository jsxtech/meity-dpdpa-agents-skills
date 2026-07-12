---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Training & Awareness"
type: "skill"
---

# DPDP Training & Awareness Skill

## Skill Identity

**Skill Name:** dpdp-training-awareness
**Domain:** Privacy Training, Staff Awareness, Culture, Behaviour Change
**Skill Type:** Learning & Development, Compliance, HR
**Applicable To:** DPOs, HR Teams, L&D Teams, Compliance Officers, Department Heads

---

## Skill Purpose

Build a privacy-aware organisational culture by designing, delivering, assessing, and tracking DPDP-compliant training programmes across all roles and levels. Move staff from knowing the rules to living them.

---

## Training Programme Architecture

```
DPDP TRAINING PROGRAMME
│
├── TIER 1 — ALL STAFF (mandatory, annual)
│       DPDP basics, personal data handling, breach reporting,
│       Data Principal rights, what NOT to do
│
├── TIER 2 — ROLE-SPECIFIC (mandatory, annual)
│       ├── IT / Engineering — security, privacy by design
│       ├── Legal / Compliance — full DPDP obligations
│       ├── Customer Support — rights requests, grievance
│       ├── HR — employee data, sensitive data
│       ├── Product / UX — consent design, data minimisation
│       ├── Procurement — vendor assessments, DPAs
│       └── Marketing — consent for comms, profiling rules
│
├── TIER 3 — LEADERSHIP (mandatory, annual)
│       Board, C-Suite, Senior Management —
│       governance, liability, DPBI risk, strategic obligations
│
└── TIER 4 — SPECIALIST (as needed)
        DPO certification, DPIA facilitation,
        breach response drills, sector-specific rules
```

---

## Skill Capabilities

---

### Capability 1: Training Needs Analysis

**Trigger:** "training needs assessment", "what DPDP training do we need", "training gap analysis"

**Steps:**
1. Map all staff roles to DPDP obligations they interact with:

   | Role | DPDP Touchpoints | Training Need |
   |---|---|---|
   | All Staff | Personal data handling, breach reporting | Tier 1 |
   | Software Engineer | Data collection, storage, security, deletion | Tier 2 — Technical |
   | Product Manager | Consent design, purpose definition, DPIA | Tier 2 — Product |
   | Legal Counsel | Full Act obligations, DPAs, DPBI | Tier 2 — Legal |
   | Customer Support | Rights requests, grievance handling | Tier 2 — Support |
   | HR / Recruiter | Employee data, background checks, payroll | Tier 2 — HR |
   | Marketing | Consent for marketing, profiling, DND | Tier 2 — Marketing |
   | Procurement | Vendor assessment, DPA review | Tier 2 — Procurement |
   | Senior Management | Liability, governance, DPBI, SDF risk | Tier 3 |
   | Board / Audit Committee | Oversight, penalty exposure, reputation | Tier 3 |
   | DPO / Privacy Team | Full specialist knowledge | Tier 4 |

2. Assess current knowledge levels (baseline survey).
3. Identify gaps between current knowledge and required competency.
4. Prioritise training by risk — highest-risk roles first.

**Output:** Training Needs Analysis report; role-competency gap matrix.

---

### Capability 2: Training Curriculum Design

**Trigger:** "design DPDP training", "create training curriculum", "build privacy training programme"

**Tier 1 — All Staff Curriculum (30–45 minutes):**

```
MODULE 1: What is Personal Data? (5 mins)
  • Definition under DPDP Act
  • Examples of personal data in our organisation
  • Sensitive personal data — extra care required
  • What is NOT personal data (anonymised data)

MODULE 2: Your Responsibilities (10 mins)
  • Handle personal data only for authorised purposes
  • Minimum necessary — collect and use only what you need
  • Keep personal data confidential — do not share without authorisation
  • Keep personal data secure — lock screens, strong passwords, no USBs
  • Do not send personal data via unsecured channels (personal email, WhatsApp)
  • Work from home — same rules apply

MODULE 3: Consent Basics (5 mins)
  • What is consent and why it matters
  • You cannot process personal data without a valid basis
  • Consent must be given freely — never pressure customers / users
  • People can withdraw consent — respect it

MODULE 4: Data Principal Rights (5 mins)
  • Customers / users have the right to access, correct, delete their data
  • If you receive a rights request → escalate immediately to [team/email]
  • Never ignore or dismiss a rights request

MODULE 5: Recognising and Reporting a Breach (10 mins)
  • What is a personal data breach?
  • Examples: sent email to wrong person, laptop stolen, system hacked
  • What to do IMMEDIATELY: report to [DPO / security team] — do not delay
  • What NOT to do: do not try to handle it yourself; do not cover it up
  • Speed matters — delays make it worse

MODULE 6: Quiz (5 mins)
  • 10 scenario-based questions
  • Minimum pass mark: 80%
```

**Tier 2 — Technical / Engineering Curriculum (60–90 minutes):**

```
MODULE 1: DPDP Engineering Obligations
  • Data minimisation in code — collect only what you need
  • Purpose limitation — technical controls, not just policy
  • Encryption requirements (at rest, in transit)
  • Access control — RBAC, least privilege, MFA
  • Audit logging — who accessed what, when

MODULE 2: Privacy by Design
  • Privacy requirements in user stories
  • Consent gate implementation
  • Automated retention and deletion
  • Anonymisation vs pseudonymisation

MODULE 3: Data Principal Rights API
  • Access, correction, erasure request fulfilment
  • Technical implementation of withdrawal propagation

MODULE 4: Security — Personal Data Focus
  • OWASP top 10 in the context of personal data
  • Injection, XSS, insecure storage
  • Breach detection and incident response integration

MODULE 5: Children's Data Technical Controls
  • Age verification implementation
  • Parental consent flow
  • Disabling profiling / targeting for minors

MODULE 6: Code Review for Privacy
  • Checklist for reviewing PRs touching personal data
  • Data minimisation review
  • Logging personal data — what is acceptable
```

**Tier 3 — Leadership Curriculum (45–60 minutes):**

```
MODULE 1: DPDP Act — The Essentials for Leaders
  • What the Act requires of organisations
  • Your personal liability as a director / KMP
  • The Data Protection Board — powers, penalties

MODULE 2: Penalty Exposure
  • Penalty schedule — up to ₹250 crore per violation
  • Aggravating factors that increase penalties
  • Reputational and commercial consequences

MODULE 3: Board Obligations
  • Governance oversight of privacy programme
  • DPO appointment and independence
  • Quarterly DPO reporting to Board

MODULE 4: DPBI Proceedings
  • How a complaint becomes a DPBI inquiry
  • Organisation's response obligations
  • TDSAT appeals

MODULE 5: Significant Data Fiduciary Risk
  • SDF designation criteria — could we be designated?
  • Additional SDF obligations and costs
  • Proactive readiness
```

**Output:** Tiered training curriculum; module outlines; assessment questions.

---

### Capability 3: Training Delivery

**Trigger:** "deliver DPDP training", "run privacy training session", "launch training programme"

**Delivery Channels:**

| Channel | Best For | Notes |
|---|---|---|
| E-learning (LMS) | All staff — scalable, trackable | Build in SCORM format for LMS integration |
| Live webinar | Role-specific; Q&A sessions | Record for later access |
| In-person workshop | Leadership; specialist teams | Interactive scenarios |
| Microlearning (emails/SMS) | Ongoing awareness nudges | Monthly privacy tip |
| Onboarding module | All new hires | Within first week |
| Lunch & learn | Optional deep dives | Topical sessions on incidents, new rules |
| Phishing simulation (privacy variant) | All staff | Test breach reporting reflex |

**Launch Sequence:**
1. Senior leadership message endorsing the programme
2. Email announcement with learning objectives and deadline
3. LMS course goes live
4. Reminder at 2 weeks (non-completers)
5. Final reminder at 4 weeks
6. Manager escalation for persistent non-completers
7. Completion report to DPO

**Output:** Training delivered; completion tracker active.

---

### Capability 4: Assessment & Competency Testing

**Trigger:** "test privacy knowledge", "training assessment", "competency check DPDP"

**Assessment Design:**

```
SCENARIO-BASED ASSESSMENT EXAMPLES

Tier 1 — All Staff:

Q1: You accidentally send an email containing a customer's home address
    to the wrong recipient. What do you do?
    a) Delete the sent email and hope they don't notice
    b) Immediately report it to the DPO / security team          ← CORRECT
    c) Email the recipient asking them to delete it
    d) Wait and see if anything happens

Q2: A customer calls and asks you to delete all their data from our systems.
    What do you do?
    a) Tell them that's not possible
    b) Delete their data yourself immediately
    c) Escalate to the rights request team / DPO immediately    ← CORRECT
    d) Ask them to send a written letter

Q3: Your colleague asks you for a customer's phone number for a "quick call".
    What do you do?
    a) Share it — they're a colleague
    b) Check if they have an authorised business reason          ← CORRECT
    c) Share it and log it afterwards
    d) Share it only via WhatsApp

Tier 2 — Technical:

Q4: You are adding a new user registration form. Which fields should you include?
    a) Name, DOB, address, phone, email, occupation, income, interests
    b) Only fields required for account creation and the stated service  ← CORRECT
    c) As many fields as possible — more data is better
    d) Same fields as our competitor's form

Q5: A user's data retention period has expired. What should your code do?
    a) Archive it to cold storage indefinitely
    b) Move it to a "deleted users" table
    c) Permanently delete it per the retention schedule          ← CORRECT
    d) Flag it for manual review
```

**Scoring:**
- Pass mark: **80%** for all tiers
- Score below 80% → mandatory retake within 14 days
- Score below 80% on retake → escalate to manager and DPO
- Record scores in Training Register

**Output:** Assessment results; pass/fail records; retraining triggered for failures.

---

### Capability 5: Ongoing Awareness Programme

**Trigger:** "ongoing privacy awareness", "privacy culture", "monthly awareness", "privacy nudges"

**Annual Awareness Calendar:**

```
JANUARY    — New Year, New Habits: Top 5 Data Protection Tips
FEBRUARY   — Know Your Data: What Personal Data Do We Hold?
MARCH      — Consent Matters: How We Get It Right
APRIL      — Data Protection Week: Special events + quiz
MAY        — Breach Awareness: Spot It, Report It Fast
JUNE       — Vendor Alert: Working Safely with Third Parties
JULY       — Children's Data: Extra Care Always
AUGUST     — Data Minimisation: Collect Less, Protect More
SEPTEMBER  — Rights Month: What Customers Can Ask Us
OCTOBER    — Cybersecurity Awareness Month (cross-team)
NOVEMBER   — Cross-Border Data: What Can Travel, What Can't
DECEMBER   — Year in Review: Privacy Wins and Lessons Learned
```

**Awareness Formats:**
- Monthly email with one actionable tip
- Intranet "Privacy Corner" — updated monthly
- Privacy quiz of the month (optional, with prize)
- "Privacy Fail of the Month" — anonymised real incident (internal use only)
- Privacy Champions network — one per department to cascade awareness

**Output:** Annual awareness calendar; content plan; Privacy Champions network.

---

### Capability 6: Privacy Champions Programme

**Trigger:** "privacy champions", "department privacy representatives", "privacy network"

**Steps:**
1. Identify and appoint **1 Privacy Champion per department**:
   - Nominated by department head
   - Interested in privacy (voluntary, not forced)
   - Respected peer — informal influencer
2. Privacy Champion responsibilities:
   - First point of contact for colleagues' privacy questions
   - Cascade DPO communications and training
   - Flag privacy concerns to DPO
   - Promote privacy best practices in daily work
   - Represent department in Privacy Steering Group
3. Privacy Champion onboarding:
   - Enhanced training (Tier 2 + selected Tier 4 modules)
   - Monthly briefing with DPO
   - Access to DPO resources and Q&A
4. Recognition:
   - Privacy Champion certificate
   - Named in internal communications
   - Counted toward performance objectives

**Output:** Champions network established; onboarding complete; monthly briefing calendar.

---

### Capability 7: Training Records & Compliance Reporting

**Trigger:** "training records", "compliance training report", "who hasn't completed training", "audit training"

**Training Register Schema:**

```
TRAINING REGISTER
─────────────────────────────────────────────────────────────────────
Employee ID  | Name | Department | Role | Tier | Module | Completed | Score | Certificate
─────────────────────────────────────────────────────────────────────
EMP001 | [Name] | Engineering | Engineer | T1+T2-Tech | DPDP-2025 | 2025-03-15 | 92% | CERT-001
EMP002 | [Name] | Marketing | Manager | T1+T2-Mktg | DPDP-2025 | 2025-03-18 | 85% | CERT-002
EMP003 | [Name] | IT | Dev | T1+T2-Tech | DPDP-2025 | PENDING | — | —
```

**Compliance Metrics:**

| Metric | Target | Reporting |
|---|---|---|
| All-staff completion rate | 100% within 30 days of launch | Monthly |
| New hire completion | 100% within first week | Monthly |
| Pass rate (first attempt) | >90% | Quarterly |
| Retake completion | 100% within 14 days of fail | Monthly |
| Leadership completion | 100% | Quarterly to Board |
| Privacy Champion training | 100% | Quarterly |

**Output:** Training register; compliance dashboard; Board report.

---

### Capability 8: Breach Reporting Drill

**Trigger:** "breach reporting drill", "incident response exercise", "tabletop breach exercise", "test breach response"

**Drill Scenario Template:**

```
BREACH REPORTING DRILL — SCENARIO [X]

Scenario: An employee receives an email from a colleague asking
them to urgently send a list of 500 customer email addresses
for a "marketing campaign". They send the file. Two hours later,
they realise the email was from an external attacker (phishing).

Participants: All staff (awareness drill) / Incident response team (deep drill)

Objective:
1. Staff correctly identify this as a breach
2. Staff report to DPO / security team within [15 minutes / 1 hour]
3. Incident team activates breach response within prescribed SLA
4. DPBI notification prepared within 72 hours (simulated)

Evaluation Criteria:
□ Was breach identified quickly?
□ Was DPO / security team notified promptly?
□ Was the incident correctly classified?
□ Was breach notification to DPBI prepared accurately?
□ Were affected Data Principals identified?
□ Were containment steps taken promptly?

Debrief: Identify what worked; what needs improvement; update procedures.
```

**Output:** Drill conducted; debrief report; procedure improvements identified.

---

## Related Skills

- `dpdp-dpo-skill.md` — DPO training oversight
- `dpdp-incident-response-skill.md` — Breach drills
- `dpdp-privacy-programme-management-skill.md` — Training as programme KPI

---

## Skill Guardrails

- **Never accept** a tick-box training exercise — test understanding with scenario-based assessments.
- **Always track** completion at individual level — aggregate reports hide non-compliance.
- **Never skip** training for senior management — leadership buy-in drives culture.
- **Always refresh** training content when DPDP Rules are updated or incidents occur.
- **Always link** training records to HR system — non-completion is a performance matter.

---

## Quick Commands

| Command | Action |
|---|---|
| `/training-needs` | Conduct training needs analysis by role |
| `/training-curriculum` | Design tiered training curriculum |
| `/training-deliver` | Plan and launch training programme delivery |
| `/training-assess` | Design scenario-based assessments |
| `/training-awareness` | Build annual awareness calendar |
| `/privacy-champions` | Set up Privacy Champions programme |
| `/training-records` | Generate training compliance report |
| `/breach-drill` | Run breach reporting simulation drill |

---

## References

- DPDP Act, 2023 — Sections 8, 10
- ISO/IEC 29151 — PII Protection (includes training obligations)
- IAPP Privacy Training Framework
- NIST Privacy Framework — Govern function
