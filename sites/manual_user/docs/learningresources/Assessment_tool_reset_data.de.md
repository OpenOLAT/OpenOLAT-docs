# Bewertungswerkzeug - Daten zurücksetzen {: #reset_data}

Mit Hilfe eines **Wizards** können die Daten von Teilnehmer:innen eines Kurses zurückgesetzt werden. Dabei kann das Zurücksetzen für den gesamten Kurs oder nur für ausgewählte Kursbausteine, für alle oder ausgewählte Teilnehmer:innen erfolgen.

Sie können aber auch **ohne Wizard** selektiv Daten bestimmter Teilnehmer:innen oder Kursbausteine zurücksetzen.

Abhängig vom Kursbaustein bzw. der Kurskonfiguration werden z.B. der Fortschritt, die Versuchsanzahl, Punkte, Erfolgsstatus, Bewertungsfreigaben und auch Erinnerungen zurückgesetzt. 


## Datensicherung vor dem Zurücksetzen {: #backup}

Bevor die Daten endgültig zurückgesetzt werden, können die alten Ergebnisse heruntergeladen und gespeichert werden. 

### Sicherung des gesamten Kurses

In der (Kurs-)Administration unter **Archivierung & Reporting** können Sie Reports der Kursresultate generieren. 

![assessment_tool_reset_data_backup_course_v1_de.png](assets/assessment_tool_reset_data_backup_course_v1_de.png){ class="shadow lightbox" } 



### Sicherung eines Kursbausteins "Test"

Die Daten eines Kursbausteins "Test" können im Bewertungswerkzeug als zip-Datei heruntergeladen und gespeichert werden.

![assessment_tool_reset_data_backup_course_element_test1_v1_de.png](assets/assessment_tool_reset_data_backup_course_element_test1_v1_de.png){ class="shadow lightbox" }

Die erzeugten zip-Dateien sind dann im unteren Bereich des Bildschirms aufgelistet und können heruntergeladen werden.

![assessment_tool_reset_data_backup_course_element_test2_v1_de.png](assets/assessment_tool_reset_data_backup_course_element_test2_v1_de.png){ class="shadow lightbox" }



## Daten zurücksetzen mit Wizard {: #wizard}

![assessment_tool_reset_data_wizard1_v1_de.png](assets/assessment_tool_reset_data_wizard1_v1_de.png){ class="shadow lightbox" }

![assessment_tool_reset_data_wizard2_v1_de.png](assets/assessment_tool_reset_data_wizard2_v1_de.png){ class="shadow lightbox" }

Wählen Sie im Wizard die Optionen "Ausgewählte Teilnehmer:innen" und "Ausgewählte Kursbausteine", werden Sie im Wizard zusätzlich durch die Teilschritte geführt und zum Schluss nochmals gefragt, ob das Zurücksetzen nun so erfolgen soll.

![assessment_tool_reset_data_wizard3_v1_de.png](assets/assessment_tool_reset_data_wizard3_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#reset_data})

---


## Daten bestimmter Teilnehmer:innen ohne Wizard zurücksetzen {: #members}

![assessment_tool_reset_data_member1_v1_de.png](assets/assessment_tool_reset_data_member1_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#reset_data})

---

## Daten bestimmter Kursbausteine ohne Wizard zurücksetzen {: #course_elements}

Je nach Kursbaustein werden folgende Daten zurückgesetzt, respektive annulliert:

* Fortschritt
* Anzahl Versuche
* Testdurchläufe
* Punkte und Erfolgsstatus
* Freigabe Bewertung
* Erinnerungen

Beim Zurücksetzen wird eine entsprechende Archivdatei mit den relevanten Daten erstellt und im Anschluss heruntergeladen. Das Archiv steht zusätzlich als Download im Leistungsnachweis der Teilnehmenden zur Verfügung.

[Zum Seitenanfang ^](#reset_data})

---


## Auswirkung des Zurücksetzens


### Auswirkungen im Bewertungsformular

Attribut | Auswirkung
---------|----------
Status | Auf "Nicht gestartet" gesetzt
Freigabe Bewertungsstatus | Auf "Nicht freigegeben" gesetzt
Anzahl Lösungsversuche | Auf 0 zurückgesetzt
Punktzahl | Zurückgesetzt
Erfolgsstatus | Auf "Keine Angabe" gesetzt
Kommentar für andere Betreuende | Zurückgesetzt; Export "assessment_coach_comment.txt" ins Archiv
Individueller Kommentar / Kommentar für Teilnehmer | Zurückgesetzt; Export "assessment_comment.txt" ins Archiv
Individuelle Bewertungsdokumente | Zurückgesetzt

[Zum Seitenanfang ^](#reset_data})

---


### Auswirkungen auf Kommentare & Bewertungen

Kommentare und Bewertungen an Kursbausteinen und am Kurs bleiben erhalten.

[Zum Seitenanfang ^](#reset_data})

---


### Auswirkung auf Kurserinnerungen {: #impact_on_reminders}

Die Informationen über gesendete Erinnerungen werden gelöscht. (Gilt nur, wenn der gesamte Kurs zurückgesetzt wird.)

[Zum Seitenanfang ^](#reset_data})

---


### Auswirkung auf Leistungsnachweise {: #impact_on_evidence_of_achievements}

Der Leistungsnachweis wird zum Zeitpunkt des Resets versioniert. Er bleibt im persönlichen Menü einsehbar.

[Zum Seitenanfang ^](#reset_data})

---


### Auswirkung auf Zertifikate {: #impact_on_certificates}

Wenn der gesamte Kurs zurückgesetzt ist, wird das Zertifikat nach erfolgreicher Kursdurchführung erneut ausgestellt. 

Einmal erworbene Zertifikate werden bei den Daten der Teilnehmer:in gespeichert und sind im persönlichen Menü weiterhin einsehbar. Auch wenn ein Zertifikat abgelaufen ist oder ein Kurs ganz gelöscht wurde. 

[Zum Seitenanfang ^](#reset_data})

---


### Auswirkung auf Kursbausteine {: #impact_on_course_elements}

Das Zurücksetzen der Daten wirkt sich individuell auf einzelne Kursbausteine aus.

Sofern der Kursbaustein einen Export ins Archiv auslöst, wird dieser immer erstellt, auch wenn keine Daten vorhanden sind.

Baustein | Auswirkung
---------|----------
Aufgabe | Alle Workflow-Daten (Zuweisung, Dokumente, Erweiterungen) zurückgesetzt; Export aller Dokumente ins Archiv
Bewertung | Formular zurückgesetzt; Export der Ergebnisse ins Archiv
Blog | Einträge bleiben erhalten
Checkliste | Alle Checkboxen zurückgesetzt; Export der Ergebnisse ins Archiv
Dateidiskussion | Dateien, Themen und Beiträge bleiben erhalten
Einschreibung | Einschreibungen in Gruppen werden entfernt
Formular | Formular zurückgesetzt; Export der Ergebnisse ins Archiv
Forum | Themen und Beiträge bleiben erhalten
Gruppenaufgabe | Wenn gesamte Gruppe zurückgesetzt wird: Alle Workflow-Daten (Zuweisung, Dokumente, Erweiterungen) zurückgesetzt; Export aller Dokumente für jeden Teilnehmer ins Archiv
LTI | Bewertungsformular zurückgesetzt
Ordner | Inhalte bleiben erhalten
Podcast | Einträge bleiben erhalten
Portfolio-Aufgabe | Link zur Portfolioaufgabe entfernt
SCORM | Versuche zurückgesetzt; Export der Versuche (csv-Datei) ins Archiv
Selbsttest | Alle Durchführungen zurückgesetzt
Struktur | Punktestand zurückgesetzt (nur herkömmlicher Kurs)
Teilnehmer-Ordner | Ordner zurückgesetzt; Export aller eingereichten und zurückgegebenen Dateien ins Archiv
Terminplanung | Anmeldungen bleiben erhalten
Test | Alle Versuche zurückgesetzt; Testdurchführungen bleiben bestehen und werden als ungültig markiert; Export der Testergebnisse ins Archiv
Themenvergabe | Themen-Zuweisungen werden entfernt
Themenbörse | Zuordnungen und Einschreibungen werden zuzrückgesetzt
Übung | Übungsdaten und -versuche zurückgesetzt; Testdurchführungen bleiben bestehen und werden als ungültig markiert; Export der Testergebnisse ins Archiv
Umfrage | Reset für alle Teilnehmenden: Zurückgesetzt und Export ins Archiv; Reset für einzelne Teilnehmende: Kein Zurücksetzen und Export, da Umfragen anonym sind
Video-Aufgabe | Alle Versuche zurückgesetzt; Durchführungen bleiben bestehen und werden als ungültig markiert; Export der Testergebnisse ins Archiv
Wiki | Einträge bleiben erhalten

[Zum Seitenanfang ^](#reset_data})

---


## Daten, die nicht zurückgesetzt werden {: #no_reset}

Die folgenden Elemente werden beim Zurücksetzen nicht gelöscht:

* Mitgliedschaftsdaten (Ausnahme: Gruppenmitgliedschaft im Einschreiben-Kursbaustein)
* Logging-Daten
* Benachrichtigungsabonnements
* Chat-Protokolle
* Hochgeladene Dateien in einem öffentlichen Bereich (z. B. Ordnerbaustein)
* Forenbeiträge und andere Kommentare
* Erstellte Blog- oder Podcast-Einträge der Benutzer:innen
* Hinzugefügte Wiki-Einträge der Benutzer:innen
* Hinzugefügte Glossareinträge der Benutzer:innen

[Zum Seitenanfang ^](#reset_data})

---


## Daten neu berechnen {: #recalculate}


!!! info "Hinweis"

    Diese Funktion ist ab Release 20.2 entfernt worden, weil sie nicht mehr erforderlich ist.

Über diesen Link des Menüs kann eine Neuberechnung des Kurses angestoßen
werden. So können die Kursbewertungen und Leistungsnachweise aktualisiert, die
Berechnung für bestanden und auch manuell gesetztes "bestanden" zurückgesetzt
werden.

![Daten neu berechnen](assets/neu_berechnen1.jpg)



[Zum Seitenanfang ^](#reset_data})

---


## Weitere Informationen {: #further_information}

[Bewertungswerkzeug - Tab Teilnehmer >](../../manual_user/learningresources/Assessment_tool_tab_Users.de.md)<br>
[Kurs löschen >](../../manual_user/learningresources/Course_Delete.de.md)<br>
[Benutzer:in löschen >](../../manual_admin/usermanagement/Delete_User.de.md)<br>

[Zum Seitenanfang ^](#reset_data})



