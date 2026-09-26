---
version: "1.6.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Notice Drafting & Localisation"
type: "skill"
---

# DPDP Notice Drafting & Localisation Skill

## Skill Identity

**Skill Name:** dpdp-notice-drafting
**Domain:** Notice Templates, Layered Notices, Plain Language, Multi-Language Localisation
**Skill Type:** Operational, Content, Regulatory
**Applicable To:** Legal, Product, UX Writers, DPO, Localisation Teams

---

## Skill Purpose

Provide ready-to-use **notice templates and drafting patterns** that satisfy **Section 5 and Schedule II** of the DPDP framework — full and layered notices, just-in-time prompts, plain-language patterns, and multi-language localisation into Eighth Schedule languages. This skill supplies the content the Notice & Transparency Agent delivers.

---

## Skill Capabilities

---

### Capability 1: Schedule II Notice Template

A complete notice template populated with every Schedule II element: data collected, purpose, rights-exercise route, withdrawal route, DPBI-complaint route, and contact.

---

### Capability 2: Layered Notice Pattern

Top-layer (short) + full-notice structure for constrained surfaces (mobile, checkout, IoT), keeping the full notice one tap away.

---

### Capability 3: Just-in-Time Notice Snippets

Contextual micro-notices placed at the point of collecting a specific (often sensitive) data item.

---

### Capability 4: Plain-Language Rewriting

Convert legalese into clear, plain language at an accessible reading level, without losing required content.

---

### Capability 5: Multi-Language Localisation

Localise notices into English + requested Eighth Schedule languages, ensuring accurate, equivalent translations (not machine-only) and a language selector.

---

### Capability 6: Child-Appropriate Notice

Age-appropriate notice language and format for services likely used by children (coordinate with Children's Data Skill).

---

### Capability 7: Notice Versioning & Change Log

Version notices with effective dates, maintain a change log, and flag when re-notification/re-consent is required.

---

## Quick Commands

| Command | Action |
|---|---|
| `/notice-template` | Generate a Schedule II-compliant full notice |
| `/notice-layered` | Design a layered (top-layer + full) notice |
| `/notice-jit` | Produce just-in-time notice snippets |
| `/notice-plain` | Rewrite a notice in plain language |
| `/notice-localise` | Localise a notice into Eighth Schedule languages |
| `/notice-child` | Draft a child-appropriate notice |
| `/notice-version` | Version a notice and record the change log |

---

## Related Skills

- `dpdp-consent-manager-skill.md` — Notice linked to consent artefacts
- `dpdp-children-data-skill.md` — Child-appropriate notices
- `dpdp-privacy-by-design-skill.md` — Notice UX and dark-pattern avoidance

---

## Skill Guardrails

- **Always include** every Schedule II element — a partial notice invalidates consent.
- **Never bury** material information in lower layers or use dark patterns.
- **Always provide** the notice before or at the point of collection.
- **Always use** accurate, equivalent translations — not machine-only output for legal notices.

---

## References

- DPDP Act, 2023 — Section 5 (notice)
- MeITY DPDP Rules, 2025 — Schedule II (prescribed notice format)
- Constitution of India — Eighth Schedule (scheduled languages)
