# Icon Workflow

How OpenOlat icons get into this manual, how to use them when writing, and how to keep the two systems in sync.

## Why this exists

OpenOlat maps its own CSS classes (`o_icon_*`) to FontAwesome glyphs (and a small custom "OpenOlat font" for glyphs FontAwesome doesn't have) in `_icons.scss`. The manual used to restate that mapping by hand with FontAwesome shortcodes — which drifted whenever an icon changed in OpenOlat, and could never reproduce the custom-font or compound/mirrored icons at all.

Instead, the manual now vendors OpenOlat's own compiled icon CSS and font files, and a small MkDocs hook renders the real class directly. `_icons.scss` is the single source of truth; everything else is generated or synced from it.

## Author usage

Write the OpenOlat CSS class directly, prefixed with `o_icon_`:

```
:o_icon_o_st_icon: Structure
```

renders

```html
<i class="o_icon o_st_icon" aria-hidden="true"></i>
```

Look the class up in [Course Element Icons](../icons/course_elements_icons.md) (course elements) or the [Icon Map](../icons/reference_map.md) (every OpenOlat icon class).

- **Icons are always decorative** (`aria-hidden="true"`, no labelled form) — keep the icon next to text that names it; don't rely on the icon alone to convey meaning.
- **Compound and custom-font icons just work** — e.g. `:o_icon_o_dialog_icon:` (two layered FontAwesome glyphs) or `:o_icon_o_card2brain_icon:` (OpenOlat's own font) render exactly like any other icon, no special syntax needed.
- In a bare table cell with nothing else for scale, a compound icon's layered glyphs can look more separated than they do in the app's UI (see `o_dialog_icon` in the Icon Map for an example) — that's the icon's real, faithful rendering, not a bug. If it looks cramped against neighbouring content, an `attr_list` inline style scoped to that one occurrence is the fix (see `ICON_STYLE_OVERRIDES` in `bin/generate_reference_map.py` for a worked example) — never patch the shared icon definition itself, that would break parity with the app.

## Per-release sync

Whenever OpenOlat icons change (typically once per OpenOlat release), three steps keep the two systems in sync: first, in an OpenOlat checkout, compile the theme SCSS to regenerate the icon bundle; then run these two scripts:

- `python bin/sync_docs_css.py` — copies the compiled CSS and fonts into `docs/stylesheets/`
- `python bin/generate_reference_map.py` — regenerates the Icon Map from `_icons.scss`

Then commit the updated `docs/stylesheets/oo-docs.css`, `docs/stylesheets/fonts/`, and `sites/manual_dev/docs/icons/reference_map.md`. These three steps are the only manual work keeping the two systems in sync — everything else (rendering, class discovery) is automatic.

`course_elements_icons.md` is **not** regenerated — it's hand-maintained, since it also carries editorial content (which elements exist, how they're grouped) beyond a raw class dump.
