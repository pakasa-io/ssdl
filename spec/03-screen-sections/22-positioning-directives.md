## 22. Positioning directives

Use `pos` to specify where an element belongs. Positioning should be semantic, not pixel-perfect.

### 22.1 Anchor positions

```ssdl
pos: top
pos: bottom
pos: left
pos: right
pos: center

pos: top.left
pos: top.center
pos: top.right

pos: middle.left
pos: middle.center
pos: middle.right

pos: bottom.left
pos: bottom.center
pos: bottom.right
```

Anchor qualifiers:

```ssdl
pos: screen.top.center
pos: parent.center
pos: safe.top.right
pos: content.bottom
pos: keyboard.above
```

Examples:

```ssdl
#title: Txt "Welcome back" {
  pos: parent.top.center
}

#close_btn: IconBtn "Close" {
  pos: safe.top.right
}

#empty_state: Card {
  pos: parent.center
}
```

### 22.2 Relative positions

```ssdl
pos: below(#target)
pos: below(#target, sm)
pos: above(#target, md)
pos: left_of(#target, xs)
pos: right_of(#target, xs)
pos: before(#target)
pos: after(#target)
pos: between(#a, #b)
pos: near(#target)
```

Examples:

```ssdl
#subtitle: Txt "Log in to continue" {
  pos: below(#title, xs)
  align: center
}

#password_input: Pwd "Password" {
  pos: below(#email_input, md)
  size: same_w(#email_input) h:lg
}

#forgot_link: Link "Forgot password?" {
  pos: below(#password_input, sm)
  align: end
}
```

### 22.3 Inside and overlay positions

```ssdl
pos: inside(#card, top.left)
pos: inside(#avatar, bottom.right)
pos: overlay(#target, top.right)
pos: overlay(#target, bottom.center)
```

Examples:

```ssdl
#edit_avatar_btn: IconBtn "Edit" {
  pos: overlay(#avatar_img, bottom.right)
  size: smaller(#avatar_img, 2)
}

#badge: Badge "PRO" {
  pos: overlay(#plan_card, top.right)
  size: xs
}
```

### 22.4 Sticky and floating positions

```ssdl
pos: sticky(top)
pos: sticky(bottom)
pos: sticky(bottom.safe)
pos: floating(bottom.right)
pos: floating(top.right)
```

Examples:

```ssdl
#checkout_footer: Footer {
  pos: sticky(bottom.safe)
  size: w:fill h:hug
  pad: md
}

#add_fab: FAB "+" {
  pos: floating(bottom.right)
  size: lg
}
```

---

