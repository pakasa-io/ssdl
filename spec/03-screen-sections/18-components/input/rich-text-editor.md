### 19.20 RichTextEditor

| Directive      | Meaning                                                                              |
|----------------|--------------------------------------------------------------------------------------|
| `toolbar:`     | `bold` / `italic` / `underline` / `bullet_list` / `numbered_list` / `link` / `image` |
| `max_length:`  | Character limit                                                                      |
| `bind:`        | Binds to a `Text` field                                                              |
| `placeholder:` | Text shown when empty                                                                |
| `on change:`   | Action fired on edit — aligns with §30 event vocabulary                              |

**A11Y default role:** `textfield`.

```ssdl
#post_editor: RichTextEditor {
  in: #compose_screen
  size: w:fill h:fill
  toolbar: [bold, italic, bullet_list, link]
  bind: $post_body
  placeholder: copy.compose.body_placeholder
  max_length: 5000
  on change: updateCharCount()
}
```

---

