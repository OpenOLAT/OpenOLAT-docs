# Aufzeichnung der Kursaktivitäten {: #record_of_course_activities}

OpenOlat zeichnet Kursaktivitäten der Teilnehmenden und Kursautor:innen in Logfiles auf.

Innerhalb eines Kurses archivieren Sie die Logfiles im Werkzeug [Archivierung & Reports](../learningresources/Course_Archiving.de.md) [:octicons-tag-16:{ title="ab Release 21.0 (OO-9620)" }](https://track.frentix.com/issue/OO-9620) unter:<br>
`Kurs > Administration > Archivierung & Reports > Logfiles`

Zur Auswahl stehen:

* Admin-Logfile mit personalisierten Daten der Kursautor:innen
* Statistik-Logfile mit den anonymisierten Daten der Teilnehmenden
* Teilnehmer:innen-Logfile mit detaillierten, personalisierten Daten der Teilnehmenden

Logfiles archivieren können Besitzer:innen des Kurses sowie Lernressourcenverwalter:innen und Administrator:innen der Organisation, zu welcher der Kurs gehört. Besitzer:innen und Lernressourcenverwalter:innen wählen zwischen Admin-Logfile und Statistik-Logfile. Das Kursrecht "Datenarchivierung" öffnet das Werkzeug Archivierung & Reports, nicht aber die Logfiles. Wer nur über dieses Kursrecht verfügt, sieht unter Logfiles die Meldung "Sie sind nicht berechtigt, diese Logfiles zu archivieren."

Mit den Feldern "von" und "bis" begrenzen Sie die Logfiles auf einen Zeitraum, beide Felder sind optional. Der Zeitraum schliesst den Tag im Feld "bis" ein. Mit **Archivieren** erstellt OpenOlat die gewählten Logfiles und benachrichtigt Sie per E-Mail, sobald die ZIP-Datei bereitliegt. Das Bild zeigt die Auswahl, wie Besitzer:innen sie sehen.

![Auswahl aus Admin-Logfile und Statistik-Logfile, Statistik-Logfile angewählt, Zeitraum von und bis gesetzt](assets/course_archive_reports_logfiles_v2_de.png){ class="shadow lightbox" title="Logfiles im Werkzeug Archivierung & Reports · 2026.10.02" }

!!! info "Datenschutz"

    Aus Datenschutzgründen ist das Teilnehmer:innen-Logfile mit den personalisierten Daten der Teilnehmenden nur für Administrator:innen der Organisation verfügbar, zu welcher der Kurs gehört.

OpenOlat legt die gewählten Logfiles als ZIP-Datei (z.B. _CourseLogFiles_2010-01-28_14-55-55.zip_) in den [persönlichen Dateien](../personal_menu/File_Hub.de.md#personal_files) im Ordner `private/archive/"Kurstitel"` ab. Die ZIP-Datei enthält dann die ausgewählten Dateien _course_statistic_log.xlsx_, _course_admin_log.xlsx_ und _course_user_log.xlsx_.

Beachten Sie, dass in der Datei course_statistic_log.xlsx die Teilnehmenden folgendermassen anonymisiert sind:<br>
Jede:r Teilnehmer:in erhält eine anonyme Kennung aus 32 Zeichen (z.B. `e1c7eafdebc3c103fb8959e186326363`), die innerhalb eines Kurses gleich bleibt. Sie können so die Aktivitäten von Teilnehmer:in X im Kurs Y verfolgen, jedoch keine Vergleiche mit den Aktivitäten im Kurs Z machen, da Teilnehmer:in X im Kurs Z eine andere Kennung erhält.

Mögliche Einträge in den Logfile-Spalten **actionCrudType** (Datenbankoperation), **actionVerb** (Aktion) und **actionObject** (bearbeitetes Kursobjekt) (alphabetisch zusammengefasst):

actionCrudType| actionVerb| actionObject
---|---|---
c | add | calendar, chat, course, cpgetfile
r | copy | editor, efficency
u | denied | feed, feeditem, file, folder, forummessage, forumthread
d | do | glossary, gotonode, groupmanagement, group, grouparea, groupareaempty
e | edit | help
|  | exit | layout
|  | hide | node
|  | launch | owner
|  | lock | participant, publisher
|  | move | quota
|  | open | resource, rights, rightsempty
|  | remove | sharedfolder, spgetfile
|  | view | testattempts, testcomment, testid, testscore, testsuccess, tools, toolsempty
|  |  | waitingperson

In der Spalte **actionCrudType** werden die ausgeführten Aktionen in grundlegenden Datenbankoperationen zusammengefasst. Da diese in der Spalte actionVerb weiter aufgeschlüsselt werden, ist sie nicht weiter relevant.

Dennoch hier der Schlüssel:

* C=Create (erstellen)
* R=Read / Retrieve (lesen/holen)
* U= Update / Modify (Verändern)
* D=Delete (entfernen)
* E=Exit (beenden)

In der Spalte **actionVerb** wird nun genauer betrachtet, welche Aktion die Benutzer:innen unter „userName“ mit dem Kursobjekt aus Spalte actionObject vorgenommen haben. Der Eintrag in der Spalte **actionObject** ist also das Objekt das "verändert" wurde, zumindest aus Datenbanksicht.

![Beispieleinträge des Statistik-Logfiles mit den Spalten creationDate, userName, actionCrudType, actionVerb und actionObject](assets/course_statistic_log.gif){ class="shadow lightbox" title="Statistik-Logfile course_statistic_log.xlsx" }

Die dritte Zeile

`u / add / participant / [Gruppenname] / [Benutzername]`

wird folgendermassen gelesen (Datenbankoperation: update / modify):

`Füge Benutzer [Benutzername] zu [Gruppe] hinzu`

## Weiterführende Informationen {: #further_information}

[Kursadministration - Archivierung & Reports >](../learningresources/Course_Archiving.de.md)<br>
[Persönliche Werkzeuge: File Hub >](../personal_menu/File_Hub.de.md)<br>
[Mitgliederverwaltung >](../learningresources/Members_management.de.md)

[Zum Seitenanfang ^](#record_of_course_activities)

