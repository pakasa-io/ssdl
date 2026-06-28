| Directive                 | Meaning                                               |
|---------------------------|-------------------------------------------------------|
| `anchor:`                 | `#component_id` the popover is attached to            |
| `placement:`              | `top` / `bottom` / `left` / `right` / `auto` (§51.15) |
| `dismiss_on_outside_tap:` | Boolean (default `true`)                              |

**A11Y default role:** `dialog`. Move focus inside on open; return focus to anchor on close.

```ssdl
#info_popover: Popover {
  anchor: #info_icon
  placement: bottom
  size: w:lg h:hug
  visible_when: $info_open
  children: [#info_text]
}
```

---

