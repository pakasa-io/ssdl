## 33. ANIMATION section

Use `ANIMATION` to express motion intent for screen transitions and component enter/exit animations. This section
enables `reduced_motion` alternatives to be specified alongside each animation.

```ssdl
ANIMATION {
  screen {
    enter: slide_from_right(md)
    exit: slide_to_left(md)
    reduced_motion: instant
  }

  #error_banner {
    enter: slide_down(sm)
    exit: fade_out(xs)
    reduced_motion: instant
  }

  #skeleton {
    loop: shimmer
    reduced_motion: none
  }

  #success_icon {
    enter: scale_in(sm) then bounce(xs)
    reduced_motion: fade_in(xs)
  }
}
```

### 33.1 Animation tokens

**Enter/exit animations:**

```txt
fade_in(speed)
fade_out(speed)
slide_up(speed)
slide_down(speed)
slide_from_left(speed)
slide_from_right(speed)
slide_to_left(speed)
slide_to_right(speed)
scale_in(speed)
scale_out(speed)
bounce(speed)
shake(speed)          // For validation errors
instant               // No animation
none                  // Element does not animate
```

**Loop animations (for persistent states like loading):**

```txt
shimmer               // Skeleton loading effect
pulse                 // Pulsing opacity
spin                  // Continuous rotation (spinners)
```

**Speed tokens:**

| Token | Approximate duration |
|-------|----------------------|
| `xs`  | ~100ms               |
| `sm`  | ~200ms               |
| `md`  | ~300ms               |
| `lg`  | ~500ms               |
| `xl`  | ~700ms               |

**Easing (optional second parameter):**

```txt
fade_in(sm, ease_out)
slide_up(md, spring)
scale_in(sm, ease_in_out)
```

| Easing token  | Meaning                                                            |
|---------------|--------------------------------------------------------------------|
| `ease_in`     | Starts slow, ends fast — use for exits                             |
| `ease_out`    | Starts fast, ends slow — use for entrances                         |
| `ease_in_out` | Slow start and end — use for transitions between two stable states |
| `spring`      | Physics-based overshoot — native feel on iOS/Android               |
| `linear`      | Constant speed — use for loaders and progress indicators           |

When omitted, easing defaults to `ease_out` for enter animations and `ease_in` for exit animations.

**Chaining animations with `then`:**

Use `then` to sequence animations on the same component.

```ssdl
#success_icon {
  enter: scale_in(sm, spring) then bounce(xs)
  reduced_motion: fade_in(xs)
}
```

Each step in a `then` chain completes before the next begins. Reduced motion applies to the entire chain — specify a
single reduced-motion alternative for the full sequence.

### 33.2 Shared element transitions

```ssdl
ANIMATION {
  #product_image {
    transition: shared(product_image_hero)
  }
}
```

The string in `shared(...)` is the shared element key that the destination screen must also declare.

### 33.3 Reduced motion rule

`reduced_motion` is required on every animation that conveys meaning (entrance, exit, error shake). Use `instant` when
the animation is for delight only and absence doesn't hurt comprehension. Use the reduced-motion alternative when the
animation communicates state change (e.g., sliding in an error banner).

---

