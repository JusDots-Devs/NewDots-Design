# NewDots — Visual Design Language

> **Informed by 16 references. Distilled into one coherent language. Not a copy of any single screenshot.**

## Visual DNA

The collection speaks with a **quiet, warm, tactile minimalism** — off-white paper surfaces, generous negative space, soft continuous geometry, and restrained tonal color. Interfaces feel **calm, editorial, and grounded**: low chrome, strong content hierarchy, and subtle depth through layered surfaces rather than heavy shadows. Accent color is used sparingly as a focal signal (coral, warm orange, periwinkle) against a backdrop of warm neutrals and near-blacks.

One paragraph rule: *NewDots prefers warm paper over pure white, air over chrome, soft squircles over hard rectangles, and typographic hierarchy over decorative excess. Every screen has at most one strong focal accent; everything else recedes through muted tone and proximity.*

---

## Design Philosophy

| Dimension | Position | Evidence |
|-----------|----------|----------|
| calm ↔ energetic | **calm** (restrained) | Light airy palettes, low saturation, generous whitespace |
| minimal ↔ expressive | **minimal with one expressive accent** | Flat surfaces + single bold card/accent per composition |
| dense ↔ spacious | **spacious** | Generous padding/margins, ~40–50% negative space |
| flat ↔ layered | **subtly layered** | 1–2 elevation levels, hairline borders over shadows |
| rigid ↔ organic | **soft-organic** | Continuous corners, pill shapes, circular accents |
| functional ↔ editorial | **editorial-functional** | Asymmetric grids, image-led hierarchy, readable body |
| understated ↔ theatrical | **understated** | Muted tones, singular accent, no gradient theatrics |

**Personality**: Quiet confidence — like good paper goods. Not playful, not corporate, not brutalist. Feels crafted, not templated.

---

## Core Principles

1. **Paper-first surfaces** — Warm off-whites (`#faf9f6`–`#f1f1f0`) are the default background. White is reserved for elevated cards. Pure `#fff` never as page background.
2. **Air as structure** — Whitespace creates grouping. No enclosing lines where proximity suffices. Section gap ≥ 2× card gap.
3. **Soft geometry everywhere** — Continuous corners (squircle-like) at 16–24px, pills for single-action, circles for icon containers. Never 4–8px sharp rects.
4. **One accent, low saturation field** — Field is desaturated warm neutrals; accent (coral/orange/periwinkle) marks one primary action or hero per screen. No multi-accent rainbows.
5. **Typography does the hierarchy** — Size + weight + muted color carry hierarchy. No icon-heavy, no card-heavy separation.
6. **Hairline over shadow** — Elevation is border + subtle surface tint, not drop shadow. Shadow only at modal level.
7. **Content is the chrome** — Image/media is the decoration; UI chrome recedes. Bars are translucent or paper, not opaque blocks.

---

## Signal Map

| Principle | Frequency | Strength | Verdict |
|-----------|-----------|----------|---------|
| Warm off-white / paper bg | 13/16 | ★★★★★ | Strong — base bg token |
| Near-black text (#121211–#1a1918) warm | 12/16 | ★★★★ | Strong — text primary |
| Muted secondary (#9c9d9b / #a2a19a) | 11/16 | ★★★★ | Strong — muted token |
| Soft 16–24 radius / pills / circles | 10/16 inferred | ★★★★ | Strong — radius scale |
| Sparse accent (coral/orange/peri) | 7/16 | ★★★ | Strong — accent rule |
| Generous whitespace, low chrome | 12/16 | ★★★★★ | Strong — layout DNA |
| Flat + hairline border, minimal shadow | 11/16 | ★★★★ | Strong — surface DNA |
| Desaturated field, tonal hierarchy | 14/16 | ★★★★ | Strong — color temperature |
| Translucency / blur hints | 0/16 static frames | ☆ | Insufficient evidence — omit |
| Multi-accent / gradient-heavy | 1/16 outlier (5451bde: deep purple) | ☆ | Noise — exclude from core |

**Outliers:**
- `5451bde12f954cbe2229ab58ecc29936.jpg` — deep purple `#1c0b2b` / `#c7a6f9` is the only saturated dark ground. Treat as **context-specific** (media/hero variant), not base. Keep as `surface-inverted` variant, don't shift whole palette dark.
- `db201e8fdc9ab0f688a9a8ae660d720e.jpg` — similar periwinkle dark. Same treatment.
- `4d1a717c4fe995b416b483e89f823141.jpg` — lime/mint neons. **Noise** — incidental illustration, not systemic.

**Conflicts resolved:**
- Warm paper vs cool blue (`5e5fd7ef` #bacaf0): warm wins — cool is outlier card tint, not page ground. Keep blue as optional `surface-tinted` variant.
- Rounded vs sharp: rounded wins unanimously.

---

## Anti-Patterns (summary)

1. Per-row elevated card wrapping — use grouped paper or dividers.
2. Random 8/10/12 radii — stick to 16/24/pill/circle.
3. Pure white page bg + grey cards — invert: warm paper page, white/tinted elevated.
4. Multi-accent or gradient per screen — one accent only.
5. Heavy drop shadows — hairline/border instead.
6. Weak type hierarchy (uniform 16 regular) — enforce scale.

Full list: `ANTI_PATTERNS.md`.

---

## How to use this doc

- **Designer**: read Philosophy + Principles then Foundations for values.
- **Engineer**: tokens in `FOUNDATIONS.md`, component rules in `COMPONENTS.md`, layout in `LAYOUTS.md`.
- **Future AI agent**: you can implement a new screen that belongs without seeing the originals by following tokens + component specs + anti-patterns.

Originality: this language extracts *proportion, spacing, hierarchy, shape, surface, and color relationships* — not logos, illustrations, or exact screen compositions. No ref is reconstructed.
