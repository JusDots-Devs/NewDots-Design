# Component Language

Each component needs a **rule**, not a description. Use the spec template below. Keep rules coherent across components (same spacing ladder, same radius language, same type scale).

## Spec template

```
### <Component>
**Purpose**: one line — what it does in this language.
**Visual structure**: anatomy (container, content, affordance).
**Shape**: radius / pill / circle / squircle; responsive variant.
**Spacing**: internal padding, gap, external margin (token refs).
**Typography**: role + weight + case (e.g., labelMd 500 uppercase 0.06em).
**Color**: container / content / border / state overlay (role refs).
**Surface**: flat / elevated / translucent + elevation level.
**Elevation**: 0/1/2/3 + shadow/border treatment.
**Interaction**: press / hover / focus / drag affordance.
**States**: default / hover / pressed / focused / disabled / selected / loading / empty.
**Variants**: primary / secondary / ghost / etc. (only if refs support).
**Anti-patterns**: what breaks this component in this language.
```

## Core components — rules to set per language

### App bar
- Chrome level: invisible / tinted / elevated? In refs with low chrome, app bar is often transparent or `surface` with no divider.
- Title hierarchy: display vs headline vs title?
- Action treatment: icon-only vs text vs pill?
- Scroll behavior: collapsing / sticky / fading?

### Navigation
- Pattern: bottom bar / rail / drawer / tabs / floating toolbar?
- Shape: pill nav vs flat vs segmented?
- Active state: fill vs tint vs indicator bar vs pill?
- Density: icon+label vs icon-only?

### Tabs
- Underline vs pill vs segmented container?
- Active vs inactive weight/color?
- Scrollable vs fixed?

### Buttons
- Hierarchy: 1 primary per screen? Ghost vs filled usage?
- Shape: pill for primary, rounded rect for secondary — or uniform?
- Height: 44 / 48 / 56?
- Typography: label vs body?
- Elevation: flat vs shadow on primary only?

### Icon buttons
- Container: bare / circle / squircle? When each?
- Size: 40 / 48?
- Background: transparent vs surface vs tinted?

### FAB
- Shape: circle vs squircle vs extended pill?
- Placement: trailing bottom vs centered vs inline?
- When to use vs primary button? (FAB is for primary creation, not every CTA.)

### Cards
- Surface: white vs tinted vs bordered vs elevated?
- Radius: same as containers or larger (hero)?
- Padding: 12 / 16 / 20?
- Press: scale vs elevation vs tint?

### Lists
- Row height, divider style, leading/trailing treatment, selection.
- Connected vs separated (see `segmented-connect-list` skill for connected panel pattern).

### Chips / Tags
- Shape: pill is default; when to use rounded rect?
- Fill vs outline vs tinted?
- Icon / avatar / close affordance?

### Segmented controls
- Container shape, thumb shape, active tint, animation (slide vs fade).

### Text fields / Search
- Filled vs outlined vs underline?
- Radius: pill search vs rounded field?
- Placeholder vs label behavior?
- Focus: border vs glow vs fill change?

### Dialogs / Bottom sheets
- Radius: 16 / 24 / 28? Full-width vs centered?
- Scrim: dim vs blur?
- Action placement: trailing vs stacked?

### Menus
- Surface, radius, elevation, item height, icon usage.

### Media controls
- Progress treatment, play/pause shape, artwork ratio.

### Switches / Sliders / Progress
- Track vs thumb geometry, active color, animation.

### Banners / Empty / Loading
- Illustration style, copy hierarchy, CTA placement.

---

## Coherence checks (apply after drafting all components)

- [ ] All components use same spacing ladder (no one-off `13px`).
- [ ] Radii use same scale (no random `10px` among `8/16/24`).
- [ ] Typography roles consistent (buttons always same label style).
- [ ] Icon size/weight uniform.
- [ ] Elevation levels make sense as a stack (no component at elevation 3 that should be 1).
- [ ] Color roles consistent (primary means same thing everywhere).
- [ ] Press/hover/focus treatment is one language, not per-component invention.

## Platform mapping

| Language token | Android (Compose) | Web (CSS) | iOS (SwiftUI) |
|---|---|---|---|
| `--radius-md` | `RoundedCornerShape(16.dp)` | `border-radius: 16px` | `.cornerRadius(16)` / `ContinuousRoundedRectangle` |
| `--space-4` | `16.dp` | `1rem` | `16` |
| `--color-primary` | `colorScheme.primary` | `var(--color-primary)` | `Color.primary` |
| `--elevation-1` | `surfaceContainer + 1.dp shadow` | `box-shadow: ...` | `.shadow(...)` |

Prefer project conventions over this table when integrating (Phase 8).
