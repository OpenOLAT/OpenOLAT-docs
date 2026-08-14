# Modul BigBlueButton {: #bbb}

Das virtuelle Klassenzimmer BigBlueButton wird in der System-Administration aktiviert:<br>
`Administration > Externe Werkzeuge > BigBlueButton`

Dieser Artikel beschreibt die Konfiguration von mehreren BigBlueButton-Servern, das Load-Balancing und das Einrichten von systemweiten Raumvorlagen.

Die Anleitung zur Konfiguration von einzelnen Online-Terminen für Kursbesitzer
wird im Kapitel [Kursbaustein BigBlueButton](../../manual_user/learningresources/Course_Element_BigBlueButton.de.md) beschrieben.

---

## Tab "Konfiguration" {: #tab_config}

  *  **Modul "BigBlueButton":** Aktivierung der Funktionalität
  *  **Aktivieren für:** Freischaltung der Funktionalität einzeln für Kursbaustein "BigBlueButton", Kurs Termine [:octicons-tag-16:{ title="ab Release 20.0.1 (OO-8237)" }](https://track.frentix.com/issue/OO-8237), Kursbaustein "Terminplanung", Gruppen und Betreuer:innen-Chat
  *  **Online-Termine ohne Datum:** Zusätzliche Möglichkeit neben Online-Terminen auch "permanente Raumreservationen" ohne Datum freizuschalten. Diese sind im Kalender nicht ersichtlich und zählen zu jedem Zeitpunkt in den Limiten der Raumvorlage als belegt.
  *  **Profilbild übernehmen:** Das Profilbild aus dem OpenOlat-Benutzerprofil wird im Online-Termin als Avatar angezeigt. Gäste und Benutzer:innen ohne Profilbild erhalten keinen Avatar [:octicons-tag-16:{ title="ab Release 16.0 (OO-5435)" }](https://track.frentix.com/issue/OO-5435)
  *  **Server:** In der Konfiguration werden die zur Verfügung stehenden BigBlueButton-Server pro OpenOlat-Instanz eingetragen.
  *  **Button "Server hinzufügen":** [Details siehe unten >](#add_server)
  *  **Aufzeichnungen Handler:** Native oder Opencast
  *  **Aufzeichnungen nie löschen:** Die Aufzeichnungen bleiben auf dem externen Server erhalten, auch wenn der Online-Termin oder der Kurs in OpenOlat gelöscht wird. Die Option erscheint nur, wenn als Aufzeichnungen Handler "Opencast" gewählt ist [:octicons-tag-16:{ title="ab Release 15.3.8 (OO-5170)" }](https://track.frentix.com/issue/OO-5170)
  *  **Standardwert für die Veröffentlichung von Aufnahmen:** Voreinstellung, für wen neue Aufzeichnungen sichtbar sind. Zur Auswahl stehen "Besitzer:innen / Betreuer:innen", "Kurs / Gruppe Teilnehmer:innen", "Alle Teilnehmer:innen des Meetings (ausser Gäste)" und "Gäste". Beim Erstellen eines Online-Termins lässt sich die Voreinstellung übersteuern [:octicons-tag-16:{ title="ab Release 20.1.12 (OO-9037)" }](https://track.frentix.com/issue/OO-9037)
  *  **Online-Termine automatisch löschen:** x Tage nach Termin-Ende
  *  **Limit aller Präsentationsdateien pro Meeting (MB):** Pflichtfeld mit Angabe erlaubter Megabyte

![Tab Konfiguration des Moduls BigBlueButton: das Modul wird einzeln für Kursbausteine, Kurstermine, Gruppen und Betreuer:innen-Chat freigegeben, darunter folgen Serverliste, Aufzeichnungs-Handler und Aufbewahrungsfrist der Online-Termine](assets/bbb_admin_config_v1_de.png){ class="shadow lightbox" }


### BigBlueButton-Server hinzufügen {: #add_server}

Mit Klick auf den Button "Server hinzufügen" im Tab Konfiguration öffnen Sie ein Popup für die Angaben.

  *  **BigBlueButton API URL**: URL BBB-Server
  *  **Shared secret**: API Key BBB-Server
  *  **Capacity factor**: Server-Gewichtung im Load-Balancing
  *  **Server aktivieren**: Server steht für das Load-Balancing zur Verfügung
  *  **Nur manuelle Auswahl**: Nur manuell ausgewählte Server stehen für das Load-Balancing zur Verfügung
  *  **Button "Serververbindung testen"**: Eine sehr praktische Hilfe um den Zugriff auf den hier angegebenen Server zu prüfen.

![Dialog Server hinzufügen: API URL und Shared secret sind Pflicht, der Kapazitätsfaktor steuert die Last, mit Serververbindung testen prüfen Sie die Angaben vor dem Speichern](assets/bbb_admin_add_server_v1_de.png){ class="shadow lightbox" }


---

## Tab "Server" {: #tab_server}

Hier werden die zur Verfügung stehenden BigBlueButton-Server pro OpenOlat-Instanz angezeigt.

![Tab Server des Moduls BigBlueButton: je Server zeigt die Liste Kapazität und aktuelle Last mit Meetings, Moderator:innen und Teilnehmer:innen, der Filter trennt dieses OpenOlat von allen OpenOlats](assets/bbb_admin_server_v1_de.png){ class="shadow lightbox" }


### Load-Balancing [:octicons-tag-16:{ title="ab Release 14.2.7 (OO-4626)" }](https://track.frentix.com/issue/OO-4626) {: #load_balancing}

Ziel ist es, die erzeugte Last von gleichzeitigen Online-Terminen durch die Berücksichtigung von Performance-Parametern (wie Anzahl Videos und Anzahl Teilnehmenden der Meetings) auf den verfügbaren BigBlueButton-Server zu verteilen. OpenOlat besitzt dazu ein integriertes Load-Balancing. Beim initialen Start des Online-Termins (je nach Konfiguration durch den Moderator oder den ersten Teilnehmenden) wird der Server mit der geringsten Auslastung für das Meeting ausgewählt. Die Auslastung berechnet sich aus den unterschiedlichen Messfaktoren und gewichtet das Ergebnis mit dem Kapazitätsfaktor. 

Über den Filter können die Server-Kennzahlen über den gesamten BBB-Server oder nur die Sessions des aktuellen OpenOlat-Servers ausgegeben werden.

### Kapazitätsfaktor {: #capacity_factor}

Der Kapazitätsfaktor wird mit einem Wert zwischen 1 und 100 pro Server erfasst. Die berechnete Anzahl Benutzer* auf dem Server wird mit dem Kapazitätsfaktor multipliziert. Somit gleicht sich ein Server mit stärkerer Performance (RAM/CPU/Disk) einem Schwächeren an.

 _* Gewichtung bei der Zählung von Benutzern von hoch zu tief: Video-Benutzer, Audio-Benutzer, Viewer_


---

## Tab "Raumvorlagen" {: #tab_room-templates}

Die Raumvorlagen stehen bei der Erstellung eines neuen Online-Termins zur Auswahl. Die Vorlagen steuern:

  * Die zur Verfügung stehenden Funktionen und Standard-Einstellungen im Online-Termin.
  * Die Anzahl möglicher gleichzeitiger Nutzer pro Raum.
  * Einschränkungen betreffend Dauer und Anzahl der zur Verfügung stehenden Online-Räume.

![Tab Raumvorlagen des Moduls BigBlueButton: je Vorlage legen Räume, Teilnehmerzahl und Dauer den Rahmen fest, die mitgelieferten Systemvorlagen lassen sich bearbeiten, aber nicht löschen](assets/bbb_admin_room-templates_v1_de.png){ class="shadow lightbox" }


### Konfiguration Raumvorlage {: #room_config}

  *  **Raumname:** Bezeichnung der Raumvorlage
  *  **Beschreibung:** Beschreibung der Raumvorlage (z.B. Lernszenario, Einsatzgebiet)
  *  **Anzahl Teilnehmer:innen:** Maximale Anzahl Teilnehmer:innen (Viewer)
  *  **Dauer (Minuten):** Maximale Länge der Online-Termine
  *  **Raumvorlage aktivieren:** Aktivierte Raumvorlagen stehen in Kursen/Gruppen für neue Online-Termine zur Verfügung und können von Kursbesitzern gewählt werden
  *  **Anzahl Räume:** Maximale Anzahl der gleichzeitigen Räume dieser Raumvorlage
  *  **Offen für externe Benutzer:** Es wird automatisch ein Direktlink für Externe generiert, so dass sie den BigBlueButton Raum betreten können ohne vorher OpenOlat aufrufen zu müssen. Der Link wird dann in der Raumkonfiguration angezeigt und kann auch bei Bedarf vom Kursbesitzer oder -Betreuer geändert werden sowie an Gäste weitergegeben werden.
  * **Benutzer:in bei Eintritt akzeptieren (Warteraum):** 
     * Abgeschaltet (Alle können sofort eintreten.)
     * Alle Benutzer:innen (Jeder Zutritt müssen bestätigt werden.)
     * Nur Gäste und externe Benutzer:innen (Nur der Zutritt von Gästen und externen Benutzer:innen muss bestätigt werden.) 
  *  **Raumvorlage aktiviert für:** Bestimmt, welche Rollen die Raumvorlage für neue Online-Termine nutzen können. Wird die Option "Gruppenmitglied" aktiviert, kann die Vorlage auch in OpenOlat [Gruppen](../../manual_user/groups/Using_Group_Tools.de.md) verwendet und weiter konfiguriert werden.

![Konfiguration einer Raumvorlage: Name, Teilnehmerzahl und Dauer bestimmen den Raum, der Warteraum steuert den Eintritt, und die Liste unten gibt die Vorlage je Rolle frei](assets/bbb_admin_room-template_config_v1_de.png){ class="shadow lightbox" }


### Voreinstellungen der Raumvorlage

![Voreinstellungen der Raumvorlage: je Verhalten eine Ja-Nein-Wahl, etwa nur Moderatorenkamera, Aufzeichnungen zulassen, Breakout-Räume und das automatische Sperren der Teilnehmer:innen beim Eintritt](assets/bbb_admin_room-template_default_v1_de.png){ class="shadow lightbox" }


### Voreinstellungen für gesperrte Teilnehmer

![Voreinstellungen für gesperrte Teilnehmer:innen: sieben Ja-Nein-Wahlen bestimmen, was die Sperre abschaltet, von Kamera und Mikrofon über beide Chats bis zu Notizen, Teilnehmerliste und Layoutanpassung](assets/bbb_admin_room-template_default_locked_participants_v1_de.png){ class="shadow lightbox" }


---

## Tab "Online-Termine" {: #tab_online-meetings}

Übersicht der konfigurierten Online-Termine mit der Möglichkeit, direkt in den
Kurs/Gruppe (Kontext) zu wechseln und/oder diesen Online-Termin zu löschen.
Über die Suche können auch gezielt BigBlueButton-Räume ermittelt und zum Beispiel schnell markiert und gelöscht werden.

![Tab Online-Termine des Moduls BigBlueButton: die Liste führt alle Termine der Instanz mit Zeitraum, Raumvorlage, Server, Kontext und Anzahl Aufzeichnungen](assets/bbb_admin_online-meetings_v1_de.png){ class="shadow lightbox" }


---

## Tab "Kalender" {: #tab_calendar}

Kalenderübersicht über alle erfassten Online-Termine, um Zeiten mit hoher Belegung zu prüfen und Überschneidungen grafisch anzuzeigen.

![Tab Kalender des Moduls BigBlueButton: alle Online-Termine der Instanz in der Wochenansicht, umschaltbar auf Monat, Tag und Jahr](assets/bbb_admin_calendar_v1_de.png){ class="shadow lightbox" }



---

## Weitere Informationen

[Anleitung zur Konfiguration von einzelnen Online-Terminen für Kursbesitzer:innen im Kursbaustein BigBlueButton](../../manual_user/learningresources/Course_Element_BigBlueButton.de.md)


