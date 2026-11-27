# Kursbausteine im Überblick {: #course_elements}

:octicons-device-camera-video-24: **Video-Einführung**: [Was sind Kursbausteine?](<https://www.youtube.com/embed/JM6iSrfkHog>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}

Aus Kursbausteinen bauen Sie Ihren Kurs auf. Mit ihnen stellen Sie Inhalte bereit und strukturieren sie, fördern Zusammenarbeit und Austausch, prüfen den Wissensstand der Teilnehmenden und regeln Organisatorisches.

Im Kurseditor ordnet OpenOlat die Kursbausteine in fünf Gruppen. Sie sehen die Gruppen im Dialog "Kursbausteine einfügen":<br>
`Kurs > Administration > Kurseditor > Kursbausteine einfügen`

![Alle Kursbausteine, die sich in einen Kurs einfügen lassen, nach Gruppen geordnet, dazu die Einträge Mehrere Checklisten und Mehrere HTML-Seiten](assets/course_elements_index_V2_de.png){ class="shadow lightbox" title="Dialog Kursbausteine einfügen im Kurseditor" }

Das Handbuch ordnet die Kursbausteine in denselben Gruppen. Jede Gruppe hat eine eigene Seite mit allen Kursbausteinen der Gruppe:

Gruppe | Wozu
---------|----------
[Wissensvermittlung](Knowledge_Transfer/index.de.md) | Kursinhalte bereitstellen und den Kurs strukturieren, auch mit Inhalten, die ausserhalb von OpenOlat erstellt wurden.
[Wissensüberprüfung](Assessment/index.de.md) | Den Wissensstand der Teilnehmenden prüfen, ihre Arbeiten bewerten und sie befragen.
[Kommunikation und Kollaboration](Communication_and_Collaboration/index.de.md) | Austausch und Zusammenarbeit im Kurs, auch live in virtuellen Klassenzimmern.
[Verwaltung und Organisation](Administration_and_Organisation/index.de.md) | Die Einschreibung in Gruppen, die Vergabe von Themen und Terminen sowie Informationen und E-Mails an die Teilnehmenden.
[Andere](Other/index.de.md) | Eigene und externe Webseiten, externe Lernapplikationen über LTI (Learning Tools Interoperability), Linklisten, Themenvergabe und Auswahl.

## Allgemeines zu Kursbausteinen

Alle Kursbausteine haben die Tabs "Titel und Beschreibung" und "Layout". Weitere Tabs hängen vom Kurstyp ab: Den Tab "Lernpfad" haben die Kursbausteine in Lernpfadkursen, die Tabs "Sichtbarkeit" und "Zugang" die Kursbausteine in herkömmlichen Kursen.

Neben den Kursbausteinen gestalten Sie Kurse mit weiteren Werkzeugen und Lernressourcen. Sie sind in den jeweiligen Kapiteln beschrieben.

## Leistungsbewertung {: #performance_assessment}

Viele Kursbausteine können Sie zur summativen oder formativen Bewertung nutzen oder zur Fortschrittskontrolle. Die Bewertungen der bewertbaren Kursbausteine sehen und bearbeiten Sie im [Bewertungswerkzeug](../Assessment_tool_overview/index.de.md). Alle Einstellungen beschreibt die Seite des jeweiligen Kursbausteins:

* [Aufgabe](../Course_Element_Task/index.de.md) (manuelle Bewertung)
* [Gruppenaufgabe](../Course_Element_Grouptask.de.md) (manuelle Bewertung)
* [Portfolioaufgabe](../Course_Element_Portfolio_Task.de.md) (manuelle Bewertung)
* [Checkliste](../Course_Element_Checklist.de.md) (manuelle & automatische Bewertung)
* [Bewertung](../Course_Element_Assessment.de.md) (manuelle Bewertung)
* [LTI](../Course_Element_LTI_Page.de.md) (automatische Bewertung, wird von LTI-Seite übertragen)
* [SCORM](../Course_Element_SCORM_Learning_Content.de.md) (automatische Bewertung, wird durch SCORM-Modul übertragen)
* [Test](../Course_Element_Test/index.de.md) (automatische & manuelle Bewertung)
* [Videoaufgabe](../Course_Element_Video_Task.de.md#tab_assessment) (automatische & manuelle Bewertung, nur im Modus "Test: Situationen erkennen")

Die Fortschrittskontrolle steuern [Lernpfadkurse](../Learning_path_course/index.de.md) über das Erledigungskriterium, das Sie im Kurseditor pro Kursbaustein im Tab "Lernpfad" festlegen. Mit dem Kriterium "Bestätigung durch Benutzer:in" bestätigen die Teilnehmenden die Bearbeitung selbst über den Toggle-Button "Als erledigt markieren".

![Toggle-Button Als erledigt markieren neben der Pfeilnavigation](../assets/learning_path_mark_as_done_v1_de.png){ class="shadow lightbox" title="Kurs-Toolbar in der Teilnehmer:innenansicht eines Lernpfadkurses" }

Eine Übersicht aller Kriterien finden Sie auf der Seite [Lernpfadkurs - Kurseditor](../Learning_path_course_Course_editor.de.md#completion_criterion).

### Rangliste [:octicons-tag-16:{ title="ab Release 11.3 (OO-2133)" }](https://track.frentix.com/issue/OO-2133) {: #highscore}

Vergeben Sie in einem Kursbaustein Punkte, können Sie den Teilnehmenden eine Rangliste anzeigen. Die Rangliste ermöglicht einen spielerischen Vergleich und kann die Teilnehmenden motivieren.

Die Rangliste richten Sie im Tab "HighScore" ein. Den Tab haben alle bewertbaren Kursbausteine ausser Übung und Videoaufgabe, dazu der Kursbaustein "Struktur". Voraussetzung ist, dass der Kursbaustein Punkte vergibt, zum Beispiel ein Test, eine Aufgabe oder eine Bewertung.

Schalten Sie zuerst "Highscore anzeigen" ein. Unter "Anfangsdatum (optional)" legen Sie fest, ab wann OpenOlat die Rangliste zeigt. Ohne Anfangsdatum zeigt OpenOlat die Rangliste, sobald die Bewertung der Person freigegeben ist: beim Test direkt nach dem Beenden, beim Kursbaustein "Bewertung" erst, wenn Betreuer:innen die Bewertung abschliessen und freigeben. Zwischengespeicherte Punkte genügen nicht. Mit "Daten der Benutzer:innen anonymisieren" zeigt die Rangliste die Personen anonymisiert statt mit Vor- und Nachnamen.

Danach wählen Sie, welche Elemente die Rangliste zeigt: "Gratulationstitel", "Siegertreppchen", "Histogramm" und "Liste der besten Teilnehmer:innen". Bei der Liste legen Sie fest, ob sie alle Teilnehmenden oder nur eine bestimmte Anzahl der besten zeigt. Mindestens eine dieser Optionen muss gewählt sein.

![Gratulationstitel mit dem eigenen Platz, Siegertreppchen mit drei Rängen, Histogramm der Punkteverteilung und Liste der besten Teilnehmer:innen](../assets/course_elements_highscore_v1_de.png){ class="shadow lightbox" title="Rangliste eines Kursbausteins aus Sicht der Teilnehmenden · 2026.11.02" }

## Schreibschutz der Bewertungskonfiguration [:octicons-tag-16:{ title="ab Release 21.1 (OO-9647)" }](https://track.frentix.com/issue/OO-9647){:target="_blank"} {: #assessment_config_read_only}

Sobald für einen bewertbaren Kursbaustein Bewertungen vorhanden sind, zeigt OpenOlat im Kurseditor die Einstellungen schreibgeschützt an, die das Bewertungsergebnis verändern. Ein Schloss-Symbol vor der Beschriftung zeigt, welche Einstellungen das sind. Die übrigen Einstellungen im selben Tab bleiben bearbeitbar.

Der Grund: Jede Änderung an den Bewertungsregeln löst beim Publizieren eine Neuberechnung aller bestehenden Bewertungen aus. Die Neuberechnung lässt sich nicht rückgängig machen. Der Schreibschutz stellt sicher, dass Sie diesen Eingriff bewusst auslösen.

Als vorhanden gilt eine Bewertung, sobald mindestens eine Person für diesen Kursbaustein eine Punktzahl, einen Bestanden-Status oder eine Note hat. Ein Status allein genügt nicht: Hat eine Person den Kursbaustein nur gestartet, bleibt die Konfiguration bearbeitbar. Die Prüfung gilt je Kursbaustein. Bewertungen in einem anderen Kursbaustein des Kurses lösen den Schreibschutz nicht aus.

Der Schreibschutz gilt in Lernpfadkursen und in herkömmlichen Kursen. Die Kursbausteine "Selbsttest" und "Fragebogen" kennen ihn nicht.

### Schreibgeschützte Einstellungen bearbeiten {: #enable_edit_mode}

Im schreibgeschützten Zustand steht unter der Legende "Konfiguration Bewertung" der Hinweis: "Da bereits **Bewertungen vorhanden** sind, werden bestimmte Einstellungen als **schreibgeschützt** angezeigt. Um Änderungen vorzunehmen, müssen Sie den Bearbeitungsmodus aktivieren - bei Änderungen werden alle vorhandenen Bewertungen neu berechnet."

![Hinweis mit der Schaltfläche "Bearbeitungsmodus aktivieren" unter "Konfiguration Bewertung", davor ein Schloss an jeder schreibgeschützten Einstellung, "Bewertungsformular" ohne Schloss](../assets/assessment_read_only_info_v1_de.png){ class="shadow lightbox" title="Tab Konfiguration einer Checkliste mit vorhandenen Bewertungen · 2026.11.02" }

Im Hinweis steht die Schaltfläche "Bearbeitungsmodus aktivieren" mit dem Symbol eines offenen Schlosses. Nach dem Klick sind die schreibgeschützten Einstellungen bearbeitbar, und an der Stelle des Hinweises steht die Warnung: "Sie bearbeiten derzeit die Konfiguration der Bewertung, obwohl bereits Bewertungen vorhanden sind. Wenn Sie die Änderungen speichern und veröffentlichen, werden alle vorhandenen Bewertungen **neu berechnet**. Dieser Vorgang kann **nicht rückgängig** gemacht werden."

![Warnung zur Neuberechnung an der Stelle des Hinweises, die Einstellungen unter "Konfiguration Bewertung" ohne Schloss und bearbeitbar](../assets/assessment_read_only_warning_v1_de.png){ class="shadow lightbox" title="Tab Konfiguration einer Checkliste im Bearbeitungsmodus · 2026.11.02" }

Sind noch keine Bewertungen vorhanden, erscheinen weder Hinweis noch Warnung. Der Tab ist dann direkt bearbeitbar.

Der Bearbeitungsmodus gilt nur, solange Sie den Kursbaustein im Kurseditor bearbeiten. Öffnen Sie den Kursbaustein später wieder im Kurseditor, ist der Schreibschutz wieder aktiv. Eine Einstellung, die den Schreibschutz dauerhaft aufhebt, gibt es nicht.

### Betroffene Kursbausteine {: #read_only_course_elements}

Die bewertbaren Kursbausteine gliedern ihre Bewertungsregeln gleich: Oben stehen unter der Legende "Konfiguration Bewertung" der Hinweis und die Einstellungen, die der Schreibschutz erfasst. Darunter stehen unter "Bewertungsformular" die Einstellungen "Individueller Kommentar" und "Individuelle Bewertungsdokumente", die bearbeitbar bleiben. Die Tabelle zeigt, in welchem Tab Sie den Schreibschutz antreffen und was er erfasst.

Kursbaustein | Tab | Schreibgeschützt | Bleibt bearbeitbar
---------|----------|----------|----------
[Test](../Course_Element_Test/Test_Setup.de.md#tab_configuration) | "Test-Konfiguration" | "Bewertung mit Einstufung/Noten" samt Bewertungsskala, "Bei Kurs-Bewertung berücksichtigen" | alle übrigen Einstellungen, zum Beispiel "Testzeitraum festlegen", "Korrektur" und "Report"
[SCORM 1.2](../Course_Element_SCORM_Learning_Content.de.md#editor_tab_learning_content) | "Lerninhalt" | die Einstellungen unter "Konfiguration Bewertung", zum Beispiel "Resultat aus SCORM übertragen", "Maximal erreichbare Punkte", "Notwendige Punktzahl für 'bestanden'" und "Bei Kurs-Bewertung berücksichtigen" | "Reduzieren von Punkten bei erneutem Versuch verhindern", "Lösungsversuche nur zählen, wenn Punkte übertragen werden", "Maximale Anzahl Lösungsversuche", die Bereiche "SCORM" und "Einstellungen"
[Aufgabe](../Course_Element_Task/Task_Setup.de.md#grading) | "Bewertung" | "Rubrik-Bewertung", Punkte, Einstufung/Noten, Bestanden/Nicht bestanden, "Bei Kurs-Bewertung berücksichtigen" | "Bewertungsformular"
[Gruppenaufgabe](../Course_Element_Grouptask.de.md#tab_assessment) | "Bewertung" | Punkte, Einstufung/Noten, Bestanden/Nicht bestanden, "Bei Kurs-Bewertung berücksichtigen" | "Bewertungsformular"
[Videoaufgabe](../Course_Element_Video_Task.de.md#tab_assessment) | "Bewertung" | alle Einstellungen unter "Konfiguration Bewertung", darunter Punkte, Einstufung/Noten, Bestanden/Nicht bestanden, "Bei Kurs-Bewertung berücksichtigen" | "Bewertungsformular"
[Portfolioaufgabe](../Course_Element_Portfolio_Task.de.md#tab_assessment) | "Bewertung" | Punkte, Einstufung/Noten, Bestanden/Nicht bestanden, "Bei Kurs-Bewertung berücksichtigen" | "Bewertungsformular"
[Bewertung](../Course_Element_Assessment.de.md#tab_assessment) | "Bewertung" | "Rubrik-Bewertung", "Punkte vergeben", "Bewertung mit Einstufung/Noten", "Bestanden/Nicht bestanden ausgeben", "Bei Kurs-Bewertung berücksichtigen" | "Status "Korrigieren" setzen, wenn Zugriff gewährt", "Bewertungsformular"
[Checkliste](../Course_Element_Checklist.de.md#tab_configuration) | "Konfiguration" | Punkte, Einstufung/Noten, Bestanden/Nicht bestanden samt "Art der Ausgabe" und Schwellen, "Bei Kurs-Bewertung berücksichtigen" | "Konfiguration der Checkliste" mit dem Abgabedatum, "Bewertungsformular"
[Struktur](../Course_Element_Structure.de.md#score), nur im herkömmlichen Kurs | "Punkte" | die ganze Legende "Zusammengefasste Bewertung" | keine

Einstellungen, die ohnehin nicht bearbeitbar sind, bleiben es auch im Bearbeitungsmodus, zum Beispiel "Minimal erreichbare Punkte" bei der Videoaufgabe.

## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Kursbausteine im Kurseditor >](../General_Configuration_of_Course_Elements.de.md)<br>
[Löschen, Verschieben und Kopieren von Kursbausteinen >](../Deleting_Moving_and_Copying_Course_Elements.de.md)<br>
[Kurseditorwerkzeuge >](../Using_additional_Course_Editor_Tools.de.md)

**youtube**<br>
[Was sind Kursbausteine?](<https://www.youtube.com/embed/JM6iSrfkHog>)<br>
[Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>)

[Zum Seitenanfang ^](#course_elements)
