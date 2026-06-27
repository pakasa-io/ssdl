### 19.38 Table

| Directive         | Meaning                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------|
| `columns:`        | Array of column defs — see §51.20                                                                   |
| `data:`           | Bound collection                                                                                    |
| `sortable:`       | Boolean — enable column sorting                                                                     |
| `on sort:`        | Action fired with `{ column: String, direction: asc/desc }` when user taps a sortable column header |
| `on row_tap:`     | Action fired with the row's bound data item when user taps a row                                    |
| `frozen_columns:` | First N columns stay fixed on horizontal scroll                                                     |
| `selection:`      | `none` / `single` / `multi`                                                                         |
| `empty_state:`    | Component shown when data is empty                                                                  |

**A11Y default role:** `grid`.

```ssdl
#transactions_table: Table {
  in: #content
  data: $transactions
  columns: [
    { id: date,        header: "Date",        width: md,   sortable: true  },
    { id: description, header: "Description", width: fill                  },
    { id: amount,      header: "Amount",      width: md,   sortable: true  }
  ]
  on sort: sortTransactions($column, $direction)   // $column = column id string; $direction = "asc" | "desc"
  selection: none
  empty_state: #transactions_empty
}
```

---

