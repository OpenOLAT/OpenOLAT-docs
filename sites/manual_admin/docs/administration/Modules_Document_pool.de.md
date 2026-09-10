# Modul Dokumentenpool {: #module_document_pool}

!!! info "Was ist der Dokumentenpool?"

	Der Dokumentenpool ist eine taxonomiebasierte Dokumentenverwaltung, welche
	kompetenzbasiert freigeschaltet werden kann. Es kann so beispielsweise die
	Ressourcenverwaltung für Lehrmaterialien basierend auf der Dozierkompetenz
	abgebildet werden.

	Der Dokumentenpool kann für alle OpenOlat-Benutzer freigeschaltet werden, also
	auch für Lernende.

	Die Dokumente aus dem Dokumentenpool stehen nur im Dokumentenpool zur
	Verfügung und können nicht in einen Kurs eingebunden werden.

	Weitere Informationen finden Sie im Kapitel
	[Taxonomie](Modules_Taxonomy.de.md).

Der Dokumentenpool kann als Site in der Hauptnavigation oben eingeschaltet
werden.

![Site Dokumentenpool in der Hauptnavigation mit Taxonomiebaum links und Dateiablage der ausgewählten Ebene rechts, hier die Ordner Grammatik und Texte](assets/Dokumentenpool_beispiel_DE.png){ class="shadow lightbox" }

## Tab Dokumentenpool

Im Tab "Dokumentenpool" kann der Dokumentenpool eingeschaltet werden. In der
Navigation wird er jedoch erst sichtbar, wenn die Site entsprechend
freigeschaltet ist.

Hier kann anschliessend der WebDAV Mountpunkt definiert
werden. Dann muss die Taxonomie ausgewählt werden. Den Inhalt der Taxonomie
definieren Sie unter `Administration > Module > Taxonomie`.

Zudem können Vorlagen aktiviert werden. Die Vorlagen werden dann im
Dokumentenpool direkt unter der Hauptnavigation angezeigt. Dort können
Systemadministratoren Dokumente hochladen und allen zur Verfügung stellen,
unabhängig von ihren Zugriffsrechten im Dokumentpool.

![Tab Dokumentenpool in der System-Administration mit Checkbox Dokumentenpool einschalten, Feldern WebDAV Mountpunkt und Taxonomie sowie Checkbox Vorlagen aktivieren](assets/Dokumentenpool_DE.png){ class="shadow lightbox" }

## Tab Zugangsberechtigung

Hier können nun die Rechte für die einzelnen Ebenentypen aus der Taxonomie
definiert werden. Damit hier ein Kompetenztyp erscheint, muss er also zuerst
unter `Administration > Module > Taxonomie` im Tab "Ebenentypen" erfasst werden.

  * **In Dokumentenpool verwenden:** Mit dieser Option wird definiert, ob dieser Kompetenztyp im Dokumentpool auftaucht.
  *  **Dokumenten einschalten**: Nur wenn diese Option aktiviert ist, können auf dieser Ebene Dokumente hochgeladen werden. Ansonsten wird diese Ebene als Struktur ohne Ordnerinhalte abgebildet. 
  *  **Verwalter-Kompetenz:** zulassen oder nicht<br>
  *  **Dozier-Kompetenz**: In der Dozier-Kompetenz können die Zugriffsrechte auf die einzelnen Ebenen im Dokumentenpool definiert werden. Als erstes wird ausgewählt, ob die Personen mit der Dozier-Kompetenz lesenden Zugriff auf diese Ebene erhalten. Wenn ja, können diese Benutzer die Inhalte auf dieser Ebene lesen. Ausserdem kann mit einer Zahl definiert werden, auf wie viele übergeordnete Taxonomieebenen der lesende Zugriff zusätzlich gestattet werden soll.<br>
Wenn zusätzlich noch "Schreibender Zugriff gestatten" aktiviert wird, können
diese Benutzer auch Dokumente hochladen.<br>
  *  **Haben-Kompetenz**: lesenden Zugriff gestatten oder nicht<br>
  *  **Ziel-Kompetenz:** lesenden Zugriff gestatten oder nicht  

Diese Einstellungen müssen nun für alle definierten Kompetenztypen wiederholt
werden.

Zudem muss den Benutzern die entsprechende Kompetenz zugewiesen werden. Dies
geschieht entweder über die Synchronisation von einem externen
Benutzerverwaltungssystem oder direkt im OpenOlat. Im OpenOlat ist dies
entweder in der Benutzerverwaltung oder in der `Administration > Module >
Taxonomie` möglich.

Ferner können hier Einstellungen für die Kompetenztypen "Handlungsfeld" und
"Fach" vorgenommen werden.

![Tab Zugangsberechtigungen, Kompetenztyp "Handlungsfeld": Schalter für Verwendung, Dokumente, Verwalter-, Haben- und Ziel-Kompetenz, Dozier-Kompetenz zusätzlich mit Zahl übergeordneter Ebenen](assets/Dokumentenpool_Zugangsberechtigung_DE.png){ class="shadow lightbox" }

## Tab Infoseite

Zum Schluss kann eine Infoseite gestaltet werden. Diese erscheint auf der
obersten Ebene des Dokumentenpools. Es empfiehlt sich, hier beispielsweise
eine Anleitung zum Gebrauch des Dokumentenpools zu hinterlegen.

![Infoseite auf der obersten Ebene der Site Dokumentenpool mit dem Willkommenstext](assets/Dokumentenpool_Infoseite.png){ class="shadow lightbox" }

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Taxonomie >](Modules_Taxonomy.de.md)

[Zum Seitenanfang ^](#module_document_pool)
