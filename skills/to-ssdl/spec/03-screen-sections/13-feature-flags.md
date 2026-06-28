## 13. FEATURE_FLAGS section

Use `FEATURE_FLAGS` to declare which feature flags affect this screen, what they gate, and what the fallback is.

```ssdl
FEATURE_FLAGS {
  new_payment_flow {
    when enabled:
      show #new_payment_section
      hide #legacy_payment_section
    when disabled:
      show #legacy_payment_section
      hide #new_payment_section
    default: disabled
  }

  enhanced_error_messages {
    when enabled:
      $error_display_mode := detailed
    default: enabled
    fallback: disabled    // value used when the flag service is unreachable
  }
}
```

### 13.1 Feature flag fields

| Field            | Meaning                                                                  | Required    |
|------------------|--------------------------------------------------------------------------|-------------|
| `when enabled:`  | Effects when the flag evaluates to enabled                               | Yes         |
| `when disabled:` | Effects when the flag evaluates to disabled                              | Recommended |
| `default:`       | Flag value in production before a controlled rollout begins              | Yes         |
| `fallback:`      | Flag value used when the flag service is unreachable or evaluation fails | Recommended |

`default:` and `fallback:` are independent. Example: a new feature may have `default: disabled` (off before rollout) and
`fallback: disabled` (safe off if flag service fails). A critical fix may have `default: enabled` but
`fallback: enabled` (fail open). Always specify `fallback:` for flags that gate user-visible features.

### 13.2 Feature flag rules

- Every component whose `visible_when` or `hidden_when` condition references a feature flag must have a corresponding
  `FEATURE_FLAGS` entry.
- The `default:` field must be `enabled` or `disabled`. It documents the flag's state in production before a controlled
  rollout.
- Feature flag conditions in `visible_when` should delegate to a named flag rather than embedding the flag check inline:

Preferred:

```ssdl
#new_payment_section: Card {
  visible_when: flag.new_payment_flow.enabled
}
```

Avoid (flag logic scattered, not auditable):

```ssdl
#new_payment_section: Card {
  visible_when: $user.bucket == "experiment_b"
}
```

---

