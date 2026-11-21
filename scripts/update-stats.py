"""Count solved problems by difficulty and by language in readme.md, redraw charts.

Usage: python3 scripts/update-stats.py
"""

import re
from collections import Counter
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "readme.md"
STATS_START, STATS_END = "<!-- stats:start -->", "<!-- stats:end -->"
LANG_START, LANG_END = "<!-- lang-stats:start -->", "<!-- lang-stats:end -->"

LEVEL_COLORS = {"Easy": "#00b8a3", "Medium": "#ffc01e", "Hard": "#ff375f"}
LANG_COLORS = {"Python": "#3776ab", "C": "#a8b9cc"}

text = README.read_text()

# Parse readme rows: "| <id> | ... | (Easy|Medium|Hard) |" and infer language from
# the solution link (main.c -> C, index.py -> Python).
levels = Counter()
langs = Counter()
for line in text.splitlines():
    if not line.startswith("|"):
        continue
    m = re.match(r"^\| \d+\*? \| .+? \| (Easy|Medium|Hard) \|", line)
    if not m:
        continue
    levels[m.group(1)] += 1
    if "main.c)" in line:
        langs["C"] += 1
    elif "index.py)" in line:
        langs["Python"] += 1

def make_chart(start, end, title, data, colors):
    slices = sorted(
        ((k, data[k]) for k in colors if data[k]), key=lambda x: -x[1]
    )
    theme = ", ".join(f'"pie{i}": "{colors[k]}"' for i, (k, _) in enumerate(slices, 1))
    lines = [
        start,
        "```mermaid",
        f'%%{{init: {{"themeVariables": {{{theme}}}}}}}%%',
        f"pie showData title {sum(data.values())} {title}",
        *(f'    "{k}" : {n}' for k, n in slices),
        "```",
        end,
    ]
    return "\n".join(lines)

# --- difficulty chart (existing block) ---
stats_chart = make_chart(STATS_START, STATS_END, "problems solved", levels, LEVEL_COLORS)
before, rest = text.split(STATS_START, 1)
after = rest.split(STATS_END, 1)[1]
text = before + stats_chart + after

# --- language chart (new block, inserted right after the stats block) ---
lang_chart = make_chart(LANG_START, LANG_END, "solutions by language", langs, LANG_COLORS)
if LANG_START in text:
    before, rest = text.split(LANG_START, 1)
    after = rest.split(LANG_END, 1)[1]
    text = before + lang_chart + after
else:
    # insert after the stats block
    marker = STATS_END
    idx = text.index(marker) + len(marker)
    text = text[:idx] + "\n\n" + lang_chart + text[idx:]

README.write_text(text)
print("levels:", ", ".join(f"{k}: {v}" for k, v in levels.items()))
print("langs:", ", ".join(f"{k}: {v}" for k, v in langs.items()))
