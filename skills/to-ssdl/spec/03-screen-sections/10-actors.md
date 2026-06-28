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

