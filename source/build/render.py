#!/usr/bin/env python3
"""Render FragilityFracture.ie Instagram cards (1080x1080) from cards.json.

Brand values are lifted from the live site's compiled CSS, not invented:
  brand yellow #E7D549 / hover #d4c43e / gold .ie #c8a800
  ink #434343 / hero black #111111 / cream #FDFDF5
  system UI font stack, extrabold headlines, 11px uppercase eyebrows

Usage:  python3 render.py            # renders every card in cards.json
        python3 render.py A2 C4      # renders only cards whose id starts with these
"""

import json
import os
import subprocess
import sys
import shutil
from pathlib import Path

BUILD = Path(__file__).resolve().parent
ROOT = BUILD.parent
OUT = ROOT / "images"
TMP = BUILD / ".html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SIZE = 1080
PAD = 88

FONT = ('-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, '
        '"Helvetica Neue", Arial, sans-serif')

THEMES = {
    "dark":   dict(bg="#111111", eyebrow="#E7D549", ink="#ffffff",
                   sub="#cccccc", source="#777777", rule="#E7D549",
                   chip_bg="#E7D549", chip_fg="#434343",
                   word="#ffffff", dot="#E7D549", url="#888888"),
    "cream":  dict(bg="#FDFDF5", eyebrow="#aaaaaa", ink="#434343",
                   sub="#666666", source="#aaaaaa", rule="#E7D549",
                   chip_bg="#E7D549", chip_fg="#434343",
                   word="#434343", dot="#c8a800", url="#aaaaaa"),
    "white":  dict(bg="#ffffff", eyebrow="#aaaaaa", ink="#434343",
                   sub="#666666", source="#aaaaaa", rule="#E7D549",
                   chip_bg="#E7D549", chip_fg="#434343",
                   word="#434343", dot="#c8a800", url="#aaaaaa"),
    "yellow": dict(bg="#E7D549", eyebrow="rgba(67,67,67,.55)", ink="#434343",
                   sub="rgba(67,67,67,.78)", source="rgba(67,67,67,.45)",
                   rule="#434343", chip_bg="#434343", chip_fg="#E7D549",
                   word="#434343", dot="rgba(67,67,67,.55)", url="rgba(67,67,67,.55)"),
}


def fit(text, big, small, short, long_):
    """Step the type size down as the string gets longer."""
    n = len(text)
    if n <= short:
        return big
    if n >= long_:
        return small
    span = (n - short) / (long_ - short)
    return round(big - (big - small) * span)


def footer(t):
    return f"""
    <div class="footer">
      <div class="lockup">
        <span class="chip">FF</span>
        <span class="word">FragilityFracture<span class="dot">.ie</span></span>
      </div>
      <span class="url">fragilityfracture.ie</span>
    </div>"""


def body_for(c, t):
    layout = c["layout"]

    if layout == "hero":
        s1 = fit(c["line1"], 96, 68, 16, 34)
        s2 = fit(c["line2"], 96, 68, 16, 34)
        return f"""
        <div class="main">
          <h1 class="hero">
            <span style="display:block;color:{t['rule']};font-size:{s1}px">{c['line1']}</span>
            <span style="display:block;color:{t['ink']};font-size:{s2}px">{c['line2']}</span>
          </h1>
          <p class="sub">{c['sub']}</p>
        </div>"""

    if layout == "stat":
        fs = fit(c["figure"], 190, 108, 5, 11)
        return f"""
        <div class="main">
          <p class="figure" style="font-size:{fs}px">{c['figure']}</p>
          <div class="rule"></div>
          <p class="label">{c['label']}</p>
          <p class="sub">{c['sub']}</p>
        </div>"""

    if layout == "duo":
        return f"""
        <div class="main">
          <div class="duo">
            <div class="duocol">
              <p class="figure" style="font-size:118px">{c['figureA']}</p>
              <div class="rule"></div>
              <p class="label" style="font-size:33px">{c['labelA']}</p>
            </div>
            <div class="duodiv"></div>
            <div class="duocol">
              <p class="figure" style="font-size:118px">{c['figureB']}</p>
              <div class="rule"></div>
              <p class="label" style="font-size:33px">{c['labelB']}</p>
            </div>
          </div>
          <p class="sub" style="margin-top:52px">{c['sub']}</p>
        </div>"""

    if layout == "sites":
        lis = "".join(
            f'<li><span class="dotmark"></span>{i}</li>' for i in c["items"])
        return f"""
        <div class="main">
          <ul class="sites">{lis}</ul>
          <div class="rule" style="margin-top:46px"></div>
          <p class="sub">{c['sub']}</p>
        </div>"""

    if layout in ("quote", "question"):
        qs = fit(c["quote"], 82, 50, 34, 96)
        cta = ""
        if c.get("cta"):
            cta = f'<div class="cta">{c["cta"]}</div>'
        return f"""
        <div class="main">
          <div class="rule" style="margin-bottom:44px"></div>
          <p class="quote" style="font-size:{qs}px">{c['quote']}</p>
          <p class="sub">{c['sub']}</p>
          {cta}
        </div>"""

    raise ValueError(f"unknown layout: {layout}")


def html_for(c):
    t = THEMES[c["theme"]]
    source = f'<p class="source">{c["source"]}</p>' if c.get("source") else ""
    cta_bg = t["rule"]
    cta_fg = "#434343" if c["theme"] != "yellow" else "#E7D549"
    cta_bg = "#E7D549" if c["theme"] != "yellow" else "#434343"

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  * {{ margin:0; padding:0; box-sizing:border-box; -webkit-font-smoothing:antialiased; }}
  body {{ width:{SIZE}px; height:{SIZE}px; background:{t['bg']};
          font-family:{FONT}; overflow:hidden; }}
  .card {{ width:{SIZE}px; height:{SIZE}px; padding:{PAD}px;
           display:flex; flex-direction:column; }}
  .eyebrow {{ font-size:19px; font-weight:700; letter-spacing:.18em;
              text-transform:uppercase; color:{t['eyebrow']}; }}
  .main {{ flex:1; display:flex; flex-direction:column; justify-content:center; }}
  .hero {{ font-weight:800; line-height:1.05; letter-spacing:-.02em; }}
  .figure {{ font-weight:800; color:{t['ink']}; line-height:.92;
             letter-spacing:-.035em; font-variant-numeric:tabular-nums; }}
  .rule {{ width:96px; height:7px; background:{t['rule']};
           border-radius:99px; margin:34px 0; }}
  .label {{ font-size:41px; font-weight:700; color:{t['ink']};
            line-height:1.24; letter-spacing:-.01em; max-width:860px; }}
  .quote {{ font-weight:800; color:{t['ink']}; line-height:1.12;
            letter-spacing:-.022em; max-width:900px; }}
  .sub {{ font-size:28px; color:{t['sub']}; line-height:1.5;
          margin-top:30px; max-width:840px; }}
  .duo {{ display:flex; align-items:stretch; gap:52px; }}
  .duocol {{ flex:1; }}
  .duodiv {{ width:2px; background:{t['source']}; opacity:.4; }}
  .duo .rule {{ margin:24px 0; width:64px; height:6px; }}
  .sites {{ list-style:none; }}
  .sites li {{ font-size:66px; font-weight:800; color:{t['ink']};
               line-height:1.36; letter-spacing:-.02em;
               display:flex; align-items:center; gap:26px; }}
  .dotmark {{ width:16px; height:16px; border-radius:99px;
              background:{t['rule']}; flex:0 0 auto; }}
  .cta {{ display:inline-block; align-self:flex-start; margin-top:38px;
          background:{cta_bg}; color:{cta_fg}; font-weight:700; font-size:26px;
          padding:18px 30px; border-radius:14px; }}
  .source {{ font-size:17px; color:{t['source']}; margin-bottom:26px;
             line-height:1.4; }}
  .footer {{ display:flex; align-items:center; justify-content:space-between;
             border-top:1px solid {t['source']}33; padding-top:26px; }}
  .lockup {{ display:flex; align-items:center; gap:12px; }}
  .chip {{ background:{t['chip_bg']}; color:{t['chip_fg']}; border-radius:10px;
           padding:7px 11px; font-size:23px; font-weight:800;
           letter-spacing:-.03em; line-height:1; }}
  .word {{ font-size:27px; font-weight:700; color:{t['word']};
           letter-spacing:-.01em; }}
  .dot {{ color:{t['dot']}; }}
  .url {{ font-size:23px; font-weight:600; color:{t['url']};
          letter-spacing:.01em; }}
</style></head>
<body><div class="card">
  <p class="eyebrow">{c.get('eyebrow','')}</p>
  {body_for(c, THEMES[c['theme']])}
  {source}
  {footer(THEMES[c['theme']])}
</div></body></html>"""


def main():
    wanted = sys.argv[1:]
    cards = json.loads((BUILD / "cards.json").read_text())
    if wanted:
        cards = [c for c in cards
                 if any(c["id"].startswith(w) for w in wanted)]

    OUT.mkdir(exist_ok=True)
    TMP.mkdir(exist_ok=True)

    for c in cards:
        f = TMP / f"{c['id']}.html"
        f.write_text(html_for(c))
        png = OUT / f"{c['id']}.png"
        subprocess.run([
            CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1",
            f"--screenshot={png}",
            f"--window-size={SIZE},{SIZE}",
            f"file://{f}",
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  {c['id']}.png  [{c['layout']}/{c['theme']}]")

    print(f"\n{len(cards)} cards -> {OUT}")


if __name__ == "__main__":
    main()
