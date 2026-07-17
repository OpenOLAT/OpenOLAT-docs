# Course Elements — Icon Reference

This page lists every course element with its real OpenOlat icon, ready to use in the manual.

Icons are rendered with the `:o_icon_<class>:` syntax — a MkDocs hook (`hooks/oo_icons.py`) that turns the token directly into `<i class="o_icon <class>" aria-hidden="true"></i>`, styled by `docs/stylesheets/oo-docs.css` (synced from OpenOlat's own `_icons.scss` via `bin/sync_docs_css.py`). This shows the exact icon OpenOlat uses — including the custom OpenOlat-font glyphs and layered/mirrored icons that a FontAwesome substitute could never reproduce.

**Usage:** insert an icon into a manual page with its CSS class, e.g.:

```
:o_icon_o_st_icon: Structure
```

---

## Content

| Icon | Name DE | Name EN | Alias | CSS Class |
|------|---------|---------|-------|-----------|
| :o_icon_o_bc_icon: | Ablageordner | Folder | `bc` | `o_bc_icon` |
| :o_icon_o_blog_icon: | Blog | Blog | `blog` | `o_blog_icon` |
| :o_icon_o_filetype_file: | Dokument | Document | `document` | `o_filetype_file` |
| :o_icon_o_tu_icon: | Externe Seite | External Page | `tu` | `o_tu_icon` |
| :o_icon_o_sp_icon: | HTML-Seite | HTML Page | `sp` | `o_sp_icon` |
| :o_icon_o_page_icon: | Inhaltsseite (Seite) | Page | `cepage` | `o_page_icon` |
| :o_icon_o_cp_icon: | CP-Lerninhalt | CP Learning Content | `cp` | `o_cp_icon` |
| :o_icon_o_ll_icon: | Linkliste | Link List | `ll` | `o_ll_icon` |
| :o_icon_o_podcast_icon: | Podcast | Podcast | `podcast` | `o_podcast_icon` |
| :o_icon_o_scorm_icon: | SCORM 1.2 | SCORM 1.2 | `scorm` | `o_scorm_icon` |
| :o_icon_o_st_icon: | Struktur | Structure | `st` | `o_st_icon` |
| :o_icon_o_icon_video: | Video | Video | `video` | `o_icon_video` |
| :o_icon_o_livestream_icon: | Video Livestream | Video Live Stream | `livestream` | `o_livestream_icon` |
| :o_icon_o_wiki_icon: | Wiki | Wiki | `wiki` | `o_wiki_icon` |

---

## Collaboration

| Icon | Name DE | Name EN | Alias | CSS Class |
|------|---------|---------|-------|-----------|
| :o_icon_o_dialog_icon:{: style="padding-right:4px;" } | Dateidiskussion | File Dialog | `dialog` | `o_dialog_icon` |
| :o_icon_o_co_icon: | E-Mail | E-Mail | `co` | `o_co_icon` |
| :o_icon_o_fo_icon: | Forum | Forum | `fo` | `o_fo_icon` |
| :o_icon_o_infomsg_icon: | Mitteilungen | Notifications | `info` | `o_infomsg_icon` |
| :o_icon_o_cmembers_icon: | Teilnehmerliste | Participant List | `cmembers` | `o_cmembers_icon` |

---

## Assessment & Tasks

| Icon | Name DE | Name EN | Alias | CSS Class |
|------|---------|---------|-------|-----------|
| :o_icon_o_gta_icon: | Aufgabe | Task | `ita` | `o_gta_icon` |
| :o_icon_o_gta_icon: | Gruppenaufgabe | Group Task | `gta` | `o_gta_icon` |
| :o_icon_o_ms_icon: | Bewertung | Assessment | `ms` | `o_ms_icon` |
| :o_icon_o_cl_icon: | Checkliste | Checklist | `checklist` | `o_cl_icon` |
| :o_icon_o_ep_icon: | Portfolioaufgabe | Portfolio Task | `ep` | `o_ep_icon` |
| :o_icon_o_icon_form: | Formular | Form | `form` | `o_icon_form` |
| :o_icon_o_iqself_icon: | Selbsttest | Self-Test | `iqself` | `o_iqself_icon` |
| :o_icon_o_iqtest_icon: | Test / Prüfung | Test | `iqtest` | `o_iqtest_icon` |
| :o_icon_o_practice_icon: | Übung | Practice | `practice` | `o_practice_icon` |
| :o_icon_o_survey_icon: | Umfrage | Survey | `survey` | `o_survey_icon` |
| :o_icon_o_icon_videotask: | Videoaufgabe | Video Task | `videotask` | `o_icon_videotask` |

---

## Administration & Organization

| Icon | Name DE | Name EN | Alias | CSS Class |
|------|---------|---------|-------|-----------|
| :o_icon_o_en_icon: | Einschreibung | Enrolment | `en` | `o_en_icon` |
| :o_icon_o_cal_icon: | Kalender | Calendar | `cal` | `o_cal_icon` |
| :o_icon_o_pf_icon: | Teilnehmerordner | Participant Folder | `pf` | `o_pf_icon` |
| :o_icon_o_appointment_icon: | Terminplanung | Appointment Scheduling | `appointments` | `o_appointment_icon` |
| :o_icon_o_den_icon: | Terminvergabe | Assignment of Dates | `den` | `o_den_icon` |
| :o_icon_o_icon_topicbroker: | Themenbörse | Topic Broker | `topicbroker` | `o_icon_topicbroker` |
| :o_icon_o_projectbroker_icon: | Themenvergabe (alt) | Topic Assignment | `projectbroker` | `o_projectbroker_icon` |
| :o_icon_o_icon_cns: | Auswahl | Selection | `cns` | `o_icon_cns` |
| :o_icon_o_lti_icon: | LTI-Seite | LTI Page | `lti` | `o_lti_icon` |

---

## Other

### Virtual Classroom

| Icon | Name DE | Name EN | Alias | CSS Class |
|------|---------|---------|-------|-----------|
| :o_icon_o_vc_icon: | BigBlueButton | BigBlueButton | `bigbluebutton` | `o_vc_icon` |
| :o_icon_o_vc_icon: | Zoom | Zoom | `zoom` | `o_vc_icon` |
| :o_icon_o_vc_icon: | Microsoft Teams | Microsoft Teams | `msteams` | `o_vc_icon` |
| :o_icon_o_vitero_icon: | vitero | vitero | `vitero` | `o_vitero_icon` |
| :o_icon_o_vc_icon: | Adobe Connect | Adobe Connect | `adobeconnect` | `o_vc_icon` |
| :o_icon_o_gotomeeting_icon: | GoToMeeting | GoToMeeting | `gotomeeting` | `o_gotomeeting_icon` |
| :o_icon_o_openmeetings_icon: | OpenMeetings | OpenMeetings | `openmeetings` | `o_openmeetings_icon` |

---

### Third-party Integrations

These use OpenOlat's own custom icon font (fontello-built) rather than FontAwesome — glyphs FontAwesome doesn't have for these external brands. The `:o_icon_<class>:` syntax renders them exactly like any other icon on this page; no special handling needed.

| Icon | Name DE | Name EN | Alias | CSS Class |
|------|---------|---------|-------|-----------|
| :o_icon_o_card2brain_icon: | card2brain Lernkarten | card2brain Flashcards | `card2brain` | `o_card2brain_icon` |
| :o_icon_o_edusharing_icon: | edu-sharing | edu-sharing | `edusharing` | `o_edusharing_icon` |
| :o_icon_o_edubase_icon: | Edubase | Edubase | `edubase` | `o_edubase_icon` |
| :o_icon_o_jupyter_icon: | JupyterHub | JupyterHub | `jupyterHub` | `o_jupyter_icon` |
| :o_icon_o_mediasite_icon: | MediaSite | MediaSite | `mediaSite` | `o_mediasite_icon` |
| :o_icon_o_opencast_icon: | Opencast | Opencast | `opencast` | `o_opencast_icon` |
