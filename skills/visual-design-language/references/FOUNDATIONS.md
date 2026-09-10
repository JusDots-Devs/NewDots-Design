# Foundations — Tokens, Analysis, Synthesis

## Discovery

### Directory resolution
Search order: `design-inspiration/`, `design_inspiration/`, `inspiration/`, `references/`, `./` (if >3 images). Prefer the dir with most `*.png/jpg/jpeg/webp/avif`. If tie, ask user. Never silently pick.

### Supported formats
`png, jpg, jpeg, webp, avif` — read natively. `heic/heif` — flag for conversion (`sips -s format jpeg` or `magick`). `pdf` — extract first page as png.

### Inventory fields per image
```
filename, W×H, aspect ratio, format, bytes, md5, pHash (8×8 DCT), quantized palette (5 colors), luminance histogram (for light/dark bias)
```

### Duplicate detection
- Identical MD5 → exact duplicate.
- pHash Hamming ≤ 6 → near-duplicate (crop/resize/compression variant).
Report table; default keep both but note in synthesis to avoid double-weighting.

### Output
`/tmp/vdl-inventory.json` + markdown table. This is the source of truth for counts.

---

## Analysis (per-image)

Use this checklist per image. Emit bullets, not paragraphs.

### Layout
- Composition: single-column / grid / asymmetric / editorial / dashboard?
- Alignment: flush-left / centered / mixed? Baseline grid visible?
- Margins: tight / generous / bleed? Estimate px relative to viewport.
- Whitespace: airy / balanced / dense? Content-to-chrome ratio.
- Grouping: proximity / enclosure / rule lines?
- Hierarchy: size / weight / color / position cues?
- Proportions: hero ratio, card aspect, golden vs square?
- Focal points: 1 hero vs multi-focal vs uniform.

### Geometry
- Corner radius: sharp (0–4) / soft (8–16) / pill (999) / squircle (continuous) / mixed? Note per-component variation.
- Shape language: rectilinear / organic / brutalist / neumorphic?
- Container heights: ~44 / 48 / 56 / 64 pattern?
- Stroke vs fill containers?

### Typography
- Display/headline/title/body/label — estimate scale (e.g., 32/24/18/16/12) and weight (400/500/700).
- Line-height: tight (1.1) / comfortable (1.4–1.6) / loose?
- Tracking: tight / normal / wide? Uppercase labels?
- Alignment: left / center / justified?
- Hierarchy signal: size vs weight vs color vs case?

### Color
- Background: warm white / cool white / dark / tinted?
- Surface: white / tinted / translucent?
- Primary: where used (button / accent / text)? Saturation?
- Accent behavior: single accent vs multi-accent vs monochrome?
- Muted text: opacity / tint?
- Contrast: high / mid / low? WCAG estimate.
- Gradients: none / subtle / bold? Direction?
- Temperature: warm / cool / neutral?

### Surfaces
- Flat / layered / glass / bordered / shadowed?
- Elevation: 0 / 1 / 2+ levels? Shadow softness/spread?
- Borders: none / hairline / strong / inner?
- Blur: none / backdrop-blur / frosted?
- Depth: flat vs z-axis storytelling?

### Components (present? treatment?)
App bar, nav, tabs, buttons, icon buttons, FAB, cards, lists, chips, segmented controls, text fields, search, dialogs, bottom sheets, menus, media controls, switches, sliders, progress, banners, empty/loading. Mark `—` if not visible.

### Iconography
- Stroke (outlined) / fill (solid) / duotone?
- Weight: light / regular / bold?
- Size: 16 / 20 / 24?
- Container: bare / circle / squircle?
- Consistency: uniform vs mixed?

### Motion (only if evidence)
Look for: shared-element hints (hero image → detail), spring overshoot in mockup sequence, staggered list, morphing FAB, sliding sheets, parallax. If single static frame → "insufficient evidence."

---

## Synthesis

### Frequency thresholds
- **Recurring** ≥60% of images
- **Common** 30–60%
- **Rare** <30% → candidate outlier

### Strong signals
Rank by: frequency × visual weight (how much it defines the "feel"). Top 3–5 drive the DNA statement.

### Secondary signals
Recurring but low weight (e.g., "all use 1px divider" — supports but doesn't define).

### Outliers
Classify:
- **Legitimate variation** — coherent alternative within same language (e.g., dark mode variant) → keep as variant.
- **Context-specific** — pattern valid only in one screen type (e.g., onboarding illustration style) → scope it.
- **Noise** — incidental, off-brand → exclude from token derivation.

### Conflicts
Non-exhaustive: rounded vs sharp, dense vs airy, vibrant vs muted, flat vs elevated, centered vs flush, serif vs sans. Do not average → pick the side with stronger signal + better coherence. Document the rejected alternative.

---

## Tokens

### Naming
Use platform-agnostic names mapped to implementation:
```
--space-1  .. --space-8
--radius-sm/md/lg/xl/pill/circle
--font-display/headline/title/body/label  (+ size/weight/line-height/letter-spacing)
--color-bg/surface/surface-elevated/primary/on-primary/primary-container/accent/muted/border/shadow
--elevation-0/1/2/3
--motion-duration-fast/normal/slow + --motion-easing-standard/emphasized/spring
--icon-size-sm/md/lg
```

### Value guidance
- **Spacing**: base unit 4 or 8. Scale example (if refs generous): 4, 8, 12, 16, 24, 32, 48, 64. If refs dense: 4, 8, 12, 16, 20, 24, 32, 40. Pick one ladder; do not mix.
- **Radii**: if refs soft → 8/12/16/24/pill; if refs sharp → 0/4/8/12; if squircle → continuous (iOS-style `~28` or `superellipse`).
- **Typography**: infer scale ratio. Calm → 1.125; editorial → 1.25–1.33; dramatic → 1.5 for display only.
- **Color**: always roles + relationships. Never a flat hex list.
- **Elevation**: 0 = flat, 1 = subtle (y=1 blur=8 alpha=0.08), 2 = card (y=4 blur=16), 3 = modal (y=12 blur=32). Map to shadow tokens or `surfaceContainer` hierarchy if M3.

### Where tokens live
- Web: `tokens.css` / `tailwind.config`
- Android: `Theme.kt` + `tokens.xml` or Compose `CompositionLocal`
- iOS: `DesignTokens.swift`
- Cross-platform: `design-tokens.json` (Style Dictionary)
