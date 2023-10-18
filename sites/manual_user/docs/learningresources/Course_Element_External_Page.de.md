# Kursbaustein "Externe Seite" {: #external_page}

## Steckbrief

Name | Externe Seite
---------|----------
Icon | ![Externe Seite Icon](assets/external_page.png){ class=size24  }
Verfügbar seit | Neuauflage mit Release 18
Funktionsgruppe | Wissensvermittlung
Verwendungszweck | Anzeige von externen Webinhalten innerhalb eines OpenOlat-Kurses und Einbinden in die Kursnavigation
Bewertbar | nein
Spezialität / Hinweis | 

Mit Hilfe des Kursbausteins "Externe Seite" können Sie eine externe Internetseite aufrufen. Geben Sie einfach die gewünschte URL in der Konfiguration im Tab "Seiteninhalt" ein um die externe Seite in Ihre Kursnavigation zu integrieren. Für die Anzeige der verlinkten Seite werden Ihnen die Varianten

  * "Eingebettet" (Quelle verborgen),
  * "Eingebettet" (Quelle sichtbar),
  * "Neues Browserfenster" (Quelle sichtbar) und
  * "Vollständig integriert" (Quelle verborgen)

angeboten.

Für Seiten, die eine Authentifizierung erfordern und deren Quelle verborgen ist, können Sie "Seite Passwort geschützt" aktivieren und die notwendigen Zugangsdaten eintragen.

Der Einsatz dieses Kursbausteins empfiehlt sich, wenn Sie beispielsweise Seiten mit Datenbankabfragen (Literaturrecherche-Tool, Online-Übungen aus dem Web, etc.) einbinden möchten. Es lassen sich nur externe Seiten über die Protokolle HTTP und HTTPS verlinken.

## Tab "Seiteninhalt" konfigurieren

**URL:** Dieses Eingabefeld müssen Sie ausfüllen. Hier geben Sie die Webseite an, auf der die gewünschten externen Inhalte liegen (im Format:_http://www.musterseite.com_)

**Darstellung konfigurieren:** Sie können zwischen vier Optionen wählen:

*  _Vollständig integriert (Quelle verborgen):_ Dies bedeutet, dass die externe HTML-Seite geparst und vollständig in die OpenOlat-Seite eingebaut wird. Die HTML-Seiten dürfen ausschliesslich Ressourcen wie Bilder, Flash, Videos oder Links mit **relativen Pfaden** enthalten. Absolute Pfade wie "http://..." sowie relativ absolute Pfade wie "/public" (relativ zu einem Basis URI) sind nicht erlaubt.
  
*  _Eingebettet (Quelle verborgen):_ Hier wird die externe HTML-Seite in ein sog. «iframe» eingebaut. Die Internet-Adresse der externen Seite ist für den Benutzer nicht sichtbar. Die HTML-Seiten dürfen ausschliesslich Ressourcen wie Bilder, Flash, Videos oder Links mit **relativen Pfaden** enthalten. Absolute Pfade wie "http://..." sowie relativ absolute Pfade wie "/public" (relativ zu einem Basis URI) sind nicht erlaubt.
  
*  _Eingebettet (Quelle sichtbar):_ Hier wird die externe HTML-Seite ebenfalls in ein «iframe» eingebaut. Im Quellcode der OLAT-Seite kann die Internet-Adresse der externen Seite eingesehen werden.
*  _Neues Browser-Fenster (Quelle sichtbar):_ Als weitere Option können Sie die externe Seite auch in einem eigenen Browserfenster anzeigen lassen.

Eingebettete Frames («iframe») verhalten sich wie eigene Browser-Fenster, die jedoch Bestandteil der HTML-Seite des Ursprungsfensters sind.  

Vorteil von «iframe»: Sie können beliebige Inhalte (komplexe Webseiten in verschachtelten Frames, mathML etc.) in OLAT anzeigen lassen.  

Nachteil von «iframe»: Die Inhalte erscheinen unter Umständen mit eigenen Scroll-Balken.

!!! info "Info"

    Sollten Sie sich nicht sicher sein, welche Variante in Ihrem Fall die Richtige ist, dann beginnen Sie mit der Option „Vollständig integriert“ und testen die anderen Darstellungsmöglichkeiten, bis die verlinkte Seite wie gewünscht angezeigt wird.