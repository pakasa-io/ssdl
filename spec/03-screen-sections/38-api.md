## 38. API section

Use `API` to describe backend requests and responses used by the screen.

```ssdl
API {
  LoginAPI.login {
    request: POST /auth/login
    auth: none

    body: {
      email: String
      password: String
    }

    success 200: {
      token: Token
      refresh_token: Token
      user_id: ID
      expires_at: DateTime
    }

    errors: {
      400: invalid_request
      401: invalid_credentials
      423: account_locked
      429: rate_limited
      500: server_error
    }

    timeout_ms: 10000
    retry: none
    cache: none
  }
}
```

Recommended fields:

| Field        | Meaning                                                       |
|--------------|---------------------------------------------------------------|
| `request`    | HTTP method and endpoint                                      |
| `auth`       | Token/session requirement: `bearer`, `api_key`, `none`        |
| `params`     | Path/query params                                             |
| `headers`    | Required headers                                              |
| `body`       | Request body                                                  |
| `success`    | Success response shape                                        |
| `errors`     | Known error statuses                                          |
| `timeout_ms` | Client timeout                                                |
| `retry`      | Retry behavior: `none`, `once`, `exponential backoff max:<n>` |
| `cache`      | Cache strategy (see §15.1)                                    |

### 38.1 Required ERRORS coverage

Every status code listed in `API.errors` must have a corresponding entry in the `ERRORS` section or be explicitly marked
as handled globally:

```ssdl
errors: {
  400: invalid_request      // handled: globally by HTTP interceptor
  401: invalid_credentials  // handled: ERR-401
  500: server_error         // handled: ERR-500
}
```

Inline `// handled:` comments satisfy LINT-006 when a global handler covers the case.

---

