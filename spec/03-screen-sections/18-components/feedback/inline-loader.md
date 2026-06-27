### 19.43 InlineLoader

Reuses standard directives only (`size:`, `visible_when:`). No component-specific directives.

**A11Y default role:** `none` (decorative) when scoped to a row or card that itself has a loading state — the parent's
`loading_when:` state should be announced instead. Use `a11y: announce_when_visible` only when the `InlineLoader` is the
sole indication that something is happening (no loading text or state change on the parent).

```ssdl
#sync_loader: InlineLoader {
  in: #order_row
  pos: right_of(#order_status, sm)
  size: xs
  visible_when: $order.syncing
}
```

---

