## 20. UI directive grammar

```ssdl
UIComponent     := ComponentId ":" ComponentType [String] ComponentBlock
ComponentBlock  := "{" ComponentDirective* "}"

ComponentDirective := ParentDirective
                    | PositionDirective
                    | AlignmentDirective
                    | SizeDirective
                    | SpacingDirective
                    | LayerDirective
                    | StyleDirective
                    | BehaviorDirective
                    | ContentDirective
                    | InputConstraintDirective
                    | AutofillDirective
                    | BindingDirective
                    | KeyboardDirective
                    | ValidationDirective
                    | StateDirective
                    | TestDirective
                    | ConditionDirective
                    | AnimationDirective
                    | TransitionDirective
                    | EventDirective
                    | ChildrenDirective
                    | AccessibilityDirective
                    | CustomDirective

ParentDirective       := "in:" ComponentId
PositionDirective     := "pos:" Position
AlignmentDirective    := "align:" Alignment
SizeDirective         := "size:" SizeExpr
SpacingDirective      := ("gap:" | "pad:" | "margin:" | "inset:") SpacingToken
LayerDirective        := "layer:" LayerExpr
StyleDirective        := "style:" StyleToken
BehaviorDirective     := "behavior:" BehaviorExpr
ContentDirective      := ("label:" | "placeholder:" | "helper_text:" | "error:"
                       | "value:" | "text:") (CopyKey | String | Expression)
InputConstraintDirective := ("min:" | "max:" | "step:") Number
AutofillDirective     := ("autocomplete:" AutocompleteType) | ("autocapitalize:" CapType)
BindingDirective      := "bind:" FieldId
KeyboardDirective     := "keyboard:" KeyboardType
ValidationDirective   := "validation:" "none"
StateDirective        := ("checked_when:" | "selected_when:" | "disabled_when:") Condition
TestDirective         := "test_id:" String
ConditionDirective    := ("visible_when:" | "hidden_when:" | "enabled_when:"
                       | "loading_when:" | "readonly_when:") Condition
AnimationDirective    := "animate:" AnimationExpr                          // see §33.1
TransitionDirective   := "transition:" "shared(" SharedElementKey ")"      // see §33.2; SharedElementKey must match the destination screen's declaration
EventDirective        := "on" EventName ":" Effect ["when" Condition]
ChildrenDirective     := "children:" "[" ComponentId* "]"
AccessibilityDirective:= "a11y:" AccessibilityExpr

// Component-specific directives (see §19 for per-component usage)
LottieDirective       := ("source:" String) | ("autoplay:" Boolean) | ("loop:" Boolean)
                       | ("speed:" Number) | ("progress:" FieldId)
MapDirective          := ("center:" LatLng) | ("zoom:" ZoomToken) | ("markers:" FieldId)
                       | ("interactive:" Boolean)
OTPDirective          := ("length:" Integer) | ("mask:" Boolean)
PhoneDirective        := ("default_country:" CountryCode) | ("allowed_countries:" "[" CountryCode+ "]")
SegmentedDirective    := "segments:" "[" SegmentDef+ "]"
ToggleGroupDirective  := ("options:" "[" ToggleOption+ "]") | ("selection:" SelectionMode)
TagInputDirective     := ("max_tags:" Integer) | ("suggestions:" FieldId)
LocationDirective     := ("bias_country:" CountryCode) | ("result_types:" LocationResultType)
ColorPickerDirective  := ("mode:" ColorMode) | ("palette:" "[" HexColor+ "]")
ScannerDirective      := ("formats:" "[" BarcodeFormat+ "]") | ("overlay_hint:" String)
RichTextDirective     := ("toolbar:" "[" RichTextTool+ "]") | ("max_length:" Integer)
                       // on change: is handled by the standard EventDirective
CarouselDirective     := ("fill:" Boolean) | ("peek:" SpacingToken) | ("snap:" Boolean)
                       | ("indicator:" Boolean) | ("pagination:" PaginationStrategy)
                       | ("orientation:" Orientation) | ("current:" FieldId)
                       // fill:true = full-bleed page mode; fill:false (default) = peek carousel mode
SectionListDirective  := ("sections:" FieldId) | ("section_header:" ComponentId) | ("sticky_headers:" Boolean) | ("empty_state:" ComponentId)
TableDirective        := ("columns:" "[" ColumnDef+ "]") | ("sortable:" Boolean) | ("frozen_columns:" Integer) | ("on row_tap:" Effect)
AccordionDirective    := ("items:" FieldId) | ("allow_multiple:" Boolean)
CollapsibleDirective  := ("open:" Condition) | ("on toggle:" Effect)
DrawerDirective       := ("side:" DrawerSide) | ("gesture_enabled:" Boolean) | ("overlay:" Boolean)
NavBarDirective       := ("title:" String) | ("left:" ComponentId) | ("right:" "[" ComponentId+ "]")
                       | ("large_title:" Boolean) | ("translucent:" Boolean)
TabBarDirective       := ("items:" "[" ComponentId+ "]")
SpeedDialDirective    := ("direction:" Direction)
                       // children are SpeedDialItem components; no inline actions array
SpeedDialItemDir      := ("icon:" String) | ("text:" String)
ContextMenuDirective  := ("trigger:" ContextTrigger) | ("anchor:" ComponentId)
                       // children are ContextMenuItem components; no inline items array
ContextMenuItemDir    := ("text:" String) | ("icon:" String) | ("destructive:" Boolean)
ActionSheetDirective  := ("title:" String) | ("message:" String) | ("actions:" "[" SheetAction+ "]") | ("cancel_label:" String)
DialogDirective       := ("title:" String) | ("message:" String) | ("confirm_label:" String)
                       | ("cancel_label:" String) | ("destructive:" Boolean)
                       // cancel_label omitted = single-button dialog
ModalDirective        := ("dismissible:" Boolean) | ("dismiss_on_outside_tap:" Boolean)
                       // Modal holds arbitrary content via children:; see §19.44 — use Dialog for title+message+actions
EmptyStateDirective   := ("type:" EmptyStateType) | ("illustration:" String) | ("title:" String)
                       | ("description:" String) | ("cta:" CTAExpr)  // see §51.28 for type values
ProgressDirective     := ("style:" ProgressStyle) | ("value:" NumberOrField) | ("max:" Number) | ("indeterminate:" Boolean)
StepIndicatorDirective:= ("steps:" Integer) | ("current:" NumberOrField) | ("style:" StepStyle)
LoadingOverlayDir     := ("message:" String) | ("cancelable:" Boolean)
PullToRefreshDir      := ("refreshing:" FieldIdOrState) | ("custom_indicator:" ComponentId)
NetworkBannerDir      := ("offline_msg:" String) | ("reconnecting_msg:" String)
BannerDirective       := ("type:" BannerType) | ("dismissible:" Boolean) | ("icon:" String)
                       // BannerType = info (default) | success | warning | error
StickyHeaderDir       := ("collapse_height:" SizeToken) | ("expanded_content:" ComponentId)
                       | ("collapsed_content:" ComponentId) | ("parallax:" Boolean)
HStackDirective       := ("wrap:" Boolean) | ("row_gap:" SpacingToken)
                       // wrap:true enables line-wrapping
GridDirective         := ("masonry:" Boolean) | ("columns:" Integer)
                       // masonry:true enables variable item heights
FormGroupDirective    := ("required:" Boolean)
PriceTagDirective     := ("amount:" NumberOrField) | ("currency:" String) | ("original:" NumberOrField)
StatDirective         := ("subtitle:" String) | ("trend:" TrendDir) | ("trend_value:" StringOrField)
NumberBadgeDirective  := ("count:" NumberOrField) | ("max:" Integer)
StatusIndicatorDir    := ("status:" StatusValue) | ("color:" String)
QRCodeDirective       := ("value:" String) | ("error_correction:" ECLevel)
ThumbnailDirective    := ("src:" String) | ("fallback:" String) | ("aspect:" AspectRatio)
PopoverDirective      := ("anchor:" ComponentId) | ("placement:" PopoverPlacement)
                       | ("dismiss_on_outside_tap:" Boolean)
SearchBarDirective    := ("show_filter:" Boolean) | ("autofocus:" Boolean)
TagDirective          := ("text:" String) | ("removable:" Boolean) | ("style:" TagStyle)
RatingDirective       := ("value:" NumberOrField) | ("max:" Integer) | ("style:" RatingStyle)
```

---

