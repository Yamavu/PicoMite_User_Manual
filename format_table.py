#!/usr/bin/env python3

from typing import Iterator, Optional
from pathlib import Path
from dataclasses import dataclass

import re
import sys

p = Path("src/command/PicoMite_User_Manual_c.txt")


def prep_name(name):
    repl = [r"\S+\s*\|.+", r"\W", r"<br\s*\\?>"]
    for r in repl:
        name = re.sub(r, "_", name)
    name = re.sub("_+", "_", name)
    name = name.strip("_").lower()
    name = name[:40]
    return name


def guess_left_column_width(page: str):
    lines = page.strip().split("\n")
    if len(lines) > 2:
        lines = lines[:-2]
    first_space_indices = []
    for line in lines:
        match = re.search(r"^.* {4,}\b", line)
        if match:
            first_space_indices.append(match.end())
    if not first_space_indices:
        return None
    from collections import Counter

    counts = Counter(first_space_indices)
    most_common_width = counts.most_common(1)[0][0]
    return most_common_width


@dataclass
class Entry:
    title: Optional[str]
    content: Optional[str]

    def add_line(self, title, content):
        self.title += " " + title.strip()
        self.content += " " + content.strip()

    def save(self, output_dir: Path, prefix: str):
        self.title = re.sub(r" {2,}", " ", self.title)
        self.content = re.sub(r"\.\n", ".\n\n ", self.content)
        self.content = re.sub(r" {2,}", " ", self.content)
        _filename = prep_name(self.title)
        output_file = output_dir / f"{prefix}{_filename}.md"
        md_content = f"## {self.title}\n\n{self.content}"
        output_file.write_text(md_content)
        print(output_file, len(self.content))


def split_entries(input_file: Path) -> Iterator[Entry]:
    content: str = input_file.read_text()
    current_entry = Entry(*[""] * 2)
    for page in content.split("\f"):
        for pattern in [
            r"\s+PicoMite[ A-Za-z]Page +\d+\s\Z",
            r"\s+Page +\d+ +PicoMite[ A-Za-z]+\s\Z",
        ]:
            page = re.sub(
                pattern=pattern,
                repl="\n\n\n",
                string=page,
                flags=re.MULTILINE,
            )
        left_col_width = guess_left_column_width(page)
        prev_title = ""
        for line in page.splitlines():
            _title_line = (
                line[:left_col_width].strip() if len(line) > left_col_width else line
            )
            if prev_title == "" and re.match(r"^[A-Z].+", _title_line):
                current_entry.title = current_entry.title.strip()
                yield current_entry
                current_entry = Entry(*[""] * 2)
            current_entry.title += f" {_title_line}"
            current_entry.content += (
                line[left_col_width:] if len(line) > left_col_width else ""
            )


def main():
    """Main function to handle command-line arguments and script execution."""
    if len(sys.argv) != 3:
        usage = f"Usage: {sys.argv[0]} <table-file> <output-root>"
        print(usage, file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_root = Path(sys.argv[2])

    if output_root.is_dir():
        assert output_root.exists(), f"output root {output_root!s} missing."
        output_dir = output_root
        prefix = ""
    elif output_root.is_file():
        output_dir = output_root.parent
        prefix = output_root.name
    for entry in split_entries(input_file):
        entry.save(output_dir, prefix)


if __name__ == "__main__":
    main()
