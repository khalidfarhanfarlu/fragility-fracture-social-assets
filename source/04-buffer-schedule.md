# Buffer schedule — what's live

All 32 posts are scheduled to **@athenahealtheducation** (Instagram Business, channel `6a57c33580cc80cdcabd20e8`, Buffer org "Khalid Farhan"). Auto-publish, 10:00 Irish time, Mon 20 Jul → Mon 21 Sep 2026. Verified: 32 scheduled, 0 errors.

## Hosting

Buffer's API can't read local files — it fetches media by public URL. So the assets are pushed to a public repo and served over jsDelivr, the same pattern as the SecondPassport job:

- Repo: `khalidfarhanfarlu/fragility-fracture-social-assets` (public)
- Cards: `https://cdn.jsdelivr.net/gh/khalidfarhanfarlu/fragility-fracture-social-assets@main/images/<id>.png`
- Reels: `https://cdn.jsdelivr.net/gh/khalidfarhanfarlu/fragility-fracture-social-assets@main/reels/reel-<n>.mp4`

**Do not delete or rename that repo while posts are pending.** Buffer resolves the URL at publish time, not at schedule time. If the repo goes away, every unpublished post fails.

## The reels

The four originals were HEVC, 1440×2560, ~60MB each. Instagram doesn't reliably accept HEVC, so they were transcoded to H.264 / 1080×1920 / AAC / faststart, 8–12MB each. Originals untouched at `5.mp4`–`8.mp4`; converted copies in `reels-h264/`.

| File | Posts | Topic (read from the visuals — audio not verified) |
|---|---|---|
| reel-7 | Tue 21 Jul | What a fragility fracture is, and diagnosis |
| reel-6 | Tue 28 Jul | Calcium needs Vitamin D; sunlight, food, supplements |
| reel-5 | Tue 4 Aug | Where calcium comes from, including non-dairy |
| reel-8 | Tue 11 Aug | Menopause, bone loss, and exercise |

Captions were written from the on-screen visuals plus the verified site stats, because there was no way to transcribe the audio locally. **If any reel says something different from what its caption claims, edit the caption in Buffer before its date.**

## Full run

| Date | Type | Asset |
|---|---|---|
| Mon 20 Jul | Card | A1 Silent epidemic |
| Tue 21 Jul | Reel | reel-7 Fragility fracture |
| Wed 22 Jul | Card | A2 400,000 |
| Fri 24 Jul | Card | B1 What is a fragility fracture |
| Mon 27 Jul | Card | A3 1 in 3 / 1 in 5 |
| Tue 28 Jul | Reel | reel-6 Calcium + Vitamin D |
| Wed 29 Jul | Card | C1 99% |
| Fri 31 Jul | Card | D1 Risk factors |
| Mon 3 Aug | Card | A4 30,000 |
| Tue 4 Aug | Reel | reel-5 Calcium sources |
| Wed 5 Aug | Card | B3 Fracture sites |
| Fri 7 Aug | Card | C3 Calcium needs Vitamin D |
| Mon 10 Aug | Card | B2 First visible sign |
| Tue 11 Aug | Reel | reel-8 Menopause + exercise |
| Wed 12 Aug | Card | C6 76% |
| Fri 14 Aug | Card | E1 Peak bone mass |
| Mon 17 Aug | Card | A7 Doubles your risk |
| Wed 19 Aug | Card | C5 The calcium gap |
| Fri 21 Aug | Card | D2 DXA scan |
| Mon 24 Aug | Card | B4 Men |
| Wed 26 Aug | Card | C2 Body takes it from bones |
| Fri 28 Aug | Card | C7 Dairy |
| Mon 31 Aug | Card | A6 74% untreated |
| Wed 2 Sep | Card | C8 4× Vitamin D |
| Fri 4 Sep | Card | B5 Menopause |
| Mon 7 Sep | Card | A5 €460m |
| Wed 9 Sep | Card | C9 85% |
| Fri 11 Sep | Card | D4 45% |
| Mon 14 Sep | Card | D3 Fracture Liaison Service |
| Wed 16 Sep | Card | C4 1,200mg |
| Fri 18 Sep | Card | E2 Exercise |
| Mon 21 Sep | Card | E3 Early testing |

Ordering rules held: never two "Test & Treat" cards in one week, never two yellow cards back to back. D4 and C4 were swapped from the original plan to keep the first rule.

## Notes

- Captions run long and lead with the number or the counter-intuitive line, then land on one action ("ask your GP", "check the label with your pharmacist", "risk check is two minutes"). 7 hashtags each, tuned per card.
- Every clinical claim in a caption carries its source inline.
- Every card has alt text set, which Instagram uses for screen readers. Relevant for a 50+ audience.
- The run finishes 21 Sep, before Irish clocks change on 25 Oct, so every `dueAt` is a clean `+01:00`. If you extend past 25 Oct, the offset becomes `+00:00`.
- **Bio still needs updating** — the link should point at `fragilityfracture.ie/am-i-at-risk`, not the homepage, and the medical disclaimer belongs there since the cards don't carry it. Suggested bio text is in `03-content-plan.md`.
