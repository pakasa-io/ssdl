### 19.31 PullToRefresh

| Directive           | Meaning                                                                   |
|---------------------|---------------------------------------------------------------------------|
| `on refresh:`       | Action when pull gesture completes — required (LINT-039)                  |
| `refreshing:`       | Boolean field or state bound to in-progress refresh — required (LINT-039) |
| `custom_indicator:` | Optional `#component_id` to override the platform default pull animation  |

Wrap around a `Scroll` or `List`.

```ssdl
#orders_refresh: PullToRefresh {
  in: #screen
  on refresh: refreshOrders()
  refreshing: @refreshing
  children {
    #orders_list: List { ... }
  }
}
```

---

