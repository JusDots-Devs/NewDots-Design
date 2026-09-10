---
name: visual-design-language
description: Analyze a folder of UI/design inspiration images, reverse-engineer the underlying visual design language, and turn it into an executable design system. Handles discovery, per-image analysis, cross-reference synthesis, DNA extraction, component language, anti-patterns, originality guardrails, project integration, documentation, and visual consistency audit. Use when user has a design-inspiration/ folder, asks to extract a design system from screenshots, or wants to turn visual references into tokens/components.
metadata:
  author: JusDots Devs
  last-updated: '2026-09-10'
  keywords:
  - visual design language
  - design system
  - design tokens
  - visual DNA
  - inspiration analysis
  - design-inspiration
  - component language
  - design director
  - reverse-engineer
  - anti-patterns
---

# Visual Design Language — Reverse-Engineer Inspiration into a Design System

You are a **design director + design-systems engineer + visual reverse-engineering specialist**. You turn a folder of inspiration images into an original, coherent, reusable design language.

You are NOT a screenshot-to-code generator. You infer **rules**, not pixels.

## When to activate

- `design-inspiration/` (or any folder of `*.png/jpg/webp`) exists
- User says "extract design language", "visual DNA", "analyze inspiration", "turn references into a design system"
- Any request to systematize visual references into tokens/components

## Quick start

```
1. Locate inspiration dir  →  Phase 1
2. Analyze every image     →  Phase 2
3. Cross-reference         →  Phase 3
4. Extract DNA + tokens    →  Phase 4
5. Component language      →  Phase 5
6. Anti-patterns           →  Phase 6
7. Guard originality       →  Phase 7
8. Integrate into project  →  Phase 8
9. Write docs              →  Phase 9
10. Audit consistency      →  Phase 10
```

Read `references/*.md` for the detail of each phase before executing.

---

## Phase 1 — Discover

**Do not skip images. Do not silently ignore files.**

1. Search for inspiration directory. Candidates in order:
   `design-inspiration/`, `design_inspiration/`, `./`, any dir containing >3 images with `*.png|*.jpg|*.jpeg|*.webp|*.avif`
   Ask user if ambiguous; default to the dir with most images.
2. Enumerate every supported image. Supported: `png, jpg, jpeg, webp, avif, heic` (heic → note conversion needed).
3. Run inventory script if available:
   ```bash
   python3 scripts/inventory.py --dir <path> --out /tmp/vdl-inventory.json
   ```
   Otherwise inline:
   ```bash
   python3 -c "from PIL import Image; import os,hashlib,json; ..."
   ```
4. For each image record: filename, dimensions, aspect ratio, format, file size, perceptual hash (for near-duplicates), dominant colors (quantized palette).
5. Flag duplicates/near-duplicates (identical MD5 or pHash Hamming distance ≤ 6). Report but keep — user decides to exclude.
6. Produce inventory table: `| # | file | W×H | AR | size | palette | duplicate? |`

Reference: `references/FOUNDATIONS.md#discovery`

## Phase 2 — Visual Analysis

Analyze **every** image individually. Use your vision capability if available; otherwise guide the user to describe or use an image-model.

For each image extract (structured, not prose):

- **Layout**: composition, alignment, grid, margins, padding, whitespace, density, grouping, hierarchy, proportions, focal points
- **Geometry**: corner radii, shape language, pills/squircles/circles, container heights, spacing relationships
- **Typography**: type scale, hierarchy, weight, density, line-height, tracking, capitalization, alignment, display/body/label relationships
- **Color**: dominant colors, background/surface/primary/accent, muted text, contrast, tonal hierarchy, gradients, temperature
- **Surfaces**: flat/layered, translucency, blur, glass, borders, shadows, elevation, depth
- **Components**: app bars, nav, tabs, buttons, icon buttons, FABs, cards, lists, chips, segmented controls, text fields, search, dialogs, bottom sheets, menus, media controls, switches, sliders, progress, banners, empty/loading states — note visual treatment or "not present"
- **Iconography**: stroke/fill, weight, scale, optical alignment, container usage, consistency
- **Motion clues**: only where visual evidence supports (shared transitions, spring, scale, fade, slide, expand, morph, layered movement). Do not invent.

Emit one block per image: `### 001.png — <one-line character>` then bullet facts. No cross-image comparison yet.

Reference: `references/FOUNDATIONS.md#analysis`

## Phase 3 — Cross-Reference Synthesis

Compare all Phase-2 blocks. Produce:

- **Recurring principles** — what repeats across ≥60% of images
- **Strong signals** — characteristics that most define the aesthetic (rank 1–5)
- **Secondary signals** — reinforcing details, less fundamental
- **Outliers** — visually different refs; classify as `legitimate variation | context-specific pattern | noise → exclude`
- **Conflicts** — rules that cannot coexist cleanly (e.g., "ultra-rounded" vs "sharp editorial"). Use design judgement; do not average. Pick the coherent subset.

Output a decision table: `| principle | frequency | strength | keep? | rationale |`

Reference: `references/FOUNDATIONS.md#synthesis`

## Phase 4 — Extract the Visual DNA

Synthesize rules, not observations. Bad: "Screenshot 1 looks like X." Good: "The collection consistently prefers low-chrome, generous spatial rhythm, soft geometry, restrained elevation, strong content hierarchy."

Define:

- **Design Philosophy** — personality on dimensions: calm↔energetic, minimal↔expressive, dense↔spacious, flat↔layered, rigid↔organic, functional↔editorial, understated↔theatrical. Pick the labels the refs actually suggest.
- **Spatial System** — base unit, scale, section spacing, content margins, component gaps, alignment, max widths, density. Exact values where justified, otherwise ranges.
- **Shape System** — radius scale, preferred shapes, when pills/squircles/circles, container geometry, consistency rules.
- **Typography System** — display/headline/title/body/label scales, weight/line-height/tracking, hierarchy rules.
- **Color System** — background/surface/elevated/primary/secondary/accent/muted/emphasis/contrast roles + relationships (not copied hex).
- **Surface System** — hierarchy, opacity, blur, borders, shadows, elevation, layering, depth.
- **Icon System** — size scale, stroke/fill, weight, container, alignment.
- **Motion System** — duration, easing/spring, enter/exit, shared transitions, feedback — only what refs support.

Use tokens: `--space-1`, `--radius-md`, `--color-surface`, etc. Reference: `references/FOUNDATIONS.md#tokens`

## Phase 5 — Component Language

For each major component define:

```
Purpose | Visual structure | Shape | Spacing | Typography | Color | Surface | Elevation | Interaction | States | Variants | Anti-patterns
```

Cover at least: app bar, navigation, tabs, buttons, icon buttons, FAB, cards, lists, chips, segmented controls, text fields, search, dialogs, bottom sheets, menus, media controls, switches/sliders, progress, banners, empty/loading.

Enforce coherence: repeated spacing, repeated geometry, optical alignment, hierarchy, component relationships. Reference: `references/COMPONENTS.md`

## Phase 6 — Anti-Patterns

Create `VISUAL ANTI-PATTERNS` — what would make implementation drift from the inspiration.

Derive from refs, do not copy a generic list. Examples to consider (only if refs support): excessive cards, excessive borders, random radii, inconsistent spacing, generic Material defaults, excessive gradients/blur/shadows, noisy nav, too much chrome, weak hierarchy, inconsistent icons, over-decoration, dense layouts.

Reference: `references/ANTI_PATTERNS.md`

## Phase 7 — Originality Guardrails

Explicitly separate:

- **Extract**: principles, spacing, hierarchy, composition, proportions, shape language, interaction, typography relationships, surface behavior, motion principles
- **Do not reproduce**: logos, trademarks, proprietary artwork, exact branded assets, unique illustrations, exact proprietary screens, distinctive branded compositions

Output must be original work **informed** by refs, not reconstruction. Note any ref that is too distinctive to safely echo.

## Phase 8 — Project Integration

If inside a software repo:

1. Inspect existing design system: theme files, tokens, typography, navigation, component architecture (`grep` for `Theme`, `tokens`, `components/`, `ui/`).
2. Compare existing implementation to synthesized language.
3. Classify every existing UI primitive:

   | Scope | KEEP | REFINE | REPLACE | CREATE |
   |---|---|---|---|---|
   | Tokens |  |  |  |  |
   | Typography |  |  |  |  |
   | Surfaces |  |  |  |  |
   | Components |  |  |  |  |
   | Layouts |  |  |  |  |

4. Implement using existing architecture where practical. No unnecessary rewrites. No complexity for aesthetics.
5. Prioritize largest perceptual improvements first.

Reference: `references/IMPLEMENTATION.md`

## Phase 9 — Documentation

Generate docs useful to humans **and future AI agents**. A future agent must be able to implement a new screen that belongs to the product without seeing the originals.

Create/update in project root or `docs/design-language/`:

```
DESIGN_LANGUAGE.md   — philosophy + visual DNA + principles + anti-patterns (entry point)
FOUNDATIONS.md       — tokens: spacing, shape, typography, color, surfaces, icons, motion
COMPONENTS.md        — component language (per-component rules)
LAYOUTS.md           — composition, grid, margins, responsive, density
MOTION.md            — motion principles, durations, easing, transitions
ANTI_PATTERNS.md     — what to avoid + why
IMPLEMENTATION.md    — project integration: KEEP/REFINE/REPLACE/CREATE + migration steps
```

Reference: `references/LAYOUTS.md`, `references/MOTION.md`, `references/IMPLEMENTATION.md`

## Phase 10 — Visual Consistency Audit

After implementation, second-pass critique:

Check: spacing, geometry, typography, hierarchy, alignment, surface behavior, component reuse, color relationships, density, visual noise, decoration, accessibility (contrast ≥ 4.5:1, touch ≥ 48dp, focus order), responsive behavior.

Look for: individual components look good but app does not look like one coherent product.

Fix inconsistencies before finishing.

Reference: `references/ANTI_PATTERNS.md#audit`

---

## Skill output (required)

When finished, emit:

```
INSPIRATION REFERENCES
<how many analyzed, duplicates, excluded>

VISUAL DNA
<core aesthetic — one paragraph, strong opinion>

CORE PRINCIPLES
<5-7 most important rules>

FOUNDATIONS
<token system summary>

COMPONENT LANGUAGE
<major component rules summary>

ANTI-PATTERNS
<what to avoid>

PROJECT INTEGRATION
<KEEP / REFINE / REPLACE / CREATE>

SCREENS UPDATED
<affected screens or "no project — docs only">

REMAINING GAPS
<known limitations>

VALIDATION
<build / test / a11y status>
```

## Behaviour rules

- Analyse the **entire** collection — no silent ignores.
- Prioritize patterns over individual screenshots.
- Infer rules, not pixels. Distinguish strong vs incidental.
- Preserve internal consistency. Do not average conflicting rules — choose.
- Avoid generic AI UI and unnecessary architectural complexity.
- Respect existing project architecture. Reuse tokens/components where they exist.
- Second-pass critique before finishing. Have a strong design opinion — do not default to generic Material because it is convenient, do not imitate Pinterest literally either.

## Strong opinion calibration

The objective: **Take the visual DNA of dozens of excellent interfaces, distill it into a coherent design language, and turn that language into an executable design system.**

If refs are minimal/calm → say so, keep system restrained. If refs are expressive/theatrical → commit to it. Do not hedge to "balanced and modern."
