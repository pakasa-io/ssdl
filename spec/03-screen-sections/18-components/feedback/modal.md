### 19.44 Modal

Arbitrary-content modal container. Unlike `Dialog` (the fixed title + message + confirm/cancel shape, §19.26), `Modal`
imposes no internal structure — you supply `children:`. Reach for `Modal` when the overlay hosts a form, a custom
layout, or anything richer than a confirm prompt; reach for `Dialog` for the standard title/message/actions pattern.

| Directive                 | Meaning                                                              |
|---------------------------|----------------------------------------------------------------------|
| `dismissible:`            | Boolean — show a close affordance / allow swipe-down (default `true`) |
| `dismiss_on_outside_tap:` | Boolean — tapping the scrim closes the modal (default `true`)        |
| `on dismiss:`             | Action fired when the modal is dismissed                             |

**A11Y default role:** `dialog`. Trap focus inside while open; move focus in on present and return it to the trigger on
dismiss.

```ssdl
#filters_modal: Modal {
  in: #screen
  layer: z:modal
  visible_when: $filters_open
  on dismiss: set $filters_open := false
  children: [#filters_form, #apply_btn]
}
```

---

