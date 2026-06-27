### 19.41 Collapsible

| Directive    | Meaning                                       |
|--------------|-----------------------------------------------|
| `open:`      | Boolean field or state controlling visibility |
| `on toggle:` | Action fired when open state changes          |

Author supplies the trigger component — typically a `Btn` or `Link` with `on tap: set $open := !$open`.

**A11Y:** The trigger component must reflect expanded/collapsed state. Add `a11y: "Show advanced options, collapsed"` /
`"Hide advanced options, expanded"` on the trigger, or use `aria_expanded: $show_advanced` if the platform supports it.
The collapsible region itself needs no additional role.

```ssdl
#advanced_options: Collapsible {
  in: #form
  open: $show_advanced
  on toggle: set $show_advanced := !$show_advanced
  children: [#advanced_fields]
}
```

---

