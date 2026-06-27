### 19.17 ToggleGroup

| Directive    | Meaning                                            |
|--------------|----------------------------------------------------|
| `options:`   | Array of `{ label, icon?, value }`                 |
| `selection:` | `single` / `multi` — see §51.25                    |
| `bind:`      | Scalar field for `single`; array field for `multi` |

**A11Y default role:** `radiogroup` for `single`; `group` for `multi`. Each toggle option should announce its label and
selected state — `"{label}, selected"` / `"{label}, not selected"`. For `multi` selection, also announce the total
number of selected options when focus moves away: `"{n} filters selected"`.

```ssdl
#dietary_filters: ToggleGroup {
  in: #filter_bar
  options: $dietary_options
  selection: multi
  bind: $active_filters
  size: w:fill
}
```

---

