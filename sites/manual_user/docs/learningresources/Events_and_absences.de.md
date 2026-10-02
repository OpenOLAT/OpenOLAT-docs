# Termine und Absenzen {: #course_admin_events_and_absences}

Das Absenzenmanagement ermöglicht es, Anwesenheitslisten online zu führen und Fehlzeiten zu dokumentieren. Die Anwesenheitskontrolle wird jeweils kursbezogen durchgeführt.

Dazu können im Kurs **Termine** angelegt werden, die sich in mehrere **Einheiten** unterteilen lassen. So kann beispielsweise ein Vormittag (Termin) in mehrere Zeitblöcke (Einheiten) gegliedert werden. Dadurch ist es möglich, dass Teilnehmende nur für einzelne Einheiten eines Termins als abwesend markiert werden, ohne den gesamten Termin zu verlieren.

Termine und Einheiten werden entweder von den Kursbesitzer:innen selbst erstellt oder über ein externes Verwaltungssystem mit OpenOlat synchronisiert. Alle Termine erscheinen auch im Kurskalender, sofern der Kurs einen Kalender beinhaltet.

Bevor das Absenzenmanagement genutzt werden kann, muss es von den Kursbesitzer:innen aktiviert werden. Dies geschieht unter `Kurs > Administration > Einstellungen > Tab Durchführung`. Nach der Aktivierung können weitere Einstellungen vorgenommen werden, und in der Toolbar erscheint zusätzlich die Option "Termine".


## "Termine" in der Toolbar {: #toolbar_events}

**Kursbesitzer:innen** können hier Termine hinzufügen und Absenzen organisieren. Zusätzlich erscheint für Kursbesitzer:innen in der Kurs-Administration das Menü "Termine und Absenzen". Die Möglichkeiten sind dabei überwiegend identisch. 

![Menüeintrag "Termine und Absenzen" öffnet die Termin- und Absenzenverwaltung für Kursbesitzer:innen](assets/events_and_absences_adminmenu_v1_de.png){ class="shadow lightbox" title="Menü Administration eines Kurses" }

**Kursbetreuer:innen** sehen das Menü "Termine" nur in der Toolbar, nicht aber in der Kurs-Administration. Auch können sie *keine* neuen Termine anlegen, nur die vorhandenen einsehen und, sofern aktiviert, Absenzen erfassen. Es kann auch nach Terminen gefiltert werden, für die man als Betreuer:in eingetragen ist.

![Betreuer:innen erreichen die Termine nur über das Toolbar-Icon "Termine"; das Menü Administration enthält für sie keinen Eintrag "Termine und Absenzen"](assets/events_and_absences_toolbar_for_coach_v1_de.png){ class="shadow lightbox" title="Kurs-Toolbar in der Sicht der Betreuer:innen" }

**Teilnehmende** sehen das Menü "Termine" in der Toolbar und können so rasch synchrone Präsenz- oder Online-Termine erkennen, z.B. im Rahmen von Blended-Learning. 

![Teilnehmende öffnen über das Toolbar-Icon "Termine" die Terminliste des Kurses mit Datum, Zeit, Einheiten, Status, Ort und Dozenten](assets/TN_Termine_Absenzen.jpg){ class="shadow lightbox" title="Terminliste in der Sicht der Teilnehmenden" }

Persönliche Fehlzeiten finden Teilnehmende dann bei den "Persönlichen Werkzeugen" im [Menü "Absenzen"](../personal_menu/Absences.de.md).

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

Im Folgenden wird die Ansicht der Termine und Absenzen für **Kursbesitzer:innen** näher beschrieben. 

## Tab Termine [:octicons-tag-16:{ title="ab Release 12.0 (OO-2636)" }](https://track.frentix.com/issue/OO-2636) {: #tab_events}

![Die Terminverwaltung für Kursbesitzer:innen mit den Tabs Termine, Teilnehmer:innen und Rekurse, dem Button "Termin hinzufügen" und der aufgeklappten Detailansicht eines Termins](assets/Termine_Kursbesitzende_20.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

### Termine anzeigen {: #display_events}

Im Tab "Termine" können dem Kurs Termine hinzugefügt und nach unterschiedlichen Kriterien gefiltert angezeigt werden. Wurde der Termin z.B. Fachbereichen zugeordnet (Taxonomie), kann nach diesen gefiltert werden. Um Details zu einem Termin anzuzeigen, klicken Sie auf das + zu Beginn der betreffenden Zeile.

Im 3-Punkte-Menü am Ende jeder Zeile finden Sie die Aktionen zu einem Termin:

- **Bearbeiten** und **Kopieren**
- **Ändere in Online Meeting** oder **Ändere in vor Ort Termin**, bei einem Termin mit Online Meeting zusätzlich **Online Meeting beitreten**
- **Als Prüfung markieren**, bei einem bereits markierten Termin stattdessen **Prüfung editieren** und **Prüfung löschen**, siehe [Termin als Prüfung markieren](#mark_event_as_exam)
- **Absenzenliste** und **Präsenzliste** als PDF, **Log** und **Export** als Excel-Datei
- **Termin wiederöffnen** bei einem abgeschlossenen oder abgesagten Termin, siehe [Termine wiederöffnen](#reopen_events)
- **Löschen**

Wird der Kurs im Course Planner verwendet, fehlen Bearbeiten, Kopieren, die Umstellung auf ein Online Meeting oder einen vor Ort Termin und Löschen, weil die Termine im Course Planner verwaltet werden. Stammen die Termine aus einem externen Verwaltungssystem, können Bearbeiten und Löschen ebenfalls fehlen. Welche Einträge Betreuer:innen im selben Menü sehen, beschreibt die Seite zur Toolbar: [Menü am Zeilenende](../learningresources/Toolbar_Events.de.md#lists_and_export)

![Das 3-Punkte-Menü eines Termins bietet unter anderem Bearbeiten, Kopieren, Ändere in Online Meeting, Als Prüfung markieren, Absenzen- und Präsenzliste, Export und Termin wiederöffnen](assets/Termine_Asenzen.jpg){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

Über die Spaltenauswahl (Zahnrad) blenden Sie weitere Spalten ein. Ist das Modul "Räume" aktiviert, steht dort zusätzlich die Spalte "Räume" mit den gebuchten Räumen des Termins. Sie ist standardmässig ausgeblendet.


[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Ansichten: Zeitansicht und Tabelle {: #views}

Die Terminliste steht in zwei Ansichten zur Verfügung. Rechts über der Liste stehen die beiden Umschalter nebeneinander: links die "Zeitansicht", rechts die "Tabellenansicht". Für Kursbesitzer:innen ist die Tabellenansicht voreingestellt, Teilnehmende sehen die Zeitansicht.

In der Zeitansicht steht jeder Termin als eigener Block, nach Jahr und Datum gruppiert. Der Kopf des Blocks nennt links den Titel und das Kennzeichen des Termins mit dem Statusabzeichen, darunter die Zeit. Rechts steht das 3-Punkte-Menü mit den Aktionen zum Termin. Optional kommen dazu: die Fachbereiche als Etiketten unter dem Titel, der Ort, und bei einem Online Meeting die Schaltfläche zum Beitreten. Sind Vor- oder Nachlaufzeiten erfasst, erscheinen sie als Minutenangabe hinter der Zeit.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Detailansicht eines Termins [:octicons-tag-16:{ title="ab Release 21.0 (OO-9526)" }](https://track.frentix.com/issue/OO-9526){:target="_blank"} {: #event_details}

In der Tabellenansicht klappt ein Klick auf das + zu Beginn einer Zeile die Detailansicht auf, in der Zeitansicht der Pfeil am unteren Rand des Blocks. Der Inhalt ist in beiden Ansichten derselbe.

In der Tabellenansicht steht zuoberst eine Titelzeile mit Titel und Kennzeichen des Termins, den Abzeichen "Status" und "Absenzen" und rechts der Aktion "Bearbeiten". In der Zeitansicht entfällt sie, weil der Kopf des Blocks diese Angaben bereits trägt; bearbeitet wird dort über das 3-Punkte-Menü.

Die Attributzeile fasst die Eckwerte zusammen: Datum, Zeit, Teilnehmer:innen und Präsenz. "Einheit" erscheint nur, wenn der Termin mehr als eine Einheit umfasst, "Ort" nur, wenn ein Ort erfasst ist.

Danach folgen die Dozent:innen als Personenkarten mit Visitenkarte, E-Mail und Chat. Ist niemand eingetragen, steht dort "Keine Dozenten verfügbar.".

Die übrigen Angaben erscheinen nur, wenn sie am Termin gepflegt sind:

* **Online Meeting**: "Online Meeting beitreten" als hervorgehobene Schaltfläche, dazu der Link auf eine hinterlegte Aufzeichnung.
* **Raum**: die Raumkarte unter dem Label "Raum", bei mehreren Räumen unter "Räume". Ist ein Raum im Zeitraum des Termins doppelt gebucht, steht die Warnung unterhalb der Raumkarte und die Karte erhält einen gelben Rand. [:octicons-tag-16:{ title="ab Release 21.0.2 (OO-9641)" }](https://track.frentix.com/issue/OO-9641){:target="_blank"}
* **Beschreibung** und **Vorbereitung/Nachbereitung** als eigene Absätze.

Zuunterst steht die Tabelle der Elemente, deren Teilnehmende zum Termin gehören.

![Aufgeklappter Terminblock mit Eckwerten, Dozentenfeld, Raumkarte, Beschreibung und Elementtabelle](assets/events_and_absences_timeline_v1_de.png){ class="shadow lightbox" title="Zeitansicht der Terminliste" }

Räume werden im Course Planner zugewiesen. Ein eigenständiger Kurs zeigt deshalb keine Raumkarten: [Räume für einen Termin belegen >](../area_modules/Course_Planner_Events.de.md#room_booking)

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termin erstellen/bearbeiten {: #edit_events}

Zum Hinzufügen (weiterer) Termine verwenden Sie den Button "Termin hinzufügen" rechts oben über der Liste im Tab "Termine".

![Button "Termin hinzufügen" rechts oben über der Terminliste](assets/events_and_absences_tab_events_create1_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

!!! info "Wichtig"

    Der Button "Termin hinzufügen" wird nur angezeigt, wenn es sich um einen eigenständigen Kurs handelt. Siehe `Kurs > Administration > Einstellungen > Tab Freigabe > Abschnitt Verwendung`.<br>Wird der Kurs im Course Planner verwendet, werden die Termine im Course Planner erstellt und verwaltet.

Es öffnet sich ein Popup zur Erfassung aller Angaben zum Termin. 

![Eingabemaske für einen neuen Termin mit den Pflichtfeldern Titel, Datum und Zeit, dem Toggle Online Meeting und dem Schalter Präsenz](assets/events_and_absences_tab_events_create2_v3_de.png){ class="shadow lightbox" title="Dialog Termin hinzufügen" }

 **Titel**: Vergeben Sie einen sinnvollen Namen.

 **Kennzeichen**: Die optionale Angabe eines Kennzeichens dient zur Unterscheidung bei Terminen mit gleichem Titel.

 **Datum**: Ein Datum muss zwingend angegeben werden.

 **Zeit**: Auch die Zeitangabe ist ein Pflichtfeld. Denn z.B. können Kalendereinträge nur mit einer Zeitangabe korrekt angezeigt werden.

 **Einheit**: Hier wird angegeben, wie viele (Zeit-)Einheiten dieser Termin umfasst.<br>
 Ein Termin kann 1 - 12 Einheiten umfassen.<br>
 Beispiel: Ein Termin umfasst 2 Stunden, die in 4 thematische Einheiten gegliedert sind (4 x 0.5 Stunden).

!!! info "Wichtig"

    Stammen die Termine aus einem externen Verwaltungssystem, das sie nach OpenOlat synchronisiert, ist das Feld "Einheit" in OpenOlat gesperrt. Der Wert kommt aus diesem System und wird dort geändert. Gesperrt ist das Feld ausserdem, sobald die Anwesenheitskontrolle des Termins abgeschlossen ist.

 **Ort**: Hier wird angegeben, wo dieser Termin stattfindet. Das kann z.B. ein Präsenzort oder die genaue Zimmerbezeichnung sein.

 **Online Meeting**: Soll der Termin online stattfinden, schalten Sie den Toggle-Button "Online Meeting" ein. Zur Auswahl stehen BigBlueButton, Microsoft Teams und "Sitzungs-Link". Der Sitzungs-Link deckt weitere Anbieter ab, zum Beispiel Zoom. Geben Sie dafür den "Name des Sitzungsanbieters" und die "URL für Sitzungsteilnahme" an.<br>
 Das Online Meeting übernimmt Titel, Zeit und Personen aus dem Termin. Später öffnen Sie es in der Terminliste über "Online Meeting beitreten".
Lernende haben Zugriff über den Kalender oder das Icon "Termine" in der Toolbar.

**URL für Aufzeichnung**: Es kann eine beliebige URL angegeben werden, unter der eine Aufzeichnung des Meetings aufgerufen wird. Die URL kann auch angegeben werden, wenn der Toggle-Button "Online Meeting" ausgeschaltet ist.

**Fachbereiche**: Hier können Sie den Termin einem oder mehreren Begriffen einer hinterlegten Taxonomie zuordnen. Dadurch kann der Termin dann schneller gefunden werden.

**Dozenten**: Für jeden Termin muss ein:e Kursbetreuer:in ausgewählt werden. Nur die ausgewählten Kursbetreuer:innen können die Anwesenheitskontrolle durchführen. (Als Dozent:in kann nur eine Person hinzugefügt werden, die auch die Rolle "Betreuer:in" besitzt.) Möchte ein:e Kursbesitzer:in ebenfalls diese Funktion übernehmen, muss sich diese Person zusätzlich als Kursbetreuer:in in den Kurs eintragen.

**Beschreibung**: Hier können Sie optional eine Beschreibung für den Termin hinzufügen.

**Vorbereitung/Nachbereitung**: Falls Sie den Teilnehmenden einen Vor- bzw. Nachbereitungsauftrag zum jeweiligen Termin geben möchten, kann dieser hier hinzugefügt werden. Er wird im Kalender angezeigt, sofern die Termine mit dem Kurskalender synchronisiert werden: `Kurs > Administration > Einstellungen > Tab Durchführung`.

**Präsenz**: Wird der Schalter auf "Aus" gestellt, ist die Absenzenerfassung für den Termin deaktiviert.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine kopieren oder löschen {: #copy_delete_events}

Sobald in der ersten Spalte mindestens ein Termin selektiert ist, erscheinen über der Liste der Termine die Buttons zum Kopieren und Löschen von Terminen.<br>
Alternativ können die Optionen zum Kopieren und Löschen unter den 3 Punkten am Ende einer Zeile aufgerufen werden.

![Bei selektiertem Termin erscheinen über der Liste die Buttons "Kopieren" und "Löschen"; dieselben Optionen stehen im 3-Punkte-Menü am Ende der Zeile](assets/events_and_absences_tab_events_copy_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine importieren [:octicons-tag-16:{ title="ab Release 13.0 (OO-3666)" }](https://track.frentix.com/issue/OO-3666){:target="_blank"} {: #import_events}

Viele Termine auf einmal erfassen Sie schneller mit einer Excel-Datei als einzeln im Dialog. Klicken Sie dazu im Tab "Termine" auf den kleinen Pfeil neben dem Button "Termin hinzufügen" und wählen Sie "Termine importieren". Der Assistent "Termine aus Excel importieren" bietet die "Vorlage Excelimport" zum Herunterladen. Kopieren Sie die ausgefüllten Zeilen aus der Excel-Datei in das Feld "Kopierte Zeilen aus Exceldatei (Kommasepariert)".

![Der kleine Pfeil neben dem Button "Termin hinzufügen" öffnet die Option "Termine importieren"](assets/events_and_absences_tab_events_import_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Termin als Prüfung markieren [:octicons-tag-16:{ title="ab Release 14.0 (OO-4045)" }](https://track.frentix.com/issue/OO-4045) {: #mark_event_as_exam}

Findet ein Termin als Prüfung statt, markieren Sie ihn über "Als Prüfung markieren" im 3-Punkte-Menü. OpenOlat legt dafür einen Prüfungsmodus an, der Datum, Zeit und Teilnehmende aus dem Termin übernimmt. Im folgenden Dialog wählen Sie die Kursbausteine der Prüfung und schalten bei Bedarf den [Safe Exam Browser](../../manual_how-to/SEB/SEB.de.md) ein: [Prüfungsmodus aus einem Termin](../learningresources/Assessment_mode.de.md#exam_from_event)

![Eintrag "Als Prüfung markieren" im 3-Punkte-Menü am Ende der Terminzeile](assets/events_and_absences_tab_events_mark_as_exam_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

Nach dem Speichern zeigt die Spalte "Prüfung" ein Symbol, und das 3-Punkte-Menü bietet "Prüfung editieren" und "Prüfung löschen". Die Prüfung erscheint zudem in der Prüfungsverwaltung des Kurses unter `Kurs > Administration > Prüfungsverwaltung`.

![Symbol in der Spalte Prüfung und die Einträge Prüfung editieren und Prüfung löschen im 3-Punkte-Menü](assets/events_and_absences_tab_events_exam_marked_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.02" }

Denselben Eintrag haben Betreuer:innen in der Toolbar. Wer ihn ausserdem nutzen kann und warum er fehlen kann, beschreibt die Seite zur Toolbar: [Wenn "Als Prüfung markieren" fehlt](../learningresources/Toolbar_Events.de.md#mark_as_exam_missing)

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine absagen {: #cancel_events}

Das Absagen von Terminen findet über das [Termin-Icon in der Toolbar](../learningresources/Toolbar_Events.de.md#cancel_events) statt.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine abschliessen {: #close_events}

Das Abschliessen von Terminen findet über das [Termin-Icon in der Toolbar](../learningresources/Toolbar_Events.de.md#close_events) statt.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Termine wiederöffnen {: #reopen_events}

Ein bereits abgeschlossener Termin kann von Kursbesitzer:innen wiedergeöffnet werden. Sie finden die Option "Termin wiederöffnen" unter den 3 Punkten in der Zeile eines Termins.

![Die Option "Termin wiederöffnen" im 3-Punkte-Menü eines erledigten Termins](assets/events_and_absences_reopen_event1_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

Alternativ kann ein Termin auch über das Buch-Symbol (Absenz editieren) wiedergeöffnet werden.

![Das Buch-Symbol "Absenz editieren" öffnet die Absenzenerfassung; der Button "Termin wiederöffnen" öffnet den abgeschlossenen Termin erneut](assets/Termin_wiederoeffnen_20.jpg){ class="shadow lightbox" title="Absenzenerfassung eines Termins" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Dozent:innen verwalten [:octicons-tag-16:{ title="ab Release 20.0.3 (OO-8622)" }](https://track.frentix.com/issue/OO-8622) {: #manage_teachers}

Sobald in der ersten Spalte mindestens ein Termin selektiert ist, erscheint über der Liste der Termine der Button "Dozent:innen verwalten".

![Bei selektiertem Termin erscheint über der Terminliste der Button "Dozent:innen verwalten" neben den Buttons "Kopieren" und "Löschen"](assets/events_and_absences_tab_events_teachers1_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration" }

![Im Dialog "Dozent:innen verwalten" werden Dozent:innen per Checkbox einzelnen Terminen oder über die Buttons allen Terminen zugewiesen oder entzogen](assets/events_and_absences_tab_events_teachers2_v1_de.png){ class="shadow lightbox" title="Dialog Dozent:innen verwalten" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Teilnehmer:innen ausschliessen {: #exclude_participants}

Bei geöffneter Detailansicht eines Termins (nach Klick auf das + zu Beginn der betreffenden Zeile) wird am unteren Rand ein Icon mit 3 Punkten angezeigt. Dort finden Sie die Möglichkeit, die Teilnehmer:innen vom gewählten Termin auszuschliessen.

![Das 3-Punkte-Menü am unteren Rand der Termin-Detailansicht enthält die Option "Teilnehmer ausschliessen"](assets/events_and_absences_tab_events_exclude_participants_v1_de.png){ class="shadow lightbox" title="Detailansicht eines Termins" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)


---


## Tab Teilnehmer:innen {: #tab_participants}

Im Tab "Teilnehmer:innen" erhalten Sie eine Übersicht über alle Teilnehmer:innen des Kurses oder der ausgewählten Gruppen. (Ohne Besitzer:innen und Betreuer:innen, sofern diese nicht zusätzlich in der Rolle Teilnehmer:in eingetragen sind.) Über den Button "Drucken" kann die Liste gedruckt werden.

![Die Teilnehmerliste zeigt je Person Erstzulassung, Einheiten, Anwesend, Unentschuldigt, Entschuldigt, Dispensiert und den farbigen Fortschrittsbalken](assets/Termine_Tab_TN_20.png){ class="shadow lightbox" title="Tab Teilnehmer:innen in der Kurs-Administration" }

**Erstzulassung**<br>
Mit der Erstzulassung wird definiert, wann der Teilnehmende mit dem Kurs begonnen hat.

**Einheiten**<br>
Hier wird die maximale Anzahl von Einheiten, die eine Person erreichen kann, angezeigt, unabhängig davon, ob der Termin schon stattgefunden hat oder nicht.

**Anwesend**<br>
Hier wird angezeigt, an wie vielen Einheiten die Person anwesend war. Berücksichtigt wird dabei die Anzahl der abgeschlossenen (erledigten) Absenzen.


**Unentschuldigt**<br>
Einheiten, bei denen die Person als unentschuldigt gekennzeichnet wurde.

**Entschuldigt**<br>
Einheiten, bei denen die Person als entschuldigt gekennzeichnet wurde. Der Grund kann angegeben werden.

**Dispensiert**<br>
Einheiten, für die die Person dispensiert wurde. Ob Dispensen als anwesend gezählt werden, legt die Konfiguration des Absenzenmanagements fest.

**Fortschritt**<br>
Im Fortschritt wird die Anwesenheit grafisch dargestellt. Grün symbolisiert die Anwesenheit, orange entschuldigte, rot abwesende bzw. unentschuldigte und blau dispensierte Einheiten.

:o_icon_o_midwarn:<br>
In der Achtungsspalte mit diesem Symbol wird angezeigt, ob die definierte Anwesenheitsquote erreicht worden ist. Das rote Symbol :o_icon_o_icon_error: bedeutet, dass die Quote unter dem erforderlichen Limit liegt. Das Warnsymbol :o_icon_o_icon_warning: erscheint, wenn die Quote weniger als fünf Prozentpunkte über dem Limit liegt.

:fontawesome-solid-circle-info:<br>
In der Infospalte werden Informationen angezeigt, welche von der Standardeinstellung abweichen. Dies ist beispielsweise ein persönlicher Schwellwert oder ein späterer Kursstart. Diese beiden Optionen können in den Einstellungen (Stift) definiert werden. Der persönliche Schwellwert definiert die zu erreichende Anwesenheitsquote für die betreffende Person.

Wenn Änderungen nicht sofort sichtbar sind, loggen Sie sich bitte aus und wieder ein. 

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Schwellwert für Präsenzpflicht individuell anpassen {: #personal_rate}

Der für den Kurs generell eingestellte Schwellwert für die Anwesenheitspflicht kann individuell angepasst werden. Wählen Sie dazu im Tab "Teilnehmer:innen" die betreffende Person und klicken Sie auf das Icon zum Bearbeiten.

![Im Dialog "Teilnehmer:innen-Schwellwert bearbeiten" werden der persönliche Schwellwert und die Erstzulassung einer Person angepasst; der Kursschwellwert wird angezeigt](assets/events_and_absences_tab_participants_personal_rate_v1_de.png){ class="shadow lightbox" title="Dialog Teilnehmer:innen-Schwellwert bearbeiten" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


## Tab Rekurse {: #tab_appeals}

Wurden Rekurse eingereicht, können Sie sich als Kursbesitzer:in unter diesem Tab einen Überblick verschaffen. Filter helfen Ihnen bei einer grösseren Anzahl von Rekursen.

![Der Tab "Rekurse" listet eingereichte Rekurse und bietet einen Filter nach Pendent, Angenommen und Abgelehnt](assets/events_and_absences_tab_appeals1_v1_de.png){ class="shadow lightbox" title="Tab Rekurse in der Kurs-Administration" }

Die Bearbeitung der Rekurse erfolgt in der Regel durch Absenzenverwalter:innen, die kursübergreifend alle Rekurse in der zentralen [kursübergreifenden Absenzenverwaltung](../area_modules/Absence_Management.de.md) abrufen können. 

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Persönliche Absenzen >](../personal_menu/Absences.de.md)<br>
[Erfassung und Verwaltung der Absenzen in einem Kurs durch Betreuer:innen >](../learningresources/Toolbar_Events.de.md)<br>
[Course Planner: Termine >](../area_modules/Course_Planner_Events.de.md)<br>
[Safe Exam Browser >](../../manual_how-to/SEB/SEB.de.md)<br>
[Prüfungsverwaltung: Prüfungsmodus >](../learningresources/Assessment_mode.de.md)<br>
[Kursübergreifende Absenzenverwaltung durch Absenzenverwalter:innen >](../area_modules/Absence_Management.de.md)

**Weiterführend**<br>
[Basiskonzept Termine und Absenzen >](../basic_concepts/Events_and_Absences.de.md)<br>
[Aktivierung und Konfiguration des Absenzenmanagements durch Administrator:innen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Konfiguration der Absenzenverwaltung in einem Kurs >](../learningresources/Course_Settings_Execution.de.md)<br>
[Kursübergreifende Absenzenerfassung im Coachingtool >](../area_modules/Coaching.de.md)<br>
[Modul Räume (Admin) >](../../manual_admin/administration/Modules_Rooms.de.md)

[Zum Seitenanfang ^](#course_admin_events_and_absences)

