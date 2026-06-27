### 19.2 MapView

| Directive           | Meaning                                                                       |
|---------------------|-------------------------------------------------------------------------------|
| `center:`           | Initial map center — `{ lat, lng }` or `$field`                               |
| `zoom:`             | Initial zoom — `street`, `neighborhood`, `city`, `region`, `country` (§51.11) |
| `markers:`          | Bound collection; each item rendered as a map pin                             |
| `interactive:`      | Boolean — allow pan/zoom/tap; `false` for static display                      |
| `on region_change:` | Action fired when user pans or zooms                                          |
| `on marker_tap:`    | Action fired when a marker is tapped                                          |

**A11Y default role:** `image`. Describe the region in `a11y:`.
**Permissions:** displaying user location requires `PERMISSIONS.location.when_in_use` (LINT-041).

```ssdl
#delivery_map: MapView {
  in: #content
  size: w:fill h:xl
  center: $order.delivery_location
  zoom: neighborhood
  markers: $order.route_pins
  interactive: false
  a11y: "Delivery route map"
}
```

---

