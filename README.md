# SSDL — Single-Screen Specification Definition Language

> A compact, human-readable, implementation-agnostic text format for specifying a single mobile app screen — its UI, layout, state, business logic, data contracts, analytics, accessibility, and acceptance criteria — in one file.

[![Spec version](https://img.shields.io/badge/spec-v1.4.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-stable-brightgreen)](ssdl.spec.md)

---

## What is SSDL?

SSDL is a **text-first language for describing one mobile screen at a time**. A single `.ssdl` file captures *screen intent*: what the screen contains, how it behaves, what data it depends on, what rules apply, and how users move through it — in a form that product, design, engineering, QA, analytics, and AI/code-generation workflows can all read.

SSDL is **not** a replacement for design files or implementation code. It sits between them: precise enough to remove ambiguity for delivery and QA, but implementation-agnostic, so the same spec works for **iOS, Android, React Native, Flutter, SwiftUI, Jetpack Compose, or mobile web**.

Layout is expressed as **hints, not pixels** — `center`, `top.right`, `below(#title, md)`, `w:fill`, `h:hug`, `sticky(bottom.safe)` — so a spec describes structure and relationships without pretending to be a renderer.

## Why SSDL?

| Goal | What it buys you |
|------|------------------|
| **Human-readable** | A PM, designer, engineer, or QA tester understands a screen without a parser. |
| **Precise enough for delivery** | Reduces ambiguity around UI, states, business rules, and edge cases. |
| **Implementation-agnostic** | One spec drives any mobile platform or framework. |
| **AI-friendly** | Consistent structure supports generation, linting, summarization, and conversion into tickets or test cases. |
| **Flexible** | Simple screens stay short; complex screens scale to full detail. |
| **Testable** | Acceptance criteria and state transitions are explicit enough for QA. |
| **Accessible by default** | Accessibility is a first-class section, not an afterthought. |

## A quick taste

SSDL supports a **compact mode** for fast drafting and a **full mode** for engineering handoff. Here's the compact form:

```ssdl
SCREEN Login v1

MODEL {
  $email!: Email     := ""
  $password!: String := ""
  $email_valid    ==> matchesEmail(trim($email))
  $password_valid ==> length($password) >= 8
  $is_loading     ==> @loading
  $can_submit     ==> $email_valid && $password_valid && !$is_loading
}

UI {
  #email:    Input label:copy.login.email    bind:$email
  #password: Pwd   label:copy.login.password bind:$password
  #submit:   Btn "Log In" enabled:$can_submit loading:@loading on tap:submitLogin()
}

VAL
  $email.empty    => "Email is required"
  $password.empty => "Password is required"

AC
  AC-01: Given valid credentials, When user taps #submit, Then LoginAPI.login is called
```

See [`sample.login.ssdl`](sample.login.ssdl) for the same screen written out in **full mode** — every section populated, ready for handoff and QA.

## Anatomy of a spec

A complete file is a `SCREEN` declaration, optional `import` lines, then a series of sections in a recommended order:

```
SCREEN · META · PURPOSE · SCOPE · ROUTE · ACTORS · ENTRY · EXIT · PERMISSIONS
FEATURE_FLAGS · MODEL · DATA · COPY · UI · STATES · LIFECYCLE · ANIMATION
VALIDATION · VALIDATION_UI · BUSINESS_RULES · ACTIONS · FLOW · API · NAVIGATION
ANALYTICS · A11Y · ERRORS · ACCEPTANCE · OPEN_QUESTIONS
```

Only **`SCREEN`, `ROUTE`, `MODEL`, `UI`, `STATES`, `FLOW`, and `ACCEPTANCE`** are mandatory for a production screen. Everything else can be omitted on simple screens — though the production default is to include all sections, even if some are short.

## Shorthand at a glance

| Symbol | Meaning | Example |
|--------|---------|---------|
| `$field` | Screen model field | `$email`, `$password` |
| `!` / `?` | Required / optional | `$email!`, `$avatar_url?` |
| `#id` | UI component ID | `#login_btn` |
| `@state` | Screen state | `@loading` |
| `:=` | Default value / assignment | `$remember_me := false` |
| `==>` | Derived / computed field | `$can_submit ==> $form_valid && !$is_loading` |
| `=>` | Effect / result | `401 => show #error_banner` |
| `->` | Navigation / transition | `login.success -> Home` |
| `~>` | Async call / external op | `submit ~> POST /auth/login` |
| `on` / `when` / `do` | Trigger / guard / action | `on tap #submit when $can_submit do submitLogin()` |
| `BR-xx` `VAL-xx` `ERR-xx` `AC-xx` | Rule, validation, error, acceptance IDs | `AC-05`, `ERR-401` |

The full symbol table, plus the compact ↔ full alias mapping, is in [§3 of the spec](ssdl.spec.md).

## Reuse: imports & fragments

Common components, copy, error handlers, API contracts, and accessibility standards live in **fragment files** and are pulled into screens with `import` (named definitions) or `include` (inlined section content):

```ssdl
SCREEN OrderDetail v1

import { #app_nav, #app_tab_bar } from "@shared/navigation.ssdl" at v2
import { copy.common, ERR-NETWORK } from "@shared/design_system.ssdl" at v3
```

Fragments carry their own `FRAGMENT` header and changelog, support `export` to control their public surface, version pinning via `at v<n>`, and `@alias` paths configured in `ssdl.config.json`. See **§4a / §4b** of the spec.

## Repository contents

| File | What it is |
|------|------------|
| [`ssdl.spec.md`](ssdl.spec.md) | The complete SSDL v1.4.0 language specification — 55 sections covering grammar, component taxonomy, every directive, linting rules, and adoption workflow. |
| [`CHANGELOG.md`](CHANGELOG.md) | Per-version history of the SSDL specification. |
| [`lint-rules.md`](lint-rules.md) | The `LINT-xxx` automated-review rule catalogue (§51 of the spec). |
| [`completeness-checklist.md`](completeness-checklist.md) | The pre-`ready` completeness checklist (§50 of the spec). |
| [`sample.login.ssdl`](sample.login.ssdl) | A reference login screen written in full mode — the canonical worked example. |
| [`template.minimal.ssdl`](template.minimal.ssdl) | A fill-in-the-blanks minimal screen template — copy it to start a new spec. |
| [`LICENSE`](LICENSE) | MIT. |

> **Note:** This repository defines the *language* and provides a reference example. The spec describes conventions for tooling — file naming, an `ssdl.config.json` schema, and `LINT-xxx` rules — that parsers, linters, and generators are expected to implement; no such tooling ships here yet.

## File naming

```txt
screen.<feature>.<screen-name>.ssdl     # screen specs
<category>.<name>.fragment.ssdl          # shared fragments
```

Examples: `screen.auth.login.ssdl`, `screen.checkout.payment-method.ssdl`, `shared.navigation.fragment.ssdl`.

## Versioning

The spec is versioned independently of any screen. The current language version is **1.4.0** — see [CHANGELOG.md](CHANGELOG.md) for the full per-version history. Individual screens and fragments declare their own version (`SCREEN Login v1`, `FRAGMENT navigation v2`), recorded in each file's `META.changelog` / `FRAGMENT_META.changelog`.

## License

[MIT](LICENSE) © 2026 pakasa-io
