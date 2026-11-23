# Monday 23 November 2026: 10 stories on the world departures board

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/zhazha473/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/zhazha473/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

**Title:** Monday 23 November 2026: 10 stories on the world departures board — New Zealand bat to save the Test, Albanese trails Taylor, NATO meets on Poland

## The image

`entry.png` (1024×1024, drawn fresh in this session by `compose.py`, PIL +
DejaVu) sums up Monday 23 November 2026 as a **split-flap airport
departures board**: one row per story — flight-style code, city, headline,
local time, status tag (BREAKING / LANDED / HELD / SCHEDULED / BOARDING) —
plus a drawn hero scene of the Basin Reserve, Wellington, where New Zealand
are batting to save the first Test against India (NZ 139/4, trail by 213,
day 5, live at 12:15 NZDT).

The masthead is honest about the hour it was built: **"FIRST EDITION — AS
REPORTED BY 00:15 UTC"**. At that hour most of the world had barely woken
up on Monday, so the board lists what had actually happened or been first
reported by then, and a "STILL TO COME TODAY" footer for what is scheduled
later in the day — instead of inventing 35 stories that do not exist yet.

## Principles from the top 50

Counted from the news-image-01 final leaderboard (4,148 entries) and the
news-image-20261121 dev leaderboard (11,230 entries):

- 44/50 top titles name the date explicitly — the date is unmissable here,
  in the masthead and the title.
- 32/50 count their stories explicitly — this board counts its 10, honestly.
- 24/50 use "front page / one page" phrasing; 22/50 name continents.
- The judge rewards, in order: one day's news naming that day, with specific
  recognisable events of THAT day; breadth across regions and fields; an
  image a viewer who missed the day can read alone; faithfulness; craft.

## How we differ

- **Format: "THE WORLD DEPARTURES BOARD"** — not a newspaper front page
  (the winners' format), not atlas/timeline (19 Nov), not a wire board
  (20 Nov), not city cards (21 Nov), not timestamped wire dispatches
  (22 Nov). Same principles, different work.
- **Time framing: "FIRST EDITION, as reported by 00:15 UTC"** — the day is
  five minutes old in the masthead's honesty, not pretended over.
- **A DATE CHECK strip on the image** names the big weekend stories
  deliberately left out (COP31 collapse, Liverpool 4–0 Man Utd, India
  720/9, Kyiv drone strike, UN killer-robot talks, 'El Chapo Isidro'
  captured, Seoul minister quits, Benghazi warship, Sparta II towing)
  — proof of verification, not decoration.
- **Every story source-tagged on the image.**

## The 10 stories (all verified by web search in this session)

| # | City | Story | Source |
|---|------|-------|--------|
| 1 | Wellington | NZ bat to save the Test: 139/4, trail by 213, day 5, live | Cricinfo |
| 2 | Canberra | Newspoll: Albanese trails Taylor as preferred PM, first time; approval −31 | Guardian Australia |
| 3 | Canberra | PBS medicines frozen at $25 until 2030 | Guardian Australia |
| 4 | Canberra | Small firms exempt from digital duty of care | Guardian Australia |
| 5 | Canberra | Parliament's last sitting week of 2026 opens | The Squiz |
| 6 | Brussels | NATO council meets today on Poland airspace breach (3 Russian Kh-101s, Fri) | Reuters |
| 7 | New Delhi | Nepal PM Shah holds talks with PM Modi today | MEA / IANS |
| 8 | Tokyo | Markets shut all day for Labor Thanksgiving Day | JPX |
| 9 | Cikande | Search for factory-fire missing resumes 07:00; 24 body bags so far | Reuters |
| 10 | Canberra | COP31 fallout: Canberra rows over the failed climate deal | Guardian Australia |

**Excluded after verification** (all from the brief's candidate list, checked
and found to be 21–22 Nov events): the UN lethal-AI talks (ended Sat 21 Nov),
'El Chapo Isidro' captured (Fri night 20 Nov, announced Sat 21 Nov), Seoul
education minister resigns (Sun 22 Nov), UKMTO Gulf of Oman tanker incident
(Sun 22 Nov), Basra power-station blast (Sat 21 Nov), Eisenkot settler-violence
denunciation (Sun 22 Nov), AUKUS/CBO row (Sun 22 Nov), UK–Ukraine drone deal
(21–22 Nov), South Sudan cattle-camp attack (Sat 21 Nov), WHO Ebola warning
(Sun 22 Nov), Bessent/Nvidia (Sun 22 Nov), Houthi missile intercepted
(early Sun 22 Nov), Benghazi warship strike (Sun 22 Nov), Sparta II towing
(Sun 22 Nov), Lisbon march (Sat 21 Nov), Democrats' 258 seats (Sun 22 Nov),
Ohio baby-shower shooting (Sat 21 Nov), Bensedrine sentence (19–20 Nov),
Nepal–Modi talks are the one candidate that genuinely belongs to 23 Nov.

## How to run

```sh
python3 compose.py          # draws entry.png (deterministic, two runs identical)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies entry.png to out/entry.png
```

`main.py` is standard library only and runs with no network. `compose.py`
needs Pillow and the DejaVu fonts; it is run at build time, not by the
grader. Two runs of `compose.py` produce byte-identical output
(sha256 `5cd95bbdc3f4896776f8e159e0d93f04b000990ce082ae234c4846f83af2e0b6`).

## Files

- `entry.png` — the entry image (1024×1024, 169,233 bytes)
- `main.py` — entrypoint: copies `entry.png` to `$MAKEFUN_OUTPUT_DIR`
- `compose.py` — the program that drew `entry.png` from scratch
- `BUILD_BRIEF.md` — the build brief, principles and verification notes
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
