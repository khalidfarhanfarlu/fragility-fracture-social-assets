# FragilityFracture.ie — Brand Kit for Social

Everything here was extracted from the live site's compiled CSS and rendered HTML on 15 July 2026, not guessed. Use it as the single source of truth for any asset we make.

## Logo lock-up

The site's logo is a two-part lock-up in the header:

- A rounded-corner chip containing **FF** — background `#E7D549`, text `#434343`, bold, tight tracking.
- The wordmark **FragilityFracture** in `#434343`, followed by **.ie** in gold `#c8a800`.

There is no separate image file for the logo; it is built in HTML/CSS. Our cards rebuild it the same way, so it matches the site pixel for pixel.

## Colours

| Role | Hex | Where the site uses it |
|---|---|---|
| Brand yellow | `#E7D549` | Logo chip, buttons, accent word in the hero headline, rules under stats |
| Yellow hover / deep | `#d4c43e` | Button hover state |
| Gold | `#c8a800` | The `.ie` in the wordmark |
| Ink (primary text) | `#434343` | Body text and headings sitewide; also `<body>` text colour |
| Hero black | `#111111` | Homepage hero section background |
| Charcoal | `#2d2d2d` | Secondary dark panels |
| Cream | `#FDFDF5` | Soft section backgrounds |
| White | `#FFFFFF` | Page background |
| Grey 555 / 666 / 888 / aaa | `#555555` `#666666` `#888888` `#aaaaaa` | Nav, body copy, captions, source lines |
| Slate | `#1e293b` | Occasional dark heading |

Yellow is an accent, never a large text colour on white. On the site it appears as a chip, a button, a short rule, or one accent word on a dark background. We keep that discipline.

## Type

The site loads no webfont. It runs on the system UI stack:

```
-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif
```

Our cards use the same stack and render on macOS, so they come out in SF Pro — identical to what an Irish visitor sees on an iPhone.

Weights and sizes copied from the site:

- Hero headline: `font-extrabold` (800), line-height `1.05`, ~3.4rem at desktop
- Section headings: `font-extrabold` or `font-bold` (700–800), `#434343`
- Body: regular, `#666666`, relaxed line-height
- Eyebrow labels: 11px, bold, uppercase, `tracking-widest`, `#aaaaaa`
- Source lines: 10px, `#aaaaaa`

## Tone

Clinical but plain. Urgent without scaremongering. The site's own line is the whole strategy in one sentence: *"Early testing and treatment change outcomes."*

Rules we follow in captions:

- Never diagnose, never promise an outcome, never recommend a dose as instruction. Point to a GP or pharmacist.
- Every clinical claim carries a source.
- Keep the medical disclaimer in the bio, not on every card.
- Irish English throughout: oestrogen, not estrogen. Euro symbol before the number.

## Card system

Five layouts, all 1080×1080, all with the logo lock-up and `fragilityfracture.ie` in the footer.

1. **Hero dark** — `#111111` background, yellow eyebrow, white headline with one yellow accent line. Mirrors the homepage hero.
2. **Stat** — cream or white, oversized numeral in `#434343`, yellow rule beneath, plain-English label.
3. **Cream quote** — `#FDFDF5`, dark headline, yellow rule.
4. **Yellow** — `#E7D549` field, `#434343` ink. Used sparingly for the strongest single lines.
5. **Question** — dark, for the "should I…?" prompts that push to the risk checker.

Safe margins are 88px. Instagram crops the top and bottom of a 1:1 in some surfaces, so nothing important sits within 60px of an edge.

## Attribution

Athena Pharma is the site's sponsor and appears in the footer as "Supported By". The Instagram account is Athena Health Education. Cards carry the FragilityFracture.ie mark because that is where the traffic goes; Athena's role is stated in the account bio rather than stamped on every image.
