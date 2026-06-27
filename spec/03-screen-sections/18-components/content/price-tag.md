### 19.8 PriceTag

| Directive   | Meaning                                           |
|-------------|---------------------------------------------------|
| `amount:`   | Current price — Money or `$field`                 |
| `currency:` | ISO code or symbol (default: app locale)          |
| `original:` | Strikethrough original price — shown when present |

**A11Y default role:** `text` — announce as `"{amount}, was {original}"` when `original:` is set.

```ssdl
#item_price: PriceTag {
  in: #product_card
  amount: $product.sale_price
  original: $product.list_price
  style: label_lg
  a11y: "{$product.sale_price}, was {$product.list_price}"
}
```

---

