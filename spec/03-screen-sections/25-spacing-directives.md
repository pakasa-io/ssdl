## 25. Spacing directives

Use spacing tokens for gaps, padding, margins, and insets.

```txt
none
xxs
xs
sm
md
lg
xl
xxl
```

### 25.1 Spacing properties

| Directive | Meaning                                        |
|-----------|------------------------------------------------|
| `gap`     | Space between children in a container          |
| `pad`     | Internal padding inside a component            |
| `margin`  | External spacing around a component            |
| `inset`   | Safe or edge inset, often for overlays/footers |

Examples:

```ssdl
#form: VStack {
  gap: md
  pad: lg
}

#card: Card {
  margin: md
  pad: lg
}

#footer: Footer {
  pos: sticky(bottom.safe)
  inset: safe.bottom
  pad: md
}
```

### 25.2 Directional spacing

Directional forms are allowed when needed.

```ssdl
pad: top:lg right:md bottom:lg left:md
margin: top:sm bottom:xl
inset: bottom:safe
```

---

