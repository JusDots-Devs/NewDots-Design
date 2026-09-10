# Layouts — Composition & Responsive

## Dominant composition

**Editorial single-column with generous air**. Content stacks vertically; grouping by whitespace; media provides visual rhythm. No multi-column dashboard grid. Asymmetry is subtle (left-aligned text, right-aligned actions) not geometric.

## Grid

No strict 12-col grid observed in refs — use fluid + alignment:

- **Gutters / gaps**: 16 (card grid), 24 (section gap)
- **Margins**: 16 phone / 24 tablet / 24 + max-width centered desktop
- **Baseline**: 4 unit, text aligned to 16 inner margin.

If a grid is needed for card sections, use 2-col on phone (min 160), 3–4 on tablet — not rigid 12-col.

## Spacing rhythm

Canonical screen:

```
outer page padding: 16 (phone)
hero:   bottom 32–48 to next section
section header: bottom 16 to content
card grid: gap 16
list: row gap 2 (grouped) or divider only
section-to-section: 32–48
```

Whitespace is always ≥ content padding. When in doubt, add air — not chrome.

## Content widths

- **Phone**: full bleed with 16 inner margin.
- **Tablet**: 640–720 centered or 2-pane (list + detail) with 24 gutter.
- **Desktop**: 1024–1280 max-width; reading/empty states max 720 centered.

## Section patterns

### 1. Stacked sections (default)
Vertical stack, 24–32 gap, header `label` 12 uppercase muted or `headline` 24 depending on importance. Divider optional — whitespace preferred.

### 2. Grouped connected panel
For settings/menus/short lists: connected list (outer 28, inner 6, gap 2) on `surface` over `bg`. Header `label` above panel with 12 gap.

### 3. Card grid
2-col phone, 3-col tablet. Card `md` 16 radius, 16 padding. Use for discovery/gallery.

### 4. Carousel (when needed)
Horizontal scroll of hero cards `lg` 24 radius, peek 24 trailing. Not core to these refs but compatible — use `centered-hero-carousel` skill if implemented.

## Responsive behavior

- **Reflow** for reading content (fill width).
- **Reveal** for card grids (+1 column at 600/840).
- **Transform**: bottom pill nav (phone) → rail (tablet+). App bar remains 56.
- Breakpoints: `compact <600`, `medium 600–840`, `expanded >840` (Android) or `640/768/1024` (web).

No responsive mockup observed — principle is "content reflows, nav transforms, never horizontal scroll for primary content."

## Hierarchy

- Hero: `display` or `headline` + large media
- Section: `headline` or `label` uppercase
- Card: `title` + `body-sm` + `label` meta
- List: `body` + `body-sm` muted + `label` trailing

## Checklist

- [ ] Margins consistent (16 phone, 24 tablet+)?
- [ ] Section gaps 24–48, not random?
- [ ] Max-width respected?
- [ ] No orphaned single card on wide screens?
- [ ] Whitespace intentional, not just leftover?
