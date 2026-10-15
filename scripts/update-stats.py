"""Count solved problems by difficulty in readme.md and redraw the stats chart.

Usage: python3 scripts/update-stats.py
"""

import re
from collections import Counter
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "readme.md"
START, END = "<!-- stats:start -->", "<!-- stats:end -->"
COLORS = {"Easy": "#00b8a3", "Medium": "#ffc01e", "Hard": "#ff375f"}

text = README.read_text()
levels = Counter(re.findall(r"^\| \d+\*? \| .+? \| (Easy|Medium|Hard) \|", text, re.M))

# Mermaid colors pie slices by size order, so sort first and assign colors to match.
slices = sorted(((lvl, levels[lvl]) for lvl in COLORS if levels[lvl]), key=lambda x: -x[1])
theme = ", ".join(f'"pie{i}": "{COLORS[lvl]}"' for i, (lvl, _) in enumerate(slices, 1))

chart = "\n".join([
    START,
    "```mermaid",
    f"%%{{init: {{\"themeVariables\": {{{theme}}}}}}}%%",
    f"pie showData title {sum(levels.values())} problems solved",
    *(f'    "{lvl}" : {n}' for lvl, n in slices),
    "```",
    END,
])

before, rest = text.split(START, 1)
after = rest.split(END, 1)[1]
README.write_text(before + chart + after)
print(", ".join(f"{lvl}: {n}" for lvl, n in slices))
