# SSDL authoring — grounding, conventions, and a principal-UX pass

The SSDL specification is the language authority. This file covers how to consume it, where files go, and how a
principal mobile UI/UX engineer fills each section. It does **not** restate the grammar — load that from the spec.

## Lazy loading by trigger (the load order)

Follow `AGENT_PROTOCOL.md`, *reactively*: read the index once, then load each spec file only when a
**trigger** — an SSDL token about to be emitted — fires. Read **`agent.manifest.yml` first** (the index, bundled
with this skill; every pointer in it resolves relative to the **skill directory**) — but read **no** spec file until
a trigger calls for it.

| When about to… (trigger) | Lazily `load()` | Manifest key |
|--------------------------|-----------------|--------------|
| start any UI/layout/component work (first time only) | the `ui_core` base (12 directive/layout files) — **once per engagement** | `bundles.ui_core` |
| place a component `C` in a screen | `C`'s file, then resolve its `with:` (children) and `needs:` (sections/enums) | `components.C.f` (+ `.with` / `.needs`) |
| use a `standard` component (no file) | nothing — `ui_core` already covers it | `standard` |
| author a screen section (route, model, validation, api, a11y, …) | that section's file | `sections.<keyword>` |
| write a value-vocabulary directive (`keyboard:`, `autocomplete:`, a `style:` token, an animation token, …) | the enum catalog | `enums` |
| hit a `§N` / name-anchor inside a loaded file | the referenced file | resolve via the manifest |
| see a component **not** in `components ∪ standard` | nothing — it is **invalid**; reject it | — |

- **Closure** — repeat until no new file is pulled in by a `with:` / `needs:` / cross-reference.
- **Release** — after a screen is written, drop its component/section bodies from context; keep only the small
  `ui_core` base + the journey map. Lazy *unload* matters as much as lazy load.
- `components ∪ standard` is the complete, authoritative component set — **use only those**; a `standard` component
  (no `f:`) is fully specified by `ui_core`, not under-documented.
- Defer to **loaded file content** for authority rules; never author from memory of the language. The slices are
  sufficient; the monolithic `ssdl.spec.md` is **not** bundled with the skill (it lives only in the SSDL repo).

## File naming and placement

```
screen.<feature>.<screen-name>.ssdl     # one screen per file
<category>.<name>.fragment.ssdl          # shared, importable fragments
```

Examples: `screen.checkout.cart.ssdl`, `screen.auth.login.ssdl`, `nav.app-shell.fragment.ssdl`,
`design.tokens.fragment.ssdl`. For the full corpus layout — feature-first with a `shared/` DRY core, the promotion
rule, and fragment versioning — see `output-structure.md`. When generating into an existing project, match what is
already there.

## Mandatory vs optional sections

Mandatory for a production screen: **`SCREEN`, `ROUTE`, `MODEL`, `UI`, `STATES`, `FLOW`, `ACCEPTANCE`.** Everything
else is added when the operation needs it — but the production default is to author all relevant sections, even
short ones. Use the recommended section order (see `assets/template.minimal.ssdl`); keep sections in that order so
files are scannable.

## Compact vs full mode

Draft in **compact mode** to explore a journey quickly (the dense `#id: Btn "Label" on tap:fn()` form). Expand to
**full mode** for handoff — every section populated, ready for engineering and QA. `assets/sample.login.ssdl` is
the canonical full-mode reference; `assets/template.minimal.ssdl` is the fill-in-the-blanks skeleton in the correct
order. Start from the template, not a blank file.

## Symbols (quick reference; spec §3 is authority)

`$field` model field · `!`/`?` required/optional · `#id` component · `@state` screen state · `:=` default/assign ·
`==>` derived/computed · `=>` effect/result · `->` navigation/transition · `~>` async call · `on/when/do`
trigger/guard/action · `BR-/VAL-/ERR-/AC-xx` rule/validation/error/acceptance IDs.

## A principal-UX pass over each section

Author each section as a senior designer-engineer would, **from the screen's KB fact card** (the real attributes,
contracts, and constraints extracted from source) plus the section's spec slice — never invent what the source
already defines (see `kb/README.md`). These are the judgments that make the output good, not just valid:

- **META** — owner, platform, status, changelog. Set `status: draft` until the completeness checklist passes.
- **PURPOSE / SCOPE** — one crisp reason the screen exists; `SCOPE.out` is as important as `in` to prevent creep.
- **ROUTE** — pick `access:` deliberately (public/authenticated/optional); mark required `params:` with `!`; the
  path is the deep-link contract.
- **ACTORS** — humans and systems the screen touches; every `ACTORS.systems` entry should map to an `API`/`DATA`
  entry or carry a `// reason:`.
- **ENTRY / EXIT** — the inbound/outbound edges of the navigation graph (see `navigation-stitching.md`). Be
  exhaustive and honest about back.
- **PERMISSIONS** — present whenever the screen touches camera, location, notifications, contacts, biometrics;
  state `request_when:` and the denied path.
- **FEATURE_FLAGS** — gate any conditional component or behavior here; reference the flag from `UI`/`FLOW`.
- **MODEL** — the screen's state shape; push logic into derived fields (`==>`) rather than duplicating it in
  actions; give sensible defaults (`:=`).
- **DATA** — `source:` and explicit `read:`/`write:`; declare cache strategy for remote reads.
- **COPY** — user-facing strings as keys (parameterized with ICU where needed); keep tone consistent.
- **UI** — layout as **hints, not pixels** (`center`, `below(#x, md)`, `w:fill`, `sticky(bottom.safe)`); choose
  components from the taxonomy only; ensure every text-bearing component has a `style:` token; cover loading,
  empty, error, success states in the layout, not just the happy path.
- **STATES / STATE_TRANSITIONS** — enumerate every meaningful state; declare `initial:`; author
  `STATE_TRANSITIONS` for 3+ states and ensure each state is reachable. `STATE_TRANSITIONS` is canonical over
  `STATES`.
- **LIFECYCLE** — re-view, foreground, background behavior; define what refetches or resumes on return.
- **ANIMATION** — enter/exit/shared-element motion with a `reduced_motion` alternative for every animation.
- **VALIDATION** — sync, cross-field, and async rules with `VAL-` IDs and user-facing messages.
- **BUSINESS_RULES** — testable `BR-` rules; do not also encode the same guard in `ACTIONS`.
- **ACTIONS** — pseudocode for non-trivial behavior; async work shows loading and failure handling.
- **FLOW** — wire user events to actions/navigation (`on tap #x when guard do fn()`).
- **API** — request/response shapes, auth, cache, error statuses, timeout, retry.
- **NAVIGATION** — the executable transitions; reconcile with `EXIT`.
- **ANALYTICS** — events with trigger + props; include a `privacy` block for auth/payment/personal-data screens.
- **A11Y** — focus order, labels, touch targets ≥44pt, dynamic type, contrast, reduced motion. Author it, don't
  bolt it on.
- **ERRORS** — `ERR-` handlers tied to API/validation failures, with recovery and the UI shown.
- **ACCEPTANCE** — `AC-` criteria covering happy path, validations, errors, navigation, re-view, and accessibility.

## Reuse with fragments

Pull shared definitions in rather than repeating them:

```ssdl
import { copy.common } from "@shared/copy.ssdl" at v1
import { ERR-NETWORK } from "@shared/errors.ssdl" at v1
import { VAL-email } from "@shared/validators.ssdl" at v1
```

Use `import` for named definitions and `include` for inlined section content. Pin versions with `at v<n>`; imports
use logical `@alias/<name>.ssdl` paths resolved by `ssdl.config.json` (see §46). **Split shared definitions by
concern** — nav, design tokens, copy, error map, validators, models, api — rather than one catch-all. When a
pattern recurs in 2+ screens of a journey, lift it into a **feature-local** fragment; when a 2nd **feature** needs
it, **promote it to `shared/`** (see `output-structure.md`).

**The app shell is reuse by inheritance, not per-screen import.** Put the nav/tab/drawer chrome in
`@shared/navigation.ssdl`, place it once in an `AppShell` base layout, and have every in-app screen
**`extends AppShell`** — the chrome is inherited, never re-imported per screen (LINT-054). Exception screens
(`auth`/`modal`/`immersive`/`wizard`) extend an exception base or annotate `// chrome: <category>` (LINT-055). See
`navigation-stitching.md` ("App shell").

## The authority chain (do not violate)

- `STATE_TRANSITIONS` is canonical over `STATES`.
- Guards live in `BUSINESS_RULES` **or** `ACTIONS`, not both.
- `ACTORS.systems` ↔ `API`/`DATA`; `NAVIGATION` ↔ `EXIT`; UI child/parent references are mutually consistent.

When unsure of exact syntax for any of the above, load the relevant `sections.<keyword>` file from the manifest —
that file governs.
