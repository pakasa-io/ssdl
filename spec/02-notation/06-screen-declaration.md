## 6. Screen declaration

Use a short screen name and a version number.

```ssdl
SCREEN Login v1
```

For screen variants, prefer the `extends` mechanism over duplicated screens. Use a separate name only when screens
diverge significantly.

```ssdl
SCREEN CheckoutPayment v2
SCREEN CheckoutPaymentGuest v1 extends CheckoutPayment v2
```

See §47 for the full variant and inheritance specification.

---

