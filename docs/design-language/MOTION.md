# Motion

> Static refs only — no strong motion evidence. This system is deliberately minimal.

## Philosophy

**Calm and crisp**. Motion is feedback, not decoration. Nothing loops except loading spinner. No parallax, no staged reveals — they would contradict the quiet paper language.

## Durations

```
--motion-duration-fast:    150ms  press, toggle, icon morph
--motion-duration-normal:  240ms  sheet, nav pill slide, card expand
--motion-duration-slow:    360ms  hero / page transition
```

## Easing

```
--motion-easing-standard:  cubic-bezier(0.2, 0, 0, 1)  // emphasizedDecelerate — entering
--motion-easing-spring:    spring(damping 0.78, stiffness 340) // press, draggable thumb
--motion-easing-emphasized: cubic-bezier(0.05, 0.7, 0.1, 1) // sheet / modal
```

One language: standard for most, spring for press/drag. Do not mix bezier + spring for same class.

## Transitions

- **Enter/exit (sheets, dialogs, menus)**: `fade + translateY 8→0` 240ms emphasized.
- **Nav pill**: thumb slides spring 180–220ms.
- **Card press**: `scale 0.98` 120ms spring + overlay 8% — or elevation 1→0, pick one.
- **Shared-element**: **no evidence** in refs → do not assume hero transition. If later observed, use `scale + fade + radius 16→24 morph` 360ms.

## Layered / staggered

No evidence. Do not add stagger to lists — would feel performative against calm language. If depth is later added, stagger max 24ms.

## Interaction feedback

- **Press**: scale 0.98 or tint 8%, 120ms spring — uniform across all pressables.
- **Hover** (desktop/web): elevation 0→1 or tint 8%, 120ms.
- **Focus**: outline 2px `primary` at 40% + offset 2px — always, 0ms.

## What not to do

- No perpetual loops, no decorative parallax, no per-component custom easing, no >400ms for non-hero.

## Platform snippets

| Concept | Android (Compose) | Web (CSS) | iOS |
|---------|-------------------|-----------|-----|
| Press | `animateFloatAsState(spring(...))` | `transition: transform 150ms ease-out` | `.animation(.spring(...))` |
| Sheet | `AnimatedVisibility(slideInVertically)` | `transform: translateY(100%)→0` | `.transition(.move(edge:.bottom))` |

## Evidence note

If future motion refs are added, revisit: shared transitions, scroll-linked app bar, and carousel morph may then be promoted from "omitted" to specified.
