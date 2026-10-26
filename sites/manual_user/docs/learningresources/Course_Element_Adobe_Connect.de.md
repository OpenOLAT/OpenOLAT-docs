# Kursbaustein "Adobe Connect" {: #adobe_connect}


## Steckbrief

Name | Adobe Connect
---------|----------
Icon | :o_icon_o_vc_icon:
Verfügbar seit | Release 14.0 (OO-3888)
Funktionsgruppe | Kommunikation und Kollaboration
Verwendungszweck | Integration der Webkonferenz-Software Adobe Connect
Bewertbar | nein
Spezialität / Hinweis | Adobe Connect ist eine kommerzielle Software. Um den Kursbaustein zu nutzen, ist eine separate Lizenz und ein Serverhosting erforderlich.



## Tool Spezifisches

Standardmässig sind Kursbesitzer:innen und Betreuer:innen Adobe Connect Verwalter:innen und Teilnehmende sind Connect Teilnehmende ohne weitere Rechte.

Im Connect Raum stehen diverse Elemente (Pods) zur Verfügung, die miteinander kombiniert und in "Layouts" organisiert werden können. So können u.a. Präsentationsdateien hochgeladen und auch ein Veranstaltungsmitschnitt aktiviert werden. Sowohl die hochgeladenen Präsentationsdateien als auch die Aufzeichnungen sind in OpenOlat für die Kursbesitzer:innen und Betreuer:innen sichtbar und können den Teilnehmenden alle oder teilweise zur Verfügung gestellt werden.

![Button "Meeting beitreten", darunter im Bereich Inhalt die Aufzeichnung und die Präsentationsdateien mit dem Button "Dateien bereitstellen"](assets/connect_aufzeichnung.png){ class="shadow lightbox" title="Meeting im Kursbaustein Adobe Connect" }

## Konfiguration im Kurseditor

Hier steht der Tab "Konfiguration" für weitere Einstellungen zur Verfügung:<br>
`Kurs > Administration > Kurseditor > Kursbaustein "Adobe Connect" > Tab "Konfiguration"`

## Konfiguration in der Kursansicht {: #konfiguration-im-kursrun-geschlossener-editor}

Nachdem Sie den Kursbaustein hinzugefügt haben, erstellen Sie im Kurs bei geschlossenem Kurseditor einen Meetingraum. Klicken Sie dazu im Tab "Konfiguration" auf den Button "Meeting hinzufügen":<br>
`Kurs > Kursbaustein "Adobe Connect" > Konfiguration > Meeting hinzufügen`

Anschliessend erscheint der folgende Dialog:

![Felder Name, Beschreibung, Vorlage, Typ "Dauernd", Beginn- und Enddatum mit Vorlauf- und Nachlaufzeit](assets/connect_meeting_hinzufuegen.jpg){ class="shadow lightbox" title="Dialog Meeting hinzufügen" }

Unter dem eingetragenen Namen wird der Raum im Bereich der Meetings angezeigt. Die Beschreibung wird sichtbar nachdem man den Raum ausgewählt hat.

Sofern vorhanden können Sie eine vom Hosting-Server bereitgestellte Vorlage verwenden oder "Keine Vorlage" wählen. Definieren Sie auch ob der Raum permanent (=dauernd) oder nur zu einem bestimmten Termin zur Verfügung stehen soll. Bei einem termingebundenen Raum können Sie noch ein Vorlauf und Nachlaufzeit ergänzen.

Unabhängig von der Raumkonfiguration kann der Zugang zum Kursbaustein des Virtuellen Klassenzimmers auch wie alle anderen Kursbausteine über die Tabs Sichtbarkeit und Zugang im Kurseditor konfiguriert werden.

Ein eingebauter Adobe Connect Kursbaustein kann mehrere unterschiedlich konfigurierte Meeting-Räume enthalten. Je nach Konfiguration in der System-Administration unter `Administration > Externe Werkzeuge > Adobe Connect` führen alle eingerichteten Meetings in denselben oder verschiedene Adobe Connect Räume.

Im Tab "Meetings" wird die Übersicht der eingerichteten virtuellen Räume so angezeigt, wie sie auch für Teilnehmende sichtbar sind. Terminlich abgelaufene, termingebundene Meetings werden entsprechend gekennzeichnet.

![Listen Zukünftige Meetings und Alte Meetings mit Beginn- und Enddatum, in jeder Zeile der Link "Auswählen"](assets/connect_meetings.jpg){ class="shadow lightbox" title="Tab Meetings im Kursbaustein Adobe Connect" }

Über "Auswählen" gelangt man in das entsprechende virtuelle Klassenzimmer. Beim ersten Aufruf muss man sich für das Meeting "anmelden" und anschliessend hat man die Möglichkeit über ein weiteres Dialogfenster dem Meeting beizutreten. Mit "Meeting beitreten" gelangt man in das Virtuelle Klassenzimmer und sämtliche raumspezifischen Werkzeuge stehen zur Verfügung.

!!! note "Link zu weiteren Infos"

    Adobe Connect Anbieter Webseite: <https://www.adobe.com/de/products/adobeconnect.html>

    Da viele Hochschulen in Deutschland den [DFN Server](https://www.conf.dfn.de/anleitungen-und-dokumentation/adobe-connect) für Adobe Connect nutzen, können auch die entsprechenden Informationen interessant sein.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Adobe Connect (Anbieter-Website)](https://www.adobe.com/de/products/adobeconnect.html)<br>
[DFN Server](https://www.conf.dfn.de/anleitungen-und-dokumentation/adobe-connect)

**Weiterführend**<br>
[Kursbausteine >](Course_Elements.de.md)<br>
[Kursbaustein "GoToMeeting" >](Course_Element_GoToMeeting.de.md)<br>
[Virtuelle Klassenzimmer >](../basic_concepts/Virtual_classrooms.de.md)<br>
[Externe Werkzeuge: Übersicht >](../../manual_admin/administration/External_Tools_-_Administration.de.md)

[Zum Seitenanfang ^](#adobe_connect)
