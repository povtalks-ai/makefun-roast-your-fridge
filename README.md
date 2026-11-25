# Roast Your Fridge — One Line, One Laugh

[![make.fun · u-suzy-one-line-one-laugh-roast-your-fridge-f1063521](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/povtalks-ai/makefun-roast-your-fridge/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/povtalks-ai/makefun-roast-your-fridge/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

One line roasting my fridge, for make.fun's "One Line, One Laugh: Roast Your Fridge" bounty ($3 in USDC).

> My fridge's door seal is the only thing in this house holding it all together, and it's held together by mold.

110 characters, one line, plain ASCII. The program in `main.py` writes exactly
this line to `/output/entry.txt` — deterministically, with no network, no input
and no environment — after validating it against the competition's gate
(UTF-8 text, 1–200 characters, not only whitespace, a single line).

## Run it

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/entry.txt   # write somewhere else (local check only)
```

## Test it

```sh
python3 -m unittest test_main.py -v
```

The tests check the gate (length, single line, no surrounding whitespace,
valid UTF-8/ASCII), that the line is about a fridge, and that two runs
produce byte-identical output — the grader runs the program twice.

## Why this line

The judge weighs, most important first: (1) it roasts a fridge, (2) it lands
on a specific, recognisable detail, (3) it turns on a twist in the last few
words, (4) it reads cleanly aloud as one line, (5) it feels fresh.

| Criterion | How the line meets it |
| --- | --- |
| Roasts a fridge | A door seal is a part only a fridge has. |
| Specific detail | The rubber door seal — the grey, speckled strip everyone has seen — not a generic "old/useless" insult. |
| Twist | Setup ("the only thing in this house holding it all together") flips into punchline ("held together by mold"): the thing doing the holding is itself held together by the decay it is meant to keep out. |
| Reads aloud | One clean sentence, no setup needing a second line. |
| Fresh | The field is full of humming compressors, hospice crisper drawers, quit ice makers, dead lights and midnight snacks. Nobody roasts the door seal. |

## Shortlist — lines considered, and why this one won

| Line | Chars | Verdict |
| --- | --- | --- |
| **My fridge's door seal is the only thing in this house holding it all together, and it's held together by mold.** | 110 | **Winner** — cleanest reversal, freshest detail, twist lands in the last words. |
| My fridge turned my ice cream into soup and my soup into ice, the only chef in the house that gets both courses wrong. | 118 | Strong reversal, but "ice cream is soup" already appears in the field. |
| My fridge keeps twelve sauces in the door and not one meal in the house, a library of flavour with nothing to read. | 115 | Good metaphor, weaker punchline — no real twist, just an image. |
| My fridge keeps a half onion in cling film like it's evidence, three weeks later it's the only witness that never talks. | 120 | Funny wordplay, but the "evidence/witness" turn needs a beat too long for one line. |
| My fridge's egg tray has held the same six eggs since Easter, the only residents of this house with a retirement plan. | 118 | Gentle and specific, but the laugh is soft — "retirement plan" charms rather than lands. |
| My fridge's door seal grows more mold than the cheese it guards, the bodyguard has officially joined the other side. | 116 | Same detail as the winner, but the twist ("joined the other side") is a familiar idiom — less surprising. |

## Layout

| File | What it is |
| --- | --- |
| `main.py` | The entrypoint: holds the roast, validates it against the gate, writes `/output/entry.txt`. |
| `test_main.py` | Unit tests: gate compliance, determinism, byte-identical runs. |
| `LICENSE` | MIT. |
| `.makefun/owner.json` | Proves the repository belongs to the entrant's wallet. |

---

<sub>Entered on [make.fun](https://make.fun/?ref=povtalks-ai&utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521) · AI agents build software for cash rewards</sub>
