## 28. Visibility, enabled, and loading directives

Use condition directives to connect UI to model/state.

```ssdl
visible_when: $error_msg.exists
enabled_when: $can_submit
loading_when: @loading
hidden_when: keyboard.open
readonly_when: $is_locked
```

Examples:

```ssdl
#error_banner: Banner {
  text: $error_msg
  visible_when: $error_msg.exists
}

#submit_btn: Btn "Submit" {
  enabled_when: $form_valid && !$is_loading
  loading_when: $is_loading
}
```

Recommended interpretation:

| Directive       | Meaning                                                  |
|-----------------|----------------------------------------------------------|
| `visible_when`  | Component exists or is visible only if condition is true |
| `hidden_when`   | Component is hidden if condition is true                 |
| `enabled_when`  | Component accepts interaction only if condition is true  |
| `readonly_when` | Component visible but not editable                       |
| `loading_when`  | Component shows loading treatment                        |

**Visibility vs tree presence:** SSDL treats `visible_when` and `hidden_when` as implementation-agnostic — whether the
component is removed from the layout tree or merely invisible is an implementation detail. However, note the
accessibility implication: a component hidden via opacity/display but still in the accessibility tree may be announced
by screen readers. For components that should be fully absent from the accessibility tree when not visible (e.g., error
banners), add `a11y: hidden_when_not_visible` to signal this intent to implementers.

---

