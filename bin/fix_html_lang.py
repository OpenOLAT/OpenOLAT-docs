#!/usr/bin/env python3
"""Fix the <html lang> attribute of localized pages after a mkdocs build.

mkdocs-static-i18n 0.x only sets the Material theme language per locale when
its mkdocs-material auto-detection works. When it fails (silently, with a
build warning "Language de is not supported by mkdocs-material==..."), all
pages under site/de/ are generated with <html lang="en">.

This script walks the generated language folder(s) and rewrites the lang
attribute of the <html> tag to the folder's locale. It is idempotent and
intended to run in the Jenkins pipeline right after "mkdocs build":

    python3 bin/fix_html_lang.py [site_dir] [locale ...]

Defaults: site_dir = "site", locales = "de".
Exits 1 if a language folder is missing or a file cannot be processed.
"""

import re
import sys
from pathlib import Path

HTML_TAG_RE = re.compile(r'(<html\b[^>]*\blang=")([a-zA-Z-]+)(")')


def fix_file(path: Path, locale: str) -> bool:
    """Rewrite the lang attribute in one file. Returns True if changed."""
    html = path.read_text(encoding="utf-8")
    new_html, count = HTML_TAG_RE.subn(
        lambda m: m.group(1) + locale + m.group(3), html, count=1
    )
    if count == 0 or new_html == html:
        return False
    path.write_text(new_html, encoding="utf-8")
    return True


def main() -> int:
    site_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("site")
    locales = sys.argv[2:] or ["de"]

    if not site_dir.is_dir():
        print(f"ERROR: site dir not found: {site_dir}", file=sys.stderr)
        return 1

    failed = 0
    for locale in locales:
        lang_dir = site_dir / locale
        if not lang_dir.is_dir():
            print(f"ERROR: language folder not found: {lang_dir}", file=sys.stderr)
            failed += 1
            continue
        scanned = changed = 0
        for html_file in lang_dir.rglob("*.html"):
            scanned += 1
            try:
                if fix_file(html_file, locale):
                    changed += 1
            except Exception as e:  # noqa: BLE001 - report and keep going
                print(f"ERROR: {html_file}: {e}", file=sys.stderr)
                failed += 1
        print(f"{lang_dir}: {scanned} pages scanned, {changed} lang attributes fixed")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
