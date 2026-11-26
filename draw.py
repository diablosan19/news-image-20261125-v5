#!/usr/bin/env python3
"""Draw the news-image-20261125 front page (1024x1024) from scratch.

Every story below was verified by the build agent against two wire or
primary sources carrying a 25 November 2026 first-report date. Numbers
in decks match the headlines exactly. Prior-day stories are listed only
in the printed DATE CHECK box, never as headlines.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
MUTED = (90, 86, 78)
RED = (178, 32, 44)
BLUE = (29, 78, 137)
TEAL = (14, 110, 110)
GOLD = (176, 132, 24)
GREEN = (46, 110, 54)
RULE = (200, 192, 176)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FSB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# (headline, deck, region, utc, label, field, icon)
STORIES = [
    ("Judges urge dropping Netanyahu bribery case",
     "Court says Case 4000 conviction unlikely; AG to weigh it",
     "ISRAEL", "19:28", "CONFIRMED", "law", "scales"),
    ("Poland plans no-fly zone on Ukraine border",
     "Warsaw acts after Russian incursions; presses NATO on intercepts",
     "POLAND", "19:22", "CONFIRMED", "defence", "shield"),
    ("Saudi coalition strikes Hodeidah port",
     "Coalition hits port after evacuation warning; Saada, Amran hit too",
     "YEMEN", "00:08", "OFFICIAL", "conflict", "burst"),
    ("Houthis claim Ras Tanura refinery hit",
     "Smoke seen by satellite; Riyadh confirms no hit at refinery",
     "SAUDI ARABIA", "16:59", "CLAIM", "energy", "flame"),
    ("Saudis down 7 Houthi drones over Ras Tanura",
     "Four downed over oil port, three more in Eastern Province",
     "SAUDI ARABIA", "08:00", "CONFIRMED", "defence", "shield"),
    ("Iran says 2 tankers hit mines in Hormuz",
     "IRGC claims blasts in engine rooms; no independent confirmation",
     "STRAIT OF HORMUZ", "09:46", "CLAIM", "energy", "flame"),
    ("US tells citizens to leave Iran now",
     "Alert warns hostilities could escalate fast across the region",
     "IRAN", "14:41", "OFFICIAL", "diplomacy", "flag"),
    ("Ukraine hits 2 Russian refineries in Samara",
     "Kuibyshev and Syzran plants ablaze after overnight drone strikes",
     "RUSSIA", "02:12", "REPORTED", "energy", "flame"),
    ("Ukraine says 5 jets hit at Russian airbase",
     "MiG-31s and Su-34s damaged at Savasleyka, General Staff says",
     "RUSSIA", "06:30", "REPORTED", "defence", "plane"),
    ("Leaked files point to 490,334 Russian war dead",
     "BBC and Mediazona count Rosstat records; Kremlin silent on toll",
     "RUSSIA", "10:00", "REPORTED", "conflict", "burst"),
    ("31 killed as fuel tanker fire engulfs Cairo road",
     "Tanker overturns on Ring Road; 21 hurt, 27 vehicles charred",
     "EGYPT", "16:08", "CONFIRMED", "disaster", "flame"),
    ("Israeli strike kills Hamas security chief",
     "Mohammed Abu al-Ouf, wife and two daughters die in Gaza City",
     "GAZA", "05:00", "CONFIRMED", "conflict", "burst"),
    ("Iraq court backs Baghdad at Kurdish borders",
     "Top court lets federal troops secure all international borders",
     "IRAQ", "11:50", "OFFICIAL", "law", "scales"),
    ("RSF drone strikes kill 19 in Blue Nile",
     "Rights group reports toll in Damazin; 20 more wounded",
     "SUDAN", "10:40", "REPORTED", "conflict", "burst"),
    ("Fighting forces Ebola teams out in Congo",
     "WHO evacuates staff; outbreak tops 11,700 cases, 5,700 dead",
     "DR CONGO", "18:50", "CONFIRMED", "health", "cross"),
    ("Bangladesh lifts garment wage 36%",
     "Board sets 17,000 taka floor after weeks of protests",
     "BANGLADESH", "09:46", "CONFIRMED", "labour", "gear"),
    ("9 dead, 17 trapped in flooded Java gold mine",
     "Rescuers pull nine bodies from illegal Bogor shaft",
     "INDONESIA", "05:25", "CONFIRMED", "disaster", "drop"),
    ("Cartagena siege ends: all hostages freed",
     "Troops storm supermarket; one gunman killed, four held",
     "COLOMBIA", "16:27", "CONFIRMED", "crime", "lens"),
    ("N. Korea expels Swiss diplomat in 48 hours",
     "Pyongyang shuts office weeks after reopening in sanctions row",
     "NORTH KOREA", "06:05", "CONFIRMED", "diplomacy", "flag"),
    ("Shenzhou-24 carries 1st foreign astronaut",
     "Pakistan's Zeeshan Ali docks at Tiangong space station",
     "CHINA", "00:18", "OFFICIAL", "space", "rocket"),
    ("Solomons sign security pact with Australia",
     "No foreign bases; A$740m over 10 years for Honiara",
     "PACIFIC", "06:29", "OFFICIAL", "diplomacy", "flag"),
    ("Murmansk governor held in graft case",
     "Court orders 2 months' custody; Putin ends his powers",
     "RUSSIA", "11:00", "CONFIRMED", "law", "scales"),
    ("Second judge blocks birthright citizenship order",
     "DC court bars Trump order for children in class action",
     "USA", "17:00", "CONFIRMED", "law", "scales"),
    ("Wall Street slides as tariffs land",
     "Nasdaq ends down 0.6% after 4% plunge; Dow climbs 0.3%",
     "USA", "21:00", "CONFIRMED", "markets", "bars"),
    ("Army blows up lead explosive stock in Iowa",
     "5 tons of lead azide detonated; no lead found in air",
     "USA", "15:00", "CONFIRMED", "defence", "burst"),
    ("Six found dead after plane crash off Mississippi",
     "Family of six named; Cessna went down in the Gulf",
     "USA", "06:14", "CONFIRMED", "disaster", "plane"),
    ("Duran Duran guitarist Andy Taylor dies at 65",
     "Band announces death; he died Monday after cancer fight",
     "UNITED KINGDOM", "21:51", "CONFIRMED", "culture", "note"),
    ("Abrego Garcia reaches Spain",
     "Salvadoran lands in Madrid after leaving US under deal",
     "SPAIN", "09:19", "CONFIRMED", "immigration", "plane"),
    ("Lebanon to open second airport next month",
     "Kleiat gateway to serve north; flights to Turkey, Egypt, Jordan",
     "LEBANON", "12:00", "CONFIRMED", "infrastructure", "plane"),
]

LEAD = ("US proposes new tariffs on 14 partners",
        "Washington targets China, the EU and 12 more over excess factory "
        "capacity.",
        "WASHINGTON", "18:00", "OFFICIAL")

# Prior-day stories, named and excluded (never headlines).
DATE_CHECK = [
    ("COP31 climate talks collapse", "22 Nov"),
    ("Riyadh tower Houthi strike, 11 hurt", "24 Nov"),
    ("Huawei trade-secrets conviction", "24 Nov"),
    ("CIA cyber breach", "24 Nov"),
    ("Zelenskyy EUR115bn plea for 2027", "24 Nov"),
    ("UK sabotage warning to firms", "24 Nov"),
    ("Chen Jining graft probe announced", "24 Nov"),
    ("Miss Universe crowned in San Juan", "24 Nov"),
]

REGIONS = ["N. AMERICA", "S. AMERICA", "EUROPE", "MIDDLE EAST", "AFRICA",
           "S. ASIA", "E. ASIA", "SE ASIA", "OCEANIA"]


def wrap(d, text, f, max_w):
    """Word-boundary wrap; never splits a word."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(d, text, f, max_w, max_lines):
    """Wrap to at most max_lines, dropping whole words from the end."""
    lines = wrap(d, text, f, max_w)
    while len(lines) > max_lines:
        words = lines[-1].split()
        if len(words) > 1:
            lines[-1] = " ".join(words[:-1])
            lines = wrap(d, " ".join(lines), f, max_w)
        else:
            lines = lines[:-1]
    return lines


def fit_one_line(d, text, f, max_w):
    """Shorten to one line by dropping whole words, never mid-word."""
    while d.textlength(text, font=f) > max_w and " " in text:
        text = text.rsplit(" ", 1)[0]
    if d.textlength(text, font=f) > max_w:
        text = text[:max(0, int(max_w / 6))]
    return text


def label_color(label):
    return {"OFFICIAL": BLUE, "CONFIRMED": GREEN,
            "REPORTED": GOLD, "CLAIM": RED}[label]


def draw_icon(d, kind, x, y, s, color):
    """Small drawn glyph in a coloured square; shapes only, no photos."""
    d.rectangle([x, y, x + s, y + s], fill=color)
    c = (255, 255, 255)
    p = s / 10.0
    if kind == "scales":
        d.line([x + 5 * p, y + 2 * p, x + 5 * p, y + 8 * p], fill=c, width=2)
        d.line([x + 2 * p, y + 3 * p, x + 8 * p, y + 3 * p], fill=c, width=2)
        d.polygon([(x + 1 * p, y + 6 * p), (x + 3 * p, y + 6 * p),
                   (x + 2 * p, y + 4 * p)], outline=c)
        d.polygon([(x + 7 * p, y + 6 * p), (x + 9 * p, y + 6 * p),
                   (x + 8 * p, y + 4 * p)], outline=c)
    elif kind == "shield":
        d.polygon([(x + 5 * p, y + 1.5 * p), (x + 8.5 * p, y + 3 * p),
                   (x + 8.5 * p, y + 6 * p), (x + 5 * p, y + 8.5 * p),
                   (x + 1.5 * p, y + 6 * p), (x + 1.5 * p, y + 3 * p)],
                  outline=c, width=2)
        d.line([x + 5 * p, y + 3 * p, x + 5 * p, y + 7 * p], fill=c, width=2)
    elif kind == "burst":
        for ang in range(0, 360, 45):
            import math
            r1, r2 = 2.2 * p, 4.2 * p
            a = math.radians(ang)
            d.line([x + 5 * p + r1 * math.cos(a), y + 5 * p + r1 * math.sin(a),
                    x + 5 * p + r2 * math.cos(a), y + 5 * p + r2 * math.sin(a)],
                   fill=c, width=2)
        d.ellipse([x + 3.5 * p, y + 3.5 * p, x + 6.5 * p, y + 6.5 * p], fill=c)
    elif kind == "flame":
        d.polygon([(x + 5 * p, y + 1.5 * p), (x + 7.5 * p, y + 5 * p),
                   (x + 6.5 * p, y + 5 * p), (x + 8 * p, y + 8.5 * p),
                   (x + 2 * p, y + 8.5 * p), (x + 3.5 * p, y + 5 * p),
                   (x + 2.5 * p, y + 5 * p)], fill=c)
    elif kind == "flag":
        d.line([x + 3 * p, y + 1.5 * p, x + 3 * p, y + 8.5 * p], fill=c, width=2)
        d.polygon([(x + 3 * p, y + 1.5 * p), (x + 8 * p, y + 3 * p),
                   (x + 3 * p, y + 4.5 * p)], fill=c)
    elif kind == "cross":
        d.rectangle([x + 4 * p, y + 2 * p, x + 6 * p, y + 8 * p], fill=c)
        d.rectangle([x + 2 * p, y + 4 * p, x + 8 * p, y + 6 * p], fill=c)
    elif kind == "gear":
        d.ellipse([x + 2.5 * p, y + 2.5 * p, x + 7.5 * p, y + 7.5 * p],
                  outline=c, width=2)
        d.ellipse([x + 4 * p, y + 4 * p, x + 6 * p, y + 6 * p], fill=c)
        for ang in range(0, 360, 60):
            import math
            a = math.radians(ang)
            d.line([x + 5 * p + 3.6 * p * math.cos(a),
                    y + 5 * p + 3.6 * p * math.sin(a),
                    x + 5 * p + 4.6 * p * math.cos(a),
                    y + 5 * p + 4.6 * p * math.sin(a)], fill=c, width=2)
    elif kind == "drop":
        d.polygon([(x + 5 * p, y + 1.5 * p), (x + 8 * p, y + 6 * p),
                   (x + 2 * p, y + 6 * p)], fill=c)
        d.ellipse([x + 2.5 * p, y + 5 * p, x + 7.5 * p, y + 8.5 * p], fill=c)
    elif kind == "lens":
        d.ellipse([x + 1.5 * p, y + 1.5 * p, x + 6.5 * p, y + 6.5 * p],
                  outline=c, width=2)
        d.line([x + 6 * p, y + 6 * p, x + 8.5 * p, y + 8.5 * p], fill=c, width=2)
    elif kind == "rocket":
        d.polygon([(x + 5 * p, y + 1 * p), (x + 7 * p, y + 4.5 * p),
                   (x + 6 * p, y + 7 * p), (x + 4 * p, y + 7 * p),
                   (x + 3 * p, y + 4.5 * p)], fill=c)
        d.polygon([(x + 4 * p, y + 7 * p), (x + 6 * p, y + 7 * p),
                   (x + 5 * p, y + 9 * p)], fill=(255, 200, 60))
    elif kind == "bars":
        for i, h in enumerate((3, 6, 4.5, 8)):
            d.rectangle([x + (1.5 + i * 2) * p, y + (9 - h) * p,
                         x + (3 + i * 2) * p, y + 9 * p], fill=c)
    elif kind == "note":
        d.ellipse([x + 2.5 * p, y + 6.5 * p, x + 4.5 * p, y + 8.5 * p], fill=c)
        d.line([x + 4.5 * p, y + 7 * p, x + 4.5 * p, y + 2 * p], fill=c, width=2)
        d.line([x + 4.5 * p, y + 2 * p, x + 7.5 * p, y + 3.5 * p], fill=c, width=2)
        d.line([x + 7.5 * p, y + 3.5 * p, x + 7.5 * p, y + 7 * p], fill=c, width=2)
    elif kind == "plane":
        d.polygon([(x + 1 * p, y + 5 * p), (x + 5 * p, y + 3 * p),
                   (x + 9 * p, y + 5 * p), (x + 5 * p, y + 6.5 * p)], fill=c)
        d.polygon([(x + 4 * p, y + 6 * p), (x + 6 * p, y + 6 * p),
                   (x + 5 * p, y + 8.5 * p)], fill=c)
    else:
        d.ellipse([x + 2 * p, y + 2 * p, x + 8 * p, y + 8 * p], outline=c, width=2)


FIELD_COLOR = {
    "law": BLUE, "defence": (90, 40, 40), "conflict": RED,
    "energy": GOLD, "diplomacy": TEAL, "disaster": (120, 60, 10),
    "health": GREEN, "labour": (110, 60, 120), "crime": (60, 60, 60),
    "space": (40, 40, 110), "markets": (20, 90, 60),
    "culture": (150, 60, 90), "immigration": TEAL,
    "infrastructure": (80, 80, 90),
}


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- Masthead ----------
    d.rectangle([0, 0, W, 10], fill=INK)
    d.text((512, 26), "THE WORLD IN ONE PAGE", font=font(FB, 17),
           fill=RED, anchor="ma")
    d.text((512, 50), "Wednesday 25 November 2026", font=font(FSB, 38),
           fill=INK, anchor="ma")
    d.line([24, 96, 1000, 96], fill=INK, width=2)
    d.text((512, 104), "30 STORIES  •  9 REGIONS  •  14 FIELDS  •  "
           "EVERY STORY FIRST REPORTED 25 NOV 2026",
           font=font(FB, 13), fill=MUTED, anchor="ma")

    # ---------- Lead story ----------
    ly = 128
    d.rectangle([16, ly, 1008, ly + 92], outline=RULE, width=1)
    d.rectangle([16, ly, 1008, ly + 92], fill=(255, 255, 255))
    d.rectangle([16, ly, 22, ly + 92], fill=RED)
    hl, deck, region, utc, label = LEAD
    d.text((36, ly + 8), "LEAD", font=font(FB, 11), fill=RED)
    d.text((36, ly + 26), hl, font=font(FB, 27), fill=INK)
    d.text((36, ly + 58), deck, font=font(FR, 13), fill=MUTED)
    d.text((36, ly + 76), "WASHINGTON  •  18:00 UTC  •  OFFICIAL",
           font=font(FB, 11), fill=BLUE)
    # Lead stat panel + drawn ship scene, right side.
    px, py = 700, ly + 10
    d.rectangle([px, py, px + 292, py + 72], outline=BLUE, width=2)
    d.text((px + 12, py + 6), "14 PARTNERS  •  CHINA 20%  •  EU 15%",
           font=font(FB, 13), fill=INK)
    d.text((px + 12, py + 26), "Section 301 probe  •  hearings 25 Jan 2027",
           font=font(FR, 11), fill=MUTED)
    for i, cx in enumerate((px + 16, px + 52, px + 88)):
        d.rectangle([cx, py + 46, cx + 30, py + 66],
                    fill=[RED, BLUE, GOLD][i])
    d.rectangle([px + 130, py + 46, px + 280, py + 66], fill=(30, 60, 90))
    d.text((px + 136, py + 50), "TRADE  •  USTR", font=font(FB, 11),
           fill=(255, 255, 255))

    # ---------- Story grid: 29 cards, 3 columns x 10 rows ----------
    gx, gy, cw, ch, gapx, gapy = 8, 228, 330, 57, 8, 1
    for i, (hl, deck, region, utc, label, field, icon) in enumerate(STORIES):
        col, row = i % 3, i // 3
        x = gx + col * (cw + gapx)
        y = gy + row * (ch + gapy)
        d.rectangle([x, y, x + cw, y + ch], fill=(255, 255, 255),
                    outline=RULE, width=1)
        draw_icon(d, icon, x + 5, y + 8, 40, FIELD_COLOR[field])
        tx = x + 52
        lines = fit_lines(d, hl, font(FB, 13), cw - 60, 2)
        yy = y + 3
        for ln in lines:
            d.text((tx, yy), ln, font=font(FB, 13), fill=INK)
            yy += 15
        d.text((tx, y + 33), fit_one_line(d, deck, font(FR, 10), cw - 60),
               font=font(FR, 10), fill=MUTED)
        d.text((tx, y + 45),
               "%s  •  %s UTC  •  %s" % (region, utc, label),
               font=font(FB, 9), fill=label_color(label))

    # ---------- UTC timeline strip ----------
    ty = 812
    d.text((16, ty), "UTC TIMELINE — FIRST WIRE, 25 NOV",
           font=font(FB, 11), fill=INK)
    d.line([16, ty + 26, 1008, ty + 26], fill=INK, width=2)
    for h in range(0, 25, 4):
        tx = 16 + h / 24.0 * 992
        d.line([tx, ty + 22, tx, ty + 30], fill=INK, width=2)
        d.text((tx, ty + 32), "%02d:00" % h, font=font(FR, 9),
               fill=MUTED, anchor="ma")
    for (hl, deck, region, utc, label, field, icon) in STORIES:
        hh, mm = int(utc[:2]), int(utc[3:])
        tx = 16 + (hh + mm / 60.0) / 24.0 * 992
        d.ellipse([tx - 3, ty + 23, tx + 3, ty + 29],
                  fill=label_color(label))
    lh, lm = int(LEAD[3][:2]), int(LEAD[3][3:])
    tx = 16 + (lh + lm / 60.0) / 24.0 * 992
    d.ellipse([tx - 4, ty + 22, tx + 4, ty + 30], outline=RED, width=2)

    # ---------- DATE CHECK box ----------
    dy = 858
    d.rectangle([16, dy, 1008, dy + 88], outline=RED, width=2)
    d.rectangle([16, dy, 1008, dy + 22], fill=RED)
    d.text((28, dy + 4), "DATE CHECK — THESE ARE NOT TODAY'S NEWS: "
           "FIRST REPORTED EARLIER, EXCLUDED FROM THIS PAGE",
           font=font(FB, 12), fill=(255, 255, 255))
    for i, (name, day) in enumerate(DATE_CHECK):
        col, row = i % 2, i // 2
        x = 28 + col * 490
        y = dy + 28 + row * 14
        d.text((x, y), "✕  %s — first reported %s — excluded"
               % (name, day), font=font(FR, 11), fill=INK)

    # ---------- Footer: pin map + sources ----------
    fy = 956
    d.line([16, fy, 1008, fy], fill=INK, width=2)
    # Simplified world map: continent blobs with numbered region pins.
    mx, my = 16, fy + 8
    d.rectangle([mx, my, mx + 330, my + 44], outline=RULE, width=1)
    blobs = [(18, 6, 62, 20), (70, 12, 118, 30), (130, 5, 200, 24),
             (205, 10, 250, 26), (255, 6, 322, 30)]
    for (bx0, by0, bx1, by1) in blobs:
        d.ellipse([mx + bx0, my + by0, mx + bx1, my + by1],
                  fill=(190, 205, 220))
    pins = [(30, 20), (52, 30), (100, 14), (150, 18), (180, 26),
            (225, 16), (255, 24), (285, 18), (305, 30)]
    for n, (px_, py_) in enumerate(pins, 1):
        d.ellipse([mx + px_ - 6, my + py_ - 6, mx + px_ + 6, my + py_ + 6],
                  fill=RED)
        d.text((mx + px_, my + py_), str(n), font=font(FB, 8),
               fill=(255, 255, 255), anchor="mm")
    d.text((mx + 4, my + 48), "9 REGIONS PINNED ABOVE",
           font=font(FB, 8), fill=MUTED)
    fx = 370
    d.text((fx, fy + 8), "SOURCES: REUTERS • AP • AFP • BBC • XINHUA • "
           "OFFICIAL STATEMENTS", font=font(FB, 11), fill=INK)
    d.text((fx, fy + 26), "Every headline carries two wire sources dated "
           "25 Nov 2026. Claims are labelled CLAIM,",
           font=font(FR, 11), fill=MUTED)
    d.text((fx, fy + 40), "unverified reports REPORTED. Drawn scenes only "
           "— no photographs.",
           font=font(FR, 11), fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
