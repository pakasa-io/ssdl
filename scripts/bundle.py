#!/usr/bin/env python3
"""Bundle the split sources into ssdl.spec.md + agents/agent.manifest.yml.

Reads bundler.manifest.yml + spec/ and:
  - concatenates sections (verbatim) and re-heads each component (`### 19.<order> <title>`),
  - generates the grouped Table of Contents,
  - generates agents/agent.manifest.yml (the agent index),
  - validates the AGENT_PROTOCOL §6 guarantees, incl. §18 taxonomy <-> component-file consistency.

Usage: python3 scripts/bundle.py            (writes ssdl.spec.md + agents/agent.manifest.yml)
       python3 scripts/bundle.py --check    (builds in memory, diffs the on-disk artifacts, exits non-zero on drift)

Run from anywhere: paths resolve against the repo root (this script's parent directory).
"""
import re, os, glob, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))   # scripts/
ROOT = os.path.dirname(HERE)                         # repo root
os.chdir(ROOT)                                       # resolve spec/ + output paths against the repo root

SPEC = "spec"
OUT_SPEC, OUT_AGENT = "ssdl.spec.md", "agents/agent.manifest.yml"

# self-contained skill: the to-ssdl skill carries a vendored snapshot of the spec it consumes,
# so the skill directory works standalone. The snapshot is generated here and drift-checked.
SKILL = "skills/to-ssdl"
VENDOR_FILES = [                                    # (canonical source, vendored copy)
    (OUT_AGENT,                          f"{SKILL}/agent.manifest.yml"),
    ("agents/AGENT_PROTOCOL.md",         f"{SKILL}/AGENT_PROTOCOL.md"),
    ("assets/lint-rules.md",             f"{SKILL}/assets/lint-rules.md"),
    ("assets/completeness-checklist.md", f"{SKILL}/assets/completeness-checklist.md"),
    ("assets/template.minimal.ssdl",     f"{SKILL}/assets/template.minimal.ssdl"),
    ("assets/sample.login.ssdl",         f"{SKILL}/assets/sample.login.ssdl"),
]

# ---------- manifest ----------
man = open(os.path.join(HERE, "bundler.manifest.yml"), encoding="utf-8").read()
STUB = re.search(r'^stub: (\S+)', man, re.M).group(1)
ORDER = re.findall(r'^  - (spec/\S+)$', man, re.M)
COMP = {}  # file -> (order, title)
for o, n, c, t, f in re.findall(
        r'\{ order: (\d+), name: (\w+), category: (\w+), title: "(.*?)", file: (\S+) \}', man):
    COMP[f] = (int(o), t)

# ---------- assemble section body (re-head components) ----------
def emit(f):
    c = open(f, encoding="utf-8").read()
    if f in COMP:
        o, t = COMP[f]
        return f"### 19.{o} {t}\n\n" + c
    return c
BODY = "".join(emit(f) for f in ORDER)
TITLE = {int(m.group(1)): m.group(2) for m in re.finditer(r'(?m)^## (\d+)\. (.+)$', BODY)}

# ---------- TOC (reproduces the in-spec Contents block) ----------
STRUCT = [
    ("I · Introduction", [(None, [0, 1, 2])]),
    ("II · Notation & file anatomy", [(None, [3, 4, 5, 6])]),
    ("III · Screen sections", [
        ("Identity, scope & setup", [7, 8, 9, 10, 11, 12, 13]),
        ("Data & content", [14, 15, 16]),
        ("UI & layout", [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),
        ("State & lifecycle", [31, 32]), ("Motion", [33]),
        ("Logic", [34, 35, 36, 37]), ("Backend & navigation", [38, 39]),
        ("Instrumentation & accessibility", [40, 41, 42]), ("QA & open items", [43, 44]),
    ]),
    ("IV · Reuse & composition", [(None, [45, 46, 47])]),
    ("V · Patterns & reference", [(None, [48, 49, 50, 51, 52, 53, 54])]),
    ("VI · Adoption", [(None, [55, 56, 57, 58])]),
]
def anchor(n, t):
    h = re.sub(r'[^\w\s-]', '', f"{n}. {t}".lower())
    return re.sub(r'\s+', '-', h.strip())
def tline(n):
    return f"- [{n}. {TITLE[n]}](#{anchor(n, TITLE[n])})"
def build_toc():
    toc = []
    for part, groups in STRUCT:
        toc.append(f"**{part}**\n")
        for sub, ids in groups:
            if sub:
                toc.append(f"*{sub}*\n")
            toc.extend(tline(n) for n in ids)
            toc.append("")
    return "## Contents\n\n" + ("\n".join(toc).rstrip() + "\n") + "\n---\n\n"

def build_spec():
    return open(STUB, encoding="utf-8").read() + build_toc() + BODY

# ---------- agent.manifest.yml ----------
UI_CORE = {17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
CLEAN = {"ambiguity-and-conflict-resolution-rules": "conflict-resolution",
         "linting-rules-for-automated-review": "linting", "recommended-adoption-workflow": "adoption",
         "default-mobile-screen-layout-pattern": "default-layout", "screen-variants-and-inheritance": "variants",
         "spec-to-implementation-traceability": "traceability", "full-example-login-screen": "full-example",
         "minimal-production-template": "template", "import-and-include": "imports", "fragment-file-format": "fragments",
         "state": "states"}
EXTRA = {"SpeedDial": {"with": ["SpeedDialItem"]}, "ContextMenu": {"with": ["ContextMenuItem"]},
         "TabBar": {"with": ["TabItem"]}, "Drawer": {"with": ["DrawerItem"]},
         "Scanner": {"needs": ["permissions"]}, "MapView": {"needs": ["permissions"]},
         "LocationInput": {"needs": ["permissions"]}}
PAIRS = {"SpeedDialItem": "SpeedDial", "ContextMenuItem": "ContextMenu", "TabItem": "TabBar", "DrawerItem": "Drawer"}

def taxonomy():
    tax = {}
    for ln in open(f"{SPEC}/03-screen-sections/18-component-taxonomy.md", encoding="utf-8"):
        m = re.match(r"\|\s*`(\w+)`\s*\|\s*(.*?)\s*\|\s*$", ln)
        if m and m.group(1) != "Type":
            tax[m.group(1)] = m.group(2)
    return tax

def build_agent_manifest():
    tax = taxonomy()
    comp_file = {m[0]: m[2] for m in
                 re.findall(r'\{ order: \d+, name: (\w+), category: (\w+), title: ".*?", file: (\S+) \}', man)}
    for child, parent in PAIRS.items():
        comp_file[child] = comp_file[parent]
    ui_core, sections, enums = [], {}, None
    for p in sorted(glob.glob(f"{SPEC}/**/*.md", recursive=True)):
        if "/18-components/" in p:
            continue
        mm = re.match(r"(\d+)-(.+)\.md$", os.path.basename(p))
        if not mm:
            continue
        num, slug = int(mm.group(1)), mm.group(2)
        if num in UI_CORE:
            ui_core.append(p)
        elif num == 51:
            enums = p
        else:
            sections[CLEAN.get(slug, re.sub(r"-section(-.*)?$", "", slug))] = p
    version = re.search(r"\*\*Version:\*\* (\S+)", open(STUB, encoding="utf-8").read()).group(1)
    standard = sorted(set(tax) - set(comp_file))
    q = lambda s: '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    out = ["# agent.manifest.yml - generated index (see AGENT_PROTOCOL.md). Read once; load only what you need.",
           f'version: "{version}"', "", "bundles:", "  ui_core:"]
    out += [f"    - {p}" for p in ui_core]
    out += ["", "sections:"] + [f"  {k}: {p}" for k, p in sorted(sections.items())]
    out += ["", f"enums: {enums}", "", "components:"]
    for name in sorted(comp_file):
        parts = [f"f: {comp_file[name]}", f"s: {q(tax.get(name, ''))}"]
        parts += [f"{k}: [{', '.join(v)}]" for k, v in EXTRA.get(name, {}).items()]
        out.append(f"  {name}: {{ {', '.join(parts)} }}")
    out += ["", "standard: [" + ", ".join(standard) + "]", ""]
    # AGENT_PROTOCOL §6 (incl. §18 taxonomy <-> component files)
    assert set(comp_file) | set(standard) == set(tax), "components ∪ standard != taxonomy"
    assert all(os.path.exists(f) for f in comp_file.values()), "missing component file"
    assert all(c in tax for c in comp_file), "component absent from §18 taxonomy"
    return "\n".join(out)


# ---------- vendored self-contained skill snapshot ----------
def _vendor_pairs():
    spec_files = sorted(p for p in glob.glob(f"{SPEC}/**/*.md", recursive=True) if os.path.isfile(p))
    return [(p, os.path.join(SKILL, p)) for p in spec_files] + VENDOR_FILES

def vendor(check=False):
    """Sync (or, with check=True, verify) the self-contained snapshot under skills/to-ssdl/."""
    pairs = _vendor_pairs()
    if check:
        drift = [dst for src, dst in pairs
                 if not (os.path.exists(dst) and open(src, "rb").read() == open(dst, "rb").read())]
        keep = {os.path.normpath(dst) for _, dst in pairs}
        for v in glob.glob(f"{SKILL}/spec/**/*.md", recursive=True):   # stale vendored files
            if os.path.normpath(v) not in keep:
                drift.append(v + " (stale)")
        return drift
    shutil.rmtree(f"{SKILL}/spec", ignore_errors=True)                 # drop deletions, copy fresh
    for src, dst in pairs:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    return []

if __name__ == "__main__":
    spec, agent = build_spec(), build_agent_manifest()
    if "--check" in sys.argv:
        ok = spec == open(OUT_SPEC, encoding="utf-8").read() and \
             agent == open(OUT_AGENT, encoding="utf-8").read()
        drift = vendor(check=True)
        print("round-trip:  ", "OK ✅" if ok else "DRIFT ❌")
        print("vendored skill:", "OK ✅" if not drift else f"DRIFT ❌ ({len(drift)} file(s))")
        for d in drift[:10]:
            print("   ", d)
        sys.exit(0 if ok and not drift else 1)
    open(OUT_SPEC, "w", encoding="utf-8").write(spec)
    open(OUT_AGENT, "w", encoding="utf-8").write(agent)
    vendor()
    print(f"wrote {OUT_SPEC} + {OUT_AGENT}; vendored spec snapshot -> {SKILL}/")
