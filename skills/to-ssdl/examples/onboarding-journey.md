# Worked example — the "Sign in" operation as a stitched journey

A compact, illustrative walkthrough of `to-ssdl` output: the operation **"a returning user signs in"** modelled as a
three-screen journey — navigation-stitched, **grounded in KB facts**, with a **consistent app shell**. Files follow
`references/output-structure.md` (screens under `features/<feature>/`, shared details under `shared/`). Syntax is
illustrative — the authoritative grammar and directive options come from the spec bundled with this skill via
`agent.manifest.yml` (load `sections.route`, `sections.model`, etc.).

## Journey map (Phase 4 artifact)

```
Onboarding · Sign-in
  Welcome ──signIn──▶ Login ──auth.success⇒──▶ Home
   (public)            (public)                 (authenticated)
   chrome: auth        chrome: auth             extends AppShell
      └──register──▶ SignUp  (hand-off → Register journey)
  Entry:  Welcome (cold start; deeplink /welcome)   ·   Login (deeplink /login)
  Exit:   Home (replace-stack)  ·  SignUp (hand-off → Register journey)
  App shell: Welcome/Login are the `auth` exception (pre-auth, no chrome); Home extends AppShell.
  ⇒ = replace-stack — back must not return to Login after success
```

Closure check: every `EXIT` lands on a real node — `SignUp` is a hand-off to the separate **Register** journey, not
a dangling edge; `Welcome`/`Login` are reachable from app entry; `auth.success` replaces the stack so back cannot
re-expose `Login`; `Home` requires auth and is reached only via success.

## Grounding: KB facts before authoring (Phase 2 → Phase 5)

Login's fields aren't invented — they're extracted from the auth contract into the KB, then fed forward. Phase 5
pulls **only this screen's** facts (the shared error/validator contracts were captured in Phase 2):

```yaml
# app-spec/kb/2-data-and-contracts/13-MODEL.yaml  (excerpt — the login request)
element: MODEL
extracted_from: [ "openapi:POST /auth/login" ]
facts:
  request:
    LoginRequest:
      applies_to: [Login]          # appended retrospectively as Login is built
      attrs:
        - { attr: email,    type: string, format: email, required: true }
        - { attr: password, type: string, required: true, minLength: 8, sensitive: true }
feeds: [UI, VALIDATION, ANALYTICS, ACCEPTANCE]
```

One extracted attribute then propagates via the card's `feeds`:

```
email { format: email, required: true }
  ├─▶ MODEL       $email!: Email := ""
  ├─▶ VALIDATION  VAL-01: !matchesEmail($email) => copy.err.email
  ├─▶ UI          #email: Input bind:$email keyboard:email
  └─▶ ANALYTICS   privacy.never_send: [$email]
```

## The app shell — defined once (fragment → base → screens)

Chrome is composed in three layers: the **fragment** holds the components; the **`AppShell` base** imports them once
into fixed slots (the only place the fragment is imported — LINT-054); each **in-app screen `extends AppShell`**,
inheriting the chrome and filling `#body`. Screens never import or re-declare chrome themselves.

```ssdl
# shared/nav.app-shell.fragment.ssdl — the chrome components
FRAGMENT navigation v1
export { #app_tab_bar }
#app_tab_bar: TabBar { items: [ TabItem label:copy.nav.home    route:/home
                                TabItem label:copy.nav.search  route:/search
                                TabItem label:copy.nav.profile route:/profile ] }
```

```ssdl
# shared/layouts/app.shell.base.ssdl — the frame every in-app screen extends
SCREEN AppShell v1
import { #app_tab_bar } from "@shared/navigation.ssdl" at v1
UI {
  #screen:      SafeArea { children: [#content, #app_tab_bar] }
  #content:     Scroll { in:#screen size:w:fill h:fill children:[#body] }
  #body:        VStack { in:#content }               // the content slot each screen overrides
  #app_tab_bar: TabBar { pos: sticky(bottom.safe) }  // inherited chrome, declared once
}
```

## `features/auth/screen.auth.welcome.ssdl` — an `auth` exception (no shell)

Pre-auth and single-task, so it opts out of the shell — declared with `// chrome: auth`, never silent.

```ssdl
SCREEN Welcome v1        // chrome: auth — pre-app, no tab bar (app-shell exception)

META { feature: onboarding, owner: Growth, platform: all, status: draft, changelog: { v1: "Initial" } }
PURPOSE { Greet a user and route them to sign in or register. }
SCOPE { in: [first impression, choose sign-in vs register]  out: [actual auth, password reset] }
ROUTE { path: /welcome, access: public, params: { } }

ENTRY { - from: AppLaunch when: not authenticated
        - from: DeepLink   when: link == /welcome }
EXIT  { - to: Login  when: tap #sign_in
        - to: SignUp when: tap #register }   // hand-off → Register journey

MODEL { }   // static routing screen — no model state
COPY  { screen.title: "Welcome back" }

UI {
  #screen:   SafeArea { children: [#logo, #sign_in, #register] }
  #logo:     Img  src:copy.brand.logo pos:top.center
  #sign_in:  Btn  "Sign in"        pos:above(#register, md)
  #register: Link "Create account" pos:bottom.center
}

STATES { initial: @idle  @idle { trigger: screen.view } }
NAVIGATION { on tap #sign_in  -> Login  { route:/login }
             on tap #register -> SignUp { route:/signup } }
A11Y { focus_order: [#logo, #sign_in, #register]  touch_targets: >=44pt  contrast: wcag_aa }
ACCEPTANCE {
  AC-01: Given an unauthenticated launch, When Welcome shows, Then #sign_in and #register are reachable.
}
```

## `features/auth/screen.auth.login.ssdl` — `auth` exception, authored from KB facts

Full-mode version is `assets/sample.login.ssdl`. `MODEL`/`VALIDATION` come straight from the KB card above; the
excerpt shows the grounding + stitching + state machine.

```ssdl
SCREEN Login v1        // chrome: auth — pre-app, no tab bar

ROUTE { path: /login, access: public, params: { redirect?: string } }
MODEL { $email!: Email := ""   $password!: Password := "" }        // from KB LoginRequest.attrs
VALIDATION { VAL-01: !matchesEmail($email) => copy.err.email }     // from email { format: email }

ENTRY { - from: Welcome  when: tap #sign_in
        - from: DeepLink when: link == /login }
EXIT  { - to: Home           when: auth.success        // replace-stack
        - to: ForgotPassword when: tap #forgot }

STATES { initial: @idle  @idle {…}  @loading {…}  @error {…}  @success {…} }
STATE_TRANSITIONS {
  @idle    + tap #submit  -> @loading
  @loading + auth.success -> @success
  @loading + auth.failure -> @error
  @error   + tap #submit  -> @loading
}
ACTIONS {
  submitLogin() { set @loading
    response = LoginAPI.login(email:$email, password:$password) ~> POST /auth/login
    match response.status: 200 => set @success  else => set @error }
}
NAVIGATION { on auth.success -> Home { route: $redirect ?? /home, replace: stack }
             on tap #forgot  -> ForgotPassword { route:/forgot } }
```

Design judgments: `redirect?` lets a deep link send the user onward after auth; `replace: stack` on success so back
cannot return to `Login`; `@error → @loading` lets the user retry in place.

## `features/home/screen.home.dashboard.ssdl` — in-app, `extends AppShell`

Home inherits the shell (tab bar + frame) from the base and overrides only `#body`. It does **not** import or
re-declare the chrome.

```ssdl
SCREEN Home v1 extends AppShell v1        // inherits the app shell; fills #body

ROUTE { path: /home, access: authenticated, params: { } }

ENTRY { - from: Login     when: auth.success       // arrived via replace-stack
        - from: AppLaunch when: authenticated }     // warm start lands here, not Welcome
EXIT  { - to: Search  when: tap #app_tab_bar.search    // reason: inherited tab item routes
        - to: Profile when: tap #app_tab_bar.profile } // reason: inherited tab item routes

LIFECYCLE { on screen.view do loadDashboard()
            on app.foreground do refreshIfStale() }

STATES { initial: @loading  @loading {…}  @empty {…}  @error {…}  @ready {…} }
STATE_TRANSITIONS {
  @loading + data.loaded -> @ready
  @loading + data.empty  -> @empty
  @loading + data.failed -> @error
  @error   + tap #retry  -> @loading
}
ACTIONS { loadDashboard()  { set @loading }        // resolves to @ready / @empty / @error
          refreshIfStale() { if stale: loadDashboard() } }

OVERRIDE { UI { replace: #body with #dashboard } }  // body switches on @state; #retry in the @error view

A11Y { focus_order: [#app_tab_bar, #dashboard]  contrast: wcag_aa }
ACCEPTANCE {
  AC-01: Given a successful sign-in, When Home loads, Then the inherited tab bar is present and back does not return to Login.
  AC-02: Given a warm start while authenticated, When the app opens, Then Home is the entry, not Welcome.
}
```

## Why this is a *journey*, not three screens

- The graph is **closed**: `Welcome.EXIT→Login`, `Login.EXIT→Home`, each with a matching `ENTRY` naming its source.
- **Back is decided** per edge: push (Welcome→Login) vs replace-stack (Login→Home).
- **Cross-screen state** (the auth boundary) is explicit: `access:` flips `public` → `authenticated` at the success
  edge, and the warm-start `ENTRY` on `Home` reflects an existing session.
- **Grounded in facts**: Login's `MODEL`/`VALIDATION` come from the extracted KB card, not invented.
- **Consistent shell, declared exceptions**: `Home extends AppShell` (chrome inherited); `Welcome`/`Login` opt out
  with `// chrome: auth`. One shell, applied by inheritance, exceptions never silent.
