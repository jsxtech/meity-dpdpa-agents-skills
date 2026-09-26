---
version: "1.6.0"
last_updated: "2026-09-26"
dpdp_rules_version: "notified-2025"
domain: "Cookie & Tracking Consent"
type: "skill"
---

# DPDP Cookie & Tracking Consent Skill

## Skill Identity

**Skill Name:** dpdp-cookie-tracking
**Domain:** Web/App Tracking, Cookie Consent, SDK Governance, Consent Strings
**Skill Type:** Technical, Operational, Regulatory
**Applicable To:** Web/App Engineers, MarTech, Product, DPO

---

## Skill Purpose

Provide operational patterns for **cookie and tracking consent** under the DPDP consent framework (**Sections 5, 6, 9**) — cookie categorisation, consent banners that avoid dark patterns, SDK/tag governance, consent-string management, and the strict prohibition on tracking or behaviourally monitoring **children** (Section 9(3)). This fills the concrete web/app tracking gap that the conceptual Consent Manager skill does not address.

---

## Skill Capabilities

---

### Capability 1: Cookie & Tracker Inventory

Discover and categorise all cookies, SDKs, pixels, and trackers (strictly necessary, functional, analytics, advertising) with purpose and vendor.

---

### Capability 2: Consent Banner Design (No Dark Patterns)

Design a consent banner with balanced accept/reject options, granular per-category toggles, and no pre-ticked non-essential boxes or manipulative design.

---

### Capability 3: Prior-Consent Enforcement

Ensure non-essential trackers do not fire before consent is captured (block-until-consent), with strictly-necessary cookies exempt.

---

### Capability 4: Consent-String Management

Capture, store, and honour a machine-readable consent string per Data Principal; propagate consent state to tags/SDKs and refresh on change.

---

### Capability 5: SDK & Tag Governance

Govern third-party SDKs/tags: approval, purpose limitation, data-flow review, and removal of non-compliant trackers; flow-down of DPDP obligations to vendors.

---

### Capability 6: Children & Tracking Prohibition

Detect contexts likely to involve children and disable tracking/behavioural monitoring/targeted advertising, per Section 9(3).

---

### Capability 7: Consent Withdrawal & Re-Prompt

Make tracking consent as easy to withdraw as to give; stop tracking on withdrawal and re-prompt only at meaningful moments (avoid consent fatigue).

---

## Quick Commands

| Command | Action |
|---|---|
| `/cookie-inventory` | Discover and categorise cookies, SDKs, and trackers |
| `/cookie-banner` | Design a no-dark-pattern consent banner |
| `/cookie-prior-consent` | Enforce block-until-consent for non-essential trackers |
| `/cookie-string` | Manage machine-readable consent strings |
| `/cookie-sdk-governance` | Govern third-party SDKs and tags |
| `/cookie-children` | Disable tracking for children (S.9(3)) |
| `/cookie-withdraw` | Handle tracking-consent withdrawal and re-prompt |

---

## Related Skills

- `dpdp-consent-manager-skill.md` — Consent artefacts and interoperability
- `dpdp-privacy-by-design-skill.md` — Consent UX and dark-pattern avoidance
- `dpdp-children-data-skill.md` — Children's tracking prohibition

---

## Skill Guardrails

- **Never fire** non-essential trackers before consent is captured.
- **Never use** pre-ticked boxes or dark patterns in consent banners.
- **Never track or behaviourally monitor children** — prohibited under Section 9(3).
- **Always make** withdrawal as easy as giving consent, and stop tracking on withdrawal.
- **Always govern** third-party SDKs with purpose limitation and vendor flow-down.

---

## References

- DPDP Act, 2023 — Sections 5, 6 (notice and consent), Section 9(3) (children tracking prohibition)
- MeITY DPDP Rules, 2025 — Rule 4 (consent management)
