## 24. Sizing directives

Use `size` to express intended size. Do not use exact dimensions unless a platform-specific implementation note requires
it.

### 24.1 Base size tokens

```txt
xxs
xs
sm
md
lg
xl
xxl
```

Recommended interpretation:

| Token | Meaning                                      |
|-------|----------------------------------------------|
| `xxs` | Tiny element, such as a dot or small badge   |
| `xs`  | Extra-small element                          |
| `sm`  | Small element                                |
| `md`  | Default/medium element                       |
| `lg`  | Large, primary, or comfortable touch element |
| `xl`  | Extra-large or prominent element             |
| `xxl` | Hero-sized or highly prominent element       |

### 24.2 Width and height hints

```ssdl
size: w:fill
size: w:hug
size: w:wrap
size: w:content
size: w:full
size: w:screen

size: h:fill
size: h:hug
size: h:wrap
size: h:content
size: h:sm
size: h:lg
```

Recommended meanings:

| Token     | Meaning                                                 |
|-----------|---------------------------------------------------------|
| `hug`     | Size tightly to content                                 |
| `wrap`    | Wrap content, allowing line breaks or natural expansion |
| `fill`    | Fill available parent space                             |
| `full`    | Full size of parent on that axis                        |
| `screen`  | Full screen size on that axis                           |
| `content` | Natural content size                                    |

Examples:

```ssdl
#avatar_img: Img {
  size: w:lg h:lg
}

#login_btn: Btn "Log In" {
  size: w:fill h:lg
}

#terms_text: Txt {
  size: w:fill h:wrap
}
```

### 24.3 Relative sizing

```ssdl
size: same(#target)
size: same_w(#target)
size: same_h(#target)
size: smaller(#target)
size: smaller(#target, 1)
size: smaller(#target, 2)
size: larger(#target)
size: larger(#target, 1)
size: half_of(#target)
size: third_of(#target)
size: min(a, b)
size: max(a, b)
```

Examples:

```ssdl
#confirm_password_input: Pwd "Confirm password" {
  size: same_w(#password_input) h:lg
}

#secondary_btn: Btn "Cancel" {
  size: same_w(#primary_btn)
}

#badge: Badge "NEW" {
  size: smaller(#plan_card, 2)
}
```

### 24.4 Sizing conflict rule

If both a general size and axis-specific size are present, axis-specific values win.

```ssdl
#cta: Btn "Continue" {
  size: lg w:fill
}
```

Interpretation: large button treatment, width fills parent.

---

