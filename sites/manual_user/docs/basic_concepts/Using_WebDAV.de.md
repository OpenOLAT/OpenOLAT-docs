# Einsatz von WebDAV {: #using_webdav}

WebDAV steht für "Web-based Distributed Authoring and Versioning" und ist ein offener Standard zur Übermittlung von Dateien im Internet. OpenOlat unterstützt dieses Protokoll und ermöglicht so einen einfachen Dateitransfer von Ihrem Rechner zu OpenOlat-Ordnern.

!!! info "Vorteile von WebDAV"

    Ohne WebDAV können Dateien nur über herkömmliche Upload-Formulare in OpenOlat hochgeladen werden. Dabei wählen Sie entweder jede Datei einzeln oder mehrere gezippte Dateien aus. Mit WebDAV hingegen können Sie von Ihrem Rechner bequem mehrere Dateien oder komplette Ordnerstrukturen in OpenOlat-Ordner kopieren, z.B. in den Ablageordner eines Kurses.

## WebDAV-fähige OpenOlat-Ordner

Über WebDAV können Sie auf folgende OpenOlat-Ordner zugreifen. Die Struktur wird automatisch erstellt, sobald die Elemente in OpenOlat angelegt sind:

  * [Persönliche Dateien](../personal_menu/File_Hub.de.md#personal_files) des File Hubs (alle Benutzer:innen)
  * Ordner von [Gruppen](../groups/Using_Group_Tools.de.md)
  * [Ablageordner von Kursen](../learningresources/Storage_folder.de.md) (nur Kursbesitzer:innen)
  * [Kursbaustein "Ordner"](../learningresources/Course_Element_Folder.de.md)
  * [Ressourcenordner](../learningresources/index.de.md#resource_folder) (nur Besitzer:innen der Lernressource)
  * [Kursarchive](../learningresources/Course_Archiving.de.md) (nur Autor:innen, Lernressourcenmanager:innen und Administrator:innen) [:octicons-tag-16:{ title="ab Release 19.0 (OO-7504)" }](https://track.frentix.com/issue/OO-7504)

Wer in den jeweiligen Ordnern Dateien per WebDAV hochladen darf, ist abhängig von der konkreten Konfiguration.

## Voraussetzungen

Microsoft Windows, macOS, iOS, Android und Linux unterstützen WebDAV für die Dateiübermittlung per Drag & Drop standardmässig. Inzwischen bieten auch diverse Anwenderprogramme (z.B. Microsoft Office) WebDAV-Funktionalität an.

Um einen Ordner auf OpenOlat über WebDAV zu erreichen, benötigen Sie:

  * WebDAV-Link: Diesen Link finden Sie unterhalb von WebDAV-fähigen Ordnern oder in den [Einstellungen](../personal_menu/Settings.de.md#tab_webdav) Ihres persönlichen Menüs unter:<br>`Persönliches Menü > Einstellungen > Tab "WebDAV"`
  * Ihren OpenOlat-Benutzernamen, alternativ die hinterlegte E-Mail-Adresse
  * Ihr OpenOlat-/WebDAV-Passwort

Falls Sie mit Shibboleth oder einem Cloud Login auf OpenOlat zugreifen, können Sie sich Ihr WebDAV-Passwort in den Einstellungen im persönlichen Menü einrichten. Wählen Sie hierzu den Link "Einstellungen" und klicken Sie anschliessend im Tab "WebDAV" auf die Schaltfläche "Passwort einrichten". Wenn Sie bereits über ein OpenOlat-Passwort verfügen, verwenden Sie dieses für den WebDAV-Zugang.

## Problembehandlung

Bei Problemen gehen Sie die nachfolgenden Punkte durch:

!!! warning "Zu beachten"

    * Je nach Betriebssystem (vor allem Windows) können Dokumente grösser als 50 MB nicht über WebDAV geöffnet werden
    * Das Speichervolumen des WebDAV-Ordners ist begrenzt
    * Überprüfen, ob die Quota überschritten wurde (vor allem, wenn mehrere Dateien zusammen hochgeladen wurden)
    * Dateinamen sind auf 100 Zeichen begrenzt
    * Dateinamen dürfen nicht mehrere Leerschläge hintereinander beinhalten
    * Bei Umlauten in Ordnernamen werden ggf. Unterordner und enthaltene Dokumente nicht angezeigt

## Einrichten der WebDAV-Verbindung

??? abstract "Windows 11 (sowie 7, 8 und 10)"

    1. Starten Sie den Windows Explorer.
    2. Klicken Sie mit der rechten Maustaste auf "Dieser PC".
    3. Wählen Sie "Netzlaufwerk verbinden".
    4. Wählen Sie einen Buchstaben für das Laufwerk.
    5. Wählen Sie ganz unten den Punkt "Verbindung mit einer Webseite herstellen, auf der Sie Dokumente und Bilder speichern können" aus.
    6. Klicken Sie auf "Weiter".
    7. Markieren Sie "Eine benutzerdefinierte Webadresse auswählen".
    8. Klicken Sie auf "Weiter".
    9. Geben Sie den WebDAV-Link ein.
    10. Klicken Sie auf "Weiter".
    11. Geben Sie nun Ihren OpenOlat-Benutzernamen bzw. die hinterlegte E-Mail-Adresse und Ihr Passwort ein.
    12. Klicken Sie auf "Fertigstellen".

??? abstract "Windows Vista"

    1. Klicken Sie im Startmenü auf "Computer".
    2. Klicken Sie im folgenden Fenster in der Menüleiste oben auf "Netzlaufwerk zuordnen" (unter "Weitere Befehle").
    3. Wählen Sie ganz unten den Punkt "Verbindung mit einer Webseite herstellen" aus.
    4. Klicken Sie auf "Weiter".
    5. Markieren Sie "Eine benutzerdefinierte Netzwerkressource auswählen".
    6. Klicken Sie auf "Weiter".
    7. Geben Sie bei der Internet- oder Netzwerkadresse den WebDAV-Link ein.
    8. Klicken Sie auf "Weiter".
    9. Geben Sie nun Ihren OpenOlat-Benutzernamen bzw. die hinterlegte E-Mail-Adresse und Ihr Passwort ein.
    10. Sie können einen Namen für die WebDAV-Verbindung eingeben.
    11. Klicken Sie auf "Fertigstellen".

??? abstract "Mac"

    1. Öffnen Sie im Finder das Menü "Gehe zu" und dann "Mit Server verbinden" und geben Sie dort den WebDAV-Link ein.
    2. Geben Sie nun Ihren OpenOlat-Benutzernamen bzw. die hinterlegte E-Mail-Adresse und Ihr Passwort ein.
    3. Klicken Sie auf "OK".

??? abstract "Linux"

    Für Linux-Benutzer:innen gibt es drei Möglichkeiten:

    1. KDE Plasma: Geben Sie im Dolphin in der Pfadleiste `webdavs://` + WebDAV-Link ein. Es wird nach Benutzername und Passwort gefragt. Sollte die Pfadleiste nicht angezeigt werden, so kann sie jederzeit mit der Taste F6 aktiviert werden. Beispiel: `webdavs://www.olat.uzh.ch/olat/webdav/`.
    2. Gnome: Geben Sie `davs://` + Benutzername oder E-Mail-Adresse + `@` + WebDAV-Link ein. Beispiel: `davs://pmuster@www.olat.uzh.ch/olat/webdav/`.
    3. FUSE: WebDAV-Verzeichnisse können direkt ins Dateisystem gemountet werden (geht auch unter macOS, mehr dazu auf der [FUSE-Website](http://fuse.sourceforge.net "FUSE-Website")).

??? abstract "Alternative"

    Neben den beschriebenen Verfahren unter "Einrichten der WebDAV-Verbindung" kann alternativ ein WebDAV-Client eingesetzt werden. Je nach Umgebung, vor allem bei Windows in Verbindung mit Citrix, kann ein solcher Client stabiler funktionieren als die direkte WebDAV-Verbindung. Einige Beispiele für WebDAV-Clients:

    * Windows: Cyberduck, WinSCP
    * Mac: Cyberduck, Commander One

## Ordnerstruktur

Wenn Sie die Verbindung erfolgreich eingerichtet haben, öffnet sich auf Ihrem Rechner ein Verzeichnis, das die folgenden Unterverzeichnisse enthält:

  * **coursefolders**: Hier haben Sie Zugriff auf die [Ablageordner](../learningresources/Storage_folder.de.md) aller Kurse, die Sie besitzen. Für jeden Kurs wird automatisch ein WebDAV-Ordner angelegt. Klicken Sie auf den WebDAV-Ordner eines Kurses und Sie sehen die Dateien und die Struktur des jeweiligen Ablageordners und können Dateien hochladen, löschen, ändern usw. Neben den von Ihnen angelegten Dateien und Ordnern legt OpenOlat je nach Konfiguration automatisch weitere Ordner an. Diese erreichen Sie ebenfalls über WebDAV. Den Ablageordner sehen nur die Besitzer:innen eines Kurses. Betreuer:innen und Teilnehmende finden hier nur die Ordner der Kursbausteine "Ordner" sowie eingebundene Ressourcenordner, sofern die System-Administration diesen Zugriff freigeschaltet hat (siehe [WebDAV (Administration)](../../manual_admin/administration/WebDAV.de.md)).

    * _other_: Dieser Ordner erscheint nur, wenn die Kurse in der System-Administration nach Semesterdaten oder CPL-Elementen gruppiert werden. In diesem Ordner befinden sich alle Kurse, welche _keinem_ Semester bzw. Element zugeordnet sind.
    * _finished_: Dieser Ordner erscheint nur, wenn die Kurse nicht gruppiert werden. In diesem Ordner befinden sich alle Kurse mit dem Status "Beendet".

  * **groupfolders**: Hier finden Sie alle Gruppen, in denen Sie eingetragen sind und auf deren Ordner Sie Zugriff haben.
  * **home**: Ihre persönlichen Dateien mit den Unterordnern "private" und "public".
  * **sharedfolders**: Alle Ressourcenordner, die Sie besitzen oder auf die Sie aufgrund einer Mitgliedschaft zugreifen dürfen. Besitzer:innen und Betreuer:innen erhalten Lese- und Schreibrechte, Teilnehmende nur Leserechte.
  * **mycoursearchives**: Alle [Kursarchive](../learningresources/Course_Archiving.de.md), die Sie erstellt haben. Dieser Ordner erscheint nur für Autor:innen, Lernressourcenmanager:innen und Administrator:innen.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Persönliche Werkzeuge: File Hub >](../personal_menu/File_Hub.de.md)<br>
[Gruppenwerkzeuge nutzen >](../groups/Using_Group_Tools.de.md)<br>
[Ablageordner >](../learningresources/Storage_folder.de.md)<br>
[Kursbaustein "Ordner" >](../learningresources/Course_Element_Folder.de.md)<br>
[Lernressourcen >](../learningresources/index.de.md)<br>
[Kursadministration - Archivierung & Reports >](../learningresources/Course_Archiving.de.md)<br>
[Persönliche Konfiguration: Einstellungen >](../personal_menu/Settings.de.md)<br>
[FUSE-Website >](http://fuse.sourceforge.net)<br>
[WebDAV (Administration) >](../../manual_admin/administration/WebDAV.de.md)

[Zum Seitenanfang ^](#using_webdav)
