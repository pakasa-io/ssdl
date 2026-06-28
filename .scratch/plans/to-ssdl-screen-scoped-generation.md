# Plan — `to-ssdl`: make the work loop explicit (plan per journey, generate per screen)

**Status:** applied (in `skills/to-ssdl/`, v0.2.0) · **Date:** 2026-06-27 · **Affects:** `skills/to-ssdl/`

## Problem

The `to-ssdl` skill defines its working loop as *"one journey at a time"* and lays its phases out as a flat 1→7
pipeline, with the loop carried by a single sentence. Two problems follow:

**A — Generation granularity.** A journey is 3–7 screens, and a full-mode SSDL screen is ~20 sections (cf.
`assets/sample.login.ssdl`). Generating an entire journey in one pass risks:
- **Drift** — by the 5th screen, recall of earlier screens' `#id`s, states, and stitching is stale, producing
  inconsistent navigation.
- **Context pressure** — holding several large screens *plus* the loaded spec slices at once strains the working
  context window.

**B — Loop boundaries are implicit.** The flat phase list never states which phases run *once* and which *repeat
per journey*. It reads as a one-shot pipeline — "plan every journey (Phase 4), then generate every journey
(Phase 5)" — i.e. the **whole planset upfront**. That is not the intent, but the doc invites the misreading.

Concerns raised: *"isn't a user journey as a slice too big? context will be lost"* and *"is the skill generating
the entire planset upfront, instead of per cycle?"* — both valid, both rooted in implicit loop structure.

## Decision

Make the work an explicit **three-level nested loop**, and separate what each level is the unit *of*:

| Level | Runs | Is the unit of | Why |
|-------|------|----------------|-----|
| **Engagement** | **once** | discovery, grounding, clarifying | The candidate-journey *list* + scope + spec grounding are shared across all journeys. |
| **Journey** | **loop (outer)** | planning, closure-review, checkpoint | Navigation closure (`EXIT`↔`ENTRY`↔`NAVIGATION`) only *exists* across the whole graph; it cannot be verified screen-by-screen. |
| **Screen** | **loop (inner)** | generation + commit | Small, focused; one screen's full SSDL at a time. |

Only the **engagement** level is "upfront", and it produces just a *list* of candidate journeys — never the full
planset of maps. Each journey is architected (its map) **inside its own cycle**, just before that journey is built.

The **journey map** (the Phase-4 artifact, produced per journey) is the durable, compact context anchor — a handful
of lines encoding every cross-screen decision (nodes, edges, entry/exit, access, replace-stack marks). Screens are
generated one at a time *against the map*; the map plus the files already on disk carry the context, not recall.

### Invariants that bound context

1. **Discover once; plan per journey; generate per screen.** Phases 1–3 run once (candidate list + grounding +
   clarification); Phases 4–7 repeat per journey; Phase 5 repeats per screen. The full planset is never produced
   upfront.
2. **The journey map is planned upfront *within* its cycle** — cheap, holistic, before that journey's files are
   written. This is the only "plan ahead", and it is small (a few lines).
3. **Generate at screen scope.** For each screen: load only the spec slices it needs (manifest progressive
   disclosure bounds *spec* context), author it, self-check it against the map, **write to disk, release its body
   from working context**, move on. Never hold N full screens simultaneously.
4. **Verify closure by re-reading from disk** (Phase 6), never from memory — the AGENT_PROTOCOL rule ("resolve by
   loading, never by inference or memory"). Consistency is checked against ground truth, not recall.
5. **Commit per screen** (finer than per-journey) so each increment is durable and the working set stays small. A
   journey is "done" only when its graph closes.

### Loop shape (at a glance)

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
  Phase 6  review: re-read the written files from disk → verify closure (LINT-030, reachability, back/deep-links)
  Phase 7  checkpoint: summarize, surface blockers → next journey
```

## Changes (apply to `skills/to-ssdl/`)

### Change 1 — Reframe the workflow as an explicit nested loop (`SKILL.md`)
- Heading: `## Workflow — one journey at a time` → `## Workflow — discover once, plan per journey, build per screen`.
- Intro: state the three levels — **Phases 1–3 run once** (candidate-journey list, grounding, clarification);
  **Phases 4–7 repeat per journey**; **Phase 5 repeats per screen**. Only a candidate *list* is produced upfront,
  never the full planset. Planning, closure-review, and checkpoints are journey-scoped; generation and commits are
  screen-scoped; the journey map is the anchor carried across screens.
- Add the "Loop shape (at a glance)" diagram (above) into the skill so the nesting is visible, not inferred.
- Group the phase headings by level so the boundaries are unmissable:
  - `### Once (per engagement)` over Phases 1–3
  - `### Per journey (repeat Phases 4–7)` over Phases 4–7
  - inside Phase 5, a `Per screen (repeat)` label for the inner loop

### Change 2 — Rewrite Phase 5 as a per-screen inner loop (`SKILL.md`)
Replace the current Phase 5 prose with an explicit inner loop:
- For each screen in the agreed map, in journey order:
  1. Load the section/component slices that screen needs (per the manifest).
  2. Author the screen's full SSDL against the map (mandatory sections + those the operation requires).
  3. Self-check the screen in isolation: `#id`s internally consistent; `ENTRY`/`EXIT`/`NAVIGATION` edges match the
     map; per-screen lint.
  4. Write the file; **release its body from working context** (rely on disk + the map thereafter).
  5. Commit the screen (if committing as you go); proceed to the next.
- Keep only the journey map + the current screen's slices in working context.

### Change 3 — Phase 6 re-reads from disk (`SKILL.md`)
Phase 6 closure review must **re-read the written `.ssdl` files from disk** to reconcile the graph
(`EXIT`↔`ENTRY`↔`NAVIGATION`, LINT-030, reachability), rather than relying on recall of what was generated.

### Change 4 — Context-budget note + sizing guard (`SKILL.md` + `references/navigation-stitching.md`)
- Add a short **context-budget** note: the map is the anchor; generate and persist screen-by-screen; reload spec
  slices per screen; never hold the whole journey's bodies (or all journeys' maps) at once.
- Cross-reference the existing sizing guard (a journey past ~7 screens splits into sub-journeys; already in
  `navigation-stitching.md`) from the workflow.

## Non-goals

- Changing the SSDL language, the spec, or the manifest.
- Making the **screen** the planning/closure unit — closure needs the whole graph.
- Producing every journey's map upfront — journeys are architected one cycle at a time.
- Changing the worked example's content (already addressed in the F1–F5 consistency pass).

## Acceptance criteria

- `SKILL.md` makes the **three-level nesting explicit**: Phases 1–3 once, Phases 4–7 per journey, Phase 5 per
  screen — stated in words *and* shown in the loop diagram, so it cannot be read as a one-shot pipeline that plans
  the whole planset upfront.
- `SKILL.md` describes **plan@journey / generate@screen**, with the per-screen inner loop and the map-as-anchor.
- Phase 6 instructs re-reading files from disk for closure.
- From the skill alone, a reader can tell that only a candidate *list* is produced upfront, and that screens are
  generated and committed one at a time, with context anchored by the map + on-disk files (not recall).
- No new contradictions (re-run the consistency-review lens); `python3 scripts/bundle.py --check` unaffected.
- Optional: bump the skill `version` 0.1.0 → 0.2.0 when applied.

## Notes

- Mirrors `/implement-spec`: discover/plan at feature scope, implement incrementally; the spec/plan is the durable
  anchor. The nesting here (engagement → journey → screen) is the SSDL-shaped version of that.
- Estimated edit surface: the `## Workflow` heading/intro + phase-grouping subheads + Phases 5–6 of `SKILL.md`,
  plus one cross-reference line in `navigation-stitching.md`. Low risk, no spec/bundle impact.
