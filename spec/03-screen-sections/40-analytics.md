## 40. ANALYTICS section

Use `ANALYTICS` to specify product tracking. Include a `privacy` block to declare data handling rules.

```ssdl
ANALYTICS {
  login_viewed {
    trigger: screen.first_view   // use screen.first_view to fire once per session; screen.view fires on every re-navigation to the screen
    props: {
      source: $entry_source
    }
  }

  login_submitted {
    trigger: tap #login_btn
    dedup: none                  // allow multiple fires; user may retry after an error
    props: {
      source: $entry_source
      email_present: $email.exists
    }
  }

  login_failed {
    trigger: LoginAPI.login.failure
    dedup: none
    props: {
      error_code: response.status
    }
  }

  privacy {
    never_send: [$password, auth_token, refresh_token]
    email: hash_only
    user_id: allowed_after_auth
    consent: required_before_fire  // do not fire any event until user has accepted analytics consent
  }
}
```

**Event fields:**

| Field     | Meaning                       | Default      |
|-----------|-------------------------------|--------------|
| `trigger` | What causes the event to fire | — (required) |
| `props`   | Event properties              | `{}`         |
| `dedup`   | Deduplication strategy        | `session`    |

**`dedup` values:**

| Value             | Meaning                                                                     |
|-------------------|-----------------------------------------------------------------------------|
| `session`         | Fire at most once per app session (default for screen-view events)          |
| `screen_instance` | Fire at most once per screen push (re-entering the screen resets the guard) |
| `none`            | No deduplication — fire every time the trigger occurs                       |

**`privacy.consent` values:**

| Value                       | Meaning                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------|
| `required_before_fire`      | No events fire until the user has accepted analytics consent                      |
| `anonymized_before_consent` | Events fire without user-identifying props until consent is granted               |
| `not_required`              | Screen does not collect personally identifiable data; consent check is not needed |

Rules:

- Do not send passwords, raw tokens, secrets, or sensitive personal data.
- If emails or phone numbers are needed, specify hashing or redaction in the `privacy` block.
- Every critical CTA should have an analytics decision: tracked, intentionally not tracked, or inherited from global
  tracking.
- The `privacy` block is mandatory when the screen processes authentication, payment, or personal data.
- The `privacy.consent` field is mandatory when the screen is subject to GDPR, CCPA, or equivalent consent requirements.

---

