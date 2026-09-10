# Anti-Patterns + Visual Consistency Audit

## Deriving anti-patterns

Anti-patterns are **inferred from the refs**, not copied from a generic list. For each candidate ask:

1. Do the refs consistently avoid it? If yes → anti-pattern.
2. Do some refs use it intentionally (e.g., glass in a glass-language)? Then it is not an anti-pattern — it is a feature.
3. Would adding it make the product drift from the refs' personality?

Only list anti-patterns that pass (1). 4–8 items is enough; 15 is generic.

### Common candidates (evaluate, don't auto-include)

- Excessive cards (every row in its own elevated card)
- Excessive borders (hairlines everywhere)
- Random corner radii (8 on buttons, 24 on cards, 999 on chips — no scale)
- Inconsistent spacing (one-off `13px`, `10px` among `8/16/24`)
- Generic default Material / Tailwind styling (no opinion, looks like starter template)
- Excessive gradients (gradient everywhere, even where refs are flat)
- Excessive blur / glass (frosted header where refs are opaque)
- Excessive shadows (drop shadows in a flat language)
- Noisy navigation (too many nav patterns at once)
- Too much UI chrome (headers/footers crowd content)
- Weak typography hierarchy (everything 16px regular)
- Inconsistent icon treatment (stroke + fill + duotone mixed)
- Over-decoration (illustrations, badges, ornaments where refs are minimal)
- Visually dense layouts (no breathing room in a spacious language)
- Low contrast muted text (<4.5:1)

### Template

```md
## Visual Anti-Patterns
1. **Excessive cards** — refs use flat grouped rows, not per-row cards. Do not wrap every item in Card(elevation=2). Use grouped list or dividers.
2. **Random radii** — refs use 16/24/pill only. No 8, 10, 12 one-offs.
...
```

Each item: **name — what refs do instead — concrete rule to avoid it.**

---

## Visual Consistency Audit

Run after implementation. Check at two levels: **component** and **product**.

### Component-level

- [ ] Spacing uses token scale? No hard-coded one-offs?
- [ ] Radii from scale? Consistent across same component type?
- [ ] Typography uses type scale? No ad-hoc `fontSize: 17`?
- [ ] Color from roles? No hard-coded hex except brand override?
- [ ] Elevation intentional? Not every element at `elevation=2`?
- [ ] Icon size/weight uniform?
- [ ] Press/hover/focus states present and consistent?
- [ ] A11y: contrast ≥4.5:1, touch target ≥48dp, focus visible, contentDescription?

### Product-level (coherence)

- [ ] Do all screens look like they belong to one product? (The critical test.)
- [ ] Density consistent? (No marketing-airy hero next to cramped settings.)
- [ ] Hierarchy consistent? (Same header scale everywhere, same muted style.)
- [ ] Surface hierarchy makes sense as a stack? (No elevation inversion.)
- [ ] Navigation pattern is one choice, not three mixed?
- [ ] No visual noise? (Every decoration earns its place.)
- [ ] No unnecessary complexity? (Tokens reused, not per-screen inventions.)

### Responsive

- [ ] Margins adapt (16→24→centered max-width)?
- [ ] No orphaned single-item rows on wide screens?
- [ ] No horizontal scroll where reflow is expected?

### Fix loop

For each inconsistency:

1. Name the violation (e.g., "Settings uses 8px radius, Home uses 16px").
2. Decide: which value is the language? (Refs' strong signal.)
3. Fix at token/component level, not per-screen patch.
4. Re-audit.

### Audit output

```
CONSISTENCY AUDIT
Pass: spacing, radii, typography, color roles, icons
Fix: elevation on cards (2→1), muted text contrast 3.8→4.6, settings density compact→comfortable
Remaining: tablet layout not verified (no tablet ref) — assumed 720 max-width
```
