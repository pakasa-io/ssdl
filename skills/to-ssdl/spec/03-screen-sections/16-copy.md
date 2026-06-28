## 16. COPY section

Use `COPY` for user-facing text and localization keys.

```ssdl
COPY {
  login.title: "Welcome back"
  login.subtitle: "Log in to continue"
  login.email_label: "Email"
  login.password_label: "Password"
  login.submit: "Log In"
  login.error.invalid_credentials: "Email or password is incorrect."
}
```

Recommended rule: all user-facing strings in `UI`, `ERRORS`, `VALIDATION`, and `A11Y` should either reference `COPY`
keys or intentionally inline short one-off text.

### 16.1 Parameterized copy

Use ICU message format for strings that require interpolation.

```ssdl
COPY {
  profile.greeting: "Hello, {name}"
  cart.items: "{count, plural, one {# item} other {# items}}"
  order.status: "Order {order_id} placed on {date}"
}
```

Reference parameterized copy in UI by passing values:

```ssdl
#greeting: Txt {
  text: copy.profile.greeting { name: $user.first_name }
}

#cart_count: Txt {
  text: copy.cart.items { count: $cart.item_count }
}
```

### 16.2 Copy key conventions

```txt
<screen>.<element>             login.title
<screen>.<element>.<variant>   login.error.invalid_credentials
common.<element>               common.error.network
common.<element>.<variant>     common.action.retry
```

Maximum recommended nesting depth: 3 levels. Keys beyond 3 levels indicate the string likely belongs to a sub-component
spec.

Preferred:

```ssdl
#title: Txt {
  text: copy.login.title
}
```

Allowed for quick drafts:

```ssdl
#title: Txt "Welcome back"
```

---

