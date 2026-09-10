# Component Language

> Coherence rule: all components share the same spacing ladder, radius scale, type scale, and color roles. No per-component inventions.

Template per component: Purpose | Visual structure | Shape | Spacing | Typography | Color | Surface | Elevation | Interaction | States | Variants | Anti-patterns

---

### App bar

- **Purpose**: Screen identity + primary navigation; recedes behind content.
- **Structure**: 56h bar, title left, actions trailing. No bottom divider by default — relies on scroll elevation.
- **Shape**: none (full-width paper). Floating variant = pill (see nav).
- **Spacing**: 16 horizontal padding, 8 between actions.
- **Typography**: `title` 18/600.
- **Color**: transparent/paper (`--color-bg`) at rest; on scroll → `surface` + hairline border.
- **Surface**: flat (0). On scroll → elevation 1.
- **Elevation**: 0→1 on scroll.
- **Interaction**: title not interactive; actions are icon buttons (circle).
- **States**: default / scrolled.
- **Variants**: default, floating pill (for media screens).
- **Anti-patterns**: opaque block that competes with hero; heavy shadow; centered title that breaks hierarchy.

### Navigation

- **Purpose**: Primary wayfinding; minimal chrome.
- **Structure**: Bottom pill nav (phone) / rail (tablet+). 3–5 items, icon+label (pill nav) or icon-only (rail).
- **Shape**: bottom pill = `pill` container (radius pill) with 4 gap inside; item active = pill fill.
- **Spacing**: nav padding 8, item gap 4, item padding 12×8.
- **Typography**: `label` 12 uppercase for item labels.
- **Color**: container `surface-tinted`; active `primary`/`text-primary` fill + on-color label; inactive `muted`.
- **Surface**: tinted (not white).
- **Elevation**: 1 (card) floating over bg.
- **Interaction**: tap → pill morph, 180ms spring.
- **States**: active / inactive / pressed.
- **Variants**: bottom pill (phone), rail (tablet+).
- **Anti-patterns**: many nav patterns at once; underline tabs as nav; not floating when hero present.

### Tabs

- **Purpose**: Content switching within a screen.
- **Structure**: Segmented container with sliding thumb.
- **Shape**: container `pill`, thumb `pill`.
- **Spacing**: container 4 inner padding, thumb inset.
- **Typography**: `label-md` 14/500.
- **Color**: container `surface-tinted`, thumb `surface` + shadow 1, active `text-primary`, inactive `muted`.
- **Surface**: tinted container, white thumb.
- **Elevation**: 0 container, 1 thumb.
- **Interaction**: slide thumb spring 260ms.
- **Anti-patterns**: underline tabs (different language); per-tab random widths.

### Buttons

- **Purpose**: Action hierarchy — one primary per screen.
- **Structure**: text centered, optional leading icon 16.
- **Shape**: primary = `pill`; secondary/ghost = `pill` (uniform per screen). Height 44–48.
- **Spacing**: horizontal 20–24, vertical 12, icon gap 8.
- **Typography**: `label` 12 uppercase 0.06em (or 14/500 if larger CTAs).
- **Color**: primary = `primary` fill + `on-primary`; secondary = `surface-tinted` + `text-primary`; ghost = transparent + `text-primary`.
- **Surface**: solid fill (no border except ghost uses hairline).
- **Elevation**: 0 (flat) — no shadow.
- **Interaction**: press `scale 0.98` 120ms spring + 8% overlay.
- **States**: default / hover / pressed / disabled (40% opacity + no press) / loading (spinner inline).
- **Variants**: primary, secondary, ghost, icon-only (circle 40–48).
- **Anti-patterns**: many primaries per screen; 8px rounded rect mixed with pills; hard drop shadow.

### Icon buttons / FAB

- **Icon button**: circle 40–48, bare or `surface-tinted` bg on white. Press same as buttons.
- **FAB**: circle or squircle (24 radius) 56, `primary` fill, trailing bottom. Only for creation — not a second primary.

### Cards

- **Purpose**: Content grouping when proximity insufficient.
- **Structure**: media top (optional, ratio 16:9 or 1:1) + body (padding 16).
- **Shape**: `md` (16) default; `lg` (24) hero.
- **Spacing**: padding 16, gap 8 within, grid gap 16.
- **Typography**: title `title`, body `body-sm`, meta `label`.
- **Color**: `surface` (#fff) + hairline border; on tinted bg may be `surface` to lift.
- **Surface**: solid, not tinted.
- **Elevation**: 1 (border) — not shadow.
- **Interaction**: press → border darkens + `scale 0.99` or elevation 0 (pick one).
- **Anti-patterns**: per-row Card for list rows; shadow instead of border; inconsistent radii.

### Lists

- **Purpose**: Sequential content (settings, messages, tracks).
- **Structure**: row 56–64h, leading (icon/avatar 40 circle), content (title + subtitle), trailing (chevron/meta).
- **Shape**: rows not individually carded by default. Grouped variant uses connected panel: see below.
- **Spacing**: row padding 16, inner gap 12, divider 1px `border` with 16 inset if used. Grouped panel gap 2, group outer `xl` 28.
- **Typography**: title `body` 16/400, subtitle `body-sm` 14 muted, meta `label`.
- **Color**: bg `surface-tinted` or `surface` depending on page; dividers `border`; active tint `primary-muted`.
- **Surface**: flat; grouped panel `surface` + 0 elevation (reads as one panel).
- **Interaction**: full-row hit target, press tint 6%.
- **Variants**: plain (dividers), grouped connected panel (preferred for settings/menus).
- **Anti-patterns**: each row in its own elevated Card; inconsistent row heights; dividers + cards together (pick one).

**Connected panel (preferred)** — each row is `Card` with `0dp` elevation, `surface` fill, `segmentedShape(index,count)` (28 outer / 6 inner), spaced 2. See `segmented-connect-list` skill.

### Chips / Tags

- **Purpose**: Filters, tags, single-select.
- **Shape**: `pill`.
- **Spacing**: padding 12×8, group gap 8.
- **Typography**: `label-md` 14/500 or `label` 12 uppercase.
- **Color**: default `surface-tinted` + `text-secondary`; selected `primary` or `text-primary` fill.
- **Surface**: tinted.
- **Anti-patterns**: rounded-rect chips mixed with pill buttons.

### Segmented controls

- Same as tabs — container `surface-tinted` pill, thumb white pill, spring slide.

### Text fields / Search

- **Field**: `md` (16) radius, filled (`surface-tinted`) not outlined. Padding 12×16. Label `label` 12 muted above; placeholder `body` muted. Focus → border `border-strong` + subtle tint change, not glow.
- **Search**: `pill`, filled `surface-tinted` (or `surface` on bg), leading search icon 20, 44h. Same focus.
- **States**: default / focused / error (muted red tint + message `body-sm`) / disabled.
- **Anti-patterns**: outlined fields with heavy borders; mixed field + search shapes per screen.

### Dialogs / Bottom sheets

- **Dialog**: `lg` (24) radius, `surface`, centered, max-width 520. Padding 24. Actions trailing (ghost + primary).
- **Sheet**: `lg` top radius 24, `surface`, handle 36×4 `border-strong` centered top 12. Scrim `inverted 40%`.
- **Elevation**: 3.
- **Anti-patterns**: small 8 radius dialogs; no scrim; mixed dialog/sheet radius scale.

### Menus

- `md` radius, `surface` + border + elevation 2, item height 44–48, `body` 14, icon 20 leading. Item press tint 6%.

### Media controls

- Artwork square or 16:9, `md` radius. Progress: track 4h `border`, fill `primary`, thumb 16 circle. Play/pause circle 48 `primary`.

### Switches / Sliders / Progress

- **Switch**: track 28×16 `pill`, thumb 16 circle; off `border-strong` + `surface`, on `primary`.
- **Slider**: track 4, active `primary`, inactive `border`, thumb 16 circle `primary` with 24 hit area.
- **Progress**: linear 4 `primary` on `border` track; circular 3 stroke `primary` (no wavy unless loading hero).

### Empty / Loading / Banner

- Empty: illustration subtle, headline `headline` 24/600, body `body` 16 muted, CTA primary pill below — centered, 48 gap to illustration.
- Loading: spinner `primary` 24 stroke 3, no decorative background.
- Banner: `surface-tinted` + `md` radius + hairline, not full-width colored bar. Icon 20 leading, action trailing ghost.
