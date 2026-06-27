| Directive       | Meaning                                                              |
|-----------------|----------------------------------------------------------------------|
| `bias_country:` | ISO country code — biases results                                    |
| `result_types:` | `address` / `city` / `region` / `establishment` / `all` — see §51.27 |
| `bind:`         | Binds to `Object({ address, lat, lng })`                             |

**A11Y default role:** `textfield`.
**Permissions:** no location permission needed for the search-autocomplete path. If the implementation includes a "use
current location" affordance that accesses the device GPS sensor, declare `PERMISSIONS.location.when_in_use` (LINT-041).

```ssdl
#delivery_address: LocationInput {
  in: #checkout_form
  label: copy.checkout.delivery_address
  bind: $delivery_location
  bias_country: $user.country
  result_types: address
  placeholder: "Enter delivery address"
}
```

---

