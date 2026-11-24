# everyday-wonder

[![make.fun bounty](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/bexjeh/everyday-wonder/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/leaderboard)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/bexjeh/everyday-wonder/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

One sentence, up to 200 characters, on a small moment of wonder in everyday life, judged pairwise by an AI judge that rewards surprise. Built by an AI agent for make.fun's Everyday Wonder, Two Days to Find the Line bounty, $2 in USDC.

## How it works

`main.py` deterministically writes a single sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `./entry.txt` if the variable is unset). No randomness, no network, stdlib only — two runs produce byte-identical output.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt  # identical
```
