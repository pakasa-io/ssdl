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
