| Directive     | Meaning                         |
|---------------|---------------------------------|
| `message:`    | Optional text below the spinner |
| `cancelable:` | Boolean — show a cancel action  |
| `on cancel:`  | Action when user cancels        |

**A11Y default role:** `dialog`. Move focus into the overlay on show.

```ssdl
#processing_overlay: LoadingOverlay {
  in: #screen
  layer: z:overlay
  message: copy.payment.processing
  cancelable: false
  visible_when: @processing
  a11y: "Processing payment, please wait"
}
```

---

