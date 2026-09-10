# Motion

Only infer what refs reasonably support. Do not invent fake motion details.

## Evidence levels

- **Strong**: sequence frames, video, or interactive prototype shows movement
- **Medium**: visual cues (shared element sizing, overlapping states, blurred trail)
- **Weak**: static image that *could* animate — do not infer; mark "insufficient evidence"

If all refs are static single frames → motion section is short: durations + easing philosophy + interaction feedback only.

## Duration

Infer or default to platform-appropriate values:

```
--motion-duration-fast:    120–160ms  (press, toggle, icon morph)
--motion-duration-normal:  220–280ms  (sheet, nav, card expand)
--motion-duration-slow:    340–480ms  (hero transition, page)
--motion-duration-hero:    500–700ms  (shared-element, only if strong evidence)
```

Choose one set per language. Minimal/calm → longer, eased. Energetic → shorter, springy.

## Easing / Spring

- **Standard**: `ease-out` / `cubic-bezier(0.2, 0, 0, 1)` / `EmphasizedDecelerate` — for entering
- **Emphasized**: `emphasized` easing or `spring(DampingRatioMediumBouncy, StiffnessMedium)` — for hero/expressive moments
- **Spring**: `spring(damping=0.7–0.8, stiffness=300–400)` — for draggable, morphing, overshoot
- **Linear**: only for progress / scrubbing

Rule: one easing philosophy per language. Do not mix spring + bezier for same interaction class.

## Transitions

### Shared transitions
If refs show hero image → detail (same aspect, same radius) → infer shared-element transition with `scale + fade + radius morph`. Otherwise note "no shared-element evidence."

### Entering / Exiting
- **Fade**: `alpha 0→1` + `translateY 8→0` (subtle) — safe default
- **Slide**: sheet from bottom, drawer from edge — only if refs show sheets/drawers
- **Scale**: FAB morph `circle ↔ rounded rect` on press — if refs show press states
- **Expand**: card → detail with `clip + translate` — if refs show expansion

### Layered movement
If refs show depth (overlapping cards, parallax) → `stagger 20–40ms` + `parallax 0.5×` for background. Otherwise flat sequential.

## Interaction feedback

- **Press**: `scale 0.98` or `elevation 1→0` or `shape morph circle ↔ rounded` (pick one, apply to all pressables)
- **Hover** (desktop/web): `elevation 0→1` or `tint overlay 8%`
- **Focus**: `outline 2px primary 40%` + `offset 2px` — always, for a11y
- **Selection**: `fill tint` or `indicator bar` — one per nav type

## What not to do

- No perpetual looping animations (except loading hero with `ProgressAnimationSpec`-style wavy if refs show it)
- No decorative parallax without depth evidence
- No per-component custom easing — one language
- No long durations (>500ms) for non-hero interactions

## Platform mapping

| Concept | Android (Compose) | Web (CSS) | iOS (SwiftUI) |
|---|---|---|---|
| Fast press | `animateFloatAsState(spring(...))` | `transition: transform 150ms ease-out` | `.animation(.spring(duration:0.15))` |
| Sheet enter | `AnimatedVisibility(slideInVertically)` | `transform: translateY(100%) → 0` | `.transition(.move(edge:.bottom))` |
| Shared hero | `SharedTransitionLayout` | View Transitions API | `matchedGeometryEffect` |

## Template output

```md
## Motion
- Philosophy: springy / calm / crisp
- Durations: fast 150ms, normal 250ms, slow 400ms
- Easing: spring(damping 0.75) for press, emphasized for sheets
- Enter/exit: fade+slide 8px, 220ms
- Shared: none observed (or: hero image shared-element)
- Feedback: press scale 0.98, focus outline 2px
```
