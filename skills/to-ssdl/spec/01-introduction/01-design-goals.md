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

