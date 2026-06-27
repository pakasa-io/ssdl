## 55. Recommended adoption workflow

1. Draft the screen in compact mode.
2. Declare `FEATURE_FLAGS` and `PERMISSIONS` before expanding the model.
3. Expand `MODEL`, `UI`, `FLOW`, and `ACTIONS`.
4. Add `STATES` (with `initial:`), `STATE_TRANSITIONS`, and `LIFECYCLE`.
5. Add `VALIDATION` (including cross-field and async rules), `BUSINESS_RULES`, `API`, `ERRORS`, and `NAVIGATION`.
6. Add `ANIMATION` with `reduced_motion` alternatives.
7. Add `ANALYTICS` (with `privacy` and `consent` blocks) and `A11Y` (including `roles`).
8. Write `ACCEPTANCE` criteria covering happy path, validations, errors, navigation, re-view behavior, and
   accessibility.
9. Run the completeness checklist (§53).
10. Resolve `OPEN_QUESTIONS` or mark remaining ones with `blocks:` and `owner:`.
11. Mark `META.status: ready`.

---

