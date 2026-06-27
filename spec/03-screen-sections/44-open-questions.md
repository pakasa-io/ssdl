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

