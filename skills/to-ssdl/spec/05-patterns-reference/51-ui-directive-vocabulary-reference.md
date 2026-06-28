## 51. UI directive vocabulary reference

Layout and motion vocabulary (positions, sizes, alignment, spacing, layers, behaviors, animation) is defined — with
semantics and examples — in the body (§22–§27, §33); the subsections below for those families are pointers, not
independent definitions. The remaining subsections (§51.7 onward) are the authoritative catalog of component value
enums referenced from §17, §19, and §29. When a token here differs from the body, **the body governs.**

### 51.1 Positions

Anchor, relative (`below(#id)`, `right_of(#id)`…), inside/overlay, sticky, and floating positions — defined with
semantics and examples in **§22**.

### 51.2 Sizes

Base size tokens (`xxs`–`xxl`), width/height hints (`w:fill`, `h:hug`…), and relative sizing (`same_w(#id)`,
`smaller(#id, n)`…) — defined in **§24**.

### 51.3 Alignment

Simple, axis (`main:`/`cross:`), and reference alignment (`align_to(#id.left)`, `baseline_of(#id)`) — defined in **§23**.

### 51.4 Spacing

Spacing tokens (`none`, `xxs`–`xxl`) and directional `pad:`/`margin:`/`inset:` forms — defined in **§25**.

### 51.5 Layers

Layer and z-order tokens (`above(#id)`, `below(#id)`, `z:0`–`z:toast`) — defined in **§26**.

### 51.6 Behaviors

Runtime layout behaviors (`safe_area_aware`, `avoid_keyboard`, `stack_on_small_screen`…) — defined in **§27**.

### 51.7 Style tokens (typography)

Use `style:` on text-bearing components to indicate typographic intent. Exact rendering is determined by the design
system.

```txt
display_xl
display_lg
heading_xl
heading_lg
heading_md
heading_sm
body_lg
body_md
body_sm
label_lg
label_md
label_sm
caption
overline
code
link
```

### 51.8 Keyboard types

Use `keyboard:` on Input, TextArea, and Search components.

```txt
text           // Default text keyboard
email          // Email-optimized (@ and . keys prominent)
number         // Numeric only
decimal        // Decimal number (includes period/comma)
phone          // Phone keypad (digits, *, #)
url            // URL keyboard (/ and . keys prominent)
search         // Search keyboard (Search/Go action key)
ascii          // ASCII-only (iOS)
```

Note: `password` keyboard type is handled by the `Pwd` component; do not set `keyboard:` on `Pwd`.

### 51.9 Autocomplete types

Use `autocomplete:` on Input, Pwd, and Search components to hint the OS credential/autofill system.

```txt
email
password
new_password      // New password field — suppresses autofill, encourages strong suggestion
current_password  // Existing password field — triggers credential autofill
name
given_name
family_name
username
phone
address
postal_code
country
cc_number         // Credit card number
cc_exp            // Credit card expiry
cc_cvc            // Credit card CVC
one_time_code     // SMS OTP
off               // Explicitly disable autocomplete
```

### 51.10 Animation tokens

Enter/exit, loop, speed, and easing animation tokens are defined in **§33.1**; `transition: shared(<key>)` for
shared-element transitions is covered in **§33.2**.

### 51.11 Map zoom levels

```txt
street           // Individual buildings visible
neighborhood     // Blocks and streets
city             // City overview
region           // State/county level
country          // Country overview
```

### 51.12 Scanner formats

```txt
qr               // QR code
code128          // Code 128 barcode
ean13            // EAN-13 / UPC barcode
pdf417           // PDF417 stacked barcode (boarding passes, IDs)
data_matrix      // Data Matrix
aztec            // Aztec code
all              // Attempt all supported formats
```

### 51.13 Status values

```txt
online
offline
busy
away
do_not_disturb
custom           // Use color: to specify
```

### 51.14 Drawer sides

```txt
left
right
```

### 51.15 Popover placement

```txt
top
bottom
left
right
auto             // Platform picks the best placement based on available space
```

### 51.16 Step indicator styles

```txt
dots             // Filled/unfilled circles
numbers          // Numbered circles
bars             // Segmented horizontal bars
progress_bar     // Single linear bar showing completion fraction
```

### 51.17 Color picker modes

```txt
hex              // Single hex input
rgb              // Red/green/blue sliders
hsl              // Hue/saturation/lightness sliders
hsb              // Hue/saturation/brightness sliders
palette          // Fixed set of swatches from palette:
```

### 51.18 Tag styles

```txt
filled           // Solid background color (default)
outline          // Border only, transparent background
ghost            // No border, muted background
tonal            // Lightly tinted background matching the color token
```

### 51.19 Rating styles

```txt
star             // Five-star rating (default)
heart            // Heart icons
thumb            // Thumbs up/down binary
```

### 51.20 Table column definition

A column definition inside `columns:`:

```ssdl
{ id: col_id, header: "Display Name", width: SizeToken, sortable: true, frozen: false }
```

| Field      | Meaning                                           |
|------------|---------------------------------------------------|
| `id`       | Unique column key — used in `on sort:` payload    |
| `header`   | Visible column heading                            |
| `width`    | Size token or `fill` for remaining space          |
| `sortable` | Boolean — column header tappable for sort         |
| `frozen`   | Boolean — column stays fixed on horizontal scroll |

### 51.21 Progress styles

```txt
linear           // Horizontal track bar
circular         // Ring or donut
```

### 51.22 Aspect ratio tokens

```txt
square           // 1:1
wide             // 16:9
portrait         // 3:4
tall             // 9:16
auto             // Natural content size
```

### 51.23 QR error correction levels

```txt
L    // ~7% data recovery
M    // ~15% data recovery (default)
Q    // ~25% data recovery
H    // ~30% data recovery — use when QR may be partially obscured
```

### 51.24 Trend directions

Used by `Stat` component (`trend:` directive).

```txt
up               // Value increased positively
down             // Value decreased (may be positive or negative depending on metric)
neutral          // No significant change
```

### 51.25 Selection modes

Used by `ToggleGroup` (`selection:`) and `Table` (`selection:`).

```txt
none             // No selection
single           // One item active at a time
multi            // Multiple items may be active simultaneously
```

### 51.26 Orientation

Used by `Carousel` (`orientation:`).

```txt
horizontal       // Swipe left/right (default)
vertical         // Swipe up/down
```

### 51.27 Location result types

Used by `LocationInput` (`result_types:`).

```txt
address          // Street-level addresses
city             // Cities and towns
region           // States, counties, provinces
establishment    // Named places — restaurants, shops, landmarks
all              // All result types (default)
```

### 51.28 EmptyState types

Used by `EmptyState` (`type:` directive). Drives default illustration and heading style in the design system.

```txt
empty            // No data yet — "Nothing here yet" (default)
error            // Load or operation failed — "Something went wrong"
offline          // No network — "You're offline"
no_results       // Search or filter returned nothing — "No results found"
permission_denied // Required permission was denied — "Access needed"
custom           // Custom — pair with an explicit illustration: and title:
```

---

