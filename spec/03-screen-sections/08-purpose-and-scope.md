## 8. PURPOSE and SCOPE sections

Use `PURPOSE` to explain why the screen exists. Use `SCOPE` to prevent accidental feature creep.

```ssdl
PURPOSE {
  Allow registered users to authenticate with email and password.
}

SCOPE {
  in:
    - Email/password login
    - Forgot password entry point
    - Signup entry point

  out:
    - Social login
    - Passwordless login
    - Multi-factor authentication
}
```

---

