| Directive      | Meaning                                                   |
|----------------|-----------------------------------------------------------|
| `label:`       | Section label                                             |
| `required:`    | Boolean — shows required marker on the label              |
| `helper_text:` | Hint below the group                                      |
| `error:`       | Group-level error (distinct from individual field errors) |

```ssdl
#address_group: FormGroup {
  in: #checkout_form
  label: copy.checkout.shipping_address
  required: true
  children: [#address_line1, #address_line2, #city_input, #postcode_input]
}
```

---

