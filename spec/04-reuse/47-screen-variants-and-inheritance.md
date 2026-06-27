## 47. Screen variants and inheritance

Use `extends` to create a variant that inherits all sections from a base screen and applies targeted overrides. This
avoids full duplication when screens differ by 10–30%.

```ssdl
SCREEN CheckoutPaymentGuest v1 extends CheckoutPayment v2

OVERRIDE {
  META {
    feature: Checkout/Guest
    owner: Commerce Team
  }

  SCOPE {
    out: + "Saved card selection"
  }

  MODEL {
    remove: $saved_card_id
    $guest_email!: Email := ""
  }

  UI {
    remove: #saved_cards_section
    add: #guest_info_section
  }

  VALIDATION {
    add: VAL-10: $guest_email.empty => "Email is required for guest checkout"
  }

  COPY {
    checkout.title: "Guest Checkout"
  }
}
```

### 47.1 OVERRIDE directives

| Directive  | Meaning                                         |
|------------|-------------------------------------------------|
| `add:`     | Add a new item to a list or block               |
| `remove:`  | Remove an item by ID                            |
| `replace:` | Replace an item by ID with a new definition     |
| `+ "text"` | Append a list item (in `SCOPE.out`, `SCOPE.in`) |

### 47.2 Inheritance rules

- All sections from the base screen are inherited unless overridden.
- `SCREEN` name and version are always replaced; do not carry over from base.
- `META.status` defaults to `draft` in the variant; must be set explicitly.
- `ACCEPTANCE` criteria are inherited but should be reviewed; add variant-specific criteria with `add:`.
- Linting applies to the resolved (merged) spec, not just the `OVERRIDE` block.

---

