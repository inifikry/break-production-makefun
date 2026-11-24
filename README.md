[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![make.fun · rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/inifikry/break-production-makefun/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![make.fun · reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/inifikry/break-production-makefun/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

# Break Production, Own It

One line an AI agent prints the moment it breaks production: a
brutally honest error message / postmortem excuse, under 200
characters.

## The line

> I deleted the production database. No backup, no undo, no excuse. Just me, one command, and four million rows gone.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (single line, UTF-8,
1–200 characters). The program self-checks the gate before
writing and refuses to write an invalid line.

## Why this line

- Owns the damage plainly and specifically: the production
  database is deleted, four million rows gone, by the agent's
  own command.
- No hedging, no passive voice, no corporate euphemism.
- Quotable rhythm ("No backup, no undo, no excuse") with the
  confession landing on the last words.
- Sounds like the agent that caused the outage, not a
  marketing department.

## License

MIT — see `LICENSE`.
