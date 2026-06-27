## 32. LIFECYCLE section

Use `LIFECYCLE` to declare screen-level and app-level events that affect this screen. This is distinct from `FLOW` (
which handles user events) and `STATES` (which declares states). LIFECYCLE events drive state transitions and data
refreshes that are not user-initiated.

```ssdl
LIFECYCLE {
  on screen.view do onScreenView()
  on screen.first_view do onFirstView()
  on screen.disappear do onScreenDisappear()
  on screen.destroy do onScreenDestroy()
  on app.foreground do onAppForeground()
  on app.background do onAppBackground()
}
```

### 32.1 Lifecycle event vocabulary

| Event               | When it fires                                                                                |
|---------------------|----------------------------------------------------------------------------------------------|
| `screen.view`       | Every time the screen becomes visible — initial push AND return from a child screen or modal |
| `screen.first_view` | Only on the first presentation of this screen instance                                       |
| `screen.disappear`  | When another screen covers this one (not on destruction)                                     |
| `screen.destroy`    | When the screen is popped from the stack and cleaned up                                      |
| `app.foreground`    | When the app returns from background while this screen is active                             |
| `app.background`    | When the app moves to background while this screen is active                                 |

### 32.2 Common patterns

```ssdl
LIFECYCLE {
  // Refresh data when returning from a child screen
  on screen.view do refreshIfStale()

  // Only run analytics on first view
  on screen.first_view do {
    emit profile_viewed { source: $entry_source }
  }

  // Pause media/timers when covered
  on screen.disappear do pauseAutoplay()

  // Resume and check for external changes after app restore
  on app.foreground do checkForExternalUpdates()

  // Release resources proactively
  on app.background do releaseCameraIfActive()
}
```

### 32.3 Lifecycle error handling

All `LIFECYCLE` handlers that perform async work must specify failure behavior, either inline or via `ACTIONS`.

```ssdl
LIFECYCLE {
  on screen.view do refreshData()
}

ACTIONS {
  refreshData() {
    set @refreshing
    response = await DataAPI.get()

    match response.status:
      200 => set @loaded
      else => set @error   // Do not set @error on app.foreground — show toast instead
  }
}
```

---

