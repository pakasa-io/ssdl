## 12. PERMISSIONS section

Use `PERMISSIONS` to declare OS-level permissions the screen requires, when to request them, and how to handle each
outcome.

```ssdl
PERMISSIONS {
  camera {
    required_for: [#take_photo_btn, #scan_qr_btn]
    request_when: first_tap(#take_photo_btn)
    if not_determined:
      show #camera_rationale_sheet
    if authorized:
      enable [#take_photo_btn, #scan_qr_btn]
    if denied:
      show #camera_denied_banner
      disable [#take_photo_btn, #scan_qr_btn]
    if restricted:
      show #camera_restricted_banner
      disable [#take_photo_btn, #scan_qr_btn]
  }

  notifications {
    required_for: [#enable_alerts_btn]
    request_when: tap #enable_alerts_btn
    if denied:
      show #notifications_denied_sheet
  }
}
```

### 12.1 Supported permission types

```txt
camera
microphone
location.always
location.when_in_use
location.precise          // iOS 14+ / Android 12+: full GPS accuracy
location.approximate      // iOS 14+ / Android 12+: coarse location only
notifications
contacts
photos
biometrics
bluetooth
calendar
health                    // HealthKit (iOS) / Health Connect (Android)
tracking                  // IDFA / ATT on iOS
```

This list is not exhaustive. Teams may add project-specific permission types (e.g., `nfc`, `speech_recognition`)
following the same pattern. Each added type should document its platform scope in a `//` comment.

### 12.2 Permission states

| State            | Meaning                                             |
|------------------|-----------------------------------------------------|
| `not_determined` | User has not been asked yet                         |
| `authorized`     | User granted the permission                         |
| `denied`         | User explicitly denied                              |
| `restricted`     | Device-level restriction (parental controls, MDM)   |
| `provisional`    | Notifications only: granted quietly, without alerts |

### 12.3 Request timing options

```txt
on_view              // Request immediately on screen.view
first_tap(#id)       // Request when user first taps the gated component
explicit_action      // Request only when user taps a dedicated "Enable X" button
deferred             // Do not request; let user trigger from settings
```

---

