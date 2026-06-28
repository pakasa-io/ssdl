## 26. Layering and z-order directives

Use `layer` when components overlap or sit above/below other elements.

```ssdl
layer: above(#content)
layer: below(#modal)
layer: z:0
layer: z:1
layer: z:overlay
layer: z:modal
layer: z:toast
```

Examples:

```ssdl
#loading_overlay: Overlay {
  in: #screen
  layer: above(#content)
  visible_when: @loading
}

#toast: Toast {
  layer: z:toast
  pos: floating(bottom.center)
}
```

Recommended z-order semantics:

| Layer       | Meaning                         |
|-------------|---------------------------------|
| `z:0`       | Default content                 |
| `z:1`       | Above default content           |
| `z:overlay` | Full-screen or partial overlay  |
| `z:modal`   | Modal/dialog level              |
| `z:toast`   | Transient message above most UI |

---

