"""
MkDocs hook: fills the section "Neu in X.Y" / "New in X.Y" on the start pages of the
user manual and the admin manual from the newest release notes.

Registered in mkdocs.yml (`hooks:`) and in the preview config serve-fast.sh writes. The
build server runs MkDocs 1.4.3, which supports hooks (checked 30.10.2026).

What it does
- The start page carries the markers <!-- gen:news --> and <!-- /gen:news -->. Everything
  between them is replaced on every build; a page without markers stays as it is.
- The newest release notes are the file sites/release_notes/docs/Release_notes_X.Y(.de).md
  with the highest version. The previous version is linked in the closing sentence.
- User manual: the first five stages (Bühnen) of the release notes. A stage is an H3 in a
  content section (not "Weitere Verbesserungen") or a content H2 without H3 and without
  list items. Card title is the heading, card text the comment <!-- karte: ... --> under the
  heading, card link the first link of the stage that points into a manual. Without the
  comment the card shows the title only; without a manual link the title links to the
  release notes.
- Admin manual: the first five items of the checklist "Systemadministratoren: ...". Card
  title is the link text of the item (or the text before ":"), card text the menu path in
  backticks, card link the manual link of the item.

Rules for the release notes writers: conventions.md of the release notes project, rule 13.

Try it without a build:
  python3 oo_news.py --page <repo>/sites/manual_user/docs/general/index.de.md
prints the generated block for that page (from the repo the page lives in).
"""
import argparse
import logging
import os
import re

try:
    from markdown.extensions.toc import slugify
except ImportError:  # standalone run without the markdown package
    import unicodedata

    def slugify(value, separator):
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
        value = re.sub(r"[^\w\s-]", "", value).strip().lower()
        return re.sub(r"[{}\s]+".format(separator), separator, value)

log = logging.getLogger("mkdocs.hooks.oo_news")

BEGIN, END = "<!-- gen:news -->", "<!-- /gen:news -->"
CARDS = 5
ANCHOR = "new_in_21"  # kept stable: the anchor existed before, links may point to it
TARGETS = {  # start page (path below sites/) -> manual whose cards it shows
    "manual_user/docs/general/index.de.md": "user",
    "manual_user/docs/general/index.md": "user",
    "manual_admin/docs/index.de.md": "admin",
    "manual_admin/docs/index.md": "admin",
}
STANDARD_H2 = ("Weiteres, kurz notiert", "Administratives / Technisches", "Systemadministratoren",
               "Weitere Informationen", "Further notes", "Miscellaneous", "Administrative / Technical",
               "System administrators", "Further information")
TEXT = {
    "de": {"head": "Neu in", "rn": "Release Notes", "prev": "Die Neuerungen von Release {v} stehen in den [Release Notes {v}]({link}).",
           "admin_intro": "Diese Funktionen müssen nach dem Update in der System-Administration aktiviert oder konfiguriert werden.",
           "admin_all": "Die ganze Checkliste nach dem Update steht in den Release Notes: [Checkliste nach Update auf {v}]({link})"},
    "en": {"head": "New in", "rn": "Release notes", "prev": "The new features of release {v} are in the [release notes {v}]({link}).",
           "admin_intro": "These functions have to be activated or configured in the system administration after the update.",
           "admin_all": "The full checklist after the update is in the release notes: [Checklist after updating to {v}]({link})"},
}
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
MANUAL_RE = re.compile(r"https?://docs\.openolat\.org/(de|en)/(manual_user|manual_admin|manual_how-to)/([^#)]*?)/?(#[\w-]+)?$")
KARTE_RE = re.compile(r"<!--\s*karte:\s*(.*?)\s*-->", re.S | re.I)
ID_RE = re.compile(r"\{:\s*#([\w-]+)\s*\}")


def heading_text(line):
    return ID_RE.sub("", re.sub(r"^#+\s*", "", line)).strip()


def heading_anchor(line):
    m = ID_RE.search(line)
    return m.group(1) if m else slugify(heading_text(line), "-")


def find_sites(path):
    d = os.path.dirname(os.path.abspath(path))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "sites", "release_notes", "docs")):
            return os.path.join(d, "sites")
        d = os.path.dirname(d)
    return None


def release_notes(sites, lang):
    """Returns [(version tuple, version string, file name)] of the language, newest first."""
    rn_dir = os.path.join(sites, "release_notes", "docs")
    suffix = ".de.md" if lang == "de" else ".md"
    out = []
    for f in os.listdir(rn_dir):
        m = re.fullmatch(r"Release_notes_(\d+)\.(\d+)" + re.escape(suffix), f)
        if m:
            out.append(((int(m.group(1)), int(m.group(2))), f"{m.group(1)}.{m.group(2)}", f))
    return sorted(out, reverse=True)


def virtual(rel):
    """Path as the monorepo plugin sees it: sites/<site>/docs/x.md becomes <site>/x.md."""
    return rel.replace("/docs/", "/", 1)


def rel_link(target_virtual, page_rel):
    return os.path.relpath(target_virtual, os.path.dirname(virtual(page_rel)))


def manual_link(url, lang, page_rel):
    """Turns a docs.openolat.org manual URL into a relative .md link from the start page."""
    m = MANUAL_RE.match(url)
    if not m or m.group(1) != lang:
        return None
    manual, path, anchor = m.group(2), m.group(3), m.group(4) or ""
    target = f"{manual}/{path or 'index'}" + (".de.md" if lang == "de" else ".md")
    return rel_link(target, page_rel) + anchor


def stages(lines):
    """Yields (heading line, body lines) for every stage of the release notes."""
    h2, h2_body, h2_has_sub, cur = None, [], False, None
    for ln in lines + ["## END"]:
        if ln.startswith("## "):
            if cur:
                yield cur
                cur = None
            if h2 and not h2_has_sub and not any(re.match(r"\s*[*-] (?!\* \*)", b) for b in h2_body):
                yield (h2, h2_body)
            h2, h2_body, h2_has_sub = ln, [], False
            if heading_text(ln).startswith(STANDARD_H2):
                h2 = None
            continue
        if ln.startswith("### "):
            h2_has_sub = True
            if cur:
                yield cur
            cur = (ln, []) if h2 and not heading_text(ln).startswith(("Weitere Verbesserungen", "Further improvements")) else None
            continue
        if cur:
            cur[1].append(ln)
        elif h2 and not h2_has_sub:
            h2_body.append(ln)


def card(title, href, text, rn_label, rn_href):
    out = ['<div class="oo-mh-new" markdown>', "", f"[{title}]({href}){{ .oo-mh-new__title }}", ""]
    if text:
        out += [text, ""]
    if rn_href:
        out += [f"[{rn_label}]({rn_href}){{ .oo-mh-new__rn }}", ""]
    return out + ["</div>", ""]


def build(page_rel, sites, lang, kind):
    rns = release_notes(sites, lang)
    if not rns:
        return None
    _, version, rn_file = rns[0]
    rn_rel = rel_link(f"release_notes/{rn_file}", page_rel)
    lines = open(os.path.join(sites, "release_notes", "docs", rn_file), encoding="utf-8").read().split("\n")
    t = TEXT[lang]
    out = [f"## {t['head']} {version} {{: #{ANCHOR}}}", ""]
    cards = []
    if kind == "user":
        for head, body in stages(lines):
            text = " ".join(body)
            karte = KARTE_RE.search(text)
            href = None
            for _, url in LINK_RE.findall(KARTE_RE.sub("", text)):
                href = manual_link(url, lang, page_rel)
                if href:
                    break
            rn_href = f"{rn_rel}#{heading_anchor(head)}"
            cards.append(card(heading_text(head), href or rn_href, karte.group(1) if karte else "",
                              f"{t['rn']}: {heading_text(head)}", rn_href if href else None))
            if len(cards) == CARDS:
                break
    else:
        out += [t["admin_intro"], ""]
        sec = next((i for i, ln in enumerate(lines) if ln.startswith("## Systemadministratoren")
                    or ln.startswith("## System administrators")), None)
        if sec is None:
            return None
        rn_href = f"{rn_rel}#{heading_anchor(lines[sec])}"
        for ln in lines[sec + 1:]:
            if ln.startswith("## "):
                break
            m = re.match(r"\s*[*-] \[[ x]\]\s*(.*)", ln)
            if not m:
                continue
            item = m.group(1)
            path = re.findall(r"`([^`]+)`", item)
            link = LINK_RE.search(item)
            title = link.group(1) if link else item.split(":")[0].strip()
            href = manual_link(link.group(2), lang, page_rel) if link else None
            body = f"`Administration > {path[0]}`" if path and not path[0].startswith("Administration") else (f"`{path[0]}`" if path else "")
            cards.append(card(title, href or rn_href, body, f"{t['rn']}: {version}", rn_href if href else None))
            if len(cards) == CARDS:
                break
    out += ['<div class="oo-mh-news" markdown>', ""]
    for c in cards:
        out += c
    out += ["</div>", ""]
    if kind == "user" and len(rns) > 1:
        _, prev, prev_file = rns[1]
        out.append(t["prev"].format(v=prev, link=rel_link(f"release_notes/{prev_file}", page_rel)))
    elif kind == "admin":
        out.append(t["admin_all"].format(v=version, link=rn_href))
    return "\n".join(out)


def replace_block(markdown, block):
    start, end = markdown.find(BEGIN), markdown.find(END)
    if start < 0 or end < start:
        return markdown
    return markdown[:start + len(BEGIN)] + "\n" + block + "\n" + markdown[end:]


def page_info(abs_path):
    sites = find_sites(abs_path)
    if not sites:
        return None
    rel = os.path.relpath(os.path.abspath(abs_path), sites).replace(os.sep, "/")
    kind = TARGETS.get(rel)
    if not kind:
        return None
    return sites, rel, ("de" if rel.endswith(".de.md") else "en"), kind


def on_page_markdown(markdown, page, config, files):
    if BEGIN not in markdown:
        return markdown
    info = page_info(page.file.abs_src_path)
    if not info:
        return markdown
    sites, rel, lang, kind = info
    try:
        block = build(rel, sites, lang, kind)
    except Exception as e:  # never break the build over the news section
        log.warning("oo_news: %s not filled: %s", rel, e)
        return markdown
    return replace_block(markdown, block) if block else markdown


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--page", required=True, help="start page in an OpenOLAT-docs checkout")
    a = ap.parse_args()
    info = page_info(a.page)
    if not info:
        raise SystemExit("not a start page with a news section: " + a.page)
    sites, rel, lang, kind = info
    print(build(rel, sites, lang, kind))


if __name__ == "__main__":
    main()
