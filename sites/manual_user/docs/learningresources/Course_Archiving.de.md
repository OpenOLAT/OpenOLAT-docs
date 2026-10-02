# Kursadministration - Archivierung & Reports {: #course_archiving}

[:octicons-tag-16:{ title="ab Release 19.0 (OO-7504)" }](https://track.frentix.com/issue/OO-7504){:target="_blank"}

## Was ist das Kursarchiv?

**Wozu ein Kursarchiv?**<br>
Müssen z.B. die Ergebnisse von Teilnehmer:innen aus rechtlichen Gründen 10 Jahre aufbewahrt werden, kann der Kurs selbst gelöscht werden, während die Teilnehmerdaten separat in einem Kursarchiv aufbewahrt werden.

**Was enthält eine Archivdatei?**<br>
Sowohl in der Kursadministration als auch im Autorenbereich können Kursarchiv-Dateien (**ZIP-Dateien**) erstellt werden, in denen v.a. **Excel-Dateien** enthalten sind, bzw. für Textformate rtf Dateien. Darin sind alle in einem Kurs erbrachten Ergebnisse der Kursteilnehmer:innen tabellarisch aufgelistet. Gehören zur Archivierung noch weitere Dateien, werden diese in Unterordnern innerhalb der ZIP-Datei bereitgestellt.

**Gesamtarchiv - Teilarchiv**<br>
Auf Wunsch können auch Teilarchive erstellt werden, wenn z.B. nur die Ergebnisse eines bestimmten Kursbausteins archiviert werden sollen. (Z.B. der Abschlusstest und Übungstests sollen nicht im Archiv enthalten sein.)

Ein solches Kursarchiv ist zu unterscheiden von der Option ["Inhalt exportieren"](../learningresources/Export_Content.de.md) in der Kursadministration.

| `Kurs > Administration > Inhalt exportieren` | `Kurs > Administration > Archivierung & Reports > Kursarchivierung` | `Kurs > Administration > Archivierung & Reports > Reports` |
| ------------------------------------- | ------------------------------------- | -------------------------------------|
| Kursstruktur und Kursinhalte archivieren | Ergebnisse der Teilnehmer:innen archivieren   | Bericht mit statistischer Analyse zu einem bestimmten Kursbaustein |
| leerer Kurs ohne Teilnehmerdaten      | reine Teilnehmerdaten zur Dokumentation (Nachweis)| Report-Excel enthält mehr als die Teilnehmerdaten in den Excel des Kursarchivs |
| zur Übertragung in ein anderes LMS        | nicht wieder importierbar     | Report für gewisse Bausteine, wie z.B. Forum |
| v.a. html und xml-Dateien                | v.a. Excel-Dateien                         |kursbausteinspezifische Excel-Dateien |

Löschen Sie einen Kurs, werden automatisch alle Kursdaten (nicht die Kursbausteine) in Ihren [persönlichen Dateien](../personal_menu/File_Hub.de.md) gespeichert. Über die Rechtevergabe in der [Mitgliederverwaltung](Members_management.de.md) kann auch weiteren Personen das Recht für die gesamte Datenarchivierung gegeben werden.

## Wo finde ich Kursarchiv-Dateien?

In der obersten Button-Zeile des Autorenbereichs finden Sie ganz rechts ein Icon mit 3 Punkten. Darunter finden Sie das Kursarchiv, in dem alle vorhandenen Kursarchiv-Dateien aufgelistet sind und heruntergeladen werden können.

![Geöffnetes 3-Punkte-Menü ganz rechts in der obersten Buttonzeile mit dem Eintrag Kursarchiv](assets/course_archiving_open_v1_de.png){ class="shadow lightbox" title="Oberste Buttonzeile im Autorenbereich" }

!!! info "Wichtig"

    Im Kursarchiv werden alle von Ihnen erstellten Archive aufgelistet. <br>Administrator:innen und Lernressourcenverwalter:innen sehen im Tab "Kursarchive" auch nur die von ihnen selbst erstellten Archive oder Kurse, in denen sie Besitzer:in sind. <br>Im Tab **Kursarchivmanagement** werden Administrator:innen und Lernressourcenverwalter:innen dagegen die Archive aller Autor:innen aufgelistet.

![Tabs Kursarchive und Kursarchivmanagement über der Liste der erstellten ZIP-Dateien mit Info, Löschen und Herunterladen](assets/course_archiving_all_v1_de.png){ class="shadow lightbox" title="Seite Kursarchiv im Autorenbereich" }



## Kursarchive erstellen

### Einen einzelnen Kurs archivieren

* Öffnen Sie den Autorenbereich.
* Wählen Sie den gewünschten Kurs.
* Klicken Sie unter "**Administration**" auf die Option "**Archivierung & Reports**".
* Wählen Sie anschliessend im Bereich "Kursarchivierung" einen der Buttons "**Archiv erstellen**".

![Geöffnetes Menü Administration, markiert ist der Eintrag für Archivierung und Reports](assets/course_archiving_create_single_v1_de.png){ class="shadow lightbox" title="Menü Administration eines Kurses" }

![Menüeintrag Kursarchivierung links, rechts die Buttons Archiv erstellen über und in der leeren Archivliste](assets/course_archiving_create_single2_v1_de.png){ class="shadow lightbox" title="Kursarchivierung unter Archivierung & Reports" }


### Ein Teilarchiv erstellen

Sobald Sie **via Kursadministration** ein Archiv erstellen möchten, werden Sie als Erstes gefragt, ob es ein Gesamt- oder Teilarchiv sein soll.

![Wizard-Schritt Archivart mit der Wahl zwischen Gesamtarchiv und Teilarchiv, danach folgen Einstellungen und Übersicht](assets/course_archiving_create_partial_v1_de.png){ class="shadow lightbox" title="Dialog Kurs archivieren" }

!!! tip "Tipp"

    Erstellen Administrator:innen oder Lernressourcenverwalter:innen ein Gesamtarchiv, können sie im Wizard-Schritt "Einstellungen" bei "Log-Dateien Teilnehmer:innen" entscheiden, ob die Teilnehmenden in den Logfiles **anonymisiert oder personalisiert** erscheinen. (Je nach Anforderungen des Datenschutzes.) Archive mit personalisierten Logfiles sind anschliessend nur für administrative Rollen zugänglich.

### Gesamtarchive mehrerer Kurse im Autorenbereich erstellen

* Öffnen Sie den Autorenbereich.
* Markieren Sie alle für die Archivierung gewünschten Kurse in der 1. Spalte.
* Sobald mindestens ein Kurs selektiert ist, erscheint über der Liste eine Buttonzeile.
* Wählen Sie den Button "Kurs archivieren".

![Zwei markierte Kurse in der ersten Spalte, darüber die eingeblendete Buttonzeile mit Kurs archivieren](assets/course_archiving_create_multiple_v1_de.png){ class="shadow lightbox" title="Kursliste im Autorenbereich" }

!!! info "Wichtig"

    Werden mehrere Archive mit dieser Bulk Action erstellt, können nur Gesamtarchive erstellt werden, keine Teilarchive.


## Kursarchivmanagement

!!! info "Wichtig"

    Dieser Tab ist nur für OpenOlat Administrator:innen und Lernressourcenverwalter:innen verfügbar, nicht für Autor:innen.

Im Tab **Kursarchivmanagement** sind alle Kursarchive aufgelistet.

* Sie können durch weitere Tabs vorselektiert werden: "Alle", "Gesamtarchive", "Teilarchive", "Laufende Archivierungen" und "Nur für administrative Rollen".
* Unter dem Icon mit den 3 Punkten am Ende einer Zeile befindet sich auch die Option zum Herunterladen. Die Kursarchive können hier eine bestimmte Zeit lang heruntergeladen werden (Voreinstellung 10 Tage).

![Archive aller Autor:innen mit Filtertabs und dem 3-Punkte-Menü einer Zeile mit Metadaten anzeigen, Herunterladen und Löschen](assets/course_archiving_management_v1_de.png){ class="shadow lightbox" title="Tab Kursarchivmanagement auf der Seite Kursarchiv" }


## Was wird von den einzelnen Elementen archiviert?

### Umfragen

Es werden alle [Umfragen](../learningresources/Course_Element_Survey.de.md) des Kurses entsprechend ihrer Einbindung in der Kursstruktur angezeigt. Die gewünschten zu archivierenden Umfragen können ausgewählt und als ZIP-Datei gespeichert werden.

### Fragebogen

Speicherung der *alten* OpenOlat Fragebögen. In der Regel nicht mehr relevant, da die Fragebögen durch Formulare im Kursbaustein Umfrage ersetzt wurden.

### Tests

Es werden alle [Tests](../learningresources/Course_Element_Test.de.md) des Kurses angezeigt. Die gewünschten zu archivierenden Elemente können ausgewählt und als ZIP-Datei gespeichert werden. In der ZIP-Datei liegen dann die einzelnen ausgewählten Tests in jeweils einem extra Ordner.

Archivierte Tests werden personalisiert gespeichert und enthalten alle Testergebnisse.

Testergebnisse als PDF-Dateien enthält das Archiv, wenn Sie im Wizard-Schritt "Einstellungen" bei "Kursbausteine" die Option "Benutzerspezifisch" und beim Kursbaustein Test die Option "Erweitert – mit PDF" wählen. Die Auswahl erscheint nur, wenn in der System-Administration unter `Administration > Externe Werkzeuge > PDF Generator` der [PDF-Dienst](../../manual_admin/administration/External_Tools_-_Administration.de.md#pdf_generator) eingeschaltet ist. Die Option "Alle PDF-Dateien in einem Ordner" bietet nur der Export im Kursbaustein Test über den Button "Resultate exportieren". Mehr dazu unter [Testergebnisse archivieren](../learningresources/Course_Element_Test.de.md#archive) und [Tests exportieren](../learningresources/Test_export.de.md#pdf_files). [:octicons-tag-16:{ title="ab Release 21.1 (OO-9600)" }](https://track.frentix.com/issue/OO-9600)

![Button Resultate exportieren über der Liste der Teilnehmenden markiert](assets/test_export_results1_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen im Kursbaustein Test" }

### Kursresultate

Hier werden die *Endresultate* von allen im Kurs integrierten Assessment Bausteinen wie [Tests](../learningresources/Course_Element_Test.de.md), [Bewertungen](../learningresources/Course_Element_Assessment.de.md), [Portfolioaufgaben](../learningresources/Course_Element_Portfolio_Task.de.md), [Checklisten](../learningresources/Course_Element_Checklist.de.md), [Aufgaben](../learningresources/Course_Element_Task.de.md) usw. von allen Teilnehmenden gebündelt als ZIP-Datei archiviert. Die ZIP-Datei kann direkt heruntergeladen und gespeichert werden, liegt aber auch noch im privaten Ordner der Kursbesitzer:innen in OpenOlat.

In der ZIP-Datei findet man eine xlsx-Datei mit Informationen zu den Teilnehmenden sowie eventuell von den Teilnehmenden abgegebene Dokumente. Diese Dokumente werden pro Kursbaustein gebündelt und enthalten Unterordner mit den Namen der Teilnehmenden, die Dokumente eingereicht haben.

Kursresultate beinhalten die zusammengefasste Gesamtauswertung eines Kurses, _nicht_ einzelne Elemente.

### Aufgabe und Gruppenaufgaben [:octicons-tag-16:{ title="ab Release 14.0 (OO-3945)" }](https://track.frentix.com/issue/OO-3945)

Es werden alle [Aufgaben](../learningresources/Course_Element_Task.de.md) und [Gruppenaufgaben](../learningresources/Course_Element_Grouptask.de.md) des Kurses angezeigt. Die gewünschten zu archivierenden Aufgaben bzw. Gruppenaufgaben können ausgewählt und als ZIP-Datei gespeichert werden.

In der ZIP-Datei liegen dann die einzelnen ausgewählten Aufgaben/Gruppenaufgaben in jeweils einem extra Ordner. In diesem befinden sich dann die Ergebnisse der einzelnen Lernenden sowie der Gesamtüberblick als Excel-Datei.

### Themenvergabe

Es werden alle [Themenvergaben](../learningresources/Course_Element_Topic_Assignment.de.md) des Kurses angezeigt. Die gewünschten zu archivierenden Elemente können ausgewählt und als ZIP-Datei gespeichert werden. In der ZIP-Datei liegen dann die einzelnen ausgewählten Elemente in jeweils einem extra Ordner.

### Logfiles

Hier können die personalisierten Logfiles der Kursbesitzer:innen sowie die anonymisierten Logfiles der Teilnehmenden für einen gewählten Zeitraum gesichert werden. Je nach Umfang kann die Erstellung einige Zeit in Anspruch nehmen. Anschliessend findet man die Logfiles im persönlichen, privaten OpenOlat Ordner als ZIP-Datei mit Excel-Tabelle.

### Foren

Es werden alle [Foren](../learningresources/Course_Element_Forum.de.md) des Kurses angezeigt. Die gewünschten zu archivierenden Foren können ausgewählt und als ZIP-Datei gespeichert werden. In der ZIP-Datei liegen dann die einzelnen ausgewählten Foren in jeweils einem extra Ordner mit einer DOCX-Datei, die sämtliche Forenbeiträge umfasst.

Neben der Archivierung kann auch ein Bericht im xlsx-Format zu den gewünschten Foren generiert werden. Jedes Posting wird im Bericht als ein Zeileneintrag vermerkt und enthält Informationen zum Erstellungsdatum, letzte Änderung, Anzahl der Wörter, Zeichenzahl usw. [:octicons-tag-16:{ title="ab Release 18.0 (OO-6908)" }](https://track.frentix.com/issue/OO-6908){:target="_blank"}

### Dateidiskussion

Es werden alle [Dateidiskussionen](../learningresources/Course_Element_File_Dialog.de.md) des Kurses angezeigt. Die gewünschten zu archivierenden Elemente können ausgewählt und als ZIP-Datei gespeichert werden.

### Teilnehmer Ordner [:octicons-tag-16:{ title="ab Release 11.3 (OO-2455)" }](https://track.frentix.com/issue/OO-2455)

Es werden alle ["Teilnehmer Ordner"](../learningresources/Course_Element_Participant_Folder.de.md) Kursbausteine angezeigt. Die gewünschten zu archivierenden Elemente können ausgewählt und als ZIP-Datei gespeichert werden. In der ZIP-Datei befinden sich dann die einzelnen Elemente mit jeweils einem Ordner pro Teilnehmer mit je einem Abgabe- und Rückgabeordner.

### Wikis

Es werden alle [Wikis](../learningresources/Course_Element_Wiki.de.md) des Kurses aufgelistet. Die gewünschten zu archivierenden Wikis können ausgewählt und als ZIP-Datei gespeichert werden. In der ZIP-Datei befinden sich dann jeweils ein Ordner pro Wiki sowie einem Ordner mit Metadaten für jedes gespeicherte Wikis.

Beim Wiki werden alle Seiten und alle hochgeladenen Dateien in eine ZIP-Datei verpackt. Der Teilnehmer Ordner wird entsprechend der Ordner Struktur dieses Bausteins gespeichert.

### SCORM Resultate

Es werden alle [SCORM](../learningresources/Course_Element_SCORM_Learning_Content.de.md) Kursbausteine des Kurses aufgelistet. Die gewünschten zu archivierenden SCORM Kursbausteine können ausgewählt und die Ergebnisse als ZIP-Datei gespeichert werden.

### Checklisten

Es werden alle [Checklisten](../learningresources/Course_Element_Checklist.de.md) des Kurses aufgelistet. Die gewünschten zu archivierenden Checklisten können ausgewählt und als ZIP-Datei gespeichert werden. Die ZIP-Datei enthält einen Ordner für jede Checkliste. Darin befindet sich jeweils eine xlsx-Datei, die die Ergebnisse der Personen, die die Checklisten ausgefüllt haben enthält.

### Formulare

Es werden alle Kursbaustein [Formulare](../learningresources/Course_Element_Form.de.md) des Kurses aufgelistet. Die gewünschten Formulare können ausgewählt und als ZIP-Datei gespeichert werden. Die ZIP-Datei enthält einen Ordner für jedes Formular. Darin befindet sich jeweils eine xlsx-Datei, die die Formular Antworten der Personen, die die das Formular ausgefüllt haben, enthält.

### Videoaufgabe
Es werden alle im Kurs eingebauten Kursbausteine [Video-Aufgabe](../learningresources/Course_Element_Video_Task.de.md) unabhängig vom gewählten Modus aufgelistet. Die gewünschten Bausteine können ausgewählt und die Ergebnisse als ZIP-Datei gespeichert werden. Die ZIP-Datei enthält eine xlsx-Datei mit den Ergebnissen der einzelnen Teilnehmenden.


### Chat Historie

Hier kann der Chatverlauf als xlsx-Datei exportiert und auch gelöscht werden.

### Buchungsaufträge

Hier werden die Personen, die den Kurs gebucht haben angezeigt, sofern der Kurs über [Angebote](../learningresources/Access_configuration.de.md) verfügt.

[Zum Seitenanfang ^](#course_archiving)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Inhalt exportieren >](../learningresources/Export_Content.de.md)<br>
[Persönliche Werkzeuge: File Hub >](../personal_menu/File_Hub.de.md)<br>
[Mitgliederverwaltung >](Members_management.de.md)<br>
[Kursbaustein "Umfrage" >](../learningresources/Course_Element_Survey.de.md)<br>
[Kursbaustein "Test" >](../learningresources/Course_Element_Test.de.md)<br>
[Externe Werkzeuge: Übersicht >](../../manual_admin/administration/External_Tools_-_Administration.de.md)<br>
[Tests exportieren >](../learningresources/Test_export.de.md)<br>
[Kursbaustein "Bewertung" >](../learningresources/Course_Element_Assessment.de.md)<br>
[Kursbaustein "Portfolioaufgabe" >](../learningresources/Course_Element_Portfolio_Task.de.md)<br>
[Kursbaustein "Checkliste" >](../learningresources/Course_Element_Checklist.de.md)<br>
[Kursbaustein "Aufgabe" >](../learningresources/Course_Element_Task.de.md)<br>
[Kursbaustein "Gruppenaufgabe" >](../learningresources/Course_Element_Grouptask.de.md)<br>
[Kursbaustein "Themenvergabe" >](../learningresources/Course_Element_Topic_Assignment.de.md)<br>
[Kursbaustein "Forum" >](../learningresources/Course_Element_Forum.de.md)<br>
[Kursbaustein "Dateidiskussion" >](../learningresources/Course_Element_File_Dialog.de.md)<br>
[Kursbaustein "Teilnehmer:innen Ordner" >](../learningresources/Course_Element_Participant_Folder.de.md)<br>
[Kursbaustein "Wiki" >](../learningresources/Course_Element_Wiki.de.md)<br>
[Kursbaustein "SCORM 1.2" >](../learningresources/Course_Element_SCORM_Learning_Content.de.md)<br>
[Kursbaustein "Formular" >](../learningresources/Course_Element_Form.de.md)<br>
[Kursbaustein "Videoaufgabe" >](../learningresources/Course_Element_Video_Task.de.md)<br>
[Zugangskonfiguration / Freigabe >](../learningresources/Access_configuration.de.md)

**Weiterführend**<br>
[Aufzeichnung der Kursaktivitäten >](Record_of_Course_Activities.de.md)<br>
[Löschen (eines Kurses/einer Lernressource) >](Course_Delete.de.md)<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview.de.md)

[Zum Seitenanfang ^](#course_archiving)
