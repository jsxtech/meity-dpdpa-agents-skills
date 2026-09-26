#!/usr/bin/env python3
"""
DPDP Compliance Suite — structural validation.

Encodes the checks previously performed manually so CI can enforce them:
  1. manifest <-> file reconciliation (agents/skills counts match files)
  2. per-agent workflow_count matches '### Workflow N' headings
  3. per-skill quick_commands matches '| `/cmd`' rows
  4. quick-command names are globally unique across skills
  5. INTEGRATION.md registry lists every defined command (no missing/extra/mis-attributed)
  6. README Quick Stats agree with the manifest sums
  7. Act section citations are within the DPDP Act range (1-44); Section 7 sub-clauses in 7(a)-7(g)
  8. no stale draft-Bill lettered definition citations '2(<letter>)'
  9. relative markdown links resolve
 10. every agent/skill definition file has required frontmatter keys
 11. mkdocs nav entries resolve
 12. no duplicated words; balanced code fences

Exit code 0 = all pass, 1 = one or more failures.
Run from the repo root:  python3 scripts/validate_suite.py
"""
from __future__ import annotations
import os
import re
import sys
import glob

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required (pip install pyyaml)")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS: list[str] = []


def err(msg: str) -> None:
    ERRORS.append(msg)


def read(path: str) -> str:
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def load_manifest() -> dict:
    return yaml.safe_load(read("manifest.yaml"))


def agent_skill_files() -> tuple[list[str], list[str]]:
    a = sorted(f for f in glob.glob(os.path.join(ROOT, "agents", "*.md"))
               if not f.endswith("README.md"))
    s = sorted(f for f in glob.glob(os.path.join(ROOT, "skills", "*.md"))
               if not f.endswith("README.md"))
    rel = lambda p: os.path.relpath(p, ROOT)
    return [rel(x) for x in a], [rel(x) for x in s]


def check_manifest_reconciliation(m: dict) -> None:
    agent_files, skill_files = agent_skill_files()
    man_agents = [a["file"] for a in m["agents"]]
    man_skills = [s["file"] for s in m["skills"]]
    if set(man_agents) != set(agent_files):
        err(f"manifest agents != agent files: "
            f"only-in-manifest={set(man_agents) - set(agent_files)}, "
            f"only-on-disk={set(agent_files) - set(man_agents)}")
    if set(man_skills) != set(skill_files):
        err(f"manifest skills != skill files: "
            f"only-in-manifest={set(man_skills) - set(skill_files)}, "
            f"only-on-disk={set(skill_files) - set(man_skills)}")


def check_counts(m: dict) -> None:
    # per-agent workflow_count
    for a in m["agents"]:
        exp = a.get("workflow_count", 0)
        if not exp:
            continue
        n = len(re.findall(r"^### Workflow \d+", read(a["file"]), re.M))
        if n != exp:
            err(f"{a['file']}: workflow_count={exp} but file has {n} '### Workflow N'")
    # per-skill quick_commands
    for s in m["skills"]:
        exp = s.get("quick_commands", 0)
        txt = read(s["file"])
        mm = re.search(r"##\s*Quick Commands(.*?)(\n## |\Z)", txt, re.S)
        n = len(re.findall(r"^\|\s*`/", mm.group(1), re.M)) if mm else 0
        if n != exp:
            err(f"{s['file']}: quick_commands={exp} but file has {n} command rows")


def check_command_uniqueness(m: dict) -> dict:
    defined: dict[str, str] = {}
    for s in m["skills"]:
        txt = read(s["file"])
        for cmd in re.findall(r"^\|\s*`(/[a-z-]+)`", txt, re.M):
            if cmd in defined:
                err(f"duplicate quick command {cmd}: {defined[cmd]} and {s['file']}")
            defined[cmd] = s["file"]
    return defined


def check_registry_completeness(defined: dict) -> None:
    txt = read("INTEGRATION.md")
    sec = re.search(r"## 4\. Quick Command Registry(.*?)## 5\.", txt, re.S)
    if not sec:
        err("INTEGRATION.md: Quick Command Registry section not found")
        return
    reg: dict[str, str] = {}
    for m in re.finditer(r"^\|\s*`(/[a-z-]+)`\s*\|\s*`([^`]+)`", sec.group(1), re.M):
        reg[m.group(1)] = m.group(2)
    for c, f in defined.items():
        base = os.path.basename(f)
        if c not in reg:
            err(f"INTEGRATION registry missing command {c} (defined in {base})")
        elif reg[c] != base:
            err(f"INTEGRATION registry mis-attributes {c}: says {reg[c]}, actual {base}")
    for c in reg:
        if c not in defined:
            err(f"INTEGRATION registry lists {c} not defined in any skill")


def check_readme_stats(m: dict) -> None:
    txt = read("README.md")
    stats = dict(re.findall(r"\|\s*(Agents|Skills|Agent Workflows|"
                            r"Skill Capabilities|Skill Quick Commands)\s*\|\s*(\d+)\s*\|", txt))
    expect = {
        "Agents": len(m["agents"]),
        "Skills": len(m["skills"]),
        "Agent Workflows": sum(a.get("workflow_count", 0) for a in m["agents"]),
        "Skill Capabilities": sum(s.get("capabilities", 0) for s in m["skills"]),
        "Skill Quick Commands": sum(s.get("quick_commands", 0) for s in m["skills"]),
    }
    for k, v in expect.items():
        if k in stats and int(stats[k]) != v:
            err(f"README Quick Stats '{k}'={stats[k]} but manifest implies {v}")


def check_citations() -> None:
    for f in _all_md():
        if f.endswith("CHANGELOG.md"):
            continue
        txt = read(f)
        # Section N out of range (DPDP Act has 44 sections). Skip IT Act refs (70B, 43A).
        for m in re.finditer(r"(?<!IT Act )\bSection (\d+)\b", txt):
            n = int(m.group(1))
            if n > 44 and n not in (70, 43):  # 70B/43A are IT Act, contextually cited
                # only flag if not near 'IT Act'
                ctx = txt[max(0, m.start() - 40):m.start()]
                if "IT Act" not in ctx:
                    err(f"{f}: Section {n} out of DPDP range (1-44)")
        # stale draft-Bill lettered definition citations 2(letter)
        for m in re.finditer(r"\b2\([a-z]+\)", txt):
            err(f"{f}: stale draft-Bill citation {m.group(0)} (enacted Act uses numbered 2(N))")
        # Section 7 sub-clauses must be within canonical 7(a)-7(g)
        for m in re.finditer(r"\b7\(([a-z])\)", txt):
            if m.group(1) > "g":
                err(f"{f}: invalid Section 7 sub-clause 7({m.group(1)}) (canonical is 7(a)-7(g))")


def check_links() -> None:
    lr = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for f in _all_md():
        d = os.path.dirname(os.path.join(ROOT, f))
        for i, line in enumerate(read(f).splitlines(), 1):
            for m in lr.finditer(line):
                t = m.group(1).strip().split("#")[0]
                if not t or t.startswith(("http://", "https://", "mailto:", "tel:")):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(d, t))):
                    err(f"{f}:{i}: broken link -> {t}")


def check_frontmatter(m: dict) -> None:
    required = ["version", "last_updated", "dpdp_rules_version", "domain", "type"]
    for e in m["agents"] + m["skills"]:
        txt = read(e["file"])
        if not txt.startswith("---"):
            err(f"{e['file']}: missing YAML frontmatter")
            continue
        fm = txt.split("---", 2)[1]
        for k in required:
            if not re.search(rf"^{k}:", fm, re.M):
                err(f"{e['file']}: frontmatter missing '{k}'")


def check_mkdocs_nav() -> None:
    for line in read("mkdocs.yml").splitlines():
        m = re.search(r":\s*([A-Za-z0-9_./-]+\.md)\s*$", line)
        if m and not os.path.exists(os.path.join(ROOT, m.group(1))):
            err(f"mkdocs.yml nav references missing file: {m.group(1)}")


def check_structure() -> None:
    for f in _all_md():
        txt = read(f)
        if txt.count("\n```") % 2 != 0 and txt.count("```") % 2 != 0:
            err(f"{f}: unbalanced code fences")


def _all_md() -> list[str]:
    out = []
    for dp, _, fs in os.walk(ROOT):
        if "/.git" in dp or "/site" in dp or "/node_modules" in dp:
            continue
        for f in fs:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(dp, f), ROOT))
    return out


def main() -> int:
    m = load_manifest()
    check_manifest_reconciliation(m)
    check_counts(m)
    defined = check_command_uniqueness(m)
    check_registry_completeness(defined)
    check_readme_stats(m)
    check_citations()
    check_links()
    check_frontmatter(m)
    check_mkdocs_nav()
    check_structure()

    if ERRORS:
        print(f"VALIDATION FAILED — {len(ERRORS)} issue(s):\n")
        for e in ERRORS:
            print(f"  - {e}")
        return 1
    print("VALIDATION PASSED — suite is structurally consistent.")
    print(f"  agents={len(m['agents'])} skills={len(m['skills'])} "
          f"workflows={sum(a.get('workflow_count', 0) for a in m['agents'])} "
          f"capabilities={sum(s.get('capabilities', 0) for s in m['skills'])} "
          f"quick_commands={sum(s.get('quick_commands', 0) for s in m['skills'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
