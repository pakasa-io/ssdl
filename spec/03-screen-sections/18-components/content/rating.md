### 19.3 Rating

| Directive | Meaning                              |
|-----------|--------------------------------------|
| `value:`  | Score — Number or `$field`           |
| `max:`    | Maximum (default `5`)                |
| `style:`  | `star` (default) / `heart` / `thumb` |

**A11Y default role:** `text` — announce as `"{value} out of {max} stars"`.

```ssdl
#product_rating: Rating {
  in: #product_header
  value: $product.avg_rating
  max: 5
  style: star
  size: sm
  a11y: "{$product.avg_rating} out of 5 stars"
}
```

---

