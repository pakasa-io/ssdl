### 19.46 Grid

| Directive  | Meaning                                                               |
|------------|-----------------------------------------------------------------------|
| `columns:` | Number of columns                                                     |
| `masonry:` | Boolean — variable item heights (Pinterest-style); off = uniform rows |
| `data:`    | Bound collection (with `as` element binding)                          |
| `item:`    | Item template component ID                                            |

**A11Y note:** with `masonry: true`, VoiceOver/TalkBack read items in source order regardless of visual column — this is
expected.

```ssdl
#photo_grid: Grid {
  in: #content
  data: $photos as $photo
  item: #photo_card
  columns: 2
  masonry: true
  gap: xs
  empty_state: #photos_empty
}
```

---

