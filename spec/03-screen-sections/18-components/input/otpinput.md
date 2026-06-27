### 19.11 OTPInput

| Directive                     | Meaning                                      |
|-------------------------------|----------------------------------------------|
| `length:`                     | Cell count — required (LINT-033)             |
| `mask:`                       | Boolean — obscure digits                     |
| `autocomplete: one_time_code` | Required for SMS autofill on iOS and Android |
| `on complete:`                | Action fired when all cells are filled       |

**A11Y default role:** `textfield` with label `"One-time code, {length} digits"`.

```ssdl
#otp_input: OTPInput {
  in: #form
  length: 6
  mask: false
  autocomplete: one_time_code
  keyboard: number
  bind: $otp_code
  on complete: verifyOTP()
  a11y: "Verification code, 6 digits"
}
```

---

