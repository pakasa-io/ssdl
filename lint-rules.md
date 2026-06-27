# SSDL Linting Rules

Automated-review rules for SSDL screen specs — usable by a script, AI reviewer, or human reviewer. These rule IDs (`LINT-xxx`) are referenced throughout the [SSDL specification](ssdl.spec.md); section references such as `§48.7` point back to it.

```txt
LINT-001: Every component ID must be unique.
LINT-002: Every referenced component ID must exist.
LINT-003: Every referenced model field must exist in MODEL.
LINT-004: Every referenced COPY key must exist in COPY.
LINT-005: Every required route param must be consumed, passed onward, or intentionally ignored.
LINT-006: Every API error status must have an ERRORS entry or an inline // handled: annotation.
LINT-007: Every primary action must have at least one acceptance criterion.
LINT-008: Every form field must have validation or be explicitly marked validation:none or no_validation.
LINT-009: Every loading async action must specify a loading state.
LINT-010: Every critical navigation path must appear in NAVIGATION and ACCEPTANCE.
LINT-011: Every interactive component must have an accessibility label or inherit one from visible text.
LINT-012: Every analytics event must avoid prohibited sensitive fields.
LINT-013: A ready spec must have no unresolved OPEN_QUESTIONS (status: open or pending_*).
LINT-014: UI child-parent references must be internally consistent.
LINT-015: Visibility/enabled/loading conditions must reference valid fields or states.
LINT-016: Every component with style: must use a token from the defined style vocabulary (§48.7).
LINT-017: Every component that requires an OS permission must have a PERMISSIONS entry.
LINT-018: Every feature-flag-gated component must have a FEATURE_FLAGS entry.
LINT-019: Every List or Scroll component must specify pagination: strategy or explicitly set pagination: none.
LINT-020: OPEN_QUESTIONS with blocks: ready prevent status: ready.
LINT-021: Every LIFECYCLE event handler must reference a defined ACTIONS function or inline effect.
LINT-022: ANALYTICS.privacy block is required when the screen processes auth, payment, or personal data.
LINT-023: STATE_TRANSITIONS must be present when STATES defines three or more states.
LINT-024: Every animate: or transition: directive must have a corresponding reduced_motion alternative in ANIMATION.
LINT-025: Screen variants (extends) must not redefine SCREEN version; OVERRIDE is the only permitted diff mechanism.
LINT-026: Derived fields (==>) must not form circular dependencies; each derived field's dependency graph must be acyclic.
LINT-027: STATES must declare initial: when STATE_TRANSITIONS is present; the declared initial state must be defined in STATES.
LINT-028: ANALYTICS.privacy.consent must be present when ANALYTICS.privacy block is required (auth/payment/personal-data screens).
LINT-029: Every state defined in STATES must be reachable via at least one transition in STATE_TRANSITIONS (when STATE_TRANSITIONS is present).
LINT-030: Every destination in NAVIGATION must also appear in EXIT (and vice versa); entries present in one but absent from the other must have a // reason: comment.
LINT-031: Every component ID referenced in FLOW event targets must exist in the UI section.
LINT-032: Every entry in ACTORS.systems must correspond to an API or DATA section entry, or carry a // reason: comment explaining the exception.
LINT-033: OTPInput must declare length:.
LINT-034: Carousel must declare on slide_change: or explicitly annotate // on slide_change: not tracked.
LINT-035: NavBar must declare title:.
LINT-036: TabBar must declare items: and on tab_change:.
LINT-037: EmptyState must declare title: and cta:.
LINT-038: Progress must declare value: or indeterminate: true; declaring neither is a spec error.
LINT-039: PullToRefresh must declare on refresh: and refreshing: bound to a model field or state.
LINT-040: Scanner must declare on scan: and have a corresponding PERMISSIONS.camera entry.
LINT-041: MapView with interactive: true displaying user location must have a PERMISSIONS.location.when_in_use entry.
LINT-042: Table with selection: single or selection: multi must declare on row_tap:.
LINT-043: Accordion must declare on expand: or annotate // on expand: not tracked.
LINT-044: Drawer must declare on open: and on close:.
LINT-045: SearchBar must declare on cancel:.
LINT-046: ContextMenu ContextMenuItem components must each declare on tap:.

// Import and fragment rules
LINT-047: The import graph (across all screen and fragment files) must be acyclic. Circular imports are reported on the file that closes the cycle.
LINT-048: Every path referenced in an import or include declaration must resolve to an existing fragment file.
LINT-049: Two import declarations that bring in the same ID conflict — the later import wins; both declarations receive a warning. Resolve cleanly using as aliasing.
LINT-050: Importing a non-exported item from a fragment that has explicit export declarations is an error.
LINT-051: A local section declaration that shadows an imported item of the same ID receives a warning — local wins, but the shadow should be intentional.
LINT-052: A section declaration that appears before an include and is overridden by that include receives a warning. Move declarations after include if they are intended as overrides.
LINT-053: An imported item that is never referenced anywhere in the importing screen spec (not in UI children:, not in FLOW, not in ACTIONS, not in ERRORS, not in COPY, etc.) should be removed or annotated // imported for: <reason>.
```
