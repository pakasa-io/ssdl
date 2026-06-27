### 19.22 ContextMenu and ContextMenuItem

**ContextMenu:**

| Directive  | Meaning                                 |
|------------|-----------------------------------------|
| `trigger:` | `long_press` (default) / `right_click`  |
| `anchor:`  | `#component_id` the menu is attached to |

**ContextMenuItem:**

| Directive      | Meaning                                    |
|----------------|--------------------------------------------|
| `text:`        | Item label                                 |
| `icon:`        | Optional icon name                         |
| `destructive:` | Boolean — styles item in destructive color |
| `on tap:`      | Action fired when item is tapped           |

**A11Y:** `ContextMenu` role `menu`. Each `ContextMenuItem` role `menuitem`; destructive items should include
`"destructive action"` in their `a11y:` label. On open, focus moves to the first item; on close, focus returns to the
anchor.

```ssdl
#message_context: ContextMenu {
  anchor: #message_bubble
  children: [#ctx_reply, #ctx_copy, #ctx_delete]
}

#ctx_reply: ContextMenuItem {
  in: #message_context
  text: "Reply"
  icon: "reply"
  on tap: replyTo($message)
}

#ctx_copy: ContextMenuItem {
  in: #message_context
  text: "Copy"
  icon: "copy"
  on tap: copyMessage($message)
}

#ctx_delete: ContextMenuItem {
  in: #message_context
  text: "Delete"
  icon: "trash"
  destructive: true
  on tap: deleteMessage($message)
  a11y: "Delete, destructive action"
}
```

---

