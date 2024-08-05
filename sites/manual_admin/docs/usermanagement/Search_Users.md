# User search / Account search {: #search_user}

Benutzerverwalter:innen und Administrator:innen können auf unterschiedliche Weise nach bestimmten Benutzer:innen/Konten suchen:

!!! note "Quick Links"

    * [Eingabe von Kriterien im Suchformular](#search_user_form)
    * [Benutzer nach unterschiedlichen Rollen und Zuordnungen anzeigen lassen](#search_user_roles)
    * [Quicksearch](#search_user_quick_search)
    * [Massensuche](#search_user_bulk_search)
    * [Suchergebnisse filtern](#search_user_filter_searchresults)



## Eingabe von Kriterien im Suchformular {: #search_user_form}

Geben Sie Ihre relevanten Suchkriterien ein und bestätigen Sie mit der "Return"-Taste oder duruch Klick auf den Button "Suchen".

![user_management_search_form_v1_de.png](assets/user_management_search_form_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#search_user)


## Benutzer nach unterschiedlichen Rollen und Zuordnungen anzeigen lassen {: #search_user_roles}

Wählen Sie links im Menü eines der relevanten Suchkriterien und nehmen Sie eine Eingrenzung vor.

![user_management_search_left_menu_v1_de.png](assets/user_management_search_left_menu_v1_de.png){ class="shadow lightbox" }

### Organizations

If an OpenOlat instance uses several "organizations", the users can be
displayed here sorted accordingly.


### Organizational Roles

The following organizational roles are distinguished and can be used for a filtered display:

* Alle Systembenutzer:innen
* Autor:innen
* Gruppenverwalter:innen
* Lektionenblockverwalter:innen
* Projektverwalter:innen
* Qualityverwalter:innen
* Poolverwalter:innen
* Benutzerverwalter:innen
* Rollenverwalter:innen
* Curriculumverwalter:innen
* Lernressourcenverwalter:innen
* Linienvorgesetzte
* principals
* administrators
* Systemadministrator:innen


### Course Roles

We distiguish three course roles:

  * course owners,
  * [course coaches](../../manual_user/basic_concepts/Roles_Rights.md#course-rights-and-roles) and
  * course participants.

The members of the respective roles can be displayed and edited here.


### Group Roles

There are two group roles, which can be displayed and edited: 

* [group coaches](../../manual_user/groups/Group_Administration.md) and 
* group participants. 


### Curriculum Roles

If an OpenOlat instance uses the curriculum, there are other roles available in addition to the usual course roles, whose members can be displayed and edited.

* Curriculumbesitzer:innen
* Curriculumelementbesitzer:innen
* Klassenlehrer:innen
* Kursbesitzer:innen
* Kursbetreuer:innen
* Kursteilnehmer:innen


### Kontorollen 
(Vor Version 19.0: Benutzerrollen)

Je nach Konfiguration in der Administration im Bereich "[Modules](../administration/Modules.de.md)" → "Benutzer zu Benutzer" stehen hier weitere Rollen zur Verfügung, die gefiltert angezeigt und definiert werden können:

* Vorgesetze:r
* Untergebene:r
* Expert:in
* Zu Beurteilende:r


### Kontotypen

Hier suchen Sie innerhalb vorselektierter Kontentypen. 

* Externe Konten
* Registrierte Konten
* Anonyme Konten


### Status

Hier können angezeigt werden:

* ausstehende Benutzerkonten
* inaktive Konten
* gesperrte Konten 
* gelöschte Konten



![user_management_search_status_v1_de.png](assets/user_management_search_status_v1_de.png){ class="shadow lightbox" }


Die Tabelle "**Gelöschte Benutzer**" in der Benutzerverwaltung enthält folgende
Informationen (Spaltentitel), die im Prozess der Benutzer-Löschung relevant sind:

  *  **Del_Anmeldename:**  Im Lösch-Prozess wird der Benutzername des gelöschten Nutzers durch eine ID ersetzt.
  *  **Vorname / Nachname:**  Handelt es sich bei dem gelöschten um einen administrativen Benutzer, so werden Vor- und Nachname hier angezeigt. Diese Daten können bei Bedarf über die Aktion «Entfernen» ebenfalls gelöscht werden.
  *  **Gelöscht am:** Datum der Löschung
  *  **Letzte Anmeldung:** Datum der letzten Anmeldung
  *  **Erstellt:** Datum der Kontenerstellung
  *  **Rollen:**  Anzeige der administrativen Rollen der Person, die gelöscht wurde
  *  **Gelöscht von:** Person, die die Löschung vorgenommen hat
  *  **Filter entfernen:**  Aktion zur Löschung des Vor- und Nachnamens von administrativen Benutzern.


!!! tip "Spaltentitel anzeigen"

    Sollte eine Spalte nicht angezeigt sein, können Sie sie über das Zahnrad-Icon rechts über der Tabelle einblenden.



### Vordefinierte Suchabfragen

Unter dem Menü "**Vordefinierte Suchabfragen**" finden Sie oft benutzte Suchabfragen:

* Konten ohne Gruppen
* Fehlende Authentifizierung
* Benutzer, welche in der letzten Woche neu dazugekommen sind
* Benutzer, welche im letzten Monat  neu dazugekommen sind
* Benutzer, welche im letzten Halbjahr neu dazugekommen sind
* Neue Konten

[Zum Seitenanfang ^](#search_user)


## Quicksearch {: #search_user_quick_search}

Zur schnellen Suche geben Sie einfach einen Begriff oder einen Teil davon in das Feld "Quick Search" ein.

![user_management_quick_search_v1_de.png](assets/user_management_quick_search_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#search_user)


## Massensuche {: #search_user_bulk_search}

![user_management_bulk_search_v1_de.png](assets/user_management_bulk_search_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#search_user)


## Suchergebnisse filtern {: #search_user_filter_searchresults}

Wird nach einer Suchaktion eine Liste mit den Suchergebnissen angezeigt, kann darin mit Hilfe von Filtern die Auswahl in einem zweiten Schritt weiter spezifiziert werden.<br>
**Beispiel**:<br>
Sie suchen im ersten Schritt alle Benutzer, die einer bestimmten Organisationseinheit angehören.
Im zweiten Schritt filtern Sie in den Ergebnissen alle inaktiven Benutzer dieser Organisationseinheit heraus.
 
![user_management_filter_searchresults_v1_de.png](assets/user_management_filter_searchresults_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#search_user)


