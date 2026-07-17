#!/usr/bin/env python3
"""
Sync the OpenOlat documentation CSS bundle (oo-docs.css) and its icon fonts
from an OpenOlat checkout into this docs repo.

The bundle is generated in OpenOlat by running `cssi` (compiletheme.sh), which
produces themes/light/oo-docs.css. Re-run this script whenever OpenOlat icons
change (typically once per OpenOlat release) and commit the updated
docs/stylesheets/oo-docs.css + docs/stylesheets/fonts/.

Usage:
	python bin/sync_docs_css.py                  # expects OpenOlat at ../OpenOLAT
	OO_ROOT=/path/to/OpenOLAT python bin/sync_docs_css.py
"""
import os
import shutil
import sys

DOCS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OO_ROOT = os.environ.get('OO_ROOT', os.path.join(DOCS_ROOT, '..', 'OpenOLAT'))
STATIC = os.path.join(OO_ROOT, 'src/main/webapp/static')

DEST = os.path.join(DOCS_ROOT, 'docs/stylesheets')
FONTS = os.path.join(DEST, 'fonts')

OO_DOCS_CSS_SRC = os.path.join(STATIC, 'themes/light/oo-docs.css')

FONT_AWESOME_FONTS = [
	'fa-solid-900.woff2', 'fa-solid-900.ttf',
	'fa-regular-400.woff2', 'fa-regular-400.ttf',
	'fa-brands-400.woff2', 'fa-brands-400.ttf',
]
OPENOLAT_FONTS = ['openolat.woff2', 'openolat.woff', 'openolat.ttf']


def main():
	if not os.path.isfile(OO_DOCS_CSS_SRC):
		print(f"ERROR: oo-docs.css not found at {os.path.join(STATIC, 'themes/light')}. "
			"Run 'cssi' in OpenOlat first.", file=sys.stderr)
		sys.exit(1)

	os.makedirs(FONTS, exist_ok=True)

	shutil.copy2(OO_DOCS_CSS_SRC, os.path.join(DEST, 'oo-docs.css'))

	for fname in FONT_AWESOME_FONTS:
		shutil.copy2(os.path.join(STATIC, 'font-awesome/webfonts', fname), os.path.join(FONTS, fname))

	for fname in OPENOLAT_FONTS:
		shutil.copy2(os.path.join(STATIC, 'themes/light/fonts/openolat', fname), os.path.join(FONTS, fname))

	font_count = len(os.listdir(FONTS))
	print(f'Synced oo-docs.css + {font_count} font files into docs/stylesheets/')


if __name__ == '__main__':
	main()
