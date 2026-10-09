# Autorenbereich - Kurse und Lernressourcen erstellen {: #authoring_new_course}

## Neue OpenOlat Lernressourcen erstellen

Im Autorenbereich öffnet der Button "Erstellen" ein Menü mit den Lernressourcen, die Sie erstellen können:

![Geöffnetes Menü Erstellen mit den Lernressourcen der Liste unten, von Kurs und Kurs aus Template bis Word, Excel und PowerPoint](assets/authoring_new_course_create_menu_v1_de.png){ class="shadow lightbox" title="Menü Erstellen im Autorenbereich · 2026.10.09" }

Einige Einträge zeigt das Menü nur, wenn die System-Administration die zugehörige Funktion eingeschaltet hat: Formular, Wiki und Portfolio 2.0 Vorlage über das jeweilige Modul, Word, Excel und PowerPoint über einen [Dokumenteneditor](../../manual_admin/administration/External_Tools_-_Administration.de.md#dokumenteneditoren).

Die Buttons "Erstellen" und "Datei importieren" sehen Autor:innen, Lernressourcenverwalter:innen und Administrator:innen.

Der konkrete Erstellungsprozess ist auf den folgenden Seiten beschrieben:

* Kurs erstellen <br>
[Handbuchartikel](../learningresources/Creating_Course.de.md) | [Ausführliche Anleitung](../../manual_how-to/my_first_course/my_first_course.de.md)

* Kurs aus Template erstellen [:octicons-tag-16:{ title="ab Release 20.2 (OO-8897)" }](https://track.frentix.com/issue/OO-8897){:target="_blank"}<br>
[Handbuchartikel](../learningresources/Creating_Course.de.md#purpose)

* Tests erstellen<br>
[Handbuchartikel](../learningresources/Test.de.md) | [Ausführliche Anleitung](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md)

* Formulare erstellen <br>
[Handbuchartikel](../learningresources/Form.de.md)  | [Ausführliche Anleitung](../../manual_how-to/create_a_form/create_a_form.de.md)

* Ressourcenordner erstellen<br>
[Handbuchartikel](../learningresources/Resource_Folder.de.md) | [Ausführliche Anleitung](../../manual_how-to/multiple_use/multiple_use.de.md)

* Blog erstellen<br>
[Handbuchartikel](../learningresources/Blog.de.md) | [Ausführliche Anleitung](../../manual_how-to/blog/blog.de.md)

* Podcast erstellen <br>
[Handbuchartikel](../learningresources/Podcast.de.md) | [Ausführliche Anleitung](../../manual_how-to/podcast/podcast.de.md)

* CP-Lerninhalt erstellen<br>
[Handbuchartikel](../learningresources/CP_Editor.de.md) | [Ausführliche Anleitung](../../manual_how-to/content_package/content_package.de.md)

* Wiki erstellen <br>
[Handbuchartikel](../learningresources/Wiki.de.md) | [Ausführliche Anleitung](../../manual_how-to/wikis/wikis.de.md)

* Portfolio 2.0 Vorlage erstellen<br>
[Handbuchartikel](../learningresources/Portfolio_template_Creation.de.md)

* Glossar erstellen<br>
[Handbuchartikel](../learningresources/Glossary.de.md)

* Word-, Excel- und PowerPoint-Dateien erstellen<br>
[Handbuchartikel](../learningresources/index.de.md#further_learningresources)

!!! tip "Tipp"

    Wenn Sie Ihre Kurse systematisch aufbauen und Lernressourcen in mehreren Kursen verwenden wollen, empfiehlt es sich, die Lernressourcen im Autorenbereich statt in den Kursbausteinen der Kurse zu erstellen.

[Zum Seitenanfang ^](#authoring_new_course)

---

## Lernressourcen importieren

![Dialog mit den importierbaren Formaten, dem Feld zum Hochladen der Datei und dem Pflichtfeld Administrative Freigabe](assets/authoring_new_course_import_file_v1_de.png){ class="shadow lightbox" title="Dialog Datei importieren · 2026.10.09" }

### Datei importieren
Lernressourcen, die ausserhalb von OpenOlat erstellt oder aus einem anderen OpenOlat-System exportiert wurden, können in OpenOlat importiert werden: vorausgesetzt, sie liegen in einem kompatiblen Format vor. Importieren lassen sich aus OpenOlat exportierte Lernressourcen, Videos im Format MP4, die Standardformate IMS Content Packaging, IMS QTI 2.1 Test und SCORM 1.2 sowie beliebige Dateien.

Im Dialog "Datei importieren" laden Sie die Datei im Feld "Datei" hoch und wählen unter "Administrative Freigabe" die Organisation, der die Lernressource zugeordnet wird. Nach dem Hochladen zeigt der Dialog den erkannten Typ und das Feld "Titel der Lernressource" mit dem Titel aus der Datei, den Sie anpassen können.

Verwendet die importierte Lernressource weitere Lernressourcen, zum Beispiel ein Kurs mit einem Wiki oder einem Test, zeigt der Dialog zusätzlich "Referenzierte Ressourcen". Die Option "importieren und verknüpfen" ist vorausgewählt: OpenOlat importiert die verwendeten Lernressourcen mit und verknüpft sie. Nach dem Import eines Kurses publizieren Sie ihn im Kurseditor, damit seine Inhalte für Sie und andere OpenOlat-Benutzer:innen sichtbar sind.

Am Ende des Imports öffnet OpenOlat die Einstellungen der Lernressource auf dem [Tab "Metadaten"](../learningresources/Course_Settings_Metadata.de.md). Dort prüfen Sie Titel und Kennzeichen und nehmen weitere Konfigurationen vor, etwa die Lizenz.

### Per URL einbinden [:octicons-tag-16:{ title="ab Release 13.2 (OO-3859)" }](https://track.frentix.com/issue/OO-3859)
Externe Medien lassen sich auch per URL einbinden, ohne die Datei nach OpenOlat hochzuladen. Öffnen Sie dazu im Autorenbereich das Auswahlmenü neben dem Button "Datei importieren" und wählen Sie "Per URL einbinden".

![Eintrag Per URL einbinden im Auswahlmenü neben dem Button Datei importieren](assets/authoring_embed_via_url_v2_de.png){ class="shadow lightbox" title="Auswahlmenü im Autorenbereich" }

OpenOlat erkennt anhand der URL automatisch den passenden Ressourcentyp und legt eine entsprechende Lernressource an, in der das Medium verlinkt ist. Bei Videos entsteht so eine [Lernressource Video](../learningresources/Learning_resource_Video.de.md); sämtliche Funktionen des OpenOlat Video-Editors stehen anschliessend zur Verfügung.

![URL eines YouTube-Videos eingetragen, Typ Video erkannt und Titel der Lernressource aus der Quelle vorausgefüllt](assets/authoring_embed_via_url_dialogue_v1_de.png){ class="shadow lightbox" title="Dialog Per URL einbinden" }

Unterstützt werden folgende Ressourcen:

* Videos: MP4, m3u8, YouTube, Vimeo, Panopto
* Blog oder Podcast

Medien von weiteren Plattformen gibt die System-Administration bei Bedarf als Medien-Server frei, unter:<br>
`Administration > Login > Sicherheit > Tab "Medien-Server"`<br>
Mehr dazu unter [Sicherheit](../../manual_admin/administration/Login_Security.de.md#tab_mediaserver).

Der Dialog enthält folgende Felder:

| Feld | Beschreibung |
| ---- | ------------ |
| **URL** | Link zur externen Ressource. Nach der Eingabe ermittelt OpenOlat automatisch den Typ und, sofern verfügbar, den Titel des Mediums. |
| **Typ** | Der erkannte Ressourcentyp. Passen mehrere Typen zur URL, wählen Sie hier den gewünschten aus. |
| **Titel der Lernressource** | Pflichtfeld. Name der neuen Lernressource. Bei Videos wird der Titel aus der Quelle vorausgefüllt und kann angepasst werden. |
| **Kennzeichen** | Optionale externe Kennung, die in der Kursübersicht angezeigt wird, siehe [Kennzeichen](../learningresources/Course_Settings_Metadata.de.md#externalref). |
| **Administrative Freigabe** | Pflichtfeld. Organisation, der die Lernressource administrativ zugeordnet wird. |

Mit "Einbinden" erstellen Sie die Lernressource.

[Zum Seitenanfang ^](#authoring_new_course)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Externe Werkzeuge: Übersicht >](../../manual_admin/administration/External_Tools_-_Administration.de.md)<br>
[Kurs erstellen >](../learningresources/Creating_Course.de.md)<br>
[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../../manual_how-to/my_first_course/my_first_course.de.md)<br>
[Tests erstellen >](../learningresources/Test.de.md)<br>
[Wie gehe ich vor, wenn ich einen Test erstelle? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md)<br>
[Formulare - Übersicht >](../learningresources/Form.de.md)<br>
[Wie erstelle ich eine Formular-Lernressource? >](../../manual_how-to/create_a_form/create_a_form.de.md)<br>
[Ressourcenordner >](../learningresources/Resource_Folder.de.md)<br>
[Wie kann ich dieselben Dateien in mehreren Kursen einsetzen? >](../../manual_how-to/multiple_use/multiple_use.de.md)<br>
[Blog: Übersicht >](../learningresources/Blog.de.md)<br>
[Wie erstelle ich einen Blog? >](../../manual_how-to/blog/blog.de.md)<br>
[Podcast: Übersicht >](../learningresources/Podcast.de.md)<br>
[Wie erstelle ich einen Podcast? >](../../manual_how-to/podcast/podcast.de.md)<br>
[CP-Lerninhalt erstellen >](../learningresources/CP_Editor.de.md)<br>
[Wie erstelle ich ein Content Package? >](../../manual_how-to/content_package/content_package.de.md)<br>
[Wiki erstellen >](../learningresources/Wiki.de.md)<br>
[Wie erstelle ich ein Wiki? >](../../manual_how-to/wikis/wikis.de.md)<br>
[Portfoliovorlage: Erstellung >](../learningresources/Portfolio_template_Creation.de.md)<br>
[Glossar >](../learningresources/Glossary.de.md)<br>
[Lernressourcen >](../learningresources/index.de.md)<br>
[Kurseinstellungen - Tab Metadaten >](../learningresources/Course_Settings_Metadata.de.md)<br>
[Lernressource: Video >](../learningresources/Learning_resource_Video.de.md)<br>
[Sicherheit >](../../manual_admin/administration/Login_Security.de.md)

**Weiterführend**<br>
[Autorenbereich - Übersicht >](../area_modules/Authoring.de.md)<br>
[Kurseinstellungen >](../learningresources/Course_Settings.de.md)

**youtube**<br>
[Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>)<br>
[Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>)<br>
[Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>)<br>
[Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>)<br>
[Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>)<br>
[Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>)<br>
[Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>)<br>
[Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>)<br>
[Tests erstellen/bearbeiten](<https://www.youtube.com/embed/eNNdDdQDlfs>)

[Zum Seitenanfang ^](#authoring_new_course)
