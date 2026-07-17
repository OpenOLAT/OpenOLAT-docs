#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

SITE="${1:-manual_user}"
LANG="${2:-en}"

case "$SITE" in
	manual_user)        SECTION="User manual" ;;
	manual_admin)        SECTION="Admin manual" ;;
	manual_how-to)        SECTION="How to" ;;
	manual_dev)        SECTION="Developer cookbook" ;;
	release_notes)        SECTION="Release notes" ;;
	reference_glossary)        SECTION="Reference glossary" ;;
	*)
		echo "Unknown site: $SITE" >&2
		echo "Valid sites: manual_user manual_admin manual_how-to manual_dev release_notes reference_glossary" >&2
		exit 1
		;;
esac

case "$LANG" in
	en)
		DEFAULT_LANG=en
		DEFAULT_LANGUAGE_ONLY=true
		SEARCH_LANGS="        - en"
		;;
	de)
		DEFAULT_LANG=de
		DEFAULT_LANGUAGE_ONLY=true
		SEARCH_LANGS="        - de"
		;;
	all)
		DEFAULT_LANG=en
		DEFAULT_LANGUAGE_ONLY=false
		SEARCH_LANGS="        - en
        - de"
		;;
	*)
		echo "Unknown lang: $LANG (use en, de or all)" >&2
		exit 1
		;;
esac

if [ -x "venv/bin/mkdocs" ]; then
	MKDOCS="venv/bin/mkdocs"
	PYTHON="venv/bin/python3"
elif command -v mkdocs >/dev/null 2>&1; then
	MKDOCS="mkdocs"
	PYTHON="python3"
else
	echo "ERROR: mkdocs not found." >&2
	echo "Either create a local venv:  python3 -m venv venv && venv/bin/pip install -r requirements.txt" >&2
	echo "or install mkdocs globally:  pip3 install -r requirements.txt" >&2
	exit 1
fi

# The generated config re-declares the whole i18n plugin block (needed to
# override default_language/default_language_only), which would otherwise
# silently drop mkdocs.yml's nav_translations mapping -- MkDocs does not
# deep-merge plugin lists on INHERIT, it replaces them wholesale. Pull the
# mapping live from mkdocs.yml instead of duplicating it here, so there is a
# single source of truth and no risk of drift.
NAV_TRANSLATIONS=$("$PYTHON" -c "
import yaml
with open('mkdocs.yml') as f:
	cfg = yaml.load(f, Loader=yaml.Loader)
for p in cfg['plugins']:
	if isinstance(p, dict) and 'i18n' in p:
		nt = p['i18n'].get('nav_translations')
		if nt:
			print(yaml.dump({'nav_translations': nt}, allow_unicode=True, default_flow_style=False, width=1000), end='')
" | sed 's/^/      /')

cat > mkdocs.local.yml <<EOF
INHERIT: mkdocs.yml

plugins:
  - monorepo
  - i18n:
      default_language: ${DEFAULT_LANG}
      default_language_only: ${DEFAULT_LANGUAGE_ONLY}
      languages:
        en:
          name: English
          build: true
        de:
          name: Deutsch
          build: true
${NAV_TRANSLATIONS}
  - search:
      lang:
${SEARCH_LANGS}

nav:
  - Start:
    - Overview: index.md
  - ${SECTION}: '!include ./sites/${SITE}/mkdocs.yml'
  - '': '!include ./sites/en/mkdocs.yml'
  - '': '!include ./sites/de/mkdocs.yml'
EOF

echo "Serving ${SITE} (lang=${LANG}) via mkdocs.local.yml (using ${MKDOCS}) ..."
exec "$MKDOCS" serve -f mkdocs.local.yml --dirtyreload
