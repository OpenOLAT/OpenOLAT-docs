"""
MkDocs hook + Markdown extension: OpenOLAT icons.

Turns the inline token  :o_icon_<cssclass>:  into the exact markup OpenOLAT uses
for its font icons, e.g.

	:o_icon_o_bc_icon:   ->  <i class="o_icon o_bc_icon" aria-hidden="true"></i>
	:o_icon_o_icon_user: ->  <i class="o_icon o_icon_user" aria-hidden="true"></i>

The glyphs come from docs/stylesheets/oo-docs.css, which is synced from OpenOLAT
via scripts/sync-docs-css.sh (single source of truth: OpenOLAT _icons.scss).

Icons are decorative only, so aria-hidden is always set -- always keep the icon
next to text that names it.

Loaded as a MkDocs hook (see mkdocs.yml `hooks:`); on_config registers the
extension on the Markdown instance with a priority above pymdownx.emoji so the
:o_icon_...: token is claimed before the emoji processor sees it.
"""
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

OO_ICON_RE = r':o_icon_(o_[A-Za-z0-9_-]+):'


class OoIconInlineProcessor(InlineProcessor):
	def handleMatch(self, m, data):
		cls = m.group(1)
		el = etree.Element('i')
		el.set('class', 'o_icon ' + cls)
		el.set('aria-hidden', 'true')
		return el, m.start(0), m.end(0)


class OoIconExtension(Extension):
	def extendMarkdown(self, md):
		md.inlinePatterns.register(OoIconInlineProcessor(OO_ICON_RE, md), 'oo_icon', 180)


def makeExtension(**kwargs):
	return OoIconExtension(**kwargs)


def on_config(config, **kwargs):
	config['markdown_extensions'].append(OoIconExtension())
	return config
