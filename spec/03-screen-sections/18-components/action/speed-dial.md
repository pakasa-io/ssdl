**SpeedDial:**

| Directive    | Meaning                                    |
|--------------|--------------------------------------------|
| `direction:` | `up` (default) / `down` / `left` / `right` |
| `on open:`   | Action when dial expands                   |
| `on close:`  | Action when dial collapses                 |

**SpeedDialItem:**

| Directive | Meaning                              |
|-----------|--------------------------------------|
| `icon:`   | Icon name                            |
| `text:`   | Action label shown when dial is open |
| `on tap:` | Action fired when item is tapped     |

**A11Y:** `SpeedDial` role `menu`; `SpeedDialItem` role `menuitem`.

```ssdl
#compose_dial: SpeedDial {
  pos: floating(bottom.right)
  children: [#action_photo, #action_file, #action_link]
}

#action_photo: SpeedDialItem {
  in: #compose_dial
  icon: "camera"
  text: "Add photo"
  on tap: openCamera()
}

#action_file: SpeedDialItem {
  in: #compose_dial
  icon: "file"
  text: "Attach file"
  on tap: openFilePicker()
}

#action_link: SpeedDialItem {
  in: #compose_dial
  icon: "link"
  text: "Insert link"
  on tap: openLinkInput()
}
```

---

