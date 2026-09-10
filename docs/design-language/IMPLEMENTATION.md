# Implementation — From Language to Code

## Project state (2026-09-10)

This folder (`NewDots_DesignLang`) is currently a **design-inspiration collection only** — 16 images, no app code. Therefore there is no existing design system to KEEP/REFINE/REPLACE. This doc is the build plan for when the language is applied.

If you are an AI agent implementing a new screen, follow Foundations → Components → Layouts → this plan.

---

## Recommended stack (agnostic)

| Concern | Web | Android | iOS |
|---------|-----|---------|-----|
| Tokens | `docs/design-language/tokens.css` or `design-tokens.json` | `ui/theme/Tokens.kt` | `DesignTokens.swift` |
| Theme | `tailwind.config` extend + `globals.css` | `Theme.kt` (colorScheme/typography/shapes) | `Theme.swift` |
| Components | `src/components/` | `ui/components/` | `Components/` |
| Layouts | `src/layouts/` or page composition | `ui/layout/` / `NavigationSuiteScaffold` | `Layouts/` |

For this repo (no code yet), start with tokens + component primitives and one example screen.

---

## Classification (no existing system → all CREATE)

| Area | Action | Notes |
|------|--------|-------|
| Tokens (spacing, radii, colors, type, elevation, motion) | **CREATE** | From `FOUNDATIONS.md` |
| Typography scale | CREATE | 32/24/18/16/14/12 ladder |
| Surfaces / elevation | CREATE | 0 border-flat → 3 modal |
| Icons | CREATE | Outlined 20/24, circle container |
| App bar / nav | CREATE | Paper bar + bottom pill nav |
| Buttons / FAB | CREATE | Pill primary, tinted secondary |
| Cards / lists | CREATE | `md` cards + connected panel lists |
| Fields / search | CREATE | Filled 16 + pill search |
| Dialogs / sheets | CREATE | `lg` 24, scrim 40% |
| Layouts / grid | CREATE | Single-column editorial, max-widths |
| Motion | CREATE | 150/240/360 + standard/spring |

When integrating into an existing repo, reclassify using the KEEP/REFINE/REPLACE table in `references/IMPLEMENTATION.md`.

---

## Priority order (largest perceptual win first)

1. **Tokens** (`--color-bg`, `--color-surface`, spacing, radii) — propagate everywhere.
2. **Typography** — hierarchy is the fastest way to belong vs generic.
3. **Surfaces / elevation** — paper vs white + hairline border sets the feel.
4. **App bar + nav** — chrome level is instantly visible.
5. **Lists / cards** — most screen real-estate; adopt connected panel early.
6. **Buttons / controls** — pill + muted hierarchy.
7. **Details** — icons, empty states, motion.

## Token file starters

### Web — `tokens.css`
```css
:root {
  --color-bg: #faf9f6;
  --color-surface: #ffffff;
  --color-surface-tinted: #f1f1f0;
  --color-text-primary: #121211;
  --color-text-muted: #9c9d9b;
  --color-border: #e8e8e8;
  --color-primary: #f86746;
  --space-4: 16px; --space-5: 24px;
  --radius-md: 16px; --radius-lg: 24px; --radius-pill: 999px;
}
```

### Android — `Tokens.kt`
```kotlin
val Space4 = 16.dp; val RadiusMd = 16.dp; val RadiusLg = 24.dp
val SurfaceBg = Color(0xFFFAF9F6); val Primary = Color(0xFFF86746)
```

---

## Validation

- Build: not applicable (no code yet). When code exists, verify `assembleDebug` / `npm run build`.
- Tests: snapshot/preview tests for 16/24/720 widths.
- A11y: muted text not used for body; touch ≥48; focus visible; contrast checked.

---

## If invoked inside an existing repo

Follow `references/IMPLEMENTATION.md`:
1. Inspect theme/tokens/components/nav.
2. Fill KEEP/REFINE/REPLACE/CREATE table.
3. Implement in priority order, reusing architecture.
4. Validate build/tests/a11y.
5. Run visual consistency audit (Phase 10).
