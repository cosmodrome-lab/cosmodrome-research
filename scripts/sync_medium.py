#!/usr/bin/env python3

import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://medium.com/feed/@Cosmodrome-eng."
OUTPUT_FILE = Path("PUBLICATIONS.md")

ENTRY_PATTERN = re.compile(
    r"^- (\d{4}-\d{2}-\d{2}) — \[(.+)\]\((https?://.+)\)$"
)


def clean_url(url: str) -> str:
    return url.strip().split("?", 1)[0]


def read_existing() -> dict[str, tuple[str, str, str]]:
    publications = {}

    if not OUTPUT_FILE.exists():
        return publications

    for line in OUTPUT_FILE.read_text(encoding="utf-8").splitlines():
        match = ENTRY_PATTERN.match(line)

        if match:
            date, title, url = match.groups()
            url = clean_url(url)
            publications[url] = (date, title, url)

    return publications


def read_feed() -> list[tuple[str, str, str]]:
    request = urllib.request.Request(
        FEED_URL,
        headers={"User-Agent": "COSMODROME-Publication-Sync/1.0"},
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())

    publications = []

    for item in root.findall("./channel/item"):
        title = item.findtext("title", "").strip()
        url = clean_url(item.findtext("link", ""))
        published = item.findtext("pubDate", "").strip()

        if not title or not url or not published:
            continue

        date = parsedate_to_datetime(published).astimezone(
            timezone.utc
        ).date().isoformat()

        publications.append((date, title, url))

    return publications


def write_index(
    publications: dict[str, tuple[str, str, str]]
) -> None:
    ordered = sorted(
        publications.values(),
        key=lambda item: (item[0], item[2]),
        reverse=True,
    )

    years: dict[str, list[tuple[str, str, str]]] = {}

    for publication in ordered:
        years.setdefault(publication[0][:4], []).append(publication)

    lines = [
        "# Publications",
        "",
        "Complete index of COSMODROME public research.",
        "",
    ]

    for year in sorted(years, reverse=True):
        lines.extend([f"## {year}", ""])

        for date, title, url in years[year]:
            lines.append(f"- {date} — [{title}]({url})")

        lines.append("")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    publications = read_existing()

    for date, title, url in read_feed():
        publications.setdefault(url, (date, title, url))

    write_index(publications)


if __name__ == "__main__":
    main()
