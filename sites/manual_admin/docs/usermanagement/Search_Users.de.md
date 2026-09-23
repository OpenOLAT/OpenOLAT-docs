# Kontosuche {: #search_user}

Benutzerverwalter:innen und Administrator:innen können auf unterschiedliche Weise nach bestimmten Benutzer:innen/Konten suchen:

!!! note "Quick Links"

    * [Eingabe von Kriterien im Suchformular](#search_user_form)
    * [Konten nach unterschiedlichen Rollen und Zuordnungen anzeigen lassen](#search_user_roles)
    * [Quick Search](#search_user_quick_search)
    * [Massensuche](#search_user_bulk_search)
    * [Suchergebnisse filtern](#search_user_filter_searchresults)
    * [Spalten der Ergebnistabelle](#search_user_result_columns)



## Eingabe von Kriterien im Suchformular {: #search_user_form}

Geben Sie Ihre relevanten Suchkriterien ein und bestätigen Sie mit der "Return"-Taste oder durch Klick auf den Button "Suchen".

![Suchfelder von Anmeldename bis Kontoablauf, gegliedert in Personalien, Adresse, Institution, Rollen, Authentifizierung und Kontostatus: Kontosuche mit dem Suchformular](assets/user_management_search_form_v2_de.png){ class="shadow lightbox" }

Über der Ansicht stehen die Aktionen "Konto erstellen", "Konten importieren", "Temporäres Konto erstellen" und "Konten löschen".

Das Feld "Kontoablauf" sucht nach dem Ablaufdatum der Konten. Die Auswahl links bestimmt die Richtung: "Kontoablauf in den nächsten" findet Konten, die demnächst ablaufen, "Inaktiv seit den letzten" findet Konten, deren Ablauf zurückliegt. Rechts geben Sie die Anzahl und die Einheit an, etwa 30 Tage.

[Zum Seitenanfang ^](#search_user)


## Konten nach unterschiedlichen Rollen und Zuordnungen anzeigen lassen {: #search_user_roles}

Wählen Sie links im Menü eines der relevanten Suchkriterien und nehmen Sie eine Eingrenzung vor.

![Linkes Menü mit den Einstiegen Organisationen, Organisationsrollen, Kursrollen, Gruppenrollen, Course Planner Rollen, Kontorollen, Kontotypen, Status und Vordefinierte Suchabfragen: Kontosuche](assets/user_management_search_left_menu_v2_de.png){ class="shadow lightbox" }

### Organisationen

Verwendet eine OpenOlat Instanz mehrere "Organisationen", lassen sich die Konten hier danach sortiert darstellen.

### Organisationsrollen

Folgende Organisationsrollen werden unterschieden und können für eine
gefilterte Darstellung verwendet werden:

* Alle Systembenutzer:innen
* Autor:innen
* Gruppenverwalter:innen
* Absenzenverwalter:innen
* Projektverwalter:innen
* Qualityverwalter:innen
* Poolverwalter:innen
* Benutzerverwalter:innen
* Rollenverwalter:innen
* Kursplaner:innen
* Lernressourcenverwalter:innen
* Linienvorgesetzte
* Ausbildungsverantwortliche
* Principals
* Administrator:innen
* Systemadministrator:innen


### Kursrollen

Es werden drei Kursrollen unterschieden:

  * Kursbesitzer:innen
  * [Kursbetreuer:innen](../../manual_user/basic_concepts/Roles_Rights.de.md#kursbezogene-rollen-und-rechte) und
  * Kursteilnehmer:innen

Die Mitglieder der jeweiligen Rollen können hier angezeigt und bearbeitet
werden.

### Gruppenrollen

Es existieren zwei Gruppenrollen, die angezeigt und bearbeitet werden können: 

* [Gruppenbetreuer:innen](../../manual_user/groups/Group_Administration.de.md) und 
* Gruppenteilnehmer:innen 


### Course Planner Rollen

Nutzt eine OpenOlat Instanz den Course Planner, stehen neben üblichen Kursrollen noch weitere Rollen zur Verfügung, deren Mitglieder angezeigt und bearbeitet werden können.

* Produktbesitzer:innen
* Elementbesitzer:innen
* Klassenlehrer:innen
* Kursbesitzer:innen
* Kursbetreuer:innen
* Kursteilnehmer:innen


### Kontorollen

Je nach Konfiguration stehen hier weitere Rollen zur Verfügung, die gefiltert angezeigt und definiert werden können. Sie richten sie in der System-Administration ein unter:<br>
`Administration > Module > Benutzer zu Benutzer`, siehe [Module](../administration/Modules.de.md)

Zum Beispiel:

* Vorgesetze:r
* Untergebene:r
* Lehrlingsverantwortliche:r
* Lehrling
* Expert:in
* Mentor:in
* Mentee
* Zu Beurteilende:r
* ...


### Kontotypen

Hier suchen Sie innerhalb vorselektierter Kontotypen. 

* Externe Konten
* Registrierte Konten
* Anonyme Konten


### Status {: #status}

Hier können angezeigt werden:

* Ausstehende Konten
* Inaktive Konten
* Gesperrte Konten 
* Gelöschte Konten



![Tabelle der gelöschten Konten mit Del_Anmeldename, Gelöscht am, Erstellt und Gelöscht von, links der aufgeklappte Eintrag Status: Kontosuche mit Status Gelöschte Konten](assets/user_management_search_status_v2_de.png){ class="shadow lightbox" }


Die Tabelle "Gelöschte Konten" in der Benutzerverwaltung enthält folgende Spalten, die im Löschprozess eine Rolle spielen:

  *  **Del_Anmeldename:** Im Löschprozess ersetzt OpenOlat den Anmeldenamen des gelöschten Kontos durch eine ID.
  *  **Vorname / Nachname:** Trug das gelöschte Konto eine administrative Rolle, stehen Vor- und Nachname hier. Über die Aktion "Entfernen" löschen Sie auch diese Daten.
  *  **Gelöscht am:** Datum der Löschung
  *  **Letzte Anmeldung:** Datum der letzten Anmeldung
  *  **Erstellt:** Datum der Kontenerstellung
  *  **Rollen:** Die administrativen Rollen des gelöschten Kontos
  *  **Gelöscht von:** Person, die die Löschung vorgenommen hat
  *  **Filter entfernen:** Spalte mit der Aktion "Entfernen", die Vor- und Nachname administrativer Konten löscht.


!!! tip "Spaltentitel anzeigen"

    Sollte eine Spalte nicht angezeigt sein, können Sie sie über das Zahnrad-Icon rechts über der Tabelle einblenden.



### Vordefinierte Suchabfragen

Unter dem Menü "**Vordefinierte Suchabfragen**" finden Sie oft benutzte Suchabfragen:

* Konten ohne Gruppen
* Fehlende Authentifizierung
* Konten, welche in der letzten Woche neu dazugekommen sind
* Konten, welche im letzten Monat neu dazugekommen sind
* Konten, welche im letzten Halbjahr neu dazugekommen sind
* Neue Konten

[Zum Seitenanfang ^](#search_user)


## Quick Search {: #search_user_quick_search}

Zur schnellen Suche geben Sie einfach einen Begriff oder einen Teil davon in das Feld "Quick Search" ein.

![Markiertes Eingabefeld mit dem Button Quick Search über den übrigen Suchfeldern: Kontosuche mit dem Suchformular](assets/user_management_quick_search_v2_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#search_user)


## Massensuche {: #search_user_bulk_search}

![Markierter Link Massensuche neben der Überschrift Kontosuche: Suchformular](assets/user_management_bulk_search_v2_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#search_user)


## Suchergebnisse filtern {: #search_user_filter_searchresults}

Wird nach einer Suchaktion eine Liste mit den Suchergebnissen angezeigt, kann darin mit Hilfe von Filtern die Auswahl in einem zweiten Schritt weiter spezifiziert werden.<br>
**Beispiel**:<br>
Sie suchen im ersten Schritt alle Konten, die einer bestimmten Organisationseinheit angehören.<br>
Im zweiten Schritt filtern Sie in den Ergebnissen alle inaktiven Konten dieser Organisationseinheit heraus.

![Filterreihe mit Status, Organisationen, Inaktivierung und Mehr über der Trefferliste, das Auswahlfeld Status ist aufgeklappt: Suchergebnis der Kontosuche](assets/user_management_filter_searchresults_v2_de.png){ class="shadow lightbox" }

Über der Trefferliste stehen die Filter-Tabs "Alle", "Aktiv", "Aktiv und nicht löschbar", "Ausstehende", "Inaktiv" und "Login gesperrt" sowie die Filter "Status", "Organisationen" und "Inaktivierung". Der Filter "Inaktivierung" grenzt auf einen Zeitraum ein, in dem Konten deaktiviert wurden oder deaktiviert werden.

[Zum Seitenanfang ^](#search_user)


## Spalten der Ergebnistabelle [:octicons-tag-16:{ title="ab Release 21.1 (OO-8382)" }](https://track.frentix.com/issue/OO-8382) {: #search_user_result_columns}

Die Trefferliste führt neben den Personendaten fünf Spalten zum Lebenszyklus eines Kontos. Sie stehen in dieser Reihenfolge und beantworten die Frage, wann OpenOlat ein Konto automatisch deaktiviert oder löscht.

OpenOlat deaktiviert ein Konto, das sich in der eingestellten Frist nicht anmeldet. Die Oberfläche nennt diesen Schritt "Inaktivierung", das Konto trägt danach den Status "Inaktiv", siehe [Deaktivierung und Reaktivierung](../administration/Life_cycles_-_Administration.de.md#account_reactivation).

| Spalte | Bedeutung |
|--------|-----------|
| Kontoablauf | Das pro Konto hinterlegte Ablaufdatum. |
| Tage bis Ablauf | Verbleibende Tage bis zu diesem Datum. |
| Tage bis Inaktivierung | Verbleibende Tage, bis OpenOlat das Konto deaktiviert. Nur vorhanden bei aktivem Schalter "Konten nach Inaktivität deaktivieren". |
| Inaktivierungsdatum | Datum, an dem das Konto deaktiviert wurde. |
| Tage bis Löschung | Verbleibende Tage bis zur automatischen Löschung. Nur vorhanden bei aktivem Schalter "Inaktive Konten löschen". |

Die beiden Schalter setzen Sie in der System-Administration unter:<br>
`Administration > Lebenszyklen > Konto`, siehe [Lebenszyklen: Konto](../administration/Life_cycles_-_Administration.de.md#lifecycle_accounts)

Alle fünf Spalten sind standardmässig ausgeblendet. Blenden Sie sie über das Zahnrad-Symbol rechts über der Tabelle ein.

Dieselben Fristen führt der Reiter "Konto" einer einzelnen Person, siehe [Konto konfigurieren](Configure_User.de.md#automatic_user_lifecycle).

[Zum Seitenanfang ^](#search_user)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Rollen und Rechte >](../../manual_user/basic_concepts/Roles_Rights.de.md)<br>
[Gruppenverwaltung >](../../manual_user/groups/Group_Administration.de.md)<br>
[Module >](../administration/Modules.de.md)<br>
[Lebenszyklen: Administration >](../administration/Life_cycles_-_Administration.de.md)<br>
[Konto konfigurieren >](Configure_User.de.md)

**Weiterführend**<br>
[Konto erstellen >](Create_User.de.md)<br>
[Benutzer:in löschen >](Delete_User.de.md)

[Zum Seitenanfang ^](#search_user)
