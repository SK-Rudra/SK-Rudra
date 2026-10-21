"""
Builds the pixel-art SVG assets for the profile README.

    python scripts/build_assets.py

Writes to assets/. Edit PALETTE, STACK or LINKS below, re-run, commit.
No dependencies beyond the standard library; logo paths (from the
simple-icons project, CC0) live in scripts/icons.json.

Palette is sampled from assets/banner.gif:
  night  - deep sky behind the moon
  indigo - violet haze over the mountains
  aurora - the green aurora ribbon
  moon   - moonlight / snow highlight
  haze   - lake reflection blue
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")

PALETTE = {
    "night": "#0d1838",
    "indigo": "#262a5c",
    "aurora": "#5ccf96",
    "moon": "#eef2cf",
    "haze": "#7f93b8",
}
# light-mode counterparts (same roles, readable on white)
LIGHT = {
    "text": "#262a5c",
    "aurora": "#2f8f6a",
    "moon": "#b8923a",
    "haze": "#6b7590",
    "fade": "#dfe3f0",
}

STACK = {  # file id -> (label, icon key)
    "python": ("PYTHON", "python"),
    "pytorch": ("PYTORCH", "pytorch"),
    "huggingface": ("HUGGING FACE", "huggingface"),
    "sklearn": ("SCIKIT-LEARN", "sklearn"),
    "typescript": ("TYPESCRIPT", "typescript"),
    "nextjs": ("NEXT.JS", "nextjs"),
    "nestjs": ("NESTJS", "nestjs"),
    "nodejs": ("NODE.JS", "nodejs"),
    "postgres": ("POSTGRESQL", "postgres"),
    "prisma": ("PRISMA", "prisma"),
    "supabase": ("SUPABASE", "supabase"),
    "git": ("GIT", "git"),
    "latex": ("LATEX", "latex"),
}
LINKS = {"linkedin": "LINKEDIN", "email": "EMAIL", "repos": "REPOSITORIES"}
HEADERS = {"about": "ABOUT", "now": "NOW", "projects": "PROJECTS", "stack": "STACK", "arcade": "ARCADE"}
NAME = "SHAHRIAR KARIM RUDRA"
MOTTO = "SHIP FEWER THINGS. SHIP THEM WELL."
FAREWELL = "THANKS FOR VISITING"

REDUCED = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
ICONS = json.load(open(os.path.join(ROOT, "scripts", "icons.json")))

# ── 5x7 pixel font ──────────────────────────────────────────────
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
" ":["....."]*7,
".":[".....",".....",".....",".....",".....",".##..",".##.."],
"-":[".....",".....",".....","#####",".....",".....","....."],
}
MOON = ["..###..", ".#####.", "###.###", "#######", "##.####", ".#####.", "..###.."]  # full moon, two craters
SPARKLE = ["..#..", "..#..", "##.##", "..#..", "..#.."]
DIAMOND = ["..#..", ".###.", "#####", ".###.", "..#.."]
PINE = ["..#..", ".###.", "..#..", ".###.", "#####", "..#.."]
ARROW = ["..####", "....##", "...#.#", "..#..#", ".#....", "#....."]  # ↗


def text_w(s, k):
    return (len(s) * 6 - 1) * k


def bitmap(rows, x, y, k):
    d = []
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):
            if row[c] == "#":
                s = c
                while c < len(row) and row[c] == "#":
                    c += 1
                d.append(f"M{x+s*k} {y+r*k}h{(c-s)*k}v{k}h{-(c-s)*k}z")
            else:
                c += 1
    return "".join(d)


def text_path(s, x, y, k):
    return "".join(bitmap(F[ch], x + i * 6 * k, y, k) for i, ch in enumerate(s))


def svg(w, h, body, title, css=""):
    style = f"<style>{css}{REDUCED}</style>" if css else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" shape-rendering="crispEdges" role="img">'
            f'<title>{title}</title>{style}{body}</svg>')


def notched(x, y, w, h, n, fill):
    """Rectangle with 1-pixel stepped corners, the pixel-art 'rounded' corner."""
    return (f'<path d="M{x+n} {y}h{w-2*n}v{n}h{n}v{h-2*n}h{-n}v{n}h{-(w-2*n)}'
            f'v{-n}h{-n}v{-(h-2*n)}h{n}z" fill="{fill}"/>')


def lerp(a, b, t):
    a, b = [int(a[i:i+2], 16) for i in (1, 3, 5)], [int(b[i:i+2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


# ── assets ──────────────────────────────────────────────────────
def chip(label, icon=None, arrow=False):
    """Dark pixel chip (same on both themes, like a piece of the night sky)."""
    k, h = 2, 30
    x = 10
    body = []
    if icon:
        body.append(f'<svg x="{x}" y="8" width="14" height="14" viewBox="0 0 24 24" '
                    f'shape-rendering="geometricPrecision"><path d="{ICONS[icon]}" '
                    f'fill="{PALETTE["moon"]}"/></svg>')
        x += 14 + 8
    body.append(f'<path d="{text_path(label, x, 8, k)}" fill="{PALETTE["moon"]}"/>')
    x += text_w(label, k)
    if arrow:
        x += 8
        body.append(f'<path d="{bitmap(ARROW, x, 9, 2)}" fill="{PALETTE["aurora"]}"/>')
        x += 12
    w = x + 10
    frame = notched(0, 0, w, h, 2, PALETTE["indigo"]) + notched(2, 2, w - 4, h - 4, 2, PALETTE["night"])
    return svg(w, h, frame + "".join(body), label.title())


def header(label, dark):
    k, h = 3, 24
    moon, txt = (PALETTE["moon"], PALETTE["moon"]) if dark else (LIGHT["moon"], LIGHT["text"])
    a, fade = (PALETTE["aurora"], PALETTE["indigo"]) if dark else (LIGHT["aurora"], LIGHT["fade"])
    body = [f'<path d="{bitmap(MOON, 0, 1, k)}" fill="{moon}"/>',
            f'<path d="{text_path(label, 33, 1, k)}" fill="{txt}"/>']
    x = 33 + text_w(label, k) + 18
    n = 12
    for i in range(n):  # aurora trail fading into the night, shimmering left to right
        body.append(f'<rect class="t" style="animation-delay:{i*0.12:.2f}s" x="{x + i*12}" y="9" '
                    f'width="6" height="6" fill="{lerp(a, fade, i/(n-1))}"/>')
    w = x + n * 12
    css = "@keyframes sh{0%,100%{opacity:1}50%{opacity:.25}}.t{animation:sh 2.8s steps(3) infinite}"
    return svg(w, h, "".join(body), label.title(), css)


def wordmark(dark):
    k = 5
    fg, sh = (PALETTE["moon"], PALETTE["indigo"]) if dark else (LIGHT["text"], LIGHT["fade"])
    tw = text_w(NAME, k)
    w, h = tw + k + 30, 7 * k + k
    spark = PALETTE["aurora"] if dark else LIGHT["aurora"]
    body = (f'<path d="{text_path(NAME, k, k, k)}" fill="{sh}"/>'
            f'<path d="{text_path(NAME, 0, 0, k)}" fill="{fg}"/>'
            f'<path class="s" d="{bitmap(SPARKLE, tw + 15, 0, 3)}" fill="{spark}"/>')
    css = ("@keyframes tw{0%,100%{opacity:1}50%{opacity:0}}"
           ".s{animation:tw 1.8s steps(2) infinite}")
    return svg(w, h, body, "Shahriar Karim Rudra", css)


def bullet():
    """Small aurora diamond used as a project marker (works on both themes)."""
    return svg(10, 10, f'<path d="{bitmap(DIAMOND, 0, 0, 2)}" fill="#3fb47f"/>', "")


def footer():
    """A small night scene that closes the page, echoing the banner."""
    import random
    rnd = random.Random(1502)
    W, H, k = 720, 200, 3
    P = PALETTE
    b = []
    # sky: stepped bands with a checker dither between them
    bands = [(0, P["night"]), (70, "#121f47"), (110, "#19285a"), (140, P["indigo"])]
    for y0, col in bands:
        b.append(f'<rect y="{y0}" width="{W}" height="{H - y0}" fill="{col}"/>')
    for (y0, _), (_, col) in zip(bands[1:], bands[1:]):
        d = "".join(f"M{x} {y0 - k + (x // k % 2) * k}h{k}v{k}h-{k}z" for x in range(0, W, 2 * k))
        b.append(f'<path d="{d}" fill="{col}"/>')
    # aurora: soft vertical curtains
    import math
    for i in range(36):  # a ribbon of thin curtains: bright crown, faint tail
        x = 24 + i * 2 * k
        top = 6 + round(8 * math.sin(i / 4.5) + 3 * math.sin(i / 1.9))
        top -= top % k
        fade = 0.55 * math.sin(math.pi * (i + 0.5) / 36) ** 0.7
        hgt = 9 + 3 * ((i * 7) % 3)
        b.append(f'<g class="au" style="animation-delay:{(i % 9) * 0.35:.2f}s" opacity="{fade:.2f}">'
                 f'<rect x="{x}" y="{top + 6}" width="{k}" height="{hgt}" fill="{P["aurora"]}"/>'
                 f'<rect x="{x}" y="{top + 6 + hgt}" width="{k}" height="{hgt + 6}" fill="{P["aurora"]}" opacity=".35"/></g>')
    # stars
    for _ in range(46):
        x, y = rnd.randrange(0, W, k), rnd.randrange(6, 128, k)
        if 120 < x < 600 and 36 < y < 112:  # keep the text area clean
            continue
        col = rnd.choice([P["moon"], P["moon"], P["haze"]])
        b.append(f'<rect class="st" style="animation-delay:{rnd.random() * 3:.2f}s" x="{x}" y="{y}" '
                 f'width="{k}" height="{k}" fill="{col}"/>')
    # moon + halo
    b.append(f'<circle cx="636" cy="44" r="26" fill="{P["moon"]}" opacity=".08"/>')
    b.append(f'<path d="{bitmap(MOON, 615, 23, 6)}" fill="{P["moon"]}"/>')
    # mountains (stepped silhouettes), one snow-capped like the banner
    def ridge(xs, base, col):
        d = f"M{xs[0][0]} {base}"
        for x, y in xs:
            d += f"V{y}H{x + 2 * k}"
        d += f"V{base}z"
        b.append(f'<path d="{d}" fill="{col}"/>')
    def h(x, cx, top, slope):
        y = 160 - max(0, round(top - abs(x - cx) * slope))
        return y - y % k
    far = [(x, h(x, 470, 30, 0.22)) for x in range(300, 640, 2 * k)]
    ridge(far, 160, "#1f2758")
    peak = [(x, h(x, 624, 56, 0.6)) for x in range(520, 726, 2 * k)]
    ridge(peak, 160, "#2c3570")
    snow = [(x, y) for x, y in peak if y < 124]
    d = "".join(f"M{x} {y}h{2*k}v{(124 - y) // 2 + k - ((124 - y) // 2) % k}h-{2*k}z" for x, y in snow)
    b.append(f'<path d="{d}" fill="#c9d3ea"/>')
    # lake + moon reflection
    b.append(f'<rect y="160" width="{W}" height="40" fill="#121d43"/>')
    b.append(f'<rect y="160" width="{W}" height="{k}" fill="#2f4170"/>')
    for i, (dx, w) in enumerate([(0, 30), (6, 18), (-3, 24), (9, 12)]):
        b.append(f'<rect class="rf" style="animation-delay:{i * 0.4:.1f}s" x="{621 + dx}" '
                 f'y="{168 + i * 8}" width="{w}" height="{k}" fill="{P["moon"]}" opacity=".55"/>')
    # shore with pines on the left
    b.append(f'<path d="M0 154h84v3h30v3h24v3h21v37H0z" fill="#0f2a22"/>')
    for x, s_ in [(6, 6), (36, 8), (72, 5), (98, 4)]:
        b.append(f'<path d="{bitmap(PINE, x, 156 - 6 * s_, s_)}" fill="#1d4a36"/>')
    # text
    b.append(f'<path d="{text_path(FAREWELL, (W - text_w(FAREWELL, 4)) // 2 + 4, 52, 4)}" fill="{P["indigo"]}"/>')
    b.append(f'<path d="{text_path(FAREWELL, (W - text_w(FAREWELL, 4)) // 2, 48, 4)}" fill="{P["moon"]}"/>')
    b.append(f'<path d="{text_path(MOTTO, (W - text_w(MOTTO, 2)) // 2, 94, 2)}" fill="{P["haze"]}"/>')
    css = ("@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}.st{animation:tw 3s steps(2) infinite}"
           "@keyframes au{0%,100%{opacity:.18}50%{opacity:.5}}.au{animation:au 4s ease-in-out infinite}"
           "@keyframes rf{0%,100%{opacity:.55;transform:translateX(0)}50%{opacity:.2;transform:translateX(3px)}}"
           ".rf{animation:rf 2.6s steps(3) infinite}")
    return svg(W, H, "".join(b), "Thanks for visiting. Ship fewer things. Ship them well.", css)


def write(rel, data):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)
    return rel


if __name__ == "__main__":
    made = []
    for theme, dark in (("dark", True), ("light", False)):
        made.append(write(f"name-{theme}.svg", wordmark(dark)))
        for key, label in HEADERS.items():
            made.append(write(f"headers/{key}-{theme}.svg", header(label, dark)))
    made.append(write("footer.svg", footer()))
    made.append(write("bullet.svg", bullet()))
    for key, (label, icon) in STACK.items():
        made.append(write(f"stack/{key}.svg", chip(label, icon)))
    for key, label in LINKS.items():
        made.append(write(f"links/{key}.svg", chip(label, arrow=True)))
    print(f"wrote {len(made)} files to assets/")
