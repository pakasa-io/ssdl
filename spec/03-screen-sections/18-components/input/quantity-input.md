### 19.14 QuantityInput

| Directive | Meaning                      |
|-----------|------------------------------|
| `bind:`   | Binds to an `Integer` field  |
| `min:`    | Minimum value (default `0`)  |
| `max:`    | Maximum value                |
| `step:`   | Increment size (default `1`) |

**A11Y default role:** `adjustable` — announce as `"Quantity, {value}"`. When the user adjusts the value, announce the
new value. Minimum and maximum values should be announced when limits are reached: `"Minimum quantity reached"` /
`"Maximum quantity reached"`.

```ssdl
#qty_input: QuantityInput {
  in: #cart_row
  bind: $item.quantity
  min: 1
  max: $item.stock_count
  a11y: "Quantity, {$item.quantity}"
}
```

---

