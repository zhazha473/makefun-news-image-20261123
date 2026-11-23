#!/usr/bin/env python3
"""Draw the news-image-20261123 entry: THE WORLD DEPARTURES BOARD.

Fresh code written in this session. Deterministic: no clock, no randomness,
no network. Draws entry.png (1024x1024) from the verified story list below.

Verified 23 November 2026 stories (each re-checked by web search in this
session; anything from 21-22 Nov was excluded and named in the DATE CHECK
strip instead):
 1. WELLINGTON - NZ v India, day 5 live: NZ 139/4, trail by 213 (Cricinfo)
 2. CANBERRA - Newspoll: Albanese trails Taylor as preferred PM, first time;
    net approval -31 (Guardian Australia, Mon 23 Nov)
 3. CANBERRA - PBS medicines frozen at $25 until 2030 (Guardian Australia)
 4. CANBERRA - Small business exempt from digital duty of care (Guardian AU)
 5. CANBERRA - Parliament's last sitting week of 2026 opens (The Squiz)
 6. BRUSSELS - NATO council meets today on Poland airspace violation
    (Reuters: meeting Monday)
 7. NEW DELHI - Nepal PM Shah holds talks with PM Modi today (MEA / IANS)
 8. TOKYO - Markets closed all day for Labor Thanksgiving Day (JPX)
 9. CIKANDE - Search for factory-fire missing resumes 07:00 (Reuters)
10. COP31 FALLOUT - Canberra rows over the failed deal (Guardian AU, Mon)
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
REPORT_TIME = "00:15 UTC"

# ---- palette: split-flap departures board ----
BG       = (16, 20, 24)      # near-black board
PANEL    = (24, 30, 36)      # flap panel
PANEL2   = (30, 38, 46)      # alternating flap panel
AMBER    = (245, 178, 66)    # flap amber
AMBER_D  = (214, 148, 40)
WHITE    = (240, 238, 230)
MUTED    = (168, 178, 186)
GREEN    = (120, 200, 130)   # LIVE
RED      = (235, 96, 86)     # BREAKING
BLUE     = (110, 180, 235)   # SCHEDULED
GREY     = (150, 158, 166)
LINE     = (58, 66, 74)
HERO_BG  = (18, 46, 30)      # Basin Reserve green
HERO_PITCH = (196, 172, 120)
STRIP_BG = (74, 28, 24)      # date-check strip

F_MONO      = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
F_MONO_B    = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
F_SANS      = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_B    = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

# ---- board rows: (code, city, headline, detail, time, tag, tag_colour, source)
ROWS = [
    ("CBR", "CANBERRA",
     "Newspoll: Albanese trails Taylor as PM pick",
     "PM's net approval hits a record low of minus 31",
     "09:04 AEDT", "BREAKING", RED, "Guardian AU"),
    ("CBR", "CANBERRA",
     "PBS medicines frozen at $25 until 2030",
     "Price cap on prescriptions extended in last sitting week",
     "TODAY", "LANDED", GREEN, "Guardian AU"),
    ("CBR", "CANBERRA",
     "Small firms exempt from digital duty of care",
     "Carve-out after business groups warned of compliance costs",
     "TODAY", "LANDED", GREEN, "Guardian AU"),
    ("CBR", "CANBERRA",
     "Parliament's last sitting week of 2026 opens",
     "Gas reservation, tax and health bills crowd the final days",
     "TODAY", "BOARDING", AMBER, "The Squiz"),
    ("BRU", "BRUSSELS",
     "NATO council meets on Poland airspace breach",
     "Three Russian Kh-101 missiles flew into Poland on Friday",
     "TODAY", "SCHEDULED", BLUE, "Reuters"),
    ("DEL", "NEW DELHI",
     "Nepal PM Shah holds talks with PM Modi today",
     "First bilateral visit: energy, trade and connectivity on the table",
     "TODAY", "SCHEDULED", BLUE, "MEA / IANS"),
    ("TYO", "TOKYO",
     "Tokyo markets shut for Labor Thanksgiving Day",
     "Tokyo closed until Tuesday after Nikkei's 5% slide on Friday",
     "ALL DAY", "HELD", GREY, "JPX"),
    ("CKN", "CIKANDE",
     "Cikande search for fire missing resumes 07:00",
     "24 body bags recovered so far; 29 workers still missing",
     "07:00 WIB", "SCHEDULED", BLUE, "Reuters"),
    ("CBR", "CANBERRA",
     "COP31 fallout: Canberra rows over failed deal",
     "Liberals blast $150m co-host role; Bowen says lines were unbridgeable",
     "TODAY", "LANDED", GREEN, "Guardian AU"),
]

DATE_CHECK = (
    "NOT TODAY, LEFT OUT ON PURPOSE:  COP31 collapse (22 Nov)  |  "
    "Liverpool 4-0 Man Utd (22 Nov)  |  India 720/9 declared (22 Nov)  |  "
    "Kyiv strike, 14 missing (22 Nov)  |  UN killer-robot talks end (21 Nov)  |  "
    "'El Chapo Isidro' captured (21 Nov)  |  Seoul minister quits (22 Nov)  |  "
    "Benghazi warship sunk (22 Nov)  |  Sparta II towed out (22 Nov)"
)

FOOTER = (
    "STILL TO COME TODAY:  NATO decision  |  US markets open  |  "
    "Korea confidence 16:00 EST  |  Nifty expiry"
)

def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_hero_scene(d):
    """Drawn Basin Reserve scene: green oval, pitch, stumps, batsman, bowler."""
    x0, y0, x1, y1 = 28, 128, 668, 300
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=HERO_BG,
                        outline=LINE, width=2)
    # outfield shading + boundary rope
    d.ellipse([x0 + 30, y0 + 18, x1 - 30, y1 - 14], outline=(90, 150, 100),
              width=2)
    d.ellipse([x0 + 60, y0 + 34, x1 - 60, y1 - 30], fill=(24, 60, 38))
    # pitch strip
    d.rectangle([300, y0 + 40, 400, y1 - 34], fill=HERO_PITCH)
    d.rectangle([300, y0 + 40, 400, y1 - 34], outline=(150, 128, 84), width=1)
    # crease lines
    d.line([300, y0 + 62, 400, y0 + 62], fill=(255, 255, 255), width=2)
    d.line([300, y1 - 56, 400, y1 - 56], fill=(255, 255, 255), width=2)
    # stumps at both ends (three thin amber lines + bails)
    for sx in (332, 340, 348):
        d.line([sx, y0 + 44, sx, y0 + 60], fill=(245, 200, 90), width=3)
    for sx in (332, 340, 348):
        d.line([sx, y1 - 52, sx, y1 - 36], fill=(245, 200, 90), width=3)
    # batsman silhouette at the crease (dark figure + bat)
    bx, by = 372, y1 - 96
    d.ellipse([bx - 7, by - 34, bx + 7, by - 20], fill=(12, 14, 16))       # head
    d.line([bx, by - 20, bx - 2, by + 6], fill=(12, 14, 16), width=7)      # body
    d.line([bx - 2, by + 6, bx - 10, by + 26], fill=(12, 14, 16), width=5) # legs
    d.line([bx - 2, by + 6, bx + 8, by + 26], fill=(12, 14, 16), width=5)
    d.line([bx, by - 14, bx + 16, by + 2], fill=(12, 14, 16), width=5)     # arms+bat
    d.rectangle([bx + 14, by + 0, bx + 22, by + 18], fill=(210, 180, 120)) # bat
    # bowler silhouette mid-pitch
    wx, wy = 330, y0 + 78
    d.ellipse([wx - 6, wy - 12, wx + 6, wy], fill=(12, 14, 16))
    d.line([wx, wy, wx + 2, wy + 22], fill=(12, 14, 16), width=6)
    d.line([wx + 2, wy + 22, wx - 6, wy + 40], fill=(12, 14, 16), width=4)
    d.line([wx + 2, wy + 22, wx + 10, wy + 40], fill=(12, 14, 16), width=4)
    d.line([wx, wy + 4, wx + 16, wy - 6], fill=(12, 14, 16), width=4)
    # ball in flight
    d.ellipse([356, y0 + 66, 362, y0 + 72], fill=(235, 96, 86))
    # scoreboard strip inside the scene
    d.rectangle([x0 + 14, y1 - 30, x1 - 14, y1 - 12], fill=(10, 14, 12))
    d.text((x0 + 24, y1 - 28), "BASIN RESERVE, WELLINGTON  -  DAY 5, SESSION 1",
           font=font(F_MONO, 13), fill=MUTED)

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 112], fill=(10, 12, 14))
    d.text((28, 12), "THE WORLD", font=font(F_MONO_B, 26), fill=MUTED)
    d.text((28, 38), "DEPARTURES BOARD", font=font(F_MONO_B, 46), fill=AMBER)
    d.text((W - 28, 16), "MONDAY 23 NOVEMBER 2026",
           font=font(F_MONO_B, 22), fill=WHITE, anchor="ra")
    d.text((W - 28, 44), "FIRST EDITION - AS REPORTED BY " + REPORT_TIME,
           font=font(F_MONO, 16), fill=MUTED, anchor="ra")
    d.text((W - 28, 68), "10 STORIES  |  6 CITIES  |  ALL TIMES LOCAL",
           font=font(F_MONO_B, 15), fill=AMBER, anchor="ra")
    d.line([0, 112, W, 112], fill=AMBER, width=3)

    # ---------- hero: Wellington Test ----------
    draw_hero_scene(d)
    hx = 692
    d.text((hx, 130), "WLG", font=font(F_MONO_B, 20), fill=AMBER)
    d.text((hx, 154), "WELLINGTON", font=font(F_MONO_B, 24), fill=WHITE)
    d.text((hx, 184), "NEW ZEALAND BAT", font=font(F_MONO_B, 21), fill=WHITE)
    d.text((hx, 208), "TO SAVE THE TEST", font=font(F_MONO_B, 21), fill=WHITE)
    d.text((hx, 236), "NZ 139/4 - trail by 213", font=font(F_MONO_B, 19),
           fill=AMBER)
    d.text((hx, 260), "Conway 59*  Ravindra 37",
           font=font(F_MONO, 15), fill=MUTED)
    # LIVE tag
    tag = "LIVE"
    tw = d.textlength(tag, font=font(F_MONO_B, 15))
    d.rounded_rectangle([hx, 280, hx + tw + 16, 300], radius=4,
                        fill=GREEN)
    d.text((hx + 8, 282), tag, font=font(F_MONO_B, 15), fill=(10, 20, 12))
    d.text((hx + tw + 26, 282), "Cricinfo",
           font=font(F_MONO, 14), fill=MUTED)

    # ---------- board header ----------
    y = 316
    d.text((28, y), "FLT", font=font(F_MONO_B, 14), fill=MUTED)
    d.text((84, y), "DESTINATION", font=font(F_MONO_B, 14), fill=MUTED)
    d.text((700, y), "TIME", font=font(F_MONO_B, 14), fill=MUTED)
    d.text((800, y), "STATUS", font=font(F_MONO_B, 14), fill=MUTED)
    d.text((920, y), "SOURCE", font=font(F_MONO_B, 14), fill=MUTED)
    d.line([28, y + 22, W - 28, y + 22], fill=LINE, width=1)

    # ---------- board rows ----------
    y = 346
    row_h = 56
    f_head = font(F_MONO_B, 16)
    f_det = font(F_MONO, 13)
    f_city = font(F_MONO_B, 16)
    f_code = font(F_MONO_B, 16)
    f_time = font(F_MONO_B, 14)
    f_tag = font(F_MONO_B, 13)
    f_src = font(F_MONO, 12)
    for i, (code, city, head, det, t, tag, tcol, src) in enumerate(ROWS):
        fill = PANEL if i % 2 == 0 else PANEL2
        d.rounded_rectangle([20, y, W - 20, y + row_h - 6], radius=6, fill=fill)
        d.text((30, y + 8), code, font=f_code, fill=AMBER)
        d.text((84, y + 6), city, font=f_city, fill=WHITE)
        d.text((84, y + 28), det, font=f_det, fill=MUTED)
        # headline: single line, fitted to the 230-690 column
        # (headlines are written short enough to fit one line; if a wrap
        # ever produced a second line it would collide with the detail
        # line below, so only line 0 is ever drawn)
        lines = wrap(d, head, f_head, 450)
        d.text((230, y + 6), lines[0], font=f_head, fill=WHITE)
        d.text((700, y + 10), t, font=f_time, fill=AMBER)
        # status tag pill
        tw = d.textlength(tag, font=f_tag)
        d.rounded_rectangle([800, y + 8, 800 + tw + 12, y + 28], radius=4,
                            outline=tcol, width=1)
        d.text((806, y + 11), tag, font=f_tag, fill=tcol)
        d.text((920, y + 10), src, font=f_src, fill=MUTED)
        y += row_h

    # ---------- date check strip ----------
    sy = y + 6
    d.rounded_rectangle([20, sy, W - 20, sy + 80], radius=8, fill=STRIP_BG)
    d.text((32, sy + 8), "DATE CHECK", font=font(F_MONO_B, 15), fill=(255, 170, 150))
    lines = wrap(d, DATE_CHECK, font(F_MONO, 13), W - 64)
    ly = sy + 28
    for ln in lines[:3]:
        d.text((32, ly), ln, font=font(F_MONO, 13), fill=(245, 220, 210))
        ly += 15

    # ---------- footer ----------
    fy = sy + 90
    d.line([28, fy, W - 28, fy], fill=LINE, width=1)
    d.text((28, fy + 8), FOOTER, font=font(F_MONO_B, 14), fill=AMBER)
    note = ("Built 23 Nov 2026 from wire reports checked this session. Every story "
            "above happened or was first reported on 23 November 2026; the weekend's "
            "big stories are named in the strip above, not passed off as today's.")
    nlines = wrap(d, note, font(F_SANS, 12), W - 56)
    ny = fy + 30
    for ln in nlines:
        d.text((28, ny), ln, font=font(F_SANS, 12), fill=MUTED)
        ny += 15
    d.text((28, ny + 2),
           "Sources: Cricinfo  |  Guardian Australia  |  Reuters  |  MEA / IANS  |  JPX  |  The Squiz",
           font=font(F_SANS, 12), fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, img.size)

if __name__ == "__main__":
    main()
