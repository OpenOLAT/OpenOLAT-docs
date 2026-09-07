# Termine und Absenzen {: #events_and_absences}


## Welche Termine gibt es in OpenOlat? {: #event_types}

In OpenOlat gibt es grundsätzlich 2 Arten von Terminen:

- einfache Termine (Einträge in Kalendern)
- Termine mit Zusatzoptionen: Sie erscheinen in [Kursen](../learningresources/Events_and_absences.de.md), im [Course Planner](../area_modules/Course_Planner.de.md) und der [Absenzenverwaltung](../area_modules/Absence_Management.de.md).
Diese Termine können mit Online-Meetings verknüpft werden und es besteht die Möglichkeit zur Erfassung von Absenzen. Auch Dozent:innen können auf diese Termine gebucht werden. (Hinweis: Nur Betreuer:innen können zu Dozent:innen gemacht werden.)<br>
Termine mit Zusatzoptionen können den Status "Geplant", "Am laufen", "Erledigt" oder "Abgesagt" haben.<br>
Besteht keine Berechtigung, kann die Sicht auf Termine auch eingeschränkt sein.


|                           | einfache Termine | Termine mit Zusatzoptionen |
| ------------------------- |:-----------------:|:--------------------:|
|[Termine in Kursen](../learningresources/Events_and_absences.de.md#edit_events)|   |x|
|[Termine im Kursbaustein Terminplanung](../learningresources/Course_Element_Appointment_Scheduling.de.md)|   |x|
|[Termine im Course Planner](../area_modules/Course_Planner_Events.de.md)|   |x|
|[Termine in der Absenzenverwaltung](#access_absences)|   |x|
|[Terminplan in Projekten](../area_modules/Project_Schedule.de.md)| x |  | 
|[Termine in (Projekt-)To-dos](../area_modules/Project_Schedule.de.md)| x |  | 
|[Termine im persönlichen Menü](../personal_menu/To-Dos.de.md)| x | x | 
|[Termine in Kalendern](../personal_menu/Calendar.de.md#create_entry)| x |  | 
|[Termine in BigBlueButton](../../manual_admin/administration/BigBlueButton_module.de.md#tab_online-meetings)| x |  | 
|[Termine in Microsoft Teams](../learningresources/Course_Element_Microsoft_Teams.de.md#closed_editor_configuration)| x |  | 


[Zum Seitenanfang ^](#events_and_absences)

---

### Welche Termine (mit Zusatzoptionen) werden angezeigt? {: #event_conditions}

Die Sichtbarkeit von Terminen hängt generell davon ab,

- ob das Modul "Termine / Absenzen" in der System-Administration global aktiviert ist
- ob das Fokuselement "Termine" eingeblendet ist
- ob es tatsächlich relevante Termine gibt
- ob der Termin für die Rolle sichtbar sein soll 

[Zum Seitenanfang ^](#events_and_absences)

---

### Wo werden die Termine mit Zusatzoptionen angezeigt? {: #event_display}

Teilnehmer:innen erhalten eine Sicht auf ihre Termine in der **Toolbar** des Kurses unter dem Icon "Termine". Sie sehen dort nur ihre eigenen Termine und können keine Absenzen erfassen.

Auch auf den verschiedenen **Dashboards** der Betreuer:innen werden Termine angezeigt.

Auf den Übersichtsseiten, z.B. im Coaching und im Course Planner, stehen **Termin-Widgets** zur Verfügung.

Welche Angaben eine Terminliste enthält, hängt vom Bereich ab:

- Im **Course Planner** dient die Liste der Planung. Ein Absenzenmanagement gibt es dort nicht.
- Im **Coaching** sehen Betreuer:innen die Termine aller ihrer Kurse und erfassen dort auch die Absenzen.
- In der **Toolbar eines Kurses** sehen Teilnehmer:innen nur ihre eigenen Termine mit den für sie relevanten Angaben.

[Zum Seitenanfang ^](#events_and_absences)

---

### Welchen Status können Termine in OpenOlat haben? {: #event_status}

Termine mit Zusatzoptionen (z.B. im Course Planner oder im Coaching) haben einen der folgenden Status-Werte:

- Geplant
- Am laufen
- Erledigt
- Abgesagt

Der jeweils nächste anstehende Termin trägt statt "Geplant" das Label "Als nächstes geplant".

In den Terminlisten steht der Status in der Spalte "Status".

[Zum Seitenanfang ^](#events_and_absences)

---


## Welche Absenzen können verwaltet werden? {: #administrated_absences}

!!! info "Allgemeiner Hinweis"

    Administrator:innen können die Möglichkeiten in der [Absenzenverwaltung](../area_modules/Absence_Management.de.md) sehr detailliert einrichten. Sollte eine der beschriebenen Möglichkeiten bei Ihnen nicht zur Verfügung stehen, wenden Sie sich bitte an Ihre:n zuständige:n Administrator:in.

!!! info "Allgemeiner Hinweis"

    In OpenOlat werden prinzipiell Absenzen (Abwesenheiten) erfasst, nicht Anwesenheiten.


### Absenzen {: #absences_categories}

Die Anwesenheit bzw. Absenz von Teilnehmenden kann in folgenden Kategorien erfasst werden:

- Anwesend
- Entschuldigte Abwesenheit
- Unentschuldigte Abwesenheit
- Dispensiert

Absenzen werden in der Regel bei einer Anwesenheitskontrolle durch die **Betreuer:innen** erfasst.

**Teilnehmer:innen** finden ihre erfassten Absenzen im [persönlichen Menü](../personal_menu/Absences.de.md).

Aus den erfassten Absenzen wird eine **Anwesenheitsrate** berechnet. Durch Abgleich mit einer vorgegebenen erlaubten **Absenzquote** (z.B. 80%) kann daraus berechnet werden, ob ein Kurs als besucht gelten kann.

### Abmeldungen {: #abcenses_cancellations}

Es kann den Teilnehmer:innen erlaubt werden, dass sie sich im [persönlichen Menü](../personal_menu/Absences.de.md#tab_notices_dispensation) im Voraus abmelden.

### Entschuldigte Absenzen {: #excused_absences}

Es kann systemweit eingestellt werden, dass entschuldigte Absenzen für die Berechnung der Anwesenheitsrate als "anwesend" gezählt werden.

### Dispense {: #dispensations}

Es gibt verschiedene Gründe, warum ein:e Teilnehmer:in grundsätzlich nicht an einem bestimmten Teil eines Kurses teilnehmen kann oder muss. In diesem Fall kann eine Dispens eingerichtet werden.

### Rekurse {: #appeals}

Teilnehmer:innen haben die Möglichkeit, gegen eine von Betreuer:innen z.B. vermeintlich unentschuldigte Absenz Rekurs einzulegen. Auch die Rekurse werden in OpenOlat erfasst.

[Zum Seitenanfang ^](#events_and_absences)

---


## Wo finde ich die Absenzenverwaltung?  {: #access_absences}

Es ist zu unterscheiden zwischen 

1. der **generellen Aktivierung und Konfiguration** des Absenzenmanagements durch Administrator:innen in der System-Administration unter:<br>
   `Administration > Module > Termine / Absenzen`<br>
   [Mehr dazu >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)


2. der **Konfiguration** der Absenzenverwaltung in einem **Kurs**<br>
    Die Konfiguration der Termin- und Absenzenverwaltung für einen bestimmten Kurs erfolgt durch die Kursbesitzer:innen in der Kursadministration:<br>
    `Kurs > Administration > Einstellungen > Tab "Durchführung" > Abschnitt "Konfiguration Termin- und Absenzenverwaltung im Kurs"`<br>
    [Mehr dazu >](../learningresources/Course_Settings_Execution.de.md#config_event_and_absence_management)


3. der **Erfassung und Verwaltung** der Absenzen in einem **Kurs** durch **Kursbesitzer:innen**<br>
    Die Erfassung und Verwaltung erfolgt im Run Mode (also zur Laufzeit, nicht im Editor) durch Kursbesitzer:innen unter:<br>
    `Kurs > Administration > Termine und Absenzen > Tab "Teilnehmer"`<br>
    [Mehr dazu >](../learningresources/Events_and_absences.de.md)

4. der **Erfassung und Verwaltung** der Absenzen in einem **Kurs** durch **Betreuer:innen**<br>
    Die Erfassung und Verwaltung durch Betreuer:innen erfolgt unter:<br>
    `Toolbar > Termine`<br>
    [Mehr dazu >](../learningresources/Toolbar_Events.de.md)

5. der Übersicht über die **persönlichen Absenzen**<br>
    Die persönlichen Absenzen finden Sie und alle Teilnehmer:innen jeweils im persönlichen Menü. Hier ist die Verwaltung nur in begrenztem Rahmen und für sich persönlich möglich, z.B. in Form einer Abmeldung.<br>
    [Mehr dazu >](../personal_menu/Absences.de.md)


6. der **kursübergreifenden Absenzenerfassung** durch Betreuer:innen<br>
    Die Möglichkeit zur Erfassung von Absenzen in verschiedenen Kursen finden Betreuer:innen unter:<br>
    `Coaching > Termine / Absenzen`<br>
    [Mehr dazu >](../area_modules/Coaching.de.md)


7. der **kursübergreifenden Absenzenverwaltung** durch Berechtigte mit der Rolle Absenzenverwalter:in.<br>
    Zur Verwaltung gehört z.B. die Bearbeitung von Dispensen und Rekursen. Diese Verwaltungsaufgabe geht über die einfache Erfassung hinaus und ist deshalb einer gesonderten Rolle zugeordnet. Berechtigte finden die Werkzeuge im<br>
   **Menü der Kopfzeile: Absenzenverwaltung**<br>
   [Mehr dazu >](../area_modules/Absence_Management.de.md)


[Zum Seitenanfang ^](#events_and_absences)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Termine und Absenzen >](../learningresources/Events_and_absences.de.md)<br>
[Course Planner: Übersicht >](../area_modules/Course_Planner.de.md)<br>
[Absenzenverwaltung >](../area_modules/Absence_Management.de.md)<br>
[Kursbaustein "Terminplanung" >](../learningresources/Course_Element_Appointment_Scheduling.de.md)<br>
[Course Planner: Termine >](../area_modules/Course_Planner_Events.de.md)<br>
[Projekte - Terminplan >](../area_modules/Project_Schedule.de.md)<br>
[Persönliche Werkzeuge: To-dos >](../personal_menu/To-Dos.de.md)<br>
[Persönliche Werkzeuge: Kalender >](../personal_menu/Calendar.de.md)<br>
[Modul BigBlueButton >](../../manual_admin/administration/BigBlueButton_module.de.md)<br>
[Kursbaustein "Microsoft Teams" >](../learningresources/Course_Element_Microsoft_Teams.de.md)<br>
[Persönliche Werkzeuge: Absenzen >](../personal_menu/Absences.de.md)<br>
[Modul Termine und Absenzen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Kurseinstellungen - Tab Durchführung >](../learningresources/Course_Settings_Execution.de.md)<br>
[Toolbar: Termine >](../learningresources/Toolbar_Events.de.md)<br>
[Coaching - Übersicht >](../area_modules/Coaching.de.md)

[Zum Seitenanfang ^](#events_and_absences)

---