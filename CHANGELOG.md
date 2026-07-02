# Changelog

All notable changes to the **SSDL** (Single-Screen Specification Definition Language) specification are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and SSDL adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Section references (e.g. §4a) point to [`ssdl.spec.md`](ssdl.spec.md).

## [Unreleased]

### Added
- **LINT-054 / LINT-055** — app-shell consistency: recurring chrome (nav/tab/drawer bars, app-wide banners) must be
  imported from a shared fragment, not re-declared per screen; and when a corpus defines a shared app shell, every
  screen must include it or annotate the omission `// chrome: <category>`.

### Docs
- Clarified in §46 how an `@alias/<name>.ssdl` fragment import resolves via `ssdl.config.json` to the physical
  `<category>.<name>.fragment.ssdl` file (closing a §45/§46 gap).

## [1.5.0] - 2026-06-27

A consistency, reorganization, and packaging pass over v1.4.0. Contains breaking changes.

### Changed
- **Breaking — `ROUTE.auth` → `access:`** with values `public` / `authenticated` / `optional` (and `auth_roles` → `access_roles`); the API `auth:` request credential is unchanged.
- **Breaking — collection iteration** consolidated on `data:`/`item:` with an `as $element` binding; `repeat_for:` and the `… map …` form removed.
- **Reorganized** into a comprehension-first section order (META → PURPOSE/SCOPE → … → PERMISSIONS → FEATURE_FLAGS), made consistent across the file-structure rule, the sample, and the template, with a grouped Table of Contents. Section numbers changed accordingly.
- Standardized the "not loading" form on `$is_loading ==> @loading`; added a `text:` vs `label:` rule.

### Added
- **`~>`** async-call operator wired into the grammar.
- **`Banner { type: }`** (info/success/warning/error); **Modal** given a crisp boundary vs **Dialog**; **Grid** and **HStack** component entries; `STATE_TRANSITIONS` added to the section enumerations.
- **File-split distribution** — the spec is now maintained as per-section and per-component source files under `spec/`, assembled by `bundle.py` into `ssdl.spec.md` (a generated artifact) plus an `agent.manifest.yml` index. Consumption contract in `AGENT_PROTOCOL.md`.

### Removed
- **Breaking** — the five deprecated component tombstones (`DragHandle`, `PullRefreshIndicator`, `Pager`, `WrapStack`, `Masonry`) and all references.
- The historical "Review pass" section and the `SSDL_EXTENSIONS.md` note.

### Docs
- Extracted the completeness checklist, lint rules, and minimal template into standalone files (`completeness-checklist.md`, `lint-rules.md`, `template.minimal.ssdl`); the corresponding sections now point to them.
- Collapsed the layout/motion vocabulary into pointers to the authoritative directive sections (the value-enum catalogue is retained).

## [1.4.0]

- **§4a Import and Include** — full import system: named imports, namespace imports, `as` aliasing, `at v<n>` version pinning, relative and `@alias` paths, transitive dependency rules, conflict resolution (local wins; later import wins), `include` for inlining shared section content with before/after ordering semantics
- **§4b Fragment file format** — `FRAGMENT name v<n>` header, `FRAGMENT_META` changelog block, explicit `export` declarations, re-export barrel pattern, fragment-importing-fragment support
- **`ssdl.config.json`** — `@alias` resolution configuration at project root
- **MODEL field set imports** — `use $field_set` keyword expands imported field sets in-place
- **§3 symbols** — `import`, `from`, `at`, `as`, `include`, `export`, `FRAGMENT`, `FRAGMENT_META`, `@alias`
- **§4 file structure** — import declarations added to canonical file order
- **§5 grammar** — `Document`, `ImportDecl`, `ImportItems`, `IncludeDirective`, `FragmentDocument`, `FragmentDecl`, `ExportDecl` productions
- **§50.0 checklist** — new imports section
- **Formal file extension** — adopted `.ssdl` as the single formal file extension for all SSDL source files (screen specs and fragments), replacing the dual `.ssdl.md` convention still present in naming convention examples
- **LINT-047–053** — circular imports, path resolution, same-ID conflict, non-exported item import, local shadows

## [1.3.0]

Simplification pass.

- **Merges:** `ConfirmDialog` + `DialogBox` → `Dialog` (single type, `cancel_label:` optional); `EmptyState` + `ErrorState` → `EmptyState { type: }` (§48.28 EmptyState types); `Carousel` + `Pager` → `Carousel { fill: true }` (unified event `on slide_change:`)
- **Demotions:** `PullRefreshIndicator` → `PullToRefresh { custom_indicator: }`; `WrapStack` → `HStack { wrap: true, row_gap: }`; `DragHandle` → convention pattern; `Masonry` → `Grid { masonry: true }`
- **New child component types:** `SpeedDialItem`, `ContextMenuItem` — replaces inline object array pattern
- **Naming fixes:** `Tag.text:` (was `label:`); `Stat.subtitle:` (was `label:`); `EmptyState.description:` (was `body:`); action item `text:` (was `label:`); `RichTextEditor.on change:` (was `on content_change:`)
- **Example quality:** examples no longer show directives at default values; default-values rule documented in §16a intro

## [1.2.0]

- 53 new component types across §16.1–16.5 — content, input, action, feedback, layout
- §16a: per-component directive tables, SSDL examples, A11Y default roles
- §17 grammar: 40+ component-specific directive productions
- §48.11–48.27: vocabulary for map zoom, scanner formats, status values, popover placement, step styles, color modes, tag/rating styles, table columns, progress styles, aspect ratios, QR EC levels, trend directions, selection modes, orientation, location result types
- LINT-033–046

## [1.1.0]

- Unified `on event:` syntax — component blocks and FLOW share the same event vocabulary; `on_*` prefix removed
- `screen.view` / `screen.first_view` — canonical lifecycle event names replacing `screen.appear`
- `initial:` declaration in `STATES` — explicit initial state required when `STATE_TRANSITIONS` is present
- Cross-field validation (`fields:`) and async validation (`async:`) in `VALIDATION`
- Animation easing tokens and `then` chaining for sequenced animations
- `A11Y.roles` block — semantic role overrides with inferred defaults from component type
- Analytics `dedup:` field and `privacy.consent:` field with vocabulary and LINT-028
- `fallback:` field in `FEATURE_FLAGS` — separate from `default:`, covers flag evaluation failure
- Expanded component directives: `label:`, `placeholder:`, `helper_text:`, `error:`, `value:`, `min:`, `max:`, `step:`, `autocomplete:`, `autocapitalize:`, `checked_when:`, `selected_when:`, `disabled_when:`, `test_id:`
- §48.9 `autocomplete:` vocabulary — full credential/autofill type list
- §55 spec-to-implementation traceability — patterns for source code, tests, and PR descriptions
- Derived field rules: circular dependency prohibition, topological evaluation order, state-as-Boolean pattern (`$is_loading ==> @loading`)
- `ACTORS.secondary` removed; `primary` / `systems` fields documented with definition table
- Error category descriptions added; `timeout` category added
- 7 new lint rules (LINT-026 through LINT-032)

## [1.0.0]

Key additions over the initial draft:

- `style:` directive and typography token vocabulary — design system integration
- `LIFECYCLE` section — screen/app lifecycle events, re-appear behavior
- `PERMISSIONS` section — OS permission declaration and fallback handling
- `FEATURE_FLAGS` section — flag-gated components with registry and audit trail
- `ANIMATION` section — motion intent with mandatory `reduced_motion` alternatives
- `extends` + `OVERRIDE` — screen variant inheritance without full duplication
- ICU-format copy interpolation and pluralization
- `keyboard:` directive with formal vocabulary
- `cache:` strategy in DATA and API sections
- Structured `OPEN_QUESTIONS` with `owner:` and `blocks:`
- `STATE_TRANSITIONS` as canonical machine-readable state machine
- Authority chain for FLOW / BUSINESS_RULES / ACTIONS
- `ANALYTICS.privacy` sub-block (replaces top-level `ANALYTICS_PRIVACY`)
- `ERR-500` coverage requirement and `// handled:` API annotation
- `pagination:` and `empty_state:` on collection components
- `contrast:` in A11Y vocabulary
- 10 new lint rules (LINT-016 through LINT-025)
