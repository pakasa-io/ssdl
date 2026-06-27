## 34. Validation section

Use `VALIDATION` for field-level validation rules.

```ssdl
VALIDATION {
  VAL-01: $email.empty => "Email is required"
  VAL-02: !$email.matches(email_regex) => "Enter a valid email"
  VAL-03: $password.empty => "Password is required"
  VAL-04: length($password) < 8 => "Password must be at least 8 characters"
}
```

### 34.1 Cross-field validation

Cross-field rules use the same `condition => message` syntax and may reference any number of model fields. Attach a
`fields:` hint to tell the UI which inputs should show the error.

```ssdl
VALIDATION {
  VAL-01: $email.empty => "Email is required"
  VAL-04: length($password) < 8 => "Password must be at least 8 characters"
  VAL-05: $confirm_password != $password => "Passwords do not match"
    fields: [$confirm_password]
  VAL-06: $end_date < $start_date => "End date must be after start date"
    fields: [$start_date, $end_date]
}
```

`fields:` is optional. When omitted the error is treated as a form-level (global) error. When present, the error is
shown inline on the listed fields.

Cross-field rules are evaluated on submit and re-evaluated when any of their referenced fields change after the first
submit attempt.

### 34.2 Async validation

Use the `async:` modifier for rules that require a server round-trip. The rule declares the intent; the implementation
lives in an `ACTIONS` function.

```ssdl
VALIDATION {
  VAL-07: $username.empty => "Username is required"
  VAL-08: async: checkUsernameAvailable($username)
    when: $username.length >= 3
    loading_msg: "Checking availability…"
    error_msg: "Username is already taken"
    fields: [$username]
}
```

| Property       | Meaning                                                                                 |
|----------------|-----------------------------------------------------------------------------------------|
| `async:`       | Reference to an ACTIONS function that returns `true` (valid) or `false` (invalid)       |
| `when:`        | Guard — only run the async check when this condition is true (avoids unnecessary calls) |
| `loading_msg:` | Copy shown while the check is in flight                                                 |
| `error_msg:`   | Copy shown when the check returns invalid                                               |
| `fields:`      | Which inputs show the inline error (same as cross-field rules)                          |

Async validation runs on field blur and on submit. Results are debounced — implementations should wait at least 300ms
after the last keystroke before firing.

### 34.3 Explicit no-validation marker

Fields that intentionally have no validation must be marked to pass LINT-008. Use `validation: none` on the component:

```ssdl
#phone_input: Input {
  label: "Phone (optional)"
  bind: $phone
  keyboard: phone
  validation: none
}
```

Or annotate in `VALIDATION`:

```ssdl
VALIDATION {
  $phone: no_validation    // Optional, collected for display only
  VAL-01: $email.empty => "Email is required"
}
```

Use `VALIDATION_UI` to specify when validation errors are displayed.

```ssdl
VALIDATION_UI {
  show field error after:
    - field.blur
    - submit attempted

  clear field error when:
    - user edits field

  form_submit:
    - set $submit_attempted := true
    - show all field errors
}
```

Recommended validation display conventions:

| Situation                        | Recommended behavior                                                                         |
|----------------------------------|----------------------------------------------------------------------------------------------|
| Field untouched                  | Do not show field error                                                                      |
| Field blurred and invalid        | Show field error                                                                             |
| Submit attempted                 | Show all relevant field errors                                                               |
| User edits invalid field         | Clear or live-update field error                                                             |
| Server-side error                | Show inline/global error as appropriate                                                      |
| Cross-field rule fails on blur   | Show on submit or when the second referenced field is blurred, not on the first field's blur |
| Cross-field rule fails on submit | Show on all fields listed in `fields:`; show as form-level error if `fields:` omitted        |

---

