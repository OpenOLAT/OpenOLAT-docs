# Autorenbereich - Übersicht {: #authoring}

:octicons-device-camera-video-24: **Video-Einführung**: [Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>){:target="_blank"}

Im Autorenbereich finden OpenOlat Autor:innen alle Werkzeuge, um Kurse und andere Lernressourcen zu erstellen, zu importieren und zu bearbeiten.

Alle bereits vorhandenen Kurse und Lernressourcen werden in einer Tabelle angezeigt.

![Liste der eigenen Lernressourcen, hervorgehoben die Buttons Datei importieren, Erstellen und Hilfe & Anleitungen, die Filter-Tabs mit den Filtern und die Zeile mit Suchfeld, Zahnrad und Download](assets/authoring_overview_v1_de.png){ class="shadow lightbox" title="Tab Meine Einträge im Autorenbereich · 2026.10.08" }

Über die Buttons "Datei importieren" und "Erstellen" oben rechts legen Sie neue Kurse und Lernressourcen an, siehe [Autorenbereich - Kurse und Lernressourcen erstellen](authoring_new_course.de.md). Unter "Hilfe & Anleitungen" finden Sie die Hilfeangebote, die für den Autorenbereich eingerichtet sind.

### Favoriten {: #favourites}
Im Filter-Tab "Favoriten" finden Sie alle Lernressourcen, die Sie selbst als Favorit gekennzeichnet haben. Diese Ansicht wird standardmässig angezeigt, wenn Sie den Autorenbereich aufrufen. Haben Sie noch keine Lernressource als Favorit gekennzeichnet, öffnet OpenOlat stattdessen den Filter-Tab "Meine Einträge".

### Meine Kurse {: #my_courses}
Im Filter-Tab "Meine Kurse" finden Sie alle Kurse, die Sie erstellt haben oder bei denen Sie als Besitzer:in (Co-Autor:in) eingetragen sind. "Meine Kurse" ist eine Teilmenge von "Meine Einträge".

### Meine Einträge {: #my_entries}
Im Filter-Tab "Meine Einträge" finden Sie alle Lernressourcen, die Sie erstellt haben oder bei denen Sie als Besitzer:in (Co-Autor:in) eingetragen sind. Das sind neben den Kursen auch Test-Lernressourcen, Formulare, usw.

### Suche {: #search}
Im Filter-Tab "Suche" können Sie nach bestimmten Lernressourcen suchen. Hier sind alle Lernressourcen auffindbar, auf die Sie Zugriff haben. Sie können gezielt nach einem Titel suchen oder über die Filter Ihre Ergebnisse eingrenzen.

### Gelöscht {: #authoring-deleted}

Im Filter-Tab "Gelöscht" haben Sie Zugriff auf Ihre gelöschten Lernressourcen, bei denen Sie als Besitzer:in (Co-Autor:in) eingetragen sind. Der Tab "Gelöscht" ist somit eine Art Papierkorb. Hier können Sie Ihre Lernressourcen/Kurse wiederherstellen. Das dauerhafte Löschen der Lernressourcen/Kurse ist nur durch Administrator:innen oder Lernressourcenverwalter:innen möglich.

### Eigene Filter-Tabs erstellen [:octicons-tag-16:{ title="ab Release 16.0 (OO-5482)" }](https://track.frentix.com/issue/OO-5482){:target="_blank"} {: #custom_filter_tabs}
Sie können in der Zeile mit den Filter-Tabs "Favoriten" bis "Gelöscht" auch eine häufig benötigte Filterabfrage komplett neu erstellen.<br>Mit Klick auf "Filter speichern" können Sie Ihrer aktuellen Filterkombination einen eigenen Namen geben, die dann direkt so wieder aufgerufen werden kann.

![Menü mit drei Punkten rechts über der Filterzeile geöffnet, der Eintrag Filter speichern ist hervorgehoben](assets/authoring_save_filter_v1_de.png){ class="shadow lightbox" title="Tab Meine Einträge im Autorenbereich · 2026.09.29" }

### Buttons zum Filtern {: #filter_buttons}
In der zweiten Zeile sind bereits mehrere Buttons mit Filteroptionen angezeigt, zum Beispiel "Technischer Typ", "Durchführungsformat", "Status" und "Typ". Unter "Mehr..." können Sie weitere Buttons anzeigen. Klicken Sie zur weiteren Filterung auf den kleinen Pfeil nach unten und es werden die Filtermöglichkeiten zur Auswahl angezeigt.<br>
Der Filter "Autor:in / Besitzer:in" durchsucht den Vornamen, den Nachnamen, den Benutzernamen und die E-Mail-Adresse der Besitzer:innen. Die Suche nach der E-Mail-Adresse ist besonders nützlich, wenn mehrere Autor:innen denselben Nachnamen haben.

### Suchfeld {: #search_field}
Im Suchfeld können Sie direkt nach dem Titel suchen. Auch Teile des Titels liefern bereits ein Suchergebnis.

Weitere Details zu den Filteroptionen und zum Tabellenkonzept finden Sie auf der Seite [Mit Tabellen arbeiten](../basic_concepts/Table_Concept.de.md).

!!! tip "Tipp"

    Falls Sie einmal einen Kurs oder eine Lernressource nicht (mehr) finden, könnte es am Filter "Status" liegen. Prüfen Sie, welche Status dort ausgewählt sind. Gelöschte Lernressourcen stehen im Tab "Gelöscht".


### Spalten konfigurieren {: #configure_columns}

Über das Zahnrad-Icon kann ausgewählt werden, welche Spalten in der Tabelle angezeigt werden. Sie können so individuell die relevanten Informationen zusammenstellen.

![Zahnrad öffnet die Liste Spalten auswählen, hervorgehoben die Einträge Einstellungen, Mitgliederverwaltung und Inhalt editieren am Ende der Liste](assets/authoring_select_columns_v1_de.png){ class="shadow lightbox" title="Liste Spalten auswählen im Autorenbereich · 2026.10.08" }

**Beispiel**:<br>
In der Spalte "Ref." ist angezeigt, ob bzw. wie oft eine Lernressource in OpenOlat Kursen referenziert wurde. Klicken Sie auf diese Zahl, werden Ihnen die Kurse namentlich angezeigt. Sie können dann direkt zum gewünschten Kurs springen.

![Zahl in der Spalte Ref. öffnet die Liste Wird in folgenden Kursen eingesetzt mit dem Kurs, der den Test einsetzt](assets/autorenbereich_spalten_auswaehlen2_v2_de.png){ class="shadow lightbox" title="Spalte Ref. in der Tabelle des Autorenbereichs · 2026.09.28" }

#### Spalten für häufige Aktionen [:octicons-tag-16:{ title="ab Release 21.1 (OO-9780)" }](https://track.frentix.com/issue/OO-9780){:target="_blank"} {: #action_columns}

Brauchen Sie dieselbe Aktion oft, etwa bei vielen Kursen nacheinander die Mitglieder, sparen Sie sich mit einer Symbolspalte den Weg über das Menü unter den 3 Punkten. Drei solche Spalten blenden Sie über das Zahnrad ein:

* **Einstellungen:** Das Zahnradsymbol öffnet die Einstellungen der Lernressource im Tab "Metadaten".
* **Mitgliederverwaltung:** Das Symbol öffnet die Mitgliederverwaltung der Lernressource.
* **Inhalt editieren:** Das Stiftsymbol öffnet den Editor der Lernressource. Der Tooltip nennt ihn beim Namen, etwa "Kurseditor" oder "Testeditor". Bei Lernressourcen, die sich nicht bearbeiten lassen oder die beendet oder im Papierkorb sind, bleibt die Zelle leer.

Die drei Spalten sind ab Werk ausgeblendet. Die Spaltenauswahl bietet sie Autor:innen, Lernressourcenverwalter:innen und Administrator:innen an.

### Tabelle downloaden {: #download_table}
Sie können die gesamte Tabelle in dem aktuell angezeigten Zustand herunterladen.

### Spalten sortieren [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9204)" }](https://track.frentix.com/issue/OO-9204){:target="_blank"} {: #sort_columns}
Durch Klick auf einen Spaltentitel werden alle Einträge der Tabelle alphabetisch, nach Datum, usw. sortiert. Leere Einträge erscheinen dabei unabhängig von der Sortierrichtung immer am Ende der Liste.

**Beispiel**: Klick auf Spaltentitel "Titel der Lernressource" sortiert die Tabelle alphabetisch nach dem Titel. Bei nochmaligem Klick umgekehrt alphabetisch.

Die Spalte "Status" wird immer in folgender fester Reihenfolge sortiert: Vorbereitung, Review, Freigabe Betreuer:innen, Veröffentlicht, Beendet, Papierkorb.

#### Sortierung nach Zeitabschnitt [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9218)" }](https://track.frentix.com/issue/OO-9218){:target="_blank"}

!!! note "Hinweis"
    Die Spalte "Zeitabschnitt" sortiert Einträge chronologisch nach dem Zeitrahmen und nicht alphabetisch nach der Kurzbezeichnung. Die Reihenfolge ist:

    1. nach Beginndatum
    2. ohne Beginndatum: nach Enddatum
    3. ohne Zeitrahmen: ans Ende der Liste
    4. innerhalb desselben Zeitraums: alphabetisch

    Einträge ohne Zeitabschnitt erscheinen immer am Ende der Liste.

![Spalte Zeitabschnitt aufsteigend sortiert, zuerst nach Beginndatum, dann Einträge nur mit Enddatum, Einträge ohne Zeitabschnitt am Listenende](assets/authoring_sort_time_period_v1_de.png){ class="shadow lightbox" title="Spalte Zeitabschnitt in der Tabelle des Autorenbereichs · 2026.10.08" }

Die verfügbaren Zeitabschnitte stellt die System-Administration bereit. Wie Administrator:innen Zeitabschnitte verwalten, beschreibt die Seite [Modul Zeitabschnitte](../../manual_admin/administration/Modules_Time_Period.de.md).

[Zum Seitenanfang ^](#authoring)

---

### Typfilter [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9204)" }](https://track.frentix.com/issue/OO-9204){:target="_blank"} {: #type_filter}

Der Filter "Typ" bietet unter anderem die folgenden Bezeichnungen an: "Audio" sowie eine Gruppe "Andere", die folgende Typen zusammenfasst: "Test (QTI 1.2 - nicht mehr unterstützt)", "Fragebogen", "Film", "Animation", "Andere Datei".

[Zum Seitenanfang ^](#authoring)

---


## Weiterführende Informationen {: #further_information}

[Autorenbereich - Kurse und Lernressourcen erstellen >](authoring_new_course.de.md)<br>
[Mit Tabellen arbeiten >](../basic_concepts/Table_Concept.de.md)<br>
[Modul Zeitabschnitte >](../../manual_admin/administration/Modules_Time_Period.de.md)<br>
[Kurs erstellen >](../../manual_user/learningresources/Creating_Course.de.md)<br>
[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../../manual_how-to/my_first_course/my_first_course.de.md)<br>
[Kursbausteine im Kurseditor >](../../manual_user/learningresources/General_Configuration_of_Course_Elements.de.md)<br>
[Lernpfadkurs - Überblick >](../../manual_user/learningresources/Learning_path_course.de.md)

**youtube**<br>
[Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>)

[Zum Seitenanfang ^](#authoring)
