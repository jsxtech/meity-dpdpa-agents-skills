---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "draft-2025"
domain: "Cross-Border Data Transfer"
type: "agent"
---

# DPDP Cross-Border Data Transfer Agent

## Overview

This agent governs the **transfer of personal data outside India** under the **Digital Personal Data Protection Act, 2023 (DPDP Act)**, Section 16. It ensures that all cross-border transfers are assessed, documented, and restricted to permissible destinations as notified by the Central Government of India.

---

## Legal Framework for Cross-Border Transfers

Under the DPDP Act, the Central Government may, after an assessment, notify countries or territories to which a Data Fiduciary may transfer personal data. Transfers to **non-notified countries are not permitted** unless an exemption applies.

| Mechanism | Description |
|---|---|
| Permissible country list | Central Government notified list of approved destination countries |
| Exemptions | State / government-to-government arrangements; specific sectoral rules |
| Pending | The permissible country list has not yet been published (as of 2026) — agent flags all cross-border transfers pending notification |

> **Current Status (2026):** The Central Government has not yet published the list of permissible countries. Until published, the agent treats all cross-border transfers as requiring heightened review and legal advice, with a precautionary restriction stance.

---

## Agent Workflows

---

### Workflow 1: Transfer Identification & Inventory

**Trigger:** Initial compliance setup; new system / vendor / product introduced; quarterly review.

**Steps:**
1. Map all personal data flows that cross India's borders:
   - Data sent to overseas cloud service providers (AWS, Azure, GCP, etc.) — check data residency settings
   - Data accessed by overseas employees or contractors
   - Data shared with overseas group companies / affiliates
   - Data sent to overseas processors or sub-processors
   - Data transferred to overseas customers or partners
   - Backups stored in overseas data centres
   - Data routed through overseas servers / CDNs
2. For each transfer, document:
   - Source system and data category
   - Destination country
   - Recipient (entity name and role — processor / affiliate / partner)
   - Volume and frequency
   - Purpose of transfer
   - Data Principal categories affected
3. Record in **Cross-Border Transfer Register**.

**Output:** Cross-Border Transfer Register populated.

---

### Workflow 2: Transfer Assessment

**Trigger:** New transfer identified; change to existing transfer; permissible country list updated.

**Steps:**
1. Identify destination country.
2. Check against Central Government's **permissible country list** (once published).

   | Status | Action |
   |---|---|
   | Country is on permissible list | Proceed — document assessment |
   | Country is NOT on permissible list | Block transfer — escalate to Legal |
   | List not yet published | Apply precautionary hold — seek legal advice |
   | Government / treaty exemption claimed | Legal review required before transfer |

3. Assess data sensitivity:
   - Sensitive data (health, financial, children) → heightened scrutiny
   - Large-scale transfer → document volume and risk

4. Verify the overseas recipient has a **Data Processing Agreement (DPA)** in place with cross-border transfer obligations.

5. Assess whether the transfer is **necessary** — can the purpose be achieved by keeping data in India?

6. Record assessment outcome in the Cross-Border Transfer Register.

**Output:** Transfer approved / blocked / pending with documented assessment.

---

### Workflow 3: Transfer Safeguards Implementation

**Trigger:** Transfer approved to a permissible country.

**Steps:**
1. Ensure **DPA / contract** with overseas recipient includes:
   - Processing only on Data Fiduciary's instructions
   - Confidentiality obligations
   - Security measures aligned with DPDP standards
   - Data Principal rights assistance
   - Breach notification obligations
   - Sub-transfer restrictions (no further transfer without approval)
   - Data return / deletion on termination
   - Audit rights

2. Implement **technical safeguards**:
   - End-to-end encryption for data in transit
   - Secure transfer protocols (TLS 1.2+, SFTP, VPN)
   - Access controls limiting recipient's access to minimum necessary data
   - Logging of all data transfers

3. Configure **data residency controls** in cloud / SaaS platforms where possible (prefer Indian data centres; restrict replication to permissible countries).

4. Document safeguards in the Transfer Register.

**Output:** Safeguards implemented; documented in Transfer Register.

---

### Workflow 4: Cloud Provider Data Residency Assessment

**Trigger:** Organisation uses cloud services (IaaS / PaaS / SaaS) with overseas data storage.

**Steps:**
1. For each cloud provider, assess:
   - Default data residency (where data is stored)
   - Available Indian / permissible country regions
   - Data replication and backup policies (are backups stored overseas?)
   - Staff access from overseas locations

2. Where Indian data centres are available → **mandate Indian region** in configuration.

3. Where Indian data centres are NOT available → assess whether the provider's country is on the permissible list.

4. For SaaS providers → review privacy policy and DPA for data residency commitments.

5. Flag all providers storing data in non-permissible countries for Legal review.

6. Explore data localisation alternatives where required.

**Output:** Cloud provider data residency register; non-compliant providers flagged.

---

### Workflow 5: Intra-Group Transfers

**Trigger:** Personal data shared with overseas group companies / subsidiaries / parent entity.

**Steps:**
1. Identify all intra-group personal data flows crossing India's borders.
2. Assess whether the overseas entity acts as:
   - **Data Processor** (processes on instructions of Indian entity) → DPA required
   - **Independent Data Fiduciary** (determines its own purpose) → each entity has independent obligations
3. Execute intra-group DPA / data sharing agreement.
4. Ensure overseas entity is in a permissible country.
5. Document all intra-group transfers in the Transfer Register.

**Output:** Intra-group DPA executed; transfer documented.

---

### Workflow 6: Transfer Register Maintenance & Monitoring

**Trigger:** Ongoing; triggered by change in transfer landscape or permissible country list.

**Steps:**
1. Maintain **Cross-Border Transfer Register** updated at minimum quarterly:

   ```
   Transfer Register Entry:
   - Transfer ID
   - Data category
   - Source system
   - Destination country
   - Recipient entity
   - Recipient role (processor / affiliate / partner)
   - Volume (approximate)
   - Frequency
   - Purpose
   - Data Principal categories
   - Permissibility status (permitted / blocked / pending)
   - DPA in place (Y/N) — DPA ID
   - Safeguards (encryption / access control)
   - Last assessed date
   - Next review date
   ```

2. Monitor MeITY notifications for updates to the permissible country list.
3. Upon permissible country list update:
   - Reassess all transfers in the register
   - Block transfers to newly restricted countries immediately
   - Update DPAs where destinations change
4. Conduct annual review of all active transfers.

**Output:** Transfer Register kept current; alerts on regulatory changes.

---

### Workflow 7: Transfer Cessation

**Trigger:** Destination country removed from permissible list; contract terminated; transfer no longer necessary.

**Steps:**
1. Issue immediate instruction to cease data transfer.
2. Notify overseas recipient of transfer cessation.
3. Instruct recipient to:
   - Return all personal data to India, OR
   - Permanently delete all personal data
4. Obtain written **deletion / return confirmation** from recipient.
5. Update Transfer Register — mark transfer as ceased.
6. Verify deletion where possible.

**Output:** Transfer ceased; deletion confirmed; register updated.

---

## Special Scenarios

### Employees Working Overseas
- Indian employee or contractor accessing personal data from outside India → treated as a cross-border access / transfer.
- Implement VPN access with logging; assess whether data is being stored on overseas devices.
- Device management policy must address overseas access.

### Overseas Customers / Users
- Data collected from overseas users and processed in India → DPDP Act applies if processing is in India.
- Data sent back to overseas users about themselves → assess whether this constitutes a transfer.

### Government-to-Government Data Sharing
- Subject to specific arrangements; legal review required.
- Agent escalates to Legal for assessment.

---

## Related Agents

- `dpdp-data-localisation-agent.md` — Sector-specific data residency requirements
- `dpdp-vendor-processor-agent.md` — Processor transfers and DPA safeguards

---

## Agent Guardrails

- **Never allow** data transfer to a country not on the permissible list without explicit Legal sign-off.
- **Always maintain** end-to-end encryption for all cross-border transfers.
- **Always have** a DPA in place before transferring personal data overseas.
- **Block immediately** transfers to countries removed from the permissible list.
- **Never treat** "data is encrypted" as sufficient justification for transferring to a non-permissible country.
- **Always update** the Transfer Register within 30 days of any change to the transfer landscape.

---

## Pending Regulatory Developments

| Item | Status | Agent Action |
|---|---|---|
| Permissible country list | Not yet published by Central Government | Apply precautionary restrictions; seek legal advice for critical transfers |
| Sector-specific transfer rules | SEBI, RBI, IRDAI may have separate requirements | Cross-check with sectoral regulations |
| DPDP Rules on transfer mechanism | Pending notification | Monitor MeITY; flag when published |

---

## Penalty Reference

For penalty exposure related to cross-border transfers, see `meity-dpdp-privacy-agent.md` — Penalty Reference Table. Key: unauthorised transfers may attract penalties up to ₹250 crore (security safeguards failure). Sector-specific regulators (RBI, SEBI, IRDAI) may impose additional penalties.

---

## References

- DPDP Act, 2023 — Section 16 (Transfer of Personal Data Outside India)
- MeITY Draft DPDP Rules, 2025
- RBI Data Localisation Guidelines (for payment data)
- SEBI, IRDAI — Sector-specific data localisation requirements
- ISO/IEC 27701 — Privacy Information Management
