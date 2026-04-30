---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Privacy by Design"
type: "skill"
---

# DPDP Privacy by Design Skill

## Skill Identity

**Skill Name:** dpdp-privacy-by-design
**Domain:** Privacy Engineering, Product Development, Software Architecture
**Skill Type:** Technical, Engineering, Privacy, Compliance
**Applicable To:** Product Managers, Software Engineers, Architects, UX Designers, DPOs, QA Teams

---

## Skill Purpose

Embed privacy protections into the design and architecture of products, systems, and processes from the outset — not as an afterthought. Operationalise DPDP Act compliance at the engineering and product level, ensuring systems are built to be privacy-safe by default.

---

## Privacy by Design — 7 Foundational Principles

```
1. PROACTIVE NOT REACTIVE
   Anticipate and prevent privacy breaches before they occur.
   Do not wait for a problem to emerge.

2. PRIVACY AS THE DEFAULT
   Maximum privacy protection is the default setting.
   Users should not have to take action to protect their privacy.

3. PRIVACY EMBEDDED INTO DESIGN
   Privacy is a core feature, not a bolt-on.
   Built into the architecture, not added later.

4. FULL FUNCTIONALITY — POSITIVE-SUM
   Privacy AND functionality. Not privacy OR security.
   Avoid false trade-offs.

5. END-TO-END SECURITY
   Data protection across the full data lifecycle —
   from collection to deletion.

6. VISIBILITY AND TRANSPARENCY
   Open about practices. Policies and procedures match reality.

7. RESPECT FOR USER PRIVACY
   Keep it user-centric. Respect Data Principal rights by default.
```

---

## DPDP Act Engineering Requirements

| DPDP Obligation | Engineering Requirement |
|---|---|
| Data minimisation (Sec 4 / Sec 8) | Collect only required fields; no speculative collection |
| Purpose limitation (Sec 4) | Technical controls prevent cross-purpose data use |
| Consent (Sec 6) | Consent gate before data collection; consent store |
| Data accuracy (Sec 8) | Validation at input; correction workflow |
| Retention / deletion (Sec 8) | Automated deletion at end of retention period |
| Security safeguards (Sec 8) | Encryption, access control, audit logging |
| Data Principal rights (Sec 11–14) | Self-service rights portal; API for access/erasure |
| Breach detection (Sec 8) | Monitoring, alerting, incident response integration |
| Children's data (Sec 9) | Age verification gate; parental consent flow |

---

## Skill Capabilities

---

### Capability 1: Privacy Requirements Elicitation

**Trigger:** "define privacy requirements", "what are the privacy requirements for this feature", "DPDP requirements for new product"

**Steps:**
1. Review product / feature specification.
2. Answer the **Privacy Scoping Questions**:

   ```
   PRIVACY SCOPING CHECKLIST
   ─────────────────────────────────────────────────
   □ What personal data will this feature collect?
   □ Why is each data field necessary?
   □ Who are the Data Principals (users, employees, children)?
   □ What is the legal basis for processing?
   □ Where will data be stored (India / overseas)?
   □ Who will have access to this data internally?
   □ Will data be shared with third parties / processors?
   □ What is the retention period?
   □ How will data be deleted at end of retention?
   □ What are the security requirements?
   □ Does this involve automated decision-making?
   □ Does this involve profiling or tracking?
   □ Does this involve children's data?
   □ Is a DPIA required?
   ─────────────────────────────────────────────────
   ```

3. Map answers to DPDP obligations.
4. Generate **Privacy Requirements Document** for the product/feature.
5. Attach to product spec / user story / epic.

**Output:** Privacy Requirements Document; DPIA triggered if needed.

---

### Capability 2: Consent UX Design Review

**Trigger:** "review consent UI", "check consent design", "is our consent UX compliant", "dark patterns check"

**Steps:**
1. Review consent screens and flows against DPDP requirements.
2. Check for **dark patterns** — flag and remediate:

   | Dark Pattern | DPDP Issue | Fix |
   |---|---|---|
   | Pre-ticked consent boxes | Consent not affirmative | Remove pre-ticks; require active selection |
   | Bundled consent (all or nothing) | Consent not specific | Separate consent per purpose |
   | Confusing language | Consent not informed | Plain language rewrite |
   | Hidden withdrawal option | Withdrawal not as easy as consent | Prominent withdrawal link |
   | Consent wall (no service without unrelated consent) | Consent not free | Decouple service from unrelated consent |
   | Misleading button labels ("Accept All" vs "Manage") | Not unambiguous | Balanced, clear button labels |
   | Guilt-tripping ("No thanks, I hate privacy") | Coercive | Neutral decline option |
   | Infinite scroll consent | Not affirmative | Explicit confirmation required |

3. Verify consent notice contains all mandatory elements.
4. Verify withdrawal mechanism is accessible from within the product at all times.
5. Provide annotated UX review report with specific fixes.

**Output:** Consent UX review report; dark patterns list; remediation recommendations.

---

### Capability 3: Data Minimisation in Code Review

**Trigger:** "data minimisation review", "are we collecting too many fields", "unnecessary data in API", "review data model for DPDP"

**Steps:**
1. Review data models, API schemas, database schemas, and form fields.
2. For each data field, challenge:
   - Is this field **used** in any downstream process?
   - Is it **necessary** for the stated purpose?
   - Can the purpose be achieved with a **less identifying** alternative?
     - e.g., Age range instead of date of birth
     - e.g., City instead of precise address
     - e.g., Hashed ID instead of name
3. Flag fields that are:
   - Collected but **never used** → remove
   - Used for only one historical purpose → evaluate removal
   - More precise than needed → consider generalisation
4. Recommend **pseudonymisation** where full PII is not required at processing layer.
5. Recommend **anonymisation** for analytics / reporting datasets.

**Output:** Data minimisation report; unused fields flagged; pseudonymisation recommendations.

---

### Capability 4: Encryption & Security Architecture Review

**Trigger:** "DPDP security review", "encryption requirements", "security architecture for personal data", "is our security DPDP compliant"

**Steps:**
1. Review security architecture for personal data systems.

   **Encryption Requirements:**
   ```
   AT REST:
   □ Personal data encrypted at rest (AES-256 or equivalent)
   □ Encryption keys managed separately from data
   □ Key rotation policy in place
   □ Sensitive data (Tier 1) — additional field-level encryption

   IN TRANSIT:
   □ TLS 1.2+ for all data in transit
   □ No plaintext transmission of personal data
   □ API endpoints secured (HTTPS only)
   □ Internal service-to-service encryption

   BACKUPS:
   □ Backups encrypted
   □ Backup access controls as strict as production
   □ Backup retention aligns with data retention policy
   ```

   **Access Control Requirements:**
   ```
   □ Role-Based Access Control (RBAC) implemented
   □ Principle of least privilege enforced
   □ MFA on all systems storing personal data
   □ Privileged access management (PAM) for admins
   □ Access reviews conducted quarterly
   □ Joiners / movers / leavers process for access revocation
   ```

   **Audit Logging Requirements:**
   ```
   □ All access to personal data logged
   □ Logs are tamper-evident and immutable
   □ Log retention: minimum 1 year (or as required by law)
   □ Alerts on anomalous access patterns (SIEM)
   □ Logs do not themselves contain unnecessary personal data
   ```

2. Flag gaps and assign severity.
3. Generate Security Architecture Gap Report.

**Output:** Security review report; gaps classified; remediation plan.

---

### Capability 5: Automated Retention & Deletion Engineering

**Trigger:** "build data deletion", "automated retention", "how to implement data deletion", "DPDP deletion requirement"

**Steps:**
1. Map retention periods from the Data Retention Schedule to each data store.
2. Design **automated deletion pipeline**:

   ```
   DELETION PIPELINE DESIGN
   ────────────────────────────────────────────────────
   1. Retention Timer
      • Start timer from: [date of collection / last transaction / consent withdrawal]
      • Trigger deletion at: [retention period expiry]

   2. Deletion Scope
      • Primary database records
      • Data warehouse / analytics copies
      • Backups (scheduled overwrite within retention window)
      • Third-party / processor data (via DPA obligation)
      • Logs containing personal data

   3. Deletion Method
      • Soft delete → hard delete after n days (for recovery window)
      • Cryptographic erasure (for encrypted data — delete the key)
      • Secure overwrite for physical media

   4. Deletion Log
      • Record: Data Principal ID (hashed), data category, deletion timestamp, method
      • Store deletion log for audit purposes (do not store the deleted data)

   5. Exemptions
      • Legal hold flag → bypass deletion until hold released
      • Ongoing legal proceedings → retain with flag
      • Statutory retention override → retain with legal basis noted
   ────────────────────────────────────────────────────
   ```

3. Implement erasure API endpoint for Data Principal erasure requests.
4. Test deletion pipeline — verify data is irrecoverable after deletion.
5. Document deletion architecture in RoPA.

**Output:** Deletion pipeline design; erasure API spec; test plan; RoPA updated.

---

### Capability 6: Data Principal Rights API Design

**Trigger:** "build rights portal", "implement access request", "erasure API", "DPDP rights API"

**Steps:**
1. Design self-service **Data Principal Rights Portal** with:

   ```
   RIGHTS PORTAL FEATURES
   ─────────────────────────────────────────────────
   □ Login / identity verification
   □ View all personal data held (access request)
   □ Download data export (structured format — JSON / CSV)
   □ Request correction (form with supporting upload)
   □ Request erasure (with confirmation and exemption notice)
   □ Manage consents (view, withdraw per purpose)
   □ File a grievance
   □ Nominate another person
   □ View request history and status
   ─────────────────────────────────────────────────
   ```

2. Design **Rights Request API** for programmatic fulfilment:

   ```
   API ENDPOINTS (reference design)
   ─────────────────────────────────────────────────
   POST /rights/access-request
   POST /rights/correction-request
   POST /rights/erasure-request
   POST /rights/consent-withdrawal
   POST /rights/grievance
   POST /rights/nomination
   GET  /rights/request-status/{request_id}
   ─────────────────────────────────────────────────
   ```

3. Implement **SLA tracking** — flag requests approaching deadline.
4. Integrate with downstream systems (CRM, data warehouse, consent store, processors).
5. Log all rights requests in Rights Request Register.

**Output:** Rights portal design; API specification; SLA tracking; integration map.

---

### Capability 7: Children's Data Technical Safeguards

**Trigger:** "age verification implementation", "children's data safeguards", "parental consent technical", "DPDP children compliance"

**Steps:**
1. Implement **age gate** before any data collection:
   - Self-declaration (minimum bar — not sufficient alone for Tier 1 data)
   - AI-based age estimation
   - Document verification
   - Parent / guardian consent verification with identity check
2. On identification as under-18:
   - Require parental / guardian consent flow
   - Apply **children's data flag** to all records
   - Block profiling module
   - Block targeted advertising engine
   - Block behavioural tracking
   - Enable parental dashboard access
3. Implement **parental controls**:
   - Parent can view child's data
   - Parent can withdraw consent
   - Parent can request deletion
4. Periodic re-verification on birthday / age threshold crossing.
5. Audit children's data handling in every release cycle.

**Output:** Age verification design; parental consent flow; children's data flags; parental controls.

---

### Capability 8: Breach Detection & Response Integration

**Trigger:** "implement breach detection", "security monitoring for DPDP", "breach alerting", "incident response integration"

**Steps:**
1. Implement **anomaly detection** on personal data access:
   - Bulk data exports outside normal patterns
   - After-hours access to sensitive data
   - Failed login spikes
   - Privilege escalation events
   - Unusual data transfer volumes
2. Configure **SIEM alerts** for personal data breach indicators.
3. Integrate alerts with **Incident Response workflow**:
   - Auto-create incident ticket
   - Alert DPO and Security team
   - Trigger breach assessment checklist
4. Implement **data loss prevention (DLP)** controls:
   - Block email of large personal data files without DLP review
   - Monitor cloud storage for misconfigured public access
   - Block unapproved data transfer destinations
5. Integrate with **Breach Notification Agent** for DPBI and Data Principal notification.

**Output:** Breach detection rules; SIEM integration; DLP controls; incident response integration.

---

### Capability 9: Privacy Design Sign-Off Checklist

**Trigger:** "privacy sign-off", "is this feature ready for launch", "DPDP sign-off", "pre-launch privacy check"

**Steps:**
Run the **Pre-Launch Privacy Checklist**:

```
PRE-LAUNCH DPDP PRIVACY CHECKLIST
═══════════════════════════════════════════════════════════════
LEGAL BASIS & CONSENT
□ Legal basis identified for all processing activities
□ Consent notice drafted and reviewed by Legal / DPO
□ Consent flow implemented — affirmative, no dark patterns
□ Withdrawal mechanism accessible
□ Consent records stored

DATA MINIMISATION
□ Only necessary data fields collected
□ No unused fields in data model
□ Pseudonymisation / anonymisation applied where possible

RETENTION & DELETION
□ Retention period defined for all data categories
□ Automated deletion implemented or scheduled
□ Deletion mechanism tested and verified

SECURITY
□ Personal data encrypted at rest and in transit
□ Access controls (RBAC, least privilege) implemented
□ Audit logging enabled
□ MFA on relevant systems

DATA PRINCIPAL RIGHTS
□ Rights portal / API supports this feature's data
□ Erasure request will delete data from this feature
□ Access request will include this feature's data

VENDOR / PROCESSORS
□ DPAs executed with all vendors receiving this data
□ Cross-border transfers assessed and permissible

CHILDREN'S DATA
□ Age verification implemented (if applicable)
□ Parental consent flow implemented (if applicable)
□ Profiling / targeting disabled for children

DPIA
□ DPIA pre-screening completed
□ DPIA conducted and approved (if required)

DOCUMENTATION
□ RoPA updated for this processing activity
□ Privacy Policy updated (if new data / purpose)
□ DPO notified and sign-off obtained
═══════════════════════════════════════════════════════════════
SIGN-OFF: DPO _____________ Date _____________
          Product Owner _____________
```

**Output:** Completed pre-launch checklist; DPO sign-off; launch cleared or blocked with findings.

---

## Related Skills

- `dpdp-data-mapping-inventory-skill.md` — Data flows
- `dpdp-ai-ml-ethics-skill.md` — AI privacy engineering
- `dpdp-consent-manager-skill.md` — Consent UX

---

## Skill Guardrails

- **Block launch** if consent mechanism has dark patterns or is non-compliant.
- **Never collect** data fields that are not mapped to a specific, documented purpose.
- **Always test** deletion pipelines — verify data is irrecoverable.
- **Always build** rights fulfilment into the system — not as a manual workaround.
- **Never skip** the privacy sign-off for time-to-market pressure.

---

## Quick Commands

| Command | Action |
|---|---|
| `/pbd-requirements` | Elicit privacy requirements for product/feature |
| `/pbd-consent-review` | Review consent UX for dark patterns |
| `/pbd-data-minimisation` | Review data model for minimisation |
| `/pbd-security-review` | Review encryption and access controls |
| `/pbd-deletion-design` | Design automated retention and deletion |
| `/pbd-rights-api` | Design Data Principal rights API |
| `/pbd-children-safeguards` | Implement children's data controls |
| `/pbd-breach-detection` | Set up breach detection integration |
| `/pbd-sign-off` | Run pre-launch privacy sign-off checklist |

---

## References

- DPDP Act, 2023 — Sections 4–9
- MeITY Draft DPDP Rules, 2025
- Ann Cavoukian — Privacy by Design: 7 Foundational Principles
- OWASP Privacy Risks (Top 10)
- ISO/IEC 29101 — Privacy Architecture Framework
- NIST Privacy Framework
