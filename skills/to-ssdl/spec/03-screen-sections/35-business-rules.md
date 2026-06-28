## 35. Business rules section

Use `BUSINESS_RULES` for product or domain behavior that is not just UI validation. See §31.3 for the authority chain
between `BUSINESS_RULES`, `FLOW`, and `ACTIONS`.

```ssdl
BUSINESS_RULES {
  BR-01: when $form_valid == false => disable #login_btn

  BR-02: when LoginAPI.login returns 401 =>
    $error_msg := copy.login.error.invalid_credentials

  BR-03: when login succeeds && $redirect_to.exists =>
    nav $redirect_to

  BR-04: when login succeeds && $redirect_to.empty =>
    nav Home
}
```

Good business rules are:

- deterministic,
- testable,
- tied to a business outcome,
- independent of visual styling where possible.

---

