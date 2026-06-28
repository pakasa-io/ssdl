**TabBar:**

| Directive        | Meaning                                                    |
|------------------|------------------------------------------------------------|
| `items:`         | Array of `TabItem` component IDs — required (LINT-036)     |
| `on tab_change:` | Action with newly selected tab value — required (LINT-036) |

**TabItem:**

| Directive        | Meaning                      |
|------------------|------------------------------|
| `label:`         | Tab label                    |
| `icon:`          | Icon name or component       |
| `badge:`         | Count or string badge        |
| `selected_when:` | Condition for active styling |

**A11Y:** `TabBar` role is `tablist`; `TabItem` role is `tab`.

```ssdl
#main_tab_bar: TabBar {
  in: #screen
  pos: sticky(bottom.safe)
  items: [#tab_home, #tab_orders, #tab_profile]
  on tab_change: set $active_tab := $tab
}

#tab_home: TabItem {
  in: #main_tab_bar
  label: copy.nav.home
  icon: "home"
  selected_when: $active_tab == home
}

#tab_orders: TabItem {
  in: #main_tab_bar
  label: copy.nav.orders
  icon: "bag"
  badge: $orders.pending_count
  selected_when: $active_tab == orders
}
```

---

