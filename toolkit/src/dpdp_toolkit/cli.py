"""Command-line interface for dpdp_toolkit.

Examples:
  dpdp breach-severity --data health --volume 1k-100k \\
      --encryption encrypted_keys_exposed --harm high --children
  dpdp score --domain security_safeguards=40 --domain breach_notification=50 ...
"""
from __future__ import annotations
import argparse
import sys

from . import breach_severity as bs
from . import scoring as sc


def _cmd_breach(args: argparse.Namespace) -> int:
    res = bs.assess(bs.BreachInput(
        data_categories=args.data,
        volume=args.volume,
        encryption_state=args.encryption,
        harm_likelihood=args.harm,
        children_involved=args.children,
        cross_border=args.cross_border,
    ))
    print(f"Severity score : {res.score}")
    print(f"Tier           : {res.tier} ({res.label})")
    print(f"Notify DPBI    : {'YES' if res.notify_dpbi else 'NO'} "
          f"(within {res.dpbi_timeline_hours}h)")
    print(f"Notify Data Principals : {'YES' if res.notify_data_principals else 'NO'} "
          f"— {res.dp_rationale}")
    return 0


def _cmd_score(args: argparse.Namespace) -> int:
    domains: dict[str, float] = {}
    for pair in args.domain:
        if "=" not in pair:
            print(f"error: --domain expects key=value, got {pair!r}", file=sys.stderr)
            return 2
        k, v = pair.split("=", 1)
        domains[k.strip()] = float(v)
    res = sc.score(domains)
    print(f"Weighted score : {res.weighted_score} / 100")
    print(f"Maturity       : {res.maturity}")
    if res.critical_flags:
        print(f"Critical flags : {', '.join(res.critical_flags)}")
    print("Top priorities :")
    for d, p in res.priorities[:3]:
        print(f"  - {d} ({p})")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dpdp", description="DPDP compliance engines")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("breach-severity", help="Assess breach severity (Rule 7(3))")
    b.add_argument("--data", required=True,
                   choices=["basic", "financial", "health", "biometric", "children", "special"])
    b.add_argument("--volume", required=True, choices=["<1k", "1k-100k", "100k-1M", ">1M"])
    b.add_argument("--encryption", required=True,
                   choices=["plaintext", "encrypted_keys_exposed", "encrypted_keys_safe"])
    b.add_argument("--harm", required=True, choices=["none", "low", "medium", "high"])
    b.add_argument("--children", action="store_true")
    b.add_argument("--cross-border", action="store_true")
    b.set_defaults(func=_cmd_breach)

    s = sub.add_parser("score", help="Weighted compliance score")
    s.add_argument("--domain", action="append", default=[], metavar="KEY=VALUE",
                   help="repeatable; normalised 0-100 per domain")
    s.set_defaults(func=_cmd_score)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
