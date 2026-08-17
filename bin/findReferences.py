#!/usr/bin/env python3
"""
Find references to a manual resource, or scan the whole repository.

Usage:
    findReferences.py <resource>
        Lists all markdown files that link to the given resource (a .md page
        or an asset such as an image), plus the mkdocs.yml nav entries.
        Run this BEFORE you delete or move a resource.

    findReferences.py --all
        Scans every markdown file in all sites and reports:
        - broken references: links and images whose target file does not exist
        - orphan pages: pages that are neither in a nav nor linked by any page
        - orphan assets: files that no page and no config references

The OpenOLAT-docs repository is found via --repo, via the working directory,
or as OpenOLAT-docs next to the workspace root.

Examples:
    findReferences.py sites/manual_user/docs/personal_menu/Personal_Tools.de.md
    findReferences.py sites/manual_user/docs/personal_menu/assets/artefact.png
    findReferences.py --all

Exit codes: 0 = no findings, 1 = findings (references / broken / orphans),
2 = usage error.
"""

import argparse
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = None  # set by init_repo()
ROOTS = []
SITE_PREFIXES = set()


def locate_repo(cli_value):
    """Find the OpenOLAT-docs repository: --repo, else cwd, else workspace sibling."""
    if cli_value:
        repo = Path(cli_value).expanduser().resolve()
        if not (repo / "mkdocs.yml").is_file():
            return None
        return repo
    for candidate in [Path.cwd(), *Path.cwd().parents]:
        if (candidate / "mkdocs.yml").is_file() and (candidate / "sites").is_dir():
            return candidate
    guess = Path(__file__).resolve().parents[3] / "OpenOLAT-docs"
    if (guess / "mkdocs.yml").is_file():
        return guess
    return None

# ]( target ) or ]( target "title" ) - target may contain spaces
MD_LINK_RE = re.compile(r"\]\(\s*([^)]*?)\s*\)")
HTML_REF_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
LANG_SUFFIX_RE = re.compile(r"\.[a-z]{2}(\.md)$")
YAML_MD_TOKEN_RE = re.compile(r"""([^\s"':]+\.md)\b""")

# vendored third-party directories inside docs trees, not manual content
VENDOR_DIRS = {"lighbox"}


def doc_roots():
    """Yield (prefix, real_docs_dir) for the root site and every sub-site."""
    roots = []
    if (REPO / "docs").is_dir():
        roots.append(("", REPO / "docs"))
    sites_dir = REPO / "sites"
    if sites_dir.is_dir():
        for site in sorted(sites_dir.iterdir()):
            if (site / "docs").is_dir():
                roots.append((site.name, site / "docs"))
    return roots


def init_repo(cli_value):
    global REPO, ROOTS, SITE_PREFIXES
    REPO = locate_repo(cli_value)
    if REPO is None:
        return False
    ROOTS = doc_roots()
    SITE_PREFIXES = {prefix for prefix, _ in ROOTS if prefix}
    return True


def to_virtual(real_path):
    """Map a real file path to its virtual path (site prefix + docs-relative)."""
    real_path = real_path.resolve()
    for prefix, docs_dir in ROOTS:
        try:
            rel = real_path.relative_to(docs_dir)
        except ValueError:
            continue
        rel = rel.as_posix()
        return f"{prefix}/{rel}" if prefix else rel
    return None


def to_real(vpath):
    """Map a virtual path back to a real file path."""
    parts = vpath.split("/", 1)
    if parts[0] in SITE_PREFIXES and len(parts) > 1:
        return REPO / "sites" / parts[0] / "docs" / parts[1]
    return REPO / "docs" / vpath


def canon(vpath):
    """Canonical page identity: strip the language suffix (Foo.de.md -> Foo.md)."""
    return LANG_SUFFIX_RE.sub(r"\1", vpath)


def lang_variants(vpath, prefer_de=False):
    """The path itself plus its language siblings (base and .de variant)."""
    base = canon(vpath)
    de = base[: -len(".md")] + ".de.md"
    if prefer_de:
        return [de, base]
    if base != vpath:
        return [vpath, base]
    return [base, de]


def collect_files():
    """Return (md_files, asset_files) as {virtual_path: real_path} dicts."""
    md_files, assets = {}, {}
    for prefix, docs_dir in ROOTS:
        for real in docs_dir.rglob("*"):
            if not real.is_file() or real.name.startswith("."):
                continue
            rel = real.relative_to(docs_dir).as_posix()
            if VENDOR_DIRS.intersection(rel.split("/")[:-1]):
                continue
            vpath = f"{prefix}/{rel}" if prefix else rel
            (md_files if real.suffix == ".md" else assets)[vpath] = real
    return md_files, assets


def page_url_dir(source_vpath):
    """Virtual directory of the built page URL (directory URLs: Foo.md -> Foo/)."""
    src_dir = posixpath.dirname(source_vpath)
    name = posixpath.basename(source_vpath)
    stem = canon(name)[: -len(".md")]
    if stem == "index":
        return src_dir
    return posixpath.join(src_dir, stem)


def strip_html_comments(text):
    """Blank out <!-- ... --> spans while keeping the line structure intact."""
    lines = []
    in_comment = False
    for line in text.splitlines():
        kept = []
        pos = 0
        while pos < len(line):
            if in_comment:
                end = line.find("-->", pos)
                if end == -1:
                    pos = len(line)
                else:
                    in_comment = False
                    pos = end + 3
            else:
                start = line.find("<!--", pos)
                if start == -1:
                    kept.append(line[pos:])
                    pos = len(line)
                else:
                    kept.append(line[pos:start])
                    in_comment = True
                    pos = start + 4
        lines.append("".join(kept))
    return lines


def extract_refs(text):
    """Yield (line_number, raw_target, is_html, line_text) for every reference."""
    for line_num, line in enumerate(strip_html_comments(text), 1):
        if "--8<--" in line:
            continue
        for m in MD_LINK_RE.finditer(line):
            yield line_num, m.group(1), False, line.strip()
        for m in HTML_REF_RE.finditer(line):
            yield line_num, m.group(1), True, line.strip()


def normalize_target(raw):
    """Strip title/anchor/quoting; return None for external or anchor-only targets."""
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # drop an optional "title" part: ](path "title")
    match = re.match(r"""^(\S+)\s+["'].*["']$""", target)
    if match:
        target = match.group(1)
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    if SCHEME_RE.match(target) or target.startswith("//"):
        return None
    return unquote(target)


def candidate_vpaths(source_vpath, target, is_html):
    """All virtual paths the target may resolve to, most likely first."""
    src_dir = posixpath.dirname(source_vpath)
    url_dir = page_url_dir(source_vpath)

    prefer_de = source_vpath.endswith(".de.md")
    if target.startswith("/"):
        # built-site URL: /de/... is the German language tree, not a source path
        stripped = target.lstrip("/")
        if stripped == "de" or stripped.startswith("de/"):
            stripped = stripped[2:].lstrip("/")
            prefer_de = True
        resolved_bases = [stripped or "index"]
    else:
        bases = [url_dir, src_dir] if is_html else [src_dir, url_dir]
        resolved_bases = []
        for base in bases:
            resolved = posixpath.normpath(posixpath.join(base, target))
            if resolved in (".", "/") or resolved.startswith(".."):
                continue
            if resolved not in resolved_bases:
                resolved_bases.append(resolved)

    candidates = {}  # vpath -> is_language_variant
    for resolved in resolved_bases:
        resolved = resolved.rstrip("/")
        if not resolved:
            continue
        last = posixpath.basename(resolved)
        url_style = not resolved.endswith(".md") and ("." not in last or target.endswith("/"))
        if url_style:
            # URL-style link: ../Foo/ -> Foo.md or Foo/index.md
            files = [resolved + ".md", resolved + "/index.md"]
        else:
            files = [resolved]
        for f in files:
            if f.endswith(".md"):
                variants = lang_variants(f, prefer_de and url_style)
            else:
                variants = [f]
            for i, variant in enumerate(variants):
                if variant not in candidates or candidates[variant]:
                    candidates[variant] = i > 0
    return candidates


def scan_references(md_files):
    """Parse every page. Return a list of reference records."""
    records = []
    for vpath, real in md_files.items():
        try:
            text = real.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_num, raw, is_html, line_text in extract_refs(text):
            target = normalize_target(raw)
            if target is None:
                continue
            candidates = candidate_vpaths(vpath, target, is_html)
            records.append(
                {
                    "source": vpath,
                    "line": line_num,
                    "raw": raw,
                    "line_text": line_text,
                    "candidates": list(candidates),
                    "primary": [v for v, is_var in candidates.items() if not is_var],
                }
            )
    return records


def yaml_files():
    files = [REPO / "mkdocs.yml"]
    files += sorted(REPO.glob("sites/*/mkdocs.yml"))
    return [f for f in files if f.is_file()]


def yaml_site_prefix(yml):
    if yml.parent.name in SITE_PREFIXES:
        return yml.parent.name
    return ""


def find_yaml_entries(target_vpath):
    """Find mkdocs.yml lines that mention the target page (any language variant)."""
    hits = []
    wanted = set()
    for variant in lang_variants(target_vpath):
        wanted.add(variant)
    for yml in yaml_files():
        prefix = yaml_site_prefix(yml)
        rel_wanted = set()
        for w in wanted:
            rel_wanted.add(w)
            if prefix and w.startswith(prefix + "/"):
                rel_wanted.add(w[len(prefix) + 1 :])
        try:
            lines = yml.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line_num, line in enumerate(lines, 1):
            for token in YAML_MD_TOKEN_RE.findall(line):
                if token.strip('"').strip("'") in rel_wanted:
                    hits.append((yml.relative_to(REPO).as_posix(), line_num, line.strip()))
                    break
    return hits


def nav_page_set():
    """All canonical page ids that any mkdocs.yml mentions."""
    pages = set()
    for yml in yaml_files():
        prefix = yaml_site_prefix(yml)
        try:
            text = yml.read_text(encoding="utf-8")
        except OSError:
            continue
        for token in YAML_MD_TOKEN_RE.findall(text):
            token = token.strip('"').strip("'").lstrip("./")
            pages.add(canon(token))
            if prefix:
                pages.add(canon(f"{prefix}/{token}"))
    return pages


def config_blob():
    """Concatenated text of configs, theme overrides and hooks (asset whitelist)."""
    chunks = []
    for pattern in ("mkdocs*.yml", "sites/*/mkdocs.yml", "overrides/**/*", "hooks/**/*"):
        for f in REPO.glob(pattern):
            if f.is_file():
                try:
                    chunks.append(f.read_text(encoding="utf-8", errors="ignore"))
                except OSError:
                    pass
    return "\n".join(chunks)


def rel_display(vpath):
    """Virtual path -> repo-relative real path for display."""
    return to_real(vpath).relative_to(REPO).as_posix()


def run_reference_mode(resource):
    real = Path(resource)
    if not real.is_absolute():
        real = (Path.cwd() / resource) if (Path.cwd() / resource).exists() else REPO / resource
    target_v = to_virtual(real) if real.exists() else None
    if target_v is None:
        # allow querying an already deleted file by repo-relative path
        maybe = REPO / resource
        for prefix, docs_dir in ROOTS:
            try:
                rel = maybe.resolve().relative_to(docs_dir).as_posix()
                target_v = f"{prefix}/{rel}" if prefix else rel
                break
            except ValueError:
                continue
    if target_v is None:
        print(f"Error: {resource} is not inside a docs directory of this repository.")
        return 2
    if not real.exists():
        print(f"Note: {resource} does not exist (already deleted?). Searching anyway.\n")

    md_files, _ = collect_files()
    records = scan_references(md_files)

    exact, via_base = [], []
    for rec in records:
        if rec["source"] == target_v:
            continue  # links inside the page itself
        if target_v in rec["primary"]:
            exact.append(rec)
        elif target_v in rec["candidates"]:
            via_base.append(rec)

    print(f"References to: {rel_display(target_v)}\n")
    if exact:
        print(f"Markdown references ({len(exact)}):")
        for rec in exact:
            print(f"  {rel_display(rec['source'])}:{rec['line']}")
            print(f"      {rec['line_text'][:160]}")
    if via_base:
        print(f"\nReferences via language variant ({len(via_base)}):")
        for rec in via_base:
            print(f"  {rel_display(rec['source'])}:{rec['line']}")
            print(f"      {rec['line_text'][:160]}")

    yaml_hits = find_yaml_entries(target_v) if target_v.endswith(".md") else []
    if yaml_hits:
        print(f"\nmkdocs.yml entries ({len(yaml_hits)}):")
        for path, line_num, line in yaml_hits:
            print(f"  {path}:{line_num}")
            print(f"      {line[:160]}")

    total = len(exact) + len(via_base) + len(yaml_hits)
    if total == 0:
        print("No references found. The resource is safe to delete.")
        return 0
    print(f"\nTotal: {total} reference(s). Update them before you delete the resource.")
    return 1


def run_all_mode():
    md_files, assets = collect_files()
    all_vpaths = set(md_files) | set(assets)
    records = scan_references(md_files)

    # 1. broken references
    broken = []
    linked_pages = set()
    referenced_assets = set()
    for rec in records:
        existing = [c for c in rec["candidates"] if c in all_vpaths]
        if existing:
            for hit in existing:
                if hit.endswith(".md"):
                    linked_pages.add(canon(hit))
                else:
                    referenced_assets.add(hit)
        else:
            broken.append(rec)

    print(f"Scanned {len(md_files)} pages and {len(assets)} assets "
          f"in {len(ROOTS)} docs trees.\n")

    if broken:
        print(f"Broken references ({len(broken)}):")
        for rec in broken:
            print(f"  {rel_display(rec['source'])}:{rec['line']}  ->  {rec['raw']}")
    else:
        print("Broken references: none")

    # 2. orphan pages: in no nav and linked from no page
    nav_pages = nav_page_set()
    orphans = sorted(
        v for v in md_files
        if canon(v) not in nav_pages and canon(v) not in linked_pages and canon(v) == v
    )
    if orphans:
        print(f"\nOrphan pages ({len(orphans)}) - in no nav, linked from no page:")
        for v in orphans:
            print(f"  {rel_display(v)}")
    else:
        print("\nOrphan pages: none")

    # 3. orphan assets: referenced by no page and by no config/theme file
    blob = config_blob()
    orphan_assets = sorted(
        v for v in assets
        if v not in referenced_assets and posixpath.basename(v) not in blob
    )
    if orphan_assets:
        print(f"\nOrphan assets ({len(orphan_assets)}) - referenced nowhere:")
        for v in orphan_assets:
            print(f"  {rel_display(v)}")
    else:
        print("\nOrphan assets: none")

    findings = len(broken) + len(orphans) + len(orphan_assets)
    print(f"\nTotal findings: {findings}")
    return 1 if findings else 0


def main():
    parser = argparse.ArgumentParser(
        description="Find references to a manual resource, or scan the whole repository.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples:")[1],
    )
    parser.add_argument("resource", nargs="?", help="a .md page or an asset (image etc.)")
    parser.add_argument("--all", action="store_true",
                        help="scan all sites for broken references and orphans")
    parser.add_argument("--repo", help="path to the OpenOLAT-docs repository "
                        "(default: found via the working directory)")
    args = parser.parse_args()

    if args.all == bool(args.resource):
        parser.print_usage()
        print("Error: pass either a resource path or --all.")
        return 2
    if not init_repo(args.repo):
        print("Error: OpenOLAT-docs repository not found. Pass --repo /path/to/OpenOLAT-docs.")
        return 2
    if args.all:
        return run_all_mode()
    return run_reference_mode(args.resource)


if __name__ == "__main__":
    sys.exit(main())
