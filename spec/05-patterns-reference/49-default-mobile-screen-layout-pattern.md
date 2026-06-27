## 49. Default mobile screen layout pattern

Most mobile screens can start with this structure.

```ssdl
UI {
  #screen: SafeArea {
    size: w:screen h:screen
    behavior: safe_area_aware
    children: [#content, #footer, #overlay]
  }

  #content: Scroll {
    in: #screen
    pos: safe.top
    size: w:fill h:fill
    pad: lg
    behavior: [scroll_when_keyboard_open, dismiss_keyboard_on_scroll]
    children: [#header, #body]
  }

  #header: VStack {
    in: #content
    pos: top.center
    align: center
    gap: sm
  }

  #body: VStack {
    in: #content
    pos: below(#header, lg)
    align: stretch
    gap: md
  }

  #footer: Footer {
    in: #screen
    pos: sticky(bottom.safe)
    size: w:fill h:hug
    pad: md
    behavior: avoid_keyboard
  }

  #overlay: Overlay {
    in: #screen
    layer: z:overlay
    visible_when: @loading or @modal
  }
}
```

---

