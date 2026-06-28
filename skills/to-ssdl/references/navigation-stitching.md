# Navigation stitching — turning a business operation into a closed screen graph

This is the core discipline of `to-ssdl`. A business operation is not a pile of screens; it is a **path a user
walks**. Model it as a directed graph — screens are nodes, transitions are edges — then make that graph **closed
and consistent** before writing a single file.

## What counts as one journey

A **user journey is the connected set of screens a user moves through to accomplish a single goal** (one business
operation) — stitched by navigation, with one or a few entry points, a terminal "done" (the success exit), and the
branch / error / empty paths met along the way. It is the unit `to-ssdl` plans, generates, and reviews as one
**slice**: bigger than a screen, smaller than the app, and walkable end-to-end so it can be verified in isolation
(closed graph, decided back behavior, full state coverage).

```
operation  →  journey (a named path through the product)        ← the slice
journey     →  screens (nodes)  +  transitions (edges)
screen      →  flow (events→actions) + lifecycle (states over time) + business ops
```

A journey is the top of three nested levels — the "journeys / flows / lifecycles" being modelled:

| Level | Scope | SSDL home | Example |
|-------|-------|-----------|---------|
| **Journey** | across screens (the slice) | `ROUTE`/`ENTRY`/`EXIT`/`NAVIGATION` | "Checkout" |
| **Flow** | within a journey — reactions to user/backend | `FLOW` + `ACTIONS` | tap *Pay* → validate → `~> POST /charge` → on success → next |
| **Lifecycle** | within one screen — behavior over time | `LIFECYCLE` + `STATES` + `STATE_TRANSITIONS` | load on view; `@idle→@loading→@error/@success` |

**Sizing & boundaries.** Typically **3–7 screens**. A journey starts at an entry trigger (tab, deep link, push,
hand-off, cold start) and ends at a terminal success (goal achieved — usually a replace-stack forward exit) plus
its cancel/back/error exits. One screen alone is not a journey; the whole app is many journeys; past ~7 screens, split into sub-journeys
(below). Name each journey after its operation ("Checkout", "Onboarding", "Dispute a charge") so the graph is legible.

**Sub-journeys.** A reusable detour a journey calls and returns from — e.g. "Add payment method", invoked by both
Checkout and Profile. Author it once and reference it from each caller rather than duplicating screens.

### Examples

- **E-commerce** — separate journeys: *Browse & discover* (Home → Category → List → Product Detail) · *Checkout*
  (Cart → Address → Payment → Review → Confirmation ⇒) · *Track order* (Orders → Detail → Tracking). Shared
  sub-journeys: *Add address*, *Add payment method*. "Product Detail" alone is **not** a journey — it is one screen
  inside Browse.
- **Auth / onboarding** — three goals → three journeys (sharing Welcome/Login screens): *Sign in*
  (Welcome → Login → Home ⇒) · *Register* (Welcome → SignUp → Verify → Profile setup → Home ⇒) · *Reset password*
  (Login → Forgot → Sent → Reset → Login).
- **Fintech** — *Send money* (Home → Recipient → Amount → Review → Confirm → Receipt ⇒) · *Dispute a charge*
  (Transactions → Detail → Reason → Evidence → Submit → Confirmation ⇒). Sub-journey: *Add payee*.
- **Ride-hailing** — *Book a ride* (Map → Destination → Choose ride → Confirm → Driver en route → Trip → Rate): one
  goal, ~7 screens, with lifecycle-heavy live-update screens (*Driver en route*, *Trip*).

`⇒` = replace-stack terminal exit (back must not re-enter the journey).

## The stitching directives

Four sections wire the graph together. Author them as a set, not in isolation:

| Directive | Role in the graph | Authoring note |
|-----------|-------------------|----------------|
| `ROUTE`   | The node's address + who may reach it | `path:`, `params:` (mark required with `!`), `access: public/authenticated/optional` |
| `ENTRY`   | Inbound edges — where users arrive from | List every real source: deep link, push, tab, hand-off from another journey, cold start |
| `EXIT`    | Outbound edges — where users leave to | Every destination a user can reach, including back and cancel |
| `NAVIGATION` | The triggered transition itself | `on <event> -> <Destination> { route: /path }`; the executable form of an `EXIT` |

`EXIT` is the *declaration* of an outbound edge; `NAVIGATION` is its *implementation* (the event that fires it and
the route taken). They must agree.

## Closure rules — verify before generating, re-verify in review

1. **Every `EXIT`/`NAVIGATION` destination is a real screen** — in this journey's graph (with a matching `ENTRY`
   naming this screen as a source) or, for a **hand-off**, the entry screen of another named journey (mark it as
   such). The only forbidden case is a dangling edge — a destination that exists in no journey.
2. **Every screen is reachable** from at least one journey entry point. No orphan nodes.
3. **`EXIT` ↔ `NAVIGATION` reconcile** (LINT-030): every `NAVIGATION` destination appears in `EXIT` and vice
   versa; any asymmetry carries a `// reason:` comment.
4. **Back behavior is explicit.** Decide per transition: push (back returns), replace-stack (back does not return —
   use for auth success, post-submit confirmation), or modal (dismiss, not back).
5. **Entry points are honest.** If a screen is deep-linkable, its `ROUTE.params` cover the link and `ENTRY` lists
   the deep-link source; guard `access:` for authenticated deep links (where does an unauthenticated deep link
   land?).

## Cross-screen concerns

A journey is more than navigation — state and chrome flow across screens too.

- **Shared session/auth/cart state.** Do not duplicate it per screen. Express it through a shared fragment, route
  params passed along the path, or a `DATA` source each screen reads. Note where the journey requires
  `access: authenticated` and where the session can expire mid-journey (and where that throws the user).
- **Shared chrome.** Tab bars, nav bars, and global banners belong in a navigation fragment imported into each
  screen (`import { #app_tab_bar, #app_nav } from "@shared/navigation.ssdl" at v1`), not re-declared. A tabbed
  journey shares one `TabBar`; a stacked journey shares one `NavBar` pattern.
- **Lifecycle stitching.** Returning to a screen is a transition too. Use `LIFECYCLE` (`on screen.view`,
  `on app.foreground`) to define re-entry behavior — refetch, resume, or restore scroll — and `STATE_TRANSITIONS`
  to show how a screen moves between `@idle/@loading/@error/@success` as the user and the backend act.

## Mapping an operation to the graph (worked shape)

For "Checkout":

| Operation step | Screen | Key inbound | Key outbound |
|----------------|--------|-------------|--------------|
| Review cart | `Cart` | tab, deep link | → `Address` (proceed); → back to catalog |
| Choose address | `Address` | from `Cart` | → `Payment`; → `AddAddress` (sub-journey) and back |
| Choose payment | `Payment` | from `Address` | → `Review`; → `AddPayment` (sub-journey) and back |
| Confirm | `Review` | from `Payment` | → `Confirmation` on `place_order.success` (replace-stack) |
| Done | `Confirmation` | from `Review` | → `Home` / `OrderDetail` (replace-stack; back must not re-place the order) |

Note the design judgments a principal engineer makes here: the sub-journeys (`AddAddress`, `AddPayment`) return to
their caller; `place_order.success` replaces the stack so back cannot double-submit; `Confirmation` exits forward,
never back into `Review`.

## Present the graph as a journey map

Before Phase 5, show the user a journey map so the stitching is reviewable without reading every file:

```
Checkout (access: authenticated)
  Cart ──proceed──▶ Address ──next──▶ Payment ──next──▶ Review ──place_order.success⇒──▶ Confirmation
   ▲                  │  └─addAddress─▶ AddAddress ─back─┘                                   │
   └──────────────────┴────────────── back ───────────────────────────────────────────     └──done──▶ Home
  Entry: Cart (tab, deeplink /cart) · Exit: Home, OrderDetail
  ⇒ = replace-stack (no back)
```

Use any clear notation (arrows, an indented list, or a table) — the requirement is that every node, every edge,
the entry points, the access level, and the replace-stack transitions are visible and closed.

## Anti-patterns to avoid

- Screens with `EXIT` to a destination that exists in no journey ("I'll add it later") — close the graph, stub the
  node, or mark it a hand-off to a named journey. (A hand-off to another journey's entry is fine; a destination in
  no journey is not.)
- Re-declaring the tab/nav bar in every screen instead of a fragment.
- Modeling only the happy path — a transition out of `@error` and `@empty` is part of the journey.
- Putting business guards in two places (`BUSINESS_RULES` and `ACTIONS`) — see the authority chain in
  `ssdl-authoring.md`.
- Treating back as automatic — decide and declare it for each transition.
