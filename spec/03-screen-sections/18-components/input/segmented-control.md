### 19.16 SegmentedControl

| Directive   | Meaning                                                         |
|-------------|-----------------------------------------------------------------|
| `segments:` | Array of `{ label, value }` or bound collection                 |
| `bind:`     | Binds to a field — value matches the selected segment's `value` |

**A11Y default role:** `tablist` — each segment is a `tab`.
**Platform:** `UISegmentedControl` (iOS) / `ChipGroup` or `TabLayout` (Android) /
`@react-native-segmented-control/segmented-control` (RN).

```ssdl
#billing_cycle: SegmentedControl {
  in: #plan_form
  segments: [{ label: "Monthly", value: monthly }, { label: "Annual", value: annual }]
  bind: $billing_cycle
  size: w:fill
}
```

---

