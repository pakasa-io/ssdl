| Directive      | Meaning                                                       |
|----------------|---------------------------------------------------------------|
| `title:`       | Screen title — required (LINT-035)                            |
| `left:`        | Leading action — back button or menu icon                     |
| `right:`       | Trailing actions — array of component IDs or inline `IconBtn` |
| `large_title:` | Boolean — iOS large title style; collapses on scroll          |
| `translucent:` | Boolean — frosted glass background                            |

**A11Y default role:** `navigation`.

```ssdl
#main_nav: NavBar {
  in: #screen
  pos: sticky(top.safe)
  title: copy.orders.screen_title   // illustrative — define in COPY section of this screen's spec
  left: #back_btn
  right: [#filter_btn, #search_btn]
  large_title: false
}
```

---

