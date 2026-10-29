# Kurseinstellungen - Tab Toolbar {: #tab_toolbar}


Im Tab "Toolbar" legen Sie fest, ob die Teilnehmer:innen im Kurs die Toolbar sehen und welche Werkzeuge darin erscheinen:<br>
`Kurs > Administration > Einstellungen > Tab "Toolbar"`

Ist die Checkbox "Toolbar sichtbar für Teilnehmer:innen" eingeschaltet, wählen Sie darunter die Werkzeuge aus. Den Tab bearbeiten Besitzer:innen des Kurses, Lernressourcenverwalter:innen, Administrator:innen und Personen mit dem Recht "Kurseditor".

![Checkbox "Toolbar sichtbar für Teilnehmer:innen" eingeschaltet, darunter die aktivierbaren Werkzeuge und die Zeilen Externes Kurstool 1 bis 4](assets/course_settings_toolbar1_v2_de.png){ class="shadow lightbox" title="Tab Toolbar der Kurseinstellungen · 2026.10.29" }

So erreichen Teilnehmende die Werkzeuge, die sie während des ganzen Kurses brauchen, an einer zentralen Stelle.

**Beispiel:**

![Toolbar aus Sicht der Teilnehmenden, markiert die freigeschalteten Werkzeuge: Infoseite mit dem Info-Symbol, Lernpfad, Kalender, Mitteilungen, E-Mail, Blog, Wiki, Forum, Dokumente und Kurssuche](assets/course_settings_toolbar_v2_de.png){ class="shadow lightbox" title="Toolbar eines Kurses aus Sicht der Teilnehmenden · 2026.10.27" }

Zu den [Werkzeugen](../learningresources/Using_Additional_Course_Features.de.md) der Toolbar zählen neben der Kurssuche, dem Glossar und dem Kurs-Chat Werkzeuge, die es auch als Kursbausteine gibt, z.B. Kurskalender, Liste der Teilnehmer:innen, E-Mail, Blog, Wiki, Forum und Dokumente. Bei [Wiki](../learningresources/Wiki.de.md) und [Blog](../learningresources/Blog.de.md) können Sie auch auf bereits erstellte Lernressourcen zurückgreifen. Die übrigen Werkzeuge ähneln den entsprechenden Kursbausteinen, bieten aber nicht alle Konfigurationsmöglichkeiten, die die Kursbausteine im Kurseditor haben.

Besonders in linear aufgebauten [Lernpfadkursen](Learning_path_course.de.md) stellt die Toolbar wichtige Werkzeuge bereit, unabhängig von der Reihenfolge der Lernschritte.

[Zum Seitenanfang ^](#tab_toolbar)

---

## Externe Kurstools [:octicons-tag-16:{ title="ab Release 21.0 (OO-9488)" }](https://track.frentix.com/issue/OO-9488) {: #external_tools}

Arbeiten Ihre Teilnehmer:innen neben dem Kurs mit weiteren Webanwendungen, etwa einem Stundenplan oder einem Schulportal, legen Sie die Links dorthin als externe Kurstools direkt in die Toolbar des Kurses. Pro Kurs stehen vier externe Kurstools zur Verfügung.

Eingerichtet werden sie unter `Kurs > Administration > Einstellungen > Tab "Toolbar"`. Die Zeilen "Externes Kurstool 1" bis "Externes Kurstool 4" stehen unter den Werkzeugen der Toolbar. Sie erscheinen nur, wenn bei "Toolbar sichtbar für Teilnehmer:innen" die Checkbox "Ein" aktiviert ist. Aktivieren Sie bei einem Tool die Checkbox "Ein", erscheinen darunter die Felder "Name", "URL", "Icon" und "Sichtbar für".

![Tab Toolbar und Zeilen Externes Kurstool 1 bis 4 markiert, Kurstool 1 eingeschaltet mit ausgefülltem Name, URL, Icon und Sichtbar für](assets/course_settings_toolbar_external_tools_entry_v1_de.png){ class="shadow lightbox" title="Externe Kurstools im Tab Toolbar der Kurseinstellungen · 2026.10.02" }

| Feld | Beschreibung |
|---|---|
| **Name** | Bezeichnung in der Toolbar, max. 64 Zeichen. Pflichtfeld. |
| **URL** | Absolute URL beginnend mit `http://` oder `https://`. Relative URLs, Anker, `javascript:`, `data:`, `mailto:`, `tel:` und protokollrelative Links werden abgelehnt. Pflichtfeld. |
| **Icon** | Auswahl aus dem Icon-Katalog (rund 30 Einträge, z.B. Link, E-Mail, Kalender, Stundenplan, Absenzen-Management, Schulportal). Pflichtfeld. |
| **Sichtbar für** | Separate Checkboxen für "Teilnehmer:innen", "Betreuer:innen" sowie "Besitzer:innen und Personen mit administrativen Rollen". Jede Option gilt nur für ihre Rolle: Ein Tool, das nur für Teilnehmer:innen sichtbar ist, sehen Betreuer:innen nicht. Administrator:innen, Lernressourcenverwalter:innen, Principals und Kursplaner:innen sehen das Tool, wenn die Option für Besitzer:innen ausgewählt ist. Bei einem neu eingeschalteten Tool ist diese Option vorausgewählt. Ist keine Option gewählt, zeigt das Formular die Warnung "Das Tool ist aktiviert, aber für niemanden sichtbar. Wählen Sie mindestens eine Option." Gespeichert wird das Tool trotzdem, in der Toolbar sieht es dann niemand. |

![Externes Kurstool Stundenplan mit Kalender-Icon rechts neben der Kurssuche markiert](assets/course_toolbar_with_external_tools_v2_de.png){ class="shadow lightbox" title="Externes Kurstool in der Toolbar des Kurses · 2026.10.02" }

!!! warning "Achtung"
    Entfernen Sie bei einem Tool die Checkbox "Ein" oder schalten Sie "Toolbar sichtbar für Teilnehmer:innen" aus, löscht OpenOlat beim Speichern Name, URL und Icon der betroffenen Tools, die Auswahl unter "Sichtbar für" wird zurückgesetzt. Beim erneuten Einschalten erfassen Sie die Angaben neu.

**Kurs kopieren / importieren**

- Die Konfiguration aller vier externen Kurstools wird beim Kopieren eines Kurses mitübernommen.
- Beim Importieren eines Kurses sind alle vier Tools ausgeschaltet. Name, URL und Icon werden nicht übernommen und müssen im importierten Kurs neu erfasst werden.

!!! info "Wichtig"
    Externe Kurstools öffnen immer in einem neuen Browserfenster. Es werden keine Nutzerdaten (Name, E-Mail usw.) an das Zielsystem übertragen.

[Zum Seitenanfang ^](#tab_toolbar)

---

## Weiterführende Informationen {: #further_information}

[Einsatz weiterer Kursfunktionen der Toolbar >](Using_Additional_Course_Features.de.md)<br>
[Wiki erstellen >](Wiki.de.md)<br>
[Blog: Übersicht >](Blog.de.md)<br>
[Lernpfadkurs - Überblick >](Learning_path_course.de.md)<br>
[Kurseinstellungen >](Course_Settings.de.md)<br>
[Kurseinstellungen - Tab Optionen >](Course_Settings_Options.de.md)

[Zum Seitenanfang ^](#tab_toolbar)

