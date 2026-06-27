### 19.1 Lottie

| Directive      | Meaning                                            |
|----------------|----------------------------------------------------|
| `source:`      | Path or asset key to the `.json` Lottie file       |
| `autoplay:`    | Boolean — start playing when visible               |
| `loop:`        | Boolean — repeat indefinitely                      |
| `speed:`       | Playback multiplier — default `1.0`                |
| `progress:`    | Bind to a `$field` (0.0–1.0) to scrub manually     |
| `on complete:` | Action fired when a non-looping animation finishes |

**A11Y default role:** `none` (decorative). Override with `image` if the animation is the primary content.
**Reduced motion:** always provide a `reduced_motion` alternative in `ANIMATION` — substitute a static `Img` or `none`.

```ssdl
#success_burst: Lottie {
  in: #screen
  pos: parent.center
  size: w:xl h:xl
  source: "animations/login_success.json"
  autoplay: true
  loop: false
  visible_when: @success
  on complete: nav Home
}
```

---

