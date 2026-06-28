## 48. Compact mode

Compact mode is useful for early drafts.

```ssdl
SCREEN Login v1
ROUTE /login access:public

MODEL
  $email!: Email := ""
  $password!: String := ""
  $error_msg?: String
  $valid ==> matchesEmail(trim($email)) && length($password) >= 8
  $is_loading ==> @loading
  $can_submit ==> $valid && !$is_loading

UI
  #screen: SafeArea size:w:screen h:screen
  #content: Scroll in:#screen pos:safe.top size:w:fill h:fill pad:lg behavior:scroll_when_keyboard_open
  #form: VStack in:#content pos:center align:stretch gap:md
  #email: Input "Email" in:#form bind:$email keyboard:email size:w:fill h:lg
  #password: Pwd "Password" in:#form bind:$password size:same_w(#email) h:lg
  #forgot: Link "Forgot password?" in:#form align:end -> ForgotPassword
  #error: Banner $error_msg in:#form show:$error_msg.exists
  #submit: Btn "Log In" in:#form size:w:fill h:lg enabled:$can_submit loading:@loading on tap:submitLogin()

VAL
  $email.empty => "Email is required"
  !$email.matches(email_regex) => "Enter a valid email"
  $password.empty => "Password is required"
  length($password) < 8 => "Password must be at least 8 characters"

FLOW
  view => emit login_viewed
  tap #submit when $can_submit => submitLogin()
  tap #forgot => nav ForgotPassword

ACTION submitLogin()
  if !$can_submit return
  set @loading
  res = ~> POST /auth/login { email:$email, password:$password }
  match res.status:
    200 => securelyStore("auth_token", res.token); emit login_success; nav Home
    401 => $error_msg="Email or password is incorrect."; set @error
    500 => $error_msg="Something went wrong."; set @error
    else => $error_msg="Something went wrong."; set @error

AC
  Given invalid form Then #submit disabled
  Given valid form When tap #submit Then call POST /auth/login
  Given 200 Then nav Home
  Given 401 Then show invalid credentials error
  Given 500 Then show generic error
```

### 48.1 Compact mode grammar rules

| Element          | Compact form                                    | Full form equivalent                                                                       |
|------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------|
| Section header   | `MODEL` (no braces)                             | `MODEL { ... }`                                                                            |
| Validation rule  | `$email.empty => "Email is required"`           | `VAL-01: $email.empty => "Email is required"` — IDs are auto-assigned during expansion     |
| Single action    | `ACTION submitLogin()` + indented body          | `ACTIONS { submitLogin() { ... } }` — no `{ }` around body; indentation delimits the block |
| Multiple actions | Not supported — use full `ACTIONS { }`          | `ACTIONS { fn1() { ... } fn2() { ... } }`                                                  |
| Flow event       | `tap #submit when $can_submit => submitLogin()` | `on tap #submit when $can_submit do submitLogin()`                                         |
| AC entry         | `Given ... Then ...` (no ID)                    | `AC-01: Given ... Then ...` — IDs assigned during expansion                                |

**ID assignment during expansion:** `VAL`, `AC`, `BR`, and `ERR` entries without explicit IDs are assigned IDs
sequentially in source order (`VAL-01`, `VAL-02`…). If an entry already has an ID it is kept as-is. Gaps in numbering
after partial expansion are allowed.

Compact mode can be expanded into full mode before engineering handoff.

---

