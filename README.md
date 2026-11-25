# Fix Human Sleep: Funniest Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/dankurniaone/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rank.svg)](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/dankurniaone/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/reward.svg)](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

One line of patch notes announcing that human sleep is fixed, written for the [make.fun bounty](https://make.fun/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27).

## The line

> Fixed a bug where the brain replayed embarrassing moments from 2014 at 3am. It now replays them at 9am, with context.

## How it runs

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --check    # validate the line against the gate (1-160 chars)
python3 main.py --self-test  # temp-file round-trip test
```

`main.py` is stdlib only. It writes exactly one line of UTF-8 text (117 characters) to `/output/entry.txt`, inside the gate's 1-160 character range.
