### 19.26 Dialog

Replaces `ConfirmDialog` and `DialogBox`. Single type handles all focused dialog patterns: omit `cancel_label:` for a
single-button informational dialog; add `cancel_label:` for a two-button choice; set `destructive: true` to style the
confirm action in a destructive color.

| Directive        | Meaning                                                   |
|------------------|-----------------------------------------------------------|
| `title:`         | Dialog heading                                            |
| `message:`       | Body text                                                 |
| `confirm_label:` | Confirm/primary button label                              |
| `cancel_label:`  | Cancel button label — **omit for single-button dialogs**  |
| `destructive:`   | Boolean — styles confirm as destructive (default `false`) |
| `on confirm:`    | Action on confirm                                         |
| `on cancel:`     | Action on cancel                                          |

**A11Y default role:** `alertdialog`.

```ssdl
// Two-button destructive confirmation
#delete_confirm: Dialog {
  title: copy.orders.delete_title
  message: copy.orders.delete_message
  confirm_label: copy.common.delete
  cancel_label: copy.common.cancel
  destructive: true
  on confirm: deleteOrder($order)
  on cancel: set $confirm_open := false
  visible_when: $confirm_open
}

// Single-button informational dialog
#info_dialog: Dialog {
  title: copy.onboarding.tip_title
  message: copy.onboarding.tip_body
  confirm_label: copy.common.got_it
  on confirm: set $tip_open := false
  visible_when: $tip_open
}
```

---

