#!/usr/bin/env python3
"""Generate agent.manifest.yml (the agent index, per AGENT_PROTOCOL.md) from the split.

Sources: spec/ section + component files, the generated §18 taxonomy, and bundler.manifest.yml.
Emits the bundles / sections / enums / components / standard index and verifies the
AGENT_PROTOCOL §6 guarantees.
"""
import re, os, glob

SPEC = "spec"
UI_CORE = {17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
CLEAN = {  # verbose file slugs -> canonical section keywords
    "ambiguity-and-conflict-resolution-rules": "conflict-resolution",
    "linting-rules-for-automated-review": "linting", "recommended-adoption-workflow": "adoption",
    "default-mobile-screen-layout-pattern": "default-layout", "screen-variants-and-inheritance": "variants",
    "spec-to-implementation-traceability": "traceability", "full-example-login-screen": "full-example",
    "minimal-production-template": "template", "import-and-include": "imports", "fragment-file-format": "fragments",
}
EXTRA = {
    "SpeedDial": {"with": ["SpeedDialItem"]}, "ContextMenu": {"with": ["ContextMenuItem"]},
    "TabBar": {"with": ["TabItem"]}, "Drawer": {"with": ["DrawerItem"]},
    "Scanner": {"needs": ["permissions"]}, "MapView": {"needs": ["permissions"]},
    "LocationInput": {"needs": ["permissions"]},
}
PAIRS = {"SpeedDialItem": "SpeedDial", "ContextMenuItem": "ContextMenu", "TabItem": "TabBar", "DrawerItem": "Drawer"}

def keyword(slug):
    return CLEAN.get(slug, re.sub(r"-section(-.*)?$", "", slug))

# taxonomy (name -> meaning) from generated §18
taxonomy = {}
for ln in open(f"{SPEC}/03-screen-sections/18-component-taxonomy.md", encoding="utf-8"):
    m = re.match(r"\|\s*`(\w+)`\s*\|\s*(.*?)\s*\|\s*$", ln)
    if m and m.group(1) != "Type":
        taxonomy[m.group(1)] = m.group(2)

# components with a detail file (+ pair-children share the parent file)
comp_file = {}
for m in re.finditer(r"\{ order: \d+, name: (\w+), category: \w+, file: (\S+) \}",
                     open("bundler.manifest.yml", encoding="utf-8").read()):
    comp_file[m.group(1)] = m.group(2)
for child, parent in PAIRS.items():
    comp_file[child] = comp_file[parent]

# section files -> ui_core / sections / enums
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
        sections[keyword(slug)] = p

version = re.search(r"\*\*Version:\*\* (\S+)", open(f"{SPEC}/_stub.md", encoding="utf-8").read()).group(1)
standard = sorted(set(taxonomy) - set(comp_file))

q = lambda s: '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
out = ["# agent.manifest.yml - generated index (see AGENT_PROTOCOL.md). Read once; load only what you need.",
       f'version: "{version}"', "", "bundles:", "  ui_core:"]
out += [f"    - {p}" for p in ui_core]
out += ["", "sections:"] + [f"  {k}: {p}" for k, p in sorted(sections.items())]
out += ["", f"enums: {enums}", "", "components:"]
for name in sorted(comp_file):
    parts = [f"f: {comp_file[name]}", f"s: {q(taxonomy.get(name, ''))}"]
    parts += [f"{k}: [{', '.join(v)}]" for k, v in EXTRA.get(name, {}).items()]
    out.append(f"  {name}: {{ {', '.join(parts)} }}")
out += ["", "standard: [" + ", ".join(standard) + "]", ""]
open("agent.manifest.yml", "w", encoding="utf-8").write("\n".join(out))

# verify AGENT_PROTOCOL §6
ok = (set(comp_file) | set(standard) == set(taxonomy)
      and all(os.path.exists(f) for f in comp_file.values())
      and all(c in taxonomy for c in comp_file)
      and not any(c in comp_file for c in standard))
print("taxonomy:", len(taxonomy), " with-file:", len(comp_file), " standard:", len(standard),
      " ui_core:", len(ui_core), " sections:", len(sections))
print("AGENT_PROTOCOL §6 guarantees:", "VALID ✅" if ok else "FAIL ❌")
