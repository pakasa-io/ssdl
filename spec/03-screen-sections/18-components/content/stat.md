### 19.7 Stat

| Directive      | Meaning                                     |
|----------------|---------------------------------------------|
| `value:`       | Primary number — Number, Money, or `$field` |
| `subtitle:`    | Descriptor below the value                  |
| `trend:`       | `up` / `down` / `neutral` — see §51.24      |
| `trend_value:` | Trend magnitude text — `"+12%"` or `$field` |

**A11Y default role:** `text`.

```ssdl
#revenue_stat: Stat {
  in: #dashboard_row
  value: $metrics.revenue
  subtitle: "Revenue this month"
  trend: up
  trend_value: $metrics.revenue_change_pct
  style: heading_lg
}
```

---

