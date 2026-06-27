## 31. State section

Use `STATES` to define named screen states and what the UI should do in each state. Declare the initial state with
`initial:` at the top of the block.

```ssdl
STATES {
  initial: @idle

  @idle {
    trigger: screen.view
    ui: show form, hide #error_banner
    allowed_actions: [editFields, tapForgotPassword]
  }

  @loading {
    trigger: submitLogin.started
    ui: disable form, show spinner in #login_btn
    allowed_actions: []
  }

  @error {
    trigger: submitLogin.failed
    ui: show #error_banner, enable form
    allowed_actions: [editFields, submitLogin]
  }
}
```

`initial:` is required when `STATE_TRANSITIONS` is present. It declares which state the screen enters on first load,
before any user interaction.

### 31.1 Recommended state names

```txt
@idle
@loading
@loaded
@empty
@valid
@invalid
@dirty
@saving
@success
@error
@offline
@permission_denied
@locked
@refreshing
```

### 31.2 State-transition table format

Use `STATE_TRANSITIONS` as the **machine-readable canonical form** for all state changes. `STATES` is the human-readable
summary. When both are present, `STATE_TRANSITIONS` governs implementation. If they conflict, update `STATES` to match.

```ssdl
STATE_TRANSITIONS {
  @idle + input.changed when $form_valid -> @valid
  @idle + input.changed when !$form_valid -> @invalid
  @valid + tap #submit_btn -> @loading
  @loading + api.success -> @success
  @loading + api.failure -> @error
  @error + input.changed -> @dirty
  @dirty + $form_valid -> @valid
  @dirty + !$form_valid -> @invalid
}
```

### 31.3 Logic authority chain

Three sections can express behavioral logic. Each owns a distinct responsibility:

| Section          | Owns                                                                                       | Does NOT own                           |
|------------------|--------------------------------------------------------------------------------------------|----------------------------------------|
| `FLOW`           | Event wiring — which event triggers which action or inline effect                          | Procedural logic, domain rules         |
| `BUSINESS_RULES` | Domain invariants — rules tied to product/business outcomes, independent of visual styling | UI event wiring, procedural steps      |
| `ACTIONS`        | Procedural logic — step-by-step sequences, async calls, match/if branching                 | Simple event wiring, pure domain rules |

When the same guard appears in multiple sections, **`ACTIONS` is authoritative for execution**; `BUSINESS_RULES`
documents intent; `FLOW` documents the trigger. Do not encode the same guard as both a `BUSINESS_RULES` condition and an
`if` guard inside an `ACTIONS` function — pick one. Use `BUSINESS_RULES` for declarations that QA and product can verify
independently of implementation; use `ACTIONS` for guards that require procedural context (e.g., checking earlier steps
in the same function).

---

