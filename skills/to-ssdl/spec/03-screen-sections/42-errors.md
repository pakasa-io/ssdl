## 42. ERRORS section

Use `ERRORS` for expected failures and recovery. Every error status code declared in `API.errors` must have a
corresponding entry here or an inline `// handled:` annotation in the API section (§38.1).

```ssdl
ERRORS {
  ERR-401 {
    when: LoginAPI.login returns 401
    ui: show #error_banner with copy.login.error.invalid_credentials
    recovery: user edits credentials and retries
  }

  ERR-423 {
    when: LoginAPI.login returns 423
    ui: show #error_banner with copy.login.error.account_locked
    recovery: user contacts support
  }

  ERR-NETWORK {
    when: network unavailable
    ui: show #error_banner with copy.common.error.network
    recovery: retry after network returns
  }

  ERR-500 {
    when: LoginAPI.login returns 5xx
    ui: show #error_banner with copy.common.error.generic
    recovery: user retries; auto-retry not applied (auth context)
  }
}
```

Recommended error categories:

```txt
validation       // Client-side field or form validation failure
network          // No network connectivity
server           // 5xx response from server
permission       // OS permission denied (camera, location, etc.)
authentication   // 401 — user is not authenticated
authorization    // 403 — user lacks the required role or permission
rate_limit       // 429 — too many requests
timeout          // Request exceeded timeout_ms threshold
conflict         // 409 — state conflict (optimistic update failure, duplicate, etc.)
not_found        // 404 — resource does not exist
empty_data       // Successful fetch but no data to display
offline          // App is in offline mode (distinct from a network error mid-request)
unknown          // Unexpected error with no specific handler
```

---

