### 19.39 SearchBar

| Directive      | Meaning                              |
|----------------|--------------------------------------|
| `placeholder:` | Hint text                            |
| `bind:`        | Binds to a `String` field            |
| `show_filter:` | Boolean — show a filter icon         |
| `on cancel:`   | Action when user dismisses search    |
| `on filter:`   | Action when user taps filter         |
| `autofocus:`   | Boolean — focus immediately on mount |

```ssdl
#product_search: SearchBar {
  in: #screen
  pos: sticky(top.safe)
  size: w:fill h:lg
  placeholder: copy.shop.search_placeholder
  bind: $search_query
  show_filter: true
  on cancel: clearSearch()
  on filter: openFilters()
}
```

---

