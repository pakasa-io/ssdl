### 19.13 TagInput

| Directive        | Meaning                                     |
|------------------|---------------------------------------------|
| `max_tags:`      | Maximum number of tags                      |
| `suggestions:`   | Bound collection for autocomplete           |
| `bind:`          | Binds to `Array(String)` or `Array(Object)` |
| `on tag_add:`    | Action when a tag is added                  |
| `on tag_remove:` | Action when a tag is removed                |

**A11Y default role:** `textfield`.

```ssdl
#recipients_input: TagInput {
  in: #compose_form
  label: "To"
  bind: $recipients
  suggestions: $contact_suggestions
  max_tags: 20
  keyboard: email
  on tag_add: validateRecipient($tag)
  on tag_remove: removeRecipient($tag)
}
```

---

