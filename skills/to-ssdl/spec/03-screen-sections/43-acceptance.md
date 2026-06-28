## 43. ACCEPTANCE section

Use `ACCEPTANCE` for testable outcomes. Gherkin-style phrasing is recommended.

```ssdl
ACCEPTANCE {
  AC-01:
    Given user opens Login screen
    Then #email_input, #password_input, #login_btn, #forgot_link, and #signup_link are visible

  AC-02:
    Given $email is empty
    Then #login_btn is disabled

  AC-03:
    Given valid credentials
    When user taps #login_btn
    Then LoginAPI.login is called
    And the screen enters @loading

  AC-04:
    Given LoginAPI.login returns 401
    Then user sees "Email or password is incorrect."
    And user remains on Login screen
}
```

Recommended acceptance coverage:

- default render,
- primary happy path,
- each validation rule,
- each major business rule,
- each major error path,
- navigation paths,
- analytics events for critical actions,
- accessibility baseline.

---

