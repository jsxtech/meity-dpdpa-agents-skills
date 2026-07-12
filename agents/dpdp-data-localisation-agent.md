---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "Data Localisation"
type: "agent"
---

# DPDP Data Localisation Agent

## Overview

This agent manages **data localisation obligations** for organisations operating under the **Digital Personal Data Protection Act, 2023 (DPDP Act)** and sector-specific regulations that mandate personal data to be stored, processed, or mirrored within India. It governs the intersection of DPDP cross-border transfer rules and regulatory data localisation requirements.

---

## Data Localisation Framework in India

India has a layered data localisation landscape — the DPDP Act establishes the baseline, while sector regulators impose additional or stricter requirements:

```
DATA LOCALISATION HIERARCHY
═════════════════════════════════════════════════════════════════
DPDP ACT (baseline):
  Personal data may be transferred only to countries notified
  by the Central Government as permissible.
  Permissible country list: NOT YET PUBLISHED (as of 2026)
  Default stance: Precautionary localisation pending notification

SECTOR-SPECIFIC (additional / stricter):
  RBI    : Payment system data must be stored ONLY in India
            (full localisation, no mirroring abroad)
  RBI    : Financial data — mirroring allowed in approved countries
  SEBI   : Critical data to be stored in India
  IRDAI  : Insurance data — localisation guidance issued
  TRAI   : Telecom subscriber data — confidentiality and storage norms
  NHA    : Health data — India-first approach under ABDM
  DoT    : Subscriber data and CDRs — India storage norms
═════════════════════════════════════════════════════════════════
```

---

## Agent Workflows

---

### Workflow 1: Data Localisation Inventory

**Trigger:** Initial compliance setup; new system deployment; cloud migration.

**Steps:**
1. Inventory all systems storing or processing personal data.
2. For each system, determine:
   - Physical storage location (server/data centre country)
   - Cloud provider and region configuration
   - Data replication and backup locations
   - Disaster recovery site location
   - Data accessed from which geographies (staff, vendors)
3. Map personal data categories to storage location:

   ```
   DATA LOCALISATION INVENTORY
   ─────────────────────────────────────────────────────────────────
   System / Store    | Data Category      | Storage Location | Replication | Compliant?
   ─────────────────────────────────────────────────────────────────
   CRM (Salesforce)  | Customer PII       | US (Oregon)      | None        | ❌ Review needed
   ERP (SAP)         | HR / Payroll data  | India (Mumbai)   | None        | ✅
   Payment gateway   | Payment data       | India (Chennai)  | None        | ✅ (RBI compliant)
   Analytics DB      | Pseudonymised data | Singapore        | India       | 🟡 Assess
   Email system      | Customer comms     | US (Microsoft)   | None        | ❌ Review needed
   Cloud storage     | Contracts/docs     | India (Azure IN) | None        | ✅
   ─────────────────────────────────────────────────────────────────
   ```

4. Flag all systems storing personal data outside India for assessment.
5. Identify sector-specific data subject to stricter localisation rules.

**Output:** Data Localisation Inventory; non-compliant systems flagged.

---

### Workflow 2: Sector-Specific Localisation Assessment

**Trigger:** Organisation operates in a regulated sector.

**RBI Payment Data Localisation:**
```
RULE: All data related to payment systems must be stored ONLY in India.
      Foreign mirroring or processing is prohibited.
      (RBI Circular on Storage of Payment System Data, 2018)

Scope:
  □ Full end-to-end transaction details
  □ Payment instruction information
  □ Payment infrastructure information
  □ Customer data collected for payment purposes

Required Actions:
  □ All payment data must be stored exclusively on India-based servers
  □ No mirroring to foreign servers
  □ Foreign entities may access data in India for processing — but no foreign storage
  □ Annual compliance certificate submitted to RBI

Non-Compliance Risk: RBI regulatory action; payment licence suspension
```

**RBI Financial Data (Non-Payment):**
```
RULE: Financial data may be stored/processed abroad BUT:
      A copy must be maintained in India
      (applicable to Banks, NBFCs, regulated entities)

Scope:
  □ Credit / debit card data (non-payment system data)
  □ Customer financial profiles
  □ Loan data, investment data

Required Actions:
  □ Ensure India copy is always available and current
  □ Cross-border transfer to approved RBI countries only
  □ Document data flows in compliance filing
```

**SEBI Data Localisation:**
```
RULE: Critical data of market participants to be maintained in India.
      (SEBI Cyber Security Circular — periodic updates)

Scope:
  □ Trading data
  □ Investor KYC / account data
  □ Surveillance data
  □ Risk management data

Required Actions:
  □ Primary storage in India
  □ Disaster recovery in India (or RBI-approved country)
  □ Overseas data processing only with SEBI permission
```

**IRDAI Data:**
```
RULE: Policyholder data and insurance records to be maintained in India.
      (IRDAI Guidelines on Information and Cyber Security)

Required Actions:
  □ Policy data, claims data — stored in India
  □ Cross-border processing only with IRDAI compliance
```

**TRAI / DoT Telecom Data:**
```
RULE: Subscriber data, CDRs, and lawful intercept data in India.
      (Unified Licence conditions; DoT directions)

Required Actions:
  □ All subscriber data and CDRs on India-based infrastructure
  □ No foreign access to lawful intercept data
  □ Annual compliance certification to DoT
```

**NHA Digital Health Data:**
```
RULE: Health data under ABDM / ABHA to remain in India.
      (NHA guidelines; DISHA pending)

Required Actions:
  □ ABHA health records hosted in India
  □ HIP/HIU integrations comply with data boundary rules
  □ No cross-border transfer of ABDM-linked health data
```

**Output:** Sector-specific localisation compliance assessment; mandatory actions identified.

---

### Workflow 3: Cloud Provider Data Residency Configuration

**Trigger:** New cloud service deployment; review of existing cloud services.

**Major Cloud Providers — India Regions:**

| Provider | India Regions | Services Available |
|---|---|---|
| AWS | ap-south-1 (Mumbai), ap-south-2 (Hyderabad) | Most services |
| Microsoft Azure | Central India (Pune), South India (Chennai), West India (Mumbai) | Most services |
| Google Cloud | asia-south1 (Mumbai), asia-south2 (Delhi) | Most services |
| Oracle Cloud | India West (Mumbai), India East (Hyderabad) | Most services |

**Configuration Steps:**
1. For each cloud service, review current region configuration.
2. Identify services deployed in non-India regions.
3. For personal data workloads:
   - Migrate to India region where technically feasible
   - Configure **data residency controls** to prevent data leaving India
   - Disable cross-region replication for personal data
   - Configure backups to stay within India
4. For SaaS applications:
   - Review vendor's data residency terms
   - Negotiate India data residency addendum where possible
   - If India residency unavailable → assess DPA + DPDP transfer compliance
5. Document configuration in Data Localisation Inventory.
6. Set up alerts for configuration drift (prevent data leaving India inadvertently).

**Cloud Configuration Checklist:**
```
□ Primary data region: India
□ Backup region: India (or permissible country for non-RBI data)
□ DR region: India (for RBI/payment data — mandatory)
□ Cross-region replication: DISABLED for personal data
□ CDN edge caching of personal data: DISABLED or India-only
□ Multi-tenancy data isolation: Verified — our data stays in our region
□ Staff access from overseas: Documented — access to India-stored data
□ Vendor sub-processors: All data residency confirmed
```

**Output:** Cloud configuration updated; residency controls verified; configuration baseline documented.

---

### Workflow 4: Data Localisation for Cross-Border Business Operations

**Trigger:** Organisation has overseas offices, subsidiaries, or outsourcing.

**Common Scenarios:**

**Scenario A — Overseas Team Accessing India-Stored Data:**
```
Situation: Offshore team (e.g., Philippines, UK, US) accesses CRM with Indian customer data.
DPDP Treatment: Data is accessed from overseas — treated as a cross-border access risk.

Controls:
□ Data remains stored in India — no copy made overseas
□ Access via VPN / Citrix to India environment (data doesn't leave India)
□ Screen-only access — no data download to overseas devices
□ Access logging — all overseas access audited
□ DPA or intra-group agreement covers overseas access team
□ DPDP cross-border assessment: access-only vs storage/processing distinction
```

**Scenario B — Overseas Parent Company Needing Customer Data:**
```
Situation: US parent wants access to Indian subsidiary's customer database.
DPDP Treatment: Cross-border transfer; requires permissible country or DPDP exemption.

Controls:
□ Assess whether US is on permissible country list (pending)
□ Intra-group DPA executed covering transfer
□ Data minimised — share only what parent legitimately needs
□ Purpose limitation — parent cannot use data for own purposes
□ India copy maintained at all times
□ Consider data access in India model (parent accesses India-hosted data)
```

**Scenario C — BPO / KPO Processing Indian Customer Data:**
```
Situation: Outsourced support centre in Sri Lanka processes customer data.
DPDP Treatment: Cross-border transfer to processor.

Controls:
□ Assess whether Sri Lanka is on permissible country list
□ DPA with BPO covering DPDP obligations
□ Consider India-based BPO alternative (avoids transfer entirely)
□ If overseas BPO used — data minimised; no personal data downloads to local devices
□ Regular security audits of BPO
```

**Output:** Cross-border operations assessment; recommended controls; DPA requirements.

---

### Workflow 5: Data Localisation Compliance Monitoring

**Trigger:** Ongoing; triggered by system changes, new vendor deployments, configuration audits.

**Monitoring Controls:**
1. **Monthly:**
   - Cloud billing/configuration review — new services deployed in non-India regions?
   - New vendor onboarding review — any overseas data storage?
   - Alert review — any data leaving India unexpectedly?

2. **Quarterly:**
   - Full Data Localisation Inventory review
   - Cross-border Transfer Register update
   - Configuration drift check on cloud environments
   - Sector regulator compliance certificate due dates

3. **Annually:**
   - Independent audit of data localisation controls
   - RBI/SEBI/IRDAI compliance certifications (as required)
   - DPO sign-off on localisation compliance

**Monitoring Alerts to Configure:**
```
□ Alert: New S3 bucket / Cloud Storage created outside India region
□ Alert: Data replication rule created to overseas region
□ Alert: Large data export to overseas IP range
□ Alert: New SaaS application connected without residency review
□ Alert: Overseas VPN access to personal data systems (log + review)
```

**Output:** Localisation monitoring controls operational; alerts configured; quarterly reviews scheduled.

---

### Workflow 6: Incident — Unauthorised Data Outside India

**Trigger:** Data found stored or processed outside India without authorisation.

**Steps:**
1. Classify severity:
   - Payment/financial data outside India → **P1 Critical** (RBI violation)
   - Other personal data outside India in non-permissible country → **P1 Critical**
   - Personal data in country with strong privacy protections (temporarily) → **P2 High**
2. Immediately stop the data flow / transfer.
3. Assess whether data can be deleted from overseas location.
4. Notify DPO, Legal, CISO immediately.
5. Assess notification obligations:
   - DPBI (if constitutes a breach of DPDP obligations)
   - RBI / SEBI / IRDAI (if sector data was exposed)
   - CERT-In (if security incident involved)
6. Document incident, containment actions, and root cause.
7. Prevent recurrence: configuration controls, staff training, approval process.

**Output:** Incident contained; notifications filed; recurrence prevention implemented.

---

## Data Localisation Compliance Matrix

```
DATA LOCALISATION COMPLIANCE MATRIX
Organisation: _______________   Date: _______________

Data Category        | Regulator | Localisation Rule      | Current Storage | Compliant?
─────────────────────────────────────────────────────────────────────────────────────────
Payment system data  | RBI       | India ONLY             | [Location]      | [Y/N]
Financial data       | RBI       | India copy mandatory   | [Location]      | [Y/N]
Customer PII (gen.)  | DPDP      | Permissible country    | [Location]      | [Y/N/Pending]
Health / ABDM data   | NHA       | India preferred        | [Location]      | [Y/N]
Investor data        | SEBI      | Critical data in India | [Location]      | [Y/N]
Policyholder data    | IRDAI     | India                  | [Location]      | [Y/N]
Subscriber / CDR     | DoT/TRAI  | India                  | [Location]      | [Y/N]
Employee data        | DPDP+Labour| India preferred       | [Location]      | [Y/N]
```

---

## Related Agents

- `dpdp-cross-border-transfer-agent.md` — Transfer assessments and safeguards
- `dpdp-vendor-processor-agent.md` — Processor cloud residency requirements

---

## Penalty Reference

For penalty exposure related to data localisation violations, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Key: transfer violations per se attract penalties up to ₹50 crore under the "Other breaches" head. If a transfer also results in a security safeguard failure (e.g., inadequate protections lead to a breach), the ₹250 crore head may apply. Sector-specific regulators (RBI, SEBI, IRDAI) may impose additional penalties independently.

---

## Agent Guardrails

- **Never migrate** RBI payment system data to an overseas cloud — this is an absolute prohibition.
- **Always obtain** DPO and Legal sign-off before deploying any personal data workload outside India.
- **Always default** to India storage when in doubt — precautionary localisation pending DPDP Rules.
- **Never assume** "data is encrypted" removes the localisation obligation — it does not.
- **Always check** sector-specific localisation rules before relying solely on DPDP.

---

## References

- DPDP Act, 2023 — Section 16 (Transfer of Personal Data Outside India)
- RBI Circular on Storage of Payment System Data, 2018
- RBI Master Direction on IT Framework for NBFC / Banks
- SEBI Cyber Security and Cyber Resilience Circular
- IRDAI Guidelines on Information and Cyber Security
- DoT Unified Licence Conditions
- NHA / ABDM Data Governance Policies
- CERT-In Cyber Incident Reporting Directions, 2022
