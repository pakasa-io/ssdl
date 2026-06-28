## 11. ENTRY and EXIT sections

Use these sections to describe how users arrive and leave.

```ssdl
ENTRY {
  - from: AppLaunch
    when: user.authenticated == false

  - from: SessionExpired
    when: token.expired == true
}

EXIT {
  - to: Home
    when: login.success && $redirect_to.empty

  - to: ForgotPassword
    when: tap #forgot_link
}
```

Prefer `ENTRY`/`EXIT` for high-level journey mapping and `NAVIGATION` for implementation-level route transitions.

---

