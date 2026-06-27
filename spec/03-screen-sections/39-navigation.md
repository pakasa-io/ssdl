## 39. NAVIGATION section

Use `NAVIGATION` for route transitions and stack behavior.

```ssdl
NAVIGATION {
  on login.success when $redirect_to.exists -> $redirect_to {
    replace_stack: true
  }

  on login.success when $redirect_to.empty -> Home {
    route: /home
    replace_stack: true
  }

  on tap #forgot_link -> ForgotPassword {
    route: /forgot-password
  }

  back_behavior {
    default: previous_screen
    when opened_from_session_expired: disabled
  }
}
```

Recommended navigation properties:

| Property        | Meaning                                           |
|-----------------|---------------------------------------------------|
| `route`         | Destination path                                  |
| `params`        | Destination params                                |
| `replace_stack` | Whether destination replaces history              |
| `presentation`  | `push`, `modal`, `sheet`, `replace`, `tab_switch` |
| `back_behavior` | Hardware/software back behavior                   |
| `deep_link`     | Associated deep link                              |

---

