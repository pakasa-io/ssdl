| Directive | Meaning                                                              |
|-----------|----------------------------------------------------------------------|
| `status:` | `online` / `offline` / `busy` / `away` / `do_not_disturb` / `custom` |
| `label:`  | Optional visible label alongside the dot                             |
| `color:`  | Override dot color when `status: custom`                             |

**A11Y default role:** `text` with label `"{status}"`.

```ssdl
#user_status: StatusIndicator {
  pos: overlay(#avatar, bottom.right)
  status: $user.presence_status
  size: xs
  a11y: "{$user.name} is {$user.presence_status}"
}
```

---

