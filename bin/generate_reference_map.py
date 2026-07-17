#!/usr/bin/env python3
"""
Regenerate sites/manual_dev/docs/icons/reference_map.md from the OpenOlat source
of truth (src/main/webapp/static/themes/light/modules/_icons.scss), instead of
the hand-maintained, one-off table it used to be.

For every OpenOlat icon CSS class it records which FontAwesome icon (name +
variant: fa-solid / fa-regular / fa-brands) it uses, or "OpenOlat font" for the
custom OpenOlat icon-font glyphs that have no FontAwesome equivalent. Usage
counts ("Occurrences") are derived by grepping the OpenOlat src/main tree.

The class list is cross-checked against the vendored docs/stylesheets/oo-docs.css
(the actual bundle shipped to the manual) so the table only documents classes
that really exist in what readers' browsers load, and so any drift between
_icons.scss and the vendored bundle is surfaced instead of silently ignored.

Usage:
	python bin/generate_reference_map.py                  # expects OpenOlat at ../OpenOLAT
	OO_ROOT=/path/to/OpenOLAT python bin/generate_reference_map.py

Re-run this together with scripts/sync-docs-css.sh whenever OpenOlat icons change
(typically once per OpenOlat release), and commit the updated reference_map.md.
"""
import os
import re
import sys
from collections import defaultdict

DOCS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OO_ROOT = os.environ.get('OO_ROOT', os.path.join(DOCS_ROOT, '..', 'OpenOLAT'))
ICONS_SCSS = os.path.join(OO_ROOT, 'src/main/webapp/static/themes/light/modules/_icons.scss')
SRC_MAIN = os.path.join(OO_ROOT, 'src/main')
OO_DOCS_CSS = os.path.join(DOCS_ROOT, 'docs/stylesheets/oo-docs.css')
OUTPUT = os.path.join(DOCS_ROOT, 'sites/manual_dev/docs/icons/reference_map.md')

OPENOLAT_FONT_VARIANT = 'OpenOlat font'

# o_dialog_icon composites a second glyph (a comment-bubble badge) via ::after,
# positioned a few px above and right of the base 'file' glyph -- correct and
# faithful to OpenOlat's own rendering (verified: not a CSS bug), but in a bare
# table cell with nothing else for scale/context the small gap between the two
# shapes reads as "two unrelated icons" rather than one badge. padding-right
# gives it a touch more breathing room so it doesn't look cramped against the
# next column; this is a docs-only spacing tweak (attr_list on this one
# rendering), not a change to the shared icon definition.
ICON_STYLE_OVERRIDES = {
	'o_dialog_icon': 'padding-right:4px;',
}

CLASS_TOKEN_RE = re.compile(r'\.(o_[A-Za-z0-9_-]+)')
PSEUDO_SUFFIX_RE = re.compile(r'(:before|:after)$')
COMBINATOR_RE = re.compile(r'[ >~+\[\]]')
ADD_ICON_RE = re.compile(
	r"@include\s+o-add-icon\(\s*['\"]([a-z0-9-]+)['\"]\s*(?:,\s*(true|false))?"
)
ADD_BRAND_ICON_RE = re.compile(r"@include\s+o-add-brand-icon\(\s*['\"]([a-z0-9-]+)['\"]")
FONTELLO_CONTENT_RE = re.compile(r"content\s*:\s*['\"]\\([Ee][0-9a-fA-F]+)['\"]")
FONTELLO_FONT_RE = re.compile(r"font-family\s*:\s*openolat")


def strip_comments(text):
	text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
	text = re.sub(r'//[^\n]*', '', text)
	return text


def split_rules(text):
	"""Yield (selector_header, body) for each top-level '<selector> { ... }' rule.
	body includes any nested braces (e.g. '& { ... }') unparsed."""
	i = 0
	n = len(text)
	while i < n:
		brace = text.find('{', i)
		if brace == -1:
			break
		# A handful of upstream rules end with a stray ';' after the closing
		# '}' (e.g. "... transform: rotate(180deg) };"). Left alone, that
		# semicolon -- along with any @import/$var statements that precede a
		# rule -- leaks into the NEXT header and corrupts its selector match.
		# Only the text after the last top-level ';' can be an actual selector
		# list (selectors never contain ';'), so discard everything before it.
		header = text[i:brace].rsplit(';', 1)[-1].strip()
		depth = 1
		j = brace + 1
		while j < n and depth > 0:
			if text[j] == '{':
				depth += 1
			elif text[j] == '}':
				depth -= 1
			j += 1
		body = text[brace + 1:j - 1]
		yield header, body
		i = j


def extract_classes_from_selector(sel):
	"""Extract every '.o_class' token from a selector, but only if the
	selector is PURELY a chain of class tokens (with an optional single
	leading bare element name, e.g. 'i.o_lp_done') and an optional trailing
	:before/:after -- no combinators, attribute selectors, or other pseudo-
	classes. This covers plain '.o_class', element+class 'i.o_class', and
	compound class chains '.o_class1.o_class2', while correctly rejecting
	descendant/child selectors ('.o_disabled>.o_icon_delete'), state pseudo-
	classes (':hover'), and Sass placeholder selectors ('%o_icon_foo')."""
	if COMBINATOR_RE.search(sel):
		return []
	core = PSEUDO_SUFFIX_RE.sub('', sel)
	tokens = CLASS_TOKEN_RE.findall(core)
	if not tokens:
		return []
	remainder = re.sub(r'^[a-zA-Z]*', '', core, count=1)
	remainder = CLASS_TOKEN_RE.sub('', remainder)
	if remainder != '':
		return []
	return tokens


def parse_icons_scss(path):
	"""Returns dict class_name -> list of (fa_name_or_None, variant)."""
	with open(path, encoding='utf-8') as f:
		text = strip_comments(f.read())

	classes = {}
	skipped = []

	for header, body in split_rules(text):
		selectors = [s.strip() for s in header.split(',')]
		class_names = []
		for sel in selectors:
			class_names.extend(extract_classes_from_selector(sel))
		if not class_names:
			continue

		# Each hit is (fa_name_or_None, variant, glyph_id) -- glyph_id disambiguates
		# hits that would otherwise look identical for GROUPING purposes. For
		# FontAwesome-backed hits fa_name already disambiguates (glyph_id == fa_name).
		# For OpenOlat-font hits fa_name is always None (we don't have per-glyph FA
		# names), so glyph_id must be the actual codepoint -- otherwise every OpenOlat-
		# font class collapses into a single (None, 'OpenOlat font') group and all but
		# one class silently loses its rendered icon (see: only card2brain visible).
		hits = []
		for m in ADD_ICON_RE.finditer(body):
			fa_name = m.group(1)
			solid = (m.group(2) != 'false')
			variant = 'fa-solid' if solid else 'fa-regular'
			hits.append((fa_name, variant, fa_name))
		for m in ADD_BRAND_ICON_RE.finditer(body):
			hits.append((m.group(1), 'fa-brands', m.group(1)))
		fontello_match = FONTELLO_CONTENT_RE.search(body)
		if fontello_match and FONTELLO_FONT_RE.search(body):
			hits.append((None, OPENOLAT_FONT_VARIANT, fontello_match.group(1).upper()))

		if not hits:
			skipped.append((class_names, header))
			continue

		for cls in class_names:
			classes.setdefault(cls, [])
			for h in hits:
				if h not in classes[cls]:
					classes[cls].append(h)

	return classes, skipped


TOKEN_RE = re.compile(r'o_[A-Za-z0-9_-]+')


def build_usage_counts(class_names):
	"""Single pass over src/main: tokenize every file once and count occurrences
	of all o_* tokens, then look up each requested class. Far cheaper than
	re-walking/re-reading the whole tree once per class.

	.css/.scss files are skipped: they only contain each class's own icon
	*definition* (plus incidental SCSS nesting/@extend references), which
	would inflate every class's count by at least one and doesn't reflect
	real usage -- Occurrences should count where a class is actually applied
	(Java, Velocity, JS, ...), not where its icon is declared.

	Any directory literally named 'test' is pruned too -- this excludes
	src/test (if ever reachable from the scan root) and, more immediately,
	the ~48 node_modules/*/test folders bundled with the paella JS player,
	which are third-party test fixtures, not OpenOlat usage."""
	counts = defaultdict(int)
	wanted = set(class_names)
	skip_ext = ('.css', '.scss')
	for root, dirs, files in os.walk(SRC_MAIN):
		dirs[:] = [d for d in dirs if d != 'test']
		for fname in files:
			if fname.lower().endswith(skip_ext):
				continue
			path = os.path.join(root, fname)
			try:
				with open(path, encoding='utf-8', errors='ignore') as f:
					content = f.read()
			except (IsADirectoryError, PermissionError):
				continue
			for token in TOKEN_RE.findall(content):
				if token in wanted:
					counts[token] += 1
	return counts


def parse_oo_docs_css_classes(path):
	with open(path, encoding='utf-8') as f:
		css = f.read()
	return set(re.findall(r'\.(o_[A-Za-z0-9_-]+)', css))


def build_rows(classes, usage_counts):
	"""Group classes by their FULL hit list (not just the primary icon) --
	compound-icon classes (multiple @include o-add-icon calls, e.g.
	o_dialog_icon combining 'file' + 'comment') must never be merged into a
	group of unrelated classes that merely share the same PRIMARY icon, or
	their extra layer(s) get silently dropped from the table. Within a group
	of classes sharing the exact same hit list, the first class shows the
	Icon/FA Icon/Variant cells; the rest leave them blank (matches the
	pre-existing table convention for classes that render an identical icon)."""
	groups = defaultdict(list)
	for cls, hits in classes.items():
		groups[tuple(hits)].append(cls)

	def group_sort_key(item):
		hits, _members = item
		fa_name, variant, _glyph_id = hits[0]
		return (fa_name or '', variant, hits)

	rows = []
	for hits, members in sorted(groups.items(), key=group_sort_key):
		members.sort()
		fa_name, variant, _glyph_id = hits[0]
		extra = hits[1:]
		fa_display = fa_name or ''
		variant_display = variant
		if extra:
			fa_display = ', '.join([fa_name or ''] + [h[0] or '' for h in extra])
			variant_display = ', '.join([variant] + [h[1] for h in extra])
		for idx, cls in enumerate(members):
			if idx == 0:
				style = ICON_STYLE_OVERRIDES.get(cls)
				icon_token = f':o_icon_{cls}:' + (f'{{: style="{style}" }}' if style else '')
				rows.append({
					'icon': icon_token,
					'fa_icon': f'`{fa_display}`' if fa_display else '',
					'variant': variant_display,
					'oo_class': f'`{cls}`',
					'count': usage_counts.get(cls, 0),
				})
			else:
				rows.append({
					'icon': '',
					'fa_icon': '',
					'variant': '',
					'oo_class': f'`{cls}`',
					'count': usage_counts.get(cls, 0),
				})
	return rows


def render_markdown(rows, total_classes, total_refs, fa_icon_count):
	lines = []
	lines.append('# Icon Map')
	lines.append('')
	lines.append('OpenOlat maps [FontAwesome](https://fontawesome.com/) icons, and a small set of custom')
	lines.append('**OpenOlat font** glyphs, to its own CSS classes (`o_icon_*`). One FontAwesome icon can')
	lines.append('correspond to multiple OpenOlat classes — each class represents its own semantic context.')
	lines.append('')
	lines.append('The **OpenOlat font** is a small custom icon font (built with fontello) that OpenOlat')
	lines.append('ships in addition to FontAwesome, for glyphs FontAwesome does not offer: brand/product')
	lines.append('logos (card2brain, Opencast, edu-sharing, Jupyter, Mediasite), Creative Commons license')
	lines.append('badges, and a few drawing-tool icons.')
	lines.append('')
	lines.append('!!! info "Source data"')
	lines.append(f'    {fa_icon_count} FontAwesome icons · {total_classes} OpenOlat classes · {total_refs} references in source code (`src/main`)')
	lines.append('')
	lines.append('## Usage')
	lines.append('')
	lines.append('Icons are embedded with the `:o_icon_<class>:` MkDocs syntax, which renders the exact OpenOlat markup:')
	lines.append('')
	lines.append('```html')
	lines.append('<i class="o_icon o_icon_user" aria-hidden="true"></i>')
	lines.append('```')
	lines.append('')
	lines.append('## Icon Mapping Table')
	lines.append('')
	lines.append('| Icon | FA Icon | Variant | OpenOlat CSS Class | Occurrences |')
	lines.append('|------|---------|---------|---------------------|------------:|')
	for r in rows:
		lines.append(f"| {r['icon']} | {r['fa_icon']} | {r['variant']} | {r['oo_class']} | {r['count']} |")
	lines.append('')
	return '\n'.join(lines)


def main():
	if not os.path.isfile(ICONS_SCSS):
		print(f'ERROR: _icons.scss not found at {ICONS_SCSS}. Set OO_ROOT to your OpenOlat checkout.', file=sys.stderr)
		sys.exit(1)
	if not os.path.isfile(OO_DOCS_CSS):
		print(f'ERROR: oo-docs.css not found at {OO_DOCS_CSS}. Run scripts/sync-docs-css.sh first.', file=sys.stderr)
		sys.exit(1)

	classes, skipped = parse_icons_scss(ICONS_SCSS)
	print(f'Parsed {len(classes)} icon classes from _icons.scss.')
	if skipped:
		print(f'NOTE: {len(skipped)} class selector(s) had no o-add-icon/o-add-brand-icon/OpenOlat-font rule '
			'in their own block and were skipped (they may be pure style modifiers, not icon definitions):')
		for class_names, header in skipped:
			print(f'  - {", ".join(class_names)}  (selector: {header[:80]})')

	css_classes = parse_oo_docs_css_classes(OO_DOCS_CSS)
	parsed_classes = set(classes.keys())
	missing_from_css = sorted(parsed_classes - css_classes)
	# 'o_icon' itself and 'o_icon-*' are FontAwesome's own generated utility/
	# modifier classes (sizing, rotation, stacking, fixed-width, ...), inherited
	# via the $fa-css-prefix override -- not per-glyph icon definitions, so
	# their absence from _icons.scss is expected and not worth reporting.
	missing_from_scss = sorted(
		c for c in (css_classes - parsed_classes)
		if c != 'o_icon' and not c.startswith('o_icon-')
	)
	if missing_from_css:
		print(f'WARNING: {len(missing_from_css)} class(es) parsed from _icons.scss are missing from '
			f'oo-docs.css (stale bundle? re-run sync-docs-css.sh): {missing_from_css[:10]}{"..." if len(missing_from_css) > 10 else ""}')
	if missing_from_scss:
		print(f'WARNING: {len(missing_from_scss)} class(es) appear in oo-docs.css but were not parsed from '
			f'_icons.scss as icon definitions (parser gap, or a pure style modifier -- check manually): '
			f'{missing_from_scss}')

	print('Scanning src/main for usage counts (single pass)...')
	usage_counts = build_usage_counts(classes.keys())
	rows = build_rows(classes, usage_counts)
	total_refs = sum(r['count'] for r in rows)
	fa_icon_count = len({hits[0][0] for hits in classes.values() if hits[0][0]} |
		{h[0] for hits in classes.values() for h in hits[1:] if h[0]})
	md = render_markdown(rows, len(classes), total_refs, fa_icon_count)

	with open(OUTPUT, 'w', encoding='utf-8') as f:
		f.write(md)
	print(f'Wrote {len(rows)} rows to {OUTPUT}')


if __name__ == '__main__':
	main()
