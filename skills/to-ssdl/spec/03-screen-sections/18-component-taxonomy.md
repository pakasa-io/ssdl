## 18. Component taxonomy

### 18.1 Content components

| Type              | Meaning                                                                                |
|-------------------|----------------------------------------------------------------------------------------|
| `Txt`             | Static text                                                                            |
| `RichTxt`         | Rich/formatted text                                                                    |
| `Img`             | Image                                                                                  |
| `Thumbnail`       | Small image with lazy loading and placeholder fallback                                 |
| `Icon`            | Icon                                                                                   |
| `Avatar`          | User/profile image                                                                     |
| `Badge`           | Small text label/status marker                                                         |
| `NumberBadge`     | Count bubble — notification dot with a numeric value (99+)                             |
| `Tag`             | Inline removable label; pill/chip shape — filter tags, category labels, selected items |
| `StatusIndicator` | Colored presence dot — online, offline, busy, away                                     |
| `Rating`          | Read-only star/heart/thumb score display                                               |
| `Stat`            | Single KPI block — large number + label + optional trend                               |
| `PriceTag`        | Formatted price with optional strikethrough original price                             |
| `QRCode`          | Display-only QR code generated from a value                                            |
| `Lottie`          | JSON-driven animation — success bursts, empty state illustrations, loading delight     |
| `MapView`         | Embedded interactive or static map                                                     |
| `Divider`         | Visual divider                                                                         |
| `Spacer`          | Flexible empty space                                                                   |

### 18.2 Input components

| Type               | Meaning                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Input`            | Text input                                                                                                                                                                                                               |
| `Pwd`              | Password input                                                                                                                                                                                                           |
| `TextArea`         | Multiline input                                                                                                                                                                                                          |
| `Search`           | Search input field (no cancel/filter chrome — use `SearchBar` for the full UI)                                                                                                                                           |
| `OTPInput`         | Fixed-length segmented code entry — SMS verify, 2FA, PIN                                                                                                                                                                 |
| `PhoneInput`       | Phone number field with integrated country code picker                                                                                                                                                                   |
| `TagInput`         | Multi-value freeform entry with removable chips — email recipients, tags                                                                                                                                                 |
| `QuantityInput`    | Inline +/- styled quantity selector — e-commerce, cart; distinct from `Stepper` which is generic                                                                                                                         |
| `LocationInput`    | Address/place autocomplete field — Google Places style                                                                                                                                                                   |
| `RichTextEditor`   | Formatted text authoring with toolbar — bold, italic, lists, links                                                                                                                                                       |
| `Chk`              | Checkbox                                                                                                                                                                                                                 |
| `Radio`            | Radio button                                                                                                                                                                                                             |
| `Switch`           | Toggle                                                                                                                                                                                                                   |
| `SegmentedControl` | Mutually exclusive inline option switcher — sets a value, not triggers an action. Platform: `UISegmentedControl` (iOS) / `ChipGroup` or `TabLayout` (Android) / `@react-native-segmented-control/segmented-control` (RN) |
| `ToggleGroup`      | Group of toggle buttons where one or more can be active — filter bars, multi-select chip sets                                                                                                                            |
| `Select`           | Picker/dropdown                                                                                                                                                                                                          |
| `Slider`           | Range/value slider                                                                                                                                                                                                       |
| `Stepper`          | Increment/decrement control                                                                                                                                                                                              |
| `DatePicker`       | Date-only selector                                                                                                                                                                                                       |
| `TimePicker`       | Time-only selector                                                                                                                                                                                                       |
| `DateTimePicker`   | Combined date and time selector                                                                                                                                                                                          |
| `ColorPicker`      | Color selection — hex, RGB, HSL, or palette                                                                                                                                                                              |
| `Scanner`          | Camera QR/barcode capture trigger                                                                                                                                                                                        |
| `FilePicker`       | File/image selector from device library                                                                                                                                                                                  |

### 18.3 Action components

| Type              | Meaning                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| `Btn`             | Button                                                                                                    |
| `IconBtn`         | Icon button                                                                                               |
| `Link`            | Tappable text/link                                                                                        |
| `MenuBtn`         | Button opening a menu                                                                                     |
| `FAB`             | Floating action button — single primary action                                                            |
| `SpeedDial`       | FAB that expands into a set of sub-action buttons — Material Design pattern; children are `SpeedDialItem` |
| `SpeedDialItem`   | Individual action in a `SpeedDial` — icon + text + tap handler                                            |
| `ContextMenu`     | Long-press or right-click contextual action list anchored to a component; children are `ContextMenuItem`  |
| `ContextMenuItem` | Individual item in a `ContextMenu` — text + optional icon + optional destructive flag                     |

### 18.4 Feedback components

| Type             | Meaning                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Banner`         | Inline/global message; `type:` sets severity — see §19.45                                                                                                                                                                                |
| `NetworkBanner`  | Offline/reconnecting persistent notice — always visible while condition holds                                                                                                                        |
| `Toast`          | Temporary auto-dismissing message                                                                                                                                                                    |
| `Snackbar`       | Temporary bottom message with optional action                                                                                                                                                        |
| `Spinner`        | Indeterminate loading indicator                                                                                                                                                                      |
| `InlineLoader`   | Small spinner scoped to a list item, card, or button area                                                                                                                                            |
| `Skeleton`       | Loading placeholder for a content region                                                                                                                                                             |
| `Progress`       | Progress indicator — use `style: linear` for a track bar or `style: circular` for a ring; use `indeterminate: true` when progress is unknown                                                         |
| `StepIndicator`  | Step/page progress — dots, numbers, or bars indicating position in a funnel or onboarding flow                                                                                                       |
| `EmptyState`     | Structured state region — illustration + title + description + CTA. Use `type:` to express intent: `empty` (no data), `error` (load failed), `offline`, `no_results`, `permission_denied`, `custom`. |
| `LoadingOverlay` | Full-screen blocking spinner with optional message and cancel                                                                                                                                        |
| `Modal`          | Arbitrary-content modal container (see §19.44)                                                                                                                                                                         |
| `Dialog`         | Focused dialog — title + message + confirm button + optional cancel; use `destructive: true` for destructive confirm actions. Replaces `ConfirmDialog` and `DialogBox`.                              |
| `ActionSheet`    | Option list presented as an overlay — iOS action sheet / Android bottom option menu                                                                                                                  |
| `Sheet`          | Bottom sheet content container                                                                                                                                                                       |
| `Popover`        | Anchored floating panel — can contain interactive content; distinct from `Tooltip` which is read-only                                                                                                |
| `Tooltip`        | Read-only helper text anchored to a component                                                                                                                                                        |

### 18.5 Layout components

| Type            | Meaning                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| `Container`     | Generic parent                                                                                                               |
| `SafeArea`      | Safe-area-aware wrapper                                                                                                      |
| `Scroll`        | Scrollable container                                                                                                         |
| `PullToRefresh` | Refresh trigger wrapper around a `Scroll` — declares pull gesture and refresh handler                                        |
| `VStack`        | Vertical stack                                                                                                               |
| `HStack`        | Horizontal stack; use `wrap: true` for wrapping chip/tag rows                                                                |
| `ZStack`        | Layered stack                                                                                                                |
| `Grid`          | Regular-column grid layout; use `masonry: true` for irregular (Pinterest-style) item heights                                 |
| `Card`          | Grouped content container                                                                                                    |
| `Section`       | Semantic content group                                                                                                       |
| `FormGroup`     | Logical grouping of related form fields with a shared section label, helper text, and error state                            |
| `Header`        | Top region                                                                                                                   |
| `NavBar`        | Top navigation bar — title, leading back/menu action, trailing actions                                                       |
| `StickyHeader`  | Collapsing/parallax header that pins at the top on scroll; transitions to a compact `NavBar`                                 |
| `Footer`        | Bottom region                                                                                                                |
| `TabBar`        | Bottom tab navigation container — holds `TabItem` components                                                                 |
| `TabItem`       | Individual tab within `TabBar` or `Tabs` — label, icon, badge count, selected state                                          |
| `Drawer`        | Side navigation panel — slides in from left or right edge                                                                    |
| `DrawerItem`    | Individual item within a `Drawer`                                                                                            |
| `Overlay`       | Overlay layer                                                                                                                |
| `List`          | Flat list container                                                                                                          |
| `ListItem`      | List row/item                                                                                                                |
| `SectionList`   | Grouped list with sticky section headers — contacts A–Z, grouped settings                                                    |
| `Table`         | Columnar data grid — sortable, frozen columns, optional row selection                                                        |
| `Tabs`          | Inline tab set within a screen (content switching, not navigation)                                                           |
| `Accordion`     | Expandable/collapsible section with a tappable header                                                                        |
| `Collapsible`   | Generic show/hide wrapper — no built-in header affordance; use when you supply your own trigger                              |
| `Carousel`      | Pageable item strip — use `fill: true` for full-bleed pages; default shows partial peek of adjacent items                    |
| `SearchBar`     | Full search UI with input, cancel button, and optional filter affordance; wraps `Search` input                               |

---

