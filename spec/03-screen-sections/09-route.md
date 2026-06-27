## 9. ROUTE section

Use `ROUTE` to define how the screen is addressed and whether authentication is required.

```ssdl
ROUTE {
  path: /login
  type: screen
  access: public
  params: {
    entry_source?: String
    redirect_to?: String
  }
}
```

Recommended route fields:

| Field              | Meaning                      | Example values                                     |
|--------------------|------------------------------|----------------------------------------------------|
| `path`             | Canonical route path         | `/login`, `/checkout/payment`                      |
| `type`             | Presentation mode            | `screen`, `modal`, `bottom_sheet`, `dialog`, `tab` |
| `access`           | Access requirement           | `public`, `authenticated`, `optional`              |
| `access_roles`     | Role-based gate (optional)   | `admin`, `premium`, `verified`                     |
| `requires_plan`    | Subscription gate (optional) | `premium`, `pro`                                   |
| `params`           | Route params                 | `order_id!: ID`                                    |
| `deep_links`       | External links               | `myapp://login`                                    |
| `restore_behavior` | Behavior after app restore   | `restore`, `reload`, `redirect`                    |

Example with required params:

```ssdl
ROUTE {
  path: /orders/:order_id
  type: screen
  access: authenticated
  params: {
    order_id!: ID
    open_receipt?: Boolean := false
  }
}
```

---

