## 30. Event directives

Use `on <event>:` for component-specific events. The event name matches the FLOW vocabulary — no `on_` prefix. An
optional `when <condition>` guard may be appended inline.

```ssdl
on tap: submitLogin()
on long_press: showContextMenu()
on swipe_left: showDeleteAction()
on swipe_right: markAsDone()
on swipe_up: dismiss()
on swipe_down: minimize()
on change: validate $email
on focus: set $active_field := email
on blur: validate $email
on submit: submitLogin()
on scroll.end: loadNextPage()
on refresh: refreshData()
on appear: onComponentAppear()
on disappear: onComponentDisappear()
on select: onItemSelected($item)
on deselect: onItemDeselected($item)
```

Examples:

```ssdl
#password_input: Pwd "Password" {
  bind: $password
  on submit: submitLogin() when $can_submit
}

#order_row: ListItem {
  on swipe_left: showDeleteConfirm($order)
  on long_press: showOrderOptions($order)
}

#retry_btn: Btn "Retry" {
  visible_when: @error
  on tap: retryLastAction()
}
```

### 30.1 Component-to-FLOW event mapping

When a component declares `on <event>:`, the corresponding FLOW entry uses a namespaced event name for system-level
events. Direct user gestures map one-to-one.

| Component directive | FLOW event                        | Notes                                |
|---------------------|-----------------------------------|--------------------------------------|
| `on tap:`           | `on tap #id`                      | Direct                               |
| `on long_press:`    | `on long_press #id`               | Direct                               |
| `on swipe_left:`    | `on swipe_left #id`               | Direct                               |
| `on swipe_right:`   | `on swipe_right #id`              | Direct                               |
| `on swipe_up:`      | `on swipe_up #id`                 | Direct                               |
| `on swipe_down:`    | `on swipe_down #id`               | Direct                               |
| `on change:`        | `on input.change #id`             | Input value changed                  |
| `on focus:`         | `on focus #id`                    | Field gained focus                   |
| `on blur:`          | `on blur #id`                     | Field lost focus                     |
| `on submit:`        | `on keyboard.submit #id`          | Keyboard submit action               |
| `on scroll.end:`    | `on scroll.near_end #id`          | Scroll approached end                |
| `on refresh:`       | `on refresh #id`                  | Pull-to-refresh triggered            |
| `on select:`        | `on select #id`                   | Item selected                        |
| `on deselect:`      | `on deselect #id`                 | Item deselected                      |
| `on appear:`        | `on screen.view` (lifecycle)      | Component became visible; see §32    |
| `on disappear:`     | `on screen.disappear` (lifecycle) | Component left visible area; see §32 |

---

