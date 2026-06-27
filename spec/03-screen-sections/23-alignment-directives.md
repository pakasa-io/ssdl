## 23. Alignment directives

Use `align` for internal or external alignment.

### 23.1 Simple alignment

```ssdl
align: start
align: center
align: end
align: stretch
```

Examples:

```ssdl
#header: VStack {
  align: center
}

#form: VStack {
  align: stretch
}

#forgot_link: Link "Forgot password?" {
  align: end
}
```

### 23.2 Axis alignment

Use `main` and `cross` for stack-like containers.

```ssdl
align: main:start cross:stretch
align: main:center cross:center
align: main:end cross:center
align: main:space_between cross:center
align: main:space_around cross:center
```

Example:

```ssdl
#signup_row: HStack {
  align: main:center cross:center
  gap: xs
}
```

### 23.3 Reference alignment

```ssdl
align: align_to(#target.left)
align: align_to(#target.right)
align: align_to(#target.center)
align: baseline_of(#target)
```

Example:

```ssdl
#helper_text: Txt "Use at least 8 characters" {
  pos: below(#password_input, xs)
  align: align_to(#password_input.left)
}
```

---

