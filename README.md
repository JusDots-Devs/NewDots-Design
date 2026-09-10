<div align="center">

# NewDots Design — Visual Design Language

### Turn any folder of UI inspiration into a coherent design system

*Your agent, now a design director + systems engineer.*

[![Version](https://img.shields.io/badge/version-1.0.0-7c4dff?style=flat-square)](https://github.com/JusDots-Devs/NewDots-Design/releases/tag/v1.0.0)
[![License](https://img.shields.io/badge/License-Apache_2.0-4285f4?style=flat-square)](LICENSE)
[![Design](https://img.shields.io/badge/design--language-tokens_+_components_-ff7043?style=flat-square)](#)
[![Skills](https://img.shields.io/badge/skills-OpenCode_+_Claude_+_Cursor-ffab00?style=flat-square)](https://skills.sh)

**Analyze a `design-inspiration/` folder, reverse-engineer its visual DNA, and ship tokens, components, and layouts — with a single prompt.**

</div>

<div align="center">

```sh
npx https://github.com/JusDots-Devs/NewDots-Design
```

*or* `npx skills add JusDots-Devs/NewDots-Design` · zero deps · 10 seconds · works everywhere

</div>

---

## TL;DR

**The Problem:** Design inspiration is scattered across dozens of screenshots. Teams eyeball spacing, guess colors, and rebuild generic Material/Tailwind defaults. The result is inconsistent spacing, random radii, weak hierarchy, and UIs that feel templated.

**The Solution:** A reusable agent skill that behaves like a **design director + design-systems engineer**. It inspects every image, cross-references the collection, distills *rules* (not pixels), and outputs an executable design language — tokens, components, layouts, motion, anti-patterns — then integrates it into your project's existing architecture.

### Why NewDots Design?

| What you get | Why it matters |
|---|---|
| **Rules, not pixels** — spacing ladders, radius scales, type hierarchy, color relationships | No screenshot-to-code cloning; produces an original system informed by refs |
| **Analyzes every image** — inventory, per-image breakdown, cross-reference synthesis | No silent ignores; duplicates/outliers/conflicts handled explicitly |
| **Opinionated & coherent** — one palette, one geometry, one density | Stops “radius salad” and card soup; product looks like one product |
| **Project-aware** — `KEEP / REFINE / REPLACE / CREATE` against your existing tokens/components | Reuses your architecture; no gratuitous rewrites |
| **Docs a future agent can use** — `DESIGN_LANGUAGE.md` + foundations/components/layouts/motion/anti-patterns/implementation | A new screen can be built without re-seeing the originals |
| **Visual audit built in** — spacing/geometry/typography/hierarchy/a11y second pass | Catches “components look good but product doesn’t” drift |

---

## Quick Example

Ask your agent — the skill activates automatically:

```sh
# In OpenCode / Claude Code / Cursor, just prompt:

> "Analyze the design-inspiration folder and extract the visual design language."

# Agent delivers:
#  Inventory (16 refs) → per-image analysis → synthesis → tokens → components
#  → docs/design-language/{DESIGN_LANGUAGE,FOUNDATIONS,COMPONENTS,LAYOUTS,MOTION,ANTI_PATTERNS,IMPLEMENTATION}.md

> "Apply it to this repo — keep what matches, refine what doesn’t."

# Agent:
#  KEEP tokens that align, REFINE radii 8→16, REPLACE card soup with connected panels,
#  CREATE pill nav + filled fields — using your existing Theme / tokens architecture

> "Audit for visual consistency."

# Agent: spacing ✓ radii ✓ hierarchy ✓ — fixes elevation 2→1 on cards, muted contrast 3.8→4.6
```

<details>
<summary><strong>More prompts the skill handles</strong></summary>

- *“What’s the visual DNA of these screenshots?”* → philosophy + core principles
- *“Generate tokens for this inspiration set — spacing, shape, type, color.”* → `FOUNDATIONS.md`
- *“Build the component language — buttons, cards, lists, nav, fields.”* → `COMPONENTS.md`
- *“Derive anti-patterns so we don’t drift.”* → `ANTI_PATTERNS.md`
- *“Integrate without rewriting our design system.”* → `IMPLEMENTATION.md` with classification
- *“Does this screen belong to the same product?”* → visual consistency audit

</details>

---

## Design Philosophy

The skill does not default to generic Material or imitate Pinterest literally. It **infers and commits**:

```
calm ↔ energetic  ·  minimal ↔ expressive  ·  dense ↔ spacious
flat ↔ layered    ·  rigid ↔ organic      ·  functional ↔ editorial
```

Example output from the included 16-ref set (warm paper minimalism):

> *Quiet, warm, tactile — off-white paper, generous air, soft squircles (16/24/pill), desaturated neutrals + one coral accent, hairline over shadow. Low chrome, type-driven hierarchy.*

Your collection will produce its own language — the skill has a strong opinion per collection, not a house style.

---

## Installation

### 1 · One-liner (fastest)

```sh
npx https://github.com/JusDots-Devs/NewDots-Design
```

Installs to every detected agent (`~/.config/opencode/skills/`, `~/.opencode/skills/`, `~/.claude/skills/`, `~/.cursor/skills/`). Manage later:

```sh
npx https://github.com/JusDots-Devs/NewDots-Design upgrade    # reinstall / update
npx https://github.com/JusDots-Devs/NewDots-Design uninstall  # remove
```

### 2 · skills CLI (recommended for teams)

```sh
npx skills add https://github.com/JusDots-Devs/NewDots-Design          # interactive
npx skills add JusDots-Devs/NewDots-Design -g -a opencode -y           # CI-friendly, global
npx skills add JusDots-Devs/NewDots-Design --skill visual-design-language --list  # preview
```

Browse & discover: [skills.sh](https://skills.sh)

### 3 · Manual

```sh
git clone https://github.com/JusDots-Devs/NewDots-Design
cp -r NewDots-Design/skills/visual-design-language ~/.config/opencode/skills/
# restart your agent
```

**Requirements:** Node ≥18 for installer only; the skill itself is Markdown — zero runtime deps. The helper scripts use Python + Pillow optionally.

---

## Quick Start

```sh
# 1. Install (pick one method above)
npx https://github.com/JusDots-Devs/NewDots-Design

# 2. Restart your agent (OpenCode / Claude Code / Cursor)

# 3. Put screenshots in design-inspiration/ (or point at any image folder)
mkdir -p design-inspiration
# add 5–50 PNG/JPG/WEBP

# 4. Prompt — skill auto-activates on keywords:
#    "design inspiration", "visual DNA", "design system", "tokens", "analyze references"
> Analyze the design-inspiration folder and build the design language

# 5. Integrate / audit
> Apply it to this repo without rewriting the architecture
> Audit for visual consistency
```

<details>
<summary><strong>Helper scripts (optional)</strong></summary>

```sh
# Inventory — enumerate, dedupe, palette
python3 ~/.config/opencode/skills/visual-design-language/scripts/inventory.py \
  --dir design-inspiration --out /tmp/vdl-inventory.json

# Audit — check generated docs + project
python3 ~/.config/opencode/skills/visual-design-language/scripts/visual-audit.py \
  --docs docs/design-language --project . --out /tmp/vdl-audit.md
```

</details>

---

## What’s Inside

```
skills/visual-design-language/
├── SKILL.md                      # 10-phase router + behavior rules + output contract
├── references/
│   ├── FOUNDATIONS.md            # discovery, per-image analysis checklist, synthesis, tokens
│   ├── COMPONENTS.md             # per-component spec template + coherence checks
│   ├── LAYOUTS.md                # composition, grid, spacing rhythm, responsive
│   ├── MOTION.md                 # durations, easing, transitions, feedback (only when evidenced)
│   ├── ANTI_PATTERNS.md          # deriving anti-patterns + consistency audit checklist
│   └── IMPLEMENTATION.md         # project inspection → KEEP/REFINE/REPLACE/CREATE → validation
└── scripts/
    ├── inventory.py              # enumerate + dedupe + palette + markdown table + JSON
    └── visual-audit.py           # token/component doc + project audit

docs/design-language/             # example output (warm paper minimalism, 16 refs)
├── DESIGN_LANGUAGE.md            # philosophy + DNA + principles + signal map
├── FOUNDATIONS.md                # tokens: spacing, shape, type, color, surface, icon, motion
├── COMPONENTS.md                 # app bar, nav, tabs, buttons, cards, lists, fields …
├── LAYOUTS.md                    # editorial single-column, generous air, responsive
├── MOTION.md                     # calm/crisp, 150/240/360
├── ANTI_PATTERNS.md              # 10 derived anti-patterns
└── IMPLEMENTATION.md             # build plan — all CREATE (no code yet → docs only)

design-inspiration/               # 16 example refs (used to produce the above docs)
```

---

## Skill Workflow (10 phases)

```
1 Discover         → locate & inventory every image, dedupe, palette
2 Visual Analysis  → per-image: layout/geometry/type/color/surface/components/icons/motion
3 Synthesis        → recurring vs strong vs secondary vs outlier vs conflict
4 Visual DNA       → philosophy + spatial/shape/type/color/surface/icon/motion systems (rules)
5 Component Language → per-component Purpose/Structure/Shape/Spacing/Type/Color/Surface/Elevation/Interaction/States/Variants/Anti-patterns
6 Anti-Patterns    → VISUAL ANTI-PATTERNS derived from refs
7 Originality      → extract principles (yes) vs logos/trademarks/screens (no)
8 Integration      → inspect project → KEEP/REFINE/REPLACE/CREATE → implement
9 Documentation    → DESIGN_LANGUAGE.md + FOUNDATIONS/COMPONENTS/LAYOUTS/MOTION/ANTI_PATTERNS/IMPLEMENTATION.md
10 Audit           → spacing/geometry/type/hierarchy/surface/reuse/color/density/noise/a11y — fix drift
```

The skill is a **design director**, not a screenshot-to-code generator. Output is original work informed by refs.

---

## Troubleshooting

### Skill doesn’t activate
Name it: `> Using the visual-design-language skill, analyze the design-inspiration folder`

### Installed but not found by `npx skills list`
```sh
npx skills list              # project + global
npx skills list -g           # global only
npx skills add JusDots-Devs/NewDots-Design -g -a opencode -y  # force global + agent
```

### `npx https://…` fails
Retry; repo is public and needs no token. Behind a proxy, use manual method. For private forks, `GITHUB_TOKEN` or `gh auth login`.

### Images not found
Put them in `design-inspiration/` or say: `> Inspiration is in ./screenshots — analyze it`

### Wants to rewrite my architecture
It shouldn’t — Phase 8 says reuse existing `Theme`/`tokens`/`components`. Prompt: `> Apply the language using existing architecture; prioritize perceptual wins`

---

## Limitations

| Area | Note |
|---|---|
| Static images only | No video/prototype → motion is conservative (durations + easing only, no shared-element unless evidenced) |
| Vision is agent-dependent | Some runners need a vision model to see images; otherwise describe or use helper script palettes |
| No automatic Figma import | Ingests exported PNG/JPG/WEBP, not live Figma API |
| Color pickers are quantized | `inventory.py` palettes are 5-color quantizations, not full gamut |
| No app code in repo | `IMPLEMENTATION.md` is “all CREATE — docs only”; when you add code, re-run Phase 8 |

---

## License

**Apache-2.0** — see [LICENSE](LICENSE).

Built with care by [JusDots-Devs](https://github.com/JusDots-Devs) · Feedback at [opencode#issues](https://github.com/anomalyco/opencode)

`npx https://github.com/JusDots-Devs/NewDots-Design`

</div>
