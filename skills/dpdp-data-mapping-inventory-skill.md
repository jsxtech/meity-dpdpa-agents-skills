---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Data Mapping & Inventory"
type: "skill"
---

# DPDP Data Mapping & Inventory Skill

## Skill Identity

**Skill Name:** dpdp-data-mapping-inventory
**Domain:** Personal Data Discovery, Classification & Records of Processing Activities
**Skill Type:** Technical, Compliance, Privacy Engineering
**Applicable To:** DPOs, Data Engineers, IT Teams, Privacy Teams, Compliance Officers

---

## Skill Purpose

Enable organisations to discover, classify, map, and maintain a complete inventory of all personal data they hold and process — a foundational requirement under the DPDP Act before any other compliance obligation can be fulfilled.

---

## Knowledge Base

### Why Data Mapping is DPDP-Critical

Every DPDP obligation depends on knowing what personal data exists:
- **Consent** — you cannot obtain consent without knowing what data you are collecting
- **Purpose limitation** — you cannot enforce purpose limits without knowing where data flows
- **Retention** — you cannot delete data you cannot find
- **Rights fulfilment** — you cannot respond to access / erasure requests without a data map
- **Breach notification** — you cannot assess breach scope without knowing what data was affected
- **Vendor management** — you cannot manage processors without knowing what data they receive
- **DPDP Audit** — the Records of Processing Activities (RoPA) is the primary audit artefact

---

### Data Classification Framework

```
TIER 1 — SENSITIVE PERSONAL DATA (highest protection)
  • Health and medical data
  • Financial data (bank accounts, cards, transactions)
  • Biometric data (fingerprint, face, iris, voice)
  • Children's data (under 18)
  • Location data (precise, real-time)
  • National ID numbers (Aadhaar, PAN, Passport)
  • Sexual orientation / gender identity
  • Religious / political beliefs / caste

TIER 2 — PERSONAL DATA (standard protection)
  • Name, address, email, phone
  • Date of birth / age
  • IP address / device identifiers
  • Employment details
  • Education records
  • Purchase history / preferences

TIER 3 — PSEUDONYMISED DATA (reduced risk, still personal data)
  • Data that can be re-identified with a key or additional information
  • Hashed identifiers linked to personal data records

TIER 4 — ANONYMISED DATA (not personal data — DPDP does not apply)
  • Data from which identity cannot be reasonably re-established
  • Aggregated statistics with no individual-level data
```

---

## Skill Capabilities

---

### Capability 1: Personal Data Discovery

**Trigger:** "find all personal data", "what data do we hold", "data discovery", "personal data inventory"

**Steps:**
1. Define discovery scope (systems, departments, geographies).
2. Identify all data stores:
   - Structured: databases, data warehouses, CRMs, ERPs, HRMSs
   - Semi-structured: spreadsheets, CSV files, JSON/XML data feeds
   - Unstructured: emails, documents, chat logs, scanned forms
   - Cloud: SaaS platforms, cloud storage buckets, analytics tools
   - Physical: paper records, printed reports
3. For each data store, identify:
   - Owner / custodian (team responsible)
   - Location (system name, server, cloud region)
   - Data categories present
   - Estimated record volume
   - Access controls in place
4. Flag **shadow IT** — personal data held outside approved systems.
5. Compile discovery findings into Data Store Register.

**Output:** Data Store Register; shadow IT findings; discovery report.

---

### Capability 2: Personal Data Classification

**Trigger:** "classify our data", "data classification", "sensitive data identification", "what is sensitive data under DPDP"

**Steps:**
1. For each data element discovered, assign:
   - **Data Category** (name / contact / financial / health / biometric / children / etc.)
   - **Tier** (1 Sensitive / 2 Personal / 3 Pseudonymised / 4 Anonymised)
   - **DPDP Applicability** (Y/N)
2. Flag all Tier 1 Sensitive data for enhanced controls:
   - Encryption at rest and in transit (mandatory)
   - Strict access control (need-to-know only)
   - Separate consent for processing
   - Enhanced retention controls
3. Flag all children's data (under 18) — parental consent required.
4. Document classification decisions in Data Classification Register.

**Output:** Data Classification Register; Tier 1 data flagged for enhanced controls.

---

### Capability 3: Data Flow Mapping

**Trigger:** "map data flows", "where does data go", "data flow diagram", "personal data flows"

**Steps:**
1. For each processing activity, trace personal data through its full lifecycle:

   ```
   COLLECTION → STORAGE → PROCESSING → SHARING → RETENTION → DELETION
   ```

2. Map:
   - **Source** — how is data collected (form, API, purchase, third party)?
   - **Input systems** — where is data first stored?
   - **Processing systems** — what systems transform or analyse data?
   - **Output / sharing** — who receives data (internal teams, processors, third parties)?
   - **Cross-border flows** — does data leave India?
   - **Deletion point** — where and how is data deleted at end of retention?

3. Produce **Data Flow Diagram (DFD)** per processing activity.
4. Identify all **data transfer points** — flag any without DPAs.
5. Identify **data silos** — data held without a clear processing purpose.

**Output:** Data Flow Diagrams; transfer points with DPA status; data silos flagged.

---

### Capability 4: Records of Processing Activities (RoPA) Creation

**Trigger:** "create RoPA", "records of processing activities", "processing register", "document our processing"

**Steps:**
1. For each identified processing activity, create a RoPA entry:

```
ROPA ENTRY TEMPLATE
═══════════════════════════════════════════════════════════
Processing Activity ID  : [PA-XXX]
Activity Name           : [e.g., Customer Account Management]
Department / Owner      : [e.g., Product Team]
Activity Description    : [Brief description]

DATA PRINCIPALS
  Categories            : [e.g., Registered customers, prospects]

PERSONAL DATA
  Categories            : [e.g., Name, email, phone, purchase history]
  Tier Classification   : [1-Sensitive / 2-Personal]
  Estimated Volume      : [e.g., 2 million records]

PURPOSE OF PROCESSING
  Primary Purpose       : [e.g., Order fulfilment]
  Secondary Purposes    : [e.g., Customer support, fraud prevention]

LEGAL BASIS
  Basis                 : [Consent / Legitimate Use — specify]
  Consent Reference     : [Consent form / version]

DATA SOURCES
  Source                : [Direct from user / Third party / Generated]

SYSTEMS INVOLVED
  Primary System        : [e.g., CRM — Salesforce India]
  Secondary Systems     : [e.g., Data Warehouse, Analytics]

RECIPIENTS / SHARING
  Internal              : [Teams with access]
  Processors            : [Vendor name — purpose — DPA ref]
  Third Parties         : [Name — purpose — legal basis for sharing]

CROSS-BORDER TRANSFERS
  Transfer?             : [Y/N]
  Destination           : [Country]
  Safeguards            : [DPA / Permissibility status]

RETENTION
  Retention Period      : [e.g., 7 years from last transaction]
  Retention Basis       : [Legal / Contractual / Consent]
  Deletion Method       : [Secure wipe / Auto-purge]

SECURITY MEASURES
  Controls              : [Encryption / RBAC / Audit logging]

DPIA
  Required?             : [Y/N]
  DPIA ID               : [If conducted]

Last Updated            : [Date]
RoPA Owner              : [Name]
═══════════════════════════════════════════════════════════
```

2. Compile all RoPA entries into the master RoPA document.
3. Review with DPO for completeness and accuracy.
4. Schedule quarterly RoPA updates.

**Output:** Complete RoPA document; DPO-reviewed; quarterly update scheduled.

---

### Capability 5: Data Minimisation Assessment

**Trigger:** "are we collecting too much data", "data minimisation", "unnecessary data", "reduce data collection"

**Steps:**
1. For each data element in the inventory, ask:
   - Is this data element **necessary** for the stated purpose?
   - Can the purpose be achieved **without** this data element?
   - Can this data be **anonymised or pseudonymised** to reduce risk?
   - Is this data **actually used** or just collected "in case"?
2. Flag unnecessary data elements — recommend removal from collection.
3. Identify data elements that can be **anonymised** after a short processing window.
4. Identify data elements that can be **pseudonymised** to reduce risk while preserving utility.
5. Generate Data Minimisation Recommendations Report.

**Output:** Data minimisation report; unnecessary fields flagged; anonymisation opportunities identified.

---

### Capability 6: Retention & Deletion Mapping

**Trigger:** "data retention mapping", "when should data be deleted", "retention periods", "expired data"

**Steps:**
1. For each data category in the inventory, determine retention period:

   | Retention Basis | Source |
   |---|---|
   | Legal requirement | Income Tax Act, Companies Act, IT Act, sector regulations |
   | Contractual obligation | Contract terms with customer / partner |
   | Consent-based | Until consent withdrawn or purpose fulfilled |
   | Legitimate use | Until purpose is fulfilled |

2. Map retention periods to data stores and systems.
3. Identify data that **has already exceeded** its retention period → flag for immediate deletion.
4. Identify data for which **no retention period is defined** → flag as gap.
5. Verify deletion mechanisms exist in each system:
   - Automated deletion / scheduled purge
   - Manual deletion procedure
   - Archiving + deletion workflow
6. Generate Retention Mapping Report with gap analysis.

**Output:** Retention mapping; expired data flagged; deletion mechanism gaps identified.

---

### Capability 7: RoPA Maintenance & Change Management

**Trigger:** "update RoPA", "new processing activity", "RoPA review", "processing activity changed"

**Steps:**
1. Trigger RoPA update when:
   - New processing activity is introduced
   - Existing activity changes materially (new data, new purpose, new processor)
   - Quarterly scheduled review
   - Post-audit finding
2. Update the relevant RoPA entry.
3. Version-stamp the RoPA with update date.
4. Notify DPO of material changes.
5. Assess whether the change requires:
   - Fresh consent from Data Principals
   - Updated privacy notice
   - New or updated DPIA
   - New or updated DPA with processors

**Output:** Updated RoPA; DPO notified; downstream actions triggered.

---

## Data Inventory Master Schema

```
DATA INVENTORY
├── Data Store Register
│     ├── Store ID, Name, Type, Owner, Location, Access Controls
│     └── Data Categories Present, Record Volume
│
├── Data Classification Register
│     ├── Data Element, Category, Tier (1-4)
│     └── DPDP Applicability, Enhanced Controls Required
│
├── Data Flow Diagrams
│     └── [One per processing activity]
│
├── Records of Processing Activities (RoPA)
│     └── [One entry per processing activity]
│
└── Retention Schedule
      └── [Data Category → Retention Period → Deletion Method]
```

---

## Related Skills

- `dpdp-privacy-by-design-skill.md` — Data flow design
- `dpdp-audit-checklist-skill.md` — Audit evidence
- `dpdp-privacy-risk-management-skill.md` — Risk from data inventory

---

## Skill Guardrails

- **Never assume** that anonymised data is safe without verifying re-identification risk.
- **Always flag** children's data (Tier 1) for parental consent verification.
- **Always link** RoPA entries to DPIAs, DPAs, and consent records.
- **Never allow** a new processing activity to go live without a RoPA entry.
- **Always escalate** discovery of personal data in unapproved or shadow systems.

---

## Quick Commands

| Command | Action |
|---|---|
| `/data-discovery` | Run personal data discovery across systems |
| `/data-classify` | Classify data elements by tier and sensitivity |
| `/data-flow-map` | Map data flows for a processing activity |
| `/create-ropa` | Create or update Records of Processing Activities |
| `/data-minimisation` | Assess data collection for necessity |
| `/retention-map` | Map retention periods and flag expired data |
| `/ropa-update` | Trigger RoPA update for a changed activity |

---

## References

- DPDP Act, 2023 — Sections 4, 5, 8
- MeITY Draft DPDP Rules, 2025
- ISO/IEC 27701 — Privacy Information Management (Annex B — RoPA)
- ISO/IEC 29101 — Privacy Architecture Framework
