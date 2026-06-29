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

**How imports resolve.** Screens reference a fragment by a logical `@alias/<name>.ssdl` path, not by its physical
filename — `ssdl.config.json` maps the alias (e.g. `@shared`) and the logical `<name>` to the physical
`<category>.<name>.fragment.ssdl` file. So `import { … } from "@shared/navigation.ssdl"` resolves to
`shared.navigation.fragment.ssdl`, and import statements stay stable when a fragment is renamed or recategorised.

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

