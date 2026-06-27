## 14. MODEL section

Use `MODEL` to define screen-local data, defaults, required fields, optional fields, and derived values.

```ssdl
MODEL {
  $email!: Email := ""
  $password!: String := ""
  $remember_me: Boolean := false
  $error_msg?: String
  $is_loading ==> @loading                          // derived from state; see §14.1

  $email_valid ==> matchesEmail(trim($email))
  $password_valid ==> length($password) >= 8
  $form_valid ==> $email_valid && $password_valid
  $can_submit ==> $form_valid && !$is_loading
}
```

### 14.1 Field notation

```ssdl
$field_name!: Type := default
$field_name?: Type
$derived_field ==> expression
```

| Notation      | Meaning                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `$email!`     | Required field — in `MODEL`: must be non-empty/non-null before form submission; in `ROUTE.params`: caller must supply this value at navigation time |
| `$error_msg?` | Optional field — may be null or absent; never blocks submission                                                                                     |
| `:=`          | Default value or assignment                                                                                                                         |
| `==>`         | Computed/derived value — re-evaluated whenever any referenced field changes                                                                         |

**Derived field rules:**

- A derived field (`==>`) may reference other derived fields, but circular dependencies are forbidden. `$a ==> f($b)`
  and `$b ==> g($a)` is a spec error.
- Evaluation order follows a topological sort of the dependency graph. Declare fields in any order; implementations must
  resolve the correct evaluation sequence.
- A derived field must not use `:=` assignment — it is read-only. Use a regular field with `:=` if you need a writable
  computed default.
- To expose a screen state as a Boolean in the model, derive it from the state: `$is_loading ==> @loading`. Do not
  maintain a parallel Boolean field that mirrors state — they will drift.

### 14.2 Recommended types

```txt
String
Text
Email
Password
Number
Integer
Decimal
Money
Boolean
Date
DateTime
Enum(...)
Object(...)
Array(...)
URL
ImageURL
ID
Token
Phone
JSON
```

Examples:

```ssdl
MODEL {
  $plan_id!: ID
  $billing_cycle: Enum(monthly, annual) := monthly
  $subtotal: Money := 0
  $discount?: Money
  $total ==> $subtotal - coalesce($discount, 0)
}
```

---

