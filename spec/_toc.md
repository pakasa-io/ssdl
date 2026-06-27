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

