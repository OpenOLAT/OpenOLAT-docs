# Modul Microsoft Teams {: #teams_module}

Microsoft Teams ist die Webkonferenz-Lösung von Microsoft. In Kursen und Gruppen legen Kursbesitzer:innen, Betreuer:innen und Gruppenbetreuer:innen damit Online-Termine an, zu denen die Teilnehmenden aus OpenOlat heraus beitreten. Welche Arten von Online-Terminen dabei zur Wahl stehen, legen Administrator:innen für die ganze Instanz fest, zum Beispiel ob jeder Termin ein Datum braucht und damit im Kalender erscheint.

Sie konfigurieren das Modul in der System-Administration unter:<br>
`Administration > Externe Werkzeuge > Microsoft Teams`

Die Voraussetzungen für die Anbindung an Microsoft 365 beschreibt die Seite [Externe Werkzeuge: Übersicht](External_Tools_-_Administration.de.md#_microsoft_teams). Wie Kursbesitzer:innen und Betreuer:innen einzelne Online-Termine anlegen, steht im Benutzerhandbuch im Kapitel [Kursbaustein "Microsoft Teams"](../../manual_user/learningresources/Course_Element_Microsoft_Teams.de.md).

---

## Tab "Konfiguration" [:octicons-tag-16:{ title="ab Release 15.4 (OO-5124)" }](https://track.frentix.com/issue/OO-5124) {: #tab_config}

Im Tab "Konfiguration" schalten Sie Microsoft Teams für die Instanz ein und bestimmen, wo und mit welchen Varianten Online-Termine entstehen dürfen.

### Konfiguration von Microsoft Teams Integration {: #teams_config}

Die Felder "Aktivieren für" und "Online-Termine ohne Datum/permanent" erscheinen erst, wenn das Modul eingeschaltet ist.

#### Modul "Microsoft Teams" {: #module_enabled}

Schaltet Microsoft Teams für die ganze Instanz ein oder aus. Ist das Modul ausgeschaltet, steht der Kursbaustein "Microsoft Teams" im Kurseditor nicht zur Auswahl.

#### Aktivieren für {: #activate_for}

Gibt Microsoft Teams einzeln für die Orte frei, an denen Online-Termine entstehen: Kursbaustein "Microsoft Teams", Kurs Termine, Kursbaustein "Terminplanung", Gruppen und Betreuer:innen-Chat.

#### Online-Termine ohne Datum/permanent [:octicons-tag-16:{ title="ab Release 21.1.0 (OO-9666)" }](https://track.frentix.com/issue/OO-9666) {: #permanent_meetings}

Bestimmt, ob in Kursen und Gruppen permanente Reservierungen entstehen dürfen. Eine permanente Reservierung ist ein Online-Termin ohne Beginn und Ende: Der Raum steht dauerhaft offen, erscheint aber in keinem Kalender.

Mit "Ein" (Standard) bietet die Auswahl "Online-Termin hinzufügen" die Variante "Permanente Reservierung hinzufügen" an. Mit "Aus" fehlt diese Variante im Kursbaustein "Microsoft Teams", im Gruppenwerkzeug "Microsoft Teams" und im Kurswerkzeug "Teams". Jeder neue Online-Termin braucht dann Beginn und Ende und erscheint im Kalender. Das hilft Organisationen, die alle Online-Termine planen und im Kalender überblicken wollen.

Bestehende permanente Reservierungen bleiben erhalten, wenn Sie die Option auf "Aus" stellen. Sie lassen sich weiterhin öffnen, bearbeiten und ohne Datum speichern. Die Option verhindert nur, dass neue permanente Reservierungen entstehen.

Das Modul BigBlueButton kennt dieselbe Einstellung unter dem Namen "Online-Termine ohne Datum", siehe [Modul BigBlueButton](BigBlueButton_module.de.md#tab_config).

#### Anwendungs-ID (Client), Geheimer Clientschlüssel, Tenant GUID {: #tenant_credentials}

Sind in der Serverkonfiguration Zugangsdaten zum Microsoft 365 Tenant hinterlegt, zeigt der Tab sie in diesen drei Feldern zur Ansicht. Ändern lassen sie sich nur in der Serverkonfiguration. frentix-Kund:innen wenden sich für eine Änderung an den frentix Support: [support@frentix.com](mailto:support@frentix.com)

---

## Tab "Online-Termine" {: #tab_online-meetings}

Im Tab "Online-Termine" behalten Sie alle Online-Termine von Microsoft Teams in der Instanz im Blick und räumen nicht mehr benötigte Termine auf.

Die Tabelle zeigt je Termin "Name", "Ohne Datum", "Beginn", "Ende" und "Kontext". Ein Klick auf den Kontext öffnet den Kurs oder die Gruppe, in der der Termin angelegt ist. Über die Suche finden Sie einzelne Termine. Mit "Löschen" entfernen Sie einen Termin, oder mehrere markierte Termine gesammelt.

---

## Tab "Kalender" {: #tab_calendar}

Im Tab "Kalender" sehen Sie, wann viele Online-Termine gleichzeitig stattfinden, und erkennen Engpässe früh. Die Ansicht öffnet in der Woche und zeigt alle Online-Termine von Microsoft Teams mit Beginn und Ende. Permanente Reservierungen erscheinen hier nicht, weil sie kein Datum haben.

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Externe Werkzeuge: Übersicht >](External_Tools_-_Administration.de.md)<br>
[Kursbaustein "Microsoft Teams" >](../../manual_user/learningresources/Course_Element_Microsoft_Teams.de.md)<br>
[Modul BigBlueButton >](BigBlueButton_module.de.md)

**Weiterführend**<br>
[Gruppenwerkzeuge nutzen >](../../manual_user/groups/Using_Group_Tools.de.md)<br>
[Virtuelle Klassenzimmer >](../../manual_user/basic_concepts/Virtual_classrooms.de.md)

[Zum Seitenanfang ^](#teams_module)
