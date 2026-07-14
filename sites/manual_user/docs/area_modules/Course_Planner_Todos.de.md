# Course Planner: To-dos [:octicons-tag-16:{ title="ab Release 21.0 (OO-9417)" }](https://track.frentix.com/issue/OO-9417){:target="_blank"} {: #course_planner_todos}

Im Course Planner lassen sich Aufgaben (To-dos) auf verschiedenen Ebenen erfassen: in der Übersicht, auf dem Produkt, auf der Durchführung und auf jedem einzelnen Element. Alle To-dos sind zentral in einer Übersicht einsehbar, ohne einzelne Durchführungen oder Elemente öffnen zu müssen. Ein Widget auf dem Dashboard zeigt offene und überfällige To-dos auf einen Blick.


[Zum Seitenanfang ^](#course_planner_todos)

---


## Tab «To-dos» auf einem Element {: #element_tab_todos}

Jedes Element im Course Planner verfügt über einen Tab **«To-dos»**. Dort erstellen, bearbeiten und verwalten Sie Aufgaben, die direkt diesem Element zugeordnet sind.


### Berechtigungen {: #todo_permissions}

* **Kursplaner:innen** und **Elementbesitzer:innen** können To-dos erstellen, bearbeiten, zuweisen und delegieren.
* **Kursbesitzer:innen** können To-dos, die ihrem Kurs zugeordnet sind, als erledigt markieren; sie können sie aber nicht erstellen oder anderweitig bearbeiten.
* **Principals** können To-dos einsehen aber nicht bearbeiten.

### Erstellen eines To-dos {: #create_todo}

Im Tab «To-dos» eines Elements klicken Sie auf **«To-do erstellen»**. Der nachfolgende Dialog enthält folgende Felder:

* **Titel** (Pflichtfeld): Bezeichnet die Aufgabe.
* **Zugewiesen** (Pflichtfeld): Die Person, die für die Erledigung verantwortlich ist.
* **Delegiert**: Die Ausführung kann an eine andere Person delegiert werden; die Verantwortung bleibt bei der zugewiesenen Person.
* **Status**: Setzt den aktuellen Bearbeitungsstand (Offen, In Bearbeitung, Erledigt).
* **Priorität**: Dringend, Hoch, Mittel oder Tief.
* **Startdatum** und **Fälligkeitsdatum**: Absolut oder [relativ zum Durchführungszeitraum](#relative_date).
* **Tags**: Frei vergebbare Schlagwörter.
* **Beschreibung**: Ergänzende Informationen zur Aufgabe.

Wählen Sie **«Starten»**, um ein To-do direkt auf den Status «In Bearbeitung» zu setzen. Mit **«Als erledigt markieren»** schliessen Sie es ab, ohne es separat zu öffnen.

!!! info "Aktionsmenu"
    Über das Aktionsmenü (3-Punkte-Symbol) einer To-do-Zeile stehen **Bearbeiten**, **Duplizieren** und **Löschen** zur Verfügung. Mit **Duplizieren** kopieren Sie ein bestehendes To-do samt seinen Eigenschaften. Diese Aktionen setzen Bearbeitungsrechte voraus.


#### Übersicht der To-do-Status {: #todo_status}

| Status | Bedeutung |
|---|---|
| Offen | Die Aufgabe ist erstellt, aber noch nicht begonnen. |
| In Bearbeitung | Die Arbeit an der Aufgabe hat begonnen. |
| Erledigt | Die Aufgabe ist abgeschlossen. |
| Gelöscht | Das To-do wurde gelöscht und ist nur noch im Filter «Gelöscht» sichtbar. |



[Zum Seitenanfang ^](#course_planner_todos)

---


## Zentrale To-do-Übersicht [:octicons-tag-16:{ title="ab Release 21.0 (OO-9418)" }](https://track.frentix.com/issue/OO-9418){:target="_blank"} {: #central_overview}

Die zentrale To-do-Übersicht fasst alle To-dos über alle Produkte und Elemente hinweg in einer Tabelle zusammen. Sie öffnen sie über den Launcher **«To-dos»** in der Launcher-Gruppe **«Produktivität»** auf dem CPL-Dashboard.

Die Übersicht zeigt alle To-dos, für die Sie zugewiesen oder delegiert sind, sowie alle To-dos in Produkten, auf die Sie Zugriff haben.


### Vordefinierte Filter {: #predefined_filters}

Mit den Schnellfiltern grenzen Sie die Ansicht thematisch ein:

| Filter | Zeigt |
|---|---|
| Alle | Alle sichtbaren To-dos |
| Meine To-dos | To-dos, bei denen Sie als «Zugewiesen» eingetragen sind |
| Offen | To-dos mit Status «Offen» |
| Überfällig | To-dos, deren Fälligkeitsdatum überschritten ist |
| Nicht zugewiesen | To-dos ohne zugewiesene Person |
| Erledigt | To-dos mit Status «Erledigt» |
| Gelöscht | Gelöschte To-dos |


### Tabellenspalten {: #table_columns}

Über das Zahnrad-Symbol wählen Sie, welche Spalten angezeigt werden. Standardmässig eingeblendet:

* **Titel** (bei neuen To-dos mit Markierung «Neu»)
* **Produkt** (das zugehörige Produkt)
* **Element** (das zugehörige Element innerhalb des Produkts)
* **Priorität**
* **Fälligkeit**
* **Status**
* **Zugewiesen**
* **Delegiert**
* **Tags**

Optional einblendbar: Zeitaufwand, Startdatum, Erledigt-Datum, Erstellt, Erstellt von, Geändert, Gelöscht, Gelöscht von.


### Sammelaktionen {: #bulk_actions}

Aktivieren Sie die Checkbox in der ersten Spalte, um einzelne To-dos zu markieren, oder wählen Sie über die Checkbox im Tabellenkopf alle To-dos der aktuellen Ansicht auf einmal aus. Sobald mindestens ein To-do markiert ist, erscheint in der Aktionsleiste die Sammelaktion **«Löschen»**.

Nach einer Sicherheitsabfrage werden die markierten To-dos gelöscht. Gelöschte To-dos sind nicht endgültig entfernt: Sie erhalten den Status «Gelöscht» und bleiben über den Filter **«Gelöscht»** einsehbar. In der Ansicht «Gelöscht» steht die Sammelaktion selbst nicht zur Verfügung.


[Zum Seitenanfang ^](#course_planner_todos)

---


## To-dos direkt für mehrere Durchführungen erstellen[:octicons-tag-16:{ title="ab Release 21.0 (OO-9539)" }](https://track.frentix.com/issue/OO-9539){:target="_blank"} {: #bulk_create}

In der Durchführungsübersicht sowie im Tab «Durchführungen» eines Produkts können Sie über eine Sammelaktion gleichzeitig ein To-do für mehrere Durchführungen erstellen.

1. Wählen Sie in der Durchführungsübersicht die gewünschten Durchführungen aus (Checkbox in der ersten Spalte).
2. Klicken Sie in der Aktionsleiste auf **«To-do erstellen»**.
3. Füllen Sie den Dialog aus. Der Kontext (Produkt und Element) wird automatisch aus der gewählten Durchführung gesetzt und ist nicht editierbar.

!!! info "Wichtig"
    Die Auswahlfelder «Zugewiesen» und «Delegiert» zeigen ausschliesslich Personen, die in den betreffenden und gewählten Durchführungen zugriffsberechtigt sind.


[Zum Seitenanfang ^](#course_planner_todos)

---


## Relatives Fälligkeitsdatum [:octicons-tag-16:{ title="ab Release 21.0 (OO-9425)" }](https://track.frentix.com/issue/OO-9425){:target="_blank"} {: #relative_date}

Beim Erstellen oder Bearbeiten eines To-dos im Course Planner können Fälligkeits- und Startdatum entweder **absolut** (ein festes Kalenderdatum) oder **relativ** (bezogen auf den Durchführungszeitraum) festgelegt werden.


### Relatives Datum konfigurieren {: #configure_relative_date}

Wählen Sie unter **Fälligkeitsdatum** die Option **«Relativ»**. Im Popover legen Sie fest:

* **Bezugsdatum**: «Beginn des Durchführungszeitraums» oder «Ende des Durchführungszeitraums».
* **Mit Versatz** (optional): Aktivieren Sie diesen Schalter, um einen Abstand zum Bezugsdatum anzugeben.
  * **Versatz**: Anzahl der Einheiten (Tage, Wochen, Monate oder Jahre).
  * **Richtung**: «vor» oder «nach» dem Bezugsdatum.

Das berechnete Datum wird als Vorschau angezeigt, solange ein Durchführungszeitraum definiert ist. Ändert sich der Durchführungszeitraum nachträglich, passt sich das Fälligkeitsdatum automatisch an.

!!! info "Wichtig"
    Relatives Datum steht nur im Course Planner zur Verfügung. Im persönlichen Menü und in anderen Kontexten (Projekt, Kurs) sind nur absolute Daten möglich.


[Zum Seitenanfang ^](#course_planner_todos)

---


## To-do-Widget [:octicons-tag-16:{ title="ab Release 21.0 (OO-9422)" }](https://track.frentix.com/issue/OO-9422){:target="_blank"} {: #todo_widget}

Das **To-do**-Widget auf dem CPL-Dashboard zeigt auf einen Blick, welche Aufgaben Ihre unmittelbare Aufmerksamkeit erfordern.

Das Widget zeigt To-dos, bei denen Sie als **«Zugewiesen»** eingetragen sind, aufgeteilt nach:

Für jedes To-do werden Titel, Priorität und Fälligkeitsdatum angezeigt. Ein Klick auf den Titel öffnet das To-do direkt.

!!! note "Dashboard Konfiguration"
    Das Widget kann wie alle CPL-Dashboard-Widgets über die Dashboard-Konfiguration ein- und ausgeblendet werden.


[Zum Seitenanfang ^](#course_planner_todos)

---


## Weitere Informationen {: #further_information}

[Course Planner: Übersicht >](Course_Planner.de.md)<br>
[Course Planner: Durchführungen >](Course_Planner_Implementations.de.md)<br>
[To-dos (persönliches Menü) >](../personal_menu/To-Dos.de.md)<br>
[Allgemeines zu To-dos >](../basic_concepts/To_Dos_Basics.de.md)<br>
[Course Planner aktivieren (Admin) >](../../manual_admin/administration/Modules_Course_Planner.de.md)<br>

[Zum Seitenanfang ^](#course_planner_todos)
