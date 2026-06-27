# Navigation stitching — turning a business operation into a closed screen graph

This is the core discipline of `to-ssdl`. A business operation is not a pile of screens; it is a **path a user
walks**. Model it as a directed graph — screens are nodes, transitions are edges — then make that graph **closed
and consistent** before writing a single file.

## The mental model

```
operation  →  journey (a named path through the product)
journey     →  screens (nodes)  +  transitions (edges)
screen      →  lifecycle (states) + business ops (model/data/api/rules/actions)
```

A single operation usually maps to one journey. Larger operations branch into sub-journeys that share screens (a
"checkout" journey hands off to an "add payment method" sub-journey and returns). Name journeys after the operation
("Checkout", "Onboarding", "Dispute a charge") so the graph is legible.

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

1. **Every `EXIT`/`NAVIGATION` destination is a real screen** in the graph, with a matching `ENTRY` on that screen
   naming this screen as a source. No dangling edges.
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

- Screens with `EXIT` to destinations that do not exist yet ("I'll add it later") — close the graph or stub the
  node explicitly.
- Re-declaring the tab/nav bar in every screen instead of a fragment.
- Modeling only the happy path — a transition out of `@error` and `@empty` is part of the journey.
- Putting business guards in two places (`BUSINESS_RULES` and `ACTIONS`) — see the authority chain in
  `ssdl-authoring.md`.
- Treating back as automatic — decide and declare it for each transition.
