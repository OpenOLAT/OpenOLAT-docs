"""
MkDocs hook: removes the attribute list of the first heading ({: #anchor}) from the page
title.

Registered in mkdocs.yml (`hooks:`) and in the preview config serve-fast.sh writes.

Why
- A nav entry without its own title ("administration/Login/index.md" instead of
  "Overview: administration/Login.md") takes the page title from the first H1.
- MkDocs 1.4.3, which the build server runs, reads that H1 as raw Markdown and keeps the
  attribute list. Header bar, browser tab, search results and the nav entry then showed
  "Login: Overview {: #login}". The heading in the page itself was always correct, because
  the attr_list extension renders it.
- MkDocs 1.5 extracts the title from the rendered heading and has no such problem. After an
  upgrade this hook does nothing and can go.

What it does
- On every page whose title ends in an attribute list ({: #id}, {#id}, {: .class},
  {: key=value}), the attribute list is cut off.
- A version marker at the end of the H1 ([:octicons-tag-16:{ title="..." }](link)) is cut
  off as well; it is an icon link, not text.
- Titles from the nav or from the front matter stay as they are, unless they carry the
  same ending.
"""
import re

ATTR_LIST = re.compile(r"\s*\{:?\s*(?:[#.]|[\w-]+=)[^{}]*\}\s*$")
MARKER = re.compile(r"\s*\[:octicons-[^\]]*\]\([^)]*\)\s*$")


def clean(title):
    previous = None
    while title != previous:
        previous = title
        title = MARKER.sub("", ATTR_LIST.sub("", title))
    return title


def on_page_markdown(markdown, page, config, files):
    if isinstance(page.title, str):
        page.title = clean(page.title)
    return markdown
