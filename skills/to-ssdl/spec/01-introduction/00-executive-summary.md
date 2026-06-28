## 0. Executive summary

SSDL, short for **Single-Screen Specification Definition Language**, is a lightweight text format for describing mobile
app screen requirements. It is designed to be readable by product, design, engineering, QA, analytics, and
AI/code-generation workflows.

SSDL is not meant to replace design files or implementation code. It describes **screen intent**: what the screen
contains, how it behaves, what data it depends on, what business rules apply, and how users move through it.

The format supports two modes:

1. **Full mode** for engineering handoff and QA.
2. **Compact mode** for fast product/design iteration.

The format intentionally uses layout **hints**, not absolute pixel-perfect implementation rules. For example, it uses
`center`, `top.right`, `below(#title, md)`, `w:fill`, `h:hug`, `smaller(#title)`, and `sticky(bottom.safe)` rather than
exact coordinates.

---

