# Customizing: Übersicht {: #customizing}

![Erscheinungsbild und Hauptnavigation der ganzen Instanz in sieben Menüpunkten, von Darstellung bis Bereiche, im aufgeklappten Menü Customizing der System-Administration](assets/admin_customizing_overview_v2_de.png){ class="shadow lightbox aside-left-lg" }

Im Menü "Customizing" passen Administrator:innen und Systemadministrator:innen das Erscheinungsbild und die Hauptnavigation der ganzen Instanz an. Sie finden diese Einstellungen in der System-Administration unter:<br>
`Administration > Customizing`

## Steckbrief

Name | Customizing
---------|----------
Verfügbar seit | Release 8.0 (2011)

---

<a id="representation-layout"></a>
## Darstellung {: #layout}

![Auswahlliste Systemlayout, Logo-Upload bis 1 MB mit Ziel-URL und Alternativ-Text, Fusszeile mit Ziel-URL und Text](assets/admin_customizing_layout_v1_de.png){ class="shadow lightbox" title="Seite Darstellung im Menü Customizing" }

### Abschnitt Layout

Hier legen Sie fest, wie die ganze Instanz aussieht: Sie wählen in der Liste "Systemlayout" eines der installierten Themes. Die Auswahl gilt für alle Personen der Instanz, nicht nur für Ihre eigene Ansicht.

Ein neues Theme lässt sich nicht in der System-Administration erstellen. Die Liste "Systemlayout" zeigt nur die Themes, die auf dem Server Ihrer Instanz installiert sind. Zum Theme gehört auch das Hintergrundbild der Anmeldeseite. Für ein neues oder individuelles Theme wenden Sie sich bei gehosteten Instanzen an den Betreiber. frentix-Kund:innen wenden sich dafür an den frentix Support: [support@frentix.com](mailto:support@frentix.com). Betreiben Sie OpenOlat selbst, legen Sie das Theme als Ordner im Verzeichnis für eigene Themes auf dem Server ab.

Wurde ein bereits geladenes Theme auf dem Server geändert, zeigen Browser oft noch die alte Fassung aus ihrem Zwischenspeicher. Mit dem Button "Neuladen aller statischen Ressourcen erzwingen" laden alle Browser die Dateien des Themes neu. [:octicons-tag-16:{ title="ab Release 12.3 (OO-3235)" }](https://track.frentix.com/issue/OO-3235)

### Abschnitt Firmen- oder Institutionslogo [:octicons-tag-16:{ title="ab Release 10.0 (OO-1167)" }](https://track.frentix.com/issue/OO-1167){:target="_blank"}

Sie können ein eigenes Logo hochladen (png-Datei), das dann in der Hauptnavigation links oben angezeigt wird. Beachten Sie, dass dieses Logo innerhalb des Themes (Gesamtlayouts) verwendet wird. Als voreingestellter Standard wird das OpenOlat-Logo angezeigt.

Zusätzlich legen Sie fest, wohin ein Klick auf das Logo führt: auf die Startseite oder auf eine selbst gewählte Ziel-URL. Im Feld für den Alternativ-Text hinterlegen Sie den Text, der anstelle des Logos erscheint.

### Abschnitt Fusszeile Eigenschaften

In diesem Abschnitt legen Sie den Text der Fusszeile rechts unten fest sowie die Ziel-URL, auf die ein Klick auf die Fusszeile führt. E-Mail- und Link-Adressen im Text werden automatisch in einen anklickbaren Link umgewandelt.

[Zum Seitenanfang ^](#customizing)



## Impressum [:octicons-tag-16:{ title="ab Release 10.0 (OO-1166)" }](https://track.frentix.com/issue/OO-1166){:target="_blank"} {: #imprint}

Administrator:innen legen fest,

* wo der Link zum Impressum erscheint (z.B. im Footer)
* ob ein Impressumstext erscheint und wie er lautet
* ob ein Text zu den Nutzungsbedingungen innerhalb des Impressums erscheint und wie der Text lautet
* ob ein Text zur Datenschutzerklärung innerhalb des Impressums erscheint und wie der Text lautet
* ob ein Kontaktformular für allgemeine Anfragen erscheinen soll und an wen die Anfrage ggf. geschickt wird

Alle Texte können in verschiedenen Sprachen hinterlegt werden.

![Eingeschaltet und auf Position Footer gesetzt erscheint das Impressum als Link in der Fusszeile, die drei Texte werden je Sprache hinterlegt](assets/admin_customizing_imprint_v1_de.png){ class="shadow lightbox" title="Seite Impressum im Menü Customizing" }

[Zum Seitenanfang ^](#customizing)



## Hilfe [:octicons-tag-16:{ title="ab Release 15.1 (OO-4562)" }](https://track.frentix.com/issue/OO-4562){:target="_blank"} {: #help}

Damit Personen bei Fragen die passende Hilfe finden, legen Sie auf der Seite "Hilfe" fest, welche Hilfemöglichkeiten das Hilfe-Icon :fontawesome-solid-circle-question: anbietet, zum Beispiel das offizielle OpenOlat Handbuch, einen eigenen Hilfekurs oder ein Kontaktformular für den Support. Je Hilfemöglichkeit wählen Sie unter "Anzeige", ob sie im Autorenbereich, in den persönlichen Werkzeugen oder auf der Login-Seite erscheint.

![Unter Anzeige die drei Orte Autorenbereich, Persönliche Werkzeuge und Login, an denen die Hilfemöglichkeit erscheint, darüber Typ, Bezeichnung je Sprache, Symbol und URL](assets/admin_customizing_help_edit_v1_de.png){ class="shadow lightbox" title="Dialog Hilfemöglichkeit bearbeiten auf der Seite Hilfe · 2026.10.20" }

[Zum Seitenanfang ^](#customizing)



## Sprachanpassungswerkzeug {: #language_adaption_tool}

Passt eine Beschriftung der Oberfläche nicht zur Sprache Ihrer Organisation, ändern Sie mit dem Sprachanpassungswerkzeug einzelne Textelemente für die ganze Instanz. Der Button "Start" öffnet das Werkzeug in einem neuen Fenster.

[Zum Seitenanfang ^](#customizing)



## Systemregistrierung {: #system_registration}

OpenOlat ist Open-Source und braucht eine aktive Community von Anwender:innen. Mit der Systemregistrierung melden Sie Ihre Installation bei openolat.org an. Sie wählen dabei, ob OpenOlat statistische Daten anonym an openolat.org überträgt, ob die Installation auf openolat.org veröffentlicht wird und ob Sie über neue Releases und Sicherheitsupdates informiert werden.

[Zum Seitenanfang ^](#customizing)



## Portal {: #portal}

Für den Tab "Portal" können verschiedene Portlets ausgewählt werden.

!!! tip "Tipp"
    Wir empfehlen diese Einrichtung nicht einzusetzen. Sie ist überholt durch etliche Module in OpenOlat und ist damit ein historisches Überbleibsel, welches dennoch nicht einfach ausgeschaltet werden kann.

[Zum Seitenanfang ^](#customizing)



## Benutzer:innen-Attribute {: #user_properties}

Welche Angaben OpenOlat zu einer Person führt, wie diese Angaben heissen und wo sie erscheinen, legen Administrator:innen und Systemadministrator:innen für die ganze Instanz fest. So bestimmen Sie an einer Stelle, welche Daten Ihre Organisation erhebt und welche Felder Personen im Profil, beim Erstellen eines Kontos oder bei der Selbstregistrierung ausfüllen. Sie finden die Einstellungen in der System-Administration unter:<br>
`Administration > Customizing > Benutzer:innen-Attribute`

Die Seite hat drei Tabs: "Attribute" für die einzelnen Angaben, "Verwendungskontexte" für die Stellen, an denen die Angaben erscheinen, und "Zurücksetzen" für die ganze Konfiguration auf einmal.

### Was ist ein Attribut? {: #user_properties_attribute}

Jedes Feld, das eine Person in ihrem Profil ausfüllt, ist ein Attribut: eine einzelne Angabe zu einer Person, zum Beispiel "Geburtsdatum" oder "Organisationseinheit / Studiengruppe". Ein Attribut ist für die ganze Instanz entweder aktiv oder deaktiviert.

Der Tab "Attribute" listet alle Attribute mit ihrem technischen Namen und ihrer Beschriftung. Dort ordnen Sie ein Attribut einer Gruppe zu und passen in der Spalte "Übersetzen" seine Beschriftung je Sprache an. Die Gruppe bestimmt, unter welcher Überschrift das Feld im Profil steht: Felder der Gruppe "account" stehen dort unter "Personalien".

### Was ist ein Verwendungskontext? {: #user_properties_context}

Dasselbe Attribut erscheint an vielen Stellen von OpenOlat: im Profil, als Spalte in der Tabelle der Benutzerverwaltung, im Formular zum Erstellen eines Kontos, beim Importieren von Benutzer:innen, in der Selbstregistrierung und in den Angaben der REST API. Jede dieser Stellen ist ein Verwendungskontext. Ein Verwendungskontext führt seine eigene Auswahl an Attributen und legt je Attribut fest, ob es dort zwingend ist. So kann eine Angabe in der Benutzerverwaltung stehen, ohne dass die Selbstregistrierung danach fragt.

Der Tab "Verwendungskontexte" listet alle Verwendungskontexte mit ihrem technischen Namen und einer Beschreibung. Das Profil heisst dort zum Beispiel "org.olat.user.ProfileFormController".

Ob eine Angabe an einer Stelle erscheint, entscheidet sich deshalb zweimal: am Attribut, das aktiv sein muss, und am Verwendungskontext, der das Attribut verwenden muss.

### Konfiguration zurücksetzen [:octicons-tag-16:{ title="ab Release 21.1.1 (OO-9781)" }](https://track.frentix.com/issue/OO-9781) {: #user_properties_reset}

Nach vielen einzelnen Änderungen ist oft nicht mehr nachvollziehbar, welche Einstellung woher stammt. Mit dem Tab "Zurücksetzen" kehren Sie zu einem festen Stand zurück. Die Auswahlliste "Vordefinierte Konfiguration laden:" bietet zwei vordefinierte Konfigurationen:

  * **Default** stellt die Systemkonfiguration wieder her, also den Stand einer neuen Installation.
  * **Minimal** verwendet dieselben Verwendungskontexte, aber nur mit den Attributen "Anmeldename", "Vorname", "Nachname" und "E-Mail". Diese Konfiguration passt, wenn Ihre Instanz so wenige Angaben zu Personen wie möglich führen soll.

OpenOlat berechnet beide aus der Systemkonfiguration der installierten Version. Sie kennen deshalb jedes Attribut und jeden Verwendungskontext dieser Version, auch nach einem Update.

Ein Zurücksetzen ersetzt alle Einstellungen der Tabs "Attribute" und "Verwendungskontexte": welche Attribute aktiv sind, ihre Gruppen und in jedem Verwendungskontext die verwendeten Attribute, ihre Reihenfolge und die Einstellungen "Zwingend", "Nur Administrator:innen" und "Benutzer:innen: nur lesend". Eigene Anpassungen gehen dabei verloren. Beschriftungen, die Sie in der Spalte "Übersetzen" angepasst haben, bleiben erhalten.

!!! warning "Achtung"
    OpenOlat lädt die gewählte Konfiguration sofort nach "OK", ohne Rückfrage. Der Schritt lässt sich nicht rückgängig machen. Notieren Sie Ihre Einstellungen vorher, wenn Sie sie später wieder herstellen wollen.

Unter der Auswahlliste fasst eine Notiz beide Konfigurationen zusammen. Nach "OK" meldet OpenOlat "Vordefinierte Konfiguration wurde geladen...".

![Auswahlliste Vordefinierte Konfiguration laden mit dem Eintrag Default, darunter die Notiz zu Default und Minimal und dass eigene Anpassungen verloren gehen](assets/admin_customizing_user_properties_reset_v1_de.png){ class="shadow lightbox" title="Tab Zurücksetzen auf der Seite Benutzer:innen-Attribute · 2026.10.20" }

#### Skype ID, Xing, LinkedIn und ICQ {: #user_properties_social_media}

Die Attribute "Skype ID", "Xing", "LinkedIn" und "ICQ" sind in der Systemkonfiguration deaktiviert. Auf einer neuen Installation und nach "Default" erscheinen sie deshalb weder im Profil noch in der Benutzerverwaltung. Braucht Ihre Organisation eines davon, aktivieren Sie es im Tab "Attribute" in der Spalte "Aktiv".

Auf einer bestehenden Installation hängt es davon ab, ob die Einstellungen dieser Seite schon einmal gespeichert wurden. Wurden sie nie geändert, sind die vier Attribute nach dem Update ebenfalls deaktiviert. Wurden sie schon einmal geändert, bleiben die vier Attribute so, wie sie gespeichert sind, bis Sie "Default" laden. Werte, die Personen bereits erfasst haben, löscht OpenOlat in keinem Fall.

[Zum Seitenanfang ^](#customizing)



## Bereiche {: #sites}

Auf der Seite "Bereiche" legen Administrator:innen fest, welche Bereiche die Hauptnavigation in der obersten Zeile anbietet, in welcher Reihenfolge und für welche Rollen. Sie finden die Seite in der System-Administration unter:<br>
`Administration > Customizing > Bereiche`

Was ein Bereich ist und wovon abhängt, ob eine Person ihn sieht, erklärt das Benutzerhandbuch auf der Seite [Bereiche und Module](../../manual_user/area_modules/index.de.md#conditions).

### Tab Reihenfolge

Im Tab "Reihenfolge" schalten Sie die Bereiche für die ganze Instanz frei und ordnen sie. Die Checkbox "Aktiviert" gibt einen Bereich frei, die Pfeile "Hoch" und "Runter" legen die Reihenfolge fest. Einzelne Einträge heissen in der Liste anders als der Bereich in der Hauptnavigation: Der Eintrag "Meine Kurse" erscheint dort als "Kurse".

Der Eintrag "Coaching Werkzeug" lässt sich nicht deaktivieren, weil Betreuer:innen und Besitzer:innen ihre Lernressourcen über das Coaching erreichen: Die Checkbox "Aktiviert" ist ausgegraut. Reihenfolge und Zugang bleiben einstellbar. [:octicons-tag-16:{ title="ab Release 21.0.1 (OO-9661)" }](https://track.frentix.com/issue/OO-9661)

![Checkbox Aktiviert beim Eintrag Coaching Werkzeug ausgegraut, Zugang und die Pfeile Hoch und Runter bleiben einstellbar](assets/admin_customizing_sites_v3_de.png){ class="shadow lightbox" title="Tab Reihenfolge auf der Seite Bereiche · 2026.10.09" }

Die Liste gilt für die ganze Instanz. Drei weitere Punkte entscheiden mit darüber, ob eine Person einen Bereich sieht.

**Das Modul muss aktiv sein.** Ein Eintrag erscheint nur, wenn zusätzlich das zugehörige Modul eingeschaltet ist. Ein aktivierter Eintrag "Katalog" bleibt ohne Wirkung, solange das [Modul Katalog](Modules_Catalog_2.0.de.md) ausgeschaltet ist. Bei ausgeschaltetem Modul ist die Checkbox "Aktiviert" des Eintrags ausgegraut.

**Die Spalte "Zugang" entscheidet je Rolle.** Sie bestimmt, welche Rollen den Bereich sehen, zum Beispiel "Registrierte Konten ohne Gäste/externe Benutzer:innen" oder "Autor:innen und Lernressourcenverwalter:innen". Zwei Personen mit verschiedenen Rollen sehen deshalb eine verschiedene Hauptnavigation.

**Der Platz in der Zeile entscheidet über die Darstellung.** Bereiche, die nicht mehr in die oberste Zeile passen, sammelt OpenOlat im Menü "Mehr" am rechten Rand. Das hängt von der Bildschirmbreite der Betrachterin ab und lässt sich nicht einstellen.


### Übrige Tabs [:octicons-tag-16:{ title="ab Release 9.1 (OO-715)" }](https://track.frentix.com/issue/OO-715){:target="_blank"}

In den Tabs "Infoseite n°1" bis "Infoseite n°4" binden Sie je einen Kurs als eigenen Bereich in die Hauptnavigation ein, zum Beispiel für Informationen an alle Personen der Instanz.

![Je Sprache ein eigener Titel und eine eigene Lernressource, hervorgehoben die Zeile für Deutsch, darüber Kurs-Toolbar für alle anzeigen und Icon CSS Class](assets/admin_customizing_infopage_v2_de.png){ class="shadow lightbox" title="Tab Infoseite n°1 auf der Seite Bereiche · 2026.10.09" }

Je Sprache hinterlegen Sie einen eigenen Titel und eine eigene Lernressource. Mit "Auswählen" öffnen Sie die Suche nach der referenzierbaren Lernressource. Erst dort verbinden Sie den Bereich mit einem Kurs. Die Checkbox "Standard" bestimmt den Eintrag, der gilt, wenn für die Sprache einer Person keiner hinterlegt ist.

Im Feld "Icon CSS Class" legen Sie das Symbol des Bereichs fest. Mit der Checkbox "Kurs-Toolbar für alle anzeigen" sehen alle Personen die Toolbar des Kurses. Ohne Häkchen sehen sie nur Personen, die den Kurs verwalten dürfen, zum Beispiel Besitzer:innen.

![Kurs aus der Liste wählen, oder über Erstellen und Datei importieren eine neue Lernressource anlegen](assets/admin_customizing_infopage_select_v1_de.png){ class="shadow lightbox" title="Dialog Referenzierbare Lernressource suchen" }

In den Tabs "Externe Seite n°1" und "Externe Seite n°2" binden Sie je Sprache eine externe URL mit eigenem Titel als Bereich ein. [:octicons-tag-16:{ title="ab Release 18.2 (OO-7398)" }](https://track.frentix.com/issue/OO-7398)

Mit der Checkbox "iFrame" zeigt OpenOlat die Seite eingebettet im Bereich an. Beim Speichern ruft OpenOlat die Adresse auf und prüft, ob die Seite eine Einbettung erlaubt. Liegt die Adresse im lokalen Netz und ist unter `Administration > Login > Sicherheit` die Checkbox "SSRF Mitigation" gewählt, weist OpenOlat die Adresse ab. Eine abgewiesene Adresse meldet OpenOlat gleich wie eine Seite, die keine Einbettung erlaubt: "Diese URL unterstützt keine iFrame Einbettung." Eine Adresse aus dem lokalen Netz lässt sich nur über eine Ausnahme in der Serverkonfiguration freigeben, siehe [Sicherheit](Login_Security.de.md#ssrf). [:octicons-tag-16:{ title="ab Release 21.1 (OO-9310)" }](https://track.frentix.com/issue/OO-9310)

[Zum Seitenanfang ^](#customizing)



## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Bereiche und Module >](../../manual_user/area_modules/index.de.md)<br>
[Modul Katalog >](Modules_Catalog_2.0.de.md)<br>
[Sicherheit >](Login_Security.de.md)

**Weiterführend**<br>
[Module: Übersicht >](Modules.de.md)<br>
[Startseite >](Landing_pages.de.md)<br>
[Navigation >](../../manual_user/basic_concepts/Navigation.de.md)

[Zum Seitenanfang ^](#customizing)


