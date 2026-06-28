| Directive  | Meaning                                          |
|------------|--------------------------------------------------|
| `mode:`    | `hex` / `rgb` / `hsl` / `hsb` / `palette`        |
| `palette:` | Array of hex strings — used with `mode: palette` |
| `bind:`    | Binds to a `String` (hex) or `Object` field      |

**A11Y default role:** `adjustable`. Announce the currently selected color value when changed —
`"Color selected: #FF5733"` or `"Red selected"` when using a named palette. For `mode: palette`, announce each swatch as
`"{color name} swatch, {n} of {total}"`.

```ssdl
#theme_color: ColorPicker {
  in: #customization_form
  label: "Accent color"
  mode: palette
  palette: $brand.color_options
  bind: $user.accent_color
}
```

---

