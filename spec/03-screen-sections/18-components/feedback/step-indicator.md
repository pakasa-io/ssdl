### 19.27 StepIndicator

| Directive  | Meaning                                               |
|------------|-------------------------------------------------------|
| `steps:`   | Total step count                                      |
| `current:` | Active step index (0-based) or `$field`               |
| `style:`   | `dots` / `numbers` / `bars` / `progress_bar` (§51.16) |

**A11Y default role:** `text` with label `"Step {current+1} of {steps}"`.

```ssdl
#onboarding_steps: StepIndicator {
  in: #footer
  steps: 4
  current: $onboarding_step
  style: dots
  a11y: "Step {$onboarding_step + 1} of 4"
}
```

---

