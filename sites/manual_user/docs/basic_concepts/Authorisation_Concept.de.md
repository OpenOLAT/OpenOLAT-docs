# Rollen und Rechte: Rechte in Kursen {: #rights_in_courses}

Nachstehend wird aufgelistet, welche Zugriffsmöglichkeiten auf Kurse die unterschiedlichen Rollen haben.

Welche Rechte die Rollen innerhalb des Course Planners haben (auf Produkte, Durchführungen, Elemente und Termine), ist unter [Rollen und Rechte im Course Planner](../area_modules/Course_Planner.de.md#roles_rights) beschrieben.


Legende

| Begriff/Symbol    | Beschreibung                                |
| ----------------- | ------------------------------------------- |
| Vollzugriff       | Zugriff lesend und schreibend               |
| Lesend            | Zugriff nur lesend                          |
| :material-cancel: | Kein Zugriff. Weder schreibend noch lesend. |
| :material-check:  | Aktion verfügbar                            |


## Rechte der Kursrollen [:octicons-tag-16:{ title="ab Release 20.1.0 (OO-8646)" }](https://track.frentix.com/issue/OO-8646)
Die Kursrollen Teilnehmer:in sowie Betreuer:in stehen stellvertretend auch für die Gruppenteilnehmer:innen/-betreuer:innen und Durchführungsteilnehmer:innen/-betreuer:innen.

|                                                             | Besitzer:innen   | Betreuer:innen    | Teilnehmer:innen  |
| ----------------------------------------------------------- | :--------------: | :---------------: | :---------------: |
| **Zugriff nach Status**                                                                                                |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | Vollzugriff      | :material-cancel: | :material-cancel: |
| ![Review](assets/s_rev_DE.png){ width=56px }                | Vollzugriff      | :material-cancel: | :material-cancel: |
| ![Freigabe Betreuer:innen](assets/s_acc_co_DE.png){ width=120px } | Vollzugriff      | Lesend            | :material-cancel: |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Vollzugriff      | Lesend            | Lesend            |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend           | Lesend            | Lesend            |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | Lesend           | :material-cancel: | :material-cancel: |
| **Kursadmin-Tools**                                                                                                    |
| Mitgliederverwaltung                                        | Vollzugriff      | :material-cancel: | :material-cancel: |
| Bewertungswerkzeug                                          | Vollzugriff      | Vollzugriff       | :material-cancel: |
| Termine und Absenzen                                        | Vollzugriff      | :material-cancel: | :material-cancel: |
| **Kursaktionen**                                                                                                       |
| Kopieren                                                    | :material-check: |                   |                   |
| Löschen                                                     | :material-check: |                   |                   |
| Exportieren                                                 | :material-check: |                   |                   |
| **Module**                                                                                                             |
| Coaching                                                    | Vollzugriff      | Vollzugriff       | :material-cancel: |

Kopieren und Löschen setzen bei Besitzer:innen zusätzlich die Organisationsrolle Autor:in, Lernressourcenverwalter:in oder Administrator:in in der Organisation des Kurses voraus. Besitzer:innen ohne eine dieser Rollen sehen diese Aktionen nicht.


[Zum Seitenanfang ^](#rights_in_courses)

---

## Rechte der organisationsweiten Rollen in einem Kurs
|                                                             | Administrator:innen | Autor:innen                            | Principal         | Linien-<br/>vorgesetzte | 
| ----------------------------------------------------------- | :-----------: | :------------------------------: | ----------------: | :----------------------: | 
| **Zugriff nach Status**                                                                                                                                       |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        | 
| ![Review](assets/s_rev_DE.png){ width=56px }                | Vollzugriff   | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        | 
| ![Freigabe Betreuer:innen](assets/s_acc_co_DE.png){ width=120px } | Vollzugriff   | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        | 
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Vollzugriff   | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        | 
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend        | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | Lesend        | :material-cancel:                | :material-cancel: | :material-cancel:        |
| **Kursadmin-Tools**                                                                                                                                           |
| Mitgliederverwaltung                                        | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        |
| Bewertungswerkzeug                                          | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        |
| Dateien eines Kurses                                        | Vollzugriff   |      Vollzugriff           | :material-cancel:           | :material-cancel:        |
| Badges                                        | Vollzugriff   |      Vollzugriff           | Lesend           | Lesend        |
| Termine und Absenzen                                        | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        |
| Archivierung & Reports                                    | Vollzugriff   |      Vollzugriff           | :material-cancel:           | :material-cancel:        |
| **Kursaktionen**                                                                                                                                              |
| Kopieren                                                    | :material-check: | :material-check: mit Freigabe |                   |                          |
| Löschen                                                     | :material-check: |                               |                   |                          |
| Exportieren                                                 | :material-check: | :material-check: mit Freigabe |                   |                          |
| Wiederherstellen                                            | :material-check: |                               |                   |                          |
| Dauerhaft löschen                                           | :material-check: |                               |                   |                          |
| **Module**                                                                                                                                                    |
| Coaching                                                    | Vollzugriff      | :material-cancel:             | :material-cancel: | Lesend                   |


[Zum Seitenanfang ^](#rights_in_courses)

---

## Rechte der Kursteilnehmer:innen
|                                                             | Registrierte Benutzer:innen                                | Anonymer Gast               | 
| ----------------------------------------------------------- | :-----------------------------------------------------: | :-------------------------: |
| **Zugriff nach Status**                                                                                                                             |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | :material-cancel:                                       | :material-cancel:           |
| ![Review](assets/s_rev_DE.png){ width=56px }                | :material-cancel:                                       | :material-cancel:           |
| ![Freigabe Betreuer:innen](assets/s_acc_co_DE.png){ width=120px } | :material-cancel:                                       | :material-cancel:           |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Lesend,<br/>wenn Zugang "Frei verfügbar" "Ohne Buchung" | Lesend,<br/>wenn Gastzugang |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend,<br/>wenn Zugang "Frei verfügbar" "Ohne Buchung" | Lesend,<br/>wenn Gastzugang |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | :material-cancel:                                       | :material-cancel:           |


[Zum Seitenanfang ^](#rights_in_courses)

---

## Rechte der Verwalter-Rollen in einem Kurs
|                                                             | Lernressourcen-<br/>verwalter:innen |  Kursplaner:innen | Absenzenverwalter:innen |
| ----------------------------------------------------------- | :---------------------------: | :------------------------: | :---------------------------: |
| **Zugriff nach Status**                                                                                                                                  |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Review](assets/s_rev_DE.png){ width=56px }                | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Freigabe Betreuer:innen](assets/s_acc_co_DE.png){ width=120px } | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend                        | :material-cancel:          | :material-cancel:             |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | Lesend                        | :material-cancel:          | :material-cancel:             |
| **Kursadmin-Tools**                                                                                                                                      |
| Mitgliederverwaltung                                        | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| Bewertungswerkzeug                                          | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| Termine und Absenzen                                        | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| **Kursaktionen**                                                                                                                                             |
| Kopieren                                                    | :material-check:              |                            |                               |
| Löschen                                                     | :material-check:              |                            |                               |
| Exportieren                                                 | :material-check:              |                            |                               |
| **Module**                                                                                                                                               |
| Coaching                                                    | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| Absenzenverwaltung                                         | :material-cancel:             | :material-cancel:          | Vollzugriff                   |


[Zum Seitenanfang ^](#rights_in_courses)

---

## Rechte der Produkt-Rollen in einem Kurs
|                                                             | Produkt-<br/>besitzer:innen |  Elementbesitzer:innen | Klassenlehrer:innen   |
| ----------------------------------------------------------- | :----------------------: | :-----------------------------: | :---------------: |
| **Zugriff nach Status**                                                                                                                      |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Review](assets/s_rev_DE.png){ width=56px }                | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Freigabe Betreuer:innen](assets/s_acc_co_DE.png){ width=120px } | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | :material-cancel:        | :material-cancel:               | :material-cancel: |
| **Admin-Tools**                                                                                                                              |
| Mitgliederverwaltung                                        | :material-cancel:        | :material-cancel:               | Lesend            |
| Bewertungswerkzeug                                          | :material-cancel:        | :material-cancel:               | Vollzugriff       |
| Termine und Absenzen                                        | :material-cancel:        | :material-cancel:               | Vollzugriff       |
| **Module**                                                                                                                                   |
| Coaching - Termine / Absenzen                               | :material-cancel:        | :material-cancel:               | Vollzugriff       |
| Coaching - Kurse                                            | :material-cancel:        | :material-cancel:               | :material-cancel: |
| Absenzenverwaltung                                         | :material-cancel:        | :material-cancel:               | :material-cancel: |


[Zum Seitenanfang ^](#rights_in_courses)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Course Planner: Übersicht >](../area_modules/Course_Planner.de.md)

**Weiterführend**<br>
[Welche Rollen gibt es? >](Roles.de.md)<br>
[Rollen zuweisen >](Assign_Roles.de.md)<br>
[Mitgliederverwaltung >](../learningresources/Members_management.de.md)<br>
[Zugangskonfiguration / Freigabe >](../learningresources/Access_configuration.de.md)

[Zum Seitenanfang ^](#rights_in_courses)
