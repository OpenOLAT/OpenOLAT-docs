# Termine und Absenzen {: #events_and_absences}


## Welche Termine gibt es in OpenOlat? {: #event_types}

In OpenOlat gibt es grundsätzlich 2 Arten von Terminen:

- einfache Termine (ohne die Möglichkeit zur Erfassung von Absenzen)
- Termine mit Absenzen (Termine im Kurs, sie erscheinen im Course Planer und der Absenzenverwaltung)<br>
Auf diese Termine können auch Dozent:innen gebucht werden. (Nur Betreuer:innen können zu Dozent:innen gemacht werden.)

|                           | einfacher Termin | Termin mit Absenzen |
| ------------------------- |:-----------------:|:--------------------:|
|[Termine im Course Planner](../area_modules/Course_Planner_Events.de.md)|   |x|
|[Termine in der Absenzenverwaltung](#access_absences)|   |x|
|[Termine in Projekten](../area_modules/Project_Schedule.de.md)| x |  | 
|[Termine in (Projekt-)To-dos](../area_modules/Project_Schedule.de.md)| x |  | 
|[Termine im persönlichen Menü](../personal_menu/To-Dos.de.md)| x | x | 
|[Termine in Kalendern](../personal_menu/Calendar.de.md#create_entry)| x | x | 
|[Termine in BigBlueButton](../../manual_admin/administration/BigBlueButton_module.de.md#tab_online-meetings)| x |  | 
|[Termine in Micorosft Teams](../learningresources/Course_Element_Microsoft_Teams.de.md#raum-konfigurieren-bei-geschlossenem-kurseditor)| x |  | 


[Zum Seitenanfang ^](#events_and_absences)

---


## Welche Absenzen können verwaltet werden? {: #administrated_absences}

!!! info "Allgemeiner Hinweis"

    Administrator:innen können die Möglichkeiten in der Absenzenverwaltung sehr detailliert einrichten. Sollte eine der beschriebenen Möglichkeiten bei Ihnen nicht zur Verfügung stehen, wenden Sie sich bitte an Ihre:n zuständige:n Adminisistrator:in.

!!! info "Allgemeiner Hinweis"

    In OpenOlat werden prinzipiell Absenzen (Abwesenheiten) erfasst, nicht Anwesenheiten.


### Absenzen {: #absences_categories}

Die Anwesenheit bzw. Absenz von Teilnehmer:innen kann in folgenden Kategorien erfasst werden:

- Anwesend
- Entschuldigte Abwesenheit
- Unentschuldigte Abwesenheit
- Dispensiert

Absenzen werden in der Regel bei einer Anwesenheitskontrolle durch die **Betreuer:innen** erfasst.

**Teilnehmer:innen** finden ihre erfassten Absenzen im [persönlichen Menü](../personal_menu/Absences.de.md).

Aus den erfassten Absenzen wird eine **Anwesenheitsrate** berechnet. Durch Abgleich mit einer vorgegebenen erlaubten **Absenzquote** (z.B. 80%) kann daraus berechnet werden, ob ein Kurs als besucht gelten kann.

### Abmeldungen {: #abcenses_cancellations}

Es kann den Teilnehmer:innen erlaubt werden, dass sie sich im [persönlichen Menü](../personal_menu/Absences.de.md#tab-abmeldung-dispense) im Voraus abmelden.

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

1. der **generellen Aktivierung und Konfiguration** des Absenzenmanagements durch Administrator:innen unter:<br>
   **Administration > Module > Termine und Absenzen**<br>
   [Mehr dazu >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)


2. der **Konfiguration** der Absenzenverwaltung in einem **Kurs**<br>
    Die Konfiguration der Termin- und Absenzenverwaltung für einen bestimmten Kurs erfolgt durch die Kursbesitzer:innen in der Kursadministration:<br>
    **Administration > Einstellungen > Tab "Durchführung" > Abschnitt "Konfiguration Termin- und Absenzenverwaltung im Kurs"**<br>
    [Mehr dazu >](../learningresources/Course_Settings_Execution.de.md#config_event_and_absence_management)


3. der **Erfassung und Verwaltung** der Absenzen in einem **Kurs** durch **Kursbesitzer:innen**<br>
    Die Erfassung und Verwaltung erfolgt im Run Mode (also zur Laufzeit, nicht im Editor) durch Kursbesitzer:innen unter:<br>
    **Administration > Termine und Absenzen > Tab Teilnehmer**<br>
    [Mehr dazu >](../learningresources/Events_and_absences.de.md)

4. der **Erfassung und Verwaltung** der Absenzen in einem **Kurs** durch **Betreuer:innen**<br>
    Die Erfassung und Verwaltung durch Betreuer:innen erfolgt unter:<br>
    **Toolbar > Termine**<br>
    [Mehr dazu >](../learningresources/x.de.md)

5. der Übersicht über die **persönlichen Absenzen**<br>
    Die persönlichen Absenzen finden Sie und alle Teilnehmer:innen jeweils im persönlichen Menü. Hier ist die Verwaltung nur in begrenztem Rahmen und für sich persönlich möglich, z.B. in Form einer Abmeldung.<br>
    [Mehr dazu >](../personal_menu/Absences.de.md)


6.  der **kursübergreifenden Absenzenerfassungung** durch Coaches<br>
    Die Möglichkeit zur Erfassung von Absenzen in verschiedenen Kursen finden Coaches im <br>
    **Coachingtool > Button "Termine/Absenzen"**.<br>
    [Mehr dazu >](../area_modules/Coaching.de.md)


7. der **kursübergreifenden Absenzenverwaltung** durch Berechtigte mit der Rolle Absenzenverwalter:in.<br>
    Zur Verwaltung gehört z.B. die Bearbeitung von Dispensen und Rekursen. Diese Verwaltungsaufgabe geht über die einfache Erfassung hinaus und ist deshalb einer gesonderten Rolle zugeordnet. Berechtigte finden die Werkzeuge im<br>
   **Menü der Kopfzeile: Absenzenverwaltung**<br>
   [Mehr dazu >](../area_modules/Absence_Management.de.md)


[Zum Seitenanfang ^](#events_and_absences)

---


## Weitere Informationen {: #further_information}

[Aktivierung und Konfiguration des Absenzenmanagements durch Administrator:innen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Konfiguration der Absenzenverwaltung in einem Kurs >](../learningresources/Course_Settings_Execution.de.md#config_event_and_absence_management)<br>
[Erfassung und Verwaltung der Absenzen in einem Kurs durch Kursbesitzer:innen >](../learningresources/Events_and_absences.de.md)<br>
[Erfassung und Verwaltung der Absenzen in einem Kurs durch Betreuer:innen >](../learningresources/Toolbar_Events.de.md)<br>
[Persönliche Absenzen >](../personal_menu/Absences.de.md)<br>
[Kursübergreifende Absenzenerfassungung im Coachingtool >](../area_modules/Coaching.de.md)<br>
[Kursübergreifende Absenzenverwaltung durch Absenzenverwalter:innen >](../area_modules/Absence_Management.de.md)<br>

[Zum Seitenanfang ^](#events_and_absences)

---