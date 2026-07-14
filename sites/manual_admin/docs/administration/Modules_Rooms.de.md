# Modul Räume [:octicons-tag-16:{ title="ab Release 21.0 (OO-9460)" }](https://track.frentix.com/issue/OO-9460){:target="_blank"} {: #module_rooms}


Mit dem Modul «Räume» verwalten Sie physische Räume in Gebäuden zentral in OpenOlat und buchen sie für Termine im Course Planner. Standort, Kapazität und Belegung eines Raums sind so an einer Stelle gepflegt und stehen für die Terminplanung zur Verfügung.


## Modul aktivieren {: #activation}

Das Modul wird von einer Person mit administrativer Rolle aktiviert:<br>
`Administration` > `Räume` > `Einstellungen`

Über den Schalter «Modul "Räume"» schalten Sie das Modul ein. Erst danach erscheinen die Segmente «Gebäude», «Räume» und «Raumplanung» sowie im Course Planner der Bereich «Raumverwaltung».

!!! info "Termine ohne Räume"
    Ist das Modul ausgeschaltet, sind diese Ansichten ausgeblendet und an Terminen lassen sich keine Räume buchen.


## Gebäude [:octicons-tag-16:{ title="ab Release 21.0 (OO-9522)" }](https://track.frentix.com/issue/OO-9522){:target="_blank"} {: #buildings}

Jeder Raum gehört zu einem Gebäude. Im Segment «Gebäude» legen Sie die Gebäude Ihrer Organisation an und pflegen deren Stammdaten. Über die Aktion «Erstellen» öffnen Sie den Dialog «Gebäude erstellen» mit den folgenden Angaben:

* **Kennzeichen** (Pflichtfeld): das massgebende Identifikationsmerkmal des Gebäudes, zum Beispiel ein Kürzel oder eine Hausnummer. Es wird überall dort angezeigt, wo auf das Gebäude verwiesen wird.
* **Beschreibung**: ein optionaler Klartext-Name wie «Hauptgebäude». Ist eine Beschreibung gesetzt, erscheint sie zusätzlich zum Kennzeichen.
* **Farbe**: eine Farbe zur schnellen Wiedererkennung des Gebäudes in Listen und im Kalender.
* **Organisationseinschränkung**: Standardmässig steht ein Gebäude der ganzen Organisation zur Verfügung. Ist der Schalter aktiviert, wählen Sie unter «Administrative Freigabe» die Organisationen aus, für die das Gebäude nutzbar sein soll.
* **Standort**: Unter «Adresse» erfassen Sie die Anschrift. Mit «Auf Karte finden» wird die Position auf der Karte gesetzt. Über die Karte öffnen Sie den Standort direkt in Apple Maps oder Google Maps.
* **Info-URL** und **Weitere Informationen**: optionale Zusatzangaben, etwa ein Link zu einer Gebäudeseite oder ein Hinweis wie «Schlüssel beim Empfang beziehen».

Ein Gebäude hat den Status «Aktiv», «Inaktiv» oder «Gelöscht». Wird ein Gebäude deaktiviert, werden auch alle seine Räume inaktiv. Löschen ist nur bei einem inaktiven Gebäude möglich und entfernt auch dessen Räume. Solange für Räume des Gebäudes noch aktive Buchungen bestehen, ist das Löschen nicht möglich. Mit den vordefinierten Filtern «Alle», «Relevant» (nur aktive Gebäude) und «Gelöscht» steuern Sie, welche Gebäude die Liste zeigt.


## Räume [:octicons-tag-16:{ title="ab Release 21.0 (OO-9524)" }](https://track.frentix.com/issue/OO-9524){:target="_blank"} {: #rooms}

Im Segment «Räume» legen Sie die einzelnen Räume an und ordnen sie einem Gebäude zu. Im Dialog «Raum erstellen» stehen unter anderem folgende Felder zur Verfügung:

* **Kennzeichen** (Pflichtfeld): das Identifikationsmerkmal des Raums, zum Beispiel die Raumnummer.
* **Beschreibung**: ein optionaler Name des Raums, etwa «Aula».
* **#Plätze** (Pflichtfeld): die Anzahl Sitzplätze. Der Wert muss grösser als 0 sein und dient dazu, bei einer Buchung zu wenig Kapazität zu erkennen.
* **Gebäude** (Pflichtfeld): das Gebäude, zu dem der Raum gehört. Zur Auswahl stehen die aktiven Gebäude.
* **Weitere Informationen**: allgemeine Zusatzangaben zum Raum.
* **Administrative Informationen**: Angaben, die nur für Personen mit einer administrativen Rolle sichtbar sind, zum Beispiel Hinweise zur Ausstattung.

In der Raumliste sehen Sie zu jedem Raum unter anderem den «Nächsten Termin» und die «Belegung» (Auslastung des laufenden Monats). Ein Symbol öffnet den «Kalender» des Raums mit seiner Belegung, über «Details» rufen Sie die Vorschau des Raums mit Standort und Karte auf. Neben der Tabellen- steht auch eine Kalenderansicht zur Verfügung.

Wie beim Gebäude hat ein Raum den Status «Aktiv», «Inaktiv» oder «Gelöscht». Ein inaktiver Raum kann nicht mehr gebucht werden; bereits vorgenommene Buchungen behalten ihre Gültigkeit. Ein Raum lässt sich nicht löschen, solange für ihn aktive Buchungen bestehen.


## Raumplanung [:octicons-tag-16:{ title="ab Release 21.0 (OO-9525)" }](https://track.frentix.com/issue/OO-9525){:target="_blank"} {: #room_scheduling}

Das Segment «Raumplanung» bündelt alle Raumbuchungen in einer Übersicht. So erkennen Sie auf einen Blick, welche Räume wann belegt sind und wo es Konflikte gibt.

Mit den vordefinierten Filtern «Alle», «Heute», «Bevorstehend» und «Mit Warnungen» sowie den Filtern nach Gebäude und Raum grenzen Sie die Anzeige ein. Neben der Tabellen- gibt es eine Kalenderansicht. Über «Im Kursplaner öffnen» springen Sie von einer Buchung zum zugehörigen Termin im Course Planner.

Die Spalte «Warnungen» macht auf Konflikte aufmerksam:

* **Doppelbuchung**: «Der Raum "..." ist in diesem Zeitraum doppelt gebucht!»
* **Zu wenig Plätze**: «Es gibt nicht genug Plätze!», wenn die Teilnehmerzahl die Anzahl Sitzplätze übersteigt.
* **Inaktiver Raum**: «Der Raum "..." ist inaktiv!»


---

## Weitere Informationen {: #further_information}

[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Termine >](../../manual_user/area_modules/Course_Planner_Events.de.md)<br>

[Zum Seitenanfang ^](#module_rooms)
