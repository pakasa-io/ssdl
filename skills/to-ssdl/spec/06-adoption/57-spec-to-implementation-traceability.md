## 57. Spec-to-implementation traceability

SSDL assigns stable IDs to business rules (`BR-xx`), validation rules (`VAL-xx`), error cases (`ERR-xx`), and acceptance
criteria (`AC-xx`). Teams should carry these IDs into implementation to make the connection between spec and code
auditable.

### 57.1 Recommended traceability patterns

**In source code** — reference the rule ID in a comment near the implementation:

```swift
// BR-03: redirect to $redirect_to on successful login
if let redirectTo = state.redirectTo {
    navigator.replace(redirectTo)
}
```

```typescript
// VAL-02: email format validation
if (!isValidEmail(email.trim())) {
    setError('email', copy.login.error.invalid_email)
}
```

**In test files** — use the AC ID as the test name or description:

```typescript
describe('AC-07: successful login stores tokens and navigates', () => {
    it('stores auth_token and refresh_token in secure storage', ...)
    it('navigates to Home when no redirect_to param', ...)
})
```

**In PR descriptions and commit messages** — cite the rule IDs being implemented:

```
feat(login): implement BR-03 redirect-after-login and VAL-01/02 email validation
```

### 57.2 What NOT to put in implementation code

- Do not replicate spec prose in code comments — the spec is the source of truth for intent.
- Do not embed `AC-xx` IDs in production runtime code — they belong in tests and tooling only.
- Do not invent new IDs in implementation; only reference IDs that exist in the spec.

---

