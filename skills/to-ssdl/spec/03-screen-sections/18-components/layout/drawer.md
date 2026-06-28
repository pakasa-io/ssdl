**Drawer:**

| Directive                | Meaning                                              |
|--------------------------|------------------------------------------------------|
| `side:`                  | `left` (default) / `right`                           |
| `width:`                 | Width of the open drawer — size token                |
| `overlay:`               | Boolean — dim content behind drawer (default `true`) |
| `gesture_enabled:`       | Boolean — allow swipe-to-open (default `true`)       |
| `on open:` / `on close:` | Actions fired on state change                        |

**DrawerItem:**

| Directive        | Meaning                                                        |
|------------------|----------------------------------------------------------------|
| `icon:`          | Icon name or component                                         |
| `label:`         | Item label                                                     |
| `selected_when:` | Active/selected condition                                      |
| `badge:`         | Badge count or string                                          |
| `on tap:`        | Action fired when item is tapped — typically `nav Destination` |

**A11Y:** `Drawer` role `navigation`; `DrawerItem` role `menuitem`.

```ssdl
#side_drawer: Drawer {
  in: #screen
  side: left
  width: lg
  visible_when: $drawer_open
  on close: set $drawer_open := false
  children: [#item_home, #item_settings]
}

#item_home: DrawerItem {
  in: #side_drawer
  icon: "home"
  label: copy.nav.home
  selected_when: $active_route == home
  on tap: nav Home
}
```

---

