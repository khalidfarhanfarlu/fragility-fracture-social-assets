# Fragility Fracture — Social Media

Instagram content for **@athenahealtheducation**, driving to **fragilityfracture.ie**.

## What's here

| File | What it is |
|---|---|
| [01-brand-kit.md](01-brand-kit.md) | The FragilityFracture.ie brand system, pulled from the live site's compiled CSS. Colours, type, logo lock-up, tone, card layouts. |
| [02-fact-check.md](02-fact-check.md) | Every supplied quote checked against the live site. **Read this one** — there are two things that need your decision. |
| [03-content-plan.md](03-content-plan.md) | The strategy, all 28 cards with ready-to-paste captions, an 8-week schedule, hashtags, bio copy, and what to build next. |
| `images/` | 28 finished 1080×1080 PNGs, ready to post. |
| `build/` | `cards.json` (all copy) + `render.py` (the renderer). Edit the JSON, re-run, get new PNGs. |

## The two decisions I need from you

1. **The site contradicts itself on women's risk.** Homepage says *1 in 3 women over 60*. The research page says *1 in 2 women over 50*. I've built on the homepage figure, but the site needs reconciling before someone notices.
2. **The fragility fracture definition she flagged has already been updated on the site**, and the live wording is better than the version in your list. I've used the live wording. If she wanted a different change, I need to know what it is.

Both are explained in [02-fact-check.md](02-fact-check.md).

## Regenerating the images

```bash
cd build
python3 render.py           # all 28
python3 render.py A2 C4     # just these
```

Copy lives in `build/cards.json`. Change the text there, re-run, and the PNG is rebuilt in the same style. Requires Google Chrome, which renders the cards headless at 1080×1080.

## Notes on the build

The brand isn't approximated. The colours (`#E7D549` yellow, `#434343` ink, `#111111` hero black, `#FDFDF5` cream, `#c8a800` gold on the `.ie`), the font stack, the weights, the 11px uppercase eyebrows, the yellow rule, and the FF logo chip are all lifted from the site's own CSS, so the cards and the landing page look like one thing.

Every clinical claim on a card carries a source line, in the same 10px grey the site uses. Sources: IFLS-DB 2024, International Osteoporosis Foundation, Institute of Medicine 2011, and Athena's own 2023 research with Empathy Research.
