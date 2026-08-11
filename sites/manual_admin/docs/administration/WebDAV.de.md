# WebDAV

## Modulkonfiguration

Das WebDAV Modul kann für das gesamte OpenOlat System ein- oder ausgeschaltet
werden. Sie finden die Einstellungen in der System-Administration unter:<br>
`Administration > Core Konfiguration > WebDAV`

Die folgenden Konfigurationen können vorgenommen werden:

  *  **WebDAV Zugang**<br>
	Schalten Sie den WebDAV Zugang systemweit ein oder aus. Wenn das Modul
	eingeschaltet ist können alle OpenOlat Benutzer das System über WebDAV nutzen
	(empfohlen).

  *  **WebDAV Links anzeigen**<br>
	Unabhängig von der WebDAV Funktion können Sie entscheiden ob die WebDAV URL in
	der Ordnerkomponente angezeigt werden soll oder nicht. Wenn diese Funktion
	ausgeschaltet ist kann WebDAV immer noch verwendet werden, es wird lediglich
	der Link nicht angezeigt.

  *  **Digest Authentication**

	!!! warning "Sicherheitshinweis"
		Die Digest-Authentication Verschlüsselung verwendet keine starke Kryptographie und kann mit entsprechendem Aufwand geknackt werden. Bei hohen Sicherheitsanforderungen sollte immer der HTTPS Zugang mit SSL Verschlüsselung verwendet werden.

  *  **WebDAV Client Verbot**<br>
	Das Ausschliessen von spezifischen WebDAV-Clients ein- / ausschalten.

  *  **Liste von User-Agent**<br>
  	Liste der nicht erlaubten User-Agents.

* * *

  *  **Kurse nach Semesterdaten gruppieren**<br>
	Aktivieren Sie diese Option um für jedes Semester einen Unterordner zu
	erstellen der alle Kurses dieses Semesters enthält. Diese Option erhöht die
	Nutzbarkeit bei vielen Kursen. Wenn diese Option aktiviert ist, wird für die beendeten Kurse kein Ordner "_beendet" erstellt. Sofern diese Option nicht aktiviert ist, sind im WebDAV alle beendeten Kurse im Ordner "_beendet" zu finden.

  *  **Kurse nach CPL Elementen gruppieren**<br>
	Aktivieren Sie diese Option um für Curriculum-Gruppen Unterordner zu
	erstellen der alle Kurses dieser Curriculum-Gruppe enthält.

  *  **"Managed" Kurse gruppieren**
  *  **Kennzeichen dem Titel voranstellen**<br>
	Legen Sie fest ob das [Kennzeichen](../../manual_user/learningresources/Course_Settings_Info.de.md) dem Kurstitel
	zur besseren Unterscheidung ähnlicher Titel vorangestellt werden soll.  

* * *

  * **Zugriff für Studenten / Betreuer Kurse**<br>
	Aktivieren Sie diese Option um auch Studenten und Betreuern den Zugriff auf ihre Kursordner zu gestatten. Es werden nur die Ordner der entsprechenden Ordner-Kursbausteine angezeigt, sowie ein eventuell eingebundene Ressourcenordner.

  *  **Zugriff für Studenten / Betreuer Favoriten**<br>
	Aktivieren Sie diese Option um auch Studenten und Betreuern den Zugriff auf Kursordner von Kursen zu gestatten, die sich in ihrer Favoritenliste befinden, deren Mitglieder sie aber nicht sind. Dies ist nur möglich mit den entsprechenden Einstellungen in der Zugriffskonfiguration. Es werden nur die Ordner der entsprechenden Ordner-Kursbausteine angezeigt, sowie ein eventuell eingebundener Ressourcenordner.

## Verwendung

Weitere Informationen zur Anwendung von WebDAV in OpenOlat finden Sie unter [Einsatz von WebDAV](../../manual_user/basic_concepts/Using_WebDAV.de.md).



