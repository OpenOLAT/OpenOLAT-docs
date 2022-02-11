# Kursbaustein "Einzelne Seite"

![](assets/single_page.png)

Im Kursbaustein „Einzelne Seite“ können Sie HTML und PDF Dateien direkt in die
Kursstruktur einbinden. Geben Sie auf diesem Weg beispielsweise zentrale
Informationen, den Kursablauf oder Literaturtipps zu Ihrem Kurs bekannt oder
platzieren Sie Inhalte wie Bilder oder Videos gezielt im Kurs. Die Dateien
selbst werden dabei im [Ablageordner ](../course_operation/Storage_folder.de.md)des Kurses angelegt.

  

Für die Einbindung von Office-Dokumenten nutzen Sie bitte den [Kursbaustein

sites/manual_user/docs/course_elements/Course_Element_Single_Page.de.md §Knowledge_Transfer.de.md§ 481
"Dokument".](Knowledge_Transfer.de.md)

## Tab Seiteninhalt

Sie haben folgende Möglichkeiten, um den gewünschten Seiteninhalt in Ihren
Kurs zu integrieren:

  * Neue HTML-Seite online erstellen
  * Eine beliebige Datei aus dem Ablageordner wählen
  * Eine Datei in den Ablageordner hochladen und mit dem Baustein verknüpfen

![](../../download/attachments/108593372/Einzelseite%EF%B9%96version=1&modificationDate=1566731300000&api=v2&effects=drop-
shadow.png)

Für die weitere Bearbeitung von HTML-Seiten können Sie den OpenOlat Editor
nutzen. Er funktioniert ähnlich wie ein Textverarbeitungsprogramm. Die
automatisch erstellte Datei, wenn Sie zum ersten Mal eine Seite erstellen,
trägt bereits den Namen des Kurselements. Einmal angelegt, öffnen Sie die
Datei mit dem Link "Datei im Editor öffnen" und Sie gelangen in den OpenOLAT
HTML Editor.

![](assets/html_editor.png)

Im HTML Editor können Sie neben den verschiedenen Formatierungen auch
Verlinkungen zu Bildern, Videos, den einzelnen Kursbausteinen des Kurses und
zu den Tools in der [Toolbar

sites/manual_user/docs/course_elements/Course_Element_Single_Page.de.md §Using_Additional_Course_Features.de.md§ 481
](../course_operation/Using_Additional_Course_Features.de.md)einfügen.

Sie können auch Dateien die Sie zuvor erstellt haben in den Ablageordner des
Kurses hochladen oder einen Ressourcenordner mit dem Kurs und dem Ablageordner
verbinden. Über den Link "Datei auswählen" werden Ihnen alle Dateien
angezeigt, die sich im Ablageordner befinden. Anschließend können Sie diese
Dateien über den Kursbaustein "Einzelne Seite" verlinken und so in Ihren Kurs
einbinden. Dieser Weg empfiehlt sich, wenn Sie die Strukturierung des
Ablageordners selbst beeinflussen möchten.

Mit der "Einzelnen Seite" können auf verschiedene Weise Videos und Audios in
den Kurs eingebunden werden. Detaillierte Information finden Sie

sites/manual_user/docs/course_elements/Course_Element_Single_Page.de.md §Single_Page_Add_edit_video.de.md§ 481
[hier](../resource_video/Single_Page_Add_edit_video.de.md).

Die Dateien können bei Bedarf später auch über den Link "Seite ersetzen"
wieder gewechselt werden.

  

Öffnen und speichern Sie HTML-Seiten, die Sie mit einem externen Editor
erstellt haben, nicht mit dem eingebauten HTML-Editor, da dadurch Teile der
Formatierung verloren gehen können. Der OpenOlat HTML-Editor enthält nur den
<body> Bereich einer HTML Seite. Sollen Einträge im HTML <head> vorgenommen
werden, muss dies in einem externen Editor erfolgen.

Unter „Sicherheitseinstellungen“ können Sie festlegen, ob Verweise in Ihren
HTML-Seiten nur auf Dateien des gleichen Ordners und auf darin enthaltene
Unterordner möglich sind, oder ob alle Dateien des Ablageordners referenziert
werden können. Dies ist beispielsweise notwendig, wenn Ihre HTML Seite
Grafiken, CSS-Dateien oder Skripte enthält, die sich in anderen Ordnern
befinden.

Ferner können Sie definieren, ob Betreuer die hinterlegte HTML-Datei
bearbeiten dürfen. Die Betreuer benötigen dafür keine Kursbesitzerrechte oder
Zugang zum Kurseditor.

## Tab Anzeige Inhalt

Im Tab „ **Anzeige Inhalt** “ definieren Sie die Einstellungen für die Anzeige
des Seiteninhalts. Hier legen Sie fest ob die Seite unverändert, oder
optimiert für OpenOlat angezeigt werden soll. Der Anzeigemodus „Optimiert für
OpenOlat“ gestattet Ihnen z.B. das Kurslayout auf den Seiteninhalt anzuwenden,
oder ein in den Kurs eingebundenes Glossar für die Seite zu aktivieren.

  

 Layout Optionen der Einzelnen Seite

* * *

 **Anzeigemodus:** Wählen Sie den Modus "Standard" um die Ressource
unverändert anzuzeigen. Dieser Modus ist geeignet für Ressourcen, bei denen es
im Modus "Optimiert für OpenOlat" zu Anzeigeproblemen kommt, was vor allem bei
extern erstelltem Inhalt passieren kann, wie z.B. HTML5 Seiten. Wählen Sie den
Modus "Optimiert für OpenOlat", wenn Sie das Kurslayout in der Seite einbinden
wollen, eine JavaScript Bibliothek verwenden möchten, das OpenOlat Glossar auf
dieser Seite anwenden wollen oder die Höhe der Seite automatisch berechnet
werden soll. Bei SCORM Modulen ist der Modus "Standard" empfohlen.

* * *

 **JavaScript hinzufügen:** Um die Funktionen des Anzeigemodus "Optimiert für
OpenOlat" nutzen zu können muss die JavaScript Bibliothek "jQuery" aktiviert
sein. Die Option "Prototype" sollte nur gewählt werden, wenn Ihre Inhalte
diese Bibliothek voraussetzen. Wählen Sie keine Bibliothek, wenn es zu
Anzeigeproblemen mit Ihren Inhalten kommt.

 **Glossarbegriffe einbinden:** Wählen Sie diese Option um die Möglichkeit der
Hervorhebung von Glossarbegriffen für Ihre HTML-Seiten zu aktivieren sofern
Sie ein Glossar in Ihrem Kurs eingebunden haben. Diese Option setzt die
Verwendung der JavaScript Bibliothek "jQuery" voraus.

 **Höhe Anzeigefläche:** Mittels des Drop-Down-Menus können Sie die Höhe der
Inhalte bestimmen. Sie haben die Möglichkeit, diese via "Automatisch" auf die
jeweilige Fensterhöhe zu setzen oder auf einen bestimmten Wert zu setzen.

 **Layout anpassen:** Wählen Sie die Option "OpenOlat Stylesheets" um das
OpenOlat und Kurslayout in Ihre Seite zu übernehmen (Schriftart, Farben,
Grösse etc). Wenn Sie diese Anpassung nicht wünschen wählen Sie die Option
"Keine".

* * *

 **Zeichensatz Inhalt:** OpenOlat versucht, den Zeichensatz automatisch zu
erkennen. Wenn die Option "Automatisch" nicht zu der gewünschten Anzeige
führt, kann die Kodierung des Inhalts anhand eines vordefinierten
Zeichensatzes konfiguriert werden (ist keine Kodierung vorhanden, wird per
Default der Zeichensatz ISO-8899-1 verwendet).

 **Zeichensatz Javascript:** Erlaubt die Kodierung des Javascript Codes anhand
eines vordefinierten Zeichensatzes (per Default wird der gleiche Zeichensatz
für Inhalt und Javascript verwendet).

In der Regel sind im Tab "Layout" keine Änderungen notwendig. Die
Standardeinstellungen passen für 90% der Kurse.

#  Mehrere Einzelseiten

![](assets/wizard_434343_64.png)

Mit dieser Option können Sie sich das Hinzufügen und organisieren von
Einzelseiten in den Kurs erleichtern und die Dateien rasch in der Kursstruktur
sichtbar machen. Wenn Sie beim Hinzufügen von Kursbausteinen "Mehrere
Einzelseiten" wählen, öffnet sich die Anzeige des Ablageordners mit allen im
jeweiligen Kurs verfügbaren Dateien. Sie können nun alle Dateien auf einmal
auswählen, die Sie direkt als Einzelne Seite hinzufügen möchten. Entscheiden
Sie auch, ob die ausgewählten Dateien nach oder als Unterordner des aktuellen
Kursbausteins eingefügt werden sollen. Die Reihenfolge kann im Anschluss
verändert werden.

Die Funktion "Mehrere Einzelseiten" bietet sich an, wenn Sie bereits mehrere
HTML-Dateien bzw. komplexe Hypermedia-Dateien extern erstellt und im

sites/manual_user/docs/course_elements/Course_Element_Single_Page.de.md §Storage_folder.de.md§ 481
[Ablageordner ](../course_operation/Storage_folder.de.md)des Kurses abgelegt haben. Achten Sie bei
komplexen Seiten mit diversen Verlinkungen zu Grafiken u.ä. darauf die Option
"Link im gesamten Ablageordner erlauben" zu aktivieren. Ferner sollten Sie die
Dateinamen möglichst schon so benennen wie Sie später im Kurs erscheinen
sollen, da der Dateiname als Kursbaustein Titel verwendet wird.

Mehrere Einzelseiten lassen sich auch sehr gut mit einem [Kursbaustein
"Struktur"](../../pages/viewpage.action%EF%B9%96pageId=108593217.html)
bündeln. So können automatisch Übersichtsseiten für die jeweiligen Inhalte
erstellt werden und die Einzelnen Seiten besser strukturiert werden.

  

  

