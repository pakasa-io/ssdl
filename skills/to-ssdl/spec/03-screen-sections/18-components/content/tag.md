| Directive    | Meaning                                               |
|--------------|-------------------------------------------------------|
| `text:`      | Tag text — copy key or inline string                  |
| `removable:` | Boolean — show remove affordance                      |
| `style:`     | `filled` / `outline` / `ghost` / `tonal` — see §51.18 |
| `on remove:` | Action when user taps the remove affordance           |

**A11Y default role:** `button` when `removable: true`; `text` otherwise.

```ssdl
#category_tag: Tag {
  in: #filter_row
  text: $category.name
  style: tonal
  removable: true
  on remove: removeFilter($category)
  a11y: "{$category.name}, remove filter"
}
```

---

