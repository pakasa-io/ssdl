# SSDL Completeness Checklist

Run through this before marking a screen spec `status: ready`. Part of the [SSDL specification](../ssdl.spec.md).

## Imports

- [ ] All `import` declarations include `at v<n>` version pins.
- [ ] Every `@alias` path is defined in `ssdl.config.json`.
- [ ] No circular import dependencies (LINT-047).
- [ ] All imported items are referenced somewhere in the spec body (LINT-053).
- [ ] No two imports conflict on the same ID (LINT-049).
- [ ] `include` directives appear before screen-specific overrides in their section (LINT-052).

## Identity and scope

- [ ] Screen has a stable `SCREEN` name and version.
- [ ] `META.status` is correct.
- [ ] `META.changelog` entry exists for this version.
- [ ] `PURPOSE` is clear.
- [ ] `SCOPE.in` and `SCOPE.out` prevent accidental feature creep.

## Routing, navigation, and access

- [ ] Route path is defined.
- [ ] Required route params are marked with `!`.
- [ ] Optional route params are marked with `?`.
- [ ] Entry points are listed.
- [ ] Exit points are listed.
- [ ] Back behavior is specified.
- [ ] Deep links are included if relevant.
- [ ] `PERMISSIONS` section is present if the screen accesses camera, location, notifications, contacts, or biometrics.
- [ ] `FEATURE_FLAGS` section is present if any component visibility is flag-gated.

## Data and model

- [ ] All UI-bound fields exist in `MODEL`.
- [ ] Derived fields are defined with `==>`.
- [ ] Defaults are defined for fields that need them.
- [ ] Data sources are listed in `DATA.read`.
- [ ] Cache strategy is specified for remote reads.
- [ ] Writes/storage effects are listed in `DATA.write`.

## UI and layout

- [ ] Every UI component has a unique `#id`.
- [ ] Every non-root component has an `in:` parent.
- [ ] Parent `children` lists are consistent with child `in:` values.
- [ ] Critical layout intent uses `pos`, `align`, `size`, and spacing directives.
- [ ] All text-bearing components have a `style:` token.
- [ ] Keyboard behavior is specified for form screens.
- [ ] Loading, empty, error, and success states are represented where relevant.
- [ ] Collection components specify `pagination:` strategy.
- [ ] Collection components specify `empty_state:`.

## States and lifecycle

- [ ] `STATES` covers all meaningful screen states.
- [ ] `STATES` declares `initial:`.
- [ ] `STATE_TRANSITIONS` is present for screens with three or more states.
- [ ] Every state in `STATES` is reachable via `STATE_TRANSITIONS`.
- [ ] `LIFECYCLE` is present for screens that need to respond to re-view, foreground, or background events.
- [ ] Lifecycle handlers that perform async work specify failure behavior.

## Animation

- [ ] `ANIMATION` is present if the screen uses non-trivial enter/exit motion.
- [ ] Every animation has a `reduced_motion` alternative.
- [ ] Shared element transitions are matched between source and destination screens.

## Logic and flow

- [ ] User events are represented in `FLOW`.
- [ ] Complex behavior has pseudocode in `ACTIONS`.
- [ ] Business rules are testable and referenced by behavior.
- [ ] Async behavior includes loading and failure handling.
- [ ] State transitions are clear.
- [ ] No guard is encoded redundantly in both `BUSINESS_RULES` and `ACTIONS`.

## API and errors

- [ ] API request shape is defined.
- [ ] API success response shape is defined.
- [ ] Known error statuses are defined.
- [ ] Every API error status has an `ERRORS` entry or an inline `// handled:` annotation.
- [ ] Timeout/network/offline behavior is specified where relevant.

## Copy, analytics, accessibility, QA

- [ ] User-facing strings are listed in `COPY` or intentionally inline.
- [ ] Parameterized copy uses ICU format where needed.
- [ ] Analytics events include trigger and properties.
- [ ] `ANALYTICS.privacy` block is present for auth/payment/personal-data screens.
- [ ] `ANALYTICS.privacy.consent` is declared for screens subject to consent requirements.
- [ ] Analytics events declare `dedup:` strategy.
- [ ] Accessibility focus order is listed.
- [ ] Screen reader labels are included for key elements.
- [ ] Non-obvious semantic roles are declared in `A11Y.roles`.
- [ ] `contrast:` is specified in `A11Y`.
- [ ] `NAVIGATION` destinations are consistent with `EXIT` destinations.
- [ ] `ACTORS.systems` entries correspond to API or DATA entries.
- [ ] Acceptance criteria cover happy path, validations, errors, navigation, re-view behavior, and accessibility.
