# Foundations — Design Tokens

Source: 16 inspiration refs. Base: warm paper minimalism, spacious, soft geometry.

---

## Spatial System

**Base unit**: 4px. Aesthetic is spacious → ladder leans generous. 8 is the workhorse.

```
--space-1:   4px   micro (icon·text, dot gap)
--space-2:   8px   tight (chip group, inline)
--space-3:  12px   related items, card inner tight
--space-4:  16px   component padding, card padding (default)
--space-5:  24px   section gap, card-to-card
--space-6:  32px   block separation
--space-7:  48px   section separation
--space-8:  64px   hero separation, page breathing room
```

- **Content margins**: 16 (phone) / 20–24 (tablet) / 24+ centered max-width (desktop). Never flush to edge except hero bleed.
- **Component gaps**: chip group 8, list rows 2 (connected panel) or 12 (separate), card grid 16, section stacks 24–32.
- **Alignment**: flush-left dominant; centered only for empty/hero states.
- **Max widths**: reading 640–720, page 1024–1280 (phone-first refs → desktop assumed).
- **Density**: default comfortable. Compact (−1 step) only for dense tables/settings. No mixing per screen.

---

## Shape System

Continuous (squircle-leaning) soft geometry. No hard 4–8px rects.

```
--radius-sm:      12px   small containers, chips (when not pill)
--radius-md:      16px   cards, fields, menus
--radius-lg:      24px   hero cards, sheets, large containers
--radius-xl:      28px   group outer corners (connected list)
--radius-pill:    999px  pills: primary button, single-tag, tab active, search
--radius-circle:  50%    icon containers, avatars, FAB
--radius-inner:    6px   connected-list inner corners (near seam)
```

Rules:
- Cards default `md` (16); hero/featured `lg` (24).
- Primary button = `pill`; secondary = `md` or `pill` (consistent per screen, not mixed).
- Icon button container = `circle`; toolbar group = `pill` container.
- Connected list: outer `xl` (28), inner `inner` (6), gap 2 — reads as one panel split into segments.
- Never introduce 8/10 radii — breaks scale.

---

## Typography System

Sans with clear hierarchy via size + weight + muted color. No serif observed.

Type scale (ratio ~1.20 comfortable; display jumps to 1.25):

```
--font-display:   32 / 36  weight 700  tracking -0.02em  (hero, empty state)
--font-headline:  24 / 32  weight 600  tracking -0.01em  (section heading)
--font-title:     18 / 26  weight 600  tracking  0        (card title, app bar)
--font-body:      16 / 24  weight 400  tracking  0        (reading, list)
--font-body-sm:   14 / 20  weight 400  tracking  0.01em   (secondary, captions within body)
--font-label:     12 / 16  weight 500  tracking  0.06em  uppercase  (meta, overline, button label)
--font-label-md:  14 / 20  weight 500  tracking  0.04em  uppercase  (chip, tab label — if not pill)
```

Rules:
- **Hierarchy signal**: size first, then weight, then muted color. Do not rely on color alone.
- **Limit**: at most 3 sizes per screen (e.g., headline + body + label). Display only for hero/empty.
- **Buttons**: `label` (12 uppercase) for pill; `label-md` for large CTA — do not use body size on buttons.
- **Line-height**: display 1.125, headline 1.33, title 1.44, body 1.5, label 1.33.
- **Alignment**: left. Center only for empty/hero. No justified.
- **Muted hierarchy**: body secondary uses `color-muted` (not smaller size).

---

## Color System

Relationships over hex dump. Warm, desaturated field + one accent.

```
--color-bg:               #faf9f6  warm paper — page background (NEVER pure white)
--color-surface:           #ffffff white — elevated card / sheet
--color-surface-tinted:    #f1f1f0  tinted surface / subtle group bg
--color-surface-elevated:  #ffffff + hairline border  (not shadow)
--color-surface-inverted:  #121211 near-black (for dark hero/media variant only)

--color-text-primary:      #121211  warm near-black (primary text, headings)
--color-text-secondary:    #5b5a5c  mid muted (secondary body)
--color-text-muted:        #9c9d9b  light muted (meta, placeholder)  — ensure ≥4.5:1 on bg? Use secondary for body; muted only for 12px label/caption on large.
--color-border:            #e8e8e8  hairline (1px)  — or #edecef on tinted
--color-border-strong:     #d7d7d7  when separation needed on white

--color-primary:           #f86746  coral (or #e86d26 warm orange) — ONE primary accent per screen
--color-on-primary:        #ffffff
--color-primary-muted:     #f8674620  12% tint for subtle fill / selection
--color-accent-alt:        #8c8af3  periwinkle — alternative accent for specific contexts (media, dark hero) — never alongside primary.

--color-success:            #708368  muted sage (desaturated, from refs)
--color-warning:            #deb270  warm sand
```

Roles:
- **Background hierarchy**: `bg` (paper) < `surface-tinted` (group) < `surface` (card) < `inverted` (hero).
- **Text hierarchy**: primary (high) > secondary (mid) > muted (low) — use opacity/tint, not grey soup.
- **Primary**: used for one CTA or hero accent per screen. Not for borders, not for every icon. Secondary actions use `surface-tinted` + `text-primary`.
- **Accent alt**: for dark/media contexts only.
- **Contrast**: text-primary on bg ≈ 16:1. Text-muted on bg ≈ 3.5:1 → do not use muted for body; use secondary (≥7:1). Verify with tooling.
- **Gradients**: none in core language. Media may use subtle warm tint, not brand gradient.
- **Temperature**: warm neutrals as base; cool tints only as card-local variant.

---

## Surface System

```
--elevation-0:  flat — bg or tinted, no border/shadow
--elevation-1:  card — surface (#fff) + 1px hairline border (#e8e8e8) + y=1 blur=8 alpha=0.04 (subtle)
--elevation-2:  raised — surface + border + y=4 blur=16 alpha=0.08
--elevation-3:  modal — surface + y=12 blur=32 alpha=0.12 + scrim #121211 40%
```

Hierarchy: most content lives at 0–1. Elevation 2 only for floating toolbar/FAB. Elevation 3 only for dialog/sheet/modal.

Other surface rules:
- **Opacity**: paper is opaque. Tint is 100% solid — no translucent page bg. Blur only on floating nav/sheet scrim if needed.
- **Borders**: hairline 1px is the primary separation — not shadow. Inner dividers use border color at 1px. No 2px borders except focus.
- **Scrim**: modal `#121211` at 40% (light scrim). No blur by default.

---

## Icon System

```
--icon-size-sm:  16px  inline, label-adjacent
--icon-size-md:  20px  buttons, list trailing (default)
--icon-size-lg:  24px  app bar, hero, empty state
```

- **Style**: stroke/outlined, regular weight (≈1.6 stroke), rounded caps. No fill/duotone except selected nav.
- **Weight**: uniform — don't mix light + bold.
- **Container**: bare on tinted; circle (40–48) with `surface-tinted` bg when on white.
- **Alignment**: optical center; 8px gap to text.

---

## Motion System

Insufficient motion evidence in static frames — system is deliberately minimal:

```
--motion-duration-fast:    150ms  press, icon morph
--motion-duration-normal:  240ms  sheet, nav, card expand
--motion-duration-slow:    360ms  hero / page
--motion-easing-standard:  cubic-bezier(0.2, 0, 0, 1)  (emphasizedDecelerate)
--motion-easing-spring:    spring(damping 0.78, stiffness 340)  (press, draggable)
--motion-easing-emphasized: cubic-bezier(0.05, 0.7, 0.1, 1)
```

- Entering: `fade + translateY 8→0` 220ms standard.
- Press: `scale 0.98` or `elevation 1→0` 120ms spring — pick one, use everywhere.
- No shared-element observed — do not claim; note "no evidence, avoid inventing."
- Focus: `outline 2px var(--color-primary) / 40%` offset 2px — always.

---

## Token Files (recommended)

- Web: `tokens.css` (+ `tailwind.config` extend) or `design-tokens.json` (Style Dictionary)
- Android: `ui/theme/Tokens.kt` + `Theme.kt` (colorScheme/typography/shapes)
- iOS: `DesignTokens.swift`
