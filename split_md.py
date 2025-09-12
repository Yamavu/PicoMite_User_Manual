#!/usr/bin/env python3

import re
import sys
from pathlib import Path
# from typing import Set, List



def prep_name(name):
    repl = [r"\S+\s*\|.+", r"\W", r"<br\s*\\?>"]
    for r in repl:
        name = re.sub(r, "_", name)

    name = re.sub("_+", "_", name)
    name = name.strip("_").lower()
    return name


def split_markdown_by_headings(file_path: str, level: int = 1):
    """
    Splits a markdown file into multiple files based on H3 headings.

    Each H3 heading that starts with a capitalized word (e.g., '### WORD')
    creates a new file named 'WORD.txt'. The content of that file is all text
    under that heading until the next H3 heading.
    """
    input_path = Path(file_path)
    output_dir = input_path.parent()

    if not input_path.is_file():
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)

    content = input_path.read_text()

    heading = r"#" * level
    heading_regex = rf"\n{heading}\s+([A-Z][^\n]*)"
    parts = []
    for m in re.finditer(heading_regex, content):
        if len(parts) > 0:
            parts[-1]["end"] = m.start(0)
        parts.append({"filename": f"{prep_name(m.group(1))}.md", "start": m.start(1)})
        # p.write_text(content[m.start(1):m.end(0)], encoding="UTF-8")
    print(parts)
    if len(parts) > 0:
        parts[-1]["end"] = len(content)
        chapter = {"filename": input_path.name, "start": 0, "end": parts[0]["start"]}
    for part in parts:
        for k in ["filename", "start", "end"]:
            assert part.get(k) is not None
        part_path = Path(part["filename"])
        if part_path.exists():
            print(f"name collission: {part_path.name}")
            print(f"print : {part_path.name}")
        else:
            part_content = f"{heading} " + content[part["start"] : part["end"]]
            part_path.write_text(part_content)
    chapter_path = Path(chapter["filename"])
    if chapter_path.exists():
        print(f"name collission: {chapter_path.name}")
        print(f"print : {chapter_path.name}")
    else:
        chapter_content = (
            content[chapter["start"] : chapter["end"] - len(heading) - 1] + "\n"
        )
        for part in parts:
            chapter_content += "{{#include " + part["filename"] + "}}\n\n"
        chapter_path.write_text(chapter_content)


def main():
    """Main function to handle command-line arguments and script execution."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <markdown-file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    split_markdown_by_headings(input_file, 2)


if __name__ == "__main__":
    main()
