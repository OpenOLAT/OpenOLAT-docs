# Ablageordner {: #storage_folder}

Der "Ablageordner" eines Kurses dient den Kursbesitzer:innen als Ablage der im Kurs verwendeten Dateien. Hierzu zählen z.B. alle verwendeten HTML-Seiten, Grafiken und Dateien, die über den Kursbaustein "Ordner" zur Verfügung gestellt werden. Die Dateien liegen sozusagen griffbereit im Hintergrund und können jederzeit über die entsprechenden Kursbausteine bereitgestellt werden. Sie öffnen den Ablageordner über `Kurs > Administration > Dateien > Ablageordner`. Diesen Weg sehen Kursbesitzer:innen, Administrator:innen, Lernressourcenverwalter:innen und Personen mit dem Kursrecht "Kurseditor".

Teilnehmende haben keinen direkten, sondern nur einen indirekten Zugriff auf Dateien des Ablageordners. Um auf die Dateien zugreifen zu können, müssen diese über entsprechende [Kursbausteine](Course_Elements/index.de.md) verlinkt sein. Ein Ablageordner ist immer kursspezifisch.

![Dateien und Ordner in der Tabellenansicht, Papierkorb und Aktionen für ausgewählte Einträge wie Zippen oder E-Mail versenden, darunter der belegte Speicher](assets/storage_folder_files_v1_de.png){ class="shadow lightbox" title="Ablageordner eines Kurses" }

Im Ablageordner können Dateien hochgeladen, gelöscht, verschoben, kopiert, per E-Mail versendet, gesucht, gezippt, ausgepackt oder erstellt werden. Gelöschte Dateien und Ordner liegen im "Papierkorb", bis OpenOlat sie nach einer festgelegten Anzahl Tage endgültig löscht. Standardmässig können in OpenOlat HTML Dokumente erstellt werden. Sind in der System-Administration ergänzende Dokumenteneditoren aktiviert, können auch noch weitere Dateiformate erstellt werden: `Administration > Externe Werkzeuge > Dokumenteneditoren`. Beispielsweise können bei Verwendung von OnlyOffice auch Word, Excel oder PowerPoint Dateien erstellt werden.

Werden Dateien hochgeladen, muss die Grössenbegrenzung sowohl für die einzelne Datei als auch das Speicherlimit des gesamten Ablageordners berücksichtigt werden. Dieses Limit gilt auch wenn die Dateien per [WebDAV](../basic_concepts/Using_WebDAV.de.md) in den Ablageordner hochgeladen werden. Die maximale Dateigrösse zeigt der Dialog "Dateien hinzufügen", den Sie über das Dropdown-Menü neben "Dateien hochladen" öffnen. Den belegten Speicher des Ablageordners sehen Sie unter der Dateiliste.

![Maximale Dateigrösse für Upload unter der Auswahl der lokalen Datei](assets/storage_folder_upload_v1_de.png){ class="shadow lightbox" title="Dialog Dateien hinzufügen im Ablageordner" }

Ferner kann der Ablageordner sinnvollerweise mit weiteren Unterordnern versehen werden und so eine systematische Strukturierung von kursbezogenen Dateien umgesetzt werden.

## Speicherverbrauch [:octicons-tag-16:{ title="ab Release 18.0.2 (OO-6938)" }](https://track.frentix.com/issue/OO-6938){:target="_blank"} {: #storage_usage}

Wird ein Kurs gross oder geht ein Upload nicht mehr durch, zeigt die Auswertung Speicherverbrauch, welche Ordner und Kursbausteine wie viel Speicher belegen und wo eine Quota die Grenze setzt. Eine Quota ist das Speicherlimit eines Ordners. So sehen Sie, wo Sie aufräumen können und ob Sie mehr Platz anfordern müssen.

Die Auswertung unterscheidet die internen Ressourcen des Kurses, also seine Ordner und Kursbausteine, von den eingebundenen Lernressourcen wie einem Test oder einem Video. Die eingebundenen Lernressourcen nennt OpenOlat externe Ressourcen.

Sie öffnen die Auswertung im Bereich "Dateien" mit dem Button :o_icon_o_icon_hdd: "Speicherverbrauch anzeigen" oben rechts:<br>
`Kurs > Administration > Dateien > Speicherverbrauch anzeigen`

![Button Speicherverbrauch anzeigen oben rechts markiert, über den Ablageorten des Kurses](assets/course_admin_files_storage_usage_button_v1_de.png){ class="shadow lightbox" title="Bereich Dateien der Kurs-Administration" }

Die Seite "Speicherverbrauch Ressourcen" zeigt oben die Werte "Gesamtgrösse", "Interne Grösse" und "Anzahl Dateien" des Kurses, dazu ein Kreisdiagramm mit dem Anteil der Ressourcen mit und ohne Quota. Darunter listet eine Tabelle den Ablageordner und die Kursbausteine in der Struktur des Kurses. Über das Suchfeld finden Sie eine Zeile nach Name oder Typ, "Alle öffnen" und "Alle schliessen" klappen die Struktur auf und zu. Je Zeile stehen der Typ, die Anzahl Dateien, die Grösse, die Quota und in der Spalte "Aktuell verwendet" ein Balken, wie viel der Quota belegt ist. Ab 80 Prozent hebt OpenOlat den Balken farbig hervor. Mit "Anzeigen" öffnen Sie den Ordner oder den Kursbaustein der Zeile. Die Tabelle lässt sich als Excel-Datei exportieren.

![Filter Alle, Intern mit Quota und Intern ohne Quota markiert, darunter die Zeile Ablageordner mit Quota und Aktion Quota anpassen](assets/course_admin_storage_usage_v1_de.png){ class="shadow lightbox" title="Seite Speicherverbrauch Ressourcen eines Kurses" }

Drei Filter grenzen die Tabelle ein:

* "Alle": alle Ordner und Kursbausteine des Kurses, auch solche ohne Dateien.
* "Intern mit Quota": die Ordner mit eigener Quota. Das sind der Ablageordner, "Unterlagen Betreuer:innen" und "Dokumente (Toolbar)" sowie die Kursbausteine "Ordner" und "Teilnehmer:innen Ordner".
* "Intern ohne Quota": die Kursbausteine, die Speicher belegen, aber keine eigene Quota haben. Das sind "Forum", "Dateidiskussion", "Aufgabe", "Gruppenaufgabe", "Seite" und "Themenbörse".

Verwendet ein Kursbaustein "Ordner" als Ablageort einen Ordner aus dem Ablageordner, erscheint er nicht als eigene Zeile. Dasselbe gilt für "Unterlagen Betreuer:innen" und "Dokumente (Toolbar)", wenn sie einen Ordner aus dem Ablageordner nutzen. Die Dateien zählen dann zum Ablageordner und fallen unter dessen Quota. Beim Kursbaustein "Teilnehmer:innen Ordner" zeigt die Tabelle je Teilnehmer:in den Abgabeordner und den Rückgabeordner. Die Quota gilt für jeden dieser Ordner einzeln.

### Quota anpassen {: #storage_usage_edit_quota}

Die Aktion "Quota anpassen" steht nur in den Zeilen mit eigener Quota: beim Ablageordner, bei "Unterlagen Betreuer:innen" und "Dokumente (Toolbar)" sowie bei den Kursbausteinen "Ordner" und "Teilnehmer:innen Ordner". Die Kursbausteine "Forum", "Dateidiskussion", "Aufgabe", "Gruppenaufgabe", "Seite" und "Themenbörse" zählen ihren Verbrauch, haben aber keine Quota, die sich anpassen lässt.

Ändern können die Quota [Administrator:innen, Systemadministrator:innen und Lernressourcenverwalter:innen](../basic_concepts/Roles/index.de.md#org) der Organisation, der der Kurs angehört. Alle anderen sehen im Dialog "Quota anpassen" die aktuellen Werte, aber keinen Button zum Speichern. Brauchen Sie für einen Ordner mehr Platz, wenden Sie sich an eine dieser Personen.

Weitere Wege, den Speicherbedarf zu senken, beschreibt die Anleitung ["Mit welchen Massnahmen kann ich den Speicherverbrauch reduzieren?"](../../manual_how-to/reduce_storage_consumption/reduce_storage_consumption.de.md).

## Automatisch angelegte Ordner [:octicons-tag-16:{ title="ab Release 19.0 (OO-7700)" }](https://track.frentix.com/issue/OO-7700)

Welche Ordner OpenOlat für einen Kurs zusätzlich anlegt, sehen Sie unter `Kurs > Administration > Dateien`. Dort stehen sie je nach Kurskonfiguration neben dem Ablageordner:

* **_courseelementdata**: Wird angelegt, sobald der Kurs mindestens einen Kursbaustein "Ordner" enthält. In diesem Ordner befinden sich alle Kursbausteine "[Ordner](../learningresources/Course_Element_Folder.de.md)" und "[Teilnehmer:innen Ordner](../learningresources/Course_Element_Participant_Folder.de.md)" eines Kurses. Die entsprechenden Ordner mit den jeweiligen Dateien erscheinen hier automatisch, nachdem sie im Kurseditor angelegt wurden, und können hier auch editiert werden.
* **_sharedfolder**: Wird angelegt, wenn der Kurs mit einem [Ressourcenordner](../learningresources/Resource_Folder.de.md) verknüpft wird. Der zugewiesene Ressourcenordner kann hier eingesehen, standardmässig jedoch nicht editiert werden. Soll eine Bearbeitung hier möglich sein, deaktivieren Sie beim gewählten Ressourcenordner die Option "Schreibgeschützt": `Kurs > Administration > Einstellungen > Optionen`.
* **_documents**: Wird angelegt, wenn im Kurs das Werkzeug "[Dokumente](Course_Settings_Toolbar.de.md#documents)" aktiviert ist. Hier liegen die Dateien, die über das Werkzeug "Dokumente" zentral zum Download bereitstehen.
* **_coachdocuments**: Wird angelegt, wenn im Kurs der Ordner "Unterlagen Betreuer:innen" aktiviert ist. Hier liegen die Dateien, die nur Betreuer:innen und Kursbesitzer:innen sehen. [:octicons-tag-16:{ title="ab Release 16.0 (OO-5566)" }](https://track.frentix.com/issue/OO-5566)

## Verbindung von Ablageordner und dem Kursbaustein "HTML-Seite"

Einzelne webspezifische Seiten (z.B. HTML, PDF), die im Ablageordner abgelegt werden, können über den Kursbaustein "[HTML-Seite](Course_Element_HTML_Page.de.md)" im Kurs sichtbar gemacht werden. Zudem kann im Kursbaustein "HTML-Seite" die Checkbox "Link in gesamten Ablageordner erlauben" ausgewählt werden. Dadurch wird es möglich, Dateien, welche sich im Ablageordner befinden, direkt in dieser HTML-Datei zu verlinken. Das ist hilfreich für die Anzeige von verknüpften Grafiken einer HTML-Seite sowie sonstigen verknüpften Dateien.

Sobald diese Checkbox aktiviert ist, ist der Pfad für andere Dateien im Ablageordner ersichtlich. Es ist dadurch möglich, auch Dateien aufzurufen, welche sich zwar im Ablageordner befinden, jedoch nicht im Kurs selbst publiziert sind.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kursbausteine im Überblick >](Course_Elements/index.de.md)<br>
[Einsatz von WebDAV >](../basic_concepts/Using_WebDAV.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../basic_concepts/Roles/index.de.md)<br>
[Mit welchen Massnahmen kann ich den Speicherverbrauch reduzieren? >](../../manual_how-to/reduce_storage_consumption/reduce_storage_consumption.de.md)<br>
[Kursbaustein "Ordner" >](Course_Element_Folder.de.md)<br>
[Kursbaustein "Teilnehmer:innen Ordner" >](Course_Element_Participant_Folder.de.md)<br>
[Ressourcenordner >](Resource_Folder.de.md)<br>
[Toolbar >](Course_Settings_Toolbar.de.md)<br>
[Kursbaustein "HTML-Seite" >](Course_Element_HTML_Page.de.md)

**Weiterführend**<br>
[Ordnerkonzept >](../basic_concepts/Folder_Concept.de.md)<br>
[Persönliche Werkzeuge: File Hub >](../personal_menu/File_Hub.de.md)

[Zum Seitenanfang ^](#storage_folder)
