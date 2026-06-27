---
name: to-ssdl
description: This skill should be used when the user asks to "convert to SSDL", "generate SSDL", "model this as SSDL", "turn this spec/PRD into SSDL", "design the screens/flows in SSDL", invokes "/to-ssdl", or wants navigation-stitched .ssdl screen specs that capture user journeys, flows, and lifecycles from a product spec, PRD, process description, or business operation. The skill acts as a principal mobile UI/UX engineer and treats the SSDL specification (via agents/agent.manifest.yml) as the language authority. It produces SSDL design artifacts, never application code.
version: 0.1.0
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

1. **Locate the spec.** Default to this repository (it contains `agents/agent.manifest.yml`). When generating in a
   different project, point at a local checkout or the SSDL repo (`github.com/pakasa-io/ssdl`) and treat its root as
   the spec root.
2. **Follow `agents/AGENT_PROTOCOL.md`.** Read `agents/agent.manifest.yml` **first**; it is the index of where to
   find what. Load `bundles.ui_core` before interpreting any UI/layout/component; load `sections.<keyword>` and
   `components.<Name>.f` files **on demand**; resolve every pointer relative to the **repo root**.
3. **Never invent vocabulary.** `components ∪ standard` in the manifest is the complete, authoritative component set.
   Use only those. Use only directives and value enums defined in the loaded section/`enums` files. The spec
   governs the language; this skill governs the journey/translation workflow.

Read `references/ssdl-authoring.md` for grounding mechanics, file naming, mandatory sections, and per-section UX
guidance. Read `references/navigation-stitching.md` for **what counts as one journey** (definition, sizing, examples) and
the core discipline of this skill — turning an operation into a closed, consistent screen graph.

## Workflow — one journey at a time

Track every journey and phase as tasks. Work a single journey through to review before starting the next, then
checkpoint (summarize, surface blockers) rather than running ahead.

### Phase 1 — Discovery
Restate the business operation(s) to be modelled and the journeys they imply. If the input is thin, ask what the
operation is, who performs it, and what "done" looks like. Produce a short list of candidate journeys and confirm
scope before going further.

### Phase 2 — Ground in the spec and any existing screens
Read `agents/agent.manifest.yml` and skim `agents/AGENT_PROTOCOL.md`. If `.ssdl` files already exist in the target
project, explore them (launch read-only explorer agents for larger codebases) to learn naming, fragments already in
use, navigation conventions, and the design-system fragment. Reuse before inventing. Report what exists.

### Phase 3 — Clarifying questions (do not skip)
Resolve ambiguities **before** designing the graph. Typical gaps: the actors and their `access:` level
(public/authenticated/optional); journey entry points (deep link, tab, push, hand-off from another flow); exit and
back behavior; auth/session boundaries; target platforms; required permissions; failure/empty/offline handling;
and which screens are net-new vs variants of existing ones. Present questions as a tight list and wait for answers.
If the user defers the decision, state the recommendation and proceed.

### Phase 4 — Journey & navigation architecture
Design the **screen graph** before writing any file (this is the heart of the skill — see
`references/navigation-stitching.md`):
- Enumerate screens as nodes; draw edges as `ENTRY`/`EXIT`/`NAVIGATION` transitions.
- Identify shared fragments (navigation chrome, design system, common errors) and cross-screen state (auth,
  session, cart).
- Map each screen's lifecycle and state machine at a high level.
- Verify the graph is **closed** (every `EXIT` lands on a real screen; every screen is reachable) and present it as
  a journey map. Offer one or two structural options when there's a real trade-off, with a recommendation. Get
  agreement on the map before generating.

### Phase 5 — Generate the stitched screens
Author the `.ssdl` files for the agreed journey, plus any new fragments. For each screen, load the section and
component files it needs (per the manifest) and write all mandatory sections (`SCREEN`, `ROUTE`, `MODEL`, `UI`,
`STATES`, `FLOW`, `ACCEPTANCE`) plus those the operation requires (`DATA`, `API`, `BUSINESS_RULES`, `VALIDATION`,
`LIFECYCLE`, `STATE_TRANSITIONS`, `NAVIGATION`, `ANALYTICS`, `A11Y`, `ERRORS`). Stitch navigation as designed.
Follow the recommended section order; mirror the conventions in `assets/template.minimal.ssdl` and
`assets/sample.login.ssdl`.

### Phase 6 — Review: navigation closure + lint + completeness
Review the journey, not just each file:
- **Navigation closure** — reconcile `EXIT` ↔ `NAVIGATION` (LINT-030), confirm every destination exists, back and
  deep-link behavior is defined, and the journey is traceable end-to-end.
- **Lint** — run the catalogue in `assets/lint-rules.md` against each file.
- **Completeness** — run `assets/completeness-checklist.md` before any screen is called `ready`.
- **Lifecycle fidelity** — `STATE_TRANSITIONS` present for 3+ states; every state reachable.
Present findings by severity and fix per the user's call.

### Phase 7 — Summary
Mark tasks complete. Output the **journey map**, the files written, key design decisions, and suggested next
journeys. Commit only when the user asks.

## Resources

- **`references/navigation-stitching.md`** — what counts as one journey (definition, sizing, examples); modelling
  an operation as a closed screen graph; `ENTRY`/`EXIT`/`NAVIGATION` reconciliation; back, deep links, cross-screen
  state and lifecycle.
- **`references/ssdl-authoring.md`** — grounding via the agent manifest, file naming, mandatory vs optional
  sections, fragment reuse, and a principal-UX pass over each SSDL section.
- **`examples/onboarding-journey.md`** — a small worked journey showing the stitched output and its journey map.
- **Spec assets** (at the SSDL repo root): `agents/agent.manifest.yml`, `agents/AGENT_PROTOCOL.md`,
  `assets/lint-rules.md`, `assets/completeness-checklist.md`, `assets/template.minimal.ssdl`,
  `assets/sample.login.ssdl`.
