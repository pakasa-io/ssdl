## 15. DATA section

Use `DATA` to declare where information comes from and where it is written.

```ssdl
DATA {
  source: mixed

  read:
    - route_param: redirect_to?
    - local: saved_email?
    - remote: GET /users/me
        cache: stale_while_revalidate ttl:300

  write:
    - secure_storage: auth_token
    - secure_storage: refresh_token
    - analytics: login events
}
```

Recommended source values:

```txt
local
remote
mixed
none
```

### 15.1 Cache strategies for remote reads

| Strategy                 | Meaning                                                                                                                                 |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `none`                   | Always fetch fresh; never read from cache                                                                                               |
| `network_only`           | Fetch from network; error if offline                                                                                                    |
| `cache_first`            | Return cached value immediately; refresh in background but do NOT update UI when fresh data arrives (fire-and-forget; avoids re-render) |
| `stale_while_revalidate` | Return cached value; simultaneously fetch fresh; update UI when fresh data arrives (causes re-render)                                   |
| `cache_only`             | Read from cache only; useful for offline-first screens                                                                                  |
| `ttl:<seconds>`          | Cache validity duration; combine with a strategy                                                                                        |

Use `DATA` to avoid ambiguity about whether a value comes from route params, local storage, backend response, cached
state, or user input.

---

