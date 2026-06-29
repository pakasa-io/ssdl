---
name: to-ssdl
description: This skill should be used when the user asks to "convert to SSDL", "generate SSDL", "model this as SSDL", "turn this spec/PRD into SSDL", "design the screens/flows in SSDL", invokes "/to-ssdl", or wants navigation-stitched .ssdl screen specs that capture user journeys, flows, and lifecycles from a product spec, PRD, process description, or business operation. The skill acts as a principal mobile UI/UX engineer and treats the SSDL specification (bundled in the skill) as the language authority. It produces SSDL design artifacts, never application code.
version: 0.7.0
---

# to-ssdl — model business operations as navigation-stitched SSDL

Operate as a **principal mobile UI/UX engineer** (design + development). Take a written input — a spec, PRD,
business-process description, ticket, or a sketch of user journeys — and produce a coherent set of
**navigation-stitched `.ssdl` screen specs** that mimic the described business operations as **user journeys,
flows, and lifecycles**.

This is the SSDL analogue of `/implement-spec`: same plan → build → review loop and the same discipline of working
one vertical deliverable at a time. The difference is the artifact. `/implement-spec` writes code; **to-ssdl writes
SSDL** — a navigable graph of screens, not an implementation. Do not generate application code.

## What "principal UI/UX engineer" changes about the output

- **Journey-first.** Model the *operation* as a path a real user walks, not a dump of screens. A business
  operation ("Checkout", "Onboarding", "Dispute a charge") becomes a stitched journey: Cart → Address → Payment →
  Review → Confirmation.
- **Full state coverage.** Every screen accounts for loading, empty, error, success, and offline — not just the
  happy path. States and their transitions are explicit (`STATES` + `STATE_TRANSITIONS`).
- **Platform-honest.** Respect mobile conventions (back behavior, safe areas, tab vs stack navigation, system
  permissions, keyboard handling) so the spec maps cleanly to iOS, Android, RN, Flutter, or mobile web.
- **Accessibility-first.** `A11Y` is authored, not appended — focus order, labels, touch targets, reduced motion.
- **Reuse over repetition.** Shared chrome (nav bars, tab bars, error handlers, design tokens) lives in fragments
  pulled in with `import`/`include`, not copy-pasted per screen.

## The SSDL spec is the authority — ground in it first

The language is defined by the SSDL specification, which is built for exactly this kind of progressive consumption.
Before authoring anything:

1. **The spec is bundled with this skill.** Alongside `SKILL.md` sit `agent.manifest.yml` (the index), `spec/`
   (the slices), `AGENT_PROTOCOL.md`, and `assets/`. **This skill's own directory is the spec root** — every
   manifest pointer (`spec/…`) resolves inside it. Nothing external is required.
2. **Follow `AGENT_PROTOCOL.md`.** Read `agent.manifest.yml` **first**; it is the index of where to find what.
   Load `bundles.ui_core` before interpreting any UI/layout/component; load `sections.<keyword>` and
   `components.<Name>.f` files **on demand**; resolve every pointer relative to the **skill directory**.
3. **Never invent vocabulary.** `components ∪ standard` in the manifest is the complete, authoritative component set.
   Use only those. Use only directives and value enums defined in the loaded section/`enums` files. The spec
   governs the language; this skill governs the journey/translation workflow.

Read `references/ssdl-authoring.md` for lazy-loading-by-trigger mechanics, file naming, mandatory sections, and per-section UX
guidance. Read `references/navigation-stitching.md` for **what counts as one journey** (definition, sizing, examples) and
the core discipline of this skill — turning an operation into a closed, consistent screen graph.

## Workflow — discover once, plan per journey, build per screen

The work is a **three-level nested loop**, not a one-shot pipeline: run **Phases 1–3 once**, then **repeat Phases
4–7 per journey**, and **within Phase 5 repeat per screen**. Only a candidate *list* of journeys is produced
upfront — never the full planset of maps. Planning, closure-review, and checkpoints are journey-scoped; generation
and commits are screen-scoped. The **journey map** (Phase 4) is the small, durable anchor that carries cross-screen
context — author each screen against the map plus the files already on disk, not recall. Track every journey and
screen as tasks.

```
ONCE  (Phases 1–3, per engagement)
  discover candidate-journey LIST + scope · ground in spec · clarify
     │
     ▼
PER JOURNEY  (Phases 4–7, outer loop)  ── repeat for each journey in the list
  Phase 4  plan THIS journey's map  ───────────────┐  (small, durable anchor)
  Phase 5  build, PER SCREEN (inner loop):         │
             for screen in map (journey order):    │
               load slices → author → self-check ──┘  (every edge checked against the map)
               → write file → release from context → commit screen
  Phase 6  review: re-read the written files from disk → verify closure
  Phase 7  checkpoint: summarize, surface blockers → next journey
```

**Context budget:** hold only the current journey's map + the current screen's spec slices; everything else lives
on disk. Reload slices per screen; never hold multiple screens' bodies — or all journeys' maps — at once.

### Once (per engagement)

#### Phase 1 — Discovery
Restate the business operation(s) to be modelled and the journeys they imply. If the input is thin, ask what the
operation is, who performs it, and what "done" looks like. Produce a short list of candidate journeys and confirm
scope before going further.

#### Phase 2 — Ground in the spec and any existing screens
Read **only `agent.manifest.yml`** up front (the index) and skim `AGENT_PROTOCOL.md` — do **not**
bulk-load spec files; each `sections.*` / `components.*` / `enums` file loads later, lazily, when a trigger fires
(Phase 5). If `.ssdl` files already exist in the target
project, explore them (launch read-only explorer agents for larger codebases) to learn naming, fragments already in
use, navigation conventions, and the design-system fragment. Reuse before inventing. Report what exists.

**Extract the project's source material** (OpenAPI, JSON schemas, DB/ERD, PRD, design specs) into the KB
(`kb/`) — fill each element's `facts` + `extracted_from`. These grounded facts are the input Phase 5 authors from;
anything missing or ambiguous lands in `OPEN_QUESTIONS`.

#### Phase 3 — Clarifying questions (do not skip)
Resolve ambiguities **before** designing the graph. Typical gaps: the actors and their `access:` level
(public/authenticated/optional); journey entry points (deep link, tab, push, hand-off from another flow); exit and
back behavior; auth/session boundaries; target platforms; required permissions; failure/empty/offline handling;
and which screens are net-new vs variants of existing ones. Present questions as a tight list and wait for answers.
If the user defers the decision, state the recommendation and proceed.

### Per journey (repeat Phases 4–7)

#### Phase 4 — Journey & navigation architecture
Design the **screen graph** before writing any file (this is the heart of the skill — see
`references/navigation-stitching.md`):
- Enumerate screens as nodes; draw edges as `ENTRY`/`EXIT`/`NAVIGATION` transitions.
- Identify shared fragments (nav chrome, design tokens, copy, error map, validators, models — see
  `references/output-structure.md`) and cross-screen state (auth, session, cart).
- Map each screen's lifecycle and state machine at a high level.
- Verify the graph is **closed** (every `EXIT` lands on a real screen; every screen is reachable) and present it as
  a journey map. Offer one or two structural options when there's a real trade-off, with a recommendation. Get
  agreement on the map before generating. If the map exceeds ~7 screens, split it into sub-journeys (see
  `references/navigation-stitching.md`).

#### Phase 5 — Build the journey, one screen at a time
If the corpus is new, first scaffold `ssdl.config.json` (the `@aliases`) and the `shared/` + `journeys/` skeleton
per `references/output-structure.md`. Then build **screen by screen** against the agreed map — never the whole
journey in one pass. For each screen, in journey order:
1. **Load by trigger.** From the screen's entry in the map, derive its triggers — the components it places and the
   sections it needs — then `load()` exactly those slices and resolve their `with:` / `needs:` / `§N` to closure
   (the trigger table is in `references/ssdl-authoring.md`). Load nothing else.
2. **Author its sections in dependency order** (the `kb/` tree: `MODEL` before `UI`, `STATES` before
   `FLOW`/`LIFECYCLE`, `API`/`ERRORS` before `ACCEPTANCE`) — *not* the comprehension order. Author each section from
   its **KB fact card** (`facts`, extracted in Phase 2 — the real attributes, contracts, and constraints) plus its
   SSDL spec slice; the card's `feeds` routes those facts into the downstream sections that consume them — and as a
section consumes a fact, append its screen to that fact's `applies_to` (which is populated retrospectively). Cover the
   mandatory sections (`SCREEN`, `ROUTE`,
   `MODEL`, `UI`, `STATES`, `FLOW`, `ACCEPTANCE`) plus those the operation requires (`DATA`, `API`,
   `BUSINESS_RULES`, `VALIDATION`, `LIFECYCLE`, `STATE_TRANSITIONS`, `NAVIGATION`, `ANALYTICS`, `A11Y`, `ERRORS`);
   mirror `assets/template.minimal.ssdl` and `assets/sample.login.ssdl`.
3. **Self-check** the screen in isolation: `#id`s internally consistent; its `ENTRY`/`EXIT`/`NAVIGATION` edges
   match the map; per-screen lint.
4. **Write** the file and **release its body from working context** — rely on the map + disk thereafter.
5. **Commit** the screen, then move to the next. (Per-screen is the recommended cadence; commit only at the user's
   direction.)

Place each file per `references/output-structure.md` — screens under their feature folder, shared details
**imported, never inlined**; author a new fragment (navigation chrome, design system, validators, error map) when
first needed and promote it to `shared/` once a 2nd feature uses it. Keep only the journey map + the current
screen's slices in working context.

#### Phase 6 — Review: navigation closure + lint + completeness
Review the journey as a whole, and **re-read the written files from disk** — do not rely on recall of what was
generated:
- **Navigation closure** — reconcile `EXIT` ↔ `NAVIGATION` (LINT-030), confirm every destination exists (in this
  journey or as a marked hand-off), back and deep-link behavior is defined, and the journey is traceable
  end-to-end.
- **Lint** — run the catalogue in `assets/lint-rules.md` against each file.
- **Completeness** — run `assets/completeness-checklist.md` before any screen is called `ready`.
- **Lifecycle fidelity** — `STATE_TRANSITIONS` present for 3+ states; every state reachable.
Present findings by severity and fix per the user's call.

#### Phase 7 — Checkpoint
Mark tasks complete. Output the **journey map**, the files written, and key design decisions; surface blockers;
then move to the next journey in the list (or stop). Commit only when the user asks.

## Resources

- **`references/navigation-stitching.md`** — what counts as one journey (definition, sizing, examples); modelling
  an operation as a closed screen graph; `ENTRY`/`EXIT`/`NAVIGATION` reconciliation; back, deep links, cross-screen
  state and lifecycle.
- **`references/ssdl-authoring.md`** — grounding via the agent manifest, file naming, mandatory vs optional
  sections, fragment reuse, and a principal-UX pass over each SSDL section.
- **`references/output-structure.md`** — the generated corpus layout (feature-first + a `shared/` DRY core), the
  promotion rule, fragment versioning, and logical imports (`@shared/<name>.ssdl`).
- **`kb/`** — the **knowledge base**: a fact-extraction scaffold (one YAML card per `.ssdl` element, in dependency
  order). Phase 2 fills each card's `facts` from the source material (OpenAPI/schemas/PRD); Phase 5 authors each
  section from its facts + spec slice, with `feeds` routing facts downstream. See `kb/README.md`.
- **`examples/onboarding-journey.md`** — a small worked journey showing the stitched output and its journey map.
- **Bundled spec** (self-contained, alongside this skill): `agent.manifest.yml` (index), `spec/` (slices),
  `AGENT_PROTOCOL.md`, and the `assets/` files (`lint-rules.md`, `completeness-checklist.md`,
  `template.minimal.ssdl`, `sample.login.ssdl`).
