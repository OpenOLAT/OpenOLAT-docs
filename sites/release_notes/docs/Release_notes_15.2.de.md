# Release Notes 15.2

Mit OpenOlat 15.2 geben wir unseren nächsten Major Release frei. Dieser bringt
Erweiterungen im BigBlueButton-Baustein mit sich, so können zum Beispiel
Recordings gezielt für bestimmte Benutzergruppen freigegeben werden. Für die
Verarbeitung der BBB-Recordings wurde ein weitere Handler integriert, der die
Recordings auf einen OpencastServer ablegt. Über einen eigenen Opencast-
Kursbaustein können Aufzeichnungen vom Opencast-Server in OpenOlat eingebunden
werden. Neben kleineren Anpassungen wurde ausserdem der Mehrfenster-Modus
weiter verbessert und bei Bedarf kann der Benutzername in OpenOlat geändert
werden.

![](assets/152/Features_Improvements_Labels_DE.png)

Seit Release 15.1 wurden über 30 neue Funktionen und Verbesserungen zu
OpenOlat hinzugefügt. Hier finden Sie die wichtigsten neuen Funktionen und
Änderungen. Zusätzlich zu wurden mehr als 20 Bugs behoben. Die komplette Liste
der Änderungen in 15.1 – 15.1.4 finden Sie
[hier](https://confluence.openolat.org/display/OO151DE/Release+Notes+15.1#ReleaseNotes15.1-ReleaseNotes-
Versionen).

* * *

## BigBlueButton - Erweiterungen

![](assets/152/Screenshot%202020-08-26%20at%2016.19.55.png){ class="shadow lightbox aside-right-lg" }

Werden BigBlueButton-Meetings aufgezeichnet, kann nun die Veröffentlichung der
Recordings gezielt gesteuert werden. Dafür wird eine Teilnehmerliste pro
Recording geführt, die es ermöglicht, die Aufzeichnung für verschiedene
Teilnehmerkreise freizugeben:

  * Besitzer und Betreuer
  * Kurs- und Gruppen-Teilnehmer
  * Alle Teilnehmer des Meetings (ausser Gäste)
  * Gäste

Zudem wurde eine Infrastruktur geschaffen, die es erlaubt, BBB-Recordings auf
einem Opencast-Server abzulegen. Eine erneute Einbindung dieser Aufzeichnungen
an anderer OpenOlat-Stelle ist über den Opencast-Baustein möglich.

* * *

## Kursbaustein Opencast

![](assets/152/Screenshot%202020-08-28%20at%2009.34.14.png){ class="shadow lightbox aside-right-lg" }

Mit dem Kursbaustein Opencast können Aufzeichnungen von Meetings und
Lehrveranstaltungen, die auf einem Opencast-Server abgelegt sind, in OpenOlat-
Kurse eingebunden werden. Die Konfiguration und Anbindung des Opencast-Servers
erfolgt in der Administration. Im Kursbaustein können entweder einzelne Videos
oder ganze Serien eingebunden werden.

* * *

## Weiteres, kurz notiert

![](assets/152/Screenshot%202020-08-28%20at%2010.43.30.png){ class="shadow lightbox aside-right-lg" }

  * Benutzername ändern ist möglich, frentix-Kunden melden sich hierfür bitte beim frentix-Support
  * Kurswerkzeuge lassen sich in Einzelseiten einbinden und via Link direkt öffnen (s. Screenshot)
  * Anzahl der Benutzer, die im Prüfungsmodus auf den Prüfungsstart warten, wird für den Betreuer im Bewertungswerkzeug angezeigt
  * Benutzer können mittels Vor- und Nachnamen zu Kursen, Gruppen usw. hinzugefügt werden
  * Kurswerkzeug "Kalender" kann auch in einem neuen Fenster geöffnet werden

* * *

 
## Technisches

  * Framework-Feature zum Erstellen neuer Fenster von einem Controller aus
  * LDAP-Benutzernamen vom OpenOlat-Benutzernamen lösen und LDAP-Benutzer über Excel-Import ermöglichen
  * Library Updates
  * Aktualisieren von Bibliotheken von Drittanbietern

!!! attention "Wichtiger Hinweis für Administratoren"
	Der JDBC-Treiber für MySQL wurde aktualisiert. Bitte unbedingt überprüfen, ob
	die Zeitzone in der Datenbank eingestellt ist, da der Treiber keine
	undefinierte Zeitzone akzeptiert.
	
	Beispiel:
	
		SET GLOBAL Zeit_Zone = 'Europa/Zürich';  
	
	Folgender Parameter ist in den olat.local.properties zu prüfen:  
	
		_db.url.options.mysql=?characterEncoding=UTF-8&connectionCollation=utf8_unicode_ci_
	
	Das "Connection Collation Attribute" ist für einige wenige Abfragen in
	OpenOlat zwingend. Bitte dieses Attribut mit der gleichen Collation setzen,
	die auch in der Datenbank verwendet wird.

* * *

  

## Release Notes - Versionen

* [YouTrack release notes 15.2](https://track.frentix.com/releaseNotes/OO?q=%2315.2%20&title=Release%20Notes%2015.2)
* [YouTrack release notes 15.2 - 15.2.13](https://track.frentix.com/issues/OO?q=%2315.2.*)

  


