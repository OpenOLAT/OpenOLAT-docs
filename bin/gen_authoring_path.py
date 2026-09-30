#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schreibt die Seiten «Der Weg zum ersten Kurs» (Einführung für Autor:innen) im Benutzerhandbuch.

Eingaben
  bin/authoring_path_views.yaml   die kuratierte Ansicht: Stationen, Stationstexte DE/EN,
                                  Begriffe je Station, Türen, Verwechslungspaare
  map.json der Concept Map        nur lesend; Begriff, Beschreibung, Synonyme, Handbuchseite,
                                  Wortlaut der Verwechslungshinweise, tiefere Teile

map.json entsteht in der Concept Map (fxIntelligence) mit
  cd <fxIntelligence>/knowledge/openolat/concept-map && CM_WORK=/tmp/cm python3 scripts/02_map_to_json.py

Ausgaben
  sites/manual_user/docs/authoring_path/index.de.md, index.md
  sites/manual_user/docs/authoring_path/<station>.de.md, <station>.md
  der markierte Block mit den Stationskacheln in sites/manual_user/docs/general/index(.de).md

Der Lauf bricht ab, ohne etwas zu schreiben, wenn ein Schlüssel der Ansicht in der Map fehlt,
ein Verwechslungspaar keine Kante in der Map hat, eine Handbuch- oder How-to-Seite nicht als
Datei vorliegt oder ein Anker fehlt.

Aufruf (aus dem Repo-Wurzelverzeichnis):
  .venv/bin/python3 bin/gen_authoring_path.py [--map /tmp/cm/map.json] [--check]
  --check  prüft nur und schreibt nichts
"""
import argparse
import json
import os
import posixpath
import re
import sys
import urllib.parse

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITES = os.path.join(ROOT, "sites")
OUT = os.path.join(SITES, "manual_user", "docs", "authoring_path")
HOME = os.path.join(SITES, "manual_user", "docs", "general")
VIEWS = os.path.join(ROOT, "bin", "authoring_path_views.yaml")
LANGS = ("de", "en")
SUFFIX = {"de": ".de.md", "en": ".md"}
TILES_BEGIN = "<!-- gen:authoring_path_tiles -->"
TILES_END = "<!-- /gen:authoring_path_tiles -->"
DEEP_MAX = 4
DROP_DE = ("nicht mehr", "deprecated", "<s>")
DROP_EN = ("no longer", "deprecated", "<s>")

errors = []


def fail(msg):
    errors.append(msg)


# ---------------------------------------------------------------- helpers ---------------------
def gender(s):
    """Map notation Autor{in} / Betreuer{innen} to the manual's colon form Autor:in."""
    if not s:
        return s
    s = re.sub(r"<s>.*?</s>", "", s)
    return re.sub(r"\{([^}]*)\}", r":\1", s).strip()


def md_escape(s):
    return s.replace("*", r"\*").replace("_", r"\_") if s else s


def page_file(path, lang):
    """path relative to sites/, without language suffix."""
    return os.path.join(SITES, path + SUFFIX[lang])


def anchors_of(fn):
    with open(fn, encoding="utf-8") as f:
        return set(re.findall(r"\{:\s*#([A-Za-z0-9_\-.]+)\s*\}", f.read()))


def h1_of(fn):
    with open(fn, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                t = re.sub(r"\{:[^}]*\}", "", line[2:])
                t = re.sub(r"\[:octicons[^\]]*\]\([^)]*\)", "", t)
                t = re.sub(r":[a-z][a-z0-9_\-]*:", "", t)
                t = re.sub(r"<[^>]+>", " ", t)
                return re.sub(r"\s+", " ", t.replace('"', "")).strip()
    return None


def _virtual(fn):
    """File system path under sites/ -> path in the monorepo build (sites/<site>/docs/x -> <site>/x)."""
    rel = os.path.relpath(fn, SITES).replace(os.sep, "/")
    site, rest = rel.split("/docs/", 1)
    return f"{site}/{rest}"


def rel_link(target_fn, from_dir, anchor=None):
    """Relative Markdown link as the monorepo plugin resolves it, not as the file system nests it."""
    r = posixpath.relpath(_virtual(target_fn), posixpath.dirname(_virtual(os.path.join(from_dir, "x.md"))))
    return r + ("#" + anchor if anchor else "")


def man_target(man):
    """Map field man: 'manual_user/learningresources/Roles[#anchor]' -> (sites path, anchor)."""
    anchor = None
    if "#" in man:
        man, anchor = man.split("#", 1)
    site, rest = man.split("/", 1)
    return f"{site}/docs/{rest}", anchor


def first_sentences(desc):
    """Short description for the term card: the first sentence, two if the first is a stub."""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ])", desc.strip())
    out = parts[0]
    if len(out) < 40 and len(parts) > 1:
        out += " " + parts[1]
    return out


# ---------------------------------------------------------------- load ------------------------
def load(map_path):
    with open(VIEWS, encoding="utf-8") as f:
        V = yaml.safe_load(f)
    with open(map_path, encoding="utf-8") as f:
        M = json.load(f)
    return V, M


def validate(V, M):
    C = M["concepts"]
    edges = {frozenset((e["a"], e["b"])): e for e in M["edges"]}
    view_keys = []
    for s in V["stations"]:
        for it in s["items"]:
            view_keys.append(it["key"])
            view_keys.extend(it.get("kids") or [])
    for k in view_keys:
        if k not in C:
            fail(f"Schlüssel der Ansicht fehlt in der Map: {k}")
    for a, b in V["apart"]:
        for k in (a, b):
            if k not in C:
                fail(f"Schlüssel eines Verwechslungspaars fehlt in der Map: {k}")
        if frozenset((a, b)) not in edges:
            fail(f"Verwechslungspaar ohne keep_apart-Kante in der Map: {a} / {b}")
    # manual pages of every concept shown on a page
    shown = set(view_keys) | {k for p in V["apart"] for k in p}
    for k in sorted(shown):
        c = C.get(k)
        if not c:
            continue
        if not c.get("man"):
            if k in view_keys:
                fail(f"Begriff ohne Handbuchseite in der Map: {k}")
            continue
        path, anchor = man_target(c["man"])
        for lang in LANGS:
            fn = page_file(path, lang)
            if not os.path.isfile(fn):
                fail(f"Handbuchseite fehlt: {os.path.relpath(fn, ROOT)} ({k})")
            elif anchor and anchor not in anchors_of(fn):
                fail(f"Anker #{anchor} fehlt in {os.path.relpath(fn, ROOT)} ({k})")
    # doors
    for s in V["stations"]:
        for door in ("howto", "read"):
            d = s.get(door)
            if not d:
                continue
            for lang in LANGS:
                fn = page_file(d["path"], lang)
                if not os.path.isfile(fn):
                    fail(f"Seite der Tür {door} fehlt: {os.path.relpath(fn, ROOT)} (Station {s['id']})")
                elif d.get("anchor") and d["anchor"] not in anchors_of(fn):
                    fail(f"Anker #{d['anchor']} fehlt in {os.path.relpath(fn, ROOT)} (Station {s['id']})")
    # further pages of the footer list
    for s in V["stations"]:
        for path in s.get("further") or []:
            for lang in LANGS:
                fn = page_file(path, lang)
                if not os.path.isfile(fn):
                    fail(f"Seite der Fussliste fehlt: {os.path.relpath(fn, ROOT)} (Station {s['id']})")
    for k in V.get("deep_exclude") or []:
        if k not in C:
            fail(f"Ausgeschlossener Schlüssel fehlt in der Map: {k}")
    return edges


# ---------------------------------------------------------------- model -----------------------
class Ctx:
    def __init__(self, V, M, edges):
        self.V, self.C, self.edges = V, M["concepts"], edges
        self.children = {}
        for k, c in self.C.items():
            for p in c.get("po") or []:
                self.children.setdefault(p, []).append(k)
        self.in_view = set()
        for s in V["stations"]:
            for it in s["items"]:
                self.in_view.add(it["key"])
                self.in_view.update(it.get("kids") or [])

    def name(self, k, lang):
        c = self.C[k]
        return gender(c["de"] if lang == "de" else (c.get("en") or c["de"]))

    def desc(self, k, lang):
        c = self.C[k]
        return gender((c.get("desc") if lang == "de" else c.get("desc_en")) or "")

    def kind(self, k, lang):
        return self.V["kind"][lang].get(self.C[k].get("kind"), self.V["kind"][lang]["concept"])

    def syn(self, k, lang):
        s = self.C[k].get("syn") or {}
        return [gender(x) for x in (s.get("user_de" if lang == "de" else "user_en") or [])]

    def man_link(self, k, lang, from_dir):
        c = self.C[k]
        if not c.get("man"):
            return None
        path, anchor = man_target(c["man"])
        fn = page_file(path, lang)
        return rel_link(fn, from_dir, anchor) if os.path.isfile(fn) else None

    def apart_for(self, k):
        out = []
        for a, b in self.V["apart"]:
            if k in (a, b):
                out.append((b if k == a else a, self.edges[frozenset((a, b))]))
        return out

    def deep(self, k, lang):
        """Deeper parts of k (part_of children outside the view): names, 'more' flag, has settings."""
        drop = DROP_DE if lang == "de" else DROP_EN
        exclude = set(self.V.get("deep_exclude") or [])
        names, attrs = [], False
        for x in self.children.get(k, []):
            if x in self.in_view or x in exclude:
                continue
            if self.name(x, lang) == self.name(k, lang):
                continue
            c = self.C[x]
            if c.get("internal"):
                continue
            raw = c["de"] if lang == "de" else (c.get("en") or c["de"])
            if any(d in raw for d in drop):
                continue
            if c.get("kind") == "attribute":
                attrs = True
            else:
                names.append(x)
        return names[:DEEP_MAX], len(names) > DEEP_MAX, attrs


# ---------------------------------------------------------------- rendering -------------------
def tiles(V, lang, prefix):
    """The seven station tiles; prefix is the relative path from the page to authoring_path/."""
    lines = ['<div class="oo-mh-stations" markdown>', ""]
    for s in V["stations"]:
        lines.append(f"1. [{s[lang]} <small>{s['sub_' + lang]}</small>]({prefix}{s['id']}{SUFFIX[lang]})")
    lines += ["", "</div>"]
    return "\n".join(lines)


def front(title, desc):
    return "---\n" + yaml.safe_dump({"title": title, "description": desc}, allow_unicode=True,
                                     sort_keys=False, width=1000) + "---\n"


GEN_NOTE = ("<!-- Generiert von bin/gen_authoring_path.py aus bin/authoring_path_views.yaml. "
            "Nicht von Hand bearbeiten. -->")


def navbar(ctx, idx, lang):
    """Die Navigation des Autorenwegs: Beschriftung, zurück, weiter. Steht vor dem Titel und am
    Seitenende. idx = -1 für die Wegseite, sonst Index der Station."""
    V, U = ctx.V, ctx.V["ui"][lang]
    stations = V["stations"]
    m = U["menu"]
    def btn(cls, href, text):
        return f'[{text}]({href}){{ .oo-mh-btn .oo-mh-btn--{cls} }}'
    if idx < 0:
        pv = btn("prev", f"../general/index{SUFFIX[lang]}", f"‹ {U['home']}")
        n = stations[0]
        nx = btn("next", f"{n['id']}{SUFFIX[lang]}", f"{m}: {n[lang]} ›")
    else:
        prev = stations[idx - 1] if idx > 0 else None
        nxt = stations[idx + 1] if idx + 1 < len(stations) else None
        pv = (btn("prev", f"{prev['id']}{SUFFIX[lang]}", f"‹ {m}: {prev[lang]}") if prev
              else btn("prev", f"index{SUFFIX[lang]}", f"‹ {U['path_back']}"))
        nx = (btn("next", f"{nxt['id']}{SUFFIX[lang]}", f"{m}: {nxt[lang]} ›") if nxt
              else btn("next", f"index{SUFFIX[lang]}", f"{U['path_back']} ›"))
    return (f'<nav class="oo-mh-nav" aria-label="{U["nav_label"]}" markdown="1">\n\n'
            f'<span class="oo-mh-nav__label">{U["nav_label"]}</span>\n{pv}\n{nx}\n\n</nav>')


def render_index(ctx, lang):
    V, U = ctx.V, ctx.V["ui"][lang]
    v = V["view"]
    phases = " ".join(
        f'<span class="oo-mh-phase{" oo-mh-phase--on" if i == 0 else ""}"><b>{p[0]}</b>: {p[1]}</span>'
        for i, p in enumerate(v["phases_" + lang]))
    first = V["stations"][0]
    before = v["before_" + lang].replace(
        "{einrichten}", f"[{first[lang]}]({first['id']}{SUFFIX[lang]})")
    out = [front(v[lang], v["lead_" + lang].split(". ")[0] + "."), GEN_NOTE, "",
           navbar(ctx, -1, lang), "",
           f"# {v[lang]} {{: #authoring_path}}", "",
           v["lead_" + lang], "",
           f'<p class="oo-mh-phases">{phases}</p>', "",
           f"## {U['stations_h']} {{: #stations}}", "",
           tiles(V, lang, ""), "",
           f'<p class="oo-mh-hint">{v["hint_" + lang]}</p>', "",
           f"## {U['before_h']} {{: #before_you_start}}", "",
           before, ""]
    return "\n".join(out)


def detail_block(ctx, k, lang, indent=""):
    """A collapsible ??? note with everything the map knows about k."""
    U = ctx.V["ui"][lang]
    other = "en" if lang == "de" else "de"
    name = ctx.name(k, lang)
    i = indent + "    "
    body = []
    d = ctx.desc(k, lang)
    if d:
        body.append(md_escape(d))
    body.append(f"**{U['other_lang']}:** {md_escape(ctx.name(k, other))}")
    syn = ctx.syn(k, lang)
    if syn:
        body.append(f"**{U['syn']}:** {md_escape(', '.join(syn))}")
    for o, e in ctx.apart_for(k):
        why = e["why"] if lang == "de" else (e.get("why_en") or e["why"])
        link = ctx.man_link(o, lang, OUT)
        oname = ctx.name(o, lang)
        label = f"[{oname}]({link})" if link else oname
        body.append(f"**{U['apart_detail'].format(other=label)}** {md_escape(why)}")
    links = []
    ml = ctx.man_link(k, lang, OUT)
    if ml:
        links.append(f"[{U['manual']}]({ml})")
    q = urllib.parse.quote(U["sophia_q"].format(name=name), safe="")
    links.append(f"[{U['sophia']}](?sophia={q})")
    body.append(" · ".join(links))
    out = [f'{indent}??? note "{U["more"].format(name=name)}"', ""]
    for b in body:
        out += [i + b, ""]
    return out


def render_station(ctx, s, idx, lang):
    V, U = ctx.V, ctx.V["ui"][lang]
    stations = V["stations"]
    mine = set()
    for it in s["items"]:
        mine.add(it["key"])
        mine.update(it.get("kids") or [])
    out = [front(s[lang], s["sub_" + lang] + ". " + s["desc_" + lang].split(". ")[0] + "."), GEN_NOTE, "",
           navbar(ctx, idx, lang), "",
           f"# {s[lang]} {{: #{s['id']}}}", "",
           f'<p class="oo-mh-sub">{s["sub_" + lang]}</p>', "",
           s["desc_" + lang], "",
           f"## {U['terms_h']} {{: #terms}}", "",
           '<div class="oo-mh-terms" markdown>', ""]
    for it in s["items"]:
        k = it["key"]
        out += ['<div class="oo-mh-term" markdown>', "",
                f'<p class="oo-mh-kind">{ctx.kind(k, lang)}</p>', "",
                f"### {ctx.name(k, lang)} {{: #{k.replace('.', '_')}}}", "",
                md_escape(first_sentences(ctx.desc(k, lang))), ""]
        out += detail_block(ctx, k, lang)
        kids = it.get("kids") or []
        if kids:
            out += [f'<p class="oo-mh-partof">{U["part_of"]}</p>', ""]
            for kk in kids:
                out += detail_block(ctx, kk, lang)
        out += ["</div>", ""]
    out += ["</div>", ""]
    # keep-apart pairs inside this station
    for a, b in V["apart"]:
        if a in mine and b in mine:
            e = ctx.edges[frozenset((a, b))]
            why = e["why"] if lang == "de" else (e.get("why_en") or e["why"])
            out += [f'!!! info "{U["apart_station"].format(a=ctx.name(a, lang), b=ctx.name(b, lang))}"', "",
                    "    " + md_escape(why), ""]
    # two doors
    h, r = s.get("howto"), s["read"]
    if h:
        try_line = f"[{U['howto_prefix']} {h[lang]}]({rel_link(page_file(h['path'], lang), OUT, h.get('anchor'))})"
    else:
        try_line = U["no_howto"]
    read_line = f"[{r[lang]}]({rel_link(page_file(r['path'], lang), OUT)})"
    out += [f"## {U['doors_h']} {{: #two_doors}}", "",
            '<div class="oo-mh-doors" markdown>', "",
            '<div class="oo-mh-door" markdown>', "",
            f'<p class="oo-mh-kicker">{U["try"]}</p>', "",
            try_line, "",
            f'{U["frentix"]} [{U["frentix_mail"]}](mailto:{U["frentix_mail"]})', "",
            "</div>", "",
            '<div class="oo-mh-door" markdown>', "",
            f'<p class="oo-mh-kicker">{U["read"]}</p>', "",
            read_line, "",
            "</div>", "", "</div>", ""]
    # deepen
    out += [f"## {U['deepen_h']} {{: #deepen}}", "", U["deepen_lead"], ""]
    rows = []
    for k in [x for it in s["items"] for x in [it["key"]] + (it.get("kids") or [])]:
        names, more, attrs = ctx.deep(k, lang)
        if not names and not attrs:
            continue
        parts = []
        if names:
            labels = []
            for x in names:
                ln = ctx.man_link(x, lang, OUT)
                labels.append(f"[{md_escape(ctx.name(x, lang))}]({ln})" if ln else md_escape(ctx.name(x, lang)))
            parts.append(", ".join(labels) + (f" {U['deepen_more']}" if more else "") + ".")
        if attrs:
            ml = ctx.man_link(k, lang, OUT)
            if ml:
                path, _ = man_target(ctx.C[k]["man"])
                title = h1_of(page_file(path, lang)) or ctx.name(k, lang)
                parts.append(U["deepen_attrs"].format(link=f"[{md_escape(title)}]({ml})"))
        rows.append(f"- **{ctx.name(k, lang)}:** " + " ".join(parts))
    out += (rows if rows else [U["deepen_none"]]) + [""]
    out += footer(ctx, s, lang, "\n".join(out))
    return "\n".join(out)


FOOT_BLOCK_MIN = 8


def _link_target(link):
    """Relative link of a station page -> (sites path of the target file, link without anchor)."""
    bare = link.split("#", 1)[0]
    virt = posixpath.normpath(posixpath.join(_virtual(os.path.join(OUT, "x.md")).rsplit("/", 1)[0], bare))
    site, rest = virt.split("/", 1)
    return os.path.join(SITES, site, "docs", rest), bare


def footer(ctx, s, lang, text):
    """Fussliste «Weiterführende Informationen»: every manual page linked on the station (one entry
    per page, no anchor, page title as link text), then the curated further pages of the view."""
    U = ctx.V["ui"][lang]
    own = os.path.join(OUT, s["id"] + SUFFIX[lang])
    seen, mentioned = set(), []
    for link in re.findall(r"\]\(([^)\s]+)\)", text):
        if link.startswith(("?", "#", "mailto:", "http")) or ".md" not in link:
            continue
        fn, bare = _link_target(link)
        if os.path.abspath(fn) == os.path.abspath(own) or fn in seen:
            continue
        seen.add(fn)
        mentioned.append((fn, bare))
    further = []
    for path in s.get("further") or []:
        fn = page_file(path, lang)
        if fn in seen:
            continue
        seen.add(fn)
        further.append((fn, rel_link(fn, OUT)))

    def entries(items):
        lines = [f"[{h1_of(fn) or os.path.basename(fn)} >]({ln})" for fn, ln in items]
        return [l + "<br>" for l in lines[:-1]] + lines[-1:]

    out = [f"## {U['foot_h']} {{: #further_information}}", ""]
    if len(mentioned) + len(further) >= FOOT_BLOCK_MIN:
        if mentioned:
            out += [f"**{U['foot_mentioned']}**<br>"] + entries(mentioned) + [""]
        if further:
            out += [f"**{U['foot_further']}**<br>"] + entries(further) + [""]
    else:
        out += entries(mentioned + further) + [""]
    out += [f"[{U['top']}](#{s['id']})", ""]
    return out


def patch_home(V, lang, write):
    fn = os.path.join(HOME, "index" + SUFFIX[lang])
    with open(fn, encoding="utf-8") as f:
        src = f.read()
    if TILES_BEGIN not in src or TILES_END not in src:
        print(f"Hinweis: kein Kachelblock in {os.path.relpath(fn, ROOT)}, übersprungen")
        return
    a = src.index(TILES_BEGIN) + len(TILES_BEGIN)
    b = src.index(TILES_END)
    new = src[:a] + "\n" + tiles(V, lang, "../authoring_path/") + "\n" + src[b:]
    if write and new != src:
        with open(fn, "w", encoding="utf-8") as f:
            f.write(new)
    print(("geschrieben " if write else "geprüft ") + os.path.relpath(fn, ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", default=os.path.join(os.environ.get("CM_WORK", "/tmp/cm"), "map.json"))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not os.path.isfile(args.map):
        sys.exit(f"map.json nicht gefunden: {args.map}")
    V, M = load(args.map)
    edges = validate(V, M)
    if errors:
        print("Abbruch, nichts geschrieben:", file=sys.stderr)
        for e in errors:
            print("  " + e, file=sys.stderr)
        sys.exit(1)
    ctx = Ctx(V, M, edges)
    pages = {}
    for lang in LANGS:
        pages["index" + SUFFIX[lang]] = render_index(ctx, lang)
        for i, s in enumerate(V["stations"]):
            pages[s["id"] + SUFFIX[lang]] = render_station(ctx, s, i, lang)
    if not args.check:
        os.makedirs(OUT, exist_ok=True)
        for name, text in pages.items():
            with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
                f.write(text)
    for lang in LANGS:
        patch_home(V, lang, not args.check)
    print(f"{'geprüft' if args.check else 'geschrieben'}: {len(pages)} Seiten in "
          f"{os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
