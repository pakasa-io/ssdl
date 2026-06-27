## 37. FLOW section

Use `FLOW` for event-driven behavior in a concise form. `FLOW` owns event wiring only — see §31.3 for the authority
chain.

Lifecycle events used in `FLOW` (`screen.view`, `screen.first_view`, `screen.disappear`, `screen.destroy`,
`app.foreground`, `app.background`) share the same vocabulary as §32.1. User-initiated events (`tap`, `input.change`,
`keyboard.submit`, `scroll.near_end`, `long_press`, `swipe_left`, etc.) are FLOW-only. For analytics event triggers,
prefer `screen.first_view` over `screen.view` to avoid duplicate fires on every re-navigation to the screen.

```ssdl
FLOW {
  on screen.view do onScreenView()

  on input.change #email_input do {
    $error_msg := null
    validate $email
    recompute $form_valid
  }

  on tap #login_btn when $can_submit do submitLogin()

  on tap #forgot_link do nav ForgotPassword

  on keyboard.submit #password_input when $can_submit do submitLogin()
}
```

A flow line has one of these shapes:

```ssdl
on <event> [target] [when <condition>] do <effect>
on <event> [target] [when <condition>] ~> <ExternalOp>   // dispatch an async API/network call directly
```

The `~>` form wires an event straight to an asynchronous external operation — e.g.
`on tap #login_btn when $can_submit ~> LoginAPI.login` — for screens that need no hand-written `ACTIONS` function; its
success and failure route through `STATE_TRANSITIONS` (`api.success` / `api.failure`) and `ERRORS`. Use `do <action>()`
when the response needs procedural handling (validation, analytics, branching).

**FLOW event names** and **component `on <event>:` directive names** share the same vocabulary — `tap`, `long_press`,
`swipe_left`, `change`, `blur`, `submit`. The only difference is syntax: component blocks use
`on <event>: <effect> [when <condition>]`; FLOW lines use `on <event> [#target] [when <condition>] do <effect>`.
Lifecycle and system events always use dot-separated namespaces: `screen.view`, `api.success`, `scroll.end`,
`keyboard.submit`.

Examples:

```ssdl
on tap #retry_btn when @error do retryLastAction()
on api.success GetProfileAPI do set @loaded
on api.failure GetProfileAPI do set @error
on scroll.near_end #list when $has_next_page do loadNextPage()
on long_press #order_row do showOrderOptions($order)
on swipe_left #order_row do showDeleteConfirm($order)
```

---

