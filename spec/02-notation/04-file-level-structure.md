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

