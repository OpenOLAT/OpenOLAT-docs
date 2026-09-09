# Modul Termine und Absenzen {: #module_events_and_absences}


Bevor das Modul "Termine und Absenzen" genutzt werden kann, muss es in der System-Administration aktiviert werden. **Administrator:innen** finden die Konfiguration unter:<br>
`Administration > Module > Termine / Absenzen`

!!! tip "Aktivierung"

    Kunden von frentix kontaktieren für die Aktivierung bitte [contact@frentix.com](mailto:contact@frentix.com). Sobald das Modul "Termine und Absenzen" aktiviert ist, können diverse zusätzliche Einstellungen für die systemweite Konfiguration vorgenommen werden. Bei Systemen mit dem fx-Release werden diese Anpassung durch frentix vorgenommen.

    **Nicht Hosting-Kunde von frentix?** Fragen Sie Ihren Systembetreiber!


[Zum Seitenanfang ^](#module_events_and_absences)

---

## Tab Konfiguration [:octicons-tag-16:{ title="ab Release 12.0 (OO-2636)" }](https://track.frentix.com/issue/OO-2636)

![Modul-Toggle und Absenzen-Option auf oberster Ebene, darunter Konfiguration auf Kursebene mit den Auswahlkarten Schreibgeschützt und Überschreibbar. Tab Konfiguration, Seite Termine / Absenzen.](assets/modules_events_and_absences_config_course_level_v3_de.png){ class="shadow lightbox" }

Die obersten zwei Optionen gelten für das ganze System. Sie stehen ausserhalb der Sektion "Konfiguration auf Kursebene".

**Modul "Termin- und Absenzenverwaltung"**: Der Hauptschalter des Moduls. Steht er auf "aus", sind alle weiteren Optionen dieses Tabs ausgeblendet und Kurse können die Termin- und Absenzenverwaltung nicht einschalten.

**Absenzen / Abmeldungen / Dispensen einschalten**: Bewirkt, dass Betreuende unter `Coaching > Termine` das Tab "Meldungen" angezeigt bekommen.

### Konfiguration auf Kursebene [:octicons-tag-16:{ title="ab Release 20.3.8 / 21.0.2 (OO-9676)" }](https://track.frentix.com/issue/OO-9676)

Diese Sektion setzt die Vorgabewerte für alle Kurse. Die Option "Standardkonfiguration" bestimmt, ob Kursbesitzende diese Werte pro Kurs ändern dürfen.

#### Standardkonfiguration {: #default_configuration }

Die Auswahl erfolgt über zwei Auswahlkarten:

- **Schreibgeschützt**: "Die Konfiguration ist schreibgeschützt und kann nicht geändert werden." Kurse übernehmen die hier gesetzten Vorgabewerte und können sie nicht ändern.
- **Überschreibbar**: "Die Konfiguration kann in den Kurseinstellungen überschrieben werden." Kursbesitzende dürfen die Vorgabewerte pro Kurs anpassen unter `Kurs > Administration > Einstellungen > Durchführung`.

Die Auswahl gilt nur für die nachfolgenden Optionen dieser Sektion. Die Werte der "Globalen Konfiguration" sind davon nicht betroffen und gelten immer systemweit.

#### Anwesenheitskontrolle einschalten {: #roll_call_enabled }

Nur mit dieser Option lässt sich eine Anwesenheitskontrolle durchführen. Dozierende sehen dann die Teilnehmenden und die Kontrollkästchen.

#### Berechnung der Anwesenheitsrate {: #attendance_rate_calculation }

Wenn diese Option eingeschaltet ist, wird eine Prozentquote der Anwesenheit berechnet.

#### Absenzenquote global in % {: #global_absence_rate }

Diese Quote gibt an, wie viel Prozent Anwesenheit gefordert ist, um die Bedingungen eines Kurses zu erfüllen.

#### Dozentenkalender synchronisieren {: #teacher_calendar_sync }

Dozierende (Kursbetreuer) bekommen Einträge in ihrem persönlichen Kalender (nicht im Kurskalender) für diejenigen Lektionenblöcke, bei welchen sie als Dozierende zugewiesen sind (Für Px-Kunden muss diese Funktion ausgeschaltet sein).

#### Kurs Kalender synchronisieren {: #course_calendar_sync }

Durch diese Option werden die erfassten Lektionenblöcke gleich direkt im Kurskalender angezeigt für alle Teilnehmer, Dozenten und Kursbesitzer.

#### Termin kann als Prüfung markiert werden {: #event_as_exam }

Das Hilfe-Symbol neben der Option zeigt den Text "Wenn diese Option aktiviert ist, kann der Termin als 'Prüfung' markiert werden. Ein markierter Termin wird im Prüfungsmodus durchgeführt, optional mit SEB."

Die Option selbst erscheint nur, wenn der Prüfungsmodus systemweit eingeschaltet ist. Den Schalter "Prüfungsmodus einschalten" finden Sie in der System-Administration unter:<br>
`Administration > e-Assessment > Prüfungsverwaltung`

Die nachfolgenden Felder "Vorlaufzeit", "Nachlaufzeit", "Erlaubte IP-Adressen", "Safe Exam Browser - Art der Benutzung" und "Herunterladbare Konfigurationsdatei" erscheinen, wenn "Standardkonfiguration" auf "Überschreibbar" steht oder wenn "Termin kann als Prüfung markiert werden" eingeschaltet ist. Sie sind nur dann alle ausgeblendet, wenn "Standardkonfiguration" auf "Schreibgeschützt" steht und die Option ausgeschaltet ist.

#### Safe Exam Browser - Art der Benutzung {: #seb_type_of_use }

Legt fest, wie der Safe Exam Browser abgesichert wird, wenn ein Termin als Prüfung markiert wird.

Prüfungsmodi, die nicht aus einem Termin entstehen, sind von dieser Einstellung unabhängig. Dort wird die Variante pro Prüfungsmodus über "Typ von Anwendung" gewählt:<br>
`Kurs > Administration > Prüfungsverwaltung`

Für den Weg über Termine gilt: **Kursbesitzende** schalten die Termin- und Absenzenverwaltung im Kurs ein unter `Kurs > Administration > Einstellungen > Durchführung` und legen die Termine an unter `Kurs > Administration > Termine und Absenzen`. Nach dem Abspeichern kann ein Termin über das 3-Punkte-Menü als Prüfung markiert werden. Das Benutzerhandbuch beschreibt die Kurseinstellungen im Detail: [Konfiguration Termin- und Absenzenverwaltung im Kurs](../../manual_user/learningresources/Course_Settings_Execution.de.md#config_event_and_absence_management)

??? info "Was Betreuende dürfen"

    Betreuende finden keinen Eintrag in der Kurs-Administration, sondern das Werkzeug "Termine" in der Kurs-Werkzeugleiste. Sie erfassen dort Anwesenheiten und Absenzen und können ihre Termine ebenfalls als Prüfung markieren. Diese Sicht beschreibt das Benutzerhandbuch: [Toolbar: Termine, Aufruf als Betreuer:in](../../manual_user/learningresources/Toolbar_Events.de.md#call_as_coach)

    Ihre Rechte werden systemweit vergeben, nicht pro Kurs: Tab "Berechtigungen" dieser Seite legt fest, ob Dozierende Absenzen entschuldigen, Meldungen erfassen oder Rekurse einsehen und bewilligen dürfen. Ein kursspezifisches Recht für Termine und Absenzen gibt es nicht.

    Im Kurs steuern Besitzende, wer einem Termin als Dozent:in zugewiesen ist: [Dozenten/Dozentinnen verwalten](../../manual_user/learningresources/Events_and_absences.de.md#manage_teachers). Betreuende sehen ihre eigenen Termine; die Einstellung "Anzeige in Kursen" in der Globalen Konfiguration legt fest, ob zusätzlich die Termine der anderen Dozierenden angezeigt werden können.

??? info "SEB-Config (empfohlen): Vorlagen aus der System-Administration"

    Die [Konfigurationsvorlagen](e-Assessment_AssessmentMgmt.de.md) werden in der System-Administration gepflegt unter:<br>
    `Administration > e-Assessment > Prüfungsverwaltung`, Tab "Safe Exam Browser Konfiguration"

    Beim Markieren eines Termins als Prüfung ist die als Standard markierte Vorlage vorausgewählt, die Auswahl erfolgt pro Prüfung. Zusätzlich erscheint das Feld "Herunterladbare Konfigurationsdatei".

??? info "SEB mit manuellen Keys: Vorgabewerte aus System- und Kurs-Administration"

    Der systemweite Vorgabewert wird direkt unter dieser Einstellung im Feld "Safe Exam Browser Key" erfasst.

    Kursweit lässt er sich überschreiben unter:<br>
    `Kurs > Administration > Einstellungen > Durchführung`, Feld ["Safe Exam Browser Key"](../../manual_user/learningresources/Course_Settings_Execution.de.md#config_event_and_absence_management)

#### Herunterladbare Konfigurationsdatei {: #seb_downloadable_config }

Diese Option erscheint bei der Variante "SEB-Config (empfohlen)". Wird der SEB eingerichtet, kann optional die Konfigurationsdatei heruntergeladen werden, die z.B. an Prüfungsteilnehmer:innen verteilt werden kann. (Dies ist wichtig, wenn für die Prüfung eigene Geräte der Teilnehmer:innen verwendet werden (BYOD).)


### Globale Konfiguration

![Systemweite Vorgaben zu Fristen, entschuldigten Absenzen und Rekursen, die kein Kurs überschreiben kann. Sektion Globale Konfiguration, Tab Konfiguration.](assets/modules_events_and_absences_global_config_v1_de.png){ class="shadow lightbox" }

Diese Werte gelten für alle Kurse. Kurse können sie nicht überschreiben.

#### Tageserfassung Absenzen {: #daily_absence_recording }

Legt fest, ab wann Dozierende Absenzen erfassen dürfen. "Nein, erst ab Startzeit des Termins" gibt den Termin erst zu seiner Startzeit frei. "Ja, Absenzerfassung für alle Termine des aktuellen Tages erlauben" gibt alle Termine des laufenden Tages frei.

#### Termine partiell durchgeführt zulassen {: #partially_done }

Beim Abschliessen eines Termins kann unter "Effektive Einheiten" die Anzahl Einheiten ausgewählt werden, welche tatsächlich durchgeführt worden sind. Die Anwesenheitsquote wird dadurch auch nur partiell berechnet.

#### Terminstatus {: #event_status }

Wenn diese Option gewählt wird, können ganze Termine abgesagt werden. Dieser Termin zahlt dann nicht zur Anwesenheitsquote.

#### Default Anzahl von geplanten Einheiten {: #default_planned_lectures }

Die Anzahl Einheiten, die ein neuer Termin voreingestellt erhält. 12 ist die maximale Anzahl von Einheiten pro Tag.

#### Erinnerungsfunktion einschalten {: #reminder_enabled }

Hiermit wird die Erinnerungsfunktion aktiviert. Anschliessend sind die Erinnerungs- und die Sperrfrist zu definieren.

#### Erinnerungsfrist {: #reminder_period }

Hier wird die Erinnerungsfrist in Anzahl Tagen eingetragen. Nachdem diese Anzahl Tage erreicht worden ist, wird der/die Dozent:in daran erinnert, die Anwesenheitskontrolle durchzuführen. Ein Tag entspricht 24 Stunden und die Zählung beginnt beim eingetragenen Ende des Termins.

#### Sperrfrist {: #auto_close_period }

Wiederum wird die Anzahl Tage eingetragen. Nachdem diese Frist abgelaufen ist, wird der Status des Termins automatisch auf erledigt gesetzt. Die bereits eingetragene Anwesenheitskontrolle wird gespeichert. Falls nichts eingetragen ist, werden alle Teilnehmenden als anwesend gespeichert. Die Sperrfristzählung beginnt am Folgetag, nachdem der Termin die Endzeit erreicht hat und läuft bis am Ende des Tages.

#### Entschuldigte Absenzen {: #authorized_absences }

Diese Option erlaubt Absenzen zu entschuldigen. Wenn diese Option nicht aktiviert ist, gelten alle Absenzen als unentschuldigt.

#### Entschuldigte Absenzen als anwesend zählen {: #authorized_absences_as_attendance }

Mit dieser Option werden die Absenzen, welche entschuldigt sind, für die Berechnung der Absenzenquote als anwesend gerechnet.

#### Absenzen standardmässig als entschuldigt zählen {: #absences_default_authorized }

Grundsätzlich gelten eingetragene Absenzen als unentschuldigt. Diese Option setzt alle eingetragenen Absenzen automatisch auf entschuldigt. Falls dies nicht zutrifft, muss die Absenz manuell auf unentschuldigt gesetzt werden.

#### Kursbesitzer:innen dürfen alle Kurse in Elementen sehen {: #owner_view_all_courses }

Betrifft die Terminliste eines Elements im Course Planner. Ist die Option ausgeschaltet, sehen Bearbeitende dort nur die Kurse, an denen sie selbst beteiligt sind. Ist sie eingeschaltet, sehen sie alle Kurse des Elements mit Terminen.

#### Rekursmöglichkeit gewähren {: #appeal_enabled }

Wenn die Rekursfrist aktiviert ist, bekommen die Teilnehmenden die Möglichkeit, für eine eingetragenen Absenz Rekurs einzureichen. Dies kann beispielsweise notwendig sein, wenn eine Absenz im Nachhinein als entschuldigt anerkannt wird oder wenn der Dozierende eine Absenz falsch eingetragen hat.

#### Rekursfrist {: #appeal_period }

Die Rekursfrist beginnt, sobald der Termin erledigt ist. Entweder hat der Dozent den Termin manuell auf erledigt gesetzt oder die Sperrfrist ist abgelaufen und der Termin wurde automatisch auf erledigt gesetzt. Die Zählung der Tage beginnt am Folgetag, nachdem der Status des Termins auf erledigt gesetzt worden ist. Anschliessend werden ganze Tage gezählt, Rekursfristschluss ist jeweils am Ende des Tages.

#### Anzeige in Kursen {: #display_in_courses }

Termine aller Dozenten oder nur eigene.


[Zum Seitenanfang ^](#module_events_and_absences)

---


## Tab Berechtigungen

In diesem Tab werden die Berechtigungen für Dozenten / Klassenlehrer hinsichtlich der Termine und Absenzen festgelegt. Diese Rechte werden systemweit vergeben. Ein kursspezifisches Recht für Termine und Absenzen gibt es nicht.

![Drei Rechteblöcke für Dozierende, Klassenlehrpersonen und Teilnehmende, alle systemweit vergeben. Tab Berechtigungen, Seite Termine / Absenzen.](assets/modules_events_and_absences_tab_permissions_v1_de.png){ class="shadow lightbox" }

### Dozenten / Klassenlehrer Berechtigungen

#### Dozenten dürfen Absenzen entschuldigen {: #teacher_authorize_absence }

Dozierende können eine erfasste Absenz als entschuldigt kennzeichnen.

#### Dozenten dürfen Rekurse einsehen {: #teacher_see_appeal }

Dozierende sehen die Rekurse zu ihren eigenen Terminen.

#### Dozenten dürfen Rekurse bewilligen {: #teacher_authorize_appeal }

Dozierende können einen Rekurs annehmen oder ablehnen.

#### Dozenten dürfen Meldungen erfassen {: #teacher_record_notice }

Dozierende können Abmeldungen, Dispensen und Absenzen ohne Abmeldung erfassen.

#### Klassenlehrer dürfen Absenzen einsehen {: #mastercoach_see_absence }

Klassenlehrpersonen sehen die Absenzen der von ihnen betreuten Personen.

#### Klassenlehrer dürfen Meldungen erfassen {: #mastercoach_record_notice }

Klassenlehrpersonen können Abmeldungen, Dispensen und Absenzen ohne Abmeldung erfassen.

#### Klassenlehrer dürfen Absenzen entschuldigen {: #mastercoach_authorize_absence }

Klassenlehrpersonen können eine erfasste Absenz als entschuldigt kennzeichnen.

#### Klassenlehrer dürfen Rekurse einsehen {: #mastercoach_see_appeal }

Klassenlehrpersonen sehen die Rekurse der von ihnen betreuten Personen.

#### Klassenlehrer dürfen Rekurse bewilligen {: #mastercoach_authorize_appeal }

Klassenlehrpersonen können einen Rekurs annehmen oder ablehnen.

#### Klassenlehrer dürfen Termine wiederöffnen {: #mastercoach_reopen_events }

Klassenlehrpersonen können einen abgeschlossenen Termin erneut öffnen, um die Anwesenheitskontrolle zu korrigieren.

#### Teilnehmer:innen dürfen sich abmelden {: #participant_notice }

Teilnehmende können sich selbst von einem Termin abmelden.



[Zum Seitenanfang ^](#module_events_and_absences)

---


## Tab Begründungen Termine

Termine können automatisch oder manuell beendet werden. Wird ein Termin z.B. früher beendet, soll dafür ein Grund angegeben werden. Der **Grund für einen abweichenden Terminabschluss** kann aus einer Liste ausgewählt werden.

Die zur Auswahl stehenden Begriffe und Beschreibungen für diese Begründungen können hier durch Administrator:innen definiert werden.

Werden hier keine Begründungen hinterlegt, erscheint die Begründungsauswahl beim Schliessen des Termins nicht.


[Zum Seitenanfang ^](#module_events_and_absences)

---


## Tab Begründungen Absenzen [:octicons-tag-16:{ title="ab Release 14.1 (OO-4155)" }](https://track.frentix.com/issue/OO-4155)

In der Kursadministration können Besitzer:innen/Betreuer:innen Absenzen erfassen.
Für die Begründung der Absenzen kann dabei aus verschiedenen Begriffen ausgewählt werden, wie z.B. "Krankheit", "Unfall", "Dozent:in krank", u.ä.

Diese dort angebotene Auswahl an Begriffen und Beschreibungen kann hier definiert werden.

[Zum Seitenanfang ^](#module_events_and_absences)

---


## Tab Report

Hier können Reports für bestimmte Zeiträume angezeigt werden. Es kann nach dem Status der Termine /Absenzen vorselektiert werden:

- Offen
- Erledigt
- Autoerledigt
- Wiedergeöffnet

Alle Reports können auch als Excel-Datei heruntergeladen werden.

[Zum Seitenanfang ^](#module_events_and_absences)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kurseinstellungen - Tab Durchführung >](../../manual_user/learningresources/Course_Settings_Execution.de.md)<br>
[Toolbar: Termine >](../../manual_user/learningresources/Toolbar_Events.de.md)<br>
[Termine und Absenzen im Kurs >](../../manual_user/learningresources/Events_and_absences.de.md)<br>
[Prüfungsverwaltung >](e-Assessment_AssessmentMgmt.de.md)

**Weiterführend**<br>
[Safe Exam Browser einrichten >](../../manual_how-to/SEB_Admin/SEB_Admin.de.md)<br>
[Modul Räume >](Modules_Rooms.de.md)<br>
[Persönliche Absenzen >](../../manual_user/personal_menu/Absences.de.md)<br>
[Kursübergreifende Absenzenverwaltung >](../../manual_user/area_modules/Absence_Management.de.md)

[Zum Seitenanfang ^](#module_events_and_absences)
