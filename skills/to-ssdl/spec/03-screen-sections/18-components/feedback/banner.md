Inline or global message strip. `type:` sets the severity, which drives the color, the default leading icon, and the
accessibility announcement priority.

| Directive      | Meaning                                                                                  |
|----------------|------------------------------------------------------------------------------------------|
| `type:`        | `info` (default) / `success` / `warning` / `error` — severity styling and a11y priority  |
| `dismissible:` | Boolean — show a close affordance (default `false`)                                       |
| `icon:`        | Override the default leading icon for the `type:`                                         |
| `on dismiss:`  | Action fired when the user closes the banner                                              |

**A11Y default role:** `status` (announced politely). `type: error` and `type: warning` raise it to `alert` (announced
assertively). Add `a11y: announce_when_visible` on banners shown conditionally so they are announced when they appear.

```ssdl
#error_banner: Banner {
  in: #form
  type: error
  text: $error_msg
  visible_when: $error_msg.exists
  a11y: announce_when_visible
}
```

---

