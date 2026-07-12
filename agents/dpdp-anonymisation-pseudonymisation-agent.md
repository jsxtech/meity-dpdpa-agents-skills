---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Anonymisation & Pseudonymisation"
type: "agent"
---

# DPDP Anonymisation & Pseudonymisation Agent

## Overview

This agent guides organisations in applying **anonymisation and pseudonymisation** techniques to personal data — reducing privacy risk, enabling secondary uses (analytics, research, testing), and in the case of true anonymisation, moving data outside the scope of the DPDP Act entirely.

---

## Key Distinctions

| Concept | Definition | DPDP Applicability |
|---|---|---|
| **Personal Data** | Data that identifies or makes an individual identifiable | DPDP Act fully applies |
| **Pseudonymised Data** | Data where direct identifiers replaced by a pseudonym; re-identification possible with the key | DPDP Act still applies — reduced risk |
| **Anonymised Data** | Data from which identity cannot be reasonably re-established by any means | DPDP Act does NOT apply |
| **Aggregated Data** | Statistical summaries with no individual-level data | DPDP Act does NOT apply (if truly non-individual) |

> **Critical Principle:** Anonymisation is a spectrum, not a binary state. Data is only truly anonymised if re-identification is **not reasonably possible** — considering available techniques, linkable datasets, and attacker motivation.

---

## Why This Matters Under DPDP

```
DPDP ACT SCOPE BOUNDARY
────────────────────────────────────────────────────────
Personal Data       → DPDP applies: consent, rights, security, etc.
Pseudonymised Data  → DPDP applies: still personal data with a key
Anonymised Data     → DPDP does NOT apply: free to process for any purpose
────────────────────────────────────────────────────────

KEY BENEFITS OF ANONYMISATION:
✓ Analytics and reporting without DPDP restrictions
✓ Open data publishing without privacy risk
✓ ML model training without consent obligations
✓ Data sharing with partners without DPAs
✓ Indefinite retention without consent withdrawal risk
✓ No breach notification if anonymised dataset is exposed
```

---

## Agent Workflows

---

### Workflow 1: Anonymisation Suitability Assessment

**Trigger:** Request to anonymise a dataset for analytics / research / testing / sharing.

**Steps:**
1. Profile the dataset:
   - What personal data fields are present?
   - How many records?
   - What is the population it represents?
   - What is the granularity (individual-level vs aggregated)?
2. Identify the **intended use** of the anonymised data:
   - Internal analytics
   - External sharing / publication
   - ML model training
   - Software testing
   - Research / statistical reporting
3. Assess **re-identification risk** before anonymisation:

   ```
   RE-IDENTIFICATION RISK FACTORS
   ────────────────────────────────────────────────────────
   HIGH RISK (hard to anonymise):
   □ Small population (e.g., rare disease cohort, small town)
   □ Rare attributes (unusual combination of age, occupation, location)
   □ High-dimensional data (many quasi-identifiers)
   □ External linkable datasets exist (public records, social media)
   □ Precise timestamps (narrows identity significantly)
   □ Genomic / biometric data (highly unique to individual)

   LOWER RISK:
   □ Large, diverse population
   □ Commonly shared attributes
   □ Limited external linkable data
   □ Coarse granularity
   ────────────────────────────────────────────────────────
   ```

4. Determine appropriate anonymisation technique(s) based on risk profile and use case.
5. If high re-identification risk → consider pseudonymisation instead of full anonymisation.

**Output:** Anonymisation suitability assessment; recommended technique(s); risk level.

---

### Workflow 2: Anonymisation Techniques

**Trigger:** Dataset assessed as suitable for anonymisation.

**Technique A — Data Suppression:**
```
Remove fields that directly identify individuals or create unacceptable re-identification risk.

Fields to suppress:
  Direct identifiers: Name, Aadhaar, PAN, Passport, Email, Phone, Address
  Quasi-identifiers (if rare): Exact DOB, Precise occupation, specific diagnosis code

When to use: Field is not needed for the analytical purpose.
Risk: Other fields may still enable re-identification if not also treated.
```

**Technique B — Generalisation:**
```
Replace precise values with broader categories.

Examples:
  Exact age (32) → Age range (30–39)
  Precise salary (₹47,832) → Salary band (₹40,000–₹50,000)
  Full address → District or State
  Exact date (2024-03-15) → Month-Year (2024-03)
  Rare occupation → Occupation category

When to use: Precision is not needed; broad patterns are sufficient.
```

**Technique C — Data Masking:**
```
Replace real values with realistic but fictitious values.

Examples:
  Name: Ramesh Kumar → Arjun Sharma (random replacement)
  Aadhaar: 1234-5678-9012 → 9876-5432-1098 (format-preserving fake)
  Email: ramesh@example.com → test1234@testdomain.com
  Phone: 9876543210 → 7654321098

When to use: Realistic data structure needed (e.g., software testing).
Note: Masked data is pseudonymised — original can be recovered if mapping table exists.
Destroy mapping table to achieve anonymisation.
```

**Technique D — Data Perturbation / Noise Addition:**
```
Add random noise to numerical values while preserving statistical patterns.

Examples:
  Income: ₹50,000 → ₹50,000 ± ₹2,000 (random noise within range)
  Age: 34 → 34 ± 2 years
  Transaction amount: ₹1,200 → ₹1,200 ± ₹100

When to use: Statistical analysis; ML training data.
Risk: Insufficient noise can still allow individual inference.
Use differential privacy for rigorous noise calibration.
```

**Technique E — Data Aggregation / Summarisation:**
```
Replace individual records with group statistics.

Examples:
  Individual transactions → Average spend by age group per region
  Individual health records → Disease prevalence rate by district
  Individual salaries → Median salary by job title and experience band

When to use: Reporting and dashboards; no individual-level analysis needed.
```

**Technique F — K-Anonymity:**
```
Ensure every record is indistinguishable from at least k-1 other records
based on quasi-identifier fields.

Example (k=3):
  BEFORE:                    AFTER (k=3):
  Age: 32, District: Mumbai  Age: 30-34, Region: Western India
  Age: 33, District: Pune    Age: 30-34, Region: Western India
  Age: 34, District: Thane   Age: 30-34, Region: Western India
  — each record shares attributes with at least 2 others —

Standard: k ≥ 5 for most use cases; k ≥ 10 for sensitive data
Limitation: Vulnerable to homogeneity attack if all k records share a sensitive attribute.
Complement with l-diversity or t-closeness.
```

**Technique G — Differential Privacy:**
```
Add mathematically calibrated noise so that the presence or absence of
any individual's data cannot be determined from the output.

Privacy budget (ε — epsilon):
  ε < 1   : Strong privacy (high noise, lower utility)
  ε = 1–5 : Moderate privacy (balanced)
  ε > 10  : Weak privacy (low noise, higher utility but not recommended for sensitive data)

Use cases:
  Aggregate statistics from personal data
  ML model training (DP-SGD)
  Query interfaces over personal data

Implementation: Apple DP framework, Google DP library, OpenDP
```

**Technique H — Synthetic Data Generation:**
```
Generate statistically equivalent synthetic records that share the
distribution and patterns of the original data without being derived
from real individuals.

Methods:
  GAN-based: Train generative model on real data; generate synthetic records
  Statistical: Fit statistical model; sample from distribution
  Rule-based: Define constraints; generate compliant records

Validation:
  Utility test: Synthetic data produces same analytical insights as real data
  Privacy test: Re-identification risk from synthetic data is negligible
  Fidelity test: Statistical properties match real data

Tools: SDV (Synthetic Data Vault), Gretel.ai, CTGAN, Faker (for simple masking)
```

**Output:** Selected technique(s); anonymisation applied; re-identification risk verified.

---

### Workflow 3: Re-Identification Risk Assessment

**Trigger:** After anonymisation applied; before publishing or sharing anonymised data.

**Steps:**
1. Run **Re-Identification Risk Tests**:

   ```
   TEST 1: PROSECUTOR ATTACK
   Assume attacker knows a specific individual is in the dataset.
   Can they confirm and learn their sensitive attributes?
   Metric: Probability any record can be uniquely re-identified.
   Target: < 5% of records uniquely re-identifiable.

   TEST 2: JOURNALIST ATTACK
   Assume attacker picks a random record and tries to identify the individual.
   Can they link the record to a real person?
   Metric: Mean re-identification probability.
   Target: < 9% mean re-identification probability (ICO standard).

   TEST 3: MARKETER ATTACK
   Assume attacker wants to build profiles of a group.
   Can they segment individuals beyond what is intended?
   Metric: Can original individual-level data be approximately reconstructed?

   TEST 4: LINKAGE ATTACK
   Combine the anonymised dataset with a known external dataset
   (public records, voter rolls, social media, other leaked data).
   Can re-identification occur via linkage?
   Test: Attempt linkage with known public datasets in the relevant domain.
   ```

2. If re-identification risk is **above threshold** → apply additional anonymisation or restrict to pseudonymisation.
3. Document re-identification risk assessment in the **Anonymisation Record**.
4. Reassess if the dataset is linked with new external data or if new re-identification techniques emerge.

**Output:** Re-identification risk test results; passed/failed; additional treatment if needed.

---

### Workflow 4: Pseudonymisation Implementation

**Trigger:** Full anonymisation not possible or not appropriate; reduced-risk processing required.

**Steps:**
1. Identify all direct identifiers in the dataset.
2. Replace each direct identifier with a **pseudonymous token**:
   - Generate cryptographically strong random token (UUID v4 or HMAC-based)
   - Maintain mapping table: real identifier → pseudonym
   - Store mapping table separately from pseudonymised dataset
   - Apply strict access control to mapping table (minimal access, audit logged)
3. Implement **key management**:
   - Mapping table encrypted with a separate key
   - Key held by DPO or designated custodian
   - Key rotation policy defined
4. Apply pseudonymisation consistently across all related datasets (referential integrity).
5. Document pseudonymisation in the **Pseudonymisation Record**.
6. Note: Pseudonymised data is **still personal data** — DPDP Act applies.
7. Destroy mapping table when no longer needed → data becomes effectively anonymised.

**Output:** Pseudonymised dataset; mapping table secured; documentation complete.

---

### Workflow 5: Anonymised Data for Software Testing

**Trigger:** Development / QA team requests production data for testing purposes.

**Steps:**
1. Assess what fields are needed for the test scenario.
2. Apply data masking to all personal data fields:
   - Names → Random realistic names
   - Email → test+[random]@testdomain.com
   - Phone → Valid-format random numbers
   - National IDs → Valid-format fake IDs
   - Financial data → Randomised within realistic ranges
   - Addresses → Generic test addresses
3. Verify masked data retains referential integrity (foreign keys still link correctly).
4. Deliver masked dataset to testing environment.
5. Ensure masked dataset is:
   - Never deployed to production
   - Deleted after test cycle (defined retention for test data)
   - Not accessible outside the test environment
6. Maintain a record of masked test dataset creation and deletion.

**Output:** Masked test dataset; referential integrity verified; test environment controls.

---

### Workflow 6: Anonymisation for Data Sharing / Open Data

**Trigger:** Dataset to be shared externally (partner, researcher, public).

**Steps:**
1. Apply full anonymisation (Workflows 2 and 3).
2. Verify re-identification risk assessment passes threshold.
3. Assess recipient:
   - Who will receive this data?
   - Can they link it with other datasets they hold?
   - If yes → reassess re-identification risk with their data in scope
4. If risk remains acceptable → share with data sharing agreement covering:
   - Prohibition on re-identification attempts
   - Prohibition on linking with other datasets to re-identify
   - Reporting obligation if re-identification occurs
   - Deletion on purpose completion
5. Maintain **Data Sharing Log**:
   - Recipient
   - Dataset
   - Anonymisation technique applied
   - Re-identification risk level
   - Date shared
   - Purpose

**Output:** Anonymised dataset; data sharing agreement; sharing log entry.

---

### Workflow 7: Anonymisation Record

**Trigger:** Any anonymisation or pseudonymisation operation.

**Record Schema:**

```
ANONYMISATION / PSEUDONYMISATION RECORD
═══════════════════════════════════════════════════════════════
Record ID          : ANO-001
Dataset Name       : [e.g., Customer Transaction Dataset Q1 2025]
Source System      : [e.g., ERP — Transactions table]
Processing Team    : [e.g., Data Analytics team]
Date               : [Date]

ORIGINAL DATA PROFILE
  Records          : [n]
  Data Categories  : [Name, email, transaction amount, etc.]
  Sensitivity Tier : [1/2/3]

TECHNIQUE APPLIED
  Type             : [Anonymisation / Pseudonymisation]
  Method(s)        : [Suppression / Generalisation / k-Anonymity / Synthetic / etc.]
  Fields Treated   : [List each field and treatment applied]

RE-IDENTIFICATION RISK (post-treatment)
  Prosecutor Risk  : [%] — [Pass/Fail]
  Journalist Risk  : [%] — [Pass/Fail]
  Linkage Risk     : [Assessed against: external dataset name] — [Pass/Fail]
  Overall Rating   : [Low / Medium / High]

DPDP APPLICABILITY
  Is output personal data? : [Yes (pseudonymised) / No (anonymised)]
  DPDP obligations remain? : [Yes / No]

INTENDED USE
  Purpose          : [Analytics / Testing / Sharing / Research]
  Recipients       : [Internal / External — specify]

MAPPING TABLE (pseudonymisation only)
  Location         : [Encrypted vault reference]
  Custodian        : [DPO / designated role]
  Destruction date : [If applicable]

DPO SIGN-OFF     : [Name] — [Date]
═══════════════════════════════════════════════════════════════
```

**Output:** Anonymisation Record filed; DPO sign-off obtained.

---

## Technique Selection Guide

```
USE CASE                         RECOMMENDED TECHNIQUE
─────────────────────────────────────────────────────────────
Internal dashboard / reporting → Aggregation + Generalisation
ML model training               → Synthetic Data + Differential Privacy
Software testing                → Data Masking (destroy mapping post-test)
Open data publication           → K-Anonymity + Suppression + Risk Test
Research sharing                → Synthetic Data or K-Anonymity
Audit log de-identification     → Pseudonymisation (key held by DPO)
Long-term data retention        → Pseudonymise early; anonymise at archive
Cross-border sharing (sensitive)→ Anonymise to remove DPDP transfer obligation
```

---

## Related Agents

- `dpdp-dpia-agent.md` — DPIA for anonymisation and pseudonymisation techniques
- `dpdp-audit-compliance-agent.md` — Audit of anonymisation controls and re-identification testing

---

## Penalty Reference

Properly anonymised data falls outside DPDP scope. However, if anonymisation is inadequate and data remains identifiable, full DPDP penalties apply. See `meity-dpdp-privacy-agent.md` — Penalty Reference Table.

---

## Agent Guardrails

- **Never claim** data is anonymised without a documented re-identification risk assessment.
- **Never use** only suppression of direct identifiers — quasi-identifiers remain a risk.
- **Always test** re-identification before sharing outside the organisation.
- **Never store** pseudonymisation mapping table in the same system as pseudonymised data.
- **Always destroy** mapping tables when no longer needed to achieve effective anonymisation.
- **Never assume** aggregated data is anonymous — small groups can reveal individuals.

---

## References

- DPDP Act, 2023 — Section 2(t) (Definition of Personal Data); Section 4 (Grounds for Processing)
- MeITY DPDP Rules, 2025
- ICO Anonymisation Code of Practice (UK) — comparative reference
- Cynthia Dwork — Differential Privacy (foundational paper)
- ISO/IEC 20889 — Privacy-Enhancing Data De-identification
- Article 29 Working Party — Opinion 05/2014 on Anonymisation Techniques
