### 19.9 Thumbnail

| Directive   | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| `src:`      | Image URL or `$field`                                     |
| `fallback:` | Image shown while loading or on error                     |
| `aspect:`   | `square` / `wide` / `portrait` / `tall` / `auto` (§51.22) |

**A11Y default role:** `image`.

```ssdl
#order_thumb: Thumbnail {
  in: #order_row
  src: $order.image_url
  fallback: "images/placeholder_product.png"
  aspect: square
  size: md
  a11y: "{$order.product_name} product image"
}
```

---

