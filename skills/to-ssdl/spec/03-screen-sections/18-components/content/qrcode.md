| Directive           | Meaning                                  |
|---------------------|------------------------------------------|
| `value:`            | String encoded in the QR                 |
| `size:`             | Standard size tokens                     |
| `error_correction:` | `L` / `M` (default) / `Q` / `H` (§51.23) |

**A11Y default role:** `image` — always provide `a11y:` describing what the code represents.

```ssdl
#payment_qr: QRCode {
  in: #payment_section
  value: $payment.qr_payload
  size: xl
  a11y: "QR code for payment — scan with your banking app"
}
```

---

