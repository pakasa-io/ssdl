Single component replaces `EmptyState` and `ErrorState`. The `type:` directive expresses semantic intent and drives
default illustration selection in the design system — omit `illustration:` to use the type default.

| Directive       | Meaning                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------|
| `type:`         | `empty` (default) / `error` / `offline` / `no_results` / `permission_denied` / `custom` — see §51.28 |
| `illustration:` | Override image path, icon name, or Lottie source; omit to use type default                           |
| `title:`        | Primary heading — required (LINT-037)                                                                |
| `description:`  | Supporting description                                                                               |
| `cta:`          | Inline CTA — `"Label" -> action()` or `"Label" -> Destination` — required (LINT-037)                 |

**A11Y:** region role `text`; CTA role `button`.

```ssdl
#orders_empty: EmptyState {
  in: #content
  pos: parent.center
  type: empty
  title: copy.orders.empty_title
  description: copy.orders.empty_body
  cta: copy.orders.empty_cta -> nav Shop
  visible_when: $orders.empty
}

#load_error: EmptyState {
  in: #content
  pos: parent.center
  type: error
  title: copy.common.error_title
  description: copy.common.error_body
  cta: copy.common.retry -> retryLoad()
  visible_when: @error
}
```

---

