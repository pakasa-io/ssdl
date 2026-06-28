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

