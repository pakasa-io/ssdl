| Directive            | Meaning                                                      |
|----------------------|--------------------------------------------------------------|
| `collapse_height:`   | Height of the pinned collapsed state                         |
| `expanded_content:`  | Component visible only when expanded                         |
| `collapsed_content:` | Component visible only when collapsed (typically a `NavBar`) |
| `parallax:`          | Boolean — scroll content behind header at reduced rate       |

```ssdl
#profile_header: StickyHeader {
  in: #scroll
  size: w:fill h:xxl
  collapse_height: lg
  expanded_content: #profile_hero
  collapsed_content: #profile_nav
  parallax: true
}
```

---

