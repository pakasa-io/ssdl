## 5. Top-level grammar

This is a practical grammar, not a formal compiler grammar. It defines how the notation should be written and
interpreted.

```ssdl
// --- Screen document ---

Document        := ScreenDecl ImportDecl* Section+
ScreenDecl      := "SCREEN" ScreenName ["extends" ScreenName "v" Version] "v" Version
ImportDecl      := "import" ImportItems "from" Path ["at" "v" Version]
ImportItems     := "{" ImportItem ("," ImportItem)* "}"
                 | CopyNamespace                       // e.g. copy.common
ImportItem      := (ComponentId | Identifier | CopyKey) ["as" Identifier]
Path            := QuotedString                        // relative path or @alias path
CopyNamespace   := "copy" "." Identifier+             // e.g. copy.common, copy.errors
IncludeDirective := "include" Path                     // valid at the top of any section block, before section-specific entries; inlines content from the named fragment file into the enclosing section
Section         := META | PURPOSE | SCOPE | ROUTE | ACTORS | ENTRY | EXIT
                 | PERMISSIONS | FEATURE_FLAGS | MODEL | DATA | COPY | UI
                 | STATES | STATE_TRANSITIONS | LIFECYCLE | ANIMATION | VALIDATION
                 | VALIDATION_UI | BUSINESS_RULES | ACTIONS | FLOW | API
                 | NAVIGATION | ANALYTICS | A11Y | ERRORS | ACCEPTANCE
                 | OPEN_QUESTIONS | OVERRIDE

// --- Fragment document ---

FragmentDocument  := FragmentDecl ExportDecl* ImportDecl* FragmentSection+
FragmentDecl      := "FRAGMENT" FragmentName "v" Version
FragmentSection   := FRAGMENT_META | UI | COPY | API | ERRORS | ACTIONS
                   | VALIDATION | MODEL | A11Y | ANALYTICS
ExportDecl        := "export" (ComponentId | Identifier | CopyNamespace)

// --- Shared terminals ---

Identifier      := letter (letter | digit | "_" | "-")*
ComponentId     := "#" Identifier
FieldId         := "$" Identifier
StateId         := "@" Identifier
CopyKey         := "copy" "." (Identifier ".")* Identifier
RuleId          := ("BR" | "VAL" | "ERR" | "AC") "-" digit+
Condition       := expression returning Boolean
Effect          := assignment | uiEffect | navigation | actionCall | asyncCall | eventEmit
AsyncCall       := [FieldId "="] "~>" (ApiMethod | HttpCall)   // async external/network call; binds result when FieldId present (§36.1, §37)
String          := quoted text
Block           := "{" lines "}"
Comment         := "//" rest-of-line      // inline or full-line; "#" is reserved for ComponentId and must not be used as a comment delimiter
```

---

