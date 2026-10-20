"""
Retro pixel-art asset generator for SK-Rudra's GitHub profile README.

Run:  python make_pixel_assets.py
Out:  assets/*.svg  (commit the whole assets/ folder to SK-Rudra/SK-Rudra)

Everything is drawn with a hand-made 5x7 bitmap font as <path> rects,
so the SVGs need no web fonts and render identically everywhere.
Edit the CONFIG block, re-run, re-commit.
"""
import os
import random

# ───────────────────────────── CONFIG ─────────────────────────────
NAME = "SHAHRIAR KARIM RUDRA"
SUBTITLE = "NLP & LLM ENGINEER // CSE @ BRAC UNIVERSITY"

SHEET = [  # character sheet fields  (label, value)
    ("NAME", "SK RUDRA"),
    ("CLASS", "NLP / LLM ENGINEER"),
    ("GUILD", "BRAC UNIVERSITY"),
    ("BASE", "DHAKA, BANGLADESH"),
    ("MAIN QUEST", "BANGLA PII REDACTION"),
]
MOTTO = "SHIP FEWER THINGS. SHIP THEM WELL."

STATS = [  # (label, level 0-10)  -> set these honestly to your own levels
    ("NLP", 8),
    ("LLMS", 7),
    ("ML", 7),
    ("FULL-STACK", 7),
    ("3D / GFX", 5),
]

SECTIONS = {  # filename -> (title, icon)
    "h-player": ("PLAYER 1", "heart"),
    "h-quests": ("QUEST LOG", "scroll"),
    "h-inventory": ("INVENTORY", "chest"),
    "h-arcade": ("ARCADE", "joystick"),
    "h-contact": ("SAVE POINT", "star"),
}

# palette
BG = "#0b0d1f"
BG2 = "#141634"
BG3 = "#1d1b4a"
CYAN = "#4cc9f0"
PINK = "#f72585"
YELLOW = "#ffd60a"
GREEN = "#80ed99"
PURPLE = "#7b2cbf"
WHITE = "#e9f1ff"
DIM = "#3a3f7a"

OUT = "assets"
random.seed(1502)

# ───────────────────────────── FONT 5x7 ─────────────────────────────
F = {
"A":[".###.","#...#","#...#","#####","#...#","#...#","#...#"],
"B":["####.","#...#","#...#","####.","#...#","#...#","####."],
"C":[".###.","#...#","#....","#....","#....","#...#",".###."],
"D":["####.","#...#","#...#","#...#","#...#","#...#","####."],
"E":["#####","#....","#....","####.","#....","#....","#####"],
"F":["#####","#....","#....","####.","#....","#....","#...."],
"G":[".###.","#...#","#....","#.###","#...#","#...#",".####"],
"H":["#...#","#...#","#...#","#####","#...#","#...#","#...#"],
"I":[".###.","..#..","..#..","..#..","..#..","..#..",".###."],
"J":["..###","...#.","...#.","...#.","...#.","#..#.",".##.."],
"K":["#...#","#..#.","#.#..","##...","#.#..","#..#.","#...#"],
"L":["#....","#....","#....","#....","#....","#....","#####"],
"M":["#...#","##.##","#.#.#","#.#.#","#...#","#...#","#...#"],
"N":["#...#","#...#","##..#","#.#.#","#..##","#...#","#...#"],
"O":[".###.","#...#","#...#","#...#","#...#","#...#",".###."],
"P":["####.","#...#","#...#","####.","#....","#....","#...."],
"Q":[".###.","#...#","#...#","#...#","#.#.#","#..#.",".##.#"],
"R":["####.","#...#","#...#","####.","#.#..","#..#.","#...#"],
"S":[".####","#....","#....",".###.","....#","....#","####."],
"T":["#####","..#..","..#..","..#..","..#..","..#..","..#.."],
"U":["#...#","#...#","#...#","#...#","#...#","#...#",".###."],
"V":["#...#","#...#","#...#","#...#","#...#",".#.#.","..#.."],
"W":["#...#","#...#","#...#","#.#.#","#.#.#","#.#.#",".#.#."],
"X":["#...#","#...#",".#.#.","..#..",".#.#.","#...#","#...#"],
"Y":["#...#","#...#",".#.#.","..#..","..#..","..#..","..#.."],
"Z":["#####","....#","...#.","..#..",".#...","#....","#####"],
"0":[".###.","#...#","#..##","#.#.#","##..#","#...#",".###."],
"1":["..#..",".##..","..#..","..#..","..#..","..#..",".###."],
"2":[".###.","#...#","....#","...#.","..#..",".#...","#####"],
"3":["#####","...#.","..#..","...#.","....#","#...#",".###."],
"4":["...#.","..##.",".#.#.","#..#.","#####","...#.","...#."],
"5":["#####","#....","####.","....#","....#","#...#",".###."],
"6":["..##.",".#...","#....","####.","#...#","#...#",".###."],
"7":["#####","....#","...#.","..#..",".#...",".#...",".#..."],
"8":[".###.","#...#","#...#",".###.","#...#","#...#",".###."],
"9":[".###.","#...#","#...#",".####","....#","...#.",".##.."],
" ":["....."]*7,
".":[".....",".....",".....",".....",".....",".##..",".##.."],
",":[".....",".....",".....",".....",".##..","..#..",".#..."],
":":[".....",".##..",".##..",".....",".##..",".##..","....."],
"-":[".....",".....",".....","#####",".....",".....","....."],
"_":[".....",".....",".....",".....",".....",".....","#####"],
"/":["....#","....#","...#.","..#..",".#...","#....","#...."],
"&":[".##..","#..#.","#.#..",".#...","#.#.#","#..#.",".##.#"],
"!":["..#..","..#..","..#..","..#..","..#..",".....","..#.."],
"?":[".###.","#...#","....#","...#.","..#..",".....","..#.."],
">":[".#...","..#..","...#.","....#","...#.","..#..",".#..."],
"<":["...#.","..#..",".#...","#....",".#...","..#..","...#."],
"@":[".###.","#...#","#.###","#.#.#","#.###","#....",".###."],
"+":[".....","..#..","..#..","#####","..#..","..#..","....."],
"'":["..#..","..#..",".#...",".....",".....",".....","....."],
"(":["...#.","..#..",".#...",".#...",".#...","..#..","...#."],
")":[".#...","..#..","...#.","...#.","...#.","..#..",".#..."],
"#":[".#.#.",".#.#.","#####",".#.#.","#####",".#.#.",".#.#."],
"=":[".....",".....","#####",".....","#####",".....","....."],
"*":[".....","#.#.#",".###.","#####",".###.","#.#.#","....."],
}


def text_w(s, k):
    return (len(s) * 6 - 1) * k


def text_path(s, x, y, k):
    """Path data for string s, top-left at (x,y), pixel size k. Merges row runs."""
    d = []
    for ci, ch in enumerate(s.upper()):
        g = F.get(ch, F["?"])
        ox = x + ci * 6 * k
        for r, row in enumerate(g):
            c = 0
            while c < 5:
                if row[c] == "#":
                    s0 = c
                    while c < 5 and row[c] == "#":
                        c += 1
                    d.append(f"M{ox+s0*k} {y+r*k}h{(c-s0)*k}v{k}h{-(c-s0)*k}z")
                else:
                    c += 1
    return "".join(d)


def text(s, x, y, k, fill, cls="", shadow=None):
    out = ""
    if shadow:
        out += f'<path d="{text_path(s, x+k, y+k, k)}" fill="{shadow}"/>'
    c = f' class="{cls}"' if cls else ""
    out += f'<path{c} d="{text_path(s, x, y, k)}" fill="{fill}"/>'
    return out


def text_c(s, cx, y, k, fill, **kw):
    return text(s, cx - text_w(s, k) // 2, y, k, fill, **kw)


def sprite(rows, x, y, k, pal, cls=""):
    """rows: list of strings; each char maps to a color in pal ('.' = empty)."""
    by_col = {}
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            ch = row[c]
            if ch in pal:
                s0 = c
                while c < len(row) and row[c] == ch:
                    c += 1
                by_col.setdefault(pal[ch], []).append(
                    f"M{x+s0*k} {y+r*k}h{(c-s0)*k}v{k}h{-(c-s0)*k}z")
            else:
                c += 1
    c = f' class="{cls}"' if cls else ""
    return f'<g{c}>' + "".join(
        f'<path d="{"".join(v)}" fill="{col}"/>' for col, v in by_col.items()) + "</g>"


def svg(w, h, body, style="", title=""):
    t = f"<title>{title.replace('&', '&amp;').replace('<', '&lt;')}</title>" if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" shape-rendering="crispEdges">{t}'
            f'<style>{style}@media (prefers-reduced-motion: reduce)'
            f'{{*{{animation:none!important}}}}</style>{body}</svg>')


def frame(w, h, k=4, col=CYAN, inner=BG):
    """Chunky pixel frame with notched corners."""
    return (f'<rect x="{k}" y="0" width="{w-2*k}" height="{h}" fill="{col}"/>'
            f'<rect x="0" y="{k}" width="{w}" height="{h-2*k}" fill="{col}"/>'
            f'<rect x="{k*2}" y="{k}" width="{w-4*k}" height="{h-2*k}" fill="{inner}"/>'
            f'<rect x="{k}" y="{k*2}" width="{w-2*k}" height="{h-4*k}" fill="{inner}"/>')


# ───────────────────────────── SPRITES (original) ─────────────────────────────
ROBOT = [  # 12x12 little companion bot
    ".....aa.....",
    ".....aa.....",
    "......w.....",
    "..wwwwwwww..",
    ".wddddddddw.",
    ".wdceddcedw.",
    ".wdceddcedw.",
    ".wddddddddw.",
    ".wddmmmmddw.",
    "..wwwwwwww..",
    "...w....w...",
    "..ww....ww..",
]
ROBOT_PAL = {"a": PINK, "w": WHITE, "d": BG3, "c": CYAN, "e": CYAN, "m": GREEN}

CODER = [  # 16x16 player portrait: hooded coder with headphones + laptop glow
    "....pppppppp....",
    "..pppppppppppp..",
    ".pppkkkkkkkkppp.",
    ".ppkkkkkkkkkkpp.",
    "hhpkssssssssk" + "phh",  # headphone cups on the sides
    "hhpsseesseessphh",
    "hhpssssssssssphh",
    "hhpssssmmssssphh",
    "..pppssssssppp..",
    "..pppppppppppp..",
    ".pppppppppppppp.",
    "ppppccccccccpppp",
    "ppppcbbbbbbcpppp",
    "pppccbbbbbbccppp",
    "pp" + "c" * 12 + "pp",
    "................",
]
CODER_PAL = {"p": PURPLE, "k": "#2b1a55", "s": "#f1c27d", "e": BG,
             "m": "#c46a4a", "h": PINK, "c": "#9aa3c7", "b": CYAN}

ICONS = {
    "heart": ([".rr.rr.", "rrrrrrr", "rrrrrrr", ".rrrrr.", "..rrr..", "...r..."], {"r": PINK}),
    "scroll": (["yyyyyy.", "ywwwwy.", ".wkkw..", ".wwww..", ".wkkw..", "yyyyyy."], {"y": YELLOW, "w": WHITE, "k": DIM}),
    "chest": ([".yyyyy.", "ybbbbby", "yyyyyyy", "ybbwbby", "ybbbbby", "yyyyyyy"], {"y": YELLOW, "b": "#8a4b2a", "w": WHITE}),
    "joystick": (["..rr...", "..rr...", "...w...", "...w...", ".ccccc.", "ccccccc"], {"r": PINK, "w": WHITE, "c": CYAN}),
    "star": (["...y...", "..yyy..", "yyyyyyy", ".yyyyy.", ".yy.yy.", "y.....y"], {"y": YELLOW}),
}


# ───────────────────────────── BANNER ─────────────────────────────
def banner():
    W, H, k = 1200, 400, 4
    b = [f'<rect width="{W}" height="{H}" fill="{BG}"/>']
    # banded sky (dithered pixel gradient)
    bands = [(0, BG), (180, BG2), (250, BG3), (300, "#2a1f5e")]
    for y0, col in bands:
        b.append(f'<rect y="{y0}" width="{W}" height="{H-y0}" fill="{col}"/>')
    for y0 in (176, 246, 296):  # checker dither on band edges
        d = "".join(f"M{x} {y0 + (x//k % 2)*k}h{k}v{k}h-{k}z" for x in range(0, W, k * 2))
        b.append(f'<path d="{d}" fill="{bands[[176,246,296].index(y0)][1]}"/>')

    # stars (twinkling)
    style = ("@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}"
             ".s{animation:tw 2.4s steps(2) infinite}"
             "@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:0}}"
             ".blink{animation:bl 1.1s steps(1) infinite}"
             "@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}"
             ".bob{animation:bob 1.6s steps(2) infinite}"
             "@keyframes shoot{0%{transform:translate(0,0);opacity:0}5%{opacity:1}"
             "20%{transform:translate(-420px,140px);opacity:0}100%{opacity:0}}"
             ".shoot{animation:shoot 7s linear infinite}"
             "@keyframes win{0%,100%{fill:" + YELLOW + "}50%{fill:" + BG2 + "}}"
             ".w{animation:win 3s steps(1) infinite}")
    for i in range(70):
        x, y = random.randrange(0, W, k), random.randrange(40, 250, k)
        if 150 < x < 1050 and 100 < y < 290:
            continue
        s = random.choice([k, k, k * 2])
        col = random.choice([WHITE, WHITE, CYAN, YELLOW])
        delay = random.random() * 2.4
        b.append(f'<rect class="s" style="animation-delay:{delay:.2f}s" x="{x}" y="{y}" '
                 f'width="{s}" height="{s}" fill="{col}"/>')
    # shooting star
    b.append(f'<g class="shoot"><rect x="1080" y="60" width="{k*2}" height="{k*2}" fill="{WHITE}"/>'
             f'<rect x="1088" y="56" width="{k*2}" height="{k}" fill="{CYAN}" opacity=".7"/>'
             f'<rect x="1096" y="52" width="{k*2}" height="{k}" fill="{CYAN}" opacity=".4"/></g>')
    # pixel moon
    moon = ["..yyyy..", ".yyyyyy.", "yyyyyyyy", "yyyyyyyy", "yyyyyyyy", "yyyyyyyy", ".yyyyyy.", "..yyyy.."]
    shade = ["........", "......dd", ".......d", ".......d", "......dd", ".....ddd", ".....dd.", "........"]
    b.append(sprite(moon, 1040, 70, 8, {"y": "#ffe9a8"}))
    b.append(sprite(shade, 1040, 70, 8, {"d": "#d9b86a"}))

    # skyline (deterministic random buildings) with flickering windows
    x = 0
    sky, wins = [], []
    while x < W:
        bw = random.randrange(40, 100, 8)
        bh = random.randrange(40, 120, 8)
        top = H - 40 - bh
        sky.append(f"M{x} {top}h{bw}v{bh+40}h-{bw}z")
        for wy in range(top + 12, H - 52, 16):
            for wx in range(x + 8, x + bw - 8, 12):
                if random.random() < 0.28:
                    cls = ' class="w" style="animation-delay:%.1fs"' % (random.random() * 3) if random.random() < 0.3 else ""
                    wins.append(f'<rect{cls} x="{wx}" y="{wy}" width="{k}" height="{k*2}" fill="{YELLOW}"/>')
        x += bw
    b.append(f'<path d="{"".join(sky)}" fill="#0f1029"/>')
    b += wins
    # ground strip
    b.append(f'<rect y="{H-40}" width="{W}" height="40" fill="{BG}"/>')
    b.append(f'<rect y="{H-40}" width="{W}" height="{k}" fill="{PINK}"/>')
    b.append(f'<rect y="{H-32}" width="{W}" height="{k}" fill="{PURPLE}"/>')

    # HUD
    b.append(text("1UP", 40, 28, 3, PINK))
    b.append(text("002026", 40, 56, 3, WHITE))
    b.append(text_c("HI-SCORE", W // 2, 28, 3, PINK))
    b.append(text_c("999999", W // 2, 56, 3, WHITE))
    b.append(text("CREDIT 01", W - 40 - text_w("CREDIT 01", 3), 28, 3, PINK))

    # name + subtitle
    nk = 7 if text_w(NAME, 7) < W - 120 else 6
    b.append(text_c(NAME, W // 2, 120, nk, CYAN, shadow=PINK))
    b.append(text_c(SUBTITLE, W // 2, 200, 3, WHITE))
    b.append(text_c("> PRESS START <", W // 2, 252, 4, YELLOW, cls="blink"))

    # companion bot on the ground
    b.append(f'<g class="bob">{sprite(ROBOT, 120, H-40-12*5, 5, ROBOT_PAL)}</g>')
    return svg(W, H, "".join(b), style, "Shahriar Karim Rudra - NLP & LLM Engineer")


# ───────────────────────────── SECTION HEADER ─────────────────────────────
def header(title, icon):
    W, H, k = 1200, 72, 4
    rows, pal = ICONS[icon]
    style = ("@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:0}}"
             ".blink{animation:bl 1s steps(1) infinite}")
    b = [frame(W, H, k, CYAN, BG)]
    b.append(sprite(rows, 28, 18, 5, pal))
    b.append(text(title, 84, 22, 4, WHITE, shadow=PINK))
    cx = 84 + text_w(title, 4) + 16
    b.append(f'<rect class="blink" x="{cx}" y="22" width="16" height="28" fill="{YELLOW}"/>')
    # dotted trail to the right
    dots = "".join(f"M{x} 34h{k*2}v{k*2}h-{k*2}z" for x in range(cx + 48, W - 40, 24))
    b.append(f'<path d="{dots}" fill="{DIM}"/>')
    return svg(W, H, "".join(b), style, title)


# ───────────────────────────── CHARACTER SHEET ─────────────────────────────
def sheet():
    W, H, k = 1200, 490, 4
    style = ("@keyframes fill{from{transform:scaleX(0)}to{transform:scaleX(1)}}"
             ".bar{transform-box:fill-box;transform-origin:left;animation:fill 1.6s steps(10) both}"
             "@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}"
             ".bob{animation:bob 1.8s steps(2) infinite}")
    b = [frame(W, H, k, PINK, BG)]
    # portrait box
    b.append(frame(240, 240, k, CYAN, BG2).replace('<rect ', '<rect transform="translate(40 40)" '))
    b.append(f'<g class="bob">{sprite(CODER, 64, 70, 12, CODER_PAL)}</g>')
    b.append(text_c("LV 21", 160, 296, 4, YELLOW))
    b.append(text_c("HP", 76, 340, 3, PINK))
    for i in range(8):
        b.append(f'<rect x="{96+i*16}" y="338" width="12" height="14" fill="{PINK if i < 7 else DIM}"/>')
    b.append(text_c("MP", 76, 368, 3, CYAN))
    for i in range(8):
        b.append(f'<rect x="{96+i*16}" y="366" width="12" height="14" fill="{CYAN if i < 6 else DIM}"/>')

    # fields
    x0, y = 320, 48
    for label, val in SHEET:
        b.append(text(label, x0, y, 3, PINK))
        b.append(text(val, x0 + 210, y, 3, WHITE))
        y += 34
    # stats
    y += 10
    b.append(text("STATS", x0, y, 3, YELLOW))
    y += 30
    for label, lvl in STATS:
        b.append(text(label, x0, y, 3, CYAN))
        bx = x0 + 210
        b.append(f'<rect x="{bx}" y="{y-4}" width="{10*28+4}" height="29" fill="{DIM}"/>')
        b.append(f'<rect class="bar" x="{bx+4}" y="{y}" width="{lvl*28-4}" height="21" fill="{GREEN}"/>')
        b.append(text(f"{lvl:02d}/10", bx + 10 * 28 + 24, y, 3, WHITE))
        y += 34
    b.append(text_c(MOTTO, W // 2 + 140, H - 46, 3, YELLOW))
    return svg(W, H, "".join(b), style, "Character sheet")


# ───────────────────────────── DIVIDER ─────────────────────────────
def divider():
    W, H, k = 1200, 48, 4
    style = ("@keyframes walk{from{transform:translateX(-80px)}to{transform:translateX(1220px)}}"
             ".walk{animation:walk 9s linear infinite}"
             "@keyframes eat{0%{opacity:1}100%{opacity:1}}")
    dots = "".join(f"M{x} 22h{k}v{k}h-{k}z" for x in range(16, W, 24))
    b = [f'<path d="{dots}" fill="{YELLOW}" opacity=".7"/>',
         f'<g class="walk">{sprite(ROBOT, 0, 0, 4, ROBOT_PAL)}</g>']
    return svg(W, H, "".join(b), style, "divider")


# ───────────────────────────── FOOTER ─────────────────────────────
def footer():
    W, H = 1200, 220
    # countdown 9..0 then loop, 1s per digit
    style = ("@keyframes d{0%,9.99%{opacity:1}10%,100%{opacity:0}}"
             ".dg{opacity:0;animation:d 10s steps(1) infinite}"
             "@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:0}}"
             ".blink{animation:bl 1s steps(1) infinite}")
    b = [frame(W, H, 4, PURPLE, BG)]
    b.append(text_c("THANKS FOR PLAYING!", W // 2, 36, 5, CYAN, shadow=PINK))
    b.append(text("CONTINUE?", W // 2 - 200, 106, 5, WHITE))
    for i, n in enumerate(range(9, -1, -1)):
        b.append(f'<g class="dg" style="animation-delay:{i}s">'
                 f'{text(str(n), W//2 + 120, 106, 5, YELLOW)}</g>')
    b.append(text_c("INSERT COIN TO COLLABORATE", W // 2, 170, 3, PINK, cls="blink"))
    return svg(W, H, "".join(b), style, "Thanks for playing")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    files = {"banner": banner(), "player-card": sheet(), "divider": divider(), "footer": footer()}
    for fn, (t, ic) in SECTIONS.items():
        files[fn] = header(t, ic)
    for fn, data in files.items():
        with open(os.path.join(OUT, fn + ".svg"), "w", encoding="utf-8") as f:
            f.write(data)
        print(f"wrote {OUT}/{fn}.svg  ({len(data)//1024} KB)")
