# Kursbaustein "Ordner"

## Steckbrief

Name | Ordner
---------|----------
Icon | ![Ordner Icon](assets/folder.png){ class=size24  }
Verfügbar seit | Neuauflage mit Release 17.1
Funktionsgruppe | Wissensvermittlung
Verwendungszweck | Bereitstellung von Dateien zum Download (z.B. Material zum Kurs)
Bewertbar | nein
Spezialität / Hinweis | Ein ähnlicher Kursbaustein ist der Kursbaustein "Teilnehmer Ordner". 


Im Kursbaustein "Ordner" können Dateien zum Download abgelegt und für die Lernenden bereitgestellt werden. Häufig wird der Kursbaustein "Ordner" dazu verwendet, Kursmaterialien wie Folien oder Skripte zur Verfügung zu stellen. Darüber hinaus kann der Kursbaustein "Ordner" auch als kollaboratives Werkzeug für den Dateiupload der Lernenden konfiguriert werden.

Bitte beachten: Die Reihenfolge der Dateien ist nicht fix. Der User kann sich die Dateien entsprechend der Spalten nach Namen, Grösse und Änderungsdatum sortieren.

## Allgemeines

Im Kursbaustein "Ordner" können Lehrende Dateien zum Download bereitstellen. Standardmässig sind Ordner Kursbausteine so konfiguriert, dass nur Besitzer und Betreuer Dateien hochladen dürfen und Kursteilnehmer lediglich das Recht haben, Dateien zu lesen bzw. herunterzuladen.

Abonnieren Sie den Ordner, um bei neuen Dokumenten benachrichtigt zu werden. Änderungen erfahren Sie per E-Mail oder unter "Abonnements" in OpenOlat.

:octicons-device-camera-video-24: **Video-Einführung**: [Abonnements](<https://www.youtube.com/embed/h9gOqt7TR7Q>){:target="_blank”}

Wenn der Ordner dazu eingesetzt wird, dass Kursteilnehmer ebenfalls Dateien hochladen dürfen, finden Sie in der Leiste über den Dateien, die entsprechenden Funktionen. Sie können dann auch Dateien löschen, Unterordner einrichten. Wenn Sie verhindern möchten, dass jemand Ihre Dateien löscht, können Sie in der Tabellenansicht auf das Icon [Metadaten](../basic_concepts/Full_Text_Search.de.md#Volltextsuche-_metadata) klicken und die Datei sperren. Gesperrte Dateien sind mit einem Schloss gekennzeichnet.

![Locked files in folder](assets/KB_Ordner_schloss.png)

!!! info "Achtung"

    Nicht verwechseln: Neben den Download Ordnern in Kursen stehen Lernenden auch [Persönliche Ordner](../personal_menu/Personal_folders.de.md) zur Verfügung, die kursunabhängig für das individuelle Lernen genutzt werden können. Ferner gibt es den Kursbaustein "Teilnehmer Ordner" (siehe unten).

## Tab Ordnerkonfiguration {: #config}

![tab folder configuration](assets/KB_Ordner_16.png)

Im Tab "Ordnerkonfiguration" des Kursbausteins legen Sie fest wo genau die Dateien dieses Ordners im Ablageordner des Kurses abgelegt werden sollen. Hierfür kann OpenOlat entweder automatisch einen Ordner (=Ablagebereich) generieren oder Sie wählen einen spezifischen Ordner aus dem Ablageordner des Kurses aus.

Wird die Option "Automatisch generierter Ordner" gewählt, legt OpenOlat den Unterordner _courselementdata_ inklusive eines Unterordners mit dem Namen des jeweiligen Kursbaustein "Ordners" an. Alle Dateien des Kursbausteins werden nun hier gespeichert.

Wählt man "Ordner aus Ablageordner des Kurses verwenden" kann ein bereits existierender Ordner aus dem Ablageordner des Kurses ausgewählt werden. Das bietet sich besonders an, wenn Sie die Dateien, die Sie bereitstellen wollen, bereits sinnvoll im Ablageordners des Kurses strukturiert hochgeladen haben. Wählen Sie im nächsten Schritt einen existierenden Ordner des Ablageordners aus oder erstellen Sie im Ablageordner einen neuen Unterordner. Über den Ablageordner können Sie, sofern in den [Kurseinstellungen](../learningresources/Course_Settings.de.md) entsprechend konfiguriert, auch auf einen verknüpften Ressourcenordner zugreifen.

Anschließend können sie im Bereich "Dateien hochladen" über den Link "Ordner verwalten" Dateien an die zuvor definierte Stelle hochladen bzw. sich die bereits hochgeladenen Dateien anzeigen lassen.

Ein Zugriff auf diesen Dateibereich ist auch bei geschlossenem Editor möglich.

### Benutzerberechtigungen einstellen

Ferner kann im Bereich "Benutzerberechtigungen" definiert werden ob auch Betreuende und/oder Teilnehmende Dateien in den Ordner hochladen und bearbeiten dürfen. Standardmäßig dürfen neben den Besitzer:innen auch Betreuer:innen, aber nicht die Teilnehmer:innen Dateien hochladen.

## Einstellungen bei geschlossenem Editor

![folder screenshot](assets/KB_Ordner.png)

Im Kursrun können Kursbesitzer und Personen mit der entsprechenden Berechtigung

  * Dateien hoch- und runterladen
  * Dateien löschen, verschieben und kopieren
  * neue Dokumente erstellen
  * je nach Dateityp auch Dateien bearbeiten (siehe unten)
  * neue Unterordner innerhalb des Kursbausteins erstellen. So kann ein Kursbaustein "Ordner" mehrere Unterordner enthalten. Die Verwendung von mehreren Kursbausteinen Ordnern sind nur notwendig, wenn die Ordner an unterschiedlichen Stellen in der Kursstruktur eingebunden werden sollen oder die Ordner mit unterschiedlichen selektiven Freigaben verbunden sind.

Um das Hoch- und Herunterladen von mehreren Dateien zu erleichtern können die Dateien gezippt zw. entzippt werden. Darüber hinaus empfiehlt sich für den Upload von umfangreicheren Materialien die Verwendung von [WebDAV](../basic_concepts/Using_WebDAV.de.md).

Ferner können alle User ...

  * Dateien des Ordners per E-Mail an registrierte OpenOlat User verschicken
  * die Dateien des Ordners nach Stichworten durchsuchen
  * den Ordner abonnieren und so schnell informiert über Änderungen informiert werden

### Metadaten {: #metadata}

Über das Zahnradsymbol können die [Metadaten](../basic_concepts/Full_Text_Search.de.md#metadata) einer Datei konfiguriert werden und so diverse Informationen hinzugefügt werden. Neben der Beschreibung und Sperreigenschaften sind besonders die Lizenzangaben relevant. Über die Lizenzangaben können Sie eine konkrete Lizenz für das Dokument hinterlegen, z.B. eine der existierenden Creative Commons Lizenzen verwenden, den Lizenzgeber eintragen sowie weitere Informationen zum Herausgeber, zur Quelle, zum Erscheinungsdatum usw. hinterlassen. Die Lizenz wird im Ordnerbaustein in einer separaten Spalte angezeigt. Mit Klick auf die Lizenz erhält der User die hinterlegten Informationen zur jeweiligen Lizenz.

In den Metadaten wird auch angezeigt, wie häufig eine Datei aufgerufen wurde. Ferner gibt es einen Link mit dem Sie die jeweilige Datei direkt verlinken können. Ob auch externe Personen auf die Datei zugreifen können, ist von den Zugangseinstellungen des Kurses abhängig.

### Dateien bearbeiten

Je nach Dateityp und Aktivierung in der OpenOlat [Administration](../../manual_admin/administration/External_Tools_-_Administration.de.md) ist es möglich Dateien, die sich im Kursbaustein "Ordner" befinden, zu bearbeiten. Sofern eine Bearbeitung möglich ist, erscheint in der Tabelle das Bearbeitungsicon ![editing icon](assets/test.png){ class=size16 }. Bei Klick auf das Icon öffnet sich der jeweilige Bearbeitungseditor, z.B. Only Office. Durch die Verwendung dieser externen, kooperativen Bearbeitungswerkzeuge, kann der Kursbaustein "Ordner" auch für das kollaborative Arbeiten der Lernenden verwendet werden.
