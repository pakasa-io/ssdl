## 3. SSDL shorthand symbols

| Symbol / keyword     | Meaning                                                  | Example                                           |
|----------------------|----------------------------------------------------------|---------------------------------------------------|
| `SCREEN`             | Declares the screen                                      | `SCREEN Login v1`                                 |
| `extends`            | Screen inherits from a base screen                       | `SCREEN GuestCheckout v1 extends Checkout v2`     |
| `META`               | Ownership and lifecycle metadata                         | `status: ready`                                   |
| `ROUTE`              | Route, params, auth, entry type                          | `path: /login`                                    |
| `PERMISSIONS`        | OS permission declarations                               | `camera { ... }`                                  |
| `FEATURE_FLAGS`      | Feature flag declarations                                | `new_ui { when enabled: ... }`                    |
| `MODEL`              | Screen-local data fields                                 | `$email!: Email := ""`                            |
| `$field`             | Screen model field                                       | `$password`                                       |
| `!`                  | Required field                                           | `$email!`                                         |
| `?`                  | Optional field or param                                  | `$avatar_url?`                                    |
| `#id`                | UI component ID                                          | `#login_btn`                                      |
| `@state`             | Screen state                                             | `@loading`                                        |
| `:=`                 | Assignment or default value                              | `$remember_me := false`                           |
| `==>`                | Derived/computed field                                   | `$can_submit ==> $form_valid && !$is_loading`        |
| `=>`                 | Effect/result                                            | `401 => show #error_banner`                       |
| `->`                 | Navigation or transition                                 | `login.success -> Home`                           |
| `~>`                 | Async call / external operation                          | `submit ~> POST /auth/login`                      |
| `on`                 | Event trigger                                            | `on tap #submit_btn`                              |
| `when`               | Guard/condition                                          | `when $can_submit`                                |
| `do`                 | Execute action                                           | `do submitLogin()`                                |
| `emit`               | Analytics/event emission                                 | `emit login_submitted`                            |
| `show` / `hide`      | Visibility effect                                        | `show #error_banner`                              |
| `enable` / `disable` | Interactivity effect                                     | `disable #submit_btn`                             |
| `nav`                | Navigate to destination                                  | `nav Home`                                        |
| `animate`            | Animation directive                                      | `animate: fade_in(sm)`                            |
| `transition`         | Shared element transition                                | `transition: shared(#avatar)`                     |
| `BR-xx`              | Business rule ID                                         | `BR-01`                                           |
| `VAL-xx`             | Validation rule ID                                       | `VAL-02`                                          |
| `ERR-xx`             | Error case ID                                            | `ERR-401`                                         |
| `AC-xx`              | Acceptance criterion ID                                  | `AC-05`                                           |
| `import`             | Import named items from a fragment file                  | `import { copy.common } from "@shared/copy.ssdl"` |
| `from`               | Source path in an import declaration                     | `from "@shared/nav.ssdl"`                         |
| `at`                 | Version pin on an import                                 | `from "@shared/nav.ssdl" at v2`                   |
| `as`                 | Rename an imported item                                  | `import { LoginAPI } as Auth from ...`            |
| `include`            | Inline-embed section content from a fragment             | `include "@standards/a11y.ssdl"`                  |
| `export`             | Mark a fragment item as publicly importable              | `export #app_nav`                                 |
| `FRAGMENT`           | Fragment file header declaration                         | `FRAGMENT navigation v1`                          |
| `FRAGMENT_META`      | Changelog and metadata for a fragment file               | `FRAGMENT_META { changelog: { ... } }`            |
| `@alias`             | Project-root path alias (configured in ssdl.config.json) | `@shared/nav.ssdl`                                |

## 3.1 DDL alias layer and compact shorthand mapping

SSDL supports both full section names and compact aliases. The full names are preferred for production handoff; aliases
are allowed for fast drafting.

### Section aliases

| Compact alias     | Full section                                                                                                                              |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `VAL`             | `VALIDATION`                                                                                                                              |
| `BR`              | `BUSINESS_RULES`                                                                                                                          |
| `ACTION <name>()` | Single function inside `ACTIONS`; compact form omits `ACTIONS { }` block and `{ }` around the function body — indented lines are the body |
| `ACTIONS`         | `ACTIONS { ... }` — full form; use when declaring multiple functions                                                                      |
| `AC`              | `ACCEPTANCE`                                                                                                                              |
| `A11Y`            | `A11Y`                                                                                                                                    |
| `NAV`             | `NAVIGATION`                                                                                                                              |

Example:

```ssdl
VAL
  $email.empty => "Email is required"
```

Equivalent full form:

```ssdl
VALIDATION {
  VAL-01: $email.empty => "Email is required"
}
```

### Property aliases

| Compact alias          | Full directive                                                                                        |
|------------------------|-------------------------------------------------------------------------------------------------------|
| `show:<condition>`     | `visible_when: <condition>`                                                                           |
| `hide:<condition>`     | `hidden_when: <condition>`                                                                            |
| `enabled:<condition>`  | `enabled_when: <condition>`                                                                           |
| `loading:<condition>`  | `loading_when: <condition>`                                                                           |
| `on <event>: <action>` | component event handler — `on tap: action()`, `on long_press: action()`, `on change: validate $field` |
| `-> Destination`       | `on tap: nav Destination` when used on an interactive component                                       |
| `access:auth`          | `access: authenticated`                                                                               |
| `Bool`                 | `Boolean`                                                                                             |

Example:

```ssdl
#submit: Btn "Log In" enabled:$can_submit loading:@loading on tap:submitLogin()
```

Equivalent full form:

```ssdl
#submit: Btn "Log In" {
  enabled_when: $can_submit
  loading_when: @loading
  on tap: submitLogin()
}
```

### Copy aliases

For text-like components, `text:` and the inline quoted string both represent visible copy.

```ssdl
#title: Txt "Welcome back"
```

Equivalent:

```ssdl
#title: Txt {
  text: "Welcome back"
}
```

For input-like components, `label:` represents the user-visible field label.

```ssdl
#email_input: Input {
  label: copy.login.email_label
}
```

**`text:` vs `label:` — pick by role:**

- `text:` is a component's own visible content — the string that *is* the element. Use it on display components (`Txt`,
  `RichTxt`, `Banner`) and on action rows whose body is the text (`Btn`, `Link`, `ActionSheet` actions, `SpeedDialItem`,
  `ContextMenuItem`).
- `label:` is a separate affordance descriptor for a control that carries other chrome — an input's field label, a
  `Chk` / `Switch` caption, a `TabItem` / `DrawerItem` label beside its icon, or a `FormGroup` section label.

---

