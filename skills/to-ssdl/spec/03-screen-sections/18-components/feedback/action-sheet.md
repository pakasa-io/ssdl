| Directive       | Meaning                                                 |
|-----------------|---------------------------------------------------------|
| `title:`        | Optional header                                         |
| `message:`      | Optional description                                    |
| `actions:`      | Array of `{ text, style: default/destructive, on tap }` |
| `cancel_label:` | Cancel action label (default `"Cancel"`)                |

**A11Y default role:** `dialog`.

```ssdl
#photo_action_sheet: ActionSheet {
  title: copy.profile.change_photo_title
  actions: [
    { text: copy.profile.take_photo,     style: default,     on tap: openCamera() },
    { text: copy.profile.choose_library, style: default,     on tap: openLibrary() },
    { text: copy.profile.remove_photo,   style: destructive, on tap: removePhoto() }
  ]
  cancel_label: copy.common.cancel
  visible_when: $photo_sheet_open
}
```

---

