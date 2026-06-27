## 36. ACTIONS section with pseudocode

Use `ACTIONS` for procedural logic. Keep pseudocode readable and implementation-agnostic.

```ssdl
ACTIONS {
  submitLogin() {
    $submit_attempted := true

    validate $email
    validate $password

    if !$form_valid:
      set @invalid
      return

    set @loading
    // $is_loading is derived from @loading — no manual assignment needed
    $error_msg := null

    emit login_submitted {
      source: $entry_source,
      email_present: $email.exists
    }

    response = await LoginAPI.login({
      email: trim($email),
      password: $password
    })

    // @loading is cleared by state transitions below (set @success / @error)

    match response.status:
      200 => handleLoginSuccess(response)
      401 => handleInvalidCredentials()
      423 => handleLockedAccount()
      else => handleGenericLoginError(response)
  }
}
```

### 36.1 Pseudocode conventions

| Pattern                   | Meaning                   |
|---------------------------|---------------------------|
| `if condition:`           | Conditional branch        |
| `match value:`            | Switch/case branch        |
| `await`                   | Await an in-process async op (local DB, timer)  |
| `$x = ~> Api.method(...)` | Async external/network call; binds result       |
| `return`                  | Stop current action       |
| `set @state`              | Change screen state       |
| `$field := value`         | Assign model value        |
| `emit event_name { ... }` | Track event               |
| `nav Destination`         | Navigate                  |
| `validate $field`         | Run validation rules      |
| `recompute $field`        | Recalculate derived value |

Use `~>` for operations that cross the app boundary (API, network, IPC); reserve `await` for in-process async (local
database, timers, file I/O). In FLOW, `on <event> ~> <Api.method>` dispatches the external call directly (§37).

---

