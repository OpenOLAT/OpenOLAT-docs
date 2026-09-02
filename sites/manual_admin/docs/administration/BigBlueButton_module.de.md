# Modul BigBlueButton {: #bbb}

Das virtuelle Klassenzimmer BigBlueButton wird in der System-Administration aktiviert:<br>
`Administration > Externe Werkzeuge > BigBlueButton`

Dieser Artikel beschreibt die Konfiguration von mehreren BigBlueButton-Servern, das Load-Balancing und das Einrichten von systemweiten Raumvorlagen.

Die Anleitung zur Konfiguration von einzelnen Online-Terminen für Kursbesitzer:innen wird im Kapitel [Kursbaustein "BigBlueButton"](../../manual_user/learningresources/bigbluebutton/index.de.md) beschrieben.

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

![Freischaltung je Einsatzort, Serverliste, Aufzeichnungen Handler und Löschfrist der Online-Termine; Tab Konfiguration im Modul BigBlueButton](assets/bbb_admin_config_v1_de.png){ class="shadow lightbox" }


### BigBlueButton-Server hinzufügen {: #add_server}

Mit Klick auf den Button "Server hinzufügen" im Tab "Konfiguration" öffnen Sie ein Popup für die Angaben.

  *  **BigBlueButton API URL:** URL BBB-Server
  *  **Shared secret:** API Key BBB-Server
  *  **Capacity factor:** Server-Gewichtung im Load-Balancing
  *  **Server aktivieren:** Server steht für das Load-Balancing zur Verfügung
  *  **Nur manuelle Auswahl:** Nur manuell ausgewählte Server stehen für das Load-Balancing zur Verfügung
  *  **Button "Serververbindung testen":** Prüft den Zugriff auf den hier angegebenen Server.

![API URL und Shared secret sind Pflicht, Serververbindung testen prüft die Angaben vor dem Speichern; Dialog Server hinzufügen](assets/bbb_admin_add_server_v1_de.png){ class="shadow lightbox" }


---

## Tab "Server" {: #tab_server}

Hier werden die zur Verfügung stehenden BigBlueButton-Server pro OpenOlat-Instanz angezeigt.

![Je Server Kapazität und aktuelle Last, der Filter trennt dieses OpenOlat von allen OpenOlats; Tab Server im Modul BigBlueButton](assets/bbb_admin_server_v1_de.png){ class="shadow lightbox" }


### Load-Balancing [:octicons-tag-16:{ title="ab Release 14.2.7 (OO-4626)" }](https://track.frentix.com/issue/OO-4626) {: #load_balancing}

Ziel ist es, die erzeugte Last von gleichzeitigen Online-Terminen durch die Berücksichtigung von Performance-Parametern (wie Anzahl Videos und Anzahl Teilnehmende der Meetings) auf die verfügbaren BigBlueButton-Server zu verteilen. OpenOlat besitzt dazu ein integriertes Load-Balancing. Beim initialen Start des Online-Termins (je nach Konfiguration durch die Moderator:in oder die erste teilnehmende Person) wird der Server mit der geringsten Auslastung für das Meeting ausgewählt. Die Auslastung berechnet sich aus den unterschiedlichen Messfaktoren und gewichtet das Ergebnis mit dem Kapazitätsfaktor.

Über den Filter zeigen Sie die Kennzahlen für alle OpenOlat-Instanzen auf dem BigBlueButton-Server ("Alle OpenOlats") oder nur für die Sessions dieser Instanz ("Dieses OpenOlat") an.

### Kapazitätsfaktor {: #capacity_factor}

Der Kapazitätsfaktor wird mit einem Wert zwischen 1 und 100 pro Server erfasst. Die berechnete Anzahl Benutzer:innen auf dem Server wird mit dem Kapazitätsfaktor multipliziert. Bei der Zählung wiegen Video-Benutzer:innen am stärksten, dann Audio-Benutzer:innen, dann Viewer. Somit gleicht sich ein Server mit stärkerer Performance (RAM/CPU/Disk) einem schwächeren an.


---

## Tab "Raumvorlagen" {: #tab_room-templates}

Die Raumvorlagen stehen bei der Erstellung eines neuen Online-Termins zur Auswahl. Die Vorlagen steuern:

  * Die zur Verfügung stehenden Funktionen und Standard-Einstellungen im Online-Termin.
  * Die Anzahl möglicher gleichzeitiger Teilnehmer:innen pro Raum.
  * Einschränkungen betreffend Dauer und Anzahl der zur Verfügung stehenden Online-Räume.

Mit dem Button "Raumvorlage erstellen" legen Sie eine neue Raumvorlage an. Die mitgelieferten Systemvorlagen (Spalte "System") lassen sich bearbeiten, aber nicht löschen.

![Je Vorlage Räume, Teilnehmer:innen und Dauer, Systemvorlagen ohne Löschen-Link; Tab Raumvorlagen im Modul BigBlueButton](assets/bbb_admin_room-templates_v1_de.png){ class="shadow lightbox" }


### Konfiguration Raumvorlage {: #room_config}

  *  **Raumname:** Bezeichnung der Raumvorlage
  *  **Beschreibung:** Beschreibung der Raumvorlage (z.B. Lernszenario, Einsatzgebiet)
  *  **Anzahl Teilnehmer:innen:** Maximale Anzahl Teilnehmer:innen (Viewer)
  *  **Dauer (Minuten):** Maximale Länge der Online-Termine
  *  **Raumvorlage aktivieren:** Aktivierte Raumvorlagen stehen in Kursen/Gruppen für neue Online-Termine zur Verfügung und können von Kursbesitzer:innen gewählt werden
  *  **Anzahl Räume:** Maximale Anzahl der gleichzeitigen Räume dieser Raumvorlage
  *  **Offen für externe Benutzer:innen:** OpenOlat generiert automatisch einen Direktlink für Externe, so dass sie den BigBlueButton-Raum betreten können, ohne vorher OpenOlat aufzurufen. Der Link wird in der Raumkonfiguration angezeigt und kann bei Bedarf von Kursbesitzer:innen oder Betreuer:innen geändert und an Gäste weitergegeben werden.
  *  **Benutzer:in bei Eintritt akzeptieren (Warteraum):**
     * Abgeschaltet (Alle können sofort eintreten.)
     * Alle Benutzer:innen (Jeder Zutritt muss bestätigt werden.)
     * Nur Gäste und externe Benutzer:innen (Nur der Zutritt von Gästen und externen Benutzer:innen muss bestätigt werden.)
  *  **Raumvorlage aktiviert für:** Bestimmt, welche Rollen die Raumvorlage für neue Online-Termine nutzen können. Wird die Option "Gruppenmitglied" aktiviert, kann die Vorlage auch in OpenOlat [Gruppen](../../manual_user/groups/Using_Group_Tools.de.md) verwendet und weiter konfiguriert werden.

![Raumname, Teilnehmer:innen und Dauer bestimmen den Raum, die Liste unten gibt die Vorlage je Rolle frei; Formular der Raumvorlage](assets/bbb_admin_room-template_config_v1_de.png){ class="shadow lightbox" }


### Voreinstellungen der Raumvorlage

![Je Verhalten eine Ja-Nein-Wahl, von Moderatorenkamera bis zum automatischen Sperren beim Eintritt; Voreinstellungen im Formular der Raumvorlage](assets/bbb_admin_room-template_default_v1_de.png){ class="shadow lightbox" }


### Voreinstellungen für gesperrte Teilnehmer:innen

![Sieben Ja-Nein-Wahlen legen fest, was die Sperre abschaltet, von Kamera bis Layoutanpassung; Abschnitt Für gesperrte Teilnehmer:innen im Formular der Raumvorlage](assets/bbb_admin_room-template_default_locked_participants_v1_de.png){ class="shadow lightbox" }


---

## Tab "Online-Termine" {: #tab_online-meetings}

Übersicht der konfigurierten Online-Termine mit der Möglichkeit, direkt in den Kurs oder die Gruppe (Kontext) zu wechseln oder den Online-Termin zu löschen. Über die Suche finden Sie gezielt einzelne BigBlueButton-Räume, markieren sie und löschen sie bei Bedarf gesammelt.

![Alle Online-Termine der Instanz mit Raumvorlage, Server und Kontext, Suchfeld und Mehrfachauswahl zum Löschen; Tab Online-Termine im Modul BigBlueButton](assets/bbb_admin_online-meetings_v1_de.png){ class="shadow lightbox" }


---

## Tab "Kalender" {: #tab_calendar}

Kalenderübersicht über alle erfassten Online-Termine, um Zeiten mit hoher Belegung zu prüfen und Überschneidungen grafisch anzuzeigen.

![Alle Online-Termine der Instanz in der Wochenansicht, umschaltbar auf Monat, Tag und Jahr; Tab Kalender im Modul BigBlueButton](assets/bbb_admin_calendar_v1_de.png){ class="shadow lightbox" }


---

## Weiterführende Informationen {: #further_information}

[Kursbaustein "BigBlueButton" >](../../manual_user/learningresources/bigbluebutton/index.de.md)<br>
[Gruppenwerkzeuge nutzen >](../../manual_user/groups/Using_Group_Tools.de.md)<br>
[Virtuelle Klassenzimmer >](../../manual_user/basic_concepts/Virtual_classrooms.de.md)<br>
[Häufig gestellte Fragen - BigBlueButton >](../../manual_user/learningresources/bigbluebutton/faq.de.md)<br>
[Kursbaustein "Terminplanung" >](../../manual_user/learningresources/Course_Element_Appointment_Scheduling.de.md)<br>
[Absenzenverwaltung >](../../manual_user/area_modules/Absence_Management.de.md)

[Zum Seitenanfang ^](#bbb)
