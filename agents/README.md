# MEITY DPDP Act — Privacy Compliance Agents

## Overview

This folder contains a comprehensive suite of compliance agents for the **Digital Personal Data Protection Act, 2023 (DPDP Act)** enacted by the Ministry of Electronics and Information Technology (MeITY), Government of India.

Each agent covers a specific compliance domain with detailed workflows, checklists, templates, and guardrails.

---

## Agent Index

| # | Agent File | Domain | Who Needs It |
|---|---|---|---|
| 1 | `meity-dpdp-privacy-agent.md` | Master overview — all obligations, rights, penalties | All Data Fiduciaries |
| 2 | `dpdp-consent-management-agent.md` | Consent lifecycle — collection, verification, withdrawal | All Data Fiduciaries |
| 3 | `dpdp-breach-notification-agent.md` | Breach detection, DPBI notification, Data Principal notification | All Data Fiduciaries |
| 4 | `dpdp-rights-request-agent.md` | Data Principal rights — access, correction, erasure, nomination | All Data Fiduciaries |
| 5 | `dpdp-dpia-agent.md` | Data Protection Impact Assessments | All (mandatory for SDFs) |
| 6 | `dpdp-vendor-processor-agent.md` | Vendor onboarding, DPAs, processor audits, offboarding | All Data Fiduciaries |
| 7 | `dpdp-policy-document-generator-agent.md` | Privacy Policy, Consent Notice, Retention Schedule, Grievance Procedure | All Data Fiduciaries |
| 8 | `dpdp-sdf-compliance-agent.md` | SDF-specific obligations — DPO, auditor, DPIA, algorithm accountability | Significant Data Fiduciaries |
| 9 | `dpdp-dpbi-complaint-response-agent.md` | DPBI complaint response, hearings, orders, TDSAT appeals | All Data Fiduciaries |
| 10 | `dpdp-audit-compliance-agent.md` | Internal audit, compliance monitoring, training, privacy by design | All Data Fiduciaries |
| 11 | `dpdp-cross-border-transfer-agent.md` | Cross-border transfer assessment, safeguards, Transfer Register | Data Fiduciaries with overseas transfers |
| 12 | `dpdp-children-data-agent.md` | Children's data — age verification, parental consent, prohibited processing, lifecycle | All (mandatory if serving under-18s) |
| 13 | `dpdp-anonymisation-pseudonymisation-agent.md` | Anonymisation techniques, re-identification testing, synthetic data, pseudonymisation | All Data Fiduciaries |
| 14 | `dpdp-legitimate-use-agent.md` | Section 7 legitimate uses — employment, state function, emergency, legal order, credit | All Data Fiduciaries |
| 15 | `dpdp-regulatory-monitoring-agent.md` | MeITY/DPBI/court monitoring, impact assessment, regulatory alerts, consultation response | DPO, Legal, Compliance |
| 16 | `dpdp-compliance-roadmap-agent.md` | Phased compliance roadmap, maturity model, progress tracking, resource planning | All Data Fiduciaries |
| 17 | `dpdp-data-localisation-agent.md` | Data localisation inventory, RBI/SEBI/IRDAI/DoT rules, cloud residency, cross-border ops | All (critical for regulated sectors) |

---

## Quick Reference — Which Agent for Which Situation?

| Situation | Agent to Use |
|---|---|
| Starting DPDP compliance from scratch | Agent 16 (roadmap) → Agent 1 (master) |
| Launching a new product / feature | Agents 5 (DPIA), 2 (consent), 7 (notices) |
| Data breach occurred | Agent 3 (breach notification) |
| Data Principal sends a rights request | Agent 4 (rights request) |
| Engaging a new vendor | Agent 6 (vendor management) |
| Transferring data outside India | Agents 11 (cross-border), 17 (localisation) |
| Designated as Significant Data Fiduciary | Agent 8 (SDF compliance) |
| DPBI complaint received | Agent 9 (DPBI response) |
| Annual compliance review | Agent 10 (audit) |
| Drafting / updating privacy policy | Agent 7 (policy generator) |
| Processing data of children | Agent 12 (children's data) |
| Anonymising data for analytics / ML | Agent 13 (anonymisation) |
| Processing without consent (employment, emergency) | Agent 14 (legitimate use) |
| Tracking DPDP Rules / DPBI orders | Agent 15 (regulatory monitoring) |
| Building a compliance programme from scratch | Agent 16 (compliance roadmap) |
| Data residency for RBI / SEBI / IRDAI | Agent 17 (data localisation) |

---

## Agent Workflow Interconnections

```
COMPLIANCE PROGRAMME FLOW
─────────────────────────────────────────────────────────────────
Agent 16 (Roadmap) ──► Agent 10 (Audit) ──► All agents
Agent 1 (Master)   ──► Routes to all specialist agents
Agent 2 (Consent)  ──► Agent 4 (Rights), Agent 7 (Policy)
Agent 3 (Breach)   ──► Agent 9 (DPBI), Agent 4 (Rights)
Agent 5 (DPIA)     ──► Agent 6 (Vendor), Agent 8 (SDF)
Agent 11 (Transfer)──► Agent 17 (Localisation), Agent 6 (Vendor)
Agent 12 (Children)──► Agent 2 (Consent), Agent 5 (DPIA)
Agent 13 (Anon.)   ──► Agent 5 (DPIA), Agent 10 (Audit)
Agent 14 (Legit.)  ──► Agent 7 (Policy), Agent 10 (Audit)
Agent 15 (Reg.)    ──► All agents (updates all on rule changes)
─────────────────────────────────────────────────────────────────
```

---

## Governing Law

- **Digital Personal Data Protection Act, 2023** (No. 22 of 2023)
- **MeITY Draft DPDP Rules, 2025** (pending final notification)
- **Regulator:** Data Protection Board of India (DPBI)
- **Ministry:** MeITY — meity.gov.in

---

## Status Note

The DPDP Rules are still being finalised as of 2026. All agents flag areas where specific timelines, formats, or requirements are pending rule notification. Legal counsel should be consulted for final compliance decisions.
