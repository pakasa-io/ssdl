`Progress` uses `style:` to choose between linear and circular rendering.

| Directive        | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| `style:`         | `linear` — horizontal track bar; `circular` — ring/donut                        |
| `value:`         | Current progress — 0 to `max`; required unless `indeterminate: true` (LINT-038) |
| `max:`           | Maximum value (default `100`)                                                   |
| `indeterminate:` | Boolean — animated indefinite progress; ignores `value:`                        |

```ssdl
#upload_progress: Progress {
  in: #upload_card
  style: linear
  value: $upload.bytes_sent
  max: $upload.total_bytes
  size: w:fill h:xxs
  a11y: "Upload progress, {$upload.bytes_sent} of {$upload.total_bytes} bytes"   // or use a derived $upload.percent ==> ($upload.bytes_sent / $upload.total_bytes) * 100 in MODEL
}

#save_ring: Progress {
  in: #form_footer
  style: circular
  indeterminate: true
  size: sm
  visible_when: @saving
}
```

---

