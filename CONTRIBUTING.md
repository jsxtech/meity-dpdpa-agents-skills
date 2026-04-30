# Contributing to the DPDP Compliance Suite

---

## Local Development Setup

```bash
# Install mkdocs with Material theme
pip install mkdocs-material

# Serve locally with live reload
mkdocs serve

# Build static site (output in site/)
mkdocs build --strict
```

---

## Adding a New Agent

File naming: `agents/dpdp-[domain]-agent.md`

Required sections:

1. YAML frontmatter (see template below)
2. Overview
3. Agent Workflows (with `### Workflow N:` sub-headings)
4. Related Agents
5. Penalty Reference
6. Agent Guardrails
7. References

Frontmatter template:

```yaml
---
version: "1.2"
last_updated: "YYYY-MM-DD"
dpdp_rules_version: "draft-2025"
domain: "[Domain Name]"
type: "agent"
---
```

**Structural note:** Two agents intentionally deviate from the standard `### Workflow N` pattern:
- `meity-dpdp-privacy-agent.md` (Master Agent) — uses `## Agent Capabilities` with subsections instead of numbered workflows, as it serves as a routing/overview agent.
- `dpdp-policy-document-generator-agent.md` — uses `### Workflow N` under an `## Agent Workflows` parent heading (normalised in v1.2).

---

## Adding a New Skill

File naming: `skills/dpdp-[domain]-skill.md`

Required sections:

1. YAML frontmatter (see template below)
2. Skill Identity
3. Capabilities
4. Quick Commands
5. Related Skills
6. Skill Guardrails
7. References

Frontmatter template:

```yaml
---
version: "1.2"
last_updated: "YYYY-MM-DD"
dpdp_rules_version: "draft-2025"
domain: "[Domain Name]"
type: "skill"
---
```

---

## Adding a New Scenario

File naming: `examples/scenario-[short-description].md`

Required sections (in order):

1. `# Scenario: [Title]`
2. `## Context` — 3-5 sentence description of the organisation and situation
3. `## Agent Sequence` — code block with numbered steps, each referencing an agent
4. `## Key Risks` — table with Risk | Penalty Exposure | Mitigation columns; all penalties marked with ⚠️
5. `## Skills to Use` — bullet list with backtick-quoted skill filenames

After creating the file, add it to `mkdocs.yml` nav under Examples and update `README.md` Scenario Walkthroughs section.

---

## Adding a New Sector Guide

File naming: `examples/sector-[sector]-guide.md`

Required sections:

1. `# DPDP Compliance Guide — [Sector]`
2. `## Regulatory Overlap` — table mapping sector requirements to DPDP sections
3. `## Recommended Agent Sequence` — code block
4. `## Compliance Checklist` — numbered checklist table
5. `## Key Penalty Risks` — table with ⚠️ markers
6. `## Common Pitfalls` — bullet list of sector-specific mistakes
7. `## Regulator-Specific Timelines` — table comparing sector regulator timelines with DPDP

After creating the file, add it to `mkdocs.yml` nav under Sector Guides and update `README.md`.

---

## Updating When DPDP Rules Change

1. Open [RULES_TRACKER.md](RULES_TRACKER.md) and identify the provision that changed.
2. Compare the final Rule text against the "Current Assumption" column.
3. Update every file listed in the "Files to Update" column.
4. Bump the `version` field in the YAML frontmatter of each updated file.
5. Update `manifest.yaml` version and `last_updated`.
6. Add an entry to [CHANGELOG.md](CHANGELOG.md).

---

## Review Checklist

Before submitting a PR, verify:

- [ ] YAML frontmatter is present with `version`, `last_updated`, `dpdp_rules_version`, `domain`, and `type`
- [ ] Agent/skill guardrails section is included
- [ ] Penalty reference section cites the correct Act section and Schedule entry
- [ ] All cross-references to other agents/skills use valid relative paths
- [ ] No stale assumptions — check against [RULES_TRACKER.md](RULES_TRACKER.md)
- [ ] Quick command prefixes follow naming conventions (see below)
- [ ] Workflows/capabilities are numbered and actionable
- [ ] Related agents/skills section lists at least one cross-reference
- [ ] References section cites specific DPDP Act sections
- [ ] CHANGELOG.md is updated with a summary of changes
- [ ] manifest.yaml is updated if adding/modifying agents or skills
- [ ] mkdocs.yml nav is updated if adding new files

---

## Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Agent file | `dpdp-[domain]-agent.md` | `dpdp-breach-notification-agent.md` |
| Skill file | `dpdp-[domain]-skill.md` | `dpdp-consent-management-skill.md` |
| Scenario file | `scenario-[description].md` | `scenario-ecommerce-data-breach.md` |
| Sector guide | `sector-[sector]-guide.md` | `sector-fintech-guide.md` |
| Frontmatter name | `dpdp-[domain]-agent` or `dpdp-[domain]-skill` | `dpdp-cross-border-transfer-agent` |
| Quick command prefix | `/dpdp-[domain]` | `/dpdp-breach notify` |
| Section headings | Title Case, no numbering in heading text | `## Agent Guardrails` |
| Domain names | Lowercase, hyphen-separated | `breach-notification`, `consent-management` |
