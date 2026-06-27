# SSDL: Single-Screen Specification Definition Language

**Version:** 1.5.0
**Changelog:** [CHANGELOG.md](CHANGELOG.md)
**Artifact type:** Markdown specification
**Purpose:** Define a compact, expressive, text-first format for specifying a single mobile app screen, including UI/UX,
layout hints, component nesting, business logic, state behavior, lifecycle, permissions, animations, navigation,
data/API contracts, analytics, accessibility, errors, and acceptance criteria.

---

## Contents

**I · Introduction**

- [0. Executive summary](#0-executive-summary)
- [1. Design goals](#1-design-goals)
- [2. Core concepts](#2-core-concepts)

**II · Notation & file anatomy**

- [3. SSDL shorthand symbols](#3-ssdl-shorthand-symbols)
- [4. File-level structure](#4-file-level-structure)
- [5. Top-level grammar](#5-top-level-grammar)
- [6. Screen declaration](#6-screen-declaration)

**III · Screen sections**

*Identity, scope & setup*

- [7. META section](#7-meta-section)
- [8. PURPOSE and SCOPE sections](#8-purpose-and-scope-sections)
- [9. ROUTE section](#9-route-section)
- [10. ACTORS section](#10-actors-section)
- [11. ENTRY and EXIT sections](#11-entry-and-exit-sections)
- [12. PERMISSIONS section](#12-permissions-section)
- [13. FEATURE_FLAGS section](#13-feature_flags-section)

*Data & content*

- [14. MODEL section](#14-model-section)
- [15. DATA section](#15-data-section)
- [16. COPY section](#16-copy-section)

*UI & layout*

- [17. UI section overview](#17-ui-section-overview)
- [18. Component taxonomy](#18-component-taxonomy)
- [19. Component-specific directives and examples](#19-component-specific-directives-and-examples)
- [20. UI directive grammar](#20-ui-directive-grammar)
- [21. Nesting and component relationships](#21-nesting-and-component-relationships)
- [22. Positioning directives](#22-positioning-directives)
- [23. Alignment directives](#23-alignment-directives)
- [24. Sizing directives](#24-sizing-directives)
- [25. Spacing directives](#25-spacing-directives)
- [26. Layering and z-order directives](#26-layering-and-z-order-directives)
- [27. Behavior directives](#27-behavior-directives)
- [28. Visibility, enabled, and loading directives](#28-visibility-enabled-and-loading-directives)
- [29. Binding directives](#29-binding-directives)
- [30. Event directives](#30-event-directives)

*State & lifecycle*

- [31. State section](#31-state-section)
- [32. LIFECYCLE section](#32-lifecycle-section)

*Motion*

- [33. ANIMATION section](#33-animation-section)

*Logic*

- [34. Validation section](#34-validation-section)
- [35. Business rules section](#35-business-rules-section)
- [36. ACTIONS section with pseudocode](#36-actions-section-with-pseudocode)
- [37. FLOW section](#37-flow-section)

*Backend & navigation*

- [38. API section](#38-api-section)
- [39. NAVIGATION section](#39-navigation-section)

*Instrumentation & accessibility*

- [40. ANALYTICS section](#40-analytics-section)
- [41. A11Y section](#41-a11y-section)
- [42. ERRORS section](#42-errors-section)

*QA & open items*

- [43. ACCEPTANCE section](#43-acceptance-section)
- [44. OPEN_QUESTIONS section](#44-open_questions-section)

**IV · Reuse & composition**

- [45. Import and Include](#45-import-and-include)
- [46. Fragment file format](#46-fragment-file-format)
- [47. Screen variants and inheritance](#47-screen-variants-and-inheritance)

**V · Patterns & reference**

- [48. Compact mode](#48-compact-mode)
- [49. Default mobile screen layout pattern](#49-default-mobile-screen-layout-pattern)
- [50. Full example: Login screen](#50-full-example-login-screen)
- [51. UI directive vocabulary reference](#51-ui-directive-vocabulary-reference)
- [52. Ambiguity and conflict-resolution rules](#52-ambiguity-and-conflict-resolution-rules)
- [53. Completeness checklist](#53-completeness-checklist)
- [54. Linting rules for automated review](#54-linting-rules-for-automated-review)

**VI · Adoption**

- [55. Recommended adoption workflow](#55-recommended-adoption-workflow)
- [56. Minimal production template](#56-minimal-production-template)
- [57. Spec-to-implementation traceability](#57-spec-to-implementation-traceability)
- [58. Closing recommendation](#58-closing-recommendation)

---

## 0. Executive summary

SSDL, short for **Single-Screen Specification Definition Language**, is a lightweight text format for describing mobile
app screen requirements. It is designed to be readable by product, design, engineering, QA, analytics, and
AI/code-generation workflows.

SSDL is not meant to replace design files or implementation code. It describes **screen intent**: what the screen
contains, how it behaves, what data it depends on, what business rules apply, and how users move through it.

The format supports two modes:

1. **Full mode** for engineering handoff and QA.
2. **Compact mode** for fast product/design iteration.

The format intentionally uses layout **hints**, not absolute pixel-perfect implementation rules. For example, it uses
`center`, `top.right`, `below(#title, md)`, `w:fill`, `h:hug`, `smaller(#title)`, and `sticky(bottom.safe)` rather than
exact coordinates.

---

## 1. Design goals

SSDL should be:

| Goal                        | Description                                                                                                                         |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Human-readable              | A PM, designer, engineer, or QA tester should understand the screen without needing a parser.                                       |
| Precise enough for delivery | The spec should reduce ambiguity around UI elements, states, business rules, and edge cases.                                        |
| Implementation-agnostic     | The same spec should work for iOS, Android, React Native, Flutter, SwiftUI, Jetpack Compose, or web-mobile.                         |
| AI-friendly                 | The structure should be consistent enough to support generation, summarization, linting, and conversion into tickets or test cases. |
| Flexible                    | A simple screen should remain short; a complex screen should support detailed logic.                                                |
| Testable                    | Acceptance criteria and state transitions should be explicit enough for QA.                                                         |
| Accessible by default       | Accessibility expectations should be specified, not treated as an afterthought.                                                     |

---

## 2. Core concepts

An SSDL file describes one screen.

A **screen** includes:

- identity and metadata,
- feature flags and permissions,
- route/navigation information,
- screen data model,
- UI component tree,
- visual layout directives,
- typography and style directives,
- animation and transition directives,
- states and state transitions,
- lifecycle event handling,
- validation rules,
- business rules,
- event flows,
- pseudocode actions,
- API/data contracts,
- analytics events,
- accessibility expectations,
- error handling,
- acceptance criteria.

Recommended file naming:

```txt
screen.<feature>.<screen-name>.ssdl
```

Examples:

```txt
screen.auth.login.ssdl
screen.checkout.payment-method.ssdl
screen.profile.edit-profile.ssdl
screen.onboarding.choose-plan.ssdl
```

---

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

## 4. File-level structure

A complete SSDL file should use this order unless a team standard says otherwise.

```ssdl
SCREEN <ScreenName> v<version>

// Import declarations — placed immediately after SCREEN, before any sections
import { #app_nav, #app_tab_bar } from "@shared/navigation.ssdl" at v2
import { copy.common, copy.errors } from "@shared/copy.ssdl" at v1
import { ERR-NETWORK, ERR-TIMEOUT } from "@shared/errors.ssdl" at v1
import { handleNetworkError } from "@shared/actions.ssdl" at v1

META { ... }
PURPOSE { ... }
SCOPE { ... }
ROUTE { ... }
ACTORS { ... }
ENTRY { ... }
EXIT { ... }
PERMISSIONS { ... }
FEATURE_FLAGS { ... }
MODEL { ... }
DATA { ... }
COPY { ... }
UI { ... }
STATES { ... }
STATE_TRANSITIONS { ... }
LIFECYCLE { ... }
ANIMATION { ... }
VALIDATION { ... }
VALIDATION_UI { ... }
BUSINESS_RULES { ... }
ACTIONS { ... }
FLOW { ... }
API { ... }
NAVIGATION { ... }
ANALYTICS { ... }
A11Y { ... }
ERRORS { ... }
ACCEPTANCE { ... }
OPEN_QUESTIONS { ... }
```

Only `SCREEN`, `ROUTE`, `MODEL`, `UI`, `STATES`, `FLOW`, and `ACCEPTANCE` are mandatory for every production screen.
Other sections may be omitted for very simple screens, but the recommended production default is to include all
sections, even if some are short.

**Section placement rationale:**

- `import` declarations immediately after `SCREEN` — shared dependencies are visible before any sections reference them.
- `PURPOSE` and `SCOPE` immediately after `META` — orient the reader on what the screen is and isn't before any config.
- `PERMISSIONS` and `FEATURE_FLAGS` after `ENTRY`/`EXIT` — describe the screen first, then its OS-access and feature gating.
- `LIFECYCLE` after `STATES` — lifecycle events drive state transitions.
- `ANIMATION` after `LIFECYCLE` — motion is tied to state/lifecycle changes.

---

## 5. Top-level grammar

This is a practical grammar, not a formal compiler grammar. It defines how the notation should be written and
interpreted.

```ssdl
// --- Screen document ---

Document        := ScreenDecl ImportDecl* Section+
ScreenDecl      := "SCREEN" ScreenName ["extends" ScreenName "v" Version] "v" Version
ImportDecl      := "import" ImportItems "from" Path ["at" "v" Version]
ImportItems     := "{" ImportItem ("," ImportItem)* "}"
                 | CopyNamespace                       // e.g. copy.common
ImportItem      := (ComponentId | Identifier | CopyKey) ["as" Identifier]
Path            := QuotedString                        // relative path or @alias path
CopyNamespace   := "copy" "." Identifier+             // e.g. copy.common, copy.errors
IncludeDirective := "include" Path                     // valid at the top of any section block, before section-specific entries; inlines content from the named fragment file into the enclosing section
Section         := META | PURPOSE | SCOPE | ROUTE | ACTORS | ENTRY | EXIT
                 | PERMISSIONS | FEATURE_FLAGS | MODEL | DATA | COPY | UI
                 | STATES | STATE_TRANSITIONS | LIFECYCLE | ANIMATION | VALIDATION
                 | VALIDATION_UI | BUSINESS_RULES | ACTIONS | FLOW | API
                 | NAVIGATION | ANALYTICS | A11Y | ERRORS | ACCEPTANCE
                 | OPEN_QUESTIONS | OVERRIDE

// --- Fragment document ---

FragmentDocument  := FragmentDecl ExportDecl* ImportDecl* FragmentSection+
FragmentDecl      := "FRAGMENT" FragmentName "v" Version
FragmentSection   := FRAGMENT_META | UI | COPY | API | ERRORS | ACTIONS
                   | VALIDATION | MODEL | A11Y | ANALYTICS
ExportDecl        := "export" (ComponentId | Identifier | CopyNamespace)

// --- Shared terminals ---

Identifier      := letter (letter | digit | "_" | "-")*
ComponentId     := "#" Identifier
FieldId         := "$" Identifier
StateId         := "@" Identifier
CopyKey         := "copy" "." (Identifier ".")* Identifier
RuleId          := ("BR" | "VAL" | "ERR" | "AC") "-" digit+
Condition       := expression returning Boolean
Effect          := assignment | uiEffect | navigation | actionCall | asyncCall | eventEmit
AsyncCall       := [FieldId "="] "~>" (ApiMethod | HttpCall)   // async external/network call; binds result when FieldId present (§36.1, §37)
String          := quoted text
Block           := "{" lines "}"
Comment         := "//" rest-of-line      // inline or full-line; "#" is reserved for ComponentId and must not be used as a comment delimiter
```

---

## 6. Screen declaration

Use a short screen name and a version number.

```ssdl
SCREEN Login v1
```

For screen variants, prefer the `extends` mechanism over duplicated screens. Use a separate name only when screens
diverge significantly.

```ssdl
SCREEN CheckoutPayment v2
SCREEN CheckoutPaymentGuest v1 extends CheckoutPayment v2
```

See §47 for the full variant and inheritance specification.

---

## 7. META section

Use `META` for ownership, delivery status, and lifecycle management.

```ssdl
META {
  feature: Authentication
  owner: Growth/Auth Team
  author: Product Manager
  platform: all
  priority: P0
  status: ready
  last_updated: 2026-05-31
  changelog: {
    v1.0.0: "Add rate-limit error and session-expiry back-behavior"
    v0.9.0: "Initial draft"
  }
}
```

Recommended values:

| Field          | Meaning                     | Example values                                                  |
|----------------|-----------------------------|-----------------------------------------------------------------|
| `feature`      | Product area                | `Authentication`, `Checkout`, `Profile`                         |
| `owner`        | Responsible team/person     | `Growth/Auth Team`                                              |
| `platform`     | Target surface              | `ios`, `android`, `web`, `all`                                  |
| `priority`     | Delivery importance         | `P0`, `P1`, `P2`                                                |
| `status`       | Spec lifecycle              | `draft`, `review`, `ready`, `in_build`, `shipped`, `deprecated` |
| `last_updated` | Last meaningful spec update | `YYYY-MM-DD`                                                    |
| `changelog`    | Per-version change summary  | `{ v1.0.0: "..." }`                                             |

---

## 8. PURPOSE and SCOPE sections

Use `PURPOSE` to explain why the screen exists. Use `SCOPE` to prevent accidental feature creep.

```ssdl
PURPOSE {
  Allow registered users to authenticate with email and password.
}

SCOPE {
  in:
    - Email/password login
    - Forgot password entry point
    - Signup entry point

  out:
    - Social login
    - Passwordless login
    - Multi-factor authentication
}
```

---

## 9. ROUTE section

Use `ROUTE` to define how the screen is addressed and whether authentication is required.

```ssdl
ROUTE {
  path: /login
  type: screen
  access: public
  params: {
    entry_source?: String
    redirect_to?: String
  }
}
```

Recommended route fields:

| Field              | Meaning                      | Example values                                     |
|--------------------|------------------------------|----------------------------------------------------|
| `path`             | Canonical route path         | `/login`, `/checkout/payment`                      |
| `type`             | Presentation mode            | `screen`, `modal`, `bottom_sheet`, `dialog`, `tab` |
| `access`           | Access requirement           | `public`, `authenticated`, `optional`              |
| `access_roles`     | Role-based gate (optional)   | `admin`, `premium`, `verified`                     |
| `requires_plan`    | Subscription gate (optional) | `premium`, `pro`                                   |
| `params`           | Route params                 | `order_id!: ID`                                    |
| `deep_links`       | External links               | `myapp://login`                                    |
| `restore_behavior` | Behavior after app restore   | `restore`, `reload`, `redirect`                    |

Example with required params:

```ssdl
ROUTE {
  path: /orders/:order_id
  type: screen
  access: authenticated
  params: {
    order_id!: ID
    open_receipt?: Boolean := false
  }
}
```

---

## 10. ACTORS section

Use `ACTORS` to define who or what interacts with the screen.

```ssdl
ACTORS {
  primary: RegisteredUser
  systems: [AnalyticsService, SecureStorage]
}
```

| Field     | Meaning                                                                    |
|-----------|----------------------------------------------------------------------------|
| `primary` | The main human role who drives this screen's interactions                  |
| `systems` | Non-human actors the screen communicates with (APIs, storage, OS services) |

**`systems`** entries should each correspond to an entry in the `API` or `DATA` section. If a system actor has no `API`
entry, add a `//` comment explaining why (e.g., global singleton, OS service).

---

## 11. ENTRY and EXIT sections

Use these sections to describe how users arrive and leave.

```ssdl
ENTRY {
  - from: AppLaunch
    when: user.authenticated == false

  - from: SessionExpired
    when: token.expired == true
}

EXIT {
  - to: Home
    when: login.success && $redirect_to.empty

  - to: ForgotPassword
    when: tap #forgot_link
}
```

Prefer `ENTRY`/`EXIT` for high-level journey mapping and `NAVIGATION` for implementation-level route transitions.

---

## 12. PERMISSIONS section

Use `PERMISSIONS` to declare OS-level permissions the screen requires, when to request them, and how to handle each
outcome.

```ssdl
PERMISSIONS {
  camera {
    required_for: [#take_photo_btn, #scan_qr_btn]
    request_when: first_tap(#take_photo_btn)
    if not_determined:
      show #camera_rationale_sheet
    if authorized:
      enable [#take_photo_btn, #scan_qr_btn]
    if denied:
      show #camera_denied_banner
      disable [#take_photo_btn, #scan_qr_btn]
    if restricted:
      show #camera_restricted_banner
      disable [#take_photo_btn, #scan_qr_btn]
  }

  notifications {
    required_for: [#enable_alerts_btn]
    request_when: tap #enable_alerts_btn
    if denied:
      show #notifications_denied_sheet
  }
}
```

### 12.1 Supported permission types

```txt
camera
microphone
location.always
location.when_in_use
location.precise          // iOS 14+ / Android 12+: full GPS accuracy
location.approximate      // iOS 14+ / Android 12+: coarse location only
notifications
contacts
photos
biometrics
bluetooth
calendar
health                    // HealthKit (iOS) / Health Connect (Android)
tracking                  // IDFA / ATT on iOS
```

This list is not exhaustive. Teams may add project-specific permission types (e.g., `nfc`, `speech_recognition`)
following the same pattern. Each added type should document its platform scope in a `//` comment.

### 12.2 Permission states

| State            | Meaning                                             |
|------------------|-----------------------------------------------------|
| `not_determined` | User has not been asked yet                         |
| `authorized`     | User granted the permission                         |
| `denied`         | User explicitly denied                              |
| `restricted`     | Device-level restriction (parental controls, MDM)   |
| `provisional`    | Notifications only: granted quietly, without alerts |

### 12.3 Request timing options

```txt
on_view              // Request immediately on screen.view
first_tap(#id)       // Request when user first taps the gated component
explicit_action      // Request only when user taps a dedicated "Enable X" button
deferred             // Do not request; let user trigger from settings
```

---

## 13. FEATURE_FLAGS section

Use `FEATURE_FLAGS` to declare which feature flags affect this screen, what they gate, and what the fallback is.

```ssdl
FEATURE_FLAGS {
  new_payment_flow {
    when enabled:
      show #new_payment_section
      hide #legacy_payment_section
    when disabled:
      show #legacy_payment_section
      hide #new_payment_section
    default: disabled
  }

  enhanced_error_messages {
    when enabled:
      $error_display_mode := detailed
    default: enabled
    fallback: disabled    // value used when the flag service is unreachable
  }
}
```

### 13.1 Feature flag fields

| Field            | Meaning                                                                  | Required    |
|------------------|--------------------------------------------------------------------------|-------------|
| `when enabled:`  | Effects when the flag evaluates to enabled                               | Yes         |
| `when disabled:` | Effects when the flag evaluates to disabled                              | Recommended |
| `default:`       | Flag value in production before a controlled rollout begins              | Yes         |
| `fallback:`      | Flag value used when the flag service is unreachable or evaluation fails | Recommended |

`default:` and `fallback:` are independent. Example: a new feature may have `default: disabled` (off before rollout) and
`fallback: disabled` (safe off if flag service fails). A critical fix may have `default: enabled` but
`fallback: enabled` (fail open). Always specify `fallback:` for flags that gate user-visible features.

### 13.2 Feature flag rules

- Every component whose `visible_when` or `hidden_when` condition references a feature flag must have a corresponding
  `FEATURE_FLAGS` entry.
- The `default:` field must be `enabled` or `disabled`. It documents the flag's state in production before a controlled
  rollout.
- Feature flag conditions in `visible_when` should delegate to a named flag rather than embedding the flag check inline:

Preferred:

```ssdl
#new_payment_section: Card {
  visible_when: flag.new_payment_flow.enabled
}
```

Avoid (flag logic scattered, not auditable):

```ssdl
#new_payment_section: Card {
  visible_when: $user.bucket == "experiment_b"
}
```

---

## 14. MODEL section

Use `MODEL` to define screen-local data, defaults, required fields, optional fields, and derived values.

```ssdl
MODEL {
  $email!: Email := ""
  $password!: String := ""
  $remember_me: Boolean := false
  $error_msg?: String
  $is_loading ==> @loading                          // derived from state; see §14.1

  $email_valid ==> matchesEmail(trim($email))
  $password_valid ==> length($password) >= 8
  $form_valid ==> $email_valid && $password_valid
  $can_submit ==> $form_valid && !$is_loading
}
```

### 14.1 Field notation

```ssdl
$field_name!: Type := default
$field_name?: Type
$derived_field ==> expression
```

| Notation      | Meaning                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `$email!`     | Required field — in `MODEL`: must be non-empty/non-null before form submission; in `ROUTE.params`: caller must supply this value at navigation time |
| `$error_msg?` | Optional field — may be null or absent; never blocks submission                                                                                     |
| `:=`          | Default value or assignment                                                                                                                         |
| `==>`         | Computed/derived value — re-evaluated whenever any referenced field changes                                                                         |

**Derived field rules:**

- A derived field (`==>`) may reference other derived fields, but circular dependencies are forbidden. `$a ==> f($b)`
  and `$b ==> g($a)` is a spec error.
- Evaluation order follows a topological sort of the dependency graph. Declare fields in any order; implementations must
  resolve the correct evaluation sequence.
- A derived field must not use `:=` assignment — it is read-only. Use a regular field with `:=` if you need a writable
  computed default.
- To expose a screen state as a Boolean in the model, derive it from the state: `$is_loading ==> @loading`. Do not
  maintain a parallel Boolean field that mirrors state — they will drift.

### 14.2 Recommended types

```txt
String
Text
Email
Password
Number
Integer
Decimal
Money
Boolean
Date
DateTime
Enum(...)
Object(...)
Array(...)
URL
ImageURL
ID
Token
Phone
JSON
```

Examples:

```ssdl
MODEL {
  $plan_id!: ID
  $billing_cycle: Enum(monthly, annual) := monthly
  $subtotal: Money := 0
  $discount?: Money
  $total ==> $subtotal - coalesce($discount, 0)
}
```

---

## 15. DATA section

Use `DATA` to declare where information comes from and where it is written.

```ssdl
DATA {
  source: mixed

  read:
    - route_param: redirect_to?
    - local: saved_email?
    - remote: GET /users/me
        cache: stale_while_revalidate ttl:300

  write:
    - secure_storage: auth_token
    - secure_storage: refresh_token
    - analytics: login events
}
```

Recommended source values:

```txt
local
remote
mixed
none
```

### 15.1 Cache strategies for remote reads

| Strategy                 | Meaning                                                                                                                                 |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `none`                   | Always fetch fresh; never read from cache                                                                                               |
| `network_only`           | Fetch from network; error if offline                                                                                                    |
| `cache_first`            | Return cached value immediately; refresh in background but do NOT update UI when fresh data arrives (fire-and-forget; avoids re-render) |
| `stale_while_revalidate` | Return cached value; simultaneously fetch fresh; update UI when fresh data arrives (causes re-render)                                   |
| `cache_only`             | Read from cache only; useful for offline-first screens                                                                                  |
| `ttl:<seconds>`          | Cache validity duration; combine with a strategy                                                                                        |

Use `DATA` to avoid ambiguity about whether a value comes from route params, local storage, backend response, cached
state, or user input.

---

## 16. COPY section

Use `COPY` for user-facing text and localization keys.

```ssdl
COPY {
  login.title: "Welcome back"
  login.subtitle: "Log in to continue"
  login.email_label: "Email"
  login.password_label: "Password"
  login.submit: "Log In"
  login.error.invalid_credentials: "Email or password is incorrect."
}
```

Recommended rule: all user-facing strings in `UI`, `ERRORS`, `VALIDATION`, and `A11Y` should either reference `COPY`
keys or intentionally inline short one-off text.

### 16.1 Parameterized copy

Use ICU message format for strings that require interpolation.

```ssdl
COPY {
  profile.greeting: "Hello, {name}"
  cart.items: "{count, plural, one {# item} other {# items}}"
  order.status: "Order {order_id} placed on {date}"
}
```

Reference parameterized copy in UI by passing values:

```ssdl
#greeting: Txt {
  text: copy.profile.greeting { name: $user.first_name }
}

#cart_count: Txt {
  text: copy.cart.items { count: $cart.item_count }
}
```

### 16.2 Copy key conventions

```txt
<screen>.<element>             login.title
<screen>.<element>.<variant>   login.error.invalid_credentials
common.<element>               common.error.network
common.<element>.<variant>     common.action.retry
```

Maximum recommended nesting depth: 3 levels. Keys beyond 3 levels indicate the string likely belongs to a sub-component
spec.

Preferred:

```ssdl
#title: Txt {
  text: copy.login.title
}
```

Allowed for quick drafts:

```ssdl
#title: Txt "Welcome back"
```

---

## 17. UI section overview

The `UI` section defines the component tree, component labels, bindings, layout hints, visibility, enabled states,
events, and accessibility hooks.

A component declaration uses this structure:

```ssdl
#component_id: ComponentType "optional visible copy" {
  in: #parent_component
  pos: <position_directive>
  align: <alignment_directive>
  size: <size_directive>
  gap: <spacing_token>
  pad: <spacing_token>
  margin: <spacing_token>
  layer: <layer_directive>
  style: <style_token>
  behavior: <behavior_directive>

  // Content and input directives
  label: <copy_key_or_string>      // User-visible field label (inputs)
  placeholder: <copy_key_or_string> // Placeholder text shown when field is empty
  helper_text: <copy_key_or_string> // Hint text below the field
  error: <expression>               // Inline error — typically errorFor($field) or a string
  value: <field_or_expression>      // Current value for display-only or non-text components
  min: <number>                     // Minimum value (Slider, Stepper, numeric Input)
  max: <number>                     // Maximum value
  step: <number>                    // Increment size (Slider, Stepper)
  autocomplete: <autocomplete_type> // Browser/OS autocomplete hint (email, password, name, etc.)
  autocapitalize: <none|words|sentences|characters>

  // Binding and interaction
  bind: $field
  keyboard: <keyboard_type>
  validation: none
  checked_when: <condition>        // For Chk, Radio, Switch — checked/selected state
  selected_when: <condition>       // For Select, Tabs — selected state
  disabled_when: <condition>       // Inverse of enabled_when; use one or the other

  // Visibility and state
  visible_when: <condition>
  hidden_when: <condition>
  enabled_when: <condition>
  loading_when: <condition_or_state>
  readonly_when: <condition>

  // Animation
  animate: <animation_directive>
  transition: <transition_directive>

  // Structure and QA
  children: [#child_1, #child_2]
  test_id: <string>                // Stable automation selector; kebab-case recommended

  // Events
  on tap: <action_or_nav>
  on long_press: <action>
  on swipe_left: <action>
  on swipe_right: <action>
  on appear: <action>
  on disappear: <action>

  // Accessibility
  a11y: <accessibility_directive>
}
```

**`errorFor($field)`** is a notional utility that returns the first active validation error message for the given model
field, or an empty value when the field is valid or has not been validated yet. It resolves by matching the `$field`
argument against the `fields:` lists declared in the `VALIDATION` section (§34), falling back to the field's `bind:`
target when no `fields:` list is present. Implementations may use an equivalent lookup (e.g., a `Map<FieldId, String>`
populated by the validation runner) rather than a literal `errorFor()` function.

Concise example:

```ssdl
#login_btn: Btn "Log In" {
  in: #form
  pos: below(#password_input, md)
  align: stretch
  size: w:fill h:lg
  style: label_lg
  enabled_when: $can_submit
  loading_when: @loading
  on tap: submitLogin()
}
```

---

## 18. Component taxonomy

### 18.1 Content components

| Type              | Meaning                                                                                |
|-------------------|----------------------------------------------------------------------------------------|
| `Txt`             | Static text                                                                            |
| `RichTxt`         | Rich/formatted text                                                                    |
| `Img`             | Image                                                                                  |
| `Thumbnail`       | Small image with lazy loading and placeholder fallback                                 |
| `Icon`            | Icon                                                                                   |
| `Avatar`          | User/profile image                                                                     |
| `Badge`           | Small text label/status marker                                                         |
| `NumberBadge`     | Count bubble — notification dot with a numeric value (99+)                             |
| `Tag`             | Inline removable label; pill/chip shape — filter tags, category labels, selected items |
| `StatusIndicator` | Colored presence dot — online, offline, busy, away                                     |
| `Rating`          | Read-only star/heart/thumb score display                                               |
| `Stat`            | Single KPI block — large number + label + optional trend                               |
| `PriceTag`        | Formatted price with optional strikethrough original price                             |
| `QRCode`          | Display-only QR code generated from a value                                            |
| `Lottie`          | JSON-driven animation — success bursts, empty state illustrations, loading delight     |
| `MapView`         | Embedded interactive or static map                                                     |
| `Divider`         | Visual divider                                                                         |
| `Spacer`          | Flexible empty space                                                                   |

### 18.2 Input components

| Type               | Meaning                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Input`            | Text input                                                                                                                                                                                                               |
| `Pwd`              | Password input                                                                                                                                                                                                           |
| `TextArea`         | Multiline input                                                                                                                                                                                                          |
| `Search`           | Search input field (no cancel/filter chrome — use `SearchBar` for the full UI)                                                                                                                                           |
| `OTPInput`         | Fixed-length segmented code entry — SMS verify, 2FA, PIN                                                                                                                                                                 |
| `PhoneInput`       | Phone number field with integrated country code picker                                                                                                                                                                   |
| `TagInput`         | Multi-value freeform entry with removable chips — email recipients, tags                                                                                                                                                 |
| `QuantityInput`    | Inline +/- styled quantity selector — e-commerce, cart; distinct from `Stepper` which is generic                                                                                                                         |
| `LocationInput`    | Address/place autocomplete field — Google Places style                                                                                                                                                                   |
| `RichTextEditor`   | Formatted text authoring with toolbar — bold, italic, lists, links                                                                                                                                                       |
| `Chk`              | Checkbox                                                                                                                                                                                                                 |
| `Radio`            | Radio button                                                                                                                                                                                                             |
| `Switch`           | Toggle                                                                                                                                                                                                                   |
| `SegmentedControl` | Mutually exclusive inline option switcher — sets a value, not triggers an action. Platform: `UISegmentedControl` (iOS) / `ChipGroup` or `TabLayout` (Android) / `@react-native-segmented-control/segmented-control` (RN) |
| `ToggleGroup`      | Group of toggle buttons where one or more can be active — filter bars, multi-select chip sets                                                                                                                            |
| `Select`           | Picker/dropdown                                                                                                                                                                                                          |
| `Slider`           | Range/value slider                                                                                                                                                                                                       |
| `Stepper`          | Increment/decrement control                                                                                                                                                                                              |
| `DatePicker`       | Date-only selector                                                                                                                                                                                                       |
| `TimePicker`       | Time-only selector                                                                                                                                                                                                       |
| `DateTimePicker`   | Combined date and time selector                                                                                                                                                                                          |
| `ColorPicker`      | Color selection — hex, RGB, HSL, or palette                                                                                                                                                                              |
| `Scanner`          | Camera QR/barcode capture trigger                                                                                                                                                                                        |
| `FilePicker`       | File/image selector from device library                                                                                                                                                                                  |

### 18.3 Action components

| Type              | Meaning                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| `Btn`             | Button                                                                                                    |
| `IconBtn`         | Icon button                                                                                               |
| `Link`            | Tappable text/link                                                                                        |
| `MenuBtn`         | Button opening a menu                                                                                     |
| `FAB`             | Floating action button — single primary action                                                            |
| `SpeedDial`       | FAB that expands into a set of sub-action buttons — Material Design pattern; children are `SpeedDialItem` |
| `SpeedDialItem`   | Individual action in a `SpeedDial` — icon + text + tap handler                                            |
| `ContextMenu`     | Long-press or right-click contextual action list anchored to a component; children are `ContextMenuItem`  |
| `ContextMenuItem` | Individual item in a `ContextMenu` — text + optional icon + optional destructive flag                     |

### 18.4 Feedback components

| Type             | Meaning                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Banner`         | Inline/global message; `type:` sets severity — see §19.45                                                                                                                                                                                |
| `NetworkBanner`  | Offline/reconnecting persistent notice — always visible while condition holds                                                                                                                        |
| `Toast`          | Temporary auto-dismissing message                                                                                                                                                                    |
| `Snackbar`       | Temporary bottom message with optional action                                                                                                                                                        |
| `Spinner`        | Indeterminate loading indicator                                                                                                                                                                      |
| `InlineLoader`   | Small spinner scoped to a list item, card, or button area                                                                                                                                            |
| `Skeleton`       | Loading placeholder for a content region                                                                                                                                                             |
| `Progress`       | Progress indicator — use `style: linear` for a track bar or `style: circular` for a ring; use `indeterminate: true` when progress is unknown                                                         |
| `StepIndicator`  | Step/page progress — dots, numbers, or bars indicating position in a funnel or onboarding flow                                                                                                       |
| `EmptyState`     | Structured state region — illustration + title + description + CTA. Use `type:` to express intent: `empty` (no data), `error` (load failed), `offline`, `no_results`, `permission_denied`, `custom`. |
| `LoadingOverlay` | Full-screen blocking spinner with optional message and cancel                                                                                                                                        |
| `Modal`          | Arbitrary-content modal container (see §19.44)                                                                                                                                                                         |
| `Dialog`         | Focused dialog — title + message + confirm button + optional cancel; use `destructive: true` for destructive confirm actions. Replaces `ConfirmDialog` and `DialogBox`.                              |
| `ActionSheet`    | Option list presented as an overlay — iOS action sheet / Android bottom option menu                                                                                                                  |
| `Sheet`          | Bottom sheet content container                                                                                                                                                                       |
| `Popover`        | Anchored floating panel — can contain interactive content; distinct from `Tooltip` which is read-only                                                                                                |
| `Tooltip`        | Read-only helper text anchored to a component                                                                                                                                                        |

### 18.5 Layout components

| Type            | Meaning                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| `Container`     | Generic parent                                                                                                               |
| `SafeArea`      | Safe-area-aware wrapper                                                                                                      |
| `Scroll`        | Scrollable container                                                                                                         |
| `PullToRefresh` | Refresh trigger wrapper around a `Scroll` — declares pull gesture and refresh handler                                        |
| `VStack`        | Vertical stack                                                                                                               |
| `HStack`        | Horizontal stack; use `wrap: true` for wrapping chip/tag rows                                                                |
| `ZStack`        | Layered stack                                                                                                                |
| `Grid`          | Regular-column grid layout; use `masonry: true` for irregular (Pinterest-style) item heights                                 |
| `Card`          | Grouped content container                                                                                                    |
| `Section`       | Semantic content group                                                                                                       |
| `FormGroup`     | Logical grouping of related form fields with a shared section label, helper text, and error state                            |
| `Header`        | Top region                                                                                                                   |
| `NavBar`        | Top navigation bar — title, leading back/menu action, trailing actions                                                       |
| `StickyHeader`  | Collapsing/parallax header that pins at the top on scroll; transitions to a compact `NavBar`                                 |
| `Footer`        | Bottom region                                                                                                                |
| `TabBar`        | Bottom tab navigation container — holds `TabItem` components                                                                 |
| `TabItem`       | Individual tab within `TabBar` or `Tabs` — label, icon, badge count, selected state                                          |
| `Drawer`        | Side navigation panel — slides in from left or right edge                                                                    |
| `DrawerItem`    | Individual item within a `Drawer`                                                                                            |
| `Overlay`       | Overlay layer                                                                                                                |
| `List`          | Flat list container                                                                                                          |
| `ListItem`      | List row/item                                                                                                                |
| `SectionList`   | Grouped list with sticky section headers — contacts A–Z, grouped settings                                                    |
| `Table`         | Columnar data grid — sortable, frozen columns, optional row selection                                                        |
| `Tabs`          | Inline tab set within a screen (content switching, not navigation)                                                           |
| `Accordion`     | Expandable/collapsible section with a tappable header                                                                        |
| `Collapsible`   | Generic show/hide wrapper — no built-in header affordance; use when you supply your own trigger                              |
| `Carousel`      | Pageable item strip — use `fill: true` for full-bleed pages; default shows partial peek of adjacent items                    |
| `SearchBar`     | Full search UI with input, cancel button, and optional filter affordance; wraps `Search` input                               |

---

## 19. Component-specific directives and examples

This section documents directives, A11Y defaults, and SSDL examples for every non-trivial component.
Standard directives (`pos`, `size`, `bind`, `visible_when`, `on tap`, `a11y`, etc.) always apply. Only
component-specific additions are listed per entry.

**Example style rule:** Never include a directive in an example if it is set to its default value. Examples should show
only the directives that change behavior from the default. This keeps examples short and prevents authors from
copy-pasting noise into production specs.

---

### 19.1 Lottie

| Directive      | Meaning                                            |
|----------------|----------------------------------------------------|
| `source:`      | Path or asset key to the `.json` Lottie file       |
| `autoplay:`    | Boolean — start playing when visible               |
| `loop:`        | Boolean — repeat indefinitely                      |
| `speed:`       | Playback multiplier — default `1.0`                |
| `progress:`    | Bind to a `$field` (0.0–1.0) to scrub manually     |
| `on complete:` | Action fired when a non-looping animation finishes |

**A11Y default role:** `none` (decorative). Override with `image` if the animation is the primary content.
**Reduced motion:** always provide a `reduced_motion` alternative in `ANIMATION` — substitute a static `Img` or `none`.

```ssdl
#success_burst: Lottie {
  in: #screen
  pos: parent.center
  size: w:xl h:xl
  source: "animations/login_success.json"
  autoplay: true
  loop: false
  visible_when: @success
  on complete: nav Home
}
```

---

### 19.2 MapView

| Directive           | Meaning                                                                       |
|---------------------|-------------------------------------------------------------------------------|
| `center:`           | Initial map center — `{ lat, lng }` or `$field`                               |
| `zoom:`             | Initial zoom — `street`, `neighborhood`, `city`, `region`, `country` (§51.11) |
| `markers:`          | Bound collection; each item rendered as a map pin                             |
| `interactive:`      | Boolean — allow pan/zoom/tap; `false` for static display                      |
| `on region_change:` | Action fired when user pans or zooms                                          |
| `on marker_tap:`    | Action fired when a marker is tapped                                          |

**A11Y default role:** `image`. Describe the region in `a11y:`.
**Permissions:** displaying user location requires `PERMISSIONS.location.when_in_use` (LINT-041).

```ssdl
#delivery_map: MapView {
  in: #content
  size: w:fill h:xl
  center: $order.delivery_location
  zoom: neighborhood
  markers: $order.route_pins
  interactive: false
  a11y: "Delivery route map"
}
```

---

### 19.3 Rating

| Directive | Meaning                              |
|-----------|--------------------------------------|
| `value:`  | Score — Number or `$field`           |
| `max:`    | Maximum (default `5`)                |
| `style:`  | `star` (default) / `heart` / `thumb` |

**A11Y default role:** `text` — announce as `"{value} out of {max} stars"`.

```ssdl
#product_rating: Rating {
  in: #product_header
  value: $product.avg_rating
  max: 5
  style: star
  size: sm
  a11y: "{$product.avg_rating} out of 5 stars"
}
```

---

### 19.4 Tag

| Directive    | Meaning                                               |
|--------------|-------------------------------------------------------|
| `text:`      | Tag text — copy key or inline string                  |
| `removable:` | Boolean — show remove affordance                      |
| `style:`     | `filled` / `outline` / `ghost` / `tonal` — see §51.18 |
| `on remove:` | Action when user taps the remove affordance           |

**A11Y default role:** `button` when `removable: true`; `text` otherwise.

```ssdl
#category_tag: Tag {
  in: #filter_row
  text: $category.name
  style: tonal
  removable: true
  on remove: removeFilter($category)
  a11y: "{$category.name}, remove filter"
}
```

---

### 19.5 NumberBadge

| Directive | Meaning                                                         |
|-----------|-----------------------------------------------------------------|
| `count:`  | Number or `$field`                                              |
| `max:`    | Display cap — counts above this show as `{max}+` (default `99`) |

**A11Y default role:** `text` — announce the full count, not the capped display.

```ssdl
#notif_badge: NumberBadge {
  pos: overlay(#notif_icon, top.right)
  count: $notifications.unread_count
  max: 99
  visible_when: $notifications.unread_count > 0
  a11y: "{$notifications.unread_count} unread notifications"
}
```

---

### 19.6 StatusIndicator

| Directive | Meaning                                                              |
|-----------|----------------------------------------------------------------------|
| `status:` | `online` / `offline` / `busy` / `away` / `do_not_disturb` / `custom` |
| `label:`  | Optional visible label alongside the dot                             |
| `color:`  | Override dot color when `status: custom`                             |

**A11Y default role:** `text` with label `"{status}"`.

```ssdl
#user_status: StatusIndicator {
  pos: overlay(#avatar, bottom.right)
  status: $user.presence_status
  size: xs
  a11y: "{$user.name} is {$user.presence_status}"
}
```

---

### 19.7 Stat

| Directive      | Meaning                                     |
|----------------|---------------------------------------------|
| `value:`       | Primary number — Number, Money, or `$field` |
| `subtitle:`    | Descriptor below the value                  |
| `trend:`       | `up` / `down` / `neutral` — see §51.24      |
| `trend_value:` | Trend magnitude text — `"+12%"` or `$field` |

**A11Y default role:** `text`.

```ssdl
#revenue_stat: Stat {
  in: #dashboard_row
  value: $metrics.revenue
  subtitle: "Revenue this month"
  trend: up
  trend_value: $metrics.revenue_change_pct
  style: heading_lg
}
```

---

### 19.8 PriceTag

| Directive   | Meaning                                           |
|-------------|---------------------------------------------------|
| `amount:`   | Current price — Money or `$field`                 |
| `currency:` | ISO code or symbol (default: app locale)          |
| `original:` | Strikethrough original price — shown when present |

**A11Y default role:** `text` — announce as `"{amount}, was {original}"` when `original:` is set.

```ssdl
#item_price: PriceTag {
  in: #product_card
  amount: $product.sale_price
  original: $product.list_price
  style: label_lg
  a11y: "{$product.sale_price}, was {$product.list_price}"
}
```

---

### 19.9 Thumbnail

| Directive   | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| `src:`      | Image URL or `$field`                                     |
| `fallback:` | Image shown while loading or on error                     |
| `aspect:`   | `square` / `wide` / `portrait` / `tall` / `auto` (§51.22) |

**A11Y default role:** `image`.

```ssdl
#order_thumb: Thumbnail {
  in: #order_row
  src: $order.image_url
  fallback: "images/placeholder_product.png"
  aspect: square
  size: md
  a11y: "{$order.product_name} product image"
}
```

---

### 19.10 QRCode

| Directive           | Meaning                                  |
|---------------------|------------------------------------------|
| `value:`            | String encoded in the QR                 |
| `size:`             | Standard size tokens                     |
| `error_correction:` | `L` / `M` (default) / `Q` / `H` (§51.23) |

**A11Y default role:** `image` — always provide `a11y:` describing what the code represents.

```ssdl
#payment_qr: QRCode {
  in: #payment_section
  value: $payment.qr_payload
  size: xl
  a11y: "QR code for payment — scan with your banking app"
}
```

---

### 19.11 OTPInput

| Directive                     | Meaning                                      |
|-------------------------------|----------------------------------------------|
| `length:`                     | Cell count — required (LINT-033)             |
| `mask:`                       | Boolean — obscure digits                     |
| `autocomplete: one_time_code` | Required for SMS autofill on iOS and Android |
| `on complete:`                | Action fired when all cells are filled       |

**A11Y default role:** `textfield` with label `"One-time code, {length} digits"`.

```ssdl
#otp_input: OTPInput {
  in: #form
  length: 6
  mask: false
  autocomplete: one_time_code
  keyboard: number
  bind: $otp_code
  on complete: verifyOTP()
  a11y: "Verification code, 6 digits"
}
```

---

### 19.12 PhoneInput

| Directive            | Meaning                                               |
|----------------------|-------------------------------------------------------|
| `default_country:`   | ISO 3166-1 alpha-2 code — pre-selected country        |
| `allowed_countries:` | Restrict picker to listed countries                   |
| `bind:`              | Binds to a `Phone` field; value includes country code |

**A11Y default role:** `textfield`.

```ssdl
#phone_input: PhoneInput {
  in: #form
  label: copy.profile.phone_label
  bind: $phone_number
  default_country: $user.country_code
  keyboard: phone
  autocomplete: phone
  a11y: "Phone number, required"
}
```

---

### 19.13 TagInput

| Directive        | Meaning                                     |
|------------------|---------------------------------------------|
| `max_tags:`      | Maximum number of tags                      |
| `suggestions:`   | Bound collection for autocomplete           |
| `bind:`          | Binds to `Array(String)` or `Array(Object)` |
| `on tag_add:`    | Action when a tag is added                  |
| `on tag_remove:` | Action when a tag is removed                |

**A11Y default role:** `textfield`.

```ssdl
#recipients_input: TagInput {
  in: #compose_form
  label: "To"
  bind: $recipients
  suggestions: $contact_suggestions
  max_tags: 20
  keyboard: email
  on tag_add: validateRecipient($tag)
  on tag_remove: removeRecipient($tag)
}
```

---

### 19.14 QuantityInput

| Directive | Meaning                      |
|-----------|------------------------------|
| `bind:`   | Binds to an `Integer` field  |
| `min:`    | Minimum value (default `0`)  |
| `max:`    | Maximum value                |
| `step:`   | Increment size (default `1`) |

**A11Y default role:** `adjustable` — announce as `"Quantity, {value}"`. When the user adjusts the value, announce the
new value. Minimum and maximum values should be announced when limits are reached: `"Minimum quantity reached"` /
`"Maximum quantity reached"`.

```ssdl
#qty_input: QuantityInput {
  in: #cart_row
  bind: $item.quantity
  min: 1
  max: $item.stock_count
  a11y: "Quantity, {$item.quantity}"
}
```

---

### 19.15 LocationInput

| Directive       | Meaning                                                              |
|-----------------|----------------------------------------------------------------------|
| `bias_country:` | ISO country code — biases results                                    |
| `result_types:` | `address` / `city` / `region` / `establishment` / `all` — see §51.27 |
| `bind:`         | Binds to `Object({ address, lat, lng })`                             |

**A11Y default role:** `textfield`.
**Permissions:** no location permission needed for the search-autocomplete path. If the implementation includes a "use
current location" affordance that accesses the device GPS sensor, declare `PERMISSIONS.location.when_in_use` (LINT-041).

```ssdl
#delivery_address: LocationInput {
  in: #checkout_form
  label: copy.checkout.delivery_address
  bind: $delivery_location
  bias_country: $user.country
  result_types: address
  placeholder: "Enter delivery address"
}
```

---

### 19.16 SegmentedControl

| Directive   | Meaning                                                         |
|-------------|-----------------------------------------------------------------|
| `segments:` | Array of `{ label, value }` or bound collection                 |
| `bind:`     | Binds to a field — value matches the selected segment's `value` |

**A11Y default role:** `tablist` — each segment is a `tab`.
**Platform:** `UISegmentedControl` (iOS) / `ChipGroup` or `TabLayout` (Android) /
`@react-native-segmented-control/segmented-control` (RN).

```ssdl
#billing_cycle: SegmentedControl {
  in: #plan_form
  segments: [{ label: "Monthly", value: monthly }, { label: "Annual", value: annual }]
  bind: $billing_cycle
  size: w:fill
}
```

---

### 19.17 ToggleGroup

| Directive    | Meaning                                            |
|--------------|----------------------------------------------------|
| `options:`   | Array of `{ label, icon?, value }`                 |
| `selection:` | `single` / `multi` — see §51.25                    |
| `bind:`      | Scalar field for `single`; array field for `multi` |

**A11Y default role:** `radiogroup` for `single`; `group` for `multi`. Each toggle option should announce its label and
selected state — `"{label}, selected"` / `"{label}, not selected"`. For `multi` selection, also announce the total
number of selected options when focus moves away: `"{n} filters selected"`.

```ssdl
#dietary_filters: ToggleGroup {
  in: #filter_bar
  options: $dietary_options
  selection: multi
  bind: $active_filters
  size: w:fill
}
```

---

### 19.18 ColorPicker

| Directive  | Meaning                                          |
|------------|--------------------------------------------------|
| `mode:`    | `hex` / `rgb` / `hsl` / `hsb` / `palette`        |
| `palette:` | Array of hex strings — used with `mode: palette` |
| `bind:`    | Binds to a `String` (hex) or `Object` field      |

**A11Y default role:** `adjustable`. Announce the currently selected color value when changed —
`"Color selected: #FF5733"` or `"Red selected"` when using a named palette. For `mode: palette`, announce each swatch as
`"{color name} swatch, {n} of {total}"`.

```ssdl
#theme_color: ColorPicker {
  in: #customization_form
  label: "Accent color"
  mode: palette
  palette: $brand.color_options
  bind: $user.accent_color
}
```

---

### 19.19 Scanner

| Directive       | Meaning                                                                          |
|-----------------|----------------------------------------------------------------------------------|
| `formats:`      | `qr` / `code128` / `ean13` / `pdf417` / `data_matrix` / `aztec` / `all` (§51.12) |
| `overlay_hint:` | Copy shown in the camera overlay                                                 |
| `on scan:`      | Action fired with decoded value — required (LINT-040)                            |

**A11Y default role:** `button`. When the camera is active, announce `"Camera active, scanning for {format}"`. Announce
scan results immediately: `"QR code detected"`. If the camera permission is denied, announce the error state rather than
silently disabling the button.

**Permissions:** requires `PERMISSIONS.camera` (LINT-040).

```ssdl
#qr_scanner: Scanner {
  in: #screen
  size: w:fill h:fill
  formats: [qr]
  overlay_hint: copy.checkin.scan_hint
  on scan: processQRCode($value)
  visible_when: $scanning_active
}
```

---

### 19.20 RichTextEditor

| Directive      | Meaning                                                                              |
|----------------|--------------------------------------------------------------------------------------|
| `toolbar:`     | `bold` / `italic` / `underline` / `bullet_list` / `numbered_list` / `link` / `image` |
| `max_length:`  | Character limit                                                                      |
| `bind:`        | Binds to a `Text` field                                                              |
| `placeholder:` | Text shown when empty                                                                |
| `on change:`   | Action fired on edit — aligns with §30 event vocabulary                              |

**A11Y default role:** `textfield`.

```ssdl
#post_editor: RichTextEditor {
  in: #compose_screen
  size: w:fill h:fill
  toolbar: [bold, italic, bullet_list, link]
  bind: $post_body
  placeholder: copy.compose.body_placeholder
  max_length: 5000
  on change: updateCharCount()
}
```

---

### 19.21 SpeedDial and SpeedDialItem

**SpeedDial:**

| Directive    | Meaning                                    |
|--------------|--------------------------------------------|
| `direction:` | `up` (default) / `down` / `left` / `right` |
| `on open:`   | Action when dial expands                   |
| `on close:`  | Action when dial collapses                 |

**SpeedDialItem:**

| Directive | Meaning                              |
|-----------|--------------------------------------|
| `icon:`   | Icon name                            |
| `text:`   | Action label shown when dial is open |
| `on tap:` | Action fired when item is tapped     |

**A11Y:** `SpeedDial` role `menu`; `SpeedDialItem` role `menuitem`.

```ssdl
#compose_dial: SpeedDial {
  pos: floating(bottom.right)
  children: [#action_photo, #action_file, #action_link]
}

#action_photo: SpeedDialItem {
  in: #compose_dial
  icon: "camera"
  text: "Add photo"
  on tap: openCamera()
}

#action_file: SpeedDialItem {
  in: #compose_dial
  icon: "file"
  text: "Attach file"
  on tap: openFilePicker()
}

#action_link: SpeedDialItem {
  in: #compose_dial
  icon: "link"
  text: "Insert link"
  on tap: openLinkInput()
}
```

---

### 19.22 ContextMenu and ContextMenuItem

**ContextMenu:**

| Directive  | Meaning                                 |
|------------|-----------------------------------------|
| `trigger:` | `long_press` (default) / `right_click`  |
| `anchor:`  | `#component_id` the menu is attached to |

**ContextMenuItem:**

| Directive      | Meaning                                    |
|----------------|--------------------------------------------|
| `text:`        | Item label                                 |
| `icon:`        | Optional icon name                         |
| `destructive:` | Boolean — styles item in destructive color |
| `on tap:`      | Action fired when item is tapped           |

**A11Y:** `ContextMenu` role `menu`. Each `ContextMenuItem` role `menuitem`; destructive items should include
`"destructive action"` in their `a11y:` label. On open, focus moves to the first item; on close, focus returns to the
anchor.

```ssdl
#message_context: ContextMenu {
  anchor: #message_bubble
  children: [#ctx_reply, #ctx_copy, #ctx_delete]
}

#ctx_reply: ContextMenuItem {
  in: #message_context
  text: "Reply"
  icon: "reply"
  on tap: replyTo($message)
}

#ctx_copy: ContextMenuItem {
  in: #message_context
  text: "Copy"
  icon: "copy"
  on tap: copyMessage($message)
}

#ctx_delete: ContextMenuItem {
  in: #message_context
  text: "Delete"
  icon: "trash"
  destructive: true
  on tap: deleteMessage($message)
  a11y: "Delete, destructive action"
}
```

---

### 19.23 ActionSheet

| Directive       | Meaning                                                 |
|-----------------|---------------------------------------------------------|
| `title:`        | Optional header                                         |
| `message:`      | Optional description                                    |
| `actions:`      | Array of `{ text, style: default/destructive, on tap }` |
| `cancel_label:` | Cancel action label (default `"Cancel"`)                |

**A11Y default role:** `dialog`.

```ssdl
#photo_action_sheet: ActionSheet {
  title: copy.profile.change_photo_title
  actions: [
    { text: copy.profile.take_photo,     style: default,     on tap: openCamera() },
    { text: copy.profile.choose_library, style: default,     on tap: openLibrary() },
    { text: copy.profile.remove_photo,   style: destructive, on tap: removePhoto() }
  ]
  cancel_label: copy.common.cancel
  visible_when: $photo_sheet_open
}
```

---

### 19.24 EmptyState

Single component replaces `EmptyState` and `ErrorState`. The `type:` directive expresses semantic intent and drives
default illustration selection in the design system — omit `illustration:` to use the type default.

| Directive       | Meaning                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------|
| `type:`         | `empty` (default) / `error` / `offline` / `no_results` / `permission_denied` / `custom` — see §51.28 |
| `illustration:` | Override image path, icon name, or Lottie source; omit to use type default                           |
| `title:`        | Primary heading — required (LINT-037)                                                                |
| `description:`  | Supporting description                                                                               |
| `cta:`          | Inline CTA — `"Label" -> action()` or `"Label" -> Destination` — required (LINT-037)                 |

**A11Y:** region role `text`; CTA role `button`.

```ssdl
#orders_empty: EmptyState {
  in: #content
  pos: parent.center
  type: empty
  title: copy.orders.empty_title
  description: copy.orders.empty_body
  cta: copy.orders.empty_cta -> nav Shop
  visible_when: $orders.empty
}

#load_error: EmptyState {
  in: #content
  pos: parent.center
  type: error
  title: copy.common.error_title
  description: copy.common.error_body
  cta: copy.common.retry -> retryLoad()
  visible_when: @error
}
```

---

### 19.25 Popover

| Directive                 | Meaning                                               |
|---------------------------|-------------------------------------------------------|
| `anchor:`                 | `#component_id` the popover is attached to            |
| `placement:`              | `top` / `bottom` / `left` / `right` / `auto` (§51.15) |
| `dismiss_on_outside_tap:` | Boolean (default `true`)                              |

**A11Y default role:** `dialog`. Move focus inside on open; return focus to anchor on close.

```ssdl
#info_popover: Popover {
  anchor: #info_icon
  placement: bottom
  size: w:lg h:hug
  visible_when: $info_open
  children: [#info_text]
}
```

---

### 19.26 Dialog

Replaces `ConfirmDialog` and `DialogBox`. Single type handles all focused dialog patterns: omit `cancel_label:` for a
single-button informational dialog; add `cancel_label:` for a two-button choice; set `destructive: true` to style the
confirm action in a destructive color.

| Directive        | Meaning                                                   |
|------------------|-----------------------------------------------------------|
| `title:`         | Dialog heading                                            |
| `message:`       | Body text                                                 |
| `confirm_label:` | Confirm/primary button label                              |
| `cancel_label:`  | Cancel button label — **omit for single-button dialogs**  |
| `destructive:`   | Boolean — styles confirm as destructive (default `false`) |
| `on confirm:`    | Action on confirm                                         |
| `on cancel:`     | Action on cancel                                          |

**A11Y default role:** `alertdialog`.

```ssdl
// Two-button destructive confirmation
#delete_confirm: Dialog {
  title: copy.orders.delete_title
  message: copy.orders.delete_message
  confirm_label: copy.common.delete
  cancel_label: copy.common.cancel
  destructive: true
  on confirm: deleteOrder($order)
  on cancel: set $confirm_open := false
  visible_when: $confirm_open
}

// Single-button informational dialog
#info_dialog: Dialog {
  title: copy.onboarding.tip_title
  message: copy.onboarding.tip_body
  confirm_label: copy.common.got_it
  on confirm: set $tip_open := false
  visible_when: $tip_open
}
```

---

### 19.27 StepIndicator

| Directive  | Meaning                                               |
|------------|-------------------------------------------------------|
| `steps:`   | Total step count                                      |
| `current:` | Active step index (0-based) or `$field`               |
| `style:`   | `dots` / `numbers` / `bars` / `progress_bar` (§51.16) |

**A11Y default role:** `text` with label `"Step {current+1} of {steps}"`.

```ssdl
#onboarding_steps: StepIndicator {
  in: #footer
  steps: 4
  current: $onboarding_step
  style: dots
  a11y: "Step {$onboarding_step + 1} of 4"
}
```

---

### 19.28 Progress

`Progress` uses `style:` to choose between linear and circular rendering.

| Directive        | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| `style:`         | `linear` — horizontal track bar; `circular` — ring/donut                        |
| `value:`         | Current progress — 0 to `max`; required unless `indeterminate: true` (LINT-038) |
| `max:`           | Maximum value (default `100`)                                                   |
| `indeterminate:` | Boolean — animated indefinite progress; ignores `value:`                        |

```ssdl
#upload_progress: Progress {
  in: #upload_card
  style: linear
  value: $upload.bytes_sent
  max: $upload.total_bytes
  size: w:fill h:xxs
  a11y: "Upload progress, {$upload.bytes_sent} of {$upload.total_bytes} bytes"   // or use a derived $upload.percent ==> ($upload.bytes_sent / $upload.total_bytes) * 100 in MODEL
}

#save_ring: Progress {
  in: #form_footer
  style: circular
  indeterminate: true
  size: sm
  visible_when: @saving
}
```

---

### 19.29 LoadingOverlay

| Directive     | Meaning                         |
|---------------|---------------------------------|
| `message:`    | Optional text below the spinner |
| `cancelable:` | Boolean — show a cancel action  |
| `on cancel:`  | Action when user cancels        |

**A11Y default role:** `dialog`. Move focus into the overlay on show.

```ssdl
#processing_overlay: LoadingOverlay {
  in: #screen
  layer: z:overlay
  message: copy.payment.processing
  cancelable: false
  visible_when: @processing
  a11y: "Processing payment, please wait"
}
```

---

### 19.30 NetworkBanner

| Directive           | Meaning                          |
|---------------------|----------------------------------|
| `offline_msg:`      | Copy when network is unavailable |
| `reconnecting_msg:` | Copy while reconnecting          |

Use `visible_when:` bound to a network state field.

```ssdl
#network_banner: NetworkBanner {
  in: #screen
  pos: sticky(top)
  offline_msg: copy.common.offline
  reconnecting_msg: copy.common.reconnecting
  visible_when: !$network.connected
  a11y: announce_when_visible
}
```

---

### 19.31 PullToRefresh

| Directive           | Meaning                                                                   |
|---------------------|---------------------------------------------------------------------------|
| `on refresh:`       | Action when pull gesture completes — required (LINT-039)                  |
| `refreshing:`       | Boolean field or state bound to in-progress refresh — required (LINT-039) |
| `custom_indicator:` | Optional `#component_id` to override the platform default pull animation  |

Wrap around a `Scroll` or `List`.

```ssdl
#orders_refresh: PullToRefresh {
  in: #screen
  on refresh: refreshOrders()
  refreshing: @refreshing
  children {
    #orders_list: List { ... }
  }
}
```

---

### 19.32 NavBar

| Directive      | Meaning                                                       |
|----------------|---------------------------------------------------------------|
| `title:`       | Screen title — required (LINT-035)                            |
| `left:`        | Leading action — back button or menu icon                     |
| `right:`       | Trailing actions — array of component IDs or inline `IconBtn` |
| `large_title:` | Boolean — iOS large title style; collapses on scroll          |
| `translucent:` | Boolean — frosted glass background                            |

**A11Y default role:** `navigation`.

```ssdl
#main_nav: NavBar {
  in: #screen
  pos: sticky(top.safe)
  title: copy.orders.screen_title   // illustrative — define in COPY section of this screen's spec
  left: #back_btn
  right: [#filter_btn, #search_btn]
  large_title: false
}
```

---

### 19.33 TabBar and TabItem

**TabBar:**

| Directive        | Meaning                                                    |
|------------------|------------------------------------------------------------|
| `items:`         | Array of `TabItem` component IDs — required (LINT-036)     |
| `on tab_change:` | Action with newly selected tab value — required (LINT-036) |

**TabItem:**

| Directive        | Meaning                      |
|------------------|------------------------------|
| `label:`         | Tab label                    |
| `icon:`          | Icon name or component       |
| `badge:`         | Count or string badge        |
| `selected_when:` | Condition for active styling |

**A11Y:** `TabBar` role is `tablist`; `TabItem` role is `tab`.

```ssdl
#main_tab_bar: TabBar {
  in: #screen
  pos: sticky(bottom.safe)
  items: [#tab_home, #tab_orders, #tab_profile]
  on tab_change: set $active_tab := $tab
}

#tab_home: TabItem {
  in: #main_tab_bar
  label: copy.nav.home
  icon: "home"
  selected_when: $active_tab == home
}

#tab_orders: TabItem {
  in: #main_tab_bar
  label: copy.nav.orders
  icon: "bag"
  badge: $orders.pending_count
  selected_when: $active_tab == orders
}
```

---

### 19.34 Drawer and DrawerItem

**Drawer:**

| Directive                | Meaning                                              |
|--------------------------|------------------------------------------------------|
| `side:`                  | `left` (default) / `right`                           |
| `width:`                 | Width of the open drawer — size token                |
| `overlay:`               | Boolean — dim content behind drawer (default `true`) |
| `gesture_enabled:`       | Boolean — allow swipe-to-open (default `true`)       |
| `on open:` / `on close:` | Actions fired on state change                        |

**DrawerItem:**

| Directive        | Meaning                                                        |
|------------------|----------------------------------------------------------------|
| `icon:`          | Icon name or component                                         |
| `label:`         | Item label                                                     |
| `selected_when:` | Active/selected condition                                      |
| `badge:`         | Badge count or string                                          |
| `on tap:`        | Action fired when item is tapped — typically `nav Destination` |

**A11Y:** `Drawer` role `navigation`; `DrawerItem` role `menuitem`.

```ssdl
#side_drawer: Drawer {
  in: #screen
  side: left
  width: lg
  visible_when: $drawer_open
  on close: set $drawer_open := false
  children: [#item_home, #item_settings]
}

#item_home: DrawerItem {
  in: #side_drawer
  icon: "home"
  label: copy.nav.home
  selected_when: $active_route == home
  on tap: nav Home
}
```

---

### 19.35 StickyHeader

| Directive            | Meaning                                                      |
|----------------------|--------------------------------------------------------------|
| `collapse_height:`   | Height of the pinned collapsed state                         |
| `expanded_content:`  | Component visible only when expanded                         |
| `collapsed_content:` | Component visible only when collapsed (typically a `NavBar`) |
| `parallax:`          | Boolean — scroll content behind header at reduced rate       |

```ssdl
#profile_header: StickyHeader {
  in: #scroll
  size: w:fill h:xxl
  collapse_height: lg
  expanded_content: #profile_hero
  collapsed_content: #profile_nav
  parallax: true
}
```

---

### 19.36 Carousel

| Directive          | Meaning                                                                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `fill:`            | Boolean — when `true`, items fill the full viewport (full-bleed page mode); when `false` (default), items show a partial peek of adjacent items    |
| `data:`            | Bound collection                                                                                                                                   |
| `item:`            | Item template component ID                                                                                                                         |
| `peek:`            | Spacing token — how much of adjacent item is visible; ignored when `fill: true`                                                                    |
| `gap:`             | Space between items                                                                                                                                |
| `snap:`            | Boolean — snap to item boundaries                                                                                                                  |
| `orientation:`     | `horizontal` (default) / `vertical` — see §51.26                                                                                                   |
| `indicator:`       | Boolean — show page dots                                                                                                                           |
| `current:`         | Bind to current page index field                                                                                                                   |
| `on slide_change:` | Action fired with current index                                                                                                                    |
| `pagination:`      | `none` / `endless_scroll`                                                                                                                          |

**A11Y default role:** scrollable region; each item should declare its own role.

```ssdl
#promo_carousel: Carousel {
  in: #home_header
  data: $promotions
  item: #promo_card
  peek: sm
  gap: sm
  indicator: true
  on slide_change: trackPromoImpression($index)   // define trackPromoImpression() in ACTIONS; emit an analytics event with slide index
  pagination: none
}
```

---

### 19.37 SectionList

| Directive         | Meaning                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `sections:`       | Bound collection of `{ title, data }`                                   |
| `section_header:` | Template component ID for section headers                               |
| `item:`           | Item template component ID                                              |
| `sticky_headers:` | Boolean — section headers pin while section is visible (default `true`) |
| `empty_state:`    | Component shown when sections is empty                                  |

```ssdl
#contacts_list: SectionList {
  in: #content
  sections: $contacts_by_letter
  section_header: #alpha_header
  item: #contact_row
  sticky_headers: true
  empty_state: #contacts_empty
}
```

---

### 19.38 Table

| Directive         | Meaning                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------|
| `columns:`        | Array of column defs — see §51.20                                                                   |
| `data:`           | Bound collection                                                                                    |
| `sortable:`       | Boolean — enable column sorting                                                                     |
| `on sort:`        | Action fired with `{ column: String, direction: asc/desc }` when user taps a sortable column header |
| `on row_tap:`     | Action fired with the row's bound data item when user taps a row                                    |
| `frozen_columns:` | First N columns stay fixed on horizontal scroll                                                     |
| `selection:`      | `none` / `single` / `multi`                                                                         |
| `empty_state:`    | Component shown when data is empty                                                                  |

**A11Y default role:** `grid`.

```ssdl
#transactions_table: Table {
  in: #content
  data: $transactions
  columns: [
    { id: date,        header: "Date",        width: md,   sortable: true  },
    { id: description, header: "Description", width: fill                  },
    { id: amount,      header: "Amount",      width: md,   sortable: true  }
  ]
  on sort: sortTransactions($column, $direction)   // $column = column id string; $direction = "asc" | "desc"
  selection: none
  empty_state: #transactions_empty
}
```

---

### 19.39 SearchBar

| Directive      | Meaning                              |
|----------------|--------------------------------------|
| `placeholder:` | Hint text                            |
| `bind:`        | Binds to a `String` field            |
| `show_filter:` | Boolean — show a filter icon         |
| `on cancel:`   | Action when user dismisses search    |
| `on filter:`   | Action when user taps filter         |
| `autofocus:`   | Boolean — focus immediately on mount |

```ssdl
#product_search: SearchBar {
  in: #screen
  pos: sticky(top.safe)
  size: w:fill h:lg
  placeholder: copy.shop.search_placeholder
  bind: $search_query
  show_filter: true
  on cancel: clearSearch()
  on filter: openFilters()
}
```

---

### 19.40 Accordion

| Directive         | Meaning                                                           |
|-------------------|-------------------------------------------------------------------|
| `items:`          | Array of `{ header, content: #component_id }` or bound collection |
| `allow_multiple:` | Boolean — multiple sections open simultaneously                   |
| `on expand:`      | Action when a section opens                                       |
| `on collapse:`    | Action when a section closes                                      |

**A11Y:** header buttons use `button` role with `expanded` state.

```ssdl
#faq_accordion: Accordion {
  in: #content
  items: $faq_items
  allow_multiple: false
  on expand: trackFaqExpand($item)
}
```

---

### 19.41 Collapsible

| Directive    | Meaning                                       |
|--------------|-----------------------------------------------|
| `open:`      | Boolean field or state controlling visibility |
| `on toggle:` | Action fired when open state changes          |

Author supplies the trigger component — typically a `Btn` or `Link` with `on tap: set $open := !$open`.

**A11Y:** The trigger component must reflect expanded/collapsed state. Add `a11y: "Show advanced options, collapsed"` /
`"Hide advanced options, expanded"` on the trigger, or use `aria_expanded: $show_advanced` if the platform supports it.
The collapsible region itself needs no additional role.

```ssdl
#advanced_options: Collapsible {
  in: #form
  open: $show_advanced
  on toggle: set $show_advanced := !$show_advanced
  children: [#advanced_fields]
}
```

---

### 19.42 FormGroup

| Directive      | Meaning                                                   |
|----------------|-----------------------------------------------------------|
| `label:`       | Section label                                             |
| `required:`    | Boolean — shows required marker on the label              |
| `helper_text:` | Hint below the group                                      |
| `error:`       | Group-level error (distinct from individual field errors) |

```ssdl
#address_group: FormGroup {
  in: #checkout_form
  label: copy.checkout.shipping_address
  required: true
  children: [#address_line1, #address_line2, #city_input, #postcode_input]
}
```

---

### 19.43 InlineLoader

Reuses standard directives only (`size:`, `visible_when:`). No component-specific directives.

**A11Y default role:** `none` (decorative) when scoped to a row or card that itself has a loading state — the parent's
`loading_when:` state should be announced instead. Use `a11y: announce_when_visible` only when the `InlineLoader` is the
sole indication that something is happening (no loading text or state change on the parent).

```ssdl
#sync_loader: InlineLoader {
  in: #order_row
  pos: right_of(#order_status, sm)
  size: xs
  visible_when: $order.syncing
}
```

---

### 19.44 Modal

Arbitrary-content modal container. Unlike `Dialog` (the fixed title + message + confirm/cancel shape, §19.26), `Modal`
imposes no internal structure — you supply `children:`. Reach for `Modal` when the overlay hosts a form, a custom
layout, or anything richer than a confirm prompt; reach for `Dialog` for the standard title/message/actions pattern.

| Directive                 | Meaning                                                              |
|---------------------------|----------------------------------------------------------------------|
| `dismissible:`            | Boolean — show a close affordance / allow swipe-down (default `true`) |
| `dismiss_on_outside_tap:` | Boolean — tapping the scrim closes the modal (default `true`)        |
| `on dismiss:`             | Action fired when the modal is dismissed                             |

**A11Y default role:** `dialog`. Trap focus inside while open; move focus in on present and return it to the trigger on
dismiss.

```ssdl
#filters_modal: Modal {
  in: #screen
  layer: z:modal
  visible_when: $filters_open
  on dismiss: set $filters_open := false
  children: [#filters_form, #apply_btn]
}
```

---

### 19.45 Banner

Inline or global message strip. `type:` sets the severity, which drives the color, the default leading icon, and the
accessibility announcement priority.

| Directive      | Meaning                                                                                  |
|----------------|------------------------------------------------------------------------------------------|
| `type:`        | `info` (default) / `success` / `warning` / `error` — severity styling and a11y priority  |
| `dismissible:` | Boolean — show a close affordance (default `false`)                                       |
| `icon:`        | Override the default leading icon for the `type:`                                         |
| `on dismiss:`  | Action fired when the user closes the banner                                              |

**A11Y default role:** `status` (announced politely). `type: error` and `type: warning` raise it to `alert` (announced
assertively). Add `a11y: announce_when_visible` on banners shown conditionally so they are announced when they appear.

```ssdl
#error_banner: Banner {
  in: #form
  type: error
  text: $error_msg
  visible_when: $error_msg.exists
  a11y: announce_when_visible
}
```

---

### 19.46 Grid

| Directive  | Meaning                                                               |
|------------|-----------------------------------------------------------------------|
| `columns:` | Number of columns                                                     |
| `masonry:` | Boolean — variable item heights (Pinterest-style); off = uniform rows |
| `data:`    | Bound collection (with `as` element binding)                          |
| `item:`    | Item template component ID                                            |

**A11Y note:** with `masonry: true`, VoiceOver/TalkBack read items in source order regardless of visual column — this is
expected.

```ssdl
#photo_grid: Grid {
  in: #content
  data: $photos as $photo
  item: #photo_card
  columns: 2
  masonry: true
  gap: xs
  empty_state: #photos_empty
}
```

---

### 19.47 HStack

| Directive  | Meaning                                             |
|------------|-----------------------------------------------------|
| `wrap:`    | Boolean — wrap children onto multiple lines         |
| `row_gap:` | Spacing between wrapped lines (companion to `gap:`) |

```ssdl
#filter_chips: HStack {
  in: #filter_bar
  wrap: true
  gap: xs
  row_gap: xs
  data: $active_filters as $filter
  item: #filter_chip
}
```

---

## 20. UI directive grammar

```ssdl
UIComponent     := ComponentId ":" ComponentType [String] ComponentBlock
ComponentBlock  := "{" ComponentDirective* "}"

ComponentDirective := ParentDirective
                    | PositionDirective
                    | AlignmentDirective
                    | SizeDirective
                    | SpacingDirective
                    | LayerDirective
                    | StyleDirective
                    | BehaviorDirective
                    | ContentDirective
                    | InputConstraintDirective
                    | AutofillDirective
                    | BindingDirective
                    | KeyboardDirective
                    | ValidationDirective
                    | StateDirective
                    | TestDirective
                    | ConditionDirective
                    | AnimationDirective
                    | TransitionDirective
                    | EventDirective
                    | ChildrenDirective
                    | AccessibilityDirective
                    | CustomDirective

ParentDirective       := "in:" ComponentId
PositionDirective     := "pos:" Position
AlignmentDirective    := "align:" Alignment
SizeDirective         := "size:" SizeExpr
SpacingDirective      := ("gap:" | "pad:" | "margin:" | "inset:") SpacingToken
LayerDirective        := "layer:" LayerExpr
StyleDirective        := "style:" StyleToken
BehaviorDirective     := "behavior:" BehaviorExpr
ContentDirective      := ("label:" | "placeholder:" | "helper_text:" | "error:"
                       | "value:" | "text:") (CopyKey | String | Expression)
InputConstraintDirective := ("min:" | "max:" | "step:") Number
AutofillDirective     := ("autocomplete:" AutocompleteType) | ("autocapitalize:" CapType)
BindingDirective      := "bind:" FieldId
KeyboardDirective     := "keyboard:" KeyboardType
ValidationDirective   := "validation:" "none"
StateDirective        := ("checked_when:" | "selected_when:" | "disabled_when:") Condition
TestDirective         := "test_id:" String
ConditionDirective    := ("visible_when:" | "hidden_when:" | "enabled_when:"
                       | "loading_when:" | "readonly_when:") Condition
AnimationDirective    := "animate:" AnimationExpr                          // see §33.1
TransitionDirective   := "transition:" "shared(" SharedElementKey ")"      // see §33.2; SharedElementKey must match the destination screen's declaration
EventDirective        := "on" EventName ":" Effect ["when" Condition]
ChildrenDirective     := "children:" "[" ComponentId* "]"
AccessibilityDirective:= "a11y:" AccessibilityExpr

// Component-specific directives (see §19 for per-component usage)
LottieDirective       := ("source:" String) | ("autoplay:" Boolean) | ("loop:" Boolean)
                       | ("speed:" Number) | ("progress:" FieldId)
MapDirective          := ("center:" LatLng) | ("zoom:" ZoomToken) | ("markers:" FieldId)
                       | ("interactive:" Boolean)
OTPDirective          := ("length:" Integer) | ("mask:" Boolean)
PhoneDirective        := ("default_country:" CountryCode) | ("allowed_countries:" "[" CountryCode+ "]")
SegmentedDirective    := "segments:" "[" SegmentDef+ "]"
ToggleGroupDirective  := ("options:" "[" ToggleOption+ "]") | ("selection:" SelectionMode)
TagInputDirective     := ("max_tags:" Integer) | ("suggestions:" FieldId)
LocationDirective     := ("bias_country:" CountryCode) | ("result_types:" LocationResultType)
ColorPickerDirective  := ("mode:" ColorMode) | ("palette:" "[" HexColor+ "]")
ScannerDirective      := ("formats:" "[" BarcodeFormat+ "]") | ("overlay_hint:" String)
RichTextDirective     := ("toolbar:" "[" RichTextTool+ "]") | ("max_length:" Integer)
                       // on change: is handled by the standard EventDirective
CarouselDirective     := ("fill:" Boolean) | ("peek:" SpacingToken) | ("snap:" Boolean)
                       | ("indicator:" Boolean) | ("pagination:" PaginationStrategy)
                       | ("orientation:" Orientation) | ("current:" FieldId)
                       // fill:true = full-bleed page mode; fill:false (default) = peek carousel mode
SectionListDirective  := ("sections:" FieldId) | ("section_header:" ComponentId) | ("sticky_headers:" Boolean) | ("empty_state:" ComponentId)
TableDirective        := ("columns:" "[" ColumnDef+ "]") | ("sortable:" Boolean) | ("frozen_columns:" Integer) | ("on row_tap:" Effect)
AccordionDirective    := ("items:" FieldId) | ("allow_multiple:" Boolean)
CollapsibleDirective  := ("open:" Condition) | ("on toggle:" Effect)
DrawerDirective       := ("side:" DrawerSide) | ("gesture_enabled:" Boolean) | ("overlay:" Boolean)
NavBarDirective       := ("title:" String) | ("left:" ComponentId) | ("right:" "[" ComponentId+ "]")
                       | ("large_title:" Boolean) | ("translucent:" Boolean)
TabBarDirective       := ("items:" "[" ComponentId+ "]")
SpeedDialDirective    := ("direction:" Direction)
                       // children are SpeedDialItem components; no inline actions array
SpeedDialItemDir      := ("icon:" String) | ("text:" String)
ContextMenuDirective  := ("trigger:" ContextTrigger) | ("anchor:" ComponentId)
                       // children are ContextMenuItem components; no inline items array
ContextMenuItemDir    := ("text:" String) | ("icon:" String) | ("destructive:" Boolean)
ActionSheetDirective  := ("title:" String) | ("message:" String) | ("actions:" "[" SheetAction+ "]") | ("cancel_label:" String)
DialogDirective       := ("title:" String) | ("message:" String) | ("confirm_label:" String)
                       | ("cancel_label:" String) | ("destructive:" Boolean)
                       // cancel_label omitted = single-button dialog
ModalDirective        := ("dismissible:" Boolean) | ("dismiss_on_outside_tap:" Boolean)
                       // Modal holds arbitrary content via children:; see §19.44 — use Dialog for title+message+actions
EmptyStateDirective   := ("type:" EmptyStateType) | ("illustration:" String) | ("title:" String)
                       | ("description:" String) | ("cta:" CTAExpr)  // see §51.28 for type values
ProgressDirective     := ("style:" ProgressStyle) | ("value:" NumberOrField) | ("max:" Number) | ("indeterminate:" Boolean)
StepIndicatorDirective:= ("steps:" Integer) | ("current:" NumberOrField) | ("style:" StepStyle)
LoadingOverlayDir     := ("message:" String) | ("cancelable:" Boolean)
PullToRefreshDir      := ("refreshing:" FieldIdOrState) | ("custom_indicator:" ComponentId)
NetworkBannerDir      := ("offline_msg:" String) | ("reconnecting_msg:" String)
BannerDirective       := ("type:" BannerType) | ("dismissible:" Boolean) | ("icon:" String)
                       // BannerType = info (default) | success | warning | error
StickyHeaderDir       := ("collapse_height:" SizeToken) | ("expanded_content:" ComponentId)
                       | ("collapsed_content:" ComponentId) | ("parallax:" Boolean)
HStackDirective       := ("wrap:" Boolean) | ("row_gap:" SpacingToken)
                       // wrap:true enables line-wrapping
GridDirective         := ("masonry:" Boolean) | ("columns:" Integer)
                       // masonry:true enables variable item heights
FormGroupDirective    := ("required:" Boolean)
PriceTagDirective     := ("amount:" NumberOrField) | ("currency:" String) | ("original:" NumberOrField)
StatDirective         := ("subtitle:" String) | ("trend:" TrendDir) | ("trend_value:" StringOrField)
NumberBadgeDirective  := ("count:" NumberOrField) | ("max:" Integer)
StatusIndicatorDir    := ("status:" StatusValue) | ("color:" String)
QRCodeDirective       := ("value:" String) | ("error_correction:" ECLevel)
ThumbnailDirective    := ("src:" String) | ("fallback:" String) | ("aspect:" AspectRatio)
PopoverDirective      := ("anchor:" ComponentId) | ("placement:" PopoverPlacement)
                       | ("dismiss_on_outside_tap:" Boolean)
SearchBarDirective    := ("show_filter:" Boolean) | ("autofocus:" Boolean)
TagDirective          := ("text:" String) | ("removable:" Boolean) | ("style:" TagStyle)
RatingDirective       := ("value:" NumberOrField) | ("max:" Integer) | ("style:" RatingStyle)
```

---

## 21. Nesting and component relationships

SSDL supports two ways to express nesting: explicit parent references and inline children.

### 21.1 Explicit parent references

```ssdl
#screen: SafeArea {
  children: [#content, #footer]
}

#content: Scroll {
  in: #screen
  children: [#header, #form]
}

#form: VStack {
  in: #content
  children: [#email_input, #password_input, #login_btn]
}
```

### 21.2 Inline nesting

```ssdl
#content: Scroll {
  in: #screen

  children {
    #header: VStack {
      children {
        #title: Txt "Welcome back"
        #subtitle: Txt "Log in to continue"
      }
    }

    #form: VStack {
      children {
        #email_input: Input "Email"
        #password_input: Pwd "Password"
        #login_btn: Btn "Log In"
      }
    }
  }
}
```

### 21.3 Recommended rule

For production handoff, prefer explicit `in:` and `children:` references because they are easier to lint, diff, and
convert into implementation tasks.

---

## 22. Positioning directives

Use `pos` to specify where an element belongs. Positioning should be semantic, not pixel-perfect.

### 22.1 Anchor positions

```ssdl
pos: top
pos: bottom
pos: left
pos: right
pos: center

pos: top.left
pos: top.center
pos: top.right

pos: middle.left
pos: middle.center
pos: middle.right

pos: bottom.left
pos: bottom.center
pos: bottom.right
```

Anchor qualifiers:

```ssdl
pos: screen.top.center
pos: parent.center
pos: safe.top.right
pos: content.bottom
pos: keyboard.above
```

Examples:

```ssdl
#title: Txt "Welcome back" {
  pos: parent.top.center
}

#close_btn: IconBtn "Close" {
  pos: safe.top.right
}

#empty_state: Card {
  pos: parent.center
}
```

### 22.2 Relative positions

```ssdl
pos: below(#target)
pos: below(#target, sm)
pos: above(#target, md)
pos: left_of(#target, xs)
pos: right_of(#target, xs)
pos: before(#target)
pos: after(#target)
pos: between(#a, #b)
pos: near(#target)
```

Examples:

```ssdl
#subtitle: Txt "Log in to continue" {
  pos: below(#title, xs)
  align: center
}

#password_input: Pwd "Password" {
  pos: below(#email_input, md)
  size: same_w(#email_input) h:lg
}

#forgot_link: Link "Forgot password?" {
  pos: below(#password_input, sm)
  align: end
}
```

### 22.3 Inside and overlay positions

```ssdl
pos: inside(#card, top.left)
pos: inside(#avatar, bottom.right)
pos: overlay(#target, top.right)
pos: overlay(#target, bottom.center)
```

Examples:

```ssdl
#edit_avatar_btn: IconBtn "Edit" {
  pos: overlay(#avatar_img, bottom.right)
  size: smaller(#avatar_img, 2)
}

#badge: Badge "PRO" {
  pos: overlay(#plan_card, top.right)
  size: xs
}
```

### 22.4 Sticky and floating positions

```ssdl
pos: sticky(top)
pos: sticky(bottom)
pos: sticky(bottom.safe)
pos: floating(bottom.right)
pos: floating(top.right)
```

Examples:

```ssdl
#checkout_footer: Footer {
  pos: sticky(bottom.safe)
  size: w:fill h:hug
  pad: md
}

#add_fab: FAB "+" {
  pos: floating(bottom.right)
  size: lg
}
```

---

## 23. Alignment directives

Use `align` for internal or external alignment.

### 23.1 Simple alignment

```ssdl
align: start
align: center
align: end
align: stretch
```

Examples:

```ssdl
#header: VStack {
  align: center
}

#form: VStack {
  align: stretch
}

#forgot_link: Link "Forgot password?" {
  align: end
}
```

### 23.2 Axis alignment

Use `main` and `cross` for stack-like containers.

```ssdl
align: main:start cross:stretch
align: main:center cross:center
align: main:end cross:center
align: main:space_between cross:center
align: main:space_around cross:center
```

Example:

```ssdl
#signup_row: HStack {
  align: main:center cross:center
  gap: xs
}
```

### 23.3 Reference alignment

```ssdl
align: align_to(#target.left)
align: align_to(#target.right)
align: align_to(#target.center)
align: baseline_of(#target)
```

Example:

```ssdl
#helper_text: Txt "Use at least 8 characters" {
  pos: below(#password_input, xs)
  align: align_to(#password_input.left)
}
```

---

## 24. Sizing directives

Use `size` to express intended size. Do not use exact dimensions unless a platform-specific implementation note requires
it.

### 24.1 Base size tokens

```txt
xxs
xs
sm
md
lg
xl
xxl
```

Recommended interpretation:

| Token | Meaning                                      |
|-------|----------------------------------------------|
| `xxs` | Tiny element, such as a dot or small badge   |
| `xs`  | Extra-small element                          |
| `sm`  | Small element                                |
| `md`  | Default/medium element                       |
| `lg`  | Large, primary, or comfortable touch element |
| `xl`  | Extra-large or prominent element             |
| `xxl` | Hero-sized or highly prominent element       |

### 24.2 Width and height hints

```ssdl
size: w:fill
size: w:hug
size: w:wrap
size: w:content
size: w:full
size: w:screen

size: h:fill
size: h:hug
size: h:wrap
size: h:content
size: h:sm
size: h:lg
```

Recommended meanings:

| Token     | Meaning                                                 |
|-----------|---------------------------------------------------------|
| `hug`     | Size tightly to content                                 |
| `wrap`    | Wrap content, allowing line breaks or natural expansion |
| `fill`    | Fill available parent space                             |
| `full`    | Full size of parent on that axis                        |
| `screen`  | Full screen size on that axis                           |
| `content` | Natural content size                                    |

Examples:

```ssdl
#avatar_img: Img {
  size: w:lg h:lg
}

#login_btn: Btn "Log In" {
  size: w:fill h:lg
}

#terms_text: Txt {
  size: w:fill h:wrap
}
```

### 24.3 Relative sizing

```ssdl
size: same(#target)
size: same_w(#target)
size: same_h(#target)
size: smaller(#target)
size: smaller(#target, 1)
size: smaller(#target, 2)
size: larger(#target)
size: larger(#target, 1)
size: half_of(#target)
size: third_of(#target)
size: min(a, b)
size: max(a, b)
```

Examples:

```ssdl
#confirm_password_input: Pwd "Confirm password" {
  size: same_w(#password_input) h:lg
}

#secondary_btn: Btn "Cancel" {
  size: same_w(#primary_btn)
}

#badge: Badge "NEW" {
  size: smaller(#plan_card, 2)
}
```

### 24.4 Sizing conflict rule

If both a general size and axis-specific size are present, axis-specific values win.

```ssdl
#cta: Btn "Continue" {
  size: lg w:fill
}
```

Interpretation: large button treatment, width fills parent.

---

## 25. Spacing directives

Use spacing tokens for gaps, padding, margins, and insets.

```txt
none
xxs
xs
sm
md
lg
xl
xxl
```

### 25.1 Spacing properties

| Directive | Meaning                                        |
|-----------|------------------------------------------------|
| `gap`     | Space between children in a container          |
| `pad`     | Internal padding inside a component            |
| `margin`  | External spacing around a component            |
| `inset`   | Safe or edge inset, often for overlays/footers |

Examples:

```ssdl
#form: VStack {
  gap: md
  pad: lg
}

#card: Card {
  margin: md
  pad: lg
}

#footer: Footer {
  pos: sticky(bottom.safe)
  inset: safe.bottom
  pad: md
}
```

### 25.2 Directional spacing

Directional forms are allowed when needed.

```ssdl
pad: top:lg right:md bottom:lg left:md
margin: top:sm bottom:xl
inset: bottom:safe
```

---

## 26. Layering and z-order directives

Use `layer` when components overlap or sit above/below other elements.

```ssdl
layer: above(#content)
layer: below(#modal)
layer: z:0
layer: z:1
layer: z:overlay
layer: z:modal
layer: z:toast
```

Examples:

```ssdl
#loading_overlay: Overlay {
  in: #screen
  layer: above(#content)
  visible_when: @loading
}

#toast: Toast {
  layer: z:toast
  pos: floating(bottom.center)
}
```

Recommended z-order semantics:

| Layer       | Meaning                         |
|-------------|---------------------------------|
| `z:0`       | Default content                 |
| `z:1`       | Above default content           |
| `z:overlay` | Full-screen or partial overlay  |
| `z:modal`   | Modal/dialog level              |
| `z:toast`   | Transient message above most UI |

---

## 27. Behavior directives

Use `behavior` to express runtime layout behavior.

```ssdl
behavior: safe_area_aware
behavior: scroll_when_keyboard_open
behavior: avoid_keyboard
behavior: dismiss_keyboard_on_scroll
behavior: collapse_on_small_screen
behavior: stack_on_small_screen
behavior: hide_on_compact
behavior: sticky_on_scroll
behavior: pin_footer_on_tall_screen
behavior: preserve_scroll_position
behavior: pull_to_refresh
behavior: paged_scroll
behavior: snap_to_item
behavior: swipe_to_dismiss
behavior: drag_to_reorder
```

Examples:

```ssdl
#content: Scroll {
  behavior: scroll_when_keyboard_open
}

#footer: Footer {
  behavior: avoid_keyboard
  pos: sticky(bottom.safe)
}

#button_row: HStack {
  behavior: stack_on_small_screen
}
```

Multiple behaviors may be listed:

```ssdl
#content: Scroll {
  behavior: [scroll_when_keyboard_open, dismiss_keyboard_on_scroll, preserve_scroll_position]
}
```

---

## 28. Visibility, enabled, and loading directives

Use condition directives to connect UI to model/state.

```ssdl
visible_when: $error_msg.exists
enabled_when: $can_submit
loading_when: @loading
hidden_when: keyboard.open
readonly_when: $is_locked
```

Examples:

```ssdl
#error_banner: Banner {
  text: $error_msg
  visible_when: $error_msg.exists
}

#submit_btn: Btn "Submit" {
  enabled_when: $form_valid && !$is_loading
  loading_when: $is_loading
}
```

Recommended interpretation:

| Directive       | Meaning                                                  |
|-----------------|----------------------------------------------------------|
| `visible_when`  | Component exists or is visible only if condition is true |
| `hidden_when`   | Component is hidden if condition is true                 |
| `enabled_when`  | Component accepts interaction only if condition is true  |
| `readonly_when` | Component visible but not editable                       |
| `loading_when`  | Component shows loading treatment                        |

**Visibility vs tree presence:** SSDL treats `visible_when` and `hidden_when` as implementation-agnostic — whether the
component is removed from the layout tree or merely invisible is an implementation detail. However, note the
accessibility implication: a component hidden via opacity/display but still in the accessibility tree may be announced
by screen readers. For components that should be fully absent from the accessibility tree when not visible (e.g., error
banners), add `a11y: hidden_when_not_visible` to signal this intent to implementers.

---

## 29. Binding directives

Use `bind` to connect a UI component to a model field.

```ssdl
#email_input: Input "Email" {
  bind: $email
  keyboard: email
}
```

For one-way display:

```ssdl
#profile_name: Txt {
  text: $user.name
}
```

For collection binding:

```ssdl
#orders_list: List {
  data: $orders as $order
  item: #order_row
  pagination: endless_scroll
  empty_state: #orders_empty
  on scroll.end: loadNextPage() when $has_next_page
}

#order_row: ListItem {
  title: $order.title
  subtitle: $order.status
  on swipe_left: showDeleteAction($order)
  on tap: nav OrderDetail { order_id: $order.id }
}
```

The `as $order` clause on `data:` names the per-element binding, which the `item:` template (`#order_row`) references as
`$order`. A container declares iteration with `data:`/`item:` **or** an explicit `children:` list — never both.
`data:`/`item:` is not limited to scrollable collections; use it on layout stacks (`HStack`, `VStack`) too — e.g. a
wrapping row of filter chips.

### 29.1 Collection directives

| Directive        | Meaning                                  |
|------------------|------------------------------------------|
| `data:`          | Bound collection + element binding       |
| `item:`          | Item template component ID               |
| `pagination:`    | Pagination strategy                      |
| `empty_state:`   | Component shown when collection is empty |
| `selection:`     | Item selection mode                      |
| `on scroll.end:` | Action when user scrolls near the end    |

Pagination strategies:

```txt
endless_scroll     // Infinite scroll; load more at bottom
load_more_btn      // Explicit "Load more" button at end of list
paged              // Full-page pagination with page indicators
none               // Fixed list, no pagination
```

Selection modes:

```txt
none               // No item selection
single             // Tap selects one item at a time
multi              // Tap toggles item selection; multiple allowed
```

---

## 30. Event directives

Use `on <event>:` for component-specific events. The event name matches the FLOW vocabulary — no `on_` prefix. An
optional `when <condition>` guard may be appended inline.

```ssdl
on tap: submitLogin()
on long_press: showContextMenu()
on swipe_left: showDeleteAction()
on swipe_right: markAsDone()
on swipe_up: dismiss()
on swipe_down: minimize()
on change: validate $email
on focus: set $active_field := email
on blur: validate $email
on submit: submitLogin()
on scroll.end: loadNextPage()
on refresh: refreshData()
on appear: onComponentAppear()
on disappear: onComponentDisappear()
on select: onItemSelected($item)
on deselect: onItemDeselected($item)
```

Examples:

```ssdl
#password_input: Pwd "Password" {
  bind: $password
  on submit: submitLogin() when $can_submit
}

#order_row: ListItem {
  on swipe_left: showDeleteConfirm($order)
  on long_press: showOrderOptions($order)
}

#retry_btn: Btn "Retry" {
  visible_when: @error
  on tap: retryLastAction()
}
```

### 30.1 Component-to-FLOW event mapping

When a component declares `on <event>:`, the corresponding FLOW entry uses a namespaced event name for system-level
events. Direct user gestures map one-to-one.

| Component directive | FLOW event                        | Notes                                |
|---------------------|-----------------------------------|--------------------------------------|
| `on tap:`           | `on tap #id`                      | Direct                               |
| `on long_press:`    | `on long_press #id`               | Direct                               |
| `on swipe_left:`    | `on swipe_left #id`               | Direct                               |
| `on swipe_right:`   | `on swipe_right #id`              | Direct                               |
| `on swipe_up:`      | `on swipe_up #id`                 | Direct                               |
| `on swipe_down:`    | `on swipe_down #id`               | Direct                               |
| `on change:`        | `on input.change #id`             | Input value changed                  |
| `on focus:`         | `on focus #id`                    | Field gained focus                   |
| `on blur:`          | `on blur #id`                     | Field lost focus                     |
| `on submit:`        | `on keyboard.submit #id`          | Keyboard submit action               |
| `on scroll.end:`    | `on scroll.near_end #id`          | Scroll approached end                |
| `on refresh:`       | `on refresh #id`                  | Pull-to-refresh triggered            |
| `on select:`        | `on select #id`                   | Item selected                        |
| `on deselect:`      | `on deselect #id`                 | Item deselected                      |
| `on appear:`        | `on screen.view` (lifecycle)      | Component became visible; see §32    |
| `on disappear:`     | `on screen.disappear` (lifecycle) | Component left visible area; see §32 |

---

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

## 32. LIFECYCLE section

Use `LIFECYCLE` to declare screen-level and app-level events that affect this screen. This is distinct from `FLOW` (
which handles user events) and `STATES` (which declares states). LIFECYCLE events drive state transitions and data
refreshes that are not user-initiated.

```ssdl
LIFECYCLE {
  on screen.view do onScreenView()
  on screen.first_view do onFirstView()
  on screen.disappear do onScreenDisappear()
  on screen.destroy do onScreenDestroy()
  on app.foreground do onAppForeground()
  on app.background do onAppBackground()
}
```

### 32.1 Lifecycle event vocabulary

| Event               | When it fires                                                                                |
|---------------------|----------------------------------------------------------------------------------------------|
| `screen.view`       | Every time the screen becomes visible — initial push AND return from a child screen or modal |
| `screen.first_view` | Only on the first presentation of this screen instance                                       |
| `screen.disappear`  | When another screen covers this one (not on destruction)                                     |
| `screen.destroy`    | When the screen is popped from the stack and cleaned up                                      |
| `app.foreground`    | When the app returns from background while this screen is active                             |
| `app.background`    | When the app moves to background while this screen is active                                 |

### 32.2 Common patterns

```ssdl
LIFECYCLE {
  // Refresh data when returning from a child screen
  on screen.view do refreshIfStale()

  // Only run analytics on first view
  on screen.first_view do {
    emit profile_viewed { source: $entry_source }
  }

  // Pause media/timers when covered
  on screen.disappear do pauseAutoplay()

  // Resume and check for external changes after app restore
  on app.foreground do checkForExternalUpdates()

  // Release resources proactively
  on app.background do releaseCameraIfActive()
}
```

### 32.3 Lifecycle error handling

All `LIFECYCLE` handlers that perform async work must specify failure behavior, either inline or via `ACTIONS`.

```ssdl
LIFECYCLE {
  on screen.view do refreshData()
}

ACTIONS {
  refreshData() {
    set @refreshing
    response = await DataAPI.get()

    match response.status:
      200 => set @loaded
      else => set @error   // Do not set @error on app.foreground — show toast instead
  }
}
```

---

## 33. ANIMATION section

Use `ANIMATION` to express motion intent for screen transitions and component enter/exit animations. This section
enables `reduced_motion` alternatives to be specified alongside each animation.

```ssdl
ANIMATION {
  screen {
    enter: slide_from_right(md)
    exit: slide_to_left(md)
    reduced_motion: instant
  }

  #error_banner {
    enter: slide_down(sm)
    exit: fade_out(xs)
    reduced_motion: instant
  }

  #skeleton {
    loop: shimmer
    reduced_motion: none
  }

  #success_icon {
    enter: scale_in(sm) then bounce(xs)
    reduced_motion: fade_in(xs)
  }
}
```

### 33.1 Animation tokens

**Enter/exit animations:**

```txt
fade_in(speed)
fade_out(speed)
slide_up(speed)
slide_down(speed)
slide_from_left(speed)
slide_from_right(speed)
slide_to_left(speed)
slide_to_right(speed)
scale_in(speed)
scale_out(speed)
bounce(speed)
shake(speed)          // For validation errors
instant               // No animation
none                  // Element does not animate
```

**Loop animations (for persistent states like loading):**

```txt
shimmer               // Skeleton loading effect
pulse                 // Pulsing opacity
spin                  // Continuous rotation (spinners)
```

**Speed tokens:**

| Token | Approximate duration |
|-------|----------------------|
| `xs`  | ~100ms               |
| `sm`  | ~200ms               |
| `md`  | ~300ms               |
| `lg`  | ~500ms               |
| `xl`  | ~700ms               |

**Easing (optional second parameter):**

```txt
fade_in(sm, ease_out)
slide_up(md, spring)
scale_in(sm, ease_in_out)
```

| Easing token  | Meaning                                                            |
|---------------|--------------------------------------------------------------------|
| `ease_in`     | Starts slow, ends fast — use for exits                             |
| `ease_out`    | Starts fast, ends slow — use for entrances                         |
| `ease_in_out` | Slow start and end — use for transitions between two stable states |
| `spring`      | Physics-based overshoot — native feel on iOS/Android               |
| `linear`      | Constant speed — use for loaders and progress indicators           |

When omitted, easing defaults to `ease_out` for enter animations and `ease_in` for exit animations.

**Chaining animations with `then`:**

Use `then` to sequence animations on the same component.

```ssdl
#success_icon {
  enter: scale_in(sm, spring) then bounce(xs)
  reduced_motion: fade_in(xs)
}
```

Each step in a `then` chain completes before the next begins. Reduced motion applies to the entire chain — specify a
single reduced-motion alternative for the full sequence.

### 33.2 Shared element transitions

```ssdl
ANIMATION {
  #product_image {
    transition: shared(product_image_hero)
  }
}
```

The string in `shared(...)` is the shared element key that the destination screen must also declare.

### 33.3 Reduced motion rule

`reduced_motion` is required on every animation that conveys meaning (entrance, exit, error shake). Use `instant` when
the animation is for delight only and absence doesn't hurt comprehension. Use the reduced-motion alternative when the
animation communicates state change (e.g., sliding in an error banner).

---

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

## 35. Business rules section

Use `BUSINESS_RULES` for product or domain behavior that is not just UI validation. See §31.3 for the authority chain
between `BUSINESS_RULES`, `FLOW`, and `ACTIONS`.

```ssdl
BUSINESS_RULES {
  BR-01: when $form_valid == false => disable #login_btn

  BR-02: when LoginAPI.login returns 401 =>
    $error_msg := copy.login.error.invalid_credentials

  BR-03: when login succeeds && $redirect_to.exists =>
    nav $redirect_to

  BR-04: when login succeeds && $redirect_to.empty =>
    nav Home
}
```

Good business rules are:

- deterministic,
- testable,
- tied to a business outcome,
- independent of visual styling where possible.

---

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

## 38. API section

Use `API` to describe backend requests and responses used by the screen.

```ssdl
API {
  LoginAPI.login {
    request: POST /auth/login
    auth: none

    body: {
      email: String
      password: String
    }

    success 200: {
      token: Token
      refresh_token: Token
      user_id: ID
      expires_at: DateTime
    }

    errors: {
      400: invalid_request
      401: invalid_credentials
      423: account_locked
      429: rate_limited
      500: server_error
    }

    timeout_ms: 10000
    retry: none
    cache: none
  }
}
```

Recommended fields:

| Field        | Meaning                                                       |
|--------------|---------------------------------------------------------------|
| `request`    | HTTP method and endpoint                                      |
| `auth`       | Token/session requirement: `bearer`, `api_key`, `none`        |
| `params`     | Path/query params                                             |
| `headers`    | Required headers                                              |
| `body`       | Request body                                                  |
| `success`    | Success response shape                                        |
| `errors`     | Known error statuses                                          |
| `timeout_ms` | Client timeout                                                |
| `retry`      | Retry behavior: `none`, `once`, `exponential backoff max:<n>` |
| `cache`      | Cache strategy (see §15.1)                                    |

### 38.1 Required ERRORS coverage

Every status code listed in `API.errors` must have a corresponding entry in the `ERRORS` section or be explicitly marked
as handled globally:

```ssdl
errors: {
  400: invalid_request      // handled: globally by HTTP interceptor
  401: invalid_credentials  // handled: ERR-401
  500: server_error         // handled: ERR-500
}
```

Inline `// handled:` comments satisfy LINT-006 when a global handler covers the case.

---

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

## 40. ANALYTICS section

Use `ANALYTICS` to specify product tracking. Include a `privacy` block to declare data handling rules.

```ssdl
ANALYTICS {
  login_viewed {
    trigger: screen.first_view   // use screen.first_view to fire once per session; screen.view fires on every re-navigation to the screen
    props: {
      source: $entry_source
    }
  }

  login_submitted {
    trigger: tap #login_btn
    dedup: none                  // allow multiple fires; user may retry after an error
    props: {
      source: $entry_source
      email_present: $email.exists
    }
  }

  login_failed {
    trigger: LoginAPI.login.failure
    dedup: none
    props: {
      error_code: response.status
    }
  }

  privacy {
    never_send: [$password, auth_token, refresh_token]
    email: hash_only
    user_id: allowed_after_auth
    consent: required_before_fire  // do not fire any event until user has accepted analytics consent
  }
}
```

**Event fields:**

| Field     | Meaning                       | Default      |
|-----------|-------------------------------|--------------|
| `trigger` | What causes the event to fire | — (required) |
| `props`   | Event properties              | `{}`         |
| `dedup`   | Deduplication strategy        | `session`    |

**`dedup` values:**

| Value             | Meaning                                                                     |
|-------------------|-----------------------------------------------------------------------------|
| `session`         | Fire at most once per app session (default for screen-view events)          |
| `screen_instance` | Fire at most once per screen push (re-entering the screen resets the guard) |
| `none`            | No deduplication — fire every time the trigger occurs                       |

**`privacy.consent` values:**

| Value                       | Meaning                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------|
| `required_before_fire`      | No events fire until the user has accepted analytics consent                      |
| `anonymized_before_consent` | Events fire without user-identifying props until consent is granted               |
| `not_required`              | Screen does not collect personally identifiable data; consent check is not needed |

Rules:

- Do not send passwords, raw tokens, secrets, or sensitive personal data.
- If emails or phone numbers are needed, specify hashing or redaction in the `privacy` block.
- Every critical CTA should have an analytics decision: tracked, intentionally not tracked, or inherited from global
  tracking.
- The `privacy` block is mandatory when the screen processes authentication, payment, or personal data.
- The `privacy.consent` field is mandatory when the screen is subject to GDPR, CCPA, or equivalent consent requirements.

---

## 41. A11Y section

Use `A11Y` for accessibility requirements.

```ssdl
A11Y {
  screen_title: "Log In"

  focus_order: [
    #email_input,
    #password_input,
    #forgot_link,
    #login_btn,
    #signup_link
  ]

  screen_reader {
    #email_input: "Email address, required"
    #password_input: "Password, required, secure text field"
    #login_btn: "Log In button"
    #error_banner: announce_when_visible
  }

  touch_targets: >=44pt
  dynamic_type: supported up_to 200%
  contrast: wcag_aa
  reduced_motion: no_required_motion

  keyboard {
    email_return: next #password_input
    password_return: submitLogin when $can_submit
  }
}
```

Recommended accessibility topics:

| Topic              | What to specify                                    |
|--------------------|----------------------------------------------------|
| Screen title       | What screen reader announces on entry              |
| Focus order        | Logical order of interactive elements              |
| Labels             | Screen-reader labels for inputs/actions            |
| Error announcement | Whether errors are announced when shown            |
| Touch targets      | Minimum interactive area                           |
| Dynamic type       | Text scaling support                               |
| Contrast           | `wcag_aa` (4.5:1) or `wcag_aaa` (7:1)              |
| Keyboard behavior  | Return key and focus movement                      |
| Reduced motion     | Behavior when animations are disabled              |
| Roles              | Semantic role overrides for non-obvious components |

### 41.1 Semantic roles

Each component type has a default inferred role (e.g., `Btn` → `button`, `Txt` → `text`, `Input` → `textfield`, `List` →
`list`). Use the `roles:` block only to override the inferred role when a component is used in a non-standard semantic
context.

```ssdl
A11Y {
  roles {
    #plan_card: listitem           // Card used as a list item inside a selection list
    #section_title: heading(2)     // Txt used as a heading — level in parentheses
    #error_banner: alert           // Banner that should interrupt screen reader flow
    #loading_overlay: none         // Overlay should be invisible to accessibility tree
  }
}
```

**Common role values:**

```txt
button
link
heading(1-6)
text
textfield
image
list
listitem
alert          // Announces immediately when visible
status         // Announces politely (lower priority than alert)
dialog
none           // Remove from accessibility tree entirely (decorative elements)
```

Roles map to `accessibilityRole` (React Native), `UIAccessibilityTraits` (iOS), and `android:accessibilityDelegate` (
Android). `heading(n)` maps to heading level where supported.

---

## 42. ERRORS section

Use `ERRORS` for expected failures and recovery. Every error status code declared in `API.errors` must have a
corresponding entry here or an inline `// handled:` annotation in the API section (§38.1).

```ssdl
ERRORS {
  ERR-401 {
    when: LoginAPI.login returns 401
    ui: show #error_banner with copy.login.error.invalid_credentials
    recovery: user edits credentials and retries
  }

  ERR-423 {
    when: LoginAPI.login returns 423
    ui: show #error_banner with copy.login.error.account_locked
    recovery: user contacts support
  }

  ERR-NETWORK {
    when: network unavailable
    ui: show #error_banner with copy.common.error.network
    recovery: retry after network returns
  }

  ERR-500 {
    when: LoginAPI.login returns 5xx
    ui: show #error_banner with copy.common.error.generic
    recovery: user retries; auto-retry not applied (auth context)
  }
}
```

Recommended error categories:

```txt
validation       // Client-side field or form validation failure
network          // No network connectivity
server           // 5xx response from server
permission       // OS permission denied (camera, location, etc.)
authentication   // 401 — user is not authenticated
authorization    // 403 — user lacks the required role or permission
rate_limit       // 429 — too many requests
timeout          // Request exceeded timeout_ms threshold
conflict         // 409 — state conflict (optimistic update failure, duplicate, etc.)
not_found        // 404 — resource does not exist
empty_data       // Successful fetch but no data to display
offline          // App is in offline mode (distinct from a network error mid-request)
unknown          // Unexpected error with no specific handler
```

---

## 43. ACCEPTANCE section

Use `ACCEPTANCE` for testable outcomes. Gherkin-style phrasing is recommended.

```ssdl
ACCEPTANCE {
  AC-01:
    Given user opens Login screen
    Then #email_input, #password_input, #login_btn, #forgot_link, and #signup_link are visible

  AC-02:
    Given $email is empty
    Then #login_btn is disabled

  AC-03:
    Given valid credentials
    When user taps #login_btn
    Then LoginAPI.login is called
    And the screen enters @loading

  AC-04:
    Given LoginAPI.login returns 401
    Then user sees "Email or password is incorrect."
    And user remains on Login screen
}
```

Recommended acceptance coverage:

- default render,
- primary happy path,
- each validation rule,
- each major business rule,
- each major error path,
- navigation paths,
- analytics events for critical actions,
- accessibility baseline.

---

## 44. OPEN_QUESTIONS section

Use this section only while the spec is not ready. Unresolved questions with `blocks: ready` prevent the spec from being
marked `status: ready`.

```ssdl
OPEN_QUESTIONS {
  Q-01 {
    question: Should invalid credentials show a global banner or field-level error?
    owner: @pm-alice
    blocks: ready
    status: open
  }

  Q-02 {
    question: What is the retry count before account lockout triggers?
    owner: @be-team
    blocks: ERRORS
    status: pending_backend
  }
}
```

### 44.1 Question fields

| Field      | Meaning                                                                       | Required |
|------------|-------------------------------------------------------------------------------|----------|
| `question` | The unresolved question                                                       | Yes      |
| `owner`    | Who is responsible for resolving it                                           | Yes      |
| `blocks`   | What the question blocks: `ready`, a section name, or a specific AC/BR/VAL ID | Yes      |
| `status`   | Current status                                                                | Yes      |

### 44.2 Status values

```txt
open               // Active, needs decision
pending_backend    // Waiting on another team (engineering, backend, data)
pending_design     // Waiting on design decision
resolved           // Decided; update spec text, then remove this entry
wont_resolve       // Intentionally deferred to a later version
```

A `ready` spec must have no questions with `status: open` or `status: pending_*`.

---

## 45. Import and Include

SSDL supports importing named items from shared fragment files and inlining shared section content. This eliminates
duplication of common components, copy, error handlers, API contracts, and accessibility standards across many screen
specs.

---

### 45.1 Import declarations

`import` declarations appear immediately after the `SCREEN` declaration and before any sections. They load named
definitions from a fragment file into the importing screen's namespace.

```ssdl
SCREEN OrderDetail v1

// Named imports — specific items
import { #app_nav, #app_tab_bar } from "@shared/navigation.ssdl" at v2
import { copy.common, copy.errors } from "@shared/copy.ssdl" at v1
import { ERR-NETWORK, ERR-TIMEOUT, ERR-500 } from "@shared/errors.ssdl" at v1
import { LoginAPI } from "@shared/apis/auth.ssdl" at v1
import { handleNetworkError, retryWithBackoff } from "@shared/actions.ssdl" at v1
import { VAL-email, VAL-phone } from "@shared/validators.ssdl" at v1

META { ... }
```

**Import syntax forms:**

```ssdl
// Named import — one or more specific items
import { ItemA, ItemB } from "path/to/fragment.ssdl"

// Named import with version pin
import { ItemA } from "path/to/fragment.ssdl" at v2

// Named import with alias — rename on import
import { ItemA } as MyAlias from "path/to/fragment.ssdl" at v1

// Namespace import — all items under a COPY prefix
import copy.common from "@shared/copy.ssdl" at v1
import copy.errors from "@shared/copy.ssdl" at v1

// Multi-alias import
import { LoginAPI } as Auth, { LogoutAPI } as Deauth from "@shared/apis/auth.ssdl" at v1
```

**Braced and unbraced COPY imports are equivalent.** The braced form `import { copy.common, copy.errors } from "..."`
and the unbraced form `import copy.common from "..."` both import COPY namespaces and produce the same result. The
unbraced form is shorthand for a single namespace; use the braced form to import multiple namespaces from the same
fragment, or to mix COPY namespaces with non-COPY items in one statement.

---

### 45.2 What can be imported

| Importable from fragment | Examples                                    |
|--------------------------|---------------------------------------------|
| UI component definitions | `#app_nav`, `#app_tab_bar`, `#product_card` |
| COPY namespaces or keys  | `copy.common`, `copy.common.error.network`  |
| API contracts            | `LoginAPI`, `OrdersAPI`                     |
| ERRORS entries           | `ERR-NETWORK`, `ERR-TIMEOUT`, `ERR-500`     |
| ACTIONS functions        | `handleNetworkError`, `retryWithBackoff`    |
| VALIDATION rules         | `VAL-email`, `VAL-phone`                    |
| MODEL field sets         | `$auth_fields`, `$pagination_fields`        |

**Not importable** (too screen-specific): `SCREEN`, `META`, `STATES`, `STATE_TRANSITIONS`, `FLOW`, `LIFECYCLE`,
`ACCEPTANCE`, `PURPOSE`, `SCOPE`.

---

### 45.3 Path resolution

SSDL supports two path forms:

**Relative paths** — always valid, no tooling required:

```ssdl
import { #app_nav } from "../shared/navigation.ssdl"
import { copy.common } from "./copy/common.ssdl"
```

**`@alias` paths** — project-root shorthand configured in `ssdl.config.json`:

```ssdl
import { #app_nav } from "@shared/navigation.ssdl"
import { copy.common } from "@copy/common.ssdl"
```

**`ssdl.config.json`** — place at the project root (alongside your `.specs/` directory):

```json
{
  "version": "1",
  "aliases": {
    "@shared": "./specs/shared",
    "@copy": "./specs/shared/copy",
    "@standards": "./specs/standards",
    "@apis": "./specs/shared/apis"
  }
}
```

If no `ssdl.config.json` exists, `@` aliases are treated as unresolvable (LINT-048 error).

---

### 45.4 Version pinning

Append `at v<n>` to pin the import to a declared fragment version:

```ssdl
import { copy.common } from "@shared/copy.ssdl" at v2
```

**Rules:**

- Version must match a version declared in the fragment's `FRAGMENT_META.changelog`.
- When the fragment releases a new version, importing screens receive a LINT warning until they update their pin or
  explicitly re-confirm the current pin.
- Omitting `at` is allowed but triggers a LINT warning in production-ready specs (status: ready) — unpinned imports are
  a maintenance risk.

---

### 45.5 Aliasing

Use `as` to rename an imported item in the importing screen's namespace:

```ssdl
// Avoid a name collision
import { ERR-NETWORK } as ERR-NET from "@shared/errors.ssdl" at v1

// Use a generic API under a screen-specific name
import { GenericAuthAPI } as LoginAPI from "@shared/apis.ssdl" at v1
```

Aliased names must not conflict with other local or imported names (LINT-049).

---

### 45.6 Conflict resolution

| Situation                              | Resolution                                                                                                                                                         |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Import vs local declaration of same ID | **Local wins.** The imported item is the fallback; the local definition overrides it. LINT-051 warns that the import is being shadowed — confirm it's intentional. |
| Two imports declaring the same ID      | **Later import wins.** LINT-049 warns on the conflict — use `as` to resolve cleanly.                                                                               |
| Import vs `include` of same key        | **Local `include` wins if it appears after;** import wins if `include` appears before. See §45.8 for ordering.                                                     |

---

### 45.7 Importing UI components — import ≠ usage

Importing a component definition does **not** place it in the screen's layout tree. After importing, you must still
reference the component explicitly in `children:` or via `in:`.

```ssdl
import { #app_nav } from "@shared/navigation.ssdl" at v2

UI {
  #screen: SafeArea {
    children: [#app_nav, #content]   // explicit reference required
  }
  // No need to re-declare #app_nav — its definition comes from the import
}
```

You may override imported component directives by re-declaring the component locally:

```ssdl
// Override just the title of the imported nav bar
#app_nav: NavBar {
  title: copy.orders.screen_title   // local override; all other directives from the import
}
```

---

### 45.8 `include` — inline section content

`include` embeds the full content of a named section from a fragment file directly into the importing screen's
corresponding section. Use it for shared standards and defaults that should apply verbatim.

```ssdl
A11Y {
  include "@standards/mobile_a11y.ssdl"   // inlines touch_targets:, contrast:, reduced_motion:

  // Screen-specific additions after include
  screen_title: "Order Detail"
  focus_order: [#order_header, #items_list, #checkout_btn]
}

ANALYTICS {
  order_viewed { trigger: screen.first_view }

  privacy {
    include "@standards/gdpr_privacy.ssdl"   // inlines consent: required_before_fire, never_send: [...]
    user_id: allowed_after_auth              // screen-specific addition
  }
}

ERRORS {
  include "@shared/common_errors.ssdl"   // inlines ERR-NETWORK, ERR-TIMEOUT, ERR-500
  ERR-404 {                              // screen-specific addition
    when: OrdersAPI.get returns 404
    ui: show #load_error with type: not_found
    recovery: user navigates back
  }
}
```

**Ordering rule:** declarations that appear **after** `include` override included values. Declarations that appear *
*before** `include` are overridden by it. When in doubt, place `include` first and local overrides after.

```ssdl
A11Y {
  contrast: wcag_aaa                    // declared BEFORE include — will be overridden
  include "@standards/mobile_a11y.ssdl" // declares contrast: wcag_aa — wins over the above
  screen_title: "Orders"                // declared AFTER include — local value wins
}
```

LINT-052 warns when a pre-include declaration is silently overridden.

---

### 45.9 Transitive dependencies

When a fragment imports from another fragment, those transitive imports are **resolved automatically** (so no
missing-dependency errors), but they are **not visible** in the importing screen unless explicitly re-imported.

```
Screen A
  imports #app_nav from fragment/nav.ssdl
    fragment/nav.ssdl imports #back_btn from fragment/buttons.ssdl

// Screen A can use #app_nav (direct import)
// Screen A CANNOT use #back_btn directly — it must add its own import if needed
```

---

### 45.10 Importable MODEL field sets

A fragment may export a named set of MODEL fields that a screen can import as a group:

```ssdl
// In @shared/model_fragments.ssdl
export $auth_fields := {
  $is_authenticated: Boolean := false
  $auth_token?: Token
  $user_id?: ID
}

// In a screen
import { $auth_fields } from "@shared/model_fragments.ssdl" at v1

MODEL {
  use $auth_fields             // expands all fields from the set into this MODEL
  $email!: Email := ""         // screen-specific additions
}
```

The `use` keyword inside `MODEL` expands an imported field set in-place.

---

## 46. Fragment file format

Fragment files contain shared, reusable SSDL definitions. They are not screen specs — they have no `SCREEN` declaration,
no `META`, no `ACCEPTANCE`. They are identified by a `FRAGMENT` header.

**File naming convention:**

```txt
<category>.<name>.fragment.ssdl
```

Examples:

```txt
shared.navigation.fragment.ssdl
shared.copy.common.fragment.ssdl
shared.errors.common.fragment.ssdl
standards.mobile_a11y.fragment.ssdl
apis.auth.fragment.ssdl
```

---

### 46.1 Fragment header

Every fragment file starts with a `FRAGMENT` declaration and a `FRAGMENT_META` block:

```ssdl
FRAGMENT navigation v2

FRAGMENT_META {
  owner: Platform/Design System Team
  last_updated: 2026-06-09
  changelog: {
    v2: "Add #app_tab_bar; rename #legacy_nav → #app_nav"
    v1: "Initial shared navigation components"
  }
}
```

The `FRAGMENT` version is what importing screens reference with `at v<n>`.

---

### 46.2 Allowed sections in a fragment

| Allowed                      | Not allowed                    |
|------------------------------|--------------------------------|
| `UI` (component definitions) | `SCREEN`                       |
| `COPY`                       | `META`                         |
| `API`                        | `STATES` / `STATE_TRANSITIONS` |
| `ERRORS`                     | `FLOW`                         |
| `ACTIONS`                    | `LIFECYCLE`                    |
| `VALIDATION`                 | `ACCEPTANCE`                   |
| `MODEL` (field set exports)  | `PURPOSE` / `SCOPE`            |
| `A11Y` (standards blocks)    | `ROUTE` / `NAVIGATION`         |
| `ANALYTICS` (privacy blocks) | `FEATURE_FLAGS`                |

---

### 46.3 Export declarations

By default, everything in a fragment is importable. To restrict the public surface, add explicit `export` declarations —
once any `export` appears, only exported items are importable.

```ssdl
FRAGMENT navigation v2

FRAGMENT_META { ... }

export #app_nav
export #app_tab_bar
// #nav_back_btn is private — used internally, not importable by consuming screens

UI {
  #app_nav: NavBar { ... }
  #app_tab_bar: TabBar { ... }
  #nav_back_btn: IconBtn { ... }   // internal helper
}
```

LINT-050: importing a non-exported item from a fragment with explicit exports is an error.

---

### 46.4 Re-export (barrel fragments)

A fragment may re-export items from other fragments to create a single import point for a design system:

```ssdl
FRAGMENT design_system v3

FRAGMENT_META {
  owner: Platform Team
  changelog: { v3: "Add copy.errors namespace", v2: "...", v1: "..." }
}

import { #app_nav, #app_tab_bar } from "./navigation.fragment.ssdl" at v2
import { copy.common, copy.errors } from "./copy.fragment.ssdl" at v1
import { ERR-NETWORK, ERR-TIMEOUT, ERR-500 } from "./errors.fragment.ssdl" at v1

// Re-export everything for consumers
export #app_nav
export #app_tab_bar
export copy.common
export copy.errors
export ERR-NETWORK
export ERR-TIMEOUT
export ERR-500
```

Consuming screens then import from one place:

```ssdl
import { #app_nav, copy.common, ERR-NETWORK } from "@shared/design_system.ssdl" at v3
```

---

### 46.5 Fragments importing fragments

Fragments may import from other fragments using the same syntax as screens. The same transitive dependency and circular
import rules apply — the full import graph across all fragment and screen files must be acyclic (LINT-047).

---

### 46.6 Fragment file example

```ssdl
FRAGMENT common_errors v1

FRAGMENT_META {
  owner: Platform/API Team
  last_updated: 2026-06-09
  changelog: {
    v1: "Initial common error handlers — network, timeout, server"
  }
}

export ERR-NETWORK
export ERR-TIMEOUT
export ERR-500

ERRORS {
  ERR-NETWORK {
    when: network unavailable
    ui: show #error_banner with copy.common.error.network
    recovery: retry after network returns
  }

  ERR-TIMEOUT {
    when: request exceeded timeout_ms threshold
    ui: show #error_banner with copy.common.error.generic
    recovery: user retries
  }

  ERR-500 {
    when: API returns 5xx
    ui: show #error_banner with copy.common.error.generic
    recovery: user retries; do not auto-retry in auth context
  }
}
```

---

## 47. Screen variants and inheritance

Use `extends` to create a variant that inherits all sections from a base screen and applies targeted overrides. This
avoids full duplication when screens differ by 10–30%.

```ssdl
SCREEN CheckoutPaymentGuest v1 extends CheckoutPayment v2

OVERRIDE {
  META {
    feature: Checkout/Guest
    owner: Commerce Team
  }

  SCOPE {
    out: + "Saved card selection"
  }

  MODEL {
    remove: $saved_card_id
    $guest_email!: Email := ""
  }

  UI {
    remove: #saved_cards_section
    add: #guest_info_section
  }

  VALIDATION {
    add: VAL-10: $guest_email.empty => "Email is required for guest checkout"
  }

  COPY {
    checkout.title: "Guest Checkout"
  }
}
```

### 47.1 OVERRIDE directives

| Directive  | Meaning                                         |
|------------|-------------------------------------------------|
| `add:`     | Add a new item to a list or block               |
| `remove:`  | Remove an item by ID                            |
| `replace:` | Replace an item by ID with a new definition     |
| `+ "text"` | Append a list item (in `SCOPE.out`, `SCOPE.in`) |

### 47.2 Inheritance rules

- All sections from the base screen are inherited unless overridden.
- `SCREEN` name and version are always replaced; do not carry over from base.
- `META.status` defaults to `draft` in the variant; must be set explicitly.
- `ACCEPTANCE` criteria are inherited but should be reviewed; add variant-specific criteria with `add:`.
- Linting applies to the resolved (merged) spec, not just the `OVERRIDE` block.

---

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

## 49. Default mobile screen layout pattern

Most mobile screens can start with this structure.

```ssdl
UI {
  #screen: SafeArea {
    size: w:screen h:screen
    behavior: safe_area_aware
    children: [#content, #footer, #overlay]
  }

  #content: Scroll {
    in: #screen
    pos: safe.top
    size: w:fill h:fill
    pad: lg
    behavior: [scroll_when_keyboard_open, dismiss_keyboard_on_scroll]
    children: [#header, #body]
  }

  #header: VStack {
    in: #content
    pos: top.center
    align: center
    gap: sm
  }

  #body: VStack {
    in: #content
    pos: below(#header, lg)
    align: stretch
    gap: md
  }

  #footer: Footer {
    in: #screen
    pos: sticky(bottom.safe)
    size: w:fill h:hug
    pad: md
    behavior: avoid_keyboard
  }

  #overlay: Overlay {
    in: #screen
    layer: z:overlay
    visible_when: @loading or @modal
  }
}
```

---

## 50. Full example: Login screen

A complete, production-grade Login screen example is maintained in [`assets/sample.login.ssdl`](assets/sample.login.ssdl).
It demonstrates every major SSDL section (§7–§44) applied to a real screen, including feature flags,
route params, model with derived fields, UI layout, states and state transitions, lifecycle handlers,
validation (sync, cross-field, and async), business rules, pseudocode actions, flow, API contracts,
navigation with replace-stack, analytics with privacy, accessibility with focus order and screen reader
labels, errors, and acceptance criteria.

---

## 51. UI directive vocabulary reference

Layout and motion vocabulary (positions, sizes, alignment, spacing, layers, behaviors, animation) is defined — with
semantics and examples — in the body (§22–§27, §33); the subsections below for those families are pointers, not
independent definitions. The remaining subsections (§51.7 onward) are the authoritative catalog of component value
enums referenced from §17, §19, and §29. When a token here differs from the body, **the body governs.**

### 51.1 Positions

Anchor, relative (`below(#id)`, `right_of(#id)`…), inside/overlay, sticky, and floating positions — defined with
semantics and examples in **§22**.

### 51.2 Sizes

Base size tokens (`xxs`–`xxl`), width/height hints (`w:fill`, `h:hug`…), and relative sizing (`same_w(#id)`,
`smaller(#id, n)`…) — defined in **§24**.

### 51.3 Alignment

Simple, axis (`main:`/`cross:`), and reference alignment (`align_to(#id.left)`, `baseline_of(#id)`) — defined in **§23**.

### 51.4 Spacing

Spacing tokens (`none`, `xxs`–`xxl`) and directional `pad:`/`margin:`/`inset:` forms — defined in **§25**.

### 51.5 Layers

Layer and z-order tokens (`above(#id)`, `below(#id)`, `z:0`–`z:toast`) — defined in **§26**.

### 51.6 Behaviors

Runtime layout behaviors (`safe_area_aware`, `avoid_keyboard`, `stack_on_small_screen`…) — defined in **§27**.

### 51.7 Style tokens (typography)

Use `style:` on text-bearing components to indicate typographic intent. Exact rendering is determined by the design
system.

```txt
display_xl
display_lg
heading_xl
heading_lg
heading_md
heading_sm
body_lg
body_md
body_sm
label_lg
label_md
label_sm
caption
overline
code
link
```

### 51.8 Keyboard types

Use `keyboard:` on Input, TextArea, and Search components.

```txt
text           // Default text keyboard
email          // Email-optimized (@ and . keys prominent)
number         // Numeric only
decimal        // Decimal number (includes period/comma)
phone          // Phone keypad (digits, *, #)
url            // URL keyboard (/ and . keys prominent)
search         // Search keyboard (Search/Go action key)
ascii          // ASCII-only (iOS)
```

Note: `password` keyboard type is handled by the `Pwd` component; do not set `keyboard:` on `Pwd`.

### 51.9 Autocomplete types

Use `autocomplete:` on Input, Pwd, and Search components to hint the OS credential/autofill system.

```txt
email
password
new_password      // New password field — suppresses autofill, encourages strong suggestion
current_password  // Existing password field — triggers credential autofill
name
given_name
family_name
username
phone
address
postal_code
country
cc_number         // Credit card number
cc_exp            // Credit card expiry
cc_cvc            // Credit card CVC
one_time_code     // SMS OTP
off               // Explicitly disable autocomplete
```

### 51.10 Animation tokens

Enter/exit, loop, speed, and easing animation tokens are defined in **§33.1**; `transition: shared(<key>)` for
shared-element transitions is covered in **§33.2**.

### 51.11 Map zoom levels

```txt
street           // Individual buildings visible
neighborhood     // Blocks and streets
city             // City overview
region           // State/county level
country          // Country overview
```

### 51.12 Scanner formats

```txt
qr               // QR code
code128          // Code 128 barcode
ean13            // EAN-13 / UPC barcode
pdf417           // PDF417 stacked barcode (boarding passes, IDs)
data_matrix      // Data Matrix
aztec            // Aztec code
all              // Attempt all supported formats
```

### 51.13 Status values

```txt
online
offline
busy
away
do_not_disturb
custom           // Use color: to specify
```

### 51.14 Drawer sides

```txt
left
right
```

### 51.15 Popover placement

```txt
top
bottom
left
right
auto             // Platform picks the best placement based on available space
```

### 51.16 Step indicator styles

```txt
dots             // Filled/unfilled circles
numbers          // Numbered circles
bars             // Segmented horizontal bars
progress_bar     // Single linear bar showing completion fraction
```

### 51.17 Color picker modes

```txt
hex              // Single hex input
rgb              // Red/green/blue sliders
hsl              // Hue/saturation/lightness sliders
hsb              // Hue/saturation/brightness sliders
palette          // Fixed set of swatches from palette:
```

### 51.18 Tag styles

```txt
filled           // Solid background color (default)
outline          // Border only, transparent background
ghost            // No border, muted background
tonal            // Lightly tinted background matching the color token
```

### 51.19 Rating styles

```txt
star             // Five-star rating (default)
heart            // Heart icons
thumb            // Thumbs up/down binary
```

### 51.20 Table column definition

A column definition inside `columns:`:

```ssdl
{ id: col_id, header: "Display Name", width: SizeToken, sortable: true, frozen: false }
```

| Field      | Meaning                                           |
|------------|---------------------------------------------------|
| `id`       | Unique column key — used in `on sort:` payload    |
| `header`   | Visible column heading                            |
| `width`    | Size token or `fill` for remaining space          |
| `sortable` | Boolean — column header tappable for sort         |
| `frozen`   | Boolean — column stays fixed on horizontal scroll |

### 51.21 Progress styles

```txt
linear           // Horizontal track bar
circular         // Ring or donut
```

### 51.22 Aspect ratio tokens

```txt
square           // 1:1
wide             // 16:9
portrait         // 3:4
tall             // 9:16
auto             // Natural content size
```

### 51.23 QR error correction levels

```txt
L    // ~7% data recovery
M    // ~15% data recovery (default)
Q    // ~25% data recovery
H    // ~30% data recovery — use when QR may be partially obscured
```

### 51.24 Trend directions

Used by `Stat` component (`trend:` directive).

```txt
up               // Value increased positively
down             // Value decreased (may be positive or negative depending on metric)
neutral          // No significant change
```

### 51.25 Selection modes

Used by `ToggleGroup` (`selection:`) and `Table` (`selection:`).

```txt
none             // No selection
single           // One item active at a time
multi            // Multiple items may be active simultaneously
```

### 51.26 Orientation

Used by `Carousel` (`orientation:`).

```txt
horizontal       // Swipe left/right (default)
vertical         // Swipe up/down
```

### 51.27 Location result types

Used by `LocationInput` (`result_types:`).

```txt
address          // Street-level addresses
city             // Cities and towns
region           // States, counties, provinces
establishment    // Named places — restaurants, shops, landmarks
all              // All result types (default)
```

### 51.28 EmptyState types

Used by `EmptyState` (`type:` directive). Drives default illustration and heading style in the design system.

```txt
empty            // No data yet — "Nothing here yet" (default)
error            // Load or operation failed — "Something went wrong"
offline          // No network — "You're offline"
no_results       // Search or filter returned nothing — "No results found"
permission_denied // Required permission was denied — "Access needed"
custom           // Custom — pair with an explicit illustration: and title:
```

---

## 52. Ambiguity and conflict-resolution rules

Use these rules when the spec contains overlapping directives.

| Situation                                                                       | Resolution                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `in:` parent conflicts with parent `children` list                              | The explicit `in:` value wins; update the parent `children` list during review.                                                                                                                                                        |
| Component has no `in:`                                                          | It is assumed to be a root child of `#screen` only if it appears in `#screen.children`; otherwise it is invalid.                                                                                                                       |
| `visible_when` and `hidden_when` both present                                   | `hidden_when` wins if both evaluate true; prefer using only one.                                                                                                                                                                       |
| General `size` and axis-specific `w:`/`h:` conflict                             | Axis-specific values win.                                                                                                                                                                                                              |
| `pos` conflicts with container ordering                                         | Container child order wins for stack/list containers; `pos` is treated as hint.                                                                                                                                                        |
| `enabled_when` conflicts with `@loading` state                                  | Loading disables interactive controls unless explicitly overridden.                                                                                                                                                                    |
| `COPY` key missing                                                              | Treat as a spec error before engineering handoff.                                                                                                                                                                                      |
| UI event and FLOW both define same action                                       | They should match. If they differ, `FLOW` is canonical for behavior; UI event is a convenience annotation.                                                                                                                             |
| API error listed but no UI error behavior                                       | Add an `ERRORS` entry or mark as `// handled: globally` in the API errors block.                                                                                                                                                       |
| Analytics event references sensitive data                                       | Remove, hash, or redact it before approval.                                                                                                                                                                                            |
| `visible_when` and `FEATURE_FLAGS` both control the same component's visibility | `FEATURE_FLAGS` governs flag-gated components; do not duplicate the flag check in `visible_when`.                                                                                                                                      |
| `animate:` and `reduced_motion: instant` (from A11Y or ANIMATION)               | `reduced_motion` always wins; `animate:` is the intended motion, `reduced_motion` is the accessible fallback.                                                                                                                          |
| `STATES` and `STATE_TRANSITIONS` conflict                                       | `STATE_TRANSITIONS` is canonical; update `STATES` to match.                                                                                                                                                                            |
| Same guard encoded in both `BUSINESS_RULES` and `ACTIONS`                       | `ACTIONS` is authoritative for execution; `BUSINESS_RULES` documents intent. Remove the guard from whichever section it fits less naturally.                                                                                           |
| `pos: below(#anchor)` where `#anchor` has `visible_when` or `hidden_when`       | When the anchor is hidden, treat `pos` as `below(next_visible_sibling_above)`. **Preferred:** place conditional elements inside a container and rely on container ordering rather than anchoring to a conditionally visible component. |

---

## 53. Completeness checklist

Run this before marking a screen spec `ready`. The full per-section checklist is maintained in
[`assets/completeness-checklist.md`](assets/completeness-checklist.md).

---

## 54. Linting rules for automated review

The full catalogue of `LINT-xxx` rules — usable by a script, AI reviewer, or human reviewer — is maintained in
[`assets/lint-rules.md`](assets/lint-rules.md).

---

## 55. Recommended adoption workflow

1. Draft the screen in compact mode.
2. Declare `FEATURE_FLAGS` and `PERMISSIONS` before expanding the model.
3. Expand `MODEL`, `UI`, `FLOW`, and `ACTIONS`.
4. Add `STATES` (with `initial:`), `STATE_TRANSITIONS`, and `LIFECYCLE`.
5. Add `VALIDATION` (including cross-field and async rules), `BUSINESS_RULES`, `API`, `ERRORS`, and `NAVIGATION`.
6. Add `ANIMATION` with `reduced_motion` alternatives.
7. Add `ANALYTICS` (with `privacy` and `consent` blocks) and `A11Y` (including `roles`).
8. Write `ACCEPTANCE` criteria covering happy path, validations, errors, navigation, re-view behavior, and
   accessibility.
9. Run the completeness checklist (§53).
10. Resolve `OPEN_QUESTIONS` or mark remaining ones with `blocks:` and `owner:`.
11. Mark `META.status: ready`.

---

## 56. Minimal production template

A minimal, fill-in-the-blanks production template — every section in recommended order — is maintained in
[`assets/template.minimal.ssdl`](assets/template.minimal.ssdl). Copy it as the starting point for a new screen spec.

---

## 57. Spec-to-implementation traceability

SSDL assigns stable IDs to business rules (`BR-xx`), validation rules (`VAL-xx`), error cases (`ERR-xx`), and acceptance
criteria (`AC-xx`). Teams should carry these IDs into implementation to make the connection between spec and code
auditable.

### 57.1 Recommended traceability patterns

**In source code** — reference the rule ID in a comment near the implementation:

```swift
// BR-03: redirect to $redirect_to on successful login
if let redirectTo = state.redirectTo {
    navigator.replace(redirectTo)
}
```

```typescript
// VAL-02: email format validation
if (!isValidEmail(email.trim())) {
    setError('email', copy.login.error.invalid_email)
}
```

**In test files** — use the AC ID as the test name or description:

```typescript
describe('AC-07: successful login stores tokens and navigates', () => {
    it('stores auth_token and refresh_token in secure storage', ...)
    it('navigates to Home when no redirect_to param', ...)
})
```

**In PR descriptions and commit messages** — cite the rule IDs being implemented:

```
feat(login): implement BR-03 redirect-after-login and VAL-01/02 email validation
```

### 57.2 What NOT to put in implementation code

- Do not replicate spec prose in code comments — the spec is the source of truth for intent.
- Do not embed `AC-xx` IDs in production runtime code — they belong in tests and tooling only.
- Do not invent new IDs in implementation; only reference IDs that exist in the spec.

---

## 58. Closing recommendation

Use SSDL as a shared contract. Keep visual design details in your design tool, but use SSDL to make the behavior, data,
layout intent, state transitions, lifecycle, permissions, animations, edge cases, analytics, accessibility, and QA
expectations explicit.

For most production mobile screens, the best balance is:

```txt
Markdown wrapper
+ SSDL sections
+ semantic UI directives (pos, size, style, animate)
+ pseudocode actions
+ API contracts with cache strategy
+ Gherkin-style acceptance criteria
+ completeness checklist
```

---

**Version history** has moved to a dedicated [CHANGELOG.md](CHANGELOG.md).
