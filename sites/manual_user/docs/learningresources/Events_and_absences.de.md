# Termine und Absenzen {: #course_admin_events_and_absences}

Mit den Terminen und Absenzen führen Sie Anwesenheitslisten online und dokumentieren Fehlzeiten. Die Anwesenheit erfassen Sie immer innerhalb eines Kurses.

Dazu legen Sie im Kurs Termine an und teilen jeden Termin in Einheiten. Ein Vormittag ist zum Beispiel ein Termin mit vier Einheiten zu je einer Stunde. Fehlt eine Person nur eine Stunde, erfassen Sie die Absenz für diese eine Einheit und nicht für den ganzen Termin.

Die Termine legen Kursbesitzer:innen selbst an, oder sie kommen aus einem externen Verwaltungssystem Ihrer Organisation. Im Kurskalender erscheinen die Termine, wenn für den Kurs "Kurs Kalender synchronisieren" eingeschaltet ist: [Kurseinstellungen - Tab Durchführung](../learningresources/Course_Settings_Execution.de.md#course_calendar_sync).

Damit Sie Termine und Absenzen im Kurs nutzen können, schalten Sie als Kursbesitzer:in die "Termin- und Absenzenverwaltung" ein:<br>
`Kurs > Administration > Einstellungen > Tab Durchführung`<br>
Danach stehen dort weitere Einstellungen bereit, und in der Kurs-Toolbar erscheint das Icon "Termine".


## "Termine" in der Toolbar {: #toolbar_events}

Als Kursbesitzer:in legen Sie hier Termine an und verwalten die Absenzen. Dieselben Möglichkeiten finden Sie weitgehend auch im Menü Administration des Kurses:<br>
`Kurs > Administration > Termine und Absenzen`

![Menüeintrag "Termine und Absenzen" öffnet die Termin- und Absenzenverwaltung für Kursbesitzer:innen](assets/events_and_absences_adminmenu_v2_de.png){ class="shadow lightbox" title="Menü Administration eines Kurses · 2026.10.09" }

Als Betreuer:in öffnen Sie die Termine nur über das Icon "Termine" in der Toolbar; im Menü Administration fehlt der Eintrag "Termine und Absenzen". Neue Termine legen Sie nicht an. Sie sehen die vorhandenen Termine und erfassen, sofern im Kurs eingeschaltet, die Absenzen. Mit "Zeigt nur meine" sehen Sie nur die Termine, bei denen Sie als Dozent:in eingetragen sind.

![Betreuer:innen erreichen die Termine nur über das Toolbar-Icon "Termine"; das Menü Administration enthält für sie keinen Eintrag "Termine und Absenzen"](assets/events_and_absences_toolbar_for_coach_v2_de.png){ class="shadow lightbox" title="Kurs-Toolbar in der Sicht der Betreuer:innen · 2026.10.09" }

Teilnehmende öffnen über das Icon "Termine" in der Toolbar ihre Termine im Kurs, vor Ort wie online, etwa in einem Blended-Learning-Kurs.

![Teilnehmende öffnen über das Toolbar-Icon "Termine" die Terminliste des Kurses mit Datum, Zeit, Titel, Status, Ort und Dozenten](assets/events_and_absences_participant_v1_de.png){ class="shadow lightbox" title="Terminliste in der Sicht der Teilnehmenden · 2026.10.09" }

Ihre eigenen Fehlzeiten finden Teilnehmende in den persönlichen Werkzeugen im [Menü "Absenzen"](../personal_menu/Absences.de.md).

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

Die folgenden Abschnitte beschreiben die Ansicht der Kursbesitzer:innen.

## Tab Termine [:octicons-tag-16:{ title="ab Release 12.0 (OO-2636)" }](https://track.frentix.com/issue/OO-2636) {: #tab_events}

![Die Terminverwaltung für Kursbesitzer:innen mit den Tabs Termine, Teilnehmer:innen und Rekurse und der aufgeklappten Detailansicht eines Termins](assets/events_and_absences_owner_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

### Termine anzeigen {: #display_events}

Im Tab "Termine" fügen Sie dem Kurs Termine hinzu und grenzen die Liste mit den Tabs und Filtern ein. Haben Sie Termine Fachbereichen (Taxonomie) zugeordnet, filtern Sie auch nach diesen. Die Details eines Termins klappen Sie mit dem + am Anfang seiner Zeile auf.

Im 3-Punkte-Menü am Ende jeder Zeile finden Sie die Aktionen zu einem Termin:

- **Bearbeiten** und "Kopieren"
- **Ändere in Online Meeting** oder "Ändere in vor Ort Termin", bei einem Termin mit Online Meeting zusätzlich "Online Meeting beitreten"
- **Als Prüfung markieren**, bei einem bereits markierten Termin stattdessen "Prüfung editieren" und "Prüfung löschen", siehe [Termin als Prüfung markieren](#mark_event_as_exam)
- **Absenzenliste** und "Präsenzliste" als PDF, "Log" und "Export" als Excel-Datei
- **Termin wiederöffnen** bei einem abgeschlossenen oder abgesagten Termin, siehe [Termine wiederöffnen](#reopen_events)
- **Löschen**

Wird der Kurs im Course Planner verwendet, fehlen Bearbeiten, Kopieren, die Umstellung auf ein Online Meeting oder einen vor Ort Termin und Löschen, weil die Termine im Course Planner verwaltet werden. Stammen die Termine aus einem externen Verwaltungssystem, können Bearbeiten und Löschen ebenfalls fehlen. Welche Einträge Betreuer:innen im selben Menü sehen, beschreibt die Seite zur Toolbar: [Menü am Zeilenende](../learningresources/Toolbar_Events.de.md#lists_and_export)

![Das 3-Punkte-Menü eines geplanten Termins bietet Bearbeiten, Kopieren, Ändere in Online Meeting, Als Prüfung markieren, Absenzen- und Präsenzliste, Log, Export und Löschen](assets/events_and_absences_event_menu_v1_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

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

In der Tabellenansicht steht zuoberst eine Titelzeile mit Titel und Kennzeichen des Termins, den Abzeichen "Status" und "Absenzen" und rechts der Aktion "Bearbeiten". In der Zeitansicht fehlt diese Zeile, weil der Kopf des Blocks dieselben Angaben zeigt; dort bearbeiten Sie den Termin über das 3-Punkte-Menü.

Darunter sehen Sie auf einer Zeile Datum, Zeit, Teilnehmer:innen und Präsenz. "Einheit" erscheint nur, wenn der Termin mehr als eine Einheit umfasst, "Ort" nur, wenn ein Ort erfasst ist.

Danach folgen die Dozent:innen als Personenkarten mit Visitenkarte, E-Mail und Chat. Ist niemand eingetragen, steht dort "Keine Dozenten verfügbar.".

Die übrigen Angaben erscheinen nur, wenn sie am Termin gepflegt sind:

* **Online Meeting**: "Online Meeting beitreten" als hervorgehobene Schaltfläche, dazu der Link auf eine hinterlegte Aufzeichnung.
* **Raum**: die Raumkarte unter dem Label "Raum", bei mehreren Räumen unter "Räume". Ist ein Raum im Zeitraum des Termins doppelt gebucht, steht die Warnung unterhalb der Raumkarte und die Karte erhält einen gelben Rand. [:octicons-tag-16:{ title="ab Release 21.0.2 (OO-9641)" }](https://track.frentix.com/issue/OO-9641){:target="_blank"}
* **Beschreibung** und "Vorbereitung/Nachbereitung" als eigene Absätze.

Zuunterst zeigt eine Tabelle, für wen der Termin gilt: eine Zeile pro Kurs, Gruppe oder Element des Course Planner, mit der Anzahl Teilnehmender und ob sie eingeschlossen oder ausgeschlossen sind. Wie Sie Teilnehmende ausnehmen, steht unter [Teilnehmer:innen ausschliessen](#exclude_participants).

![Aufgeklappter Termin mit Datum, Zeit, Ort, Präsenz, Raumkarte, Beschreibung, Vorbereitung und zuunterst der Tabelle, für wen der Termin gilt](assets/events_and_absences_timeline_v2_de.png){ class="shadow lightbox" title="Zeitansicht der Terminliste · 2026.10.09" }

Räume weisen Sie im Course Planner zu. Ein eigenständiger Kurs zeigt deshalb keine Raumkarten: [Räume für einen Termin belegen >](../area_modules/Course_Planner_Events.de.md#room_booking)

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termin erstellen/bearbeiten {: #edit_events}

Einen Termin legen Sie mit dem Button "Termin hinzufügen" rechts über der Liste im Tab "Termine" an.

![Button "Termin hinzufügen" rechts oben über der Terminliste](assets/events_and_absences_tab_events_create1_v2_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

!!! info "Wichtig"

    OpenOlat zeigt den Button "Termin hinzufügen" nur in einem eigenständigen Kurs. Die Verwendung des Kurses sehen Sie unter:<br>
    `Kurs > Administration > Einstellungen > Tab Freigabe > Abschnitt Verwendung`<br>
    Wird der Kurs im Course Planner verwendet, erstellen und verwalten Sie die Termine im Course Planner.

Im Dialog "Termin hinzufügen" erfassen Sie die Angaben zum Termin.

![Dialog mit den Pflichtfeldern Titel, Datum, Zeit und Einheit, dem eingeschalteten Online Meeting mit Sitzungs-Link und dem Schalter Präsenz](assets/events_and_absences_tab_events_create2_v4_de.png){ class="shadow lightbox" title="Dialog Termin hinzufügen · 2026.10.09" }

**Titel**: Vergeben Sie einen sinnvollen Namen.

**Kennzeichen**: Das optionale Kennzeichen unterscheidet Termine mit gleichem Titel.

**Datum**: Das Datum ist ein Pflichtfeld.

**Zeit**: Auch die Zeit ist ein Pflichtfeld, denn ohne Zeit zeigt zum Beispiel der Kalender den Termin nicht korrekt an.

**Einheit**: Hier legen Sie fest, wie viele (Zeit-)Einheiten der Termin umfasst, 1 bis 12.<br>
Beispiel: Ein Termin dauert 2 Stunden und ist in 4 thematische Einheiten gegliedert (4 x 0.5 Stunden).

!!! info "Wichtig"

    Stammen die Termine aus einem externen Verwaltungssystem, das sie nach OpenOlat synchronisiert, ist das Feld "Einheit" in OpenOlat gesperrt. Der Wert kommt aus diesem System, und Sie ändern ihn dort. Gesperrt ist das Feld ausserdem, sobald die Anwesenheitskontrolle des Termins abgeschlossen ist.

**Ort**: Hier geben Sie an, wo der Termin stattfindet, zum Beispiel den Präsenzort oder die genaue Zimmerbezeichnung.

**Online Meeting**: Soll der Termin online stattfinden, schalten Sie "Online Meeting" ein. Zur Auswahl stehen BigBlueButton, Microsoft Teams und "Sitzungs-Link". Der Sitzungs-Link deckt weitere Anbieter ab, zum Beispiel Zoom. Geben Sie dafür den "Name des Sitzungsanbieters" und die "URL für Sitzungsteilnahme" an.<br>
Das Online Meeting übernimmt Titel, Zeit und Personen aus dem Termin. Später öffnen Sie es in der Terminliste über "Online Meeting beitreten".
Teilnehmende erreichen es über den Kalender oder das Icon "Termine" in der Toolbar.

**URL für Aufzeichnung**: Hier hinterlegen Sie eine beliebige URL, unter der die Aufzeichnung des Meetings abrufbar ist. Das Feld steht auch zur Verfügung, wenn der Schalter "Online Meeting" ausgeschaltet ist.

**Fachbereiche**: Hier ordnen Sie den Termin einem oder mehreren Begriffen einer hinterlegten Taxonomie zu. So finden Sie den Termin schneller.

**Dozenten**: Wählen Sie die Kursbetreuer:innen, die den Termin leiten. Bei einem neuen Termin sind alle Kursbetreuer:innen vorgewählt. Nur die ausgewählten Kursbetreuer:innen können im Termin die Anwesenheit erfassen. (Als Dozent:in kann nur eine Person hinzugefügt werden, die auch die Rolle "Betreuer:in" besitzt.) Möchte ein:e Kursbesitzer:in ebenfalls diese Funktion übernehmen, muss sich diese Person zusätzlich als Kursbetreuer:in in den Kurs eintragen.

**Beschreibung**: Hier fügen Sie optional eine Beschreibung des Termins hinzu.

**Vorbereitung/Nachbereitung**: Hier geben Sie den Teilnehmenden einen Auftrag zur Vor- oder Nachbereitung des Termins. Der Kalender zeigt ihn, sofern die Termine mit dem Kurskalender synchronisiert werden:<br>
`Kurs > Administration > Einstellungen > Tab Durchführung`

**Präsenz**: Steht der Schalter auf "Aus", ist die Absenzenerfassung für den Termin ausgeschaltet.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine kopieren oder löschen {: #copy_delete_events}

Setzen Sie in der ersten Spalte ein Häkchen bei einem oder mehreren Terminen. Über der Liste erscheinen dann die Buttons "Kopieren" und "Löschen".<br>
Einen einzelnen Termin kopieren oder löschen Sie auch über das 3-Punkte-Menü am Ende seiner Zeile.

![Mit Häkchen bei einem Termin erscheinen über der Liste die Buttons "Kopieren" und "Löschen"; dieselben Optionen stehen im 3-Punkte-Menü am Ende der Zeile](assets/events_and_absences_tab_events_copy_v2_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

#### Einen oder mehrere Termine kopieren [:octicons-tag-16:{ title="ab Release 21.1.0 (OO-9744)" }](https://track.frentix.com/issue/OO-9744){:target="_blank"} {: #copy_events}

Findet derselbe Unterricht noch einmal statt, kopieren Sie den Termin und ändern danach nur noch Datum und Zeit. Die Kopie übernimmt die übrigen Angaben des Ausgangstermins. Sie kopieren Termine im Tab "Termine":<br>
`Kurs > Administration > Termine und Absenzen > Tab Termine`

**Einen Termin kopieren:** Wählen Sie im 3-Punkte-Menü des Termins "Kopieren". OpenOlat legt die Kopie noch nicht an, sondern öffnet den Dialog "Termin bearbeiten" mit allen übernommenen Angaben. Titel und Kennzeichen tragen den Zusatz "(Kopie)", Datum und Zeit sind noch die des Ausgangstermins. Passen Sie Datum und Zeit an und klicken Sie auf "Speichern". Erst dann entsteht der neue Termin; mit "Abbrechen" entsteht keiner. Gleich verhält sich der Button "Kopieren" über der Liste, wenn Sie genau einen Termin mit einem Häkchen ausgewählt haben.

![Der Dialog Termin bearbeiten einer Kopie: Titel und Kennzeichen mit dem Zusatz (Kopie), alle übrigen Angaben vom Ausgangstermin übernommen, Datum und Zeit noch unverändert](assets/events_and_absences_copy_event_dialog_v1_de.png){ class="shadow lightbox" title="Dialog Termin bearbeiten einer Kopie · 2026.10.21" }

**Mehrere Termine kopieren:** Setzen Sie bei den Terminen ein Häkchen und klicken Sie über der Liste auf "Kopieren". OpenOlat legt die Kopien sofort an, ohne Dialog. Jede Kopie liegt auf demselben Datum und zur selben Zeit wie ihr Ausgangstermin. Öffnen Sie danach jede Kopie mit "Bearbeiten" und datieren Sie sie um.

Die Kopie übernimmt vom Ausgangstermin:

- **Titel** und "Kennzeichen", je mit dem Zusatz "(Kopie)". Hat der Ausgangstermin kein Kennzeichen, bleibt das Feld leer.
- **Datum**, "Zeit" und "Einheit"
- **Ort** und "URL für Aufzeichnung"
- **Online Meeting**: Einen Sitzungs-Link übernimmt die Kopie mit Anbietername und URL. Bei BigBlueButton und Microsoft Teams erhält die Kopie ein eigenes Meeting mit denselben Einstellungen. So treffen sich die Teilnehmenden zweier Termine nicht im selben Meeting.
- **Fachbereiche**
- **Dozenten**: dieselben Dozent:innen wie der Ausgangstermin. Hat der Ausgangstermin keine Dozent:innen, bleibt auch die Kopie ohne. Anders als bei einem neuen Termin sind dann nicht alle Kursbetreuer:innen vorgewählt.
- **Beschreibung**, "Vorbereitung/Nachbereitung" und "Präsenz"
- **Räume**, wenn der Termin im Course Planner geplant wird und das Modul "Räume" aktiviert ist: [Termine kopieren im Course Planner](../area_modules/Course_Planner_Events.de.md#copy_events)

Nicht übernommen werden die erfassten Absenzen. Die Anwesenheitskontrolle der Kopie ist offen, auch wenn sie beim Ausgangstermin bereits abgeschlossen war.

!!! warning "Nach dem Kopieren mehrerer Termine: Teilnehmende einschliessen"

    Kopieren Sie mehrere Termine auf einmal, zeigt die Spalte "Teilnehmer:innen" bei den Kopien 0. In der Detailansicht einer Kopie steht der Kurs in der Tabelle zuunterst mit dem Status "Ausgeschlossen". Damit die Teilnehmenden zum Termin gehören, wählen Sie dort im 3-Punkte-Menü "Teilnehmer wieder einschliessen", siehe [Teilnehmer:innen ausschliessen](#exclude_participants). Eine Kopie, die Sie im Dialog "Termin bearbeiten" speichern, gilt gleich für die Teilnehmenden des Kurses.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine importieren [:octicons-tag-16:{ title="ab Release 13.0 (OO-3666)" }](https://track.frentix.com/issue/OO-3666){:target="_blank"} {: #import_events}

Viele Termine auf einmal erfassen Sie schneller mit einer Excel-Datei als einzeln im Dialog. Klicken Sie dazu im Tab "Termine" auf den kleinen Pfeil neben dem Button "Termin hinzufügen" und wählen Sie "Termine importieren". Den Pfeil gibt es nur zusammen mit dem Button, also in einem eigenständigen Kurs. Wird der Kurs im Course Planner verwendet, importieren Sie die Termine dort: [Neue Termine im Course Planner erstellen](../area_modules/Course_Planner_Events.de.md#create_events)

Der Assistent "Termine aus Excel importieren" bietet im Schritt "Dateneingabe" den Link "Vorlage Excelimport" zum Herunterladen. Die Vorlage ist eine Excel-Tabelle mit den Spalten in der Reihenfolge, die der Import verlangt. Die Kopfzeile ist englisch. Mit einem Stern markiert sind "External ID", "Title", "Lectures", "Date", "Start", "End", "Compulsory", "Teacher" und "Participants", danach folgen "Location", "Description", "Preparation" und "Comment". Drei Beispieltermine zeigen, wie Sie Dozent:innen über E-Mail-Adresse, Anmeldename oder Institutionsnummer angeben und Teilnehmende aus dem Kurs, aus einer Gruppe oder aus einem Element des Course Planner übernehmen.

Kopieren Sie die ausgefüllten Zeilen ohne die Kopfzeile aus der Excel-Datei in das Feld "Kopierte Zeilen aus Exceldatei (Kommasepariert)". Eine Zeile ohne Eintrag in "Participants" und in den Spalten danach übergeht der Import ohne Meldung. Trägt eine Zeile die External ID eines bestehenden Termins, aktualisiert der Import diesen Termin, statt einen neuen anzulegen. Im Schritt "Übersicht" sehen Sie die Termine, bevor OpenOlat sie speichert.

![Der kleine Pfeil neben dem Button "Termin hinzufügen" öffnet die Option "Termine importieren"](assets/events_and_absences_tab_events_import_v2_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Termin als Prüfung markieren [:octicons-tag-16:{ title="ab Release 14.0 (OO-4045)" }](https://track.frentix.com/issue/OO-4045) {: #mark_event_as_exam}

Findet ein Termin als Prüfung statt, markieren Sie ihn über "Als Prüfung markieren" im 3-Punkte-Menü. OpenOlat legt dafür einen Prüfungsmodus an, der Datum, Zeit und Teilnehmende aus dem Termin übernimmt. Im folgenden Dialog wählen Sie die Kursbausteine der Prüfung und schalten bei Bedarf den [Safe Exam Browser](../../manual_how-to/SEB/SEB.de.md) ein: [Prüfungsmodus aus einem Termin](../learningresources/Assessment_mode.de.md#exam_from_event)

![Eintrag "Als Prüfung markieren" im 3-Punkte-Menü am Ende der Terminzeile](assets/events_and_absences_tab_events_mark_as_exam_v2_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

Nach dem Speichern zeigt die Spalte "Prüfung" ein Symbol, und das 3-Punkte-Menü bietet "Prüfung editieren" und "Prüfung löschen". Die Prüfung erscheint zudem in der Prüfungsverwaltung des Kurses unter `Kurs > Administration > Prüfungsverwaltung`.

![Symbol in der Spalte Prüfung und die Einträge Prüfung editieren und Prüfung löschen im 3-Punkte-Menü](assets/events_and_absences_tab_events_exam_marked_v2_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

Denselben Eintrag haben Betreuer:innen in der Toolbar. Wer ihn ausserdem nutzen kann und warum er fehlen kann, beschreibt die Seite zur Toolbar: [Wenn "Als Prüfung markieren" fehlt](../learningresources/Toolbar_Events.de.md#mark_as_exam_missing)

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine absagen {: #cancel_events}

Termine sagen Sie über das [Icon "Termine" in der Toolbar](../learningresources/Toolbar_Events.de.md#cancel_events) ab.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Termine abschliessen {: #close_events}

Termine schliessen Sie über das [Icon "Termine" in der Toolbar](../learningresources/Toolbar_Events.de.md#close_events) ab.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Termine wiederöffnen [:octicons-tag-16:{ title="ab Release 13.0 (OO-3716)" }](https://track.frentix.com/issue/OO-3716){:target="_blank"} {: #reopen_events}

Als Kursbesitzer:in öffnen Sie einen abgeschlossenen Termin wieder: Wählen Sie im 3-Punkte-Menü seiner Zeile "Termin wiederöffnen".

Alternativ öffnen Sie mit dem Buch-Symbol ("Absenz editieren") die Absenzenerfassung und klicken dort auf "Termin wiederöffnen".

![Das Buch-Symbol "Absenz editieren" öffnet die Absenzenerfassung; der Button "Termin wiederöffnen" öffnet den abgeschlossenen Termin erneut](assets/events_and_absences_reopen_event2_v1_de.png){ class="shadow lightbox" title="Absenzenerfassung eines Termins · 2026.10.09" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---

### Dozent:innen verwalten [:octicons-tag-16:{ title="ab Release 20.0.3 (OO-8622)" }](https://track.frentix.com/issue/OO-8622) {: #manage_teachers}

Setzen Sie in der ersten Spalte ein Häkchen bei einem oder mehreren Terminen. Über der Liste erscheint dann der Button "Dozent:innen verwalten". Im gleichnamigen Dialog weisen Sie Dozent:innen mit einem Häkchen einzelnen Terminen zu, oder mit "Zu allen Terminen zuweisen" und "Von allen Terminen entfernen" allen gewählten Terminen auf einmal.

![Mit Häkchen bei Terminen erscheint über der Terminliste der Button "Dozent:innen verwalten" neben den Buttons "Kopieren" und "Löschen"](assets/events_and_absences_tab_events_teachers1_v2_de.png){ class="shadow lightbox" title="Tab Termine in der Kurs-Administration · 2026.10.09" }

![Im Dialog "Dozent:innen verwalten" werden Dozent:innen per Häkchen einzelnen Terminen oder über die Buttons allen Terminen zugewiesen oder entzogen](assets/events_and_absences_tab_events_teachers2_v2_de.png){ class="shadow lightbox" title="Dialog Dozent:innen verwalten · 2026.10.09" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Teilnehmer:innen ausschliessen {: #exclude_participants}

Soll eine Gruppe von Teilnehmenden nicht an einem Termin teilnehmen, nehmen Sie sie von diesem Termin aus. Öffnen Sie dazu die Detailansicht des Termins (Klick auf das + am Anfang der Zeile). In der Tabelle zuunterst steht eine Zeile pro Kurs, Gruppe oder Element. Öffnen Sie das 3-Punkte-Menü am Ende der Zeile und wählen Sie "Teilnehmer ausschliessen". Die Spalte "Status" zeigt danach "Ausgeschlossen"; mit "Teilnehmer wieder einschliessen" im selben Menü nehmen Sie die Teilnehmenden wieder auf.

![Das 3-Punkte-Menü am unteren Rand der Termin-Detailansicht enthält die Option "Teilnehmer ausschliessen"](assets/events_and_absences_tab_events_exclude_participants_v2_de.png){ class="shadow lightbox" title="Detailansicht eines Termins · 2026.10.09" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)


---


## Tab Teilnehmer:innen {: #tab_participants}

Im Tab "Teilnehmer:innen" sehen Sie auf einen Blick, wie es um die Anwesenheit aller Teilnehmer:innen des Kurses oder der ausgewählten Gruppen steht. Besitzer:innen und Betreuer:innen erscheinen nur, wenn sie zusätzlich in der Rolle Teilnehmer:in eingetragen sind. Mit dem Button "Drucken" drucken Sie die Liste.

![Die Teilnehmerliste zeigt je Person Erstzulassung, Einheiten, Anwesend, Unentschuldigt, Entschuldigt, Dispensiert, den farbigen Fortschrittsbalken und die Anwesenheit in Prozent](assets/events_and_absences_tab_participants_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen in der Kurs-Administration · 2026.10.09" }

**Erstzulassung**<br>
Die Erstzulassung legt fest, wann die Person mit dem Kurs begonnen hat.

**Einheiten**<br>
Die maximale Anzahl Einheiten, die eine Person erreichen kann, unabhängig davon, ob der Termin schon stattgefunden hat.

**Anwesend**<br>
Die Anzahl Einheiten, an denen die Person anwesend war. OpenOlat berücksichtigt dabei die abgeschlossenen (erledigten) Absenzen.


**Unentschuldigt**<br>
Einheiten, bei denen die Person als unentschuldigt gekennzeichnet ist.

**Entschuldigt**<br>
Einheiten, bei denen die Person als entschuldigt gekennzeichnet ist. Ein Grund lässt sich angeben.

**Dispensiert**<br>
Einheiten, für die die Person dispensiert ist. Ob Dispense als anwesend zählen, legen Administrator:innen in der System-Administration mit der Option "Dispense als anwesend zählen" fest:<br>
`Administration > Module > Termine / Absenzen > Tab Konfiguration`

**Fortschritt**<br>
Der Balken zeigt die Anwesenheit grafisch. Grün steht für anwesende, orange für entschuldigte, rot für abwesende bzw. unentschuldigte und blau für dispensierte Einheiten.

:o_icon_o_midwarn:<br>
Die Achtungsspalte mit diesem Symbol zeigt, ob die festgelegte Anwesenheitsquote erreicht ist. Das rote Symbol :o_icon_o_icon_error: bedeutet, dass die Quote unter dem erforderlichen Limit liegt. Das Warnsymbol :o_icon_o_icon_warning: erscheint, wenn die Quote weniger als fünf Prozentpunkte über dem Limit liegt.

**Anwesenheit**<br>
Die Anwesenheitsquote der Person in Prozent. Die Spalte erscheint zusammen mit der Achtungsspalte, wenn für den Kurs die Anwesenheitsquote berechnet wird.

:fontawesome-solid-circle-info:<br>
Die Infospalte zeigt Angaben, die von der Standardeinstellung abweichen, zum Beispiel einen persönlichen Schwellwert oder einen späteren Kursstart. Beide legen Sie mit dem Stift in der Zeile der Person fest. Der persönliche Schwellwert ist die Anwesenheitsquote, die diese Person erreichen muss.

Wenn Änderungen nicht sofort sichtbar sind, loggen Sie sich bitte aus und wieder ein.

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


### Schwellwert für Präsenzpflicht individuell anpassen {: #personal_rate}

Gilt für eine Person eine andere Anwesenheitspflicht als für den Kurs, passen Sie den Schwellwert für sie an. Wählen Sie dazu im Tab "Teilnehmer:innen" die betreffende Person und klicken Sie auf das Icon zum Bearbeiten.

![Im Dialog "Teilnehmer:innen-Schwellwert bearbeiten" werden der persönliche Schwellwert und die Erstzulassung einer Person angepasst; der Kursschwellwert wird angezeigt](assets/events_and_absences_tab_participants_personal_rate_v2_de.png){ class="shadow lightbox" title="Dialog Teilnehmer:innen-Schwellwert bearbeiten · 2026.10.09" }

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


## Tab Rekurse {: #tab_appeals}

Halten Teilnehmende eine erfasste Absenz für falsch, reichen sie einen Rekurs ein. Im Tab "Rekurse" sehen Sie als Kursbesitzer:in diese Rekurse. Bei vielen Rekursen zeigen Sie mit dem Filter rechts über der Liste nur die pendenten, angenommenen oder abgelehnten an.

![Der Tab "Rekurse" listet eingereichte Rekurse und bietet einen Filter nach Pendent, Angenommen und Abgelehnt](assets/events_and_absences_tab_appeals1_v2_de.png){ class="shadow lightbox" title="Tab Rekurse in der Kurs-Administration · 2026.10.09" }

In der Regel bearbeiten Absenzenverwalter:innen die Rekurse, und zwar für alle Kurse gemeinsam in der [Absenzenverwaltung](../area_modules/Absence_Management.de.md).

[Zum Seitenanfang ^](#course_admin_events_and_absences)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kurseinstellungen - Tab Durchführung >](../learningresources/Course_Settings_Execution.de.md)<br>
[Persönliche Werkzeuge: Absenzen >](../personal_menu/Absences.de.md)<br>
[Toolbar: Termine >](../learningresources/Toolbar_Events.de.md)<br>
[Course Planner: Termine >](../area_modules/Course_Planner_Events.de.md)<br>
[Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor? >](../../manual_how-to/SEB/SEB.de.md)<br>
[Prüfungsverwaltung: Prüfungsmodus >](../learningresources/Assessment_mode.de.md)<br>
[Absenzenverwaltung >](../area_modules/Absence_Management.de.md)

**Weiterführend**<br>
[Termine und Absenzen (Basiskonzept) >](../basic_concepts/Events_and_Absences.de.md)<br>
[Modul Termine und Absenzen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Coaching - Übersicht >](../area_modules/Coaching.de.md)<br>
[Coaching - Termine und Absenzen >](../area_modules/Coaching_Events_Absences.de.md)<br>
[Modul Räume >](../../manual_admin/administration/Modules_Rooms.de.md)

[Zum Seitenanfang ^](#course_admin_events_and_absences)

