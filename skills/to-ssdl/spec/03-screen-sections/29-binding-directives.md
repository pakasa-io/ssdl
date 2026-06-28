## 29. Binding directives

Use `bind` to connect a UI component to a model field.

```ssdl
#email_input: Input "Email" {
  bind: $email
  keyboard: email
}
```

For one-way display:

```ssdl
#profile_name: Txt {
  text: $user.name
}
```

For collection binding:

```ssdl
#orders_list: List {
  data: $orders as $order
  item: #order_row
  pagination: endless_scroll
  empty_state: #orders_empty
  on scroll.end: loadNextPage() when $has_next_page
}

#order_row: ListItem {
  title: $order.title
  subtitle: $order.status
  on swipe_left: showDeleteAction($order)
  on tap: nav OrderDetail { order_id: $order.id }
}
```

The `as $order` clause on `data:` names the per-element binding, which the `item:` template (`#order_row`) references as
`$order`. A container declares iteration with `data:`/`item:` **or** an explicit `children:` list — never both.
`data:`/`item:` is not limited to scrollable collections; use it on layout stacks (`HStack`, `VStack`) too — e.g. a
wrapping row of filter chips.

### 29.1 Collection directives

| Directive        | Meaning                                  |
|------------------|------------------------------------------|
| `data:`          | Bound collection + element binding       |
| `item:`          | Item template component ID               |
| `pagination:`    | Pagination strategy                      |
| `empty_state:`   | Component shown when collection is empty |
| `selection:`     | Item selection mode                      |
| `on scroll.end:` | Action when user scrolls near the end    |

Pagination strategies:

```txt
endless_scroll     // Infinite scroll; load more at bottom
load_more_btn      // Explicit "Load more" button at end of list
paged              // Full-page pagination with page indicators
none               // Fixed list, no pagination
```

Selection modes:

```txt
none               // No item selection
single             // Tap selects one item at a time
multi              // Tap toggles item selection; multiple allowed
```

---

