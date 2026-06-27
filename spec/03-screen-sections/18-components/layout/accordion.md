### 19.40 Accordion

| Directive         | Meaning                                                           |
|-------------------|-------------------------------------------------------------------|
| `items:`          | Array of `{ header, content: #component_id }` or bound collection |
| `allow_multiple:` | Boolean — multiple sections open simultaneously                   |
| `on expand:`      | Action when a section opens                                       |
| `on collapse:`    | Action when a section closes                                      |

**A11Y:** header buttons use `button` role with `expanded` state.

```ssdl
#faq_accordion: Accordion {
  in: #content
  items: $faq_items
  allow_multiple: false
  on expand: trackFaqExpand($item)
}
```

---

