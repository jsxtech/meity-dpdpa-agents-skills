"""dpdp_toolkit — executable engines mirroring the DPDP suite's documented rulesets.

Modules:
  - breach_severity: Rule 7(3) breach severity scoring + notification decisions
  - scoring: weighted compliance scoring (0-100) + maturity bands
"""
from . import breach_severity, scoring

__all__ = ["breach_severity", "scoring"]
__version__ = "0.1.0"
