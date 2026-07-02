# Run modes — fresh, resume, patch (re-running to-ssdl safely)

`to-ssdl` is **re-runnable and persistence-aware**. A corpus and its KB live on disk and are committed with the
project, so a second run must never start from a blank slate or blanket-overwrite prior work. Every run begins by
reading the corpus's **run ledger** and choosing a **mode**.

## The run ledger — `<corpus>/_session.yaml`

One small file at the corpus root records run state and source provenance. It is the single source of truth for
"what is done" and "what has the source changed since".

```yaml
status: in_progress            # in_progress | complete
mode_last: fresh               # fresh | resume | patch
updated: 2026-07-02
sources:                       # every source artifact grounded, with a fingerprint for drift detection
  - path: api/openapi.yaml
    fingerprint: sha256:…      # or size+mtime — how "changed since" is decided
    extracted: 2026-07-02
  - path: docs/prd.md
    fingerprint: sha256:…
    extracted: 2026-07-02
journeys:
  - name: Checkout
    status: done               # planned | building | reviewed | done
    screens:
      - { id: Cart,    status: ready }   # todo | written | reviewed | ready
      - { id: Payment, status: ready }
```

The ledger is **a guide, not a cache of content** — the `.ssdl` files and the KB remain ground truth. Re-derive from
them; never trust the ledger's status over what the files actually say (mirrors the `/implement-spec` "re-derive,
don't rely on a cached intermediate" discipline).

## Determining the mode (Phase 0)

| Found on disk | Mode | Meaning |
|---------------|------|---------|
| no corpus / no ledger | **Fresh** | first run — scaffold and build as normal |
| ledger `status: in_progress` | **Resume** | a prior run stopped mid-way — continue the unfinished work |
| ledger `status: complete` | **Patch** | corpus is built — re-run rigorously to reconcile drift + harden |

## Resume

Continue the loop where it stopped. Completed journeys/screens (ledger `done`/`ready`, files present) are **context,
not work** — read them for consistency, do not rebuild them. Build only the pending journeys/screens, updating the
ledger as each completes. At the end, verify closure across the **whole** graph — a half-built journey may have left
dangling edges into screens that now exist, or into ones still missing.

## Patch — a full run, seeded and reconciling (not a quick pass)

A complete corpus is re-run **with the same rigor and the same gates as a fresh run** — every phase, the lint
catalogue, the completeness checklist, app-shell + closure review. The only differences: patch **starts with better
context** (the existing corpus, KB, and journey maps are loaded upfront) and works by **reconciliation**, not
regeneration.

1. **Reset working status.** Flip the ledger `complete → in_progress`, `mode_last: patch`; mark journeys/screens
   `to_verify`. Nothing is assumed still-correct — every element is revisited under reconciliation.
2. **Re-ground and detect drift (Phase 2).** Re-read the source artifacts and re-fingerprint them; diff against the
   ledger `sources` and each KB card's `extracted_from`. Classify every fact: **unchanged / changed / new / removed**.
   Independently, scan the existing corpus for **gaps to harden** — missing states, absent `A11Y`, undeclared chrome,
   unhandled errors, stale lint — everything a stronger pass would now add. This is where patch's better upfront
   context pays off: you reconcile against a known baseline instead of discovering from zero.
3. **Reconcile, never overwrite (Phases 4–5, per screen, in dependency order):**
   - **changed** source fact → update the KB card (`facts` + `extracted_from` + fingerprint), then propagate via
     `feeds` to the sections that consume it and **edit those sections in place**;
   - **new** source (endpoint, entity, screen, journey) → add KB facts and author the new element as in a fresh run;
   - **gap to harden** → add the missing section / state / rule / a11y / error handler;
   - **removed** source → **surface it, never silently delete** — record it in `OPEN_QUESTIONS` and the review, and
     let the user decide; removing a screen or contract is destructive and needs confirmation.
   Read each file, apply the **delta**, and preserve hand-authored refinements that do not conflict. Never rewrite a
   whole file to change one section.
4. **Re-review (Phase 6).** `feeds` propagation ripples, so re-run the full review over every touched file **and its
   neighbours** — importers of a changed fragment, screens sharing a changed model, both ends of a changed edge. Lint
   + completeness + app-shell + closure, same catalogue as fresh.
5. **Update the ledger.** New fingerprints, `updated` date, statuses back to `done`/`ready`, `status: complete`.

## The non-destructive invariant (all modes)

Resume and patch **read-then-reconcile**; they never blanket-overwrite the corpus or the KB. A file changes only by a
targeted edit driven by a source change, a hardening gap, or a lint/closure failure — and a deletion is never silent
(surface it for the user's decision). Treat the corpus as code you are refactoring, not a scratch buffer you
regenerate.
