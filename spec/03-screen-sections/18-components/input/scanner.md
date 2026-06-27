### 19.19 Scanner

| Directive       | Meaning                                                                          |
|-----------------|----------------------------------------------------------------------------------|
| `formats:`      | `qr` / `code128` / `ean13` / `pdf417` / `data_matrix` / `aztec` / `all` (§51.12) |
| `overlay_hint:` | Copy shown in the camera overlay                                                 |
| `on scan:`      | Action fired with decoded value — required (LINT-040)                            |

**A11Y default role:** `button`. When the camera is active, announce `"Camera active, scanning for {format}"`. Announce
scan results immediately: `"QR code detected"`. If the camera permission is denied, announce the error state rather than
silently disabling the button.

**Permissions:** requires `PERMISSIONS.camera` (LINT-040).

```ssdl
#qr_scanner: Scanner {
  in: #screen
  size: w:fill h:fill
  formats: [qr]
  overlay_hint: copy.checkin.scan_hint
  on scan: processQRCode($value)
  visible_when: $scanning_active
}
```

---

