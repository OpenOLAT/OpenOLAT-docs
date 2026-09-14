# Modul Räume [:octicons-tag-16:{ title="ab Release 21.0 (OO-9460)" }](https://track.frentix.com/issue/OO-9460){:target="_blank"} {: #module_rooms}


Mit dem Modul «Räume» verwalten Sie physische Räume in Gebäuden zentral in OpenOlat und buchen sie für Termine im Course Planner. Standort, Kapazität und Belegung eines Raums sind so an einer Stelle gepflegt und stehen für die Terminplanung zur Verfügung.


## Modul aktivieren {: #activation}

Das Modul wird von einer Person mit administrativer Rolle in der System-Administration aktiviert:<br>
`Administration > Module > Räume > Einstellungen`

Über den Schalter «Modul "Räume"» schalten Sie das Modul ein. Erst danach erscheinen die Segmente «Gebäude», «Räume» und «Raumplanung» sowie im Course Planner der schreibgeschützte Bereich «Raumverwaltung».

!!! info "Termine ohne Räume"
    Ist das Modul ausgeschaltet, sind diese Ansichten ausgeblendet und an Terminen lassen sich keine Räume buchen.

### Modulabhängigkeiten [:octicons-tag-16:{ title="ab Release 21.0.2 (OO-9641)" }](https://track.frentix.com/issue/OO-9641){:target="_blank"} {: #module_dependencies}

Der Abschnitt «Modulabhängigkeiten» zeigt den Zustand der beiden Module, in denen Räume gebucht werden: «Course Planner» und «Termine / Absenzen». Je Modul steht dort «Aktiviert» oder «Deaktiviert». Beim Course Planner steht zusätzlich, welcher Rollenkreis die Site erreicht, zum Beispiel «Kursplaner:innen, Produkt- und Elementbesitzer:innen, Zertifikatsprogrammbesitzer:innen». Diesen Rollenkreis legen Sie fest unter: [Customizing: Sites >](Customizing.de.md#sites)

Ist eines der beiden Module deaktiviert, entstehen dort keine Raumbuchungen. Die Raumverwaltung bleibt bedienbar, die Raumplanung führt dann aber keine Buchungen aus diesem Modul.


## Gebäude [:octicons-tag-16:{ title="ab Release 21.0 (OO-9522)" }](https://track.frentix.com/issue/OO-9522){:target="_blank"} {: #buildings}

Die Gebäude verwalten Sie in der System-Administration unter:<br>
`Administration > Module > Räume > Gebäude`

Jeder Raum gehört zu einem Gebäude. Im Segment «Gebäude» legen Sie die Gebäude Ihrer Organisation an und pflegen deren Stammdaten. Über die Aktion «Erstellen» öffnen Sie den Dialog «Gebäude erstellen» mit den folgenden Angaben:

#### Kennzeichen (Pflichtfeld) {: #building_identifier }

Das massgebende Identifikationsmerkmal des Gebäudes, zum Beispiel ein Kürzel oder eine Hausnummer. Es wird überall dort angezeigt, wo auf das Gebäude verwiesen wird.

#### Beschreibung {: #building_description }

Ein optionaler Klartext-Name wie «Hauptgebäude». Ist eine Beschreibung gesetzt, erscheint sie zusätzlich zum Kennzeichen.

#### Farbe {: #building_color }

Eine Farbe zur schnellen Wiedererkennung des Gebäudes in Listen und im Kalender.

#### Organisationseinschränkung {: #building_org_restriction }

Standardmässig steht ein Gebäude der ganzen Organisation zur Verfügung. Ist der Schalter aktiviert, wählen Sie unter «Administrative Freigabe» die Organisationen aus, für die das Gebäude nutzbar sein soll.

#### Standort {: #building_location }

Unter «Adresse» erfassen Sie die Anschrift. Mit «Auf Karte finden» wird die Position auf der Karte gesetzt. Über die Karte öffnen Sie den Standort direkt in Apple Maps oder Google Maps.

#### Info-URL und Weitere Informationen {: #building_info }

Optionale Zusatzangaben, etwa ein Link zu einer Gebäudeseite oder ein Hinweis wie «Schlüssel beim Empfang beziehen».

Ein Gebäude hat den Status «Aktiv», «Inaktiv» oder «Gelöscht». Wird ein Gebäude deaktiviert, werden auch alle seine Räume inaktiv. Löschen ist nur bei einem inaktiven Gebäude möglich und entfernt auch dessen Räume. Solange für Räume des Gebäudes noch aktive Buchungen bestehen, ist das Löschen nicht möglich. Mit den vordefinierten Filtern «Alle», «Relevant» (nur aktive Gebäude) und «Gelöscht» steuern Sie, welche Gebäude die Liste zeigt.


## Räume [:octicons-tag-16:{ title="ab Release 21.0 (OO-9524)" }](https://track.frentix.com/issue/OO-9524){:target="_blank"} {: #rooms}

Die Räume verwalten Sie in der System-Administration unter:<br>
`Administration > Module > Räume > Räume`

Im Segment «Räume» legen Sie die einzelnen Räume an und ordnen sie einem Gebäude zu. Im Dialog «Raum erstellen» stehen unter anderem folgende Felder zur Verfügung:

#### Kennzeichen (Pflichtfeld) {: #room_identifier }

Das Identifikationsmerkmal des Raums, zum Beispiel die Raumnummer.

#### Beschreibung {: #room_description }

Ein optionaler Name des Raums, etwa «Aula».

#### #Plätze (Pflichtfeld) {: #room_seats }

Die Anzahl Sitzplätze. Der Wert muss grösser als 0 sein und dient dazu, bei einer Buchung zu wenig Kapazität zu erkennen.

#### Gebäude (Pflichtfeld) {: #room_building }

Das Gebäude, zu dem der Raum gehört. Zur Auswahl stehen die aktiven Gebäude.

#### Weitere Informationen {: #room_notes }

Allgemeine Zusatzangaben zum Raum.

#### Administrative Informationen {: #room_admin_info }

Angaben, die nur für Personen mit einer administrativen Rolle sichtbar sind, zum Beispiel Hinweise zur Ausstattung.

In der Raumliste sehen Sie zu jedem Raum unter anderem den «Nächsten Termin» und die «Belegung» (Auslastung des laufenden Monats). Ein Symbol öffnet den «Kalender» des Raums mit seiner Belegung, über «Details» rufen Sie die Vorschau des Raums mit Standort und Karte auf. Neben der Tabellen- steht auch eine Kalenderansicht zur Verfügung.

Ein Klick auf einen Kalendereintrag öffnet das Callout «Buchung» mit den Angaben zur Raumbuchung. Es steht in jeder Kalenderansicht der Raumverwaltung zur Verfügung, auch im Kalender einer einzelnen Raumzeile. [:octicons-tag-16:{ title="ab Release 21.0.3 (OO-9715)" }](https://track.frentix.com/issue/OO-9715){:target="_blank"} Was im Callout steht, beschreibt der Abschnitt [Raumplanung im Course Planner >](../../manual_user/area_modules/Course_Planner_Rooms.de.md#room_scheduling).

Wie beim Gebäude hat ein Raum den Status «Aktiv», «Inaktiv» oder «Gelöscht». Ein inaktiver Raum kann nicht mehr gebucht werden; bereits vorgenommene Buchungen behalten ihre Gültigkeit. Ein Raum lässt sich nicht löschen, solange für ihn aktive Buchungen bestehen.


## Raumplanung [:octicons-tag-16:{ title="ab Release 21.0 (OO-9525)" }](https://track.frentix.com/issue/OO-9525){:target="_blank"} {: #room_scheduling}

Die Raumplanung finden Sie in der System-Administration unter:<br>
`Administration > Module > Räume > Raumplanung`

Das Segment «Raumplanung» bündelt alle Raumbuchungen als Übersicht. Filter sowie eine Kalenderansicht stehen zur Verfügung.

Dieselbe Ansicht erreichen Kursplaner:innen im Course Planner unter `Course Planner > Tools > Raumverwaltung`. Sie unterscheidet sich nur durch die Hinweiszeile, die hier über der Tabelle steht. Die Warnungen, die Filter, die aufklappbare Detailansicht einer Buchung und das Callout «Buchung» in der Kalenderansicht sind dort beschrieben: [Raumplanung im Course Planner: Details >](../../manual_user/area_modules/Course_Planner_Rooms.de.md#room_scheduling)


---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Customizing: Übersicht >](Customizing.de.md)<br>
[Course Planner: Raumverwaltung >](../../manual_user/area_modules/Course_Planner_Rooms.de.md)

**Weiterführend**<br>
[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Termine >](../../manual_user/area_modules/Course_Planner_Events.de.md)

[Zum Seitenanfang ^](#module_rooms)
