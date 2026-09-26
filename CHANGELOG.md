---
search:
  exclude: true
---

# Changelog

All notable changes to the DPDP Compliance Suite (agents and skills) are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/).

---

## [Unreleased]

### Added
- **Suite validation script** (`scripts/validate_suite.py`) — enforces the structural checks previously done by hand: manifest↔file reconciliation, per-agent workflow counts, per-skill quick-command counts, global command-name uniqueness, INTEGRATION registry completeness, README stat agreement, Act section-range and Section 7 sub-clause validity, stale draft-Bill citation detection, relative-link integrity, frontmatter completeness, and mkdocs nav resolution.
- **CI workflow** (`.github/workflows/validate.yml`) — runs the validation script, cspell, a lychee link check, and the toolkit pytest suite on every push and pull request to `main`.
- **Executable toolkit** (`toolkit/`) — `dpdp-toolkit` Python package with a `dpdp` CLI and pytest suite implementing the documented decision engines (breach severity per Rule 7(3); weighted compliance scoring). Tests assert the engines reproduce the worked examples in the markdown, preventing docs↔code drift.

---

## [v1.7.0] — 2026-09-26

### Added
- **New agent — Grievance & DSAR Metrics Agent** (`agents/dpdp-dsar-metrics-agent.md`): operational metrics and reporting for rights requests and grievances — volume, 30-day SLA adherence (Rule 10(2)), backlog, escalation, and board/DPBI reporting. 5 workflows. Agents 25 → 26; workflows 160 → 165.
- **New skill — Intra-Group Transfer** (`skills/dpdp-intra-group-transfer-skill.md`): group-company data sharing, intra-group agreements, controller/processor role mapping, and the Section 16 cross-border overlay (no group exemption).
- **New skill — RoPA Generator** (`skills/dpdp-ropa-generator-skill.md`): Records of Processing Activities field schema, generation from the data inventory, lawful-basis and retention linkage, and DPBI-ready export.
- Skills 24 → 26; capabilities 189 → 203; quick commands 198 → 212 (+14).

### Changed
- `manifest.yaml` bumped to 1.7.0; `README.md`, `agents/README.md`, `skills/README.md`, `ARCHITECTURE.md`, `DECISION_TREE.md`, `INTEGRATION.md`, and `mkdocs.yml` reconciled for the new agent and skills.

---

## [v1.6.0] — 2026-09-26

### Added
- **Three new agents** (22 → 25 agents; workflows 145 → 160):
  - **Notice & Transparency Agent** (`agents/dpdp-notice-transparency-agent.md`) — Section 5 / Schedule II notices, layered & just-in-time notices, multi-language delivery, versioning. 5 workflows.
  - **Employee & HR Data Agent** (`agents/dpdp-employee-hr-data-agent.md`) — employee data lifecycle (recruitment→employment→exit), S.7(i) basis, monitoring, exit data. 5 workflows.
  - **Automated Decision-Making & Profiling Agent** (`agents/dpdp-adm-profiling-agent.md`) — ADM transparency, contestability, DPIA linkage, children's profiling prohibition (S.9(3)), SDF algorithmic audit (Rule 13(5)). 5 workflows.
- **Three new skills** (21 → 24 skills; capabilities 168 → 189; quick commands 177 → 198, +21):
  - **Notice Drafting & Localisation Skill** (`skills/dpdp-notice-drafting-skill.md`) — Schedule II templates, layered/just-in-time notices, plain language, Eighth Schedule localisation.
  - **Data Subject Verification Skill** (`skills/dpdp-identity-verification-skill.md`) — proportionate requester verification, anti-fraud, nominee/guardian checks, data minimisation.
  - **Cookie & Tracking Consent Skill** (`skills/dpdp-cookie-tracking-skill.md`) — cookie/tracker inventory, no-dark-pattern banners, prior-consent enforcement, SDK governance, consent strings, children tracking ban.

### Changed
- `manifest.yaml` bumped to 1.6.0 with 3 agent and 3 skill entries added.
- `README.md`, `agents/README.md`, `skills/README.md`, `ARCHITECTURE.md`, `DECISION_TREE.md`, `INTEGRATION.md`, and `mkdocs.yml` updated for the new agents/skills, routing, command registry (+21), graph nodes/edges, and decision branches.

---

## [v1.5.0] — 2026-09-26

### Added
- **Four new agents** (17 → 22 agents; workflows 124 → 145):
  - **Data Retention & Erasure Agent** (`agents/dpdp-retention-erasure-agent.md`) — purpose-based retention (Rule 8), erasure execution across systems/processors, legal hold, backup deletion. 6 workflows.
  - **Nomination & Deceased-Data Agent** (`agents/dpdp-nomination-agent.md`) — Section 14 right to nominate; deceased/incapacitated Data Principal handling. 5 workflows.
  - **Grievance Redressal Agent** (`agents/dpdp-grievance-redressal-agent.md`) — Section 13 / Rule 10(2) grievance mechanism, 30-day SLA, DPBI handoff. 5 workflows.
  - **Consent Renewal & Lifecycle Agent** (`agents/dpdp-consent-renewal-agent.md`) — renewal, re-consent on purpose change, expiry, child-to-adult transition. 5 workflows.
- **Four new skills** (17 → 21 skills; capabilities 140 → 168; quick commands 149 → 177, +28):
  - **Data Retention Schedule Skill** (`skills/dpdp-retention-schedule-skill.md`) — retention templates, deletion workflows, legal hold, backup erasure.
  - **Vendor Risk Assessment Skill** (`skills/dpdp-vendor-risk-skill.md`) — risk tiering, due-diligence questionnaires, scoring rubric, sub-processor assessment.
  - **DPDP for Startups & MSMEs Skill** (`skills/dpdp-startup-msme-skill.md`) — lean/minimum-viable compliance, founder-DPO model, Rule 23 exemption watch.
  - **Data Breach Forensics & Evidence Skill** (`skills/dpdp-breach-forensics-skill.md`) — evidence preservation, chain of custody, root-cause analysis, DPBI-ready reporting.

### Changed
- `manifest.yaml` bumped to 1.5.0 with 4 agent and 4 skill entries added.
- `README.md`, `agents/README.md`, `skills/README.md`, `ARCHITECTURE.md`, `DECISION_TREE.md`, `INTEGRATION.md`, and `mkdocs.yml` updated for the new agents/skills, routing, command registry (+28), graph nodes/edges, and decision branches.
- Corrected the drifted capability-count table in `skills/README.md` (was 139/142) to match the manifest (now 168 capabilities / 177 commands).

---

## [v1.4.0] — 2026-09-26

### Added
- **New agent — Rules Reconciliation Agent** (`agents/dpdp-rules-reconciliation-agent.md`): per-provision gap assessment against the notified DPDP Rules 2025, with 7 workflows (intake, per-Rule gap mapping, pending-item watch for Rules 14/23, evidence validation, report generation, remediation routing, re-assessment). Suite agent count 17 → 18; agent workflows 117 → 124.
- **Breach Severity & Notification Decision Engine** (`examples/breach-severity-decision-engine.md`): deterministic scoring of a breach against the Rule 7(3) severity framework → severity tier (S1–S4), DPBI/CERT-In/Data Principal notification decisions, machine-readable rule set, worked examples. Wired into the Breach Notification Agent (Workflow 2) and the Incident Response skill (new `/ir-severity` command).
- **Compliance Scoring Engine** (`examples/compliance-scoring-engine.md`): unifies the 60-question Self-Assessment and the 159-control Audit Checklist into a weighted 0–100 score with 5 maturity levels and risk-adjusted remediation priorities. Linked from `SELF_ASSESSMENT.md` and the Audit Checklist skill (new `/audit-score` command).
- **Consent Manager skill — interoperability deep-dive**: new "Interoperability & Artefact Reference (Rule 4(4))" section with an API contract, consent-request/response JSON, withdrawal-propagation sequence, status-callback contract, and artefact validation rules. Three new commands: `/cm-artefact`, `/cm-interop`, `/cm-withdraw-flow`.

### Changed
- Skill quick commands 144 → 149 (consent-manager 7→10, incident-response 9→10, audit-checklist 14→15).
- `manifest.yaml` bumped to 1.4.0; new agent entry added; skill `quick_commands` counts updated.
- `README.md`, `agents/README.md`, `INTEGRATION.md` (incl. corrected count 142 → 149), `ARCHITECTURE.md`, `DECISION_TREE.md`, and `mkdocs.yml` updated to include the new agent, the two decision engines, and the five new commands.

---

## [v1.3.2] — 2026-07-12

### Fixed
- **DPDP Rules 2025 — status updated**: `dpdp_rules_version` changed from `draft-2025` to `notified-2025` across all 36 files; "pending" language replaced with "gazetted November 2025"
- **Penalty amounts corrected** (15 errors across 10 files):
  - `penalty-exposure-calculator.md`: Consent/purpose violation ₹250cr→₹50cr; processor obligation ₹250cr→₹50cr
  - `scenario-large-employer-hr.md`: All 5 risk penalties corrected to ₹50cr (Other provisions); retention row clarified
  - `scenario-startup-app-launch.md`: Payment data transfer ₹250cr→₹50cr (S.16)
  - `scenario-cross-border-saas-vendor.md`: Transfer to non-permissible country ₹250cr→₹50cr
  - `scenario-govt-entity-processing.md`: S.17 exemption ₹150cr→₹50cr; purpose limitation ₹200cr→₹50cr
  - `scenario-gdpr-migration.md`: Legitimate interest, transfer, grievance, DPA penalties all corrected to ₹50cr
  - `sector-fintech-guide.md`: Data outside India, consent, and erasure corrected to ₹50cr
  - `sector-healthtech-guide.md`: Health data consent, research sharing, and erasure corrected to ₹50cr
  - `sector-edtech-guide.md`: Erasure penalty ₹250cr→₹50cr
  - `data-localisation-agent.md`: Transfer penalty caveated (₹50cr per se; ₹250cr only if security safeguard failure)
- **GLOSSARY.md**: Data Processor section reference 2(7)→2(8); Digital Personal Data 2(8)→2(9); resolved duplicate
- **Consent Management Agent**: Removed "research/archiving" from legitimate uses (not a S.7 ground); replaced with "voluntary provision" + S.17 clarifying note
- **Anonymisation Agent**: References section — Personal Data definition corrected from "Section 4" to "Section 2(t)"
- **mkdocs.yml**: Duplicate INTEGRATION.md nav entry removed; empty `site_url` replaced with placeholder
- **README.md**: Agent Workflows count 129→117; `.github/` removed from directory structure; Quick Stats updated
- **CONTRIBUTING.md**: Filename example corrected (`dpdp-consent-management-skill.md` → `dpdp-consent-manager-skill.md`)

### Added
- **Incident Response skill** — Capability 6A: CERT-In 6-Hour Notification (legal basis, incident types, steps, comparison table, `/ir-certin` quick command)
- **Incident Response skill** — CERT-In 6-hour row added to SLA summary table
- **Audit Checklist skill** — `/audit-quality` quick command added for Domain 5 (Data Quality & Accuracy)
- **Penalty calculator** — Cross-border transfer violation row added (₹50cr); explanatory note on ₹250cr head

### Changed
- **RULES_TRACKER.md**: Rewritten from forward-looking "pending" tracker to retrospective reconciliation log (20/24 provisions reconciled, 2 partially, 2 pending subordinate notifications)
- **REGULATORY_CALENDAR.md**: DPDP Rules (13 Nov 2025) and DPBI constitution marked ✅ Completed
- **Master Agent & Skill**: Guardrails updated from "flag pending rules" to "verify against gazetted text"
- **Incident Response SLA table**: DPBI row marked with ⚠️; 72-hour timeline now cited as DPDP Rules 2025 (statutory)
- **manifest.yaml**: Incident Response capabilities 8→9, quick_commands 8→9; Audit Checklist quick_commands 13→14
- **README Quick Stats**: Skill Capabilities 139→140, Quick Commands 142→144

---

## [v1.3.1] — 2026-04-30

### Added
- Spell-check CI job with cspell and custom DPDP dictionary (39 terms in .cspell.json)
- External link validation CI job with lychee (excludes not-yet-live govt domains, runs on PRs)
- Hindi consent notice template (ecommerce-checkout-hindi.md)
- Mermaid routing flowchart in INTEGRATION.md (visual agent routing diagram)
- Version banner (admonition) on README noting pending DPDP Rules status
- Search exclusion for CHANGELOG and CODE_OF_CONDUCT (reduces search noise)
- mkdocs.yml: tags plugin, improved search separator config

---

## [v1.3] — 2026-04-30

### Added
- **LICENSE** — CC BY-SA 4.0
- **.gitignore** — mkdocs output, Python, OS, editor files
- **INTEGRATION.md** — AI system integration guide with system prompt template, RAG chunking strategy, agent routing config (YAML), unified quick command registry (142 commands), and deployment checklist
- **CODE_OF_CONDUCT.md** — Contributor Covenant v2.1
- **3 new scenarios**: Government Entity Processing (S.7 legitimate use), GDPR-to-DPDP Migration (multinational gap analysis), Large Employer HR Data (50K employees, S.7(f))
- **Compliance Roadmap Agent**: Workflow 6 (Maturity Assessment) and Workflow 7 (Board Compliance Reporting); capabilities 5→7
- **Sector guides**: Common Pitfalls and Regulator-Specific Timelines sections added to all 3 guides (fintech, healthtech, edtech)
- **manifest.yaml**: Enriched with `tags`, `act_sections`, `priority` (1–4), and `workflow_count` for all 34 entries
- **CI**: Enhanced workflow with link-check, mkdocs build, count validation, manifest validation, and PR trigger
- **mkdocs.yml**: Production-ready with plugins, copyright, navigation.top, search.highlight, new nav entries

### Changed
- All 34 agent/skill frontmatter updated to version 1.2 / 2026-04-30
- Policy Document Generator Agent: `## Workflow` headings normalised to `### Workflow` under `## Agent Workflows` parent
- CONTRIBUTING.md: Added local dev setup, scenario/sector guide contribution guides, structural outlier documentation, expanded naming conventions
- README.md: Updated directory structure, added 3 new scenario links, added INTEGRATION.md and CODE_OF_CONDUCT.md references

---

## [v1.2.1] — 2026-04-30

### Fixed
- DPBI Complaint Response Agent: Chapter III→V (S.18–26) for DPBI establishment; References section corrected with accurate chapter breakdown (Ch V, VI, VII, VIII)
- Section 2 sub-clause format: GLOSSARY Consent Manager 2(3)→2(7), Vendor Agent 2(k)→2(8), Consent Manager Skill 2(g)→2(7) — DPDP Act uses numbered sub-clauses, not lettered
- skills/README.md: Total counts corrected to 139 capabilities / 142 commands (was ~130/~132)
- Master skill (meity-dpdp-privacy-skill.md): Added 6 missing agents to Connected Agents table (now all 17)
- manifest.yaml: Bumped version to 1.2, last_updated to 2026-04-30
- Startup scenario: DPIA flagged as best practice for non-SDFs; all penalty amounts marked ⚠️ maximum per Schedule
- Bank SDF scenario: 30-day DPO and 60-day auditor timelines marked as ⚠️ best-practice targets; all penalties marked ⚠️ maximum per Schedule
- Healthtech guide: Removed second remaining "class-action risk" reference
- Cross-border scenario: Removed second remaining "SCCs" reference

### Added
- All 6 consent notices: DATA RETENTION (S.8(7)) section with context-appropriate retention periods
- All 6 consent notices: YOUR DUTIES AS A DATA PRINCIPAL (S.15) section
- SELF_ASSESSMENT.md: Domain 13 — Enforcement Readiness & Exemptions (5 questions on S.15, S.17, S.29, S.32, Consent Manager); now 60 questions, 120 max score
- RULES_TRACKER.md: 4 new provisions — Voluntary Undertaking (S.32), TDSAT procedures (S.29), Blocking Access (S.36–37), DP duty enforcement (S.15)
- REGULATORY_CALENDAR.md: TDSAT added as monitoring source; status date updated to April 2026
- GLOSSARY.md: 4 new terms — Voluntary Undertaking, Blocking of Access, Data Principal Duties, Exemptions
- DECISION_TREE.md: Policy Document Generator row added to quick reference table
- mkdocs.yml: pymdownx.tasklist extension added for checkbox rendering

---

## [v1.2] — 2026-04-30

### Fixed
- ARCHITECTURE.md: Skill-to-Agent mapping rewritten to reflect actual 17 skills with many-to-many agent relationships (was fictional 1:1 mirrors)
- README.md: Quick Stats corrected — 122 agent workflows, 139 skill capabilities, 142 quick commands (was ~130/~132/97)
- GLOSSARY.md: Consent Manager section reference corrected from Section 9 to Section 7
- DPBI Complaint Response Agent: Chapter reference corrected from "Chapter VI, Sections 27–40" to Chapter V (S.18–26), Chapter VI–VIII (S.27–33)
- Cross-border scenario: Removed GDPR-specific "SCCs" references; replaced with "contractual safeguards" and "DPA"
- Healthtech guide: Removed non-existent S.2(t) health data definition; corrected "explicit consent" to "free, specific, informed consent"; removed "class-action risk" (no class action mechanism in DPDP Act)
- Edtech guide: Removed "registered as Data Fiduciary" language (no registration requirement in the Act)
- Breach scenario: 72-hour notification timeline flagged as best practice pending DPDP Rules (not statutory)
- Breach Notification Agent and Children's Data Agent: 24-hour parent notification marked as ⚠️ best practice recommendation
- Penalty calculator: Added missing violation categories (consent/purpose limitation failure, Data Processor obligation failure)
- Parental consent notice: Added verification mechanism description per S.9 "verifiable consent" requirement
- Health data consent notice: Replaced single bundled checkbox with granular per-purpose consent
- Skill 7 (Penalty): Corrected "Section 40" reference to "Section 36" for blocking access
- Skill 3 (Privacy by Design): Data minimisation reference corrected from "Sec 8" to "Sec 4 / Sec 8"
- CONTRIBUTING.md: Example filename corrected from `dpdp-breach-response-agent.md` to `dpdp-breach-notification-agent.md`
- DECISION_TREE.md: Added skill references to quick reference table; added missing situations (staff training, contract clauses, AI/ML processing)
- freshness.yml: Replaced hardcoded stale-date check with dynamic 6-month calculation
- mkdocs.yml: Added placeholder guidance for site_url
- GLOSSARY.md: Added note that RoPA is an inferred best practice, not an explicit statutory term

---

## [v1.1] — 2025-03-28

### Fixed
- YAML frontmatter added to all agent and skill files
- Agent/Skill Guardrails standardised across all files
- Penalty Reference sections added to all agents
- Related Agents cross-references added to all agents
- Stale data corrected:
  - Maximum penalty clarified to ₹250 crore per instance (highest single-violation cap under DPDP Act Schedule)
  - Audit checklist corrected from "200+ controls" to actual count of 159 controls
  - "Right to be forgotten" terminology corrected to "right to erasure" per DPDP Act
- Best practice assumptions flagged with ⚠️ markers where DPDP Rules are pending
- Policy Document Generator Agent: status column added to document tracking table
- Double horizontal rules (`---`) cleaned up across all files

---

## [v1.0] — 2025-03-28

### Added
- Initial release of **17 agents** and **17 skills** covering full DPDP Act 2023 compliance
- Agents cover: Master overview, Consent, Breach Notification, Rights Request, DPIA, Vendor/Processor, Policy Generator, SDF Compliance, DPBI Complaint Response, Audit, Cross-Border Transfer, Children's Data, Anonymisation/Pseudonymisation, Legitimate Use, Regulatory Monitoring, Compliance Roadmap, Data Localisation
- Skills cover: Master DPDP, Data Mapping, Privacy by Design, Sector-Specific, DPO, Consent Manager, Penalty & Enforcement, Training & Awareness, AI/ML Ethics, Incident Response, Audit Checklist, Privacy Risk Management, Children's Data, Contract Clauses, International Comparison, Legitimate Use, Privacy Programme Management
- README index files for both `/agents/` and `/skills/`

---

## Resolved

> **DPDP Rules 2025 — Notified 13 November 2025.** All files have been reconciled against the gazetted text in v1.3.2. Remaining "pending" items (SDF designations, permissible country list, Consent Manager registrations) are tracked in REGULATORY_CALENDAR.md.
