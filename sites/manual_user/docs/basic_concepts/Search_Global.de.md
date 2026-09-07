# Globale Suche {: #search_global}

Die globale Suche finden Sie oben rechts in der Kopfzeile. Klicken Sie auf das Lupen-Symbol.

Wenn Sie hier einen Suchbegriff eingeben und mit der Eingabetaste oder Klick auf die Lupe daneben bestätigen, findet eine **Suche über Alles** statt.

Das heisst, dass **im ganzen OpenOlat** gesucht wird und auch innerhalb der Dokumente. Es ist eine [Volltextsuche](Search_General.de.md#full_text_search).

![Aufgeklapptes Suchfeld der globalen Suche mit Button Suchen neben dem Lupen-Symbol oben rechts in der Kopfzeile](assets/search_global_v1_de.png){ class="shadow lightbox" }


## Suchergebnisse [:octicons-tag-16:{ title="ab Release 20.1 (OO-8767)" }](https://track.frentix.com/issue/OO-8767) {: #search_results}

In den Suchergebnissen der globalen Suche erscheinen:

* Daten / Dokumente aus Kursen, in denen man selbst Mitglied ist und auf die man als Kursmitglied auch Zugriff hat
* Daten / Dokumente aus Kursen, die unter `Kurs > Administration > Einstellungen > Freigabe` wie folgt konfiguriert sind: "Ohne Buchung" oder "Frei verfügbar"

Personendaten wie Profile, Visitenkarten oder persönliche Ordner werden nicht indexiert und erscheinen nicht in den Suchergebnissen.


## Aktivierung {: #activation}

Die globale Suche ist nur dann sichtbar und nutzbar, wenn der Suchdienst für Ihre OpenOlat Instanz eingeschaltet ist. Diese Einstellung nehmen Administrator:innen in der Server-Konfiguration vor (Eigenschaft `search.service`). Die Einstellungen zur Indexierung finden sich in der System-Administration unter `Administration > Core Konfiguration > Volltextsuche`, siehe [Core Konfiguration: Übersicht](../../manual_admin/administration/Core_functions.de.md). Ist die Suche bei Ihnen nicht sichtbar, wenden Sie sich an den oder die Administrator:in Ihrer OpenOlat Instanz.


## Weiterführende Informationen {: #further_information}

[Allgemeines zur Suche >](Search_General.de.md)<br>
[Core Konfiguration: Übersicht >](../../manual_admin/administration/Core_functions.de.md)<br>
[Lokale Suche >](Search_Local.de.md)<br>
[Personensuche >](Search_Person.de.md)<br>
[Suche in einem Kurs >](Search_in_Course.de.md)<br>
[Suche im File Hub >](Search_in_FileHub.de.md)

[Zum Seitenanfang ^](#search_global)
