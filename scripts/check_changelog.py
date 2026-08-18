#!/usr/bin/env python3
"""Validate changelog structure without third-party dependencies."""
from __future__ import annotations

import re
import sys
from pathlib import Path

VERSION_RE = re.compile(r"^## (\d+)\.(\d+)\.(\d+) — (\d{4}-\d{2}-\d{2})$")


def check(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "# Changelog":
        raise ValueError("first line must be '# Changelog'")
    headings = [line for line in lines if line.startswith("## ")]
    if not headings:
        raise ValueError("at least one version heading is required")
    versions = []
    for heading in headings:
        match = VERSION_RE.match(heading)
        if not match:
            raise ValueError(f"invalid version heading: {heading}")
        versions.append(tuple(int(part) for part in match.groups()[:3]))
    if versions != sorted(versions, reverse=True):
        raise ValueError("version headings must be in descending semantic-version order")
    for index, heading in enumerate(headings):
        start = lines.index(heading) + 1
        end = lines.index(headings[index + 1]) if index + 1 < len(headings) else len(lines)
        entries = [line.strip() for line in lines[start:end] if line.strip() and not line.startswith("#")]
        if not entries:
            raise ValueError(f"version has no entries: {heading}")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("CHANGELOG.md")
    check(target)
    print(f"changelog valid: {target}")
