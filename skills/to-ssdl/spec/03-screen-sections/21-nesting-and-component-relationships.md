## 21. Nesting and component relationships

SSDL supports two ways to express nesting: explicit parent references and inline children.

### 21.1 Explicit parent references

```ssdl
#screen: SafeArea {
  children: [#content, #footer]
}

#content: Scroll {
  in: #screen
  children: [#header, #form]
}

#form: VStack {
  in: #content
  children: [#email_input, #password_input, #login_btn]
}
```

### 21.2 Inline nesting

```ssdl
#content: Scroll {
  in: #screen

  children {
    #header: VStack {
      children {
        #title: Txt "Welcome back"
        #subtitle: Txt "Log in to continue"
      }
    }

    #form: VStack {
      children {
        #email_input: Input "Email"
        #password_input: Pwd "Password"
        #login_btn: Btn "Log In"
      }
    }
  }
}
```

### 21.3 Recommended rule

For production handoff, prefer explicit `in:` and `children:` references because they are easier to lint, diff, and
convert into implementation tasks.

---

