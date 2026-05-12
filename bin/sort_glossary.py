#!/usr/bin/env python3
"""Flatten glossary: drop ## section headers, promote ### entries, sort A-Z."""
import sys
from pathlib import Path


def sort_glossary(input_path: Path, output_path: Path) -> None:
    text = input_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Header = everything before first ## or ### (title + intro paragraph)
    header_end = 0
    for i, line in enumerate(lines):
        if line.startswith("## ") or line.startswith("### "):
            header_end = i
            break
    header = lines[:header_end]
    while header and header[-1].strip() == "":
        header.pop()

    # Collect all ### entries (ignore ## section headers)
    entries = []
    current = None

    def flush():
        nonlocal current
        if current is not None:
            while current and current[-1].strip() == "":
                current.pop()
            if any(line.strip() for line in current[1:]):
                entries.append(current)
            current = None

    for line in lines[header_end:]:
        if line.startswith("### "):
            flush()
            current = [line]
        elif line.startswith("## "):
            flush()
        else:
            if current is not None:
                current.append(line)

    flush()

    entries.sort(key=lambda e: e[0][4:].strip().lower())

    out = list(header)
    out.append("")
    for entry in entries:
        out.extend(entry)
        out.append("")

    output_path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    glossary_dir = repo_root / "sites" / "manual_user" / "docs" / "general"
    pairs = [
        (glossary_dir / "glossary.md", glossary_dir / "glossary_alphabetical.md"),
        (glossary_dir / "glossary.de.md", glossary_dir / "glossary_alphabetical.de.md"),
    ]
    for src, dst in pairs:
        if not src.exists():
            print(f"Missing: {src}", file=sys.stderr)
            continue
        sort_glossary(src, dst)


if __name__ == "__main__":
    main()
