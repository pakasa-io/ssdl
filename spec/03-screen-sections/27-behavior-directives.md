## 27. Behavior directives

Use `behavior` to express runtime layout behavior.

```ssdl
behavior: safe_area_aware
behavior: scroll_when_keyboard_open
behavior: avoid_keyboard
behavior: dismiss_keyboard_on_scroll
behavior: collapse_on_small_screen
behavior: stack_on_small_screen
behavior: hide_on_compact
behavior: sticky_on_scroll
behavior: pin_footer_on_tall_screen
behavior: preserve_scroll_position
behavior: pull_to_refresh
behavior: paged_scroll
behavior: snap_to_item
behavior: swipe_to_dismiss
behavior: drag_to_reorder
```

Examples:

```ssdl
#content: Scroll {
  behavior: scroll_when_keyboard_open
}

#footer: Footer {
  behavior: avoid_keyboard
  pos: sticky(bottom.safe)
}

#button_row: HStack {
  behavior: stack_on_small_screen
}
```

Multiple behaviors may be listed:

```ssdl
#content: Scroll {
  behavior: [scroll_when_keyboard_open, dismiss_keyboard_on_scroll, preserve_scroll_position]
}
```

---

