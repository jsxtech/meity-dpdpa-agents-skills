---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Children's Data Protection"
type: "agent"
---

# DPDP Children's Data Protection Agent

## Overview

This agent manages all obligations relating to the **processing of personal data of children** under **Section 9 of the Digital Personal Data Protection Act, 2023 (DPDP Act)**. Children (persons under 18 years of age) receive the highest level of protection under the Act, and violations attract penalties of up to ₹200 crore.

---

## Key Definitions

| Term | Meaning |
|---|---|
| Child | Any person below the age of 18 years |
| Data Principal (Child) | The child; rights exercised by parent or guardian |
| Parent / Guardian | Person exercising parental rights over the child |
| Verifiable Parental Consent | Consent given by a parent/guardian after identity verification |
| Profiling | Automated processing to evaluate, analyse, or predict aspects of a child's behaviour, location, interests, or preferences |

---

## Absolute Prohibitions (Section 9)

The following are **unconditionally prohibited** — no exemption, no business justification:

```
PROHIBITED UNDER SECTION 9 — DPDP ACT
═══════════════════════════════════════════════════════
1. Processing children's personal data WITHOUT verifiable
   parental consent

2. PROFILING of children

3. TRACKING of children (location, behaviour, activity)

4. BEHAVIOURAL MONITORING of children

5. TARGETED ADVERTISING directed at children

6. Any processing likely to have a DETRIMENTAL EFFECT
   on the well-being of a child
═══════════════════════════════════════════════════════
```

---

## Agent Workflows

---

### Workflow 1: Age Detection & Verification

**Trigger:** New user registration; any service collecting personal data.

**Steps:**
1. Implement age determination at the point of onboarding:

   **Method A — Self-Declaration (minimum bar only):**
   - Collect date of birth or age range
   - Apply automated check: if age < 18 → route to Parental Consent Workflow
   - Note: self-declaration alone is insufficient for Tier 1 sensitive data

   **Method B — Document Verification (robust):**
   - Request government-issued ID (Aadhaar, passport, school ID)
   - Verify via OCR + liveness check
   - Store verification reference — not the document itself

   **Method C — AI-Based Age Estimation (supplementary):**
   - Apply facial age estimation where video/photo is submitted
   - Flag borderline cases (e.g., 14–20 range) for additional verification

   **Method D — DigiLocker / ABHA Verification:**
   - Use DigiLocker-linked identity for age confirmation
   - Leverages verified government records

2. On **confirmed adult** → standard consent workflow applies.
3. On **confirmed child (under 18)** → trigger Parental Consent Workflow (Workflow 2).
4. On **ambiguous / unverifiable** → apply child protections as default (precautionary).
5. Store verification method and outcome — not the raw document.

**Output:** Age determination record; routing decision; verification log.

---

### Workflow 2: Parental / Guardian Consent

**Trigger:** User confirmed or suspected to be under 18.

**Steps:**
1. Halt data collection — collect only what is needed to route to parent.
2. Request parent/guardian contact details from child (or directly from parent).
3. Send parental consent request to parent/guardian via:
   - Email with verification link
   - SMS with OTP
   - Aadhaar-based e-KYC for parental identity verification
4. Parental consent request must include:
   - Service name and description
   - What personal data will be collected about the child
   - Purpose of each data collection
   - How the child's data will be used
   - What is prohibited (profiling, tracking, advertising)
   - How the parent can withdraw consent
   - Contact details of DPO / Grievance Officer
5. Parent/guardian reviews and provides **affirmative, informed consent**:
   - Digital signature or OTP confirmation
   - Record: parent identity, verification method, timestamp, consent scope
6. On consent received → activate child account with all safeguards applied.
7. On consent not received within 72 hours → suspend onboarding; send reminder. ⚠️ 72-hour timeout is a best practice recommendation — not prescribed in the Act.
8. On consent refused → account not activated; data deleted.

**Output:** Parental consent record; child account activated with protections; refusal handled.

---

### Workflow 3: Children's Data Safeguards Activation

**Trigger:** Child account confirmed and active.

**Steps:**
1. Apply **Children's Data Flag** across all systems and databases for this user.
2. Activate the following technical controls:

   ```
   MANDATORY CONTROLS FOR CHILDREN'S ACCOUNTS
   ═══════════════════════════════════════════════════════════
   □ Profiling engine        → DISABLED
   □ Tracking (location)     → DISABLED (or explicit per-use consent)
   □ Behavioural monitoring  → DISABLED
   □ Targeted advertising    → DISABLED
   □ Recommendation engine   → DISABLED or set to age-appropriate only
   □ Cross-app tracking      → DISABLED
   □ Dark patterns           → BLOCKED (verified by UX review)
   □ Push notifications      → DISABLED or parent-controlled
   □ In-app purchases        → DISABLED or parent-approved
   □ Data sharing with third parties → BLOCKED unless DPA covers children
   □ Cross-border transfer   → Extra scrutiny; DPO approval required
   ═══════════════════════════════════════════════════════════
   ```

3. Activate **Parental Dashboard** access:
   - Parent can view child's account data
   - Parent can view consent grants
   - Parent can withdraw specific consents
   - Parent can request full data deletion
   - Parent can set additional controls
4. Log activation of all controls with timestamp.

**Output:** All safeguards activated; Parental Dashboard live; controls log maintained.

---

### Workflow 4: Processing Children's Data — Permitted Activities

**Trigger:** Any processing of a child's personal data.

**Pre-Processing Check:**

```
CHILDREN'S DATA PROCESSING GATE
─────────────────────────────────────────────────────────
For EVERY processing operation on children's data:

Step 1: Is there a valid parental consent record for this purpose?
        NO → BLOCK processing; trigger re-consent or escalate

Step 2: Is this processing purpose within the consented scope?
        NO → BLOCK processing; fresh parental consent required

Step 3: Does this processing involve profiling?
        YES → BLOCK unconditionally

Step 4: Does this processing involve tracking or monitoring?
        YES → BLOCK unconditionally

Step 5: Does this processing involve advertising or marketing?
        YES → BLOCK unconditionally

Step 6: Is the data minimised to what is necessary for the purpose?
        NO → Reduce data scope before proceeding

Step 7: Does this processing remain within India?
        NO → DPO approval required before proceeding

APPROVED → Log processing with timestamp and consent reference
─────────────────────────────────────────────────────────
```

**Output:** Processing approved or blocked with log entry.

---

### Workflow 5: Parental Consent Withdrawal

**Trigger:** Parent/guardian requests withdrawal of consent.

**Steps:**
1. Authenticate parent/guardian identity.
2. Present all active consents and associated processing activities.
3. Parent selects consents to withdraw (partial or full).
4. On full withdrawal:
   - Immediately cease all processing of child's data
   - Block child's account
   - Initiate data erasure (all data processed solely on parental consent)
   - Notify child (if age-appropriate) and parent of withdrawal completion
5. On partial withdrawal:
   - Cease processing for withdrawn purpose
   - Maintain data only for remaining consented purposes
   - Notify parent of outcome
6. Propagate withdrawal to all processors and third parties.
7. Issue withdrawal confirmation to parent.
8. Log withdrawal with timestamp, scope, and propagation record.

**Output:** Withdrawal processed; data erased (where applicable); processors notified.

---

### Workflow 6: Child Reaching Age of Majority (18th Birthday)

**Trigger:** Child's stored date of birth indicates they have reached 18.

**Steps:**
1. Detect age threshold crossing (automated, based on stored DOB).
2. Notify the user directly:
   - They have reached 18 years of age
   - Parental consent is no longer required
   - They may now exercise their own Data Principal rights
   - Invite them to review and confirm / update their consents
3. Transition account:
   - Remove Children's Data Flag
   - Enable standard adult controls (profiling, recommendations, etc.) only after explicit re-consent from the now-adult user
   - Do not auto-enable previously blocked features without new consent
4. Notify parent/guardian that parental consent has lapsed.
5. Archive parental consent records (retain for audit purposes).
6. Update all systems with new status.

**Output:** Age transition completed; new consent obtained from adult user; parental records archived.

---

### Workflow 7: Children's Data Audit

**Trigger:** Quarterly review; annual audit; post-incident.

**Steps:**
1. Pull all accounts with Children's Data Flag.
2. Verify for each:
   - Valid parental consent record exists
   - Consent is not expired or withdrawn
   - All mandatory controls are active (profiling OFF, tracking OFF, advertising OFF)
   - No processing has occurred outside consented scope
   - Parental Dashboard is functional
3. Sample test parental consent validity:
   - Cross-check parent identity with verification record
   - Confirm consent scope matches active processing
4. Check for accounts that should have transitioned to adult status.
5. Verify no children's data has been shared with third parties without DPA.
6. Generate **Children's Data Audit Report**.
7. Flag anomalies for immediate remediation.

**Output:** Children's Data Audit Report; anomalies escalated; controls verified.

---

### Workflow 8: Children's Content & UX Review

**Trigger:** Launch of any product feature accessible to children; annual review.

**Steps:**
1. Review all screens, flows, and interactions accessible to child users for:
   - Age-appropriate language and design
   - No dark patterns (guilt-tripping, hidden costs, confusing toggles)
   - No persuasive design techniques targeting children (urgency, FOMO, streaks)
   - No in-app purchase prompts without parental gate
   - No social sharing features without parental consent
   - No collection of location beyond what is necessary for the feature
   - No photo/video collection without explicit per-session parental consent
2. Review notification and communication design:
   - No marketing push notifications to children
   - No email marketing to children's email addresses
   - Communications age-appropriate and approved by parent
3. Engage child safety / CSAM review for any content platform.
4. Conduct **age-appropriate design assessment** (recommended: AADC / KIDAS framework).
5. Issue sign-off or remediation list.

**Output:** Children's UX review report; design sign-off or remediation list.

---

### Workflow 9: Incident Involving Children's Data

**Trigger:** Any breach or near-miss involving children's personal data.

**Steps:**
1. Immediately classify as **P1 CRITICAL** regardless of scale.
2. Notify DPO within 30 minutes.
3. Escalate to CEO and Board within 1 hour.
4. Engage Legal Counsel immediately.
5. Invoke Breach Notification Agent — DPBI notification mandatory.
6. Notify all affected parents/guardians within 24 hours (best practice recommendation — the Act does not prescribe a separate faster timeline for children's breaches; the general 72-hour DPBI notification timeline applies per DPDP Rules 2025, Rule 7). See also: `dpdp-breach-notification-agent.md` for general breach workflow.
7. Provide dedicated support line for parent queries.
8. Assess whether child safety authorities need to be notified (e.g., NCPCR).
9. Post-incident: full children's data audit; enhanced controls review.

**Output:** P1 incident managed; parents notified within 24 hours; regulatory notifications filed.

---

## Children's Data Controls Checklist

```
CHILDREN'S DATA COMPLIANCE CHECKLIST
═════════════════════════════════════════════════════════════
AGE VERIFICATION
□ Age determination mechanism implemented before data collection
□ Mechanism goes beyond self-declaration for sensitive services
□ Borderline cases default to child treatment (precautionary)

PARENTAL CONSENT
□ Parental consent obtained for all children under 18
□ Parent/guardian identity verified before consent accepted
□ Consent request includes full disclosure of data use
□ Parental consent records maintained with verification evidence

TECHNICAL CONTROLS
□ Profiling — DISABLED for all child accounts
□ Tracking — DISABLED for all child accounts
□ Behavioural monitoring — DISABLED
□ Targeted advertising — DISABLED
□ Recommendation algorithms — DISABLED or age-gated
□ Cross-app/cross-site tracking — DISABLED
□ In-app purchases — DISABLED or parental gate
□ Third-party data sharing — BLOCKED unless DPA covers children

PARENTAL CONTROLS
□ Parental Dashboard — available and functional
□ Parents can view child's data
□ Parents can withdraw consent granularly
□ Parents can request full data deletion
□ Parents receive notifications of material changes

LIFECYCLE
□ Age-of-majority transition automated on 18th birthday
□ Re-consent from adult user before enabling adult features
□ Parental consent records archived on transition

AUDIT
□ Quarterly children's data audit conducted
□ Annual UX/content review for child-accessible features
□ Incident escalation path to P1 Critical for any breach
═════════════════════════════════════════════════════════════
```

---

## Penalty Reference

| Violation | Maximum Penalty |
|---|---|
| Non-fulfilment of children's data obligations | **₹200 crore** |
| Profiling / targeting children | Included in above |
| Processing without parental consent | Included in above |

---

## Related Agents

- `dpdp-consent-management-agent.md` — Parental consent collection and withdrawal
- `dpdp-dpia-agent.md` — DPIA mandatory for processing children's data
- `dpdp-breach-notification-agent.md` — General breach workflow (children's breaches require faster 24-hour parent notification)

---

## Agent Guardrails

- **Always default** to child treatment when age is uncertain — never assume adult.
- **Never allow** profiling, tracking, or advertising for any child account — no exceptions.
- **Always escalate** any children's data breach to P1 Critical immediately.
- **Never accept** self-declaration alone as sufficient for sensitive data processing.
- **Always notify** parents faster than standard Data Principal notification timelines.
- **Never re-enable** adult features automatically on age-of-majority — require new consent.

---

## References

- DPDP Act, 2023 — Section 9 (Processing of Personal Data of Children)
- MeITY DPDP Rules, 2025 (Notified)
- NCPCR — National Commission for Protection of Child Rights
- UK Age Appropriate Design Code (AADC) — comparative reference
- UNICEF — Guidelines on Children's Online Privacy
