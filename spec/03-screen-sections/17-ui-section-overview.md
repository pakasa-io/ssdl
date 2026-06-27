## 17. UI section overview

The `UI` section defines the component tree, component labels, bindings, layout hints, visibility, enabled states,
events, and accessibility hooks.

A component declaration uses this structure:

```ssdl
#component_id: ComponentType "optional visible copy" {
  in: #parent_component
  pos: <position_directive>
  align: <alignment_directive>
  size: <size_directive>
  gap: <spacing_token>
  pad: <spacing_token>
  margin: <spacing_token>
  layer: <layer_directive>
  style: <style_token>
  behavior: <behavior_directive>

  // Content and input directives
  label: <copy_key_or_string>      // User-visible field label (inputs)
  placeholder: <copy_key_or_string> // Placeholder text shown when field is empty
  helper_text: <copy_key_or_string> // Hint text below the field
  error: <expression>               // Inline error — typically errorFor($field) or a string
  value: <field_or_expression>      // Current value for display-only or non-text components
  min: <number>                     // Minimum value (Slider, Stepper, numeric Input)
  max: <number>                     // Maximum value
  step: <number>                    // Increment size (Slider, Stepper)
  autocomplete: <autocomplete_type> // Browser/OS autocomplete hint (email, password, name, etc.)
  autocapitalize: <none|words|sentences|characters>

  // Binding and interaction
  bind: $field
  keyboard: <keyboard_type>
  validation: none
  checked_when: <condition>        // For Chk, Radio, Switch — checked/selected state
  selected_when: <condition>       // For Select, Tabs — selected state
  disabled_when: <condition>       // Inverse of enabled_when; use one or the other

  // Visibility and state
  visible_when: <condition>
  hidden_when: <condition>
  enabled_when: <condition>
  loading_when: <condition_or_state>
  readonly_when: <condition>

  // Animation
  animate: <animation_directive>
  transition: <transition_directive>

  // Structure and QA
  children: [#child_1, #child_2]
  test_id: <string>                // Stable automation selector; kebab-case recommended

  // Events
  on tap: <action_or_nav>
  on long_press: <action>
  on swipe_left: <action>
  on swipe_right: <action>
  on appear: <action>
  on disappear: <action>

  // Accessibility
  a11y: <accessibility_directive>
}
```

**`errorFor($field)`** is a notional utility that returns the first active validation error message for the given model
field, or an empty value when the field is valid or has not been validated yet. It resolves by matching the `$field`
argument against the `fields:` lists declared in the `VALIDATION` section (§34), falling back to the field's `bind:`
target when no `fields:` list is present. Implementations may use an equivalent lookup (e.g., a `Map<FieldId, String>`
populated by the validation runner) rather than a literal `errorFor()` function.

Concise example:

```ssdl
#login_btn: Btn "Log In" {
  in: #form
  pos: below(#password_input, md)
  align: stretch
  size: w:fill h:lg
  style: label_lg
  enabled_when: $can_submit
  loading_when: @loading
  on tap: submitLogin()
}
```

---

