| Directive          | Meaning                                                                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `fill:`            | Boolean — when `true`, items fill the full viewport (full-bleed page mode); when `false` (default), items show a partial peek of adjacent items    |
| `data:`            | Bound collection                                                                                                                                   |
| `item:`            | Item template component ID                                                                                                                         |
| `peek:`            | Spacing token — how much of adjacent item is visible; ignored when `fill: true`                                                                    |
| `gap:`             | Space between items                                                                                                                                |
| `snap:`            | Boolean — snap to item boundaries                                                                                                                  |
| `orientation:`     | `horizontal` (default) / `vertical` — see §51.26                                                                                                   |
| `indicator:`       | Boolean — show page dots                                                                                                                           |
| `current:`         | Bind to current page index field                                                                                                                   |
| `on slide_change:` | Action fired with current index                                                                                                                    |
| `pagination:`      | `none` / `endless_scroll`                                                                                                                          |

**A11Y default role:** scrollable region; each item should declare its own role.

```ssdl
#promo_carousel: Carousel {
  in: #home_header
  data: $promotions
  item: #promo_card
  peek: sm
  gap: sm
  indicator: true
  on slide_change: trackPromoImpression($index)   // define trackPromoImpression() in ACTIONS; emit an analytics event with slide index
  pagination: none
}
```

---

