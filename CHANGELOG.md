---
search:
  exclude: true
---

# Changelog

All notable changes to the DPDP Compliance Suite (agents and skills) are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/).

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

## Pending

> **DPDP Rules final notification** — all files will require update when Rules are gazetted. Areas affected include: specific timelines, prescribed formats, DPBI procedural rules, SDF thresholds, Consent Manager registration requirements, cross-border transfer country list, and children's data age verification standards.
