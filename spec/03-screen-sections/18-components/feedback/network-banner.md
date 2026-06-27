### 19.30 NetworkBanner

| Directive           | Meaning                          |
|---------------------|----------------------------------|
| `offline_msg:`      | Copy when network is unavailable |
| `reconnecting_msg:` | Copy while reconnecting          |

Use `visible_when:` bound to a network state field.

```ssdl
#network_banner: NetworkBanner {
  in: #screen
  pos: sticky(top)
  offline_msg: copy.common.offline
  reconnecting_msg: copy.common.reconnecting
  visible_when: !$network.connected
  a11y: announce_when_visible
}
```

---

