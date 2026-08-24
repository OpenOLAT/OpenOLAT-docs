# Aufgaben und Gruppenaufgaben bewerten

Hier erfahren Sie wie man Bewertungen für Aufgaben und Gruppenaufgaben mit Hilfe des OpenOlat "Bewertungswerkzeugs" vornimmt.

Gehen Sie in das Bewertungswerkzeug und wählen Sie in der linken Übersicht den Assessmentbaustein aus, den Sie bewerten möchten. Hier finden Sie zwei Tabs: Übersicht und Teilnehmer:innen.

Im Tab Übersicht erhalten Sie eine Übersicht zur Bewertung dieses Kursbausteins, z.B. wie viele Personen diesen Kursbaustein schon bestanden haben. 
Im Tab Teilnehmer:innen werden die Teilnehmenden angezeigt und die eigentliche Bewertung von Teilnehmenden kann gestartet werden.

## Tab Teilnehmer:innen

**Generelle Aktionsmöglichkeiten**

![Über der Teilnehmerliste stehen die Aktionen "Neue Massenbewertung starten", "Resultate exportieren", "Daten exportieren" und "Statistik"; die Liste führt je Person Betreuer:in, Versuche, Bestanden, Aufgabe, Status und letzte Aktualisierung: Tab Teilnehmer:innen des Bewertungswerkzeugs](assets/assessment_tool_task_participants_de.png){ class="shadow lightbox" }

Kursbetreuer und Kursbesitzer haben über die entsprechenden Buttons verschiedene Aktionsmöglichkeiten: 

* Über "Resultate exportieren" die abgegebenen Dokumente aller oder ausgewählter Teilnehmenden samt einem Excel-Report herunterladen
* Über "Daten exportieren" die Bewertungsdaten der Teilnehmenden ausgeben.
* Über "Statistik" die Auswertung des Kursbausteins öffnen.
* Eine neue Massenbewertung starten und damit alle Teilnehmenden auf einmal zu bewerten.
* Die Aufgabe für alle oder mehrere ausgewählte Teilnehmenden auf den Status "abgeschlossen" zu setzen und damit die Bewertung final zu beenden. 
* Die Bewertungen der Aufgabe für alle oder mehrere ausgewählte Teilnehmenden auf einen Schlag sichtbar bzw. unsichtbar zu setzen, also freizugeben oder die Freigabe zurückzuziehen.
* Eine E-Mail an alle oder bestimmte Teilnehmende verschicken.
* Die Abgabe für bestimmte oder alle Personen zu verlängern.

Direkt auswählbar sind die Optionen "Resultate exportieren" sowie eine Massenbewertung vorzunehmen. Wie man eine Massenbewertung für Aufgaben genau erstellt erfahren Sie hier im Bereich [How to](../../manual_how-to/bulk_assessment/bulk_assessment.de.md).
Für weitere Aktionen, die sich nur auf bestimmte Teilnehmende beziehen müssen die gewünschten Teilnehmenden zunächst ausgewählt werden bevor die Optionen angezeigt werden.

![Nach Auswahl einer Zeile erscheint über der Liste eine Leiste mit sechs Aktionen für die ausgewählten Personen: "Bewertung abschliessen", "Freigeben", "Freigabe zurückziehen", "Verlängern", "Resultate exportieren" und "E-Mail": Tab Teilnehmer:innen des Bewertungswerkzeugs](assets/assessment_tool_task_bulk_actions_de.png){ class="shadow lightbox" }

## Einreichung ansehen

Bevor eine Aufgabe bewertet werden kann müssen sich die Betreuer oder Kursbesitzer die Einreichungen bzw. abgegebenen Dokumente ansehen. Dies kann entweder einzeln für jeden Teilnehmer bzw. Teilnehmerin oder in Form der Massenbewertung bzw. dem Herunterladen der abgegebenen Dokumente von mehreren Personen erfolgen. 

### Einreichungen einzelner User

Sobald von einem Lernenden eine Datei über den Button "endgültige Abgabe" eingereicht wurde, kann sie vom Lehrenden geöffnet und angeschaut werden.

Um sich die Einreichung _einer einzelnen Person_ anzeigen zu lassen wählen Sie diese Person aus und klicken Sie auf die abgegebene Datei. 

![Der Schritt Abgabe ist mit "Abgeschlossen" markiert und listet die abgegebene Datei mit Abgabedatum, den Aktionen "Öffnen" und "Laden" sowie dem Button "Abgegebene Dokumente": Bewertungsflow einer einzelnen Person im Bewertungswerkzeug](assets/Aufgabe_abgegeben.png){ class="shadow lightbox" }

Wie Sie die Assessmentbausteine einzelner Personen generell bewerten erfahren Sie  in einer [Schritt für Schritt Anleitung](Assessment_of_learners.de.md).

### Einreichungen aller oder mehrerer User

Wenn viele Lösungsversuche hochgeladen wurden, oder Sie viele Lernende bewerten müssen, empfiehlt es sich, über die Schaltfläche "Resultate exportieren" alle Lösungsversuche auf einmal herunterzuladen. Im heruntergeladenen Ordner finden Sie ebenfalls alle Aufgabenzuweisungen. 

Alternativ können Sie die gewünschten Personen auswählen und dann die Option "Resultate exportieren" wählen. 

Anschliessend können Sie das [Bewertungsformular](The_assessment_form.de.md) ausfüllen. Es erscheint bei der Bewertung eines Kursbausteins unter "Bewertung".


### Excel-Report der Resultate [:octicons-tag-16:{ title="ab Release 21.0.2 (OO-9601)" }](https://track.frentix.com/issue/OO-9601) {: #results_export}

Die ZIP-Datei aus "Resultate exportieren" enthält neben den abgegebenen Dokumenten einen Excel-Report. Er führt pro Person eine Zeile und hält fest, wer welchen Schritt wann abgeschlossen hat. Kursverantwortliche lesen daraus zum Beispiel ab, welche Betreuerin oder welcher Betreuer eine Bewertung abgeschlossen hat, und stützen darauf die Vergütung der Bewertungsarbeit.

Neben Laufnummer, Kurspfad, erstem Zugriff und den Personendaten enthält der Report diese Spalten:

Spalte | Inhalt | Erscheint
---------|----------|----------
Gruppe | Name der Gruppe, welche die Lösung abgegeben hat | nur beim Kursbaustein Gruppenaufgabe
Aufgabe | Titel der zugewiesenen Aufgabenstellung | wenn der Schritt Aufgabenstellung aktiviert ist
Schritt | Schritt des Workflows, in dem die Person aktuell steht | immer
Zuweisung abgeschlossen | Datum, an dem die Aufgabe zugewiesen wurde | wenn der Schritt Aufgabenstellung aktiviert ist
Abgabe abgeschlossen | Datum der endgültigen Abgabe | immer
Feedback abgeschlossen | Datum, an dem Rückgabe und Feedback abgeschlossen wurden | wenn der Schritt Feedback aktiviert ist
Überarbeitung abgeschlossen | Datum, an dem die Überarbeitung abgeschlossen wurde | wenn der Schritt Überarbeitung aktiviert ist
Bewertung abgeschlossen | Datum, an dem die Bewertung abgeschlossen wurde | wenn der Schritt Bewertung aktiviert ist
Bemerkungen | Bemerkungen zur Abgabe | immer
Betreuer | Die der Person zugewiesene betreuende Person | wenn die Zuweisung Betreuende/Teilnehmende aktiviert ist

Die Spalte "Betreuer" steht hinter den Bewertungsspalten (Punkte, Bestanden, Versuche, letzte Änderung).

Ein Schritt, der im Kursbaustein nicht aktiviert ist, erzeugt keine Spalte. Fehlt also zum Beispiel die Spalte "Feedback abgeschlossen", ist der Schritt Feedback in diesem Kursbaustein nicht aktiv. Welche Schritte aktiv sind, legen Kursbesitzer:innen im Kurseditor fest: `Kurs > Kurseditor > "Aufgabenbaustein" > Tab "Workflow"`.

Denselben Excel-Report erzeugt die Kursarchivierung, sofern im Kursbaustein der Schritt Bewertung aktiviert ist.


## Bewertungsmöglichkeiten Kursbaustein "Aufgabe"

Welche Schritte im Bewertungsflow genau zur Verfügung stehen, ist abhängig von der konkreten Konfiguration des Aufgaben Bausteins. Die Details werden in der Konfiguration des Kursbausteins ["Aufgabe"](../learningresources/Course_Element_Task.de.md) bzw. ["Gruppenaufgabe"](../learningresources/Course_Element_Grouptask.de.md) festgelegt. Im Bewertungswerkzeug können die Bewertungsoptionen nicht mehr geändert werden.

Falls gewünscht und entsprechend konfiguriert, kann ein Rückgabe-Dokument hochgeladen werden. Dabei könnte es sich zum Beispiel um eine ausführliche Bewertungstabelle oder eine überarbeitete Version der Einreichung handeln. Auch ist es möglich eine Einreichung über den Button "Benötigt Überarbeitung" noch einmal an den Lernenden zurückzuspielen und eine Überarbeitungsschleife auszulösen.

Sobald Teilnehmende eine Aufgabe definitiv abgegeben haben, ist eine erneute Abgabe oder ein Austauschen für sie nicht mehr möglich. Falls eine Aufgabe versehentlich abgegeben oder das falsche Dokument hochgeladen wurde, kann der Betreuer aber die "Abgabe erneut öffnen" und so dem Lernenden ermöglichen eine weitere Abgabe einzureichen.

Wie weit der Bewertungsflow schon fortgeschritten ist, erkennen sowohl die Lernenden als auch die Lehrenden an den grünen Haken an den einzelnen Bewertungsschritten.

Sobald eine Einreichung akzeptiert wurde und der User keine Einreichungen bzw. Überarbeitungen mehr vornehmen soll, sollte der Button "Abgabe akzeptieren" bestätigt werden. Dadurch sind die Bearbeitung und die Bewertung einer Aufgabe definitiv abgeschlossen. Eine entsprechende Meldung erfolgt an die Teilnehmenden.

Die weiteren Bewertungsaktionen für die Aufgabe erfolgen im unteren Teil im Bereich "Bewertung", im eigentlichen Bewertungsformular. Hier können Punkte, Feedbacks usw. hinterlegt werden. Eine Beschreibung der Möglichkeiten finden sie auch [hier](The_assessment_form.de.md).

## Bewertungsflow für Gruppenaufgaben

Die Bewertung von Einreichungen über den Kursbaustein "Gruppenaufgabe" erfolgt ähnlich wie beim Kursbaustein "Aufgabe".

 * Gehen Sie zur gewünschten Gruppenaufgabe.
 * Wählen Sie im Tab "Übersicht" die gewünschte Gruppe oder filtern Sie im Tab "Teilnehmer:innen" die gewünschte Gruppe. 
 * Sofern ein Gruppenmitglied eine Einreichung für die Gruppe vorgenommen hat, gilt diese für die gesamte Gruppe und kann nun auch für die gesamte Gruppe bewertet werden.
 * Klicken Sie auf ein Gruppenmitglied oder wählen Sie im 3-Punkte Bereich die Option "Details anzeigen / bewerten" und Sie gelangen in den Bewertungsflow für die Gruppe. 
 * Nehmen Sie die Bewertung analog zur Bewertung des Kursbausteins Aufgabe vor. 

Im Bereich "Bewertung", also dem eigentlichen Bewertungsformular, klicken Sie auf den Button "Bewerten". 

![Zuweisung, Abgabe und Rückgabe der Gruppe sind abgeschlossen, der Schritt Bewertung steht auf "Offen" und zeigt die Leistungsübersicht beider Gruppenmitglieder mit dem Button "Bewerten": Bewertungsflow einer Gruppe im Bewertungswerkzeug](assets/Gruppe_bewerten.png){ class="shadow lightbox" }

Der Vorteil einer Gruppenaufgabe ist, dass eine Bewertung für alle Gruppenmitglieder über den Button "Bewerten" auf einen Schlag vorgenommen werden kann, gleichzeitig aber auch Anpassungen für einzelne Gruppenmitglieder möglich sind.

Wenn nicht die gesamte Gruppe bestanden hat oder nicht alle dieselbe Punktzahl erhalten sollen, darf "Für die ganze Gruppe" _nicht_ ausgewählt sein. Dadurch wird eine individuelle Bewertung pro Teilnehmer:in möglich.

![Die aktivierte Checkbox "Für die ganze Gruppe" überträgt Punkte und Kommentar auf alle Gruppenmitglieder, darunter die Wahl zwischen "Nicht freigegeben" und "Freigegeben": Dialog Bewertung einer Gruppenaufgabe](assets/Gruppenbewertung.png){ class="shadow lightbox" }

!!! info "Wichtig"

    Sollen andere bewertbare Kursbausteine anstatt einer "Gruppenaufgabe" für eine Gruppe bewertet werden, müssen die Bewertungen für jedes Gruppenmitglied separat vorgenommen werden.

!!! note "Hinweis"

    Im Kursrun ist die Bewertung der einzelnen Gruppen ähnlich wie generell beim Kursbaustein Aufgabe, ebenfalls möglich.
