# Kursbaustein "Externe Seite" {: #external_page}

## Steckbrief

Name | Externe Seite
---------|----------
Icon | :o_icon_o_tu_icon:
Verfügbar seit | Neuauflage mit Release 18
Funktionsgruppe | Andere
Verwendungszweck | Anzeige von externen Webinhalten innerhalb eines OpenOlat-Kurses und Einbinden in die Kursnavigation
Bewertbar | nein
Spezialität / Hinweis | Muss von der Administration eingeschaltet werden. frentix empfiehlt den Einsatz nicht.

Mit Hilfe des Kursbausteins "Externe Seite" können Sie eine externe Internetseite aufrufen. Geben Sie einfach die gewünschte URL in der Konfiguration im Tab "Seiteninhalt" ein um die externe Seite in Ihre Kursnavigation zu integrieren. Für die Anzeige der verlinkten Seite werden Ihnen die Varianten

  * "Eingebettet (Quelle verborgen)",
  * "Eingebettet (Quelle sichtbar)" und
  * "Neues Browser-Fenster (Quelle sichtbar)"

angeboten.

Für Seiten, die eine Authentifizierung erfordern und deren Quelle verborgen ist, können Sie "Seite Passwort geschützt" aktivieren und die notwendigen Zugangsdaten eintragen.

Typische Anwendungsfälle sind Seiten mit Datenbankabfragen, zum Beispiel ein Literaturrecherche-Tool oder Online-Übungen aus dem Web. Es lassen sich nur externe Seiten über die Protokolle HTTP und HTTPS verlinken.

!!! warning "frentix empfiehlt, Domänen getrennt zu halten"

    Der Kursbaustein "Externe Seite" zeigt Inhalte einer fremden Domäne innerhalb
    Ihrer OpenOlat-Domäne an. Aus modernen Sicherheitsüberlegungen empfiehlt
    frentix, verschiedene Domänen nicht zu vermischen, und rät deshalb vom
    Einsatz dieses Kursbausteins ab.

    Eine Domäne ist die Internetadresse, unter der eine Seite ausgeliefert wird:
    Ihre OpenOlat-Instanz läuft unter einer eigenen Adresse, die eingebundene
    Seite unter einer anderen.

Verweisen Sie stattdessen mit der [Linkliste](Course_Element_Link_List.de.md) auf die Seite. Ist der Kursbaustein in Ihrer Instanz nicht verfügbar, hat Ihre Administration ihn nicht eingeschaltet.

## Tab "Seiteninhalt" konfigurieren

**URL:** Dieses Eingabefeld müssen Sie ausfüllen. Hier geben Sie die Webseite an, auf der die gewünschten externen Inhalte liegen (im Format:_https://www.musterseite.com_)

**Darstellung konfigurieren:** Sie können zwischen drei Optionen wählen:

*  _Eingebettet (Quelle verborgen):_ OpenOlat ruft die externe Seite ab und zeigt sie in einem sog. «iframe» im Kursfenster an. Die Internet-Adresse der externen Seite ist für Teilnehmende nicht sichtbar. Damit die Seite vollständig auf diesem Weg angezeigt wird, dürfen die eingebundenen HTML-Seiten Ressourcen wie Bilder, Videos oder Links nur mit **relativen Pfaden** ansprechen. Inhalte hinter absoluten Pfaden wie "https://..." oder relativ absoluten Pfaden wie "/public" lädt der Browser der Teilnehmenden direkt bei der externen Seite; deren Adresse wird dabei sichtbar.

*  _Eingebettet (Quelle sichtbar):_ Der Browser der Teilnehmenden ruft die externe Seite direkt ab und zeigt sie ebenfalls in einem «iframe» an. Im Quellcode der OpenOlat-Seite kann die Internet-Adresse der externen Seite eingesehen werden.

*  _Neues Browser-Fenster (Quelle sichtbar):_ Der Kursbaustein zeigt eine Schaltfläche, die die externe Seite in einem eigenen Browser-Tab öffnet.

**Seite Passwort geschützt:** Diese Option steht nur bei der Darstellung "Eingebettet (Quelle verborgen)" zur Verfügung. Die Zugangsdaten gelten für alle Teilnehmenden gemeinsam. Sie werden unverschlüsselt in der Konfiguration des Kursbausteins gespeichert und sind damit in jeder Kurskopie und in jedem Kursexport enthalten. Tragen Sie hier keine persönlichen Zugangsdaten ein.

Eingebettete Frames («iframe») verhalten sich wie eigene Browser-Fenster, die jedoch Bestandteil der HTML-Seite des Ursprungsfensters sind.

Vorteil von «iframe»: Sie können beliebige Inhalte (komplexe Webseiten in verschachtelten Frames, mathML etc.) in OpenOlat anzeigen lassen.

Nachteil von «iframe»: Die Inhalte erscheinen unter Umständen mit eigenen Scroll-Balken.

!!! tip "Wählen Sie die Variante nach Anzeige und Risiko"

    Die drei Varianten unterscheiden sich nicht nur darin, wie die Seite
    angezeigt wird. Bei "Eingebettet (Quelle verborgen)" ruft OpenOlat die Seite
    ab; die externe Seite erfährt dabei nichts über Ihre Teilnehmenden. Bei den
    beiden anderen Varianten verbindet sich der Browser der Teilnehmenden direkt
    mit der externen Seite. Wägen Sie beides gegeneinander ab und testen Sie die
    Darstellungsmöglichkeiten der Reihe nach, bis die verlinkte Seite wie
    gewünscht angezeigt wird.
