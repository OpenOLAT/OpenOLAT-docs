# Übersicht
Legende

| Begriff/Symbol    | Beschreibung                                |
| ----------------- | ------------------------------------------- |
| Vollzugriff       | Zugriff lesend und schreibend               |
| Lesend            | Zugriff nur lesend                          |
| :material-cancel: | Kein Zugriff. Weder schreibend noch lesend. |
| :material-check:  | Aktion verfügbar                            |

## Zugriff Kurs
In diesem Kapitel werden die Zugriffsmöglichkeiten der jeweiligen Benutzer mit unterschiedlichen Rollen aufgezeigt.
### Kursrollen
Die Kursrollen Teilnehmer sowie Betreuer stehen stellvertretend auch für die Gruppenteilnehmer/-betreuer und Curriculumteilnehmer/-betreuer.

|                                                             | Besitzer         | Betreuer          | Teilnehmer        |
| ----------------------------------------------------------- | :--------------: | :---------------: | :---------------: |
| **Zugriff nach Status**                                                                                                |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | Vollzugriff      | :material-cancel: | :material-cancel: |
| ![Review](assets/s_rev_DE.png){ width=56px }                | Vollzugriff      | :material-cancel: | :material-cancel: |
| ![Freigabe Betreuer](assets/s_acc_co_DE.png){ width=120px } | Vollzugriff      | Lesend            | :material-cancel: |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Vollzugriff      | Lesend            | Lesend            |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend           | Lesend            | Lesend            |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | Lesend           | :material-cancel: | :material-cancel: |
| **Kursadmin-Tools**                                                                                                    |
| Mitgliederverwaltung                                        | Vollzugriff      | :material-cancel: | :material-cancel: |
| Bewertungswerkzeug                                          | Vollzugriff      | Vollzugriff       | :material-cancel: |
| Lektionen&Absenzen                                          | Vollzugriff      | :material-cancel: | :material-cancel: |
| **Kursaktionen**                                                                                                       |
| Kopieren                                                    | :material-check: |                   |                   |
| Löschen                                                     | :material-check: |                   |                   |
| Exportieren                                                 | :material-check: |                   |                   |
| **Module**                                                                                                             |
| Coaching                                                    | Vollzugriff      | Vollzugriff       | :material-cancel: |

### Systemweite Rollen
|                                                             | Administrator | Autor                            | Principal         | Linien-<br/>vorgesetzter | 
| ----------------------------------------------------------- | :-----------: | :------------------------------: | ----------------: | :----------------------: | 
| **Zugriff nach Status**                                                                                                                                       |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        | 
| ![Review](assets/s_rev_DE.png){ width=56px }                | Vollzugriff   | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        | 
| ![Freigabe Betreuer](assets/s_acc_co_DE.png){ width=120px } | Vollzugriff   | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        | 
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Vollzugriff   | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        | 
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend        | Lesend,<br/>mit Freigabe         | Lesend            | :material-cancel:        |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | Lesend        | :material-cancel:                | :material-cancel: | :material-cancel:        |
| **Kursadmin-Tools**                                                                                                                                           |
| Mitgliederverwaltung                                        | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        |
| Bewertungswerkzeug                                          | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        |
| Lektionen&Absenzen                                          | Vollzugriff   | :material-cancel:                | Lesend            | :material-cancel:        |
| **Kursaktionen**                                                                                                                                              |
| Kopieren                                                    | :material-check: | :material-check: mit Freigabe |                   |                          |
| Löschen                                                     | :material-check: |                               |                   |                          |
| Exportieren                                                 | :material-check: | :material-check: mit Freigabe |                   |                          |
| Wiederherstellen                                            | :material-check: |                               |                   |                          |
| Dauerhaft löschen                                           | :material-check: |                               |                   |                          |
| **Module**                                                                                                                                                    |
| Coaching                                                    | Vollzugriff      | :material-cancel:             | :material-cancel: | Lesend                   |

#### Teilnehmer
|                                                             | Registrierter Benutzer                                  | Anonymer Gast               | 
| ----------------------------------------------------------- | :-----------------------------------------------------: | :-------------------------: |
| **Zugriff nach Status**                                                                                                                             |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | :material-cancel:                                       | :material-cancel:           |
| ![Review](assets/s_rev_DE.png){ width=56px }                | :material-cancel:                                       | :material-cancel:           |
| ![Freigabe Betreuer](assets/s_acc_co_DE.png){ width=120px } | :material-cancel:                                       | :material-cancel:           |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Lesend,<br/>wenn Zugang "Frei verfügbar" "Ohne Buchung" | Lesend,<br/>wenn Gastzugang |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend,<br/>wenn Zugang "Frei verfügbar" "Ohne Buchung" | Lesend,<br/>wenn Gastzugang |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | :material-cancel:                                       | :material-cancel:           |

#### Verwalter-Rollen
|                                                             | Lernressourcen-<br/>verwalter |  Curriculum-<br/>verwalter | Lektionenblock-<br/>verwalter |
| ----------------------------------------------------------- | :---------------------------: | :------------------------: | :---------------------------: |
| **Zugriff nach Status**                                                                                                                                  |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Review](assets/s_rev_DE.png){ width=56px }                | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Freigabe Betreuer](assets/s_acc_co_DE.png){ width=120px } | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | Lesend                        | :material-cancel:          | :material-cancel:             |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | Lesend                        | :material-cancel:          | :material-cancel:             |
| **Kursadmin-Tools**                                                                                                                                      |
| Mitgliederverwaltung                                        | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| Bewertungswerkzeug                                          | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| Lektionen&Absenzen                                          | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| **Kursaktionen**                                                                                                                                             |
| Kopieren                                                    | :material-check:              |                            |                               |
| Löschen                                                     | :material-check:              |                            |                               |
| Exportieren                                                 | :material-check:              |                            |                               |
| **Module**                                                                                                                                               |
| Coaching                                                    | Vollzugriff                   | :material-cancel:          | :material-cancel:             |
| Lektionenverwaltung                                         | :material-cancel:             | :material-cancel:          | Vollzugriff                   |

### Curriculum-Rollen
|                                                             | Curriculum-<br/>besitzer |  Curriculum-<br/>elemntbesitzer | Klassenlehrer     |
| ----------------------------------------------------------- | :----------------------: | :-----------------------------: | :---------------: |
| **Zugriff nach Status**                                                                                                                      |
| ![Vorbereitung](assets/s_prep_DE.png){ width=90px }         | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Review](assets/s_rev_DE.png){ width=56px }                | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Freigabe Betreuer](assets/s_acc_co_DE.png){ width=120px } | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Veröffentlicht](assets/s_publ_DE.png){ width=100px }      | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Beendet](assets/s_fin_DE.png){ width=63px }               | :material-cancel:        | :material-cancel:               | :material-cancel: |
| ![Papierkorb](assets/s_trash_DE.png){ width=80px }          | :material-cancel:        | :material-cancel:               | :material-cancel: |
| **Admin-Tools**                                                                                                                              |
| Mitgliederverwaltung                                        | :material-cancel:        | :material-cancel:               | Lesend            |
| Bewertungswerkzeug                                          | :material-cancel:        | :material-cancel:               | Vollzugriff       |
| Lektionen&Absenzen                                          | :material-cancel:        | :material-cancel:               | Vollzugriff       |
| **Module**                                                                                                                                   |
| Coaching - Lektionen&Absenzen                               | :material-cancel:        | :material-cancel:               | Vollzugriff       |
| Coaching - Kurse                                            | :material-cancel:        | :material-cancel:               | :material-cancel: |
| Lektionenverwaltung                                         | :material-cancel:        | :material-cancel:               | :material-cancel: |