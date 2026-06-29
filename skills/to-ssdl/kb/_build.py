#!/usr/bin/env python3
"""Build the to-ssdl knowledge base: one YAML *fact card* per .ssdl element, in the topological
(define-before-reference) order under tier folders.

The KB is a FACT-EXTRACTION layer. Phase 2 parses the project's SOURCE MATERIAL (OpenAPI, JSON
schemas, DB/ERD, PRD, design specs) and records the concrete facts into each card's `facts` (with
`extracted_from` provenance). Phase 5 authors each section from its card's `facts` + the SSDL spec
slice; `feeds` routes each card's facts to the downstream sections that consume them — grounding
generation in real contracts instead of invented ones. `feeds` is the reverse of the dependency
graph, so facts captured early (API / MODEL / ENTITIES) are in hand when later sections are written.

Each fact item is a *full descriptor* tuned to its consumers, and carries its own `applies_to`
(the screens that fact serves) — a single card holds facts spanning many screens. (Pure frame cards
have one card-level `applies_to`, since they describe one screen.)

Run:  python3 skills/to-ssdl/kb/_build.py   (regenerates the cards + _index.yaml)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TIER = {0: "0-frame", 1: "1-inputs-and-vocabulary", 2: "2-data-and-contracts", 3: "3-presentation",
        4: "4-rules-and-behavior", 5: "5-wiring", 6: "6-instrumentation", 7: "7-verification"}

# order, NAME, tier, needs (reversed into `feeds`), facts-block (rich item descriptors; per-item `applies_to`)
S = [
 (1, "SCREEN", 0, [],
  "  applies_to: []       # the screen this frame describes\n"
  "  name: null           # screen name (PRD)\n"
  "  version: null        # SCREEN version\n"
  "  title: null          # human title shown in nav (PRD/COPY)"),
 (2, "META", 0, [],
  "  applies_to: []       # the screen this frame describes\n"
  "  feature: null        # owning feature (PRD)\n"
  "  owner: null          # team\n"
  "  platform: null       # all | ios | android | web\n"
  "  priority: null       # P0 | P1 | P2\n"
  "  status: null         # draft | ready"),
 (3, "PURPOSE", 0, [],
  "  applies_to: []       # the screen this describes\n"
  "  statement: null      # why this screen exists (PRD)\n"
  "  primary_job: null    # the one job the user comes to do\n"
  "  success_metric: null # how success is measured (PRD / analytics)"),
 (4, "SCOPE", 0, [],
  "  applies_to: []       # the screen this describes\n"
  "  in: []               # included behaviours (PRD)\n"
  "  out: []              # explicitly excluded (PRD)\n"
  "  assumptions: []      # preconditions taken as given"),
 (5, "ROUTE", 1, [],
  "  applies_to: []       # screen on this route\n"
  "  path: null           # operation/route path (openapi / routing)\n"
  "  access: null         # public | authenticated | optional (from security scheme)\n"
  "  params: []           # - { name, in: path|query, type, format, required, default, example, description }\n"
  "  deep_link: null      # external deep-link pattern, if any"),
 (6, "ACTORS", 1, [],
  "  roles: []            # - { name, can_do: [...], applies_to: [screens] }                       (PRD)\n"
  "  systems: []          # - { name, kind: api|service|db, used_for, applies_to: [screens] }      (openapi / PRD)"),
 (7, "ENTRY", 1, [],
  "  from: []             # - { source, trigger, when, params_passed: [...], applies_to: [screens] }   (PRD flows)"),
 (8, "EXIT", 1, [],
  "  to: []               # - { dest, trigger, when, replace: stack?, params_passed: [...], applies_to: [screens] }   (PRD flows)"),
 (9, "PERMISSIONS", 1, [],
  "  scopes: []           # - { name, for_operation, applies_to: [screens] }                       (openapi security)\n"
  "  os: []               # - { type: camera|location|notifications|contacts|biometrics,\n"
  "                       #     required_for, request_when, rationale, if_denied, applies_to: [screens] }   (PRD / component)"),
 (10, "FEATURE_FLAGS", 1, [],
  "  flags: []            # - { name, default: enabled|disabled, gates: [components/behaviours], rollout, applies_to: [screens] }   (config / PRD)"),
 (11, "COPY", 1, [],
  "  strings: []          # - { key, text, params: [ICU vars], max_length, tone, context, applies_to: [screens] }   (PRD / i18n)"),
 (12, "STATES", 1, [],
  "  states: []           # - { name, kind: idle|loading|empty|error|success|custom, trigger, on_enter,\n"
  "                       #     initial: bool, terminal: bool, applies_to: [screens] }   (PRD / async ops)"),
 (13, "MODEL", 2, ["ROUTE"],
  "  request: {}          # <Model>: { applies_to: [screens], attrs: [ { attr, type, format, required, default, enum: [...],\n"
  "                       #            min, max, minLength, maxLength, pattern, example, sensitive: bool, description } ] }   (openapi requestBody)\n"
  "  response: {}         # <Model>: { applies_to: [screens], attrs: [ { attr, type, format, nullable, enum: [...], example,\n"
  "                       #            readOnly, sensitive: bool, relation: <Entity>, description } ] }                       (openapi 2xx body)\n"
  "  entities: {}         # <Name>: { applies_to: [screens], key, relations: [ { to, kind: one|many } ], attrs: [ ...as above... ] }   (schemas, $ref)\n"
  "  derived: []          # - { field, applies_to: [screens] }   candidate computed fields, e.g. $can_submit, $total"),
 (14, "API", 2, [],
  "  operations: []       # - { id, method, path, summary, auth: [scopes], path_params: [...], query_params: [...],\n"
  "                       #     request: <Model>, success: { status, schema }, errors: [ { status, code, schema, meaning } ],\n"
  "                       #     pagination: cursor|offset|none, idempotent: bool, cache, timeout_ms, retry, deprecated,\n"
  "                       #     applies_to: [screens] }   (openapi)"),
 (15, "DATA", 2, ["API", "MODEL"],
  "  reads: []            # - { entity|operation, source: local|remote, cache: none|swr|..., freshness, applies_to: [screens] }   (openapi / db)\n"
  "  writes: []           # - { entity|operation, effect, applies_to: [screens] }\n"
  "  offline: null        # offline / queue behaviour, if specified"),
 (16, "UI", 3, ["MODEL", "COPY", "STATES", "PERMISSIONS", "FEATURE_FLAGS"],
  "  render: []           # - { attr, from: <Model>.response, component, label_key, format, applies_to: [screens] }   (MODEL facts + design)\n"
  "  implied: []          # data -> component map (reference): array->List/Table · enum->Select/SegmentedControl · bool->Switch ·\n"
  "                       #   date->DatePicker · image->Thumbnail · money->PriceTag · status->StatusIndicator · phone->PhoneInput\n"
  "  actions: []          # - { label, intent, primary: bool, applies_to: [screens] }   (CTAs, from PRD)\n"
  "  layout: []           # - { region/hierarchy, applies_to: [screens] }   (design)\n"
  "  states_shown: []     # - { state, applies_to: [screens] }   which @states have a distinct UI"),
 (17, "VALIDATION", 4, ["MODEL"],
  "  constraints: []      # - { attr, rules: [ { kind: required|format|min|max|minLength|maxLength|pattern|enum, value } ],\n"
  "                       #     cross_field: <expr>, async: <uniqueness check>, message_key, applies_to: [screens] }   (schema + PRD)"),
 (18, "BUSINESS_RULES", 4, ["MODEL", "STATES"],
  "  rules: []            # - { id, when: <cond>, then: <effect>, rationale, source, applies_to: [screens] }   (PRD)"),
 (19, "ERRORS", 4, ["API", "UI", "COPY"],
  "  responses: []        # - { operation, status, code, schema, meaning, user_message_key, recovery, retryable: bool, applies_to: [screens] }   (openapi 4xx/5xx)"),
 (20, "STATE_TRANSITIONS", 4, ["STATES", "UI"],
  "  transitions: []      # - { from, event, guard, to, effect, applies_to: [screens] }   (PRD state machine)"),
 (21, "ACTIONS", 4, ["MODEL", "STATES", "API", "ERRORS"],
  "  calls: []            # - { name, on_event, operation, request_from: [fields], sets_states: [...],\n"
  "                       #     on_success, on_error, optimistic: bool, applies_to: [screens] }   (openapi + PRD)"),
 (22, "VALIDATION_UI", 5, ["VALIDATION", "UI"],
  "  surface: []          # - { val_id, field, when: on_blur|on_change|on_submit, display: inline|summary, applies_to: [screens] }   (design / PRD)"),
 (23, "FLOW", 5, ["UI", "STATES", "ACTIONS", "MODEL"],
  "  interactions: []     # - { event, target, guard, intent, leads_to, applies_to: [screens] }   (PRD interactions)"),
 (24, "LIFECYCLE", 5, ["ACTIONS", "STATES"],
  "  triggers: []         # - { on: view|foreground|background|resume, do, why, applies_to: [screens] }   (PRD)"),
 (25, "NAVIGATION", 5, ["UI", "EXIT"],
  "  transitions: []      # - { event, to, route, params, replace: stack?, transition, applies_to: [screens] }   (PRD flows + routes)"),
 (26, "ANIMATION", 5, ["STATES", "UI"],
  "  motion: []           # - { target, enter, exit, shared_element, reduced_motion, applies_to: [screens] }   (design)"),
 (27, "ANALYTICS", 6, ["UI", "FLOW", "MODEL"],
  "  events: []           # - { name, trigger, props: [ { name, from_field } ], when, applies_to: [screens] }   (tracking plan)\n"
  "  pii: []              # - { field, applies_to: [screens] }   never_send (lifted from MODEL 'sensitive' facts)\n"
  "  consent: null        # consent / region requirement, if any"),
 (28, "A11Y", 6, ["UI", "COPY"],
  "  per_screen: []       # - { applies_to: [screen], focus_order: [#ids], labels: [ { id, label_key } ], roles: [...] }   (design / a11y spec)\n"
  "  conventions:         # global a11y standards\n"
  "    contrast: null       # e.g. wcag_aa\n"
  "    dynamic_type: null   # support level\n"
  "    target_min: null     # min touch-target size"),
 (29, "ACCEPTANCE", 7, ["UI", "MODEL", "STATES", "API", "ERRORS", "NAVIGATION", "VALIDATION", "FLOW", "A11Y"],
  "  criteria: []         # - { id, given, when, then, source_story, covers: happy|validation|error|nav|review|a11y, applies_to: [screens] }   (PRD / stories)"),
 (30, "OPEN_QUESTIONS", 7, [],
  "  gaps: []             # - { id, about_element, question, blocks_ready: bool, source_gap, applies_to: [screens] }"),
]

# feeds = reverse(needs): which sections consume each card's facts
FEEDS = {name: [] for _, name, _, _, _ in S}
for _, name, _, needs, _ in S:
    for n in needs:
        FEEDS[n].append(name)

for order, name, tier, needs, facts in S:
    d = os.path.join(HERE, TIER[tier])
    os.makedirs(d, exist_ok=True)
    card = (f"# {order:02d}-{name} · KB fact card ({TIER[tier]})\n"
            f"# Facts extracted from the source material (Phase 2). Sections read `facts`; `feeds` routes them downstream.\n"
            f"# `applies_to` is populated retrospectively — appended as each screen that consumes a fact is built.\n"
            f"element: {name}\n"
            f"kind: section\n"
            f"order: {order}\n"
            f"tier: {TIER[tier]}\n"
            f"extracted_from: []         # provenance, e.g. 'openapi: api/openapi.yaml#/paths/~1auth~1login/post' or 'prd: docs/login.md'\n"
            f"facts:\n{facts}\n"
            f"feeds: [{', '.join(FEEDS[name])}]\n")
    open(os.path.join(d, f"{order:02d}-{name}.yaml"), "w", encoding="utf-8").write(card)

INDEX = """# _index.yaml · fast lookup over extracted facts (maintained during Phase-2 extraction).
# Resolve "where are the facts for X, and which screens/sections use them?" before authoring.
sources: {}           # "openapi: api/openapi.yaml"  -> [elements extracted from it]
operations: {}        # "POST /auth/login"           -> [cards holding its facts: API, MODEL, ERRORS, ACTIONS]
entities: {}          # "User"                       -> [MODEL, DATA, ...]
attributes: {}        # "User.email"                 -> [MODEL, VALIDATION, ANALYTICS]
screens: {}           # "screen.auth.login"         -> [facts whose applies_to includes it]
"""
open(os.path.join(HERE, "_index.yaml"), "w", encoding="utf-8").write(INDEX)
print(f"KB built: {len(S)} fact cards across {len(set(t for _,_,t,_,_ in S))} tiers + _index.yaml")
