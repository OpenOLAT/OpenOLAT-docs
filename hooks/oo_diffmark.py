"""
MkDocs hook for the local preview (serve-fast.sh): marks what changed on a page.

Every block of a page that differs from a git base (default origin/master) gets
a green bar on the left; a red dash marks the place where lines were removed
(the tooltip gives the number of removed lines). The comparison covers committed,
uncommitted and untracked changes, so the preview shows everything that is not
live yet. Set OO_DIFF_BASE to compare against another ref, e.g. HEAD.

A block is a paragraph, a heading, a list item, a table row or an image line.
Lines inside code fences, admonition titles, raw HTML and table separator rows
are never touched. The marker is an empty <span> at the start of the block's
first line, styled through :has() on its parent; unchanged pages are returned
as they are.

Registered only in the config serve-fast.sh generates (`hooks:`), never in
mkdocs.yml: the published manual stays free of markers. It runs as a hook and
not as a markdown extension (unlike oo_icons) because it needs the source path
of the page, which only on_page_markdown provides.
"""
import difflib
import os
import re
import subprocess

BASE = os.environ.get("OO_DIFF_BASE", "origin/master")

PREFIX_RE = re.compile(r"^(\s*(?:#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s*|\|\s*)?)")
UNIT_START_RE = re.compile(r"^\s*(?:#{1,6}\s|[-*+]\s|\d+\.\s|\|)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
SKIP_RE = re.compile(r"^\s*(?:!!!|\?\?\?|<|\{:|--8<--|\|?\s*:?-{3,})")

STYLE = """
<style>
.md-typeset :is(p, li, h1, h2, h3, h4, h5, h6, blockquote):has(> .oo-diff-add),
.md-typeset tr:has(> td > .oo-diff-add, > th > .oo-diff-add) {
	background: rgba(46, 158, 68, .10);
	box-shadow: -6px 0 0 #2e9e44;
}
.md-typeset .oo-diff-del::before {
	content: "";
	display: block;
	width: 3rem;
	border-top: 3px solid #d43f3a;
	margin: 0 0 .3rem -1rem;
}
</style>
"""

_root = None
_changed = set()


def _git(*args):
	return subprocess.run(["git", "-C", _root, *args], capture_output=True, text=True).stdout


def on_config(config):
	global _root, _changed
	_root = subprocess.run(
		["git", "-C", os.path.dirname(os.path.abspath(config.config_file_path)), "rev-parse", "--show-toplevel"],
		capture_output=True, text=True).stdout.strip()
	if not _root:
		_changed = set()
		return config
	_changed = set(_git("diff", "--name-only", BASE, "--", "*.md").split())
	_changed |= set(_git("ls-files", "--others", "--exclude-standard", "--", "*.md").split())
	return config


def _strip_meta(text):
	if text.startswith("---\n"):
		end = text.find("\n---\n", 4)
		if end != -1:
			return text[end + 5:]
	return text


def _units(lines):
	"""Group line indexes into blocks; code fences and blank lines separate them."""
	units, cur, in_fence = [], [], False
	for idx, line in enumerate(lines):
		if FENCE_RE.match(line):
			in_fence = not in_fence
			if cur:
				units.append(cur)
			cur = []
			continue
		if in_fence:
			continue
		if not line.strip() or (UNIT_START_RE.match(line) and cur):
			if cur:
				units.append(cur)
			cur = []
		if line.strip():
			cur.append(idx)
	if cur:
		units.append(cur)
	return units


def _mark(line, cls, title=""):
	pre = PREFIX_RE.match(line).group(1)
	attr = f' title="{title}"' if title else ""
	return f'{pre}<span class="{cls}"{attr}></span>{line[len(pre):]}'


def on_page_markdown(markdown, page, config, files):
	if not _changed:
		return markdown
	rel = os.path.relpath(page.file.abs_src_path, _root)
	if rel not in _changed:
		return markdown
	old = _strip_meta(_git("show", f"{BASE}:{rel}")).splitlines()
	new = markdown.splitlines()

	added, deleted = set(), {}
	for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
		if tag in ("replace", "insert"):
			added.update(range(j1, j2))
		elif tag == "delete":
			deleted[j1] = deleted.get(j1, 0) + i2 - i1

	# the marker goes on the first line of a block that may carry inline HTML
	anchors = []
	for unit in _units(new):
		anchor = next((i for i in unit if not SKIP_RE.match(new[i])), None)
		if anchor is not None:
			anchors.append((unit, anchor))
	if not anchors:
		return markdown

	add_at, del_at = set(), {}
	for unit, anchor in anchors:
		if any(i in added for i in unit):
			add_at.add(anchor)
	for pos, count in deleted.items():
		anchor = next((a for unit, a in anchors if unit[-1] >= pos), anchors[-1][1])
		del_at[anchor] = del_at.get(anchor, 0) + count

	for idx in sorted(add_at | set(del_at)):
		line = new[idx]
		if idx in del_at:
			line = _mark(line, "oo-diff-del", f"{del_at[idx]} Zeilen entfernt")
		if idx in add_at:
			line = _mark(line, "oo-diff-add")
		new[idx] = line
	return "\n".join(new) + "\n" + STYLE
