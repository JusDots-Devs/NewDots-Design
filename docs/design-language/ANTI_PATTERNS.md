# Visual Anti-Patterns

> Derived from the 16 refs — not a generic list. Each item says what the refs do instead and the concrete rule to avoid drift.

### 1. Every row in its own elevated card
Refs use flat grouped rows, hairline borders, or whitespace — not per-row `Card(elevation=2)`. **Rule**: use connected panel (outer 28/inner 6, gap 2) or dividers. Never wrap each list item in a Card.

### 2. Random corner radii (8/10/12)
Refs are coherent: 16 (cards/fields), 24 (hero/sheets), pill, circle. **Rule**: only `--radius-sm/md/lg/xl/pill/circle/inner`. No 8/10 one-offs.

### 3. Pure-white page background + grey cards
Refs invert: warm paper `#faf9f6` page + white cards. **Rule**: `--color-bg` is paper, `--color-surface` is white. Never `bg=#fff` with `card=#f5f5f5`.

### 4. Multiple accents per screen
Refs: at most one strong accent (coral/orange or periwinkle) per screen; field is desaturated. **Rule**: one `primary` fill per viewport. Secondaries use `surface-tinted` + `text-primary`.

### 5. Heavy drop shadows
Refs use hairline borders, not shadows. **Rule**: elevation 0–1 is border, not `shadow-8`. Shadow only at elevation 3 (modal). No `box-shadow` on cards.

### 6. Weak typographic hierarchy (uniform 16 regular)
Refs differentiate by size + weight + muted color; `label` uppercase meta is consistent. **Rule**: enforce `display/headline/title/body/label` + `text-muted` for secondary. No uniform 16.

### 7. Excessive UI chrome (opaque app bars, footers crowding content)
Refs are low-chrome; app bar is transparent/paper and defers to content/media. **Rule**: app bar 0→1 elevation on scroll only. No persistent opaque header that halves viewport.

### 8. Noisy navigation (bottom bar + drawer + tabs together)
Refs: one nav pattern per screen, pill style. **Rule**: bottom pill (phone) OR rail (tablet), not both visible. Tabs are content switches, not nav.

### 9. Gradient or blur as decoration
No gradient/blur observed. **Rule**: flat solids. Media may have warm tint but no brand gradient overlay, no frosted header. Blur only on modal scrim if needed.

### 10. Mixed icon treatments (stroke + fill + duotone)
Refs: uniform outlined stroke, regular weight. **Rule**: outlined 1.6 stroke, 20/24 size, same throughout. Selected state is fill in nav only.

---

## Audit checklist

See `SKILL.md` Phase 10 and `visual-audit.py`. Quick pass:

- [ ] No per-row Cards?
- [ ] Radii from scale only?
- [ ] Paper bg + white surface (not inverted)?
- [ ] ≤1 accent per screen?
- [ ] No shadow on cards?
- [ ] Typography uses scale + muted, not uniform?
- [ ] Chrome recedes (transparent bar)?
- [ ] Single nav pattern?
- [ ] No gradient/blur decoration?
- [ ] Icons uniform outlined?

## Example violations

| Violation | Looks like | Fix |
|-----------|------------|-----|
| Card soup | 12 Cards on settings screen | Group into connected panel(s) |
| Radius salad | Buttons 8, cards 16, sheets 12 | Buttons pill, cards 16, sheets 24 |
| White page | #fff page, grey cards | #faf9f6 page, #fff cards + border |
| Accent splatter | Coral + purple + teal in one hero | Keep coral primary, others muted or remove |
