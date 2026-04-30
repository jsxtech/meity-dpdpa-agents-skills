---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Children's Data Protection"
type: "skill"
---

# DPDP Children's Data Protection Skill

## Skill Identity

**Skill Name:** dpdp-children-data
**Domain:** Children's Data Protection, Parental Consent, Age Verification
**Skill Type:** Legal, Technical, Compliance, Child Safety
**Applicable To:** DPOs, Product Teams, Legal, Engineering, Customer Support, HR, Child Safety Officers

---

## Skill Purpose

Operationalise the highest level of personal data protection for children under the DPDP Act. Navigate the absolute prohibitions, parental consent requirements, age verification obligations, and lifecycle management of children's personal data — and design products that are safe for children by default.

---

## The Child Protection Imperative

```
CHILDREN UNDER DPDP — ZERO TOLERANCE FRAMEWORK
══════════════════════════════════════════════════════════════
Maximum Penalty     : ₹200 crore
Prohibited Actions  : No exceptions, no business justification
  1. Processing without verifiable parental consent
  2. Profiling
  3. Tracking (location, behaviour, activity)
  4. Behavioural monitoring
  5. Targeted advertising
  6. Any processing detrimental to child's well-being

Default Rule        : When age is uncertain → treat as child
Priority            : Child safety over product convenience
══════════════════════════════════════════════════════════════
```

---

## Knowledge Base

### Who is a Child?
Any person below **18 years of age** under the DPDP Act (Section 9).

### Who Exercises Rights?
A child's Data Principal rights are exercised by the **parent or lawfully appointed guardian**.

### What Triggers Enhanced Protection?
Any product, service, or processing activity that:
- Is directed at children
- Is likely to be accessed by children
- Collects age data revealing a user is under 18
- Is accessible without robust age verification

---

## Skill Capabilities

---

### Capability 1: Children's Risk Assessment

**Trigger:** "does our product reach children", "children's data risk", "DPDP children assessment"

**Steps:**
1. Assess whether any service or product is likely accessed by under-18s:

   ```
   CHILDREN'S EXPOSURE RISK SCREENING
   ─────────────────────────────────────────────────────────────
   □ Is the product/service marketed or designed for children?
   □ Does the product have significant youth appeal?
     (gaming, social, education, entertainment, sports)
   □ Is there any evidence children use the product?
     (support tickets, age data, school email domains)
   □ Can children register without explicit age verification?
   □ Is the product used in schools or by parents for children?
   □ Are there in-app features particularly attractive to children?
     (avatars, rewards, streaks, social features)
   ─────────────────────────────────────────────────────────────
   ANY YES → Apply children's data protections
   ```

2. If children are likely users → mandatory children's compliance programme.
3. Quantify: estimate % of user base likely under 18.
4. Identify all personal data collected from children.
5. Identify all processing activities applied to children's data.

**Output:** Children's exposure risk assessment; compliance programme triggered if needed.

---

### Capability 2: Age Verification Design

**Trigger:** "implement age verification", "age gate design", "how to verify age DPDP"

**Age Verification Methods — Strength Assessment:**

| Method | Strength | DPDP Sufficiency | Notes |
|---|---|---|---|
| Self-declaration (tick box "I am 18+") | Very Low | Insufficient alone | No verification; easily bypassed |
| Date of birth entry | Low | Insufficient alone | Easily falsified |
| Credit/debit card check | Medium | Sufficient for most cases | Excludes children without cards |
| Mobile number + OTP (parent) | Medium | Sufficient with parental flow | Works well for parental consent |
| Aadhaar / DigiLocker verification | High | Sufficient | Government-verified; privacy-sensitive |
| Document upload + liveness check | High | Sufficient | Robust but friction-heavy |
| AI age estimation from photo | Medium | Supplementary only | Use as triage, not sole method |
| School/institutional email block | Low | Supplementary | Does not verify age directly |

**Recommended Implementation:**
```
TIERED AGE VERIFICATION APPROACH
────────────────────────────────────────────────────────────
Tier A — Low-risk services (general content, basic info):
  Step 1: Date of birth collection
  Step 2: If under 18 → parental email/mobile consent flow
  Step 3: Parental OTP confirmation = verifiable parental consent

Tier B — Medium-risk services (social features, purchases):
  Step 1: Date of birth collection
  Step 2: If under 18 → credit/debit card check (adult holder)
     OR → Aadhaar-based parental verification
  Step 3: Parental consent with identity confirmation

Tier C — High-risk services (health, financial, sensitive data):
  Step 1: Document verification + liveness check for age
  Step 2: Parental identity verification (Aadhaar / DigiLocker)
  Step 3: Explicit written parental consent with full disclosure

BORDERLINE CASES (AI-estimated age 14–21):
  → Default to parental consent requirement
  → Do not assume adult — cost of error too high
────────────────────────────────────────────────────────────
```

**Output:** Age verification design; method selection rationale; implementation spec.

---

### Capability 3: Parental Consent Flow Design

**Trigger:** "design parental consent", "parent consent UX", "parental consent flow DPDP"

**Parental Consent Requirements:**
- Parent/guardian identity must be **verified** (not just an email address)
- Consent must be **informed** — full disclosure of what data is collected and how used
- Consent must be **specific** — per purpose, not blanket
- Consent must be **withdrawable** — as easy to withdraw as to give
- Parental consent records must be **maintained** with verification evidence

**Parental Consent Flow Design:**

```
PARENTAL CONSENT UX FLOW
════════════════════════════════════════════════════════
Step 1: Child enters age / DOB → System detects under-18

Step 2: PAUSE screen shown to child:
  "To use [Service], a parent or guardian must give permission.
   We'll send a request to your parent/guardian.
   Please enter your parent/guardian's mobile number or email."

Step 3: System sends parental consent request:
  SMS / Email → "Your child [name] wants to use [Service].
   Please review what we'll collect and how we'll use it,
   then give your permission."

Step 4: Parent opens consent request:
  → Full disclosure notice (plain language)
  → List of data to be collected
  → Each purpose explained simply
  → What is NOT done (no profiling, no advertising)
  → How to withdraw consent later
  → Parental Dashboard explained

Step 5: Parent identity verification:
  → OTP to registered mobile, OR
  → Aadhaar OTP, OR
  → Credit card micro-verification

Step 6: Parent provides consent (affirmative — tick per purpose):
  □ Account creation and basic service delivery
  □ [Other purpose if applicable]
  NOT consented by default:
  ✗ Marketing communications
  ✗ Data sharing with third parties (locked out)

Step 7: Consent confirmed → Child account activated with:
  → All safeguards applied
  → Parental Dashboard live
  → Parent receives activation confirmation

Step 8: Parental Dashboard features:
  → View child's account data
  → View active consents
  → Withdraw consent (granular or full)
  → Request data deletion
  → Set additional restrictions
════════════════════════════════════════════════════════
```

**Output:** Parental consent flow design; UX spec; disclosure notice template.

---

### Capability 4: Children's Technical Controls Checklist

**Trigger:** "technical controls for children", "implement children's safeguards", "children's account controls"

**Mandatory Controls Checklist:**

```
CHILDREN'S ACCOUNT TECHNICAL CONTROLS
═══════════════════════════════════════════════════════════════
PROCESSING RESTRICTIONS
□ Profiling engine          → DISABLED (flag = no_profile)
□ Behavioural tracking      → DISABLED
□ Location tracking         → DISABLED (or per-session parental consent)
□ Targeted advertising      → DISABLED
□ Retargeting pixels        → DISABLED
□ Cross-app tracking (ATT)  → DISABLED
□ Social graph mapping      → DISABLED
□ Interest inference        → DISABLED
□ A/B testing with personal data → DISABLED for children

CONTENT & COMMERCE
□ In-app purchases          → DISABLED or parental gate required
□ Premium/subscription upsell → DISABLED
□ Social sharing features   → DISABLED or parent-approved
□ User-generated content    → Moderated; no public profiles
□ Loot boxes / gambling features → DISABLED
□ Real-money gaming         → DISABLED

COMMUNICATIONS
□ Push notifications (marketing) → DISABLED
□ Email marketing           → DISABLED
□ SMS marketing             → DISABLED
□ Referral / invite features → DISABLED

DATA SHARING
□ Data to third-party advertisers → BLOCKED
□ Data to data brokers      → BLOCKED
□ Analytics with personal data → Anonymised only
□ SDK data collection       → Reviewed; children's flag propagated

DESIGN PATTERNS
□ Dark patterns             → Prohibited (urgency, FOMO, streaks as coercion)
□ Infinite scroll           → Restricted (session limits recommended)
□ Social comparison features → Disabled or restricted
□ Persuasive design         → Age-appropriate review required
═══════════════════════════════════════════════════════════════
```

**Output:** Controls checklist completed; non-compliant items flagged for engineering.

---

### Capability 5: Children's Privacy Notice Drafting

**Trigger:** "write children's privacy notice", "age-appropriate privacy policy", "children's notice DPDP"

**Children's Privacy Notice Template (Plain Language):**

```
CHILDREN'S PRIVACY NOTICE
[Service Name] — For users under 18 and their parents/guardians

HOW WE PROTECT YOUR CHILD'S PRIVACY

We take the privacy of children very seriously. This notice explains
what we do with your child's information and how we keep it safe.

WHAT INFORMATION WE COLLECT
To let your child use [Service], we collect:
• [Item 1, e.g., Username (chosen by your child)]
• [Item 2, e.g., Email address (for account recovery)]
• [Item 3, e.g., Progress and activity within the app]

We do NOT collect more information than we need.

WHY WE COLLECT IT
We use your child's information only to:
• [Purpose 1, e.g., Let your child use the service]
• [Purpose 2, e.g., Keep your child's account safe]
• [Purpose 3, e.g., Help your child pick up where they left off]

WHAT WE WILL NEVER DO WITH YOUR CHILD'S INFORMATION
✗ Show your child personalised advertisements
✗ Track your child's behaviour or build a profile
✗ Share your child's information with advertisers
✗ Monitor your child's activity beyond what is needed for the service
✗ Make your child's information publicly visible

HOW LONG WE KEEP IT
We keep your child's information while they use the service.
If you ask us to delete it, we will do so promptly.
We do not keep information we no longer need.

YOUR RIGHTS AS A PARENT / GUARDIAN
You can ask us to:
• Show you what information we hold about your child
• Correct any information that is wrong
• Delete your child's information
• Stop us using your child's information

CONTACT US
If you have any questions or concerns, please contact:
[DPO / Privacy contact]  |  [Email]  |  [Phone]
```

**Output:** Children's privacy notice drafted; plain language verified; DPO reviewed.

---

### Capability 6: Age-of-Majority Transition

**Trigger:** "child turns 18", "age transition", "convert child account to adult"

**Transition Workflow:**

```
AGE-OF-MAJORITY TRANSITION PROTOCOL
────────────────────────────────────────────────────────────
TRIGGER: System detects stored DOB indicates user is now 18

Day 0 — NOTIFICATION TO USER (now adult):
  Email/In-app: "You've turned 18! Your account is being updated.
  You now manage your own privacy settings. Please review and
  confirm your preferences."

Day 0–7 — REVIEW PERIOD:
  □ Account remains in child-protection mode during review
  □ User presented with full consent options (as adult)
  □ User can enable features previously blocked (with fresh consent)
  □ User sees what data is held and for what purpose

Day 7 — TRANSITION:
  □ If user has confirmed adult consents → apply new settings
  □ If user has not responded → maintain child protections by default
  □ Remove Children's Data Flag (system-wide update)
  □ Archive parental consent records (retain for audit)
  □ Notify parent/guardian that child has reached 18
     ("Parental control has ended. [Name] now manages their own account.")

WHAT REQUIRES FRESH CONSENT FROM ADULT:
  □ Marketing communications → new opt-in required
  □ Personalisation / profiling → new opt-in required
  □ Third-party data sharing → new opt-in required
  □ All features previously disabled → explicit re-enable

WHAT DOES NOT REQUIRE FRESH CONSENT:
  □ Continued basic service delivery (existing service consent continues)
────────────────────────────────────────────────────────────
```

**Output:** Transition workflow implemented; adult consents obtained; parent notified.

---

### Capability 7: Children's Data Audit

**Trigger:** "audit children's data", "verify children's data compliance", "children's data review"

**Audit Checklist:**

```
CHILDREN'S DATA AUDIT CHECKLIST
═══════════════════════════════════════════════════════════════
AGE VERIFICATION
□ Age verification gate is active on all entry points
□ Borderline cases are defaulting to child treatment
□ Self-declaration-only cases identified and escalated

PARENTAL CONSENT RECORDS
□ All accounts with Children's Flag have a valid parental consent record
□ Parental consent records include: parent ID, verification method, timestamp, scope
□ No active child accounts without parental consent
□ Withdrawn consents are correctly reflected (account suspended/deleted)

TECHNICAL CONTROLS (sample test 10 child accounts)
□ Profiling engine: DISABLED for all sampled accounts
□ Advertising targeting: DISABLED
□ Behavioural tracking: DISABLED
□ Parental Dashboard: Accessible and functional

DATA MINIMISATION
□ Only consented data fields are populated for child accounts
□ No additional data collected beyond what was disclosed to parents

THIRD-PARTY SHARING
□ No child account data sent to advertising networks
□ No child account data in analytics exports with personal identifiers
□ SDKs in app reviewed for children's data collection

LIFECYCLE
□ Age-of-majority transitions executed for accounts with DOB ≥ 18 years ago
□ Post-withdrawal data erasure completed within SLA

INCIDENT HISTORY
□ Any incidents involving children's data reviewed and resolved
═══════════════════════════════════════════════════════════════
```

**Output:** Children's data audit report; anomalies escalated; controls verified.

---

### Capability 8: Incident Response — Children's Data

**Trigger:** "breach involving children's data", "children's data incident", "child data exposure"

**Escalation — Automatic P1 Critical:**

```
CHILDREN'S DATA INCIDENT RESPONSE
════════════════════════════════════════════════════════
SEVERITY: P1 CRITICAL — No exceptions

T+0:30   DPO notified
T+1:00   CEO and Board notified
T+1:00   Legal counsel engaged
T+2:00   Containment initiated
T+4:00   Scope assessment complete
T+24:00  Parents / guardians notified directly
           (faster than standard 72-hour window)
T+48:00  DPBI notification filed
T+72:00  Full incident report to Board

SPECIAL OBLIGATIONS:
□ Notify NCPCR if scale or severity warrants
□ Consider police report if child safety risk
□ Dedicated parent support line activated
□ Post-incident: full children's data audit
□ Enhanced controls review

COMMUNICATION TO PARENTS:
□ Direct, personal communication (not mass blast)
□ Plain language — explain what happened and impact on child
□ Specific steps parents should take
□ Dedicated contact for parent queries
□ Genuine apology — not defensive corporate language
════════════════════════════════════════════════════════
```

**Output:** P1 incident managed; parents notified within 24 hours; DPBI notified; NCPCR assessed.

---

## Quick Commands

| Command | Action |
|---|---|
| `/children-risk-assess` | Assess whether product/service reaches children |
| `/children-age-verify` | Design age verification mechanism |
| `/children-consent-flow` | Design parental consent flow |
| `/children-controls` | Implement technical controls checklist |
| `/children-notice` | Draft children's privacy notice |
| `/children-transition` | Manage age-of-majority account transition |
| `/children-audit` | Run children's data compliance audit |
| `/children-incident` | Respond to children's data breach |

---

## Related Skills

- `dpdp-consent-manager-skill.md` — Parental consent
- `dpdp-ai-ml-ethics-skill.md` — AI and children
- `dpdp-privacy-by-design-skill.md` — Child-safe design

---

## Skill Guardrails

- **Never process** a child's data without verified parental consent — zero tolerance.
- **Never allow** profiling, tracking, or targeted advertising directed at children.
- **Always err on the side of treating a user as a child** when age cannot be reliably verified.
- **Always notify** parents within 24 hours of any breach involving children's data.
- **Always escalate** to legal counsel and consider NCPCR notification for serious incidents.

---

## References

- DPDP Act, 2023 — Section 9 (Children's Data)
- MeITY Draft DPDP Rules, 2025
- NCPCR — National Commission for Protection of Child Rights
- UK Age Appropriate Design Code (comparative reference)
- UNICEF Child Online Privacy Guidelines
- ISO/IEC 29101 — Privacy Architecture Framework
