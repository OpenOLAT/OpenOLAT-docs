# Kursbaustein "Gruppenaufgabe" {: #course_element_group_tasks}


## Steckbrief

Name | Gruppenaufgabe
---------|----------
Icon | :o_icon_o_gta_icon:
Verfügbar seit | Release 10.3 (OO-991)
Funktionsgruppe | Wissensüberprüfung
Verwendungszweck | Abbildung komplexer Aufgabenworkflows mit konfigurierbaren Teilschritten wie Abgabe von Lösungsdokumenten, Feedback und Überarbeitungsschlaufe, Bereitstellung der Musterlösung und Bewertung
Bewertbar | ja
Spezialität / Hinweis | dem Kursbaustein Aufgabe ähnlich



Mit dem Kursbaustein Gruppenaufgabe bearbeitet eine Gruppe eine Aufgabe gemeinsam und gibt gemeinsam ab. Der Kursbaustein funktioniert grösstenteils wie der Kursbaustein ["Aufgabe"](Course_Element_Task/index.de.md), die Details stehen dort. Die folgenden Abschnitte beschreiben, was bei der Gruppenaufgabe anders ist.

## Tab Workflow {: #workflow}
Im Tab "Workflow" legen Sie fest, wer die Gruppenaufgabe bearbeitet: Mit "Gruppe auswählen" wählen Sie eine oder mehrere Gruppen aus, mit "Lernbereich auswählen" einen oder mehrere Lernbereiche. Nur diese Gruppen sehen und bearbeiten die Aufgabe. Solange keine Gruppe gewählt ist, meldet der Kurseditor "Sie haben noch keine Gruppe gewählt", und der Kursbaustein ist bei geschlossenem Editor nicht sichtbar.

!!! info "Wichtig"

    Bei der Gruppenaufgabe fehlt im Tab "Workflow" im Bereich "Betreuung" die Option "Zuweisung Betreuende/Teilnehmende". Betreuer:innen einer Gruppe betreuen automatisch deren Gruppenaufgabe, Kursbesitzer:innen sehen alle Gruppen der Gruppenaufgabe.

Entfernen Sie einen Bestandteil des Workflows, zum Beispiel die Aufgabenstellung, fehlt er bei allen Gruppen des Kurses. Bereits gewählte Aufgaben sind dann nicht mehr sichtbar. Fügen Sie den Bestandteil wieder ein, sind sie wieder zugänglich. Fügen Sie die Aufgabenstellung erst nachträglich hinzu, muss eine Gruppe, die im Workflow schon weiter ist, keine Aufgabe mehr wählen.

Nachträgliche Änderungen am Workflow wirken sich auf alle Gruppen aus, auch wenn diese den Workflow bereits begonnen haben.

## Tab Aufgabenstellung {: #tab_task}
Bei der Gruppenaufgabe wählt jede Gruppe _eine_ Aufgabe. Sobald ein Gruppenmitglied im Schritt "Zuweisung Aufgabenstellung" eine Aufgabe gewählt hat, gilt sie für die ganze Gruppe, unabhängig davon, wer aus der Gruppe gewählt hat.

## Tab Abgabe {: #tab_submission}

Ist die Option "E-Mail Bestätigung" aktiviert, erhalten alle Teilnehmenden der Gruppe eine Bestätigung per E-Mail, unabhängig davon, wer die Dateien erstellt, hochgeladen oder abgegeben hat.

## Tab Bewertung {: #tab_assessment}
Sind für die Gruppenaufgabe bereits Bewertungen vorhanden, zeigt OpenOlat im Tab "Bewertung" die Einstellungen unter "Konfiguration Bewertung" schreibgeschützt an. Bearbeitbar bleibt der Bereich "Bewertungsformular". Mit "Bearbeitungsmodus aktivieren" machen Sie die Einstellungen wieder bearbeitbar, siehe [Schreibschutz der Bewertungskonfiguration](Course_Elements/index.de.md#assessment_config_read_only). [:octicons-tag-16:{ title="ab Release 21.1 (OO-9647)" }](https://track.frentix.com/issue/OO-9647)

Punkte und Feedback gelten für die ganze Gruppe und lassen sich für einzelne Gruppenmitglieder anpassen.

Bei geschlossenem Editor zeigt der Kursbaustein unter "Teilnehmer:innen" die zugeordneten _Gruppen_, die Sie auswählen und bewerten. Beim Bewerten legen Sie mit der Option "Für die ganze Gruppe" fest, ob die Bewertung für alle Gruppenmitglieder gilt oder nur für ein einzelnes Mitglied.

Die Liste zeigt je Gruppe die Spalten "Schritt" und "Abgabedatum". Nach Zeilenauswahl stehen je nach Konfiguration "Verlängern", "Resultate exportieren" und "E-Mail" bereit. Was die Spalten zeigen und wie Sie Zuweisung und Abgabe kontrollieren, beschreibt die Seite [Aufgabe betreuen](Course_Element_Task/Task_Coaching.de.md#coach_overview). Den Tab "Workflow" bei geschlossenem Editor gibt es nur beim Kursbaustein "Aufgabe".

### Spalte "Gruppe" im Resultat-Export [:octicons-tag-16:{ title="ab Release 21.0.2 (OO-9601)" }](https://track.frentix.com/issue/OO-9601) {: #results_export}

Der Excel-Report aus "Resultate exportieren" führt bei der Gruppenaufgabe zusätzlich die Spalte "Gruppe" mit dem Namen der Gruppe, welche die Lösung abgegeben hat. Damit bleibt im Report nachvollziehbar, welche Abgabe zu welcher Gruppe gehört. Die übrigen Spalten sind unter [Excel-Report der Resultate](Assessing_tasks_and_group_tasks.de.md#results_export) beschrieben.

## Tab Erinnerungen & To-dos {: #tab_reminders_todo}
Bei der Gruppenaufgabe erstellt OpenOlat keine To-dos, auch wenn sich die Option in diesem Tab aktivieren lässt.

## Gruppenaufgabe aus Sicht der Teilnehmenden {: #group_task_user_perspective}

Alle Entscheidungen und Abgaben im Workflow gelten für die ganze Gruppe. Stimmen Sie sich deshalb in der Gruppe ab, _bevor_ jemand endgültig abgibt, und achten Sie gemeinsam auf die Fristen.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kursbaustein "Aufgabe" >](Course_Element_Task/index.de.md)<br>
[Kursbausteine im Überblick >](Course_Elements/index.de.md)<br>
[Aufgabe betreuen >](Course_Element_Task/Task_Coaching.de.md)<br>
[Aufgaben und Gruppenaufgaben bewerten >](Assessing_tasks_and_group_tasks.de.md)

**Weiterführend**<br>
[Gruppen erstellen >](../groups/Create_Groups.de.md)<br>
[Gruppenadministration >](../groups/Group_Administration/index.de.md)

[Zum Seitenanfang ^](#course_element_group_tasks)
