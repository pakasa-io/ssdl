| Directive            | Meaning                                               |
|----------------------|-------------------------------------------------------|
| `default_country:`   | ISO 3166-1 alpha-2 code — pre-selected country        |
| `allowed_countries:` | Restrict picker to listed countries                   |
| `bind:`              | Binds to a `Phone` field; value includes country code |

**A11Y default role:** `textfield`.

```ssdl
#phone_input: PhoneInput {
  in: #form
  label: copy.profile.phone_label
  bind: $phone_number
  default_country: $user.country_code
  keyboard: phone
  autocomplete: phone
  a11y: "Phone number, required"
}
```

---

