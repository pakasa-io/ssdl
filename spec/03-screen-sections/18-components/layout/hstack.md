### 19.47 HStack

| Directive  | Meaning                                             |
|------------|-----------------------------------------------------|
| `wrap:`    | Boolean — wrap children onto multiple lines         |
| `row_gap:` | Spacing between wrapped lines (companion to `gap:`) |

```ssdl
#filter_chips: HStack {
  in: #filter_bar
  wrap: true
  gap: xs
  row_gap: xs
  data: $active_filters as $filter
  item: #filter_chip
}
```

---

