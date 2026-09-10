# Implementation — Project Integration

## Inspect existing project

Search order:

```bash
# Theme / tokens
grep -r "Theme\|colorScheme\|Typography\|Shapes\|tokens" --include="*.kt" --include="*.css" --include="*.json" . 2>/dev/null | head -20
# Components
ls src/components/ app/src/main/java/*/ui/ lib/design/ 2>/dev/null | head -20
# Navigation
grep -r "NavHost\|Navigation\|Router" --include="*.kt" --include="*.tsx" . 2>/dev/null | head -10
```

Identify:
- Current token location (`Theme.kt`, `tokens.css`, `design-tokens.json`, `tailwind.config`)
- Typography definition
- Component library (custom vs M3 vs Tailwind vs etc.)
- Navigation architecture

## Classify

For each area fill KEEP / REFINE / REPLACE / CREATE:

| Area | KEEP (already matches) | REFINE (tweak values) | REPLACE (wrong language) | CREATE (missing) |
|---|---|---|---|---|
| Tokens (spacing, radii, colors) |  |  |  |  |
| Typography scale |  |  |  |  |
| Surfaces / elevation |  |  |  |  |
| Icons |  |  |  |  |
| App bar / nav |  |  |  |  |
| Buttons / FAB |  |  |  |  |
| Cards / lists |  |  |  |  |
| Fields / search |  |  |  |  |
| Dialogs / sheets |  |  |  |  |
| Layouts / grid |  |  |  |  |
| Motion |  |  |  |  |

**Rules:**
- KEEP: already coherent with refs — do not touch.
- REFINE: structure is right, values are off (e.g., radius 8→16, spacing 8/12/16→4/8/16/24).
- REPLACE: component exists but language is wrong (e.g., heavily elevated cards in a flat language) — rewrite.
- CREATE: missing primitive needed by refs (e.g., no segmented control, no pill nav).

## Apply

### Priority order (largest perceptual win first)
1. Tokens (spacing, color roles, radii) — changes propagate
2. Typography (scale + hierarchy)
3. Surfaces / elevation (flat vs layered)
4. App bar + navigation (chrome level)
5. Lists / cards (highest screen real-estate)
6. Buttons / controls
7. Details (icons, motion, empty states)

### How to implement per platform

**Android (Compose + M3)**
```
ui/theme/Theme.kt       → colorScheme, typography, shapes
ui/theme/Tokens.kt      → spacing, radii, elevation tokens
ui/components/*.kt      → reusable components using tokens
```
Prefer `MaterialTheme.colorScheme` roles + `ButtonDefaults.shapes()` style morph if expressive. Do not hard-code hex in composables.

**Web (Tailwind / CSS)**
```
tokens.css              → @theme or :root vars
components/*.tsx        → components consuming tokens
tailwind.config         → spacing, radius, fontSize extensions
```
Use `var(--radius-md)` etc., not `rounded-[10px]`.

**iOS (SwiftUI)**
```
DesignTokens.swift      → tokens
Components/*.swift      → views
```

### Constraints

- Reuse existing architecture — do not rewrite nav or state for aesthetics.
- Do not add dependencies for what tokens can do.
- Fewest files changed. Shortest diff that makes the screen belong.

## Validation

After changes:

```bash
# Build
./gradlew assembleDebug  # or npm run build / xcodebuild
# Tests
./gradlew test  # or npm test
# A11y quick check
# - Contrast: check muted text ≥4.5:1
# - Touch: 48dp min
# - Focus order: logical
```

Report `VALIDATION` block even if build not run ("not verified — no build tool detected") rather than omitting.

## When no project exists

If invoked outside a repo (e.g., bare `design-inspiration/` folder like `NewDots_DesignLang`), skip classification and emit docs only:

```
PROJECT INTEGRATION
No project detected — docs only. Tokens and components are specified for future implementation.
```

Still produce `IMPLEMENTATION.md` with recommended stack and token file locations.
