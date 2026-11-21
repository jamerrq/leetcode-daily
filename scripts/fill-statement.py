"""Fill the problem statement, examples and constraints of src/<id>/readme.md from LeetCode.

Usage: python3 scripts/fill-statement.py <id> [<id> ...]

Only touches files whose statement, Examples and Constraints are still empty
(as left by the template); anything already filled in is skipped.

When src/<id>/index.py is still empty it also writes LeetCode's Python3
signature skeleton (the `class Solution:` and method lines), so the folder
starts with the correct method name. A solution body is never written.
"""

import json
import re
import subprocess
import sys
import textwrap
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMPTY = "\n\n## Examples\n\n## Constraints\n\n## My Solution"


class Markdown(HTMLParser):
    """Turns LeetCode's statement HTML into the markdown used in this repo's notes."""

    def __init__(self):
        super().__init__()
        self.out = []
        self.pre = False
        self.lists = []  # one entry per open list: item counter for <ol>, None for <ul>
        self.rows = None  # rows of the table being read, each a list of cells

    def close(self, marker):
        # keep trailing spaces outside the marker, so "*build *`x`" becomes "*build* `x`"
        text = "".join(self.out)
        body = text.rstrip(" ")
        self.out = [body + marker + " " * (len(text) - len(body))]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "table":
            self.rows = []
        elif self.rows is not None:
            if tag == "tr":
                self.rows.append([])
            elif tag in ("td", "th"):
                self.rows[-1].append("")
            elif tag == "code":
                self.cell("`")
        elif tag == "code" and not self.pre:
            self.out.append("`")
        elif tag in ("strong", "b") and not self.pre:
            self.out.append("**")
        elif tag == "em" and not self.pre:
            self.out.append("*")
        elif tag == "sup":
            self.out.append("^")
        elif tag == "sub":
            self.out.append("_")
        elif tag == "p" and not self.lists:
            self.out.append("\n\n")
        elif tag == "pre" or (tag == "div" and "example-block" in (attrs.get("class") or "")):
            self.pre = tag == "pre"
            self.out.append("\n\n")
        elif tag in ("ol", "ul"):
            self.lists.append(0 if tag == "ol" else None)
            self.out.append("\n")
        elif tag == "li":
            indent = "  " * (len(self.lists) - 1)
            if self.lists[-1] is None:
                self.out.append(f"\n{indent}- ")
            else:
                self.lists[-1] += 1
                self.out.append(f"\n{indent}{self.lists[-1]}. ")
        elif tag == "img":
            self.out.append(f"\n\n![]({attrs.get('src')})\n\n")
        elif tag == "br":
            self.out.append("\n")

    def cell(self, text):
        if self.rows and self.rows[-1]:
            self.rows[-1][-1] += text

    def handle_endtag(self, tag):
        if tag == "table":
            rows = [[" ".join(cell.split()) for cell in row] for row in self.rows if row]
            self.rows = None
            lines = ["| " + " | ".join(row) + " |" for row in rows]
            lines.insert(1, "|" + " --- |" * len(rows[0]))
            self.out.append("\n\n" + "\n".join(lines) + "\n\n")
        elif self.rows is not None:
            if tag == "code":
                self.cell("`")
        elif tag == "code" and not self.pre:
            self.close("`")
        elif tag in ("strong", "b") and not self.pre:
            self.close("**")
        elif tag == "em" and not self.pre:
            self.close("*")
        elif tag == "pre":
            self.pre = False
            self.out.append("\n\n")
        elif tag in ("ol", "ul"):
            self.lists.pop()
            self.out.append("\n" if self.lists else "\n\n")
        elif tag == "p" and not self.lists:
            self.out.append("\n\n")

    def handle_data(self, data):
        if self.rows is not None:
            self.cell(data)
            return
        if self.lists and not self.pre:
            # list items stay on one line; a lone space between tags is real text
            if data.strip():
                data = re.sub(r"\s*\n\s*", " ", data)
            else:
                data = "" if "\n" in data else " "
        self.out.append(data)


def to_markdown(html):
    parser = Markdown()
    parser.feed(html.replace("\r\n", "\n"))
    text = "".join(parser.out).replace("\xa0", " ").replace("``", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def format_explanation(text):
    lines = [line for line in text.split("\n") if line.strip()]
    if len(lines) == 1 or "\n\n" in text:
        return text
    if any(line.startswith("=") for line in lines):  # step by step math
        return "```text\n" + "\n".join(lines) + "\n```"
    if all(line.startswith("- ") for line in lines):
        return text
    nested = any(line.startswith("- ") for line in lines)
    return "\n".join("  " + line if nested and line.startswith("- ") else "- " + line for line in lines)


def format_examples(text):
    parts = re.split(r"\*\*\s*Example (\d+):?\s*\*\*", text)[1:]
    out = []
    for number, body in zip(parts[::2], parts[1::2]):
        lines = [line.rstrip() for line in body.replace("**", "").strip("\n").split("\n")]
        body = "\n".join(line if re.match(r"\s+[-\d]", line) else line.strip() for line in lines)
        images = re.findall(r"!\[\]\([^)]*\)", body)
        body = re.sub(r"!\[\]\([^)]*\)", "", body)
        given = re.search(r"Input:\s*(.*?)\s*Output:", body, re.S).group(1)
        result = re.search(r"Output:\s*(.*?)(?:\s*Explanation:|$)", body, re.S).group(1)
        explanation = re.search(r"Explanation:\s*(.*)$", body, re.S)
        block = f"### Example {number}:\n\n"
        block += "".join(f"{image}\n\n" for image in images)
        block += f"`Input: {' '.join(given.split())}`\n\n`Output: {' '.join(result.split())}`\n\n"
        if explanation and explanation.group(1).strip():
            text = textwrap.dedent(explanation.group(1).strip("\n")).strip()
            block += f"#### Explanation:\n\n{format_explanation(text)}\n\n"
        out.append(block)
    return "".join(out).rstrip() + "\n"


def fetch(slug):
    query = json.dumps({"query": 'query{question(titleSlug:"%s"){content codeSnippets{lang code} metaData}}' % slug})
    response = subprocess.run(
        ["curl", "-s", "-A", "Mozilla/5.0", "-H", "Content-Type: application/json",
         "-H", "Referer: https://leetcode.com/", "https://leetcode.com/graphql", "-d", query],
        capture_output=True, text=True, check=True,
    )
    return json.loads(response.stdout)["data"]["question"]


def python_skeleton(question):
    """LeetCode's Python3 snippet, with typing generics lowered so it runs on this repo's Python."""
    snippets = question.get("codeSnippets") or []
    code = next((snippet["code"] for snippet in snippets if snippet["lang"] == "Python3"), "")
    if not code.strip():
        return ""
    for name in ("List", "Dict", "Set", "Tuple", "FrozenSet"):
        code = re.sub(rf"\b{name}\b", name.lower(), code)
    return "\n".join(line.rstrip() for line in code.strip("\n").split("\n")).rstrip()


def write_skeleton(problem_id, question):
    path = ROOT / "src" / problem_id / "index.py"
    if not path.exists() or path.read_text().strip():
        return
    skeleton = python_skeleton(question)
    if skeleton:
        path.write_text(skeleton + "\n")
        print(f"{problem_id}: signature written to index.py")


def fill(problem_id):
    path = ROOT / "src" / problem_id / "readme.md"
    text = path.read_text()
    question = fetch(re.search(r"problems/([^/]+)/", text).group(1))

    level = re.search(r"\*\*Level\*\*: .*\n", text)
    if EMPTY not in text or not text[level.end():].startswith("\n## Examples"):
        print(f"{problem_id}: statement already has content, skipped")
    else:
        content = to_markdown(question["content"])
        examples = re.search(r"\*\*\s*Example 1:?\s*\*\*", content)
        constraints = re.search(r"\*\*Constraints:\*\*", content)
        statement = content[:examples.start()].strip()
        rules = content[constraints.end():].strip()
        follow_up = ""
        if match := re.search(r"\n\s*\*\*Follow[- ]up:?\*\*", rules):
            follow_up = f"\n{rules[match.start():].strip()}\n"
            rules = rules[:match.start()]
        rules = "\n".join(line for line in rules.split("\n") if line.strip())

        text = text[:level.end()] + f"\n{statement}\n" + text[level.end():]
        text = text.replace(EMPTY, f"\n\n## Examples\n\n{format_examples(content[examples.start():constraints.start()])}"
                                   f"\n## Constraints\n\n{rules}\n{follow_up}\n## My Solution", 1)
        path.write_text(text)
        print(f"{problem_id}: statement filled")

    write_skeleton(problem_id, question)


for problem_id in sys.argv[1:]:
    fill(problem_id)
