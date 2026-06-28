| Directive | Meaning                                                         |
|-----------|-----------------------------------------------------------------|
| `count:`  | Number or `$field`                                              |
| `max:`    | Display cap — counts above this show as `{max}+` (default `99`) |

**A11Y default role:** `text` — announce the full count, not the capped display.

```ssdl
#notif_badge: NumberBadge {
  pos: overlay(#notif_icon, top.right)
  count: $notifications.unread_count
  max: 99
  visible_when: $notifications.unread_count > 0
  a11y: "{$notifications.unread_count} unread notifications"
}
```

---

