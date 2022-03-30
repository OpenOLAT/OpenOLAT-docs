# WebDAV

## Modulkonfiguration

Das WebDAV Modul kann für das gesamte OpenOlat System ein- oder ausgeschaltet
werden. Die folgenden Konfigurationen können vorgenommen werden:

  *  **WebDAV Zugang**  
	Schalten Sie den WebDAV Zugang systemweit ein oder aus. Wenn das Modul
	eingeschaltet ist können alle OpenOlat Benutzer das System über WebDAV nutzen
	(empfohlen).

  *  **WebDAV Links anzeigen**  
	Unabhängig von der WebDAV Funktion können Sie entscheiden ob die WebDAV URL in
	der Ordnerkomponente angezeigt werden soll oder nicht. Wenn diese Funktion
	ausgeschaltet ist kann WebDAV immer noch verwendet werden, es wird lediglich
	der Link nicht angezeigt.

  *  **Digest Authentication bei HTTP Zugang verwenden**  
	Um WebDAV unter Windows direkt ohne den manuellen Import von Zertifikaten
	verwenden zu können ist ein Betrieb von WebDAV unter HTTP ohne SSL notwendig.
	In diesem Fall werden die Dateien unverschlüsselt übertragen. Um das Passwort
	trotzdem verschlüsselt zu übermitteln muss in diesem Fall der Digest-
	Authentication Mechanismus verwendet werden, ansonsten kann WebDAV unter
	Windows nicht verwendet werden.  
	
	!!! attention "Sicherheitshinweis"
		Die Digest-Authentication Verschlüsselung verwendet keine starke Kryptographie
		und kann mit entsprechendem Aufwand geknackt werden. Bei hohen
		Sicherheitsanforderungen sollte immer der HTTPS Zugang mit SSL Verschlüsselung
		verwendet werden. Unter Windows müssen hierfür leider Zertifikate manuell
		importiert oder spezielle WebDAV Programme verwendet werden.

  *  **WebDAV Client Verbot**  
	Das Ausschliessen von spezifischen WebDAV-Clients ein- / ausschalten

  *  **Liste von User-Agent**  
  	Liste der nicht erlaubten User-Agents.

* * *

  *  **Kurse nach Semesterdaten gruppieren**  
	Aktivieren Sie diese Option um für jedes Semester einen Unterordner zu
	erstellen der alle Kurses dieses Semesters enthält. Diese Option erhöht die
	Nutzbarkeit bei vielen Kursen. Wenn diese Option aktiviert ist, wird für die
	beendeten Kurse kein Ordner "_beendet" erstellt. Sofern diese Option nicht
	aktiviert ist, sind im WebDAV alle beendeten Kurse im Ordner "_beendet" zu
	finden.

  *  **Kurse nach Curriculum Elementen gruppieren ** 
	Aktivieren Sie diese Option um für Curriculum-Gruppen Unterordner zu
	erstellen der alle Kurses dieser Curriculum-Gruppe enthält.

  *  **Managed Kurs gruppieren**
  *  **Kennzeichen dem Titel voranstellen**  
	Legen Sie fest ob das [Kennzeichen](../../manual_user/authoring/Set_up_info_page.de.md) dem Kurstitel
	zur besseren Unterscheidung ähnlicher Titel vorangestellt werden soll.  

* * *

  * **Zugriff für Studenten / Betreuer Kurse**  
	Aktivieren Sie diese Option um auch Studenten und Betreuern den Zugriff auf
	ihre Kursordner zu gestatten. Es werden nur die Ordner der entsprechenden
	Ordner-Kursbausteine angezeigt, sowie ein eventuell eingebundene
	Ressourcenordner.

  *  **Zugriff für Studenten / Betreuer Favoriten**  
	Aktivieren Sie diese Option um auch Studenten und Betreuern den Zugriff auf
	Kursordner von Kursen zu gestatten, die sich in ihrer Favoritenliste befinden,
	deren Mitglieder sie aber nicht sind. Dies ist nur möglich mit den
	entsprechenden Einstellungen in der Zugriffskonfiguration. Es werden nur die
	Ordner der entsprechenden Ordner-Kursbausteine angezeigt, sowie ein eventuell
	eingebundener Ressourcenordner.

## Verwendung

Weitere Informationen zur Anwendung von WebDAV in OpenOlat finden Sie unter
[Einsatz von WebDAV](../../manual_user/supported_tech/Using_WebDAV.de.md).

