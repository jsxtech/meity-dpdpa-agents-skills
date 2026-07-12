# DPDP Act 2023 — Compliance Suite

!!! warning "DPDP Rules 2025"
    This suite is based on the **enacted DPDP Act 2023** and the **Notified DPDP Rules 2025** (gazetted November 2025). Content has been updated to reflect the final Rules. Timelines, formats, and thresholds derived from the Rules are now statutory. Always consult legal counsel for binding compliance decisions.

Meity DPDPA Agents Skills Workflows Notices by Jaspal 9891156880

A comprehensive collection of AI agents and skills designed to help organisations achieve and maintain compliance with India's **Digital Personal Data Protection Act, 2023**. This suite covers the full compliance lifecycle — from initial assessment and consent management to breach response and regulatory reporting.

## Quick Stats

| Metric | Count |
|---|---|
| Agents | 17 |
| Skills | 17 |
| Agent Workflows | 117 |
| Skill Capabilities | 140 |
| Skill Quick Commands | 144 |

## Getting Started

1. Start with the [Self-Assessment](SELF_ASSESSMENT.md) to score your current compliance posture.
2. Use the [Decision Tree](DECISION_TREE.md) to identify which agents and skills apply to your situation.
3. Use the [Compliance Roadmap Agent](agents/dpdp-compliance-roadmap-agent.md) for a phased implementation plan.
4. Review the [Regulatory Calendar](REGULATORY_CALENDAR.md) for key dates and deadlines.

## Directory Structure

```
├── agents/          # 17 agent definitions (assessment, monitoring, response)
├── skills/          # 17 skill definitions (operational capabilities)
├── examples/        # 7 scenario walkthroughs + 3 sector guides + 6 consent notices + penalty calculator
├── manifest.yaml    # Suite manifest with all agents, skills, and metadata
├── DECISION_TREE.md # Flowchart to select the right agent/skill
├── INTEGRATION.md   # AI system integration guide (system prompt, RAG, routing)
├── REGULATORY_CALENDAR.md
├── CHANGELOG.md
├── mkdocs.yml       # Documentation site configuration
├── SELF_ASSESSMENT.md
├── RULES_TRACKER.md
├── GLOSSARY.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

## Key Files

- [manifest.yaml](manifest.yaml) — Full suite manifest
- [DECISION_TREE.md](DECISION_TREE.md) — Agent/skill selection guide
- [INTEGRATION.md](INTEGRATION.md) — AI system integration guide (system prompt, RAG, routing)
- [ARCHITECTURE.md](ARCHITECTURE.md) — Dependency graphs and suite structure
- [REGULATORY_CALENDAR.md](REGULATORY_CALENDAR.md) — Compliance dates and deadlines
- [RULES_TRACKER.md](RULES_TRACKER.md) — DPDP Rules provision tracker and reconciliation log
- [SELF_ASSESSMENT.md](SELF_ASSESSMENT.md) — 60-question compliance self-assessment
- [GLOSSARY.md](GLOSSARY.md) — DPDP terminology reference
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute and maintain
- [Agents Overview](agents/README.md) | [Skills Overview](skills/README.md)

## Scenario Walkthroughs

- [Startup Launching a Consumer App](examples/scenario-startup-app-launch.md)
- [Bank Designated as SDF](examples/scenario-bank-sdf-designation.md)
- [Data Breach at an E-Commerce Company](examples/scenario-ecommerce-data-breach.md)
- [Cross-Border SaaS Vendor Onboarding](examples/scenario-cross-border-saas-vendor.md)
- [Government Entity Processing Citizen Data](examples/scenario-govt-entity-processing.md)
- [GDPR-to-DPDP Migration](examples/scenario-gdpr-migration.md)
- [Large Employer HR Data Processing](examples/scenario-large-employer-hr.md)

## Sector Guides

- [Fintech & Banking (RBI)](examples/sector-fintech-guide.md)
- [Healthtech & Healthcare](examples/sector-healthtech-guide.md)
- [Edtech & Education](examples/sector-edtech-guide.md)

## Consent Notice Library

Ready-to-use DPDP-compliant consent notice templates:

- [E-Commerce Checkout](examples/consent-notices/ecommerce-checkout.md)
- [Mobile App Onboarding](examples/consent-notices/mobile-app-onboarding.md)
- [Employee HR Data](examples/consent-notices/employee-hr.md)
- [Health Data Collection](examples/consent-notices/health-data.md)
- [Marketing Opt-In](examples/consent-notices/marketing-optin.md)
- [Parental Consent (Children)](examples/consent-notices/parental-consent.md)
- [E-Commerce Checkout (Hindi)](examples/consent-notices/ecommerce-checkout-hindi.md)

## Tools

- [Penalty Exposure Calculator](examples/penalty-exposure-calculator.md)

## Governing Law

This suite is aligned with:

- **Digital Personal Data Protection Act, 2023** (DPDP Act) — the primary statute
- **Ministry of Electronics and Information Technology (MeITY)** — the nodal ministry
- **Data Protection Board of India (DPBI)** — the adjudicatory body established under the Act

## Status

!!! success "DPDP Rules 2025 — Notified"
    The DPDP Rules 2025 were notified by the Central Government on 13 November 2025 and published in the Official Gazette on 14 November 2025. This suite has been updated to reflect the final Rules. Items previously marked with ⚠️ as "pending Rules" have been reconciled against the gazetted text.
