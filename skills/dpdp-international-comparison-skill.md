---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "International Comparison"
type: "skill"
---

# DPDP International Privacy Law Comparison Skill

## Skill Identity

**Skill Name:** dpdp-international-comparison
**Domain:** Comparative Privacy Law — DPDP Act vs GDPR, PDPA, CCPA, PIPL and global standards
**Skill Type:** Legal, Comparative, Regulatory, Strategy
**Applicable To:** DPOs, Legal Teams, Global Compliance Heads, Multinational Organisations, Policy Teams

---

## Skill Purpose

Enable organisations operating across multiple jurisdictions to understand how India's DPDP Act compares with major global privacy frameworks — identify overlaps, gaps, stricter requirements, and build a unified privacy programme that satisfies multiple regimes simultaneously.

---

## Jurisdiction Coverage

| Jurisdiction | Law | Regulator |
|---|---|---|
| India | Digital Personal Data Protection Act, 2023 | Data Protection Board of India (DPBI) |
| European Union / UK | GDPR / UK GDPR | EDPB / ICO |
| USA (California) | CCPA 2018 / CPRA 2020 | California Privacy Protection Agency (CPPA) |
| China | Personal Information Protection Law (PIPL), 2021 | CAC / MPS |
| Singapore | Personal Data Protection Act (PDPA), 2012 (amended 2020) | PDPC |
| Australia | Privacy Act 1988 (amended) | OAIC |
| Japan | Act on Protection of Personal Information (APPI) | PPC |
| Brazil | Lei Geral de Proteção de Dados (LGPD), 2020 | ANPD |
| Canada | PIPEDA / Bill C-27 (pending) | OPC |

---

## Capability 1: DPDP vs GDPR — Detailed Comparison

**Trigger:** "GDPR vs DPDP", "compare DPDP and GDPR", "India EU privacy comparison"

### Side-by-Side Comparison

| Aspect | DPDP Act (India) | GDPR (EU/UK) | Stricter? |
|---|---|---|---|
| **Territorial Scope** | Processing of personal data in India; processing outside India if goods/services offered to persons in India | Same broad scope | Similar |
| **Legal Bases** | Consent + Section 7 Legitimate Uses (narrower list) | 6 lawful bases (consent, contract, legal obligation, vital interests, public task, legitimate interests) | GDPR has broader bases — DPDP narrower |
| **Legitimate Interest** | NOT available as a standalone basis | Available — requires balancing test | GDPR more flexible |
| **Consent Standard** | Free, specific, informed, unconditional, unambiguous | Free, specific, informed, unambiguous | Very similar; DPDP adds "unconditional" |
| **Consent Withdrawal** | Must be as easy as giving | Same | Equal |
| **Children's Age** | Under 18 | Under 16 (can be lowered to 13 by member states) | DPDP stricter — 18 vs 16 |
| **Children's Profiling** | Absolutely prohibited | Prohibited without consent/legitimate basis | DPDP stricter — absolute prohibition |
| **Right to Access** | Yes | Yes | Equal |
| **Right to Correction** | Yes | Yes (rectification) | Equal |
| **Right to Erasure** | Yes | Yes (more extensive — GDPR uses "right to be forgotten") | GDPR more extensive |
| **Right to Portability** | Not in DPDP | Yes (GDPR Article 20) | GDPR more extensive |
| **Right to Object** | Limited — no standalone right to object | Yes (Article 21) | GDPR more extensive |
| **Automated Decisions** | No explicit provision (SDF obligations implied) | Article 22 — explicit right to object | GDPR more explicit |
| **DPO Requirement** | Only SDFs (mandatory) | Broader categories (public bodies, high-risk processing) | GDPR broader DPO obligation |
| **DPIA Requirement** | Periodic — SDFs | High-risk processing — all controllers | GDPR broader DPIA requirement |
| **Breach Notification** | Mandatory — all breaches; 72 hours to DPBI (Rule 7) | 72 hours to supervisory authority; individuals if high risk | Both 72-hour SLA; DPDP notifies all breaches, GDPR only "likely to result in risk" |
| **Cross-Border Transfer** | Permissible country list (not yet published) | Adequacy decisions, SCCs, BCRs | GDPR has established mechanisms; DPDP developing |
| **Processor Obligations** | Flow-down via DPA | Direct obligations under GDPR | GDPR more direct |
| **Maximum Penalty** | ₹250 crore (~€28M) per instance | €20M or 4% global turnover (whichever higher) | GDPR potentially much higher for large companies |
| **Penalties on Individuals** | Data Principal: ₹10,000 only | No individual penalties per se | DPDP has nominal individual duties |
| **Regulatory Body** | Data Protection Board (digital — adjudicatory) | Supervisory Authorities (proactive regulators) | GDPR regulators more proactive |

### Key Differences Summary

```
DPDP IS STRICTER THAN GDPR ON:
  ✓ Children's age threshold (18 vs 16)
  ✓ Children's profiling — absolute prohibition (no exceptions)
  ✓ Consent — "unconditional" requirement
  ✓ Cross-border transfers — narrower (permissible list only, no SCCs equivalent yet)

GDPR IS STRICTER THAN DPDP ON:
  ✓ More lawful bases (legitimate interests, contract, public task)
  ✓ Right to portability
  ✓ Right to object to processing
  ✓ Automated decision rights (Article 22)
  ✓ DPIA requirement (broader — not just SDFs)
  ✓ DPO requirement (broader scope)
  ✓ Penalty quantum (4% global turnover can exceed ₹250 crore)
  ✓ Supervisory authority powers (more proactive enforcement)
  ✓ Processor direct obligations
```

**Unified Programme Recommendation:**
For organisations subject to both GDPR and DPDP:
- Apply GDPR's broader lawful bases + DPDP's stricter consent/children standards
- Apply GDPR's DPO/DPIA requirements (broader) globally
- Apply DPDP's stricter children's protection (under-18; no profiling)
- Apply GDPR's data portability and right to object globally
- Maintain separate breach notification timelines (72 hours for both)

---

## Capability 2: DPDP vs CCPA/CPRA (California)

**Trigger:** "CCPA vs DPDP", "California privacy vs India privacy", "CPRA comparison"

| Aspect | DPDP Act (India) | CCPA / CPRA (California) | Stricter? |
|---|---|---|---|
| **Scope** | Personal data; India nexus | Consumers in California; revenue/data volume thresholds | CCPA has thresholds (small businesses exempt) |
| **Legal Basis** | Consent or legitimate use | Opt-out model (not opt-in for most processing) | DPDP stricter — opt-in consent |
| **Children** | Under 18; parental consent; no profiling | Under 16: opt-in required; Under 13: parental consent | DPDP stricter (18 vs 16 threshold) |
| **Right to Know** | Access right | Yes | Similar |
| **Right to Delete** | Erasure right | Yes (with exceptions) | Similar |
| **Right to Opt-Out of Sale** | Not explicit in DPDP | Core CCPA right | CCPA more specific |
| **Right to Portability** | Not in DPDP | Yes (CPRA) | CPRA more extensive |
| **Right to Correct** | Yes | Yes (CPRA) | Similar |
| **Sensitive Data** | Special treatment (health, financial, biometric) | Additional opt-in for sensitive data (CPRA) | Similar approach |
| **Profiling / Automated Decisions** | Children prohibited; SDF obligations | Right to opt-out (CPRA) | Both address but differently |
| **Penalties** | ₹250 crore max | $7,500 per intentional violation | CCPA per-violation; DPDP per-instance |
| **Private Right of Action** | Not in DPDP | Limited — for data breaches (CCPA) | CCPA allows individual lawsuits |

---

## Capability 3: DPDP vs PIPL (China)

**Trigger:** "PIPL vs DPDP", "China privacy vs India privacy", "PIPL comparison"

| Aspect | DPDP Act (India) | PIPL (China) | Stricter? |
|---|---|---|---|
| **Consent Standard** | Similar — free, specific, informed | Voluntary, express, fully informed | Similar |
| **Separate Consent** | Per purpose | Separate consent for each category of sensitive info | Similar |
| **Cross-Border Transfer** | Permissible country list | Security assessment + standard contract + certification | PIPL has established mechanism; DPDP developing |
| **Data Localisation** | Permissible country concept | Critical information — must stay in China | PIPL stricter localisation for critical data |
| **Right to Withdraw** | Explicit | Explicit | Similar |
| **DPIA** | SDF — periodic | Required before cross-border transfer, sensitive data, automated decisions | PIPL broader DPIA triggers |
| **Children** | Under 18 | Under 14 (minor) | DPDP stricter age threshold |
| **Penalties** | ₹250 crore | ¥50M or 5% annual revenue | PIPL potentially higher for large companies |
| **Data Localisation** | Pending permissible list | Explicit critical data localisation | PIPL more defined |
| **State Access** | State function legitimate use | Broad state access rights | PIPL broader state access |

---

## Capability 4: DPDP vs PDPA (Singapore)

**Trigger:** "PDPA vs DPDP", "Singapore privacy vs India", "PDPA comparison"

| Aspect | DPDP Act (India) | PDPA (Singapore) | Stricter? |
|---|---|---|---|
| **Legal Bases** | Consent + legitimate uses | Consent + multiple exceptions (contractual, legal necessity, legitimate interests) | PDPA more flexible |
| **Legitimate Interest** | Not available | Available with assessment | PDPA more flexible |
| **Data Portability** | Not in DPDP | Mandatory portability obligation (2021 amendment) | PDPA more extensive |
| **Breach Notification** | Mandatory | Mandatory (3 days to PDPC; notification if significant harm) | Similar |
| **DPO** | SDF mandatory | Recommended (not mandatory for most) | DPDP more prescriptive for SDFs |
| **Cross-Border Transfer** | Permissible country list | Comparable protection standard | PDPA more flexible mechanisms |
| **Penalties** | ₹250 crore | S$1M (enhanced: 10% annual turnover) | PDPA potentially higher for large companies |
| **Children** | Under 18 | Under 18 | Equal threshold |

---

## Capability 5: Multi-Jurisdiction Compliance Matrix

**Trigger:** "multi-jurisdiction privacy", "comply with GDPR and DPDP", "global privacy programme"

**Unified Compliance Framework — Apply the Strictest Standard:**

```
MULTI-JURISDICTION PRIVACY COMPLIANCE MATRIX
Apply the STRICTEST requirement across all applicable jurisdictions

CONSENT:
  Requirement: Affirmative opt-in (DPDP / GDPR standard)
  India: Free, specific, informed, unconditional, unambiguous ← APPLY
  EU: Free, specific, informed, unambiguous
  US: Opt-out in most cases (less strict — apply Indian standard globally)

CHILDREN'S AGE THRESHOLD:
  India: Under 18 ← APPLY (strictest)
  EU: Under 16 (can be 13)
  Singapore: Under 18
  Apply: Under 18 globally

CHILDREN'S PROFILING:
  India: Absolutely prohibited ← APPLY (strictest)
  EU: Prohibited without specific basis
  Apply: No profiling of under-18s globally

DATA PRINCIPAL / SUBJECT RIGHTS:
  Apply union of all rights:
  ✓ Access (all jurisdictions)
  ✓ Correction/Rectification (all)
  ✓ Erasure/Deletion (all)
  ✓ Portability (GDPR, CPRA, PDPA) ← add globally
  ✓ Right to object (GDPR, CPRA) ← add globally
  ✓ Automated decision rights (GDPR) ← add globally
  ✓ Withdrawal of consent (all)

BREACH NOTIFICATION:
  Regulator: 72 hours (GDPR) = apply globally
  Individuals: Where likely harm (GDPR, DPDP, PDPA standards)

CROSS-BORDER TRANSFER:
  Most restrictive: PIPL (security assessment) for China
  For India: await permissible country list; precautionary localisation
  For EU: adequacy / SCCs / BCRs
  Apply: jurisdiction-specific; document basis for each transfer

DPO / PRIVACY OFFICER:
  GDPR: Broader scope of mandatory DPO ← apply globally
  DPDP SDF: DPO based in India (India entity specific)

DPIA:
  GDPR: High-risk processing ← apply globally
  DPDP: SDF periodic; all high-risk
  Apply: DPIA for all high-risk processing globally
```

**Output:** Multi-jurisdiction compliance matrix; unified programme design.

---

## Capability 6: Adequacy & Transfer Mechanism Comparison

**Trigger:** "is India GDPR adequate", "transfer data from EU to India", "India adequacy"

```
TRANSFER FROM EU TO INDIA — CURRENT STATUS (2025)
══════════════════════════════════════════════════════════════
Status: India does NOT have EU adequacy decision.

Available transfer mechanisms (EU → India):
  1. Standard Contractual Clauses (SCCs) — most common
  2. Binding Corporate Rules (BCRs) — for intra-group
  3. Derogations (explicit consent, vital interests, etc.)
  4. Adequacy: Not granted; ongoing DPDP Act assessment

TRANSFER FROM INDIA TO EU:
  DPDP Act: EU likely to be on permissible country list (once published)
  EU GDPR: Applies to EU Data Subjects regardless of data location

STRATEGIC NOTE:
  Organisations transferring between India and EU should:
  1. Execute SCCs for EU → India transfers
  2. Await DPDP permissible country list for India → EU
  3. Implement GDPR standard controls for Indian entity to be
     GDPR-compliant (anticipates adequacy)
  4. Consider EU representative appointment if Indian entity
     offers services to EU data subjects
══════════════════════════════════════════════════════════════
```

**Output:** Transfer mechanism analysis; documentation required.

---

## Capability 7: Global Privacy Vocabulary Mapping

**Trigger:** "privacy terminology", "GDPR terms in DPDP", "data subject vs data principal"

```
PRIVACY TERMINOLOGY MAPPING
════════════════════════════════════════════════════════════
DPDP Act (India)         GDPR (EU)              CCPA (US)
─────────────────────────────────────────────────────────────
Data Principal           Data Subject            Consumer
Data Fiduciary           Data Controller         Business
Data Processor           Data Processor          Service Provider
Personal Data            Personal Data           Personal Information
Processing               Processing              Processing
Consent Manager          (no equivalent)         (no equivalent)
DPBI                     Supervisory Authority   CPPA
Legitimate Use           Lawful Basis            (no direct equivalent)
SDF                      (no equivalent)         (no equivalent)
─────────────────────────────────────────────────────────────

RIGHTS TERMINOLOGY MAPPING
─────────────────────────────────────────────────────────────
DPDP                    GDPR                    CCPA
Right to Information    Right of Access (Art.15) Right to Know
Right to Correction     Right to Rectification   Right to Correct
Right to Erasure        Right to Erasure (Art.17)Right to Delete
Right to Nominate       (no equivalent)          (no equivalent)
(no equivalent)         Right to Portability     Right to Portability
(no equivalent)         Right to Object          Right to Opt-Out
Grievance Redressal     Right to Complain        Right to Non-Discrimination
─────────────────────────────────────────────────────────────
```

**Output:** Terminology mapping; consistent global policy language.

---

## Quick Commands

| Command | Action |
|---|---|
| `/compare-gdpr` | Detailed DPDP vs GDPR comparison |
| `/compare-ccpa` | DPDP vs CCPA/CPRA comparison |
| `/compare-pipl` | DPDP vs PIPL (China) comparison |
| `/compare-pdpa` | DPDP vs PDPA (Singapore) comparison |
| `/multi-jurisdiction` | Build multi-jurisdiction compliance matrix |
| `/transfer-mechanism` | Analyse cross-border transfer mechanisms |
| `/privacy-vocabulary` | Map privacy terminology across jurisdictions |

---

## Related Skills

- `dpdp-contract-clauses-skill.md` — Multi-jurisdiction clauses
- `dpdp-sector-specific-skill.md` — Sector cross-jurisdiction
- `dpdp-privacy-programme-management-skill.md` — Global programme

---

## Skill Guardrails

- **Never assume** GDPR or CCPA compliance automatically satisfies DPDP requirements — each jurisdiction has unique obligations.
- **Always verify** comparisons against the latest version of each law — privacy regulations evolve frequently.
- **Always consult local legal counsel** in each jurisdiction for binding compliance decisions.
- **Never use** international comparisons to argue for a lower compliance standard under DPDP.
- **Always document** the basis for multi-jurisdiction compliance decisions.

---

## References

- Digital Personal Data Protection Act, 2023 (India)
- GDPR — Regulation (EU) 2016/679
- UK GDPR — Data Protection Act 2018
- CCPA / CPRA — California Consumer Privacy Act 2018 / 2020
- PIPL — Personal Information Protection Law 2021 (China)
- PDPA — Personal Data Protection Act 2012 (Singapore, amended 2020)
- LGPD — Lei Geral de Proteção de Dados 2020 (Brazil)
- APPI — Act on Protection of Personal Information (Japan)
- Privacy Act 1988 (Australia)
- IAPP Global Privacy Law Comparison
