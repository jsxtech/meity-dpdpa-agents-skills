# dpdp-toolkit

Executable engines that mirror the **documented rulesets** in the DPDP Compliance Suite,
so the decision logic can be computed deterministically (and tested against the worked
examples in the markdown, preventing docs↔code drift).

## Engines

| Engine | Mirrors | Module |
|---|---|---|
| Breach severity | `examples/breach-severity-decision-engine.md` (Rule 7(3)) | `dpdp_toolkit.breach_severity` |
| Compliance scoring | `examples/compliance-scoring-engine.md` | `dpdp_toolkit.scoring` |

## Install (editable)

```bash
cd toolkit
pip install -e ".[test]"
```

## CLI

```bash
dpdp breach-severity --data health --volume 1k-100k \
    --encryption encrypted_keys_exposed --harm high --children
# Severity score : 10  -> Tier S1 (Critical)

dpdp score --domain security_safeguards=40 --domain breach_notification=50 ...
```

## Tests

```bash
cd toolkit && python -m pytest
```

Tests assert each engine reproduces the worked examples documented in the suite
(e.g. breach Example C = 10 → S1; scoring worked example = 66.7 → Defined).

> **Not legal advice.** These engines encode documented decision logic to drive
> consistent triage; the Data Fiduciary remains responsible for final determinations.
