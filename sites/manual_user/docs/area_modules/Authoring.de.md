# Autorenbereich - Übersicht {: #authoring}

:octicons-device-camera-video-24: **Video-Einführung**: [Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>){:target="_blank"}

Im Autorenbereich finden OpenOlat Autor:innen alle Werkzeuge, um Kurse und andere Lernressourcen zu erstellen, zu importieren und zu bearbeiten.

Alle bereits vorhandenen Kurse und Lernressourcen werden in einer Tabelle angezeigt.

![Elf nummerierte Markierungen auf den Bedienelementen des Autorenbereichs, sie entsprechen den nummerierten Abschnitten dieser Seite](assets/autorenbereich_uebersicht1_v1_de.png){ class="shadow lightbox" }


### 1. Favoriten
Im Filter-Tab "**Favoriten**" finden Sie alle Lernressourcen, die Sie selbst als Favorit gekennzeichnet haben. Diese Ansicht wird standardmässig angezeigt, wenn Sie den Autorenbereich aufrufen.

### 2. Meine Kurse
Im Filter-Tab "**Meine Kurse**" finden Sie alle Kurse, die Sie erstellt haben oder bei denen Sie als Besitzer:in (Co-Autor:in) eingetragen sind. "Meine Kurse" ist eine Teilmenge von "Meine Einträge". 

### 3. Meine Einträge 
Im Filter-Tab "**Meine Einträge**" finden Sie alle Lernressourcen, die Sie erstellt haben oder bei denen Sie als Besitzer:in (Co-Autor:in) eingetragen sind. Das sind neben den Kursen auch Test-Lernressourcen, Formulare, usw. 

### 4. Suchmaske 
Im Filter-Tab "**Suchmaske**" können Sie nach bestimmten Lernressourcen suchen. Hier sind alle Lernressourcen auffindbar, auf die Sie Zugriff haben. Sie können gezielt nach einem Titel suchen oder über die Filter ihre Ergebnisse eingrenzen.

### 5. Gelöscht {: #authoring-deleted}

Im Filter-Tab "**Gelöscht**" haben Sie Zugriff auf Ihre gelöschten Lernressourcen bei denen Sie als Besitzer:in (Co-Autor:in) eingetragen sind. Der Tab "Gelöscht" ist somit eine Art Papierkorb. Hier können Sie Ihre Lernressourcen/Kurse wiederherstellen.
Das dauerhafte Löschen der Lernressourcen/Kurse ist nur durch Administrator:innen oder Lernressourcenverwalter:innen möglich.

### 6. Eigene Filter-Tabs erstellen 
Sie können in der Zeile mit den Filter-Tabs (1-5) auch eine häufig benötigte Filterabfrage komplett neu erstellen.<br>Mit Klick auf "Filter speichern" können Sie Ihrer aktuellen Filterkombination einen eigenen Namen geben, die dann direkt so wieder aufgerufen werden kann. ![Offenes Menü mit dem Eintrag Filter speichern rechts über der Filterzeile](assets/Autorenbereich_Filter_172.png)

### 7. Buttons zum Filtern
In der zweiten Zeile sind bereits mehrere **Buttons** mit Filteroptionen angezeigt. Unter **Mehr** können Sie weitere Buttons anzeigen. Klicken Sie zur weiteren Filterung auf den kleinen Pfeil nach unten und es werden die Filtermöglichkeiten zur Auswahl angezeigt.<br>
Der Filter "Autor/Besitzer" durchsucht den Vornamen, den Nachnamen, den Benutzernamen und die E-Mail-Adresse der Besitzer:innen. Die Suche nach der E-Mail-Adresse ist besonders nützlich, wenn mehrere Autor:innen denselben Nachnamen haben.

### 8. Suchfeld 
Im **Suchfeld** können Sie direkt nach dem Titel suchen. Auch Teile des Titels liefern bereits ein Suchergebnis.

Weitere Details zu den Filteroptionen und zum Tabellenkonzept finden Sie auf der Seite [Mit Tabellen arbeiten](../basic_concepts/Table_Concept.de.md).

!!! tip "Tipp"

    Falls Sie einmal einen Kurs oder eine Lernressource nicht (mehr) finden, könnte es eventuell am Lebenszyklus liegen. Überprüfen Sie dort die Einstellungen. Vielleicht wurde hier einfach die falsche Auswahl getroffen.


### 9. Spalten konfigurieren

Über das Zahnrad-Icon kann ausgewählt werden, welche Spalten in der Tabelle angezeigt werden. Sie können so individuell die relevanten Informationen zusammenstellen.

![Liste Spalten auswählen mit den angehakten Einträgen Zeitabschnitt und Zeitabschnitt Beschr., geöffnet über das Zahnrad](assets/autorenbereich_spalten_auswaehlen_v2_de.png){ class="shadow lightbox" }

**Beispiel**:<br>
In der Spalte "Ref." ist angezeigt, ob bzw. wie oft eine Lernressource in OpenOlat Kursen referenziert wurde. Klicken Sie auf diese Zahl, werden Ihnen die Kurse namentlich angezeigt. Sie können dann direkt zum gewünschten Kurs springen.

![Zahl 5 in der Spalte Ref. öffnet die Liste der Kurse, die die Lernressource einsetzen](assets/autorenbereich_spalten_auswaehlen2_v1_de.png){ class="shadow lightbox" }

### 10. Tabelle downloaden
Sie können die gesamte Tabelle in dem aktuell angezeigten Zustand herunterladen.

### 11. Spalten sortieren [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9204)" }](https://track.frentix.com/issue/OO-9204){:target="_blank"}
Durch Klick auf einen Spaltentitel werden alle Einträge der Tabelle alphabetisch, nach Datum, usw. sortiert. Leere Einträge erscheinen dabei unabhängig von der Sortierrichtung immer am Ende der Liste.

**Beispiel**: Klick auf Spaltentitel "Titel der Lernressource" sortiert die Tabelle alphabetisch nach dem Titel. Bei nochmaligem Klick umgekehrt alphabetisch.

Die Spalte "Status" wird immer in folgender fester Reihenfolge sortiert: Vorbereitung, Review, Zugriff für Betreuer, Veröffentlicht, Beendet, Papierkorb.

#### Sortierung nach Zeitabschnitt [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9218)" }](https://track.frentix.com/issue/OO-9218){:target="_blank"}

!!! note "Hinweis"
    Die Spalte "Zeitabschnitt" sortiert Einträge chronologisch nach dem Zeitrahmen und nicht alphabetisch nach der Kurzbezeichnung. Die Reihenfolge ist:

    1. nach Beginndatum
    2. ohne Beginndatum: nach Enddatum
    3. ohne Zeitrahmen: ans Ende der Liste
    4. innerhalb desselben Zeitraums: alphabetisch

    Einträge ohne Zeitabschnitt erscheinen immer am Ende der Liste.

![Spalte Zeitabschnitt absteigend sortiert, gleiche Zeitabschnitte stehen beieinander, der Eintrag ohne Zeitabschnitt bleibt am Listenende](assets/autorenbereich_sort_time_period_v1_de.png){ class="shadow lightbox" }

Die verfügbaren Zeitabschnitte stellt die System-Administration bereit. Wie Administrator:innen Zeitabschnitte verwalten, beschreibt die Seite [Modul Zeitabschnitte](../../manual_admin/administration/Modules_Time_Period.de.md).

[Zum Seitenanfang ^](#authoring)

---

### 12. Typfilter [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9204)" }](https://track.frentix.com/issue/OO-9204){:target="_blank"} {: #type_filter}

Der Filter "Typ" bietet unter anderem die folgenden Bezeichnungen an: "Audio" sowie eine Gruppe **Weitere**, die folgende Typen zusammenfasst: Test (QTI 1.2, nicht mehr unterstützt), Fragebogen, Film, Animation, Andere Datei.

[Zum Seitenanfang ^](#authoring)

---


## Weiterführende Informationen {: #further_information}

[Mit Tabellen arbeiten >](../basic_concepts/Table_Concept.de.md)<br>
[Modul Zeitabschnitte >](../../manual_admin/administration/Modules_Time_Period.de.md)<br>
[Kurs erstellen (Übersicht) >](../../manual_user/learningresources/Creating_Course.de.md)<br>
[Wie erstelle ich meinen ersten OpenOlat-Kurs? (Ausführliche Anleitung) >](../../manual_how-to/my_first_course/my_first_course.de.md)<br>
[Kurseditor >](../../manual_user/learningresources/General_Configuration_of_Course_Elements.de.md)<br>
[Kursdesign >](../../manual_user/learningresources/Learning_path_course.de.md)

**youtube**<br>
[Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>)

[Zum Seitenanfang ^](#authoring)
