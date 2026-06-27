# SSDL Agent Consumption Protocol

**Status:** draft · **Applies to:** the file-split distribution of the SSDL specification
**Audience:** AI agents (and tooling) that read the spec to generate, review, or lint `.ssdl` screens.

This document is the **contract** between the split spec and its automated consumers. The key words **MUST**,
**MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used as in RFC 2119. The bundler is responsible for
producing artifacts that satisfy the "Build guarantees" (§6); agents are responsible for the "Load protocol" (§4)
and "Agent obligations" (§5).

---

## 1. Artifacts and roles

| Artifact | Role | Source / Generated | Agent reads? |
|----------|------|--------------------|--------------|
| `agent.manifest.yml` | The index — *where to find what* | **Generated** | **Yes — entry point** |
| `s/NN-*.md` | One screen-section's rules (e.g. ROUTE, ANIMATION) | Source | Yes, on demand |
| `c/<category>/*.md` | One component's directive table + A11Y + example | Source | Yes, on demand |
| `s/51-vocabulary.md` | The value-enum catalog (keyboard, autocomplete, zoom…) | Source | Yes, on demand |
| `bundler.manifest.yml` | Assembly order + all metadata | Source | **No — bundler only** |
| `ssdl.spec.md` | The full, numbered, linear spec | **Generated** | Optional (full read only) |

Source files are **pure content** — no front-matter. All metadata lives in `bundler.manifest.yml`; the agent-facing
projection of it is `agent.manifest.yml`.

---

## 2. `agent.manifest.yml` schema

```yaml
bundles:        # name -> file pointer    (a named set to load for a task)
sections:       # keyword -> file pointer (one screen-section's rules)
enums:          # file pointer            (the value-enum catalog)
components:     # Name -> { f: pointer?, s: summary, with: [Name], needs: [keyword] }
standard:       # [Name]                  (valid components with no file; covered by ui_core)
version:        # the spec version this index was generated from
```

`components` ∪ `standard` is the **complete, authoritative set of valid component types**.

---

## 3. File pointers and the `load()` rule

A **file pointer** is either one path (string) or a list of paths (array). Resolution is uniform:

```
load(p) = read p            if p is a string
        = read every path   if p is an array
```

Anywhere a pointer appears (`bundles.*`, `sections.*`, `enums`, `components.*.f`) it MAY be a string or an array, and
MUST be resolved with `load()`.

---

## 4. Load protocol

The rule, compact:

```text
load(p)   = read p if string, else read every path in p
ui task   → load(bundles.ui_core)
component → if has f: load(f);  if has with:/needs: resolve those too;  else (standard) nothing extra
section   → load(sections[name])
```

In full, an agent performing a spec-derived task MUST follow this procedure:

1. **Read `agent.manifest.yml` first.** No spec-derived decision is made before this.
2. **If the task touches UI, layout, or any component:** `load(bundles.ui_core)` **before** interpreting any layout
   directive, standard directive, or component. `ui_core` is the mandatory base for all UI work.
3. **For each component `C` the screen uses:**
   - If `C ∈ components` and has `f:` → `load(C.f)`.
   - Resolve `C.with:` (load each as a component) and `C.needs:` (load each named `sections` entry / `enums`).
   - If `C ∈ standard` → load nothing further; `ui_core` fully covers it.
   - If `C ∉ components ∪ standard` → `C` is **invalid**; do not emit or accept it.
4. **For each screen section being authored or reviewed** (route, permissions, model, validation, animation, api,
   analytics, a11y, errors, …) → `load(sections[keyword])`.
5. **If any loaded file references value enums** → `load(enums)`.
6. **Repeat 3–5 to closure** (until no new file is pulled in by a `with:`/`needs:`/reference).

A component's *effective* documentation is always **`ui_core` + its own file (if any)** — a per-component file is an
addition to `ui_core`, never a replacement for it.

---

## 5. Agent obligations

- **MUST** read `agent.manifest.yml` before any spec-derived reasoning, and treat `components ∪ standard` as the
  complete set of valid component types. **MUST NOT** introduce a component absent from both.
- **MUST** `load(bundles.ui_core)` before interpreting any component or layout/standard directive.
- **MUST** `load` a component's `f:` (and resolve its `with:` / `needs:`) before using any directive specific to that
  component.
- **MUST NOT** treat an absent `f:` as missing documentation. A `standard` component is fully specified by `ui_core`.
- **MUST** resolve every cross-reference (a section's `§N` pointer, a component name-anchor) by loading the referenced
  file — never by inference or memory.
- **MUST** defer to the **loaded file content** for authority rules (e.g. `STATE_TRANSITIONS` is canonical over
  `STATES`; the ACTIONS / BUSINESS_RULES / FLOW authority chain). The spec governs; the agent does not.
- **MUST NOT** hand-edit generated artifacts (`agent.manifest.yml`, `ssdl.spec.md`, any generated bundle). Changes go
  to the source files + `bundler.manifest.yml`, followed by a re-bundle.
- **SHOULD** load only the slices a task needs, and prefer section/component files over `ssdl.spec.md` for targeted
  lookups. **SHOULD NOT** load the entire spec when slices suffice.
- **MAY** read `ssdl.spec.md` when a full linear read is the actual goal.

---

## 6. Build guarantees (what an agent may rely on)

The bundler MUST produce artifacts such that:

- Every `components` entry with an `f:` resolves to a file that exists; every `c/**` and `s/**` file is referenced by
  the manifest (no orphans).
- `components ∪ standard` equals the §18 component taxonomy (the full component set).
- Every `§N` and every name-anchor cross-reference resolves.
- `agent.manifest.yml` is a faithful projection of `bundler.manifest.yml` and the files on disk.

If any guarantee fails, the **build fails** and no stale or partial `agent.manifest.yml` / `ssdl.spec.md` is published.

---

## 7. Versioning and staleness

`agent.manifest.yml` carries `version`. An agent **SHOULD** confirm it matches the spec version it expects; on
mismatch it **SHOULD** re-read the manifest rather than rely on a cached structure. Manifest structure (keys in §2)
is itself versioned by this document.

---

## Appendix · Worked example

*Task: author a screen with a `Carousel`, a `Scanner`, and a `VStack` form.*

```
read agent.manifest.yml
load(bundles.ui_core)                         # 12 layout/directive section files — the base
Carousel → load(c/layout/carousel.md)          # fill/peek on top of ui_core
Scanner  → load(c/input/scanner.md)            # + needs:[permissions] → load(sections.permissions)
                                               # + references enums    → load(enums)
VStack   → standard → nothing extra            # ui_core already covers it
authoring MODEL/VALIDATION/FLOW → load(sections.model, sections.validation, sections.flow)
```

Files opened: `agent.manifest.yml`, the 12 `ui_core` files, `carousel.md`, `scanner.md`, `permissions`, `enums`,
plus the section files for the logic being authored — **not** the 45 other component files, and **not** the full spec.
