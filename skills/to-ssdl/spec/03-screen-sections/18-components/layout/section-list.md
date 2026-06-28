| Directive         | Meaning                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `sections:`       | Bound collection of `{ title, data }`                                   |
| `section_header:` | Template component ID for section headers                               |
| `item:`           | Item template component ID                                              |
| `sticky_headers:` | Boolean — section headers pin while section is visible (default `true`) |
| `empty_state:`    | Component shown when sections is empty                                  |

```ssdl
#contacts_list: SectionList {
  in: #content
  sections: $contacts_by_letter
  section_header: #alpha_header
  item: #contact_row
  sticky_headers: true
  empty_state: #contacts_empty
}
```

---

