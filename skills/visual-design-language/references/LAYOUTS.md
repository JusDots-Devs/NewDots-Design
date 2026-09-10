# Layouts — Composition, Grid, Responsive

## Composition principles

Infer from refs, don't impose. Common axes:

- **Single-column editorial** vs **dashboard grid** vs **masonry** vs **list-first**
- **Centered** (max-width + auto margins) vs **flush** (edge-to-edge) vs **asymmetric**
- **Layered** (overlapping cards, sheets) vs **flat** (sequential sections)
- **Anchored hero** (one large focal element per screen) vs **uniform density**

Rule: name the dominant composition and when to break it.

## Grid

- **Columns**: 4 / 6 / 12? Fixed vs fluid?
- **Gutters**: 8 / 16 / 24? Same as spacing scale?
- **Margins**: 16 (phone) / 24 (tablet) / max-width centered (desktop)?
- **Baseline grid**: 4 or 8? Text baseline alignment visible?

If refs do not show a clear grid, do not invent one — describe alignment instead: "all content aligns to 16px inner margin, no multi-column grid observed."

## Spacing

Use the spatial token scale. Define:

```
--space-1:  4   micro gap (icon–text)
--space-2:  8   tight gap (chip group)
--space-3: 12   related items
--space-4: 16   component padding
--space-5: 24   section gap
--space-6: 32   block separation
--space-7: 48   section separation
--space-8: 64   hero separation
```

Adjust values to match refs. Dense language compresses 24→20, 48→32. Spacious language expands 32→48, 64→80.

### Density guidelines

- **Comfortable** (default): `space-4` inside cards, `space-5` between sections
- **Compact** (tables, settings): one step down
- **Spacious** (marketing, hero): one step up

Never mix densities on one screen without intent.

## Content widths

- Phone: full-bleed with `16–20` inner margin
- Tablet: `640–720` centered or two-pane
- Desktop: `1024–1280` max-width, or `720` for reading

If refs are all phone portraits (common), extrapolate cautiously: "phone-first; tablet/desktop max-width 720/1024 assumed, not observed."

## Section patterns

Document recurring section treatments:

- **Stacked** (vertical rhythm, dividers or whitespace only)
- **Grouped card** (related rows in one container — see segmented-connect-list)
- **Carousel** (horizontal scroll, hero card — see centered-hero-carousel)
- **Grid cards** (2-col on phone, 3–4 on tablet)

For each, note: padding, gap, header style, divider usage.

## Responsive behavior

- **Reflow** vs **reveal** (show more columns) vs **transform** (bottom bar → rail)
- Breakpoints: infer or use project defaults (`compact <600, medium 600–840, expanded >840` for Android; `640/768/1024` for web)
- Avoid inventing responsive mockups not in refs — describe principle: "content reflows to fill width; nav collapses to bottom bar on compact."

## Visual hierarchy

- **Size**: display for hero, headline for section, title for card, body for content, label for meta
- **Weight**: 700 for emphasis, 500 for titles, 400 for body — or all 400 with size-only hierarchy (common in minimal refs)
- **Color**: primary for hero accent, muted for secondary, high contrast for primary content
- **Position**: top-left is primary focal; bottom-trailing is action

## Checklist

- [ ] Margins consistent across screens?
- [ ] Section gaps use one scale?
- [ ] Max-width respected (no infinite stretch)?
- [ ] No orphaned single-item rows on wide screens?
- [ ] Whitespace is intentional, not just gaps?
