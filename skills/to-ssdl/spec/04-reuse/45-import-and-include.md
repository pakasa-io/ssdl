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

