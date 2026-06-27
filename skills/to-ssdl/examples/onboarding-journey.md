# Worked example — the "Sign in" operation as a stitched journey

A compact, illustrative walkthrough of `to-ssdl` output: the business operation **"a returning user signs in"**
modelled as a three-screen journey, navigation-stitched, with one shared fragment. Syntax here is illustrative —
the authoritative grammar and exact directive options come from the spec via `agents/agent.manifest.yml` (load
`sections.route`, `sections.navigation`, etc.).

## Journey map (Phase 4 artifact)

```
Onboarding · Sign-in
  Welcome ──signIn──▶ Login ──auth.success⇒──▶ Home
   (public)            (public)                 (authenticated)
      └──register──▶ SignUp ─(out of scope here)
  Entry:  Welcome (cold start; deeplink /welcome)   ·   Login (deeplink /login)
  Exit:   Home (replace-stack), SignUp
  ⇒ = replace-stack — back must not return to Login after success
  Shared: shared.navigation.fragment.ssdl (#app_tab_bar) imported by Home
```

Closure check: every `EXIT` lands on a real node; `Welcome`/`Login` are reachable from app entry; `auth.success`
replaces the stack so back cannot re-expose `Login`; `Home` requires auth and is reached only via success.

## `screen.auth.welcome.ssdl`

```ssdl
SCREEN Welcome v1

META { feature: onboarding, owner: Growth, platform: all, status: draft,
       changelog: { v1: "Initial" } }

PURPOSE { Greet a returning or new user and route them to sign in or register. }
SCOPE { in: [first impression, choose sign-in vs register]  out: [actual auth, password reset] }

ROUTE { path: /welcome, type: screen, access: public, params: { } }

ENTRY {
  - from: AppLaunch when: not authenticated
  - from: DeepLink   when: link == /welcome
}
EXIT {
  - to: Login  when: tap #sign_in
  - to: SignUp when: tap #register
}

MODEL { $is_loading ==> false }

COPY { screen.title: "Welcome back" }

UI {
  #screen: SafeArea { children: [#logo, #sign_in, #register] }
  #logo:     Img    src:copy.brand.logo pos:top.center
  #sign_in:  Btn    "Sign in"      pos:above(#register, md) on tap:goSignIn()
  #register: Link   "Create account" pos:bottom.center      on tap:goRegister()
}

STATES { initial: @idle  @idle { trigger: screen.view } }

FLOW {
  on tap #sign_in  do goSignIn()
  on tap #register do goRegister()
}

NAVIGATION {
  on sign_in.tap  -> Login  { route: /login }
  on register.tap -> SignUp { route: /signup }
}

A11Y { focus_order: [#logo, #sign_in, #register]  touch_targets: >=44pt  contrast: wcag_aa }

ACCEPTANCE {
  AC-01: Given an unauthenticated launch, When Welcome shows, Then #sign_in and #register are reachable.
  AC-02: Given a tap on #sign_in, When it fires, Then the user navigates to Login.
}
```

## `screen.auth.login.ssdl`

The full-mode version of this screen is `assets/sample.login.ssdl` — reuse it. The stitching that matters for the
journey:

```ssdl
SCREEN Login v1

ROUTE { path: /login, type: screen, access: public, params: { redirect?: string } }

ENTRY {
  - from: Welcome  when: tap #sign_in
  - from: DeepLink when: link == /login
}
EXIT {
  - to: Home          when: auth.success          // replace-stack
  - to: ForgotPassword when: tap #forgot
}

# MODEL / UI / VALIDATION / ACTIONS / API as in assets/sample.login.ssdl …

STATES {
  initial: @idle
  @idle { trigger: screen.view }
  @loading { trigger: async.started }
  @error   { trigger: async.failed }
  @success { trigger: async.succeeded }
}
STATE_TRANSITIONS {
  @idle    + tap #submit     -> @loading
  @loading + auth.success    -> @success
  @loading + auth.failure    -> @error
  @error   + tap #submit     -> @loading
}

ACTIONS {
  submitLogin() {
    set @loading
    response = LoginAPI.login(email: $email, password: $password) ~> POST /auth/login
    match response.status:
      200 => set @success
      else => set @error
  }
}

NAVIGATION {
  on auth.success -> Home { route: $redirect ?? /home, replace: stack }
  on tap #forgot  -> ForgotPassword { route: /forgot }
}
```

Note the design judgments: `redirect?` route param lets a deep link send the user onward after auth;
`replace: stack` on success so back cannot return to `Login`; `@error → @loading` lets the user retry without
leaving the screen.

## `shared.navigation.fragment.ssdl`

```ssdl
FRAGMENT navigation v1
FRAGMENT_META { owner: Platform, changelog: { v1: "App shell tab bar" } }

export { #app_tab_bar }

#app_tab_bar: TabBar {
  items: [
    TabItem label:copy.nav.home    icon:home    route:/home
    TabItem label:copy.nav.search  icon:search  route:/search
    TabItem label:copy.nav.profile icon:profile route:/profile
  ]
  on tab_change: switchTab()
}
```

## `screen.home.dashboard.ssdl` (journey destination)

```ssdl
SCREEN Home v1

import { #app_tab_bar } from "@shared/navigation.ssdl" at v1

ROUTE { path: /home, type: screen, access: authenticated, params: { } }

ENTRY {
  - from: Login   when: auth.success         // arrived via replace-stack
  - from: AppLaunch when: authenticated       // warm start lands here, not Welcome
}
EXIT {
  - to: Search  when: tap #app_tab_bar.search
  - to: Profile when: tap #app_tab_bar.profile
}

LIFECYCLE {
  on screen.view    do loadDashboard()
  on app.foreground do refreshIfStale()
}

STATES {
  initial: @loading
  @loading { trigger: screen.view }
  @empty   { trigger: data.empty }
  @error   { trigger: data.failed }
  @ready   { trigger: data.loaded }
}
STATE_TRANSITIONS {
  @loading + data.loaded  -> @ready
  @loading + data.empty   -> @empty
  @loading + data.failed  -> @error
  @error   + tap #retry   -> @loading
}

# UI imports #app_tab_bar as persistent chrome; body switches on @state …

A11Y { focus_order: [#app_tab_bar]  contrast: wcag_aa }

ACCEPTANCE {
  AC-01: Given a successful sign-in, When Home loads, Then the tab bar is present and back does not return to Login.
  AC-02: Given a warm start while authenticated, When the app opens, Then Home is the entry, not Welcome.
}
```

## Why this is a *journey*, not three screens

- The graph is **closed**: `Welcome.EXIT→Login`, `Login.EXIT→Home`, each with a matching `ENTRY` naming its source.
- **Back is decided** per edge: push (Welcome→Login) vs replace-stack (Login→Home).
- **Cross-screen state** (the auth boundary) is explicit: `access:` flips from `public` to `authenticated` at the
  success edge, and the warm-start `ENTRY` on `Home` reflects an existing session.
- **Lifecycle** is real on the destination: `Home` refetches on foreground; its state machine covers
  loading/empty/error/ready, not just success.
- **Chrome is shared**, not duplicated: the tab bar is one fragment imported where the app shell begins.
