# Der Portfolio Editor {: #portfolio_editor}

Jedem Portfolioeintrag können unterschiedliche Layouts und Inhaltselemente hinzugefügt werden. Auch ältere Einträge füllen Sie mit diesen Layouts weiter. Die Konfiguration erfolgt über drei Bedienelemente: das Layoutmenü, das Blockmenü und den Inspektor.

## Bedienelemente im Überblick

Der Portfolio Editor umfasst verschiedene Menü-Bereiche für die Konfiguration:

![Portfolio Editor mit den Bedienelementen: Layoutmenü in der Kopfzeile eines Layouts, Blockmenü mit Zahnrad und Anfasser über einem Inhaltselement, rechts der Inspektor zum markierten Bild](assets/content-editor-gui.de.jpeg){ class="shadow lightbox" }

* **Layoutmenü**: Ein Layout ist ein übergeordneter Bereich, der unterschiedliche Strukturierungen des Inhalts durch Spalten und Zeilen ermöglicht. Im Layoutmenü kann ein ein- oder mehrspaltiges Layout ausgewählt, Layoutbereiche verschoben oder neue Layouts hinzugefügt werden. Löscht oder verändert man Layouts, werden existierende Blöcke in die vorhandenen Spalten geschoben. Aktuell sind folgende Layoutvorlagen verfügbar:
![Neun Layoutvorlagen mit einer bis drei Spalten, Zeilen und gemischten Aufteilungen](assets/layoutblock-template.jpg){ class="shadow lightbox" }
* **Blockmenü**: Menü eines einzelnen Inhaltselements innerhalb eines Layouts. Über das Blockmenü kann ein Inhaltselement verschoben, hinzugefügt oder gelöscht werden. Auch der Inspektor mit weiteren Einstellungen für ein Inhaltselement kann über das Zahnrad :o_icon_o_icon_inspect: aktiviert werden.
* **Inspektor**: Dient der Konfiguration einzelner Inhaltselemente. Dort befinden sich alle Einstellungen, die den Funktionsumfang sowie das Aussehen des jeweiligen Elements verändern, z.B. die Ausrichtung von Bildern. Klickt man auf die Titelzeile des Inspektor-Fensters, kann das Konfigurationsmenü selbst auch verschoben werden. Wenn Sie einen neuen Block selektieren, springt der Inspektor wieder an die Standardposition.

**Hinweis-Box im Inspektor**

Interessant ist auch die Möglichkeit, den Inhaltselementen eine Hinweis-Box hinzuzufügen. Diese Option steht für fast alle Inhaltselemente bis auf Titel und HTML-Textcode zur Verfügung.

![Inspektor eines Textelements mit eingeschalteter Hinweis-Box, Typ Wichtig, eigenem Titel und den Optionen Mit Icon und Einklappbar; links der Text als hervorgehobene Box mit Icon und Titel](assets/Hinweis-Box.png){ class="shadow lightbox" }

Hierüber können einzelne Inhaltselemente hervorgehoben und z.B. als Info, Tipp, Wichtig usw. gekennzeichnet werden. Auch die Vergabe eines eigenen Titels ist möglich. Darüber hinaus können die Hinweis-Boxen noch mit einem Icon versehen und definiert werden, ob die Hinweis-Box einklappbar ist oder nicht. Bei benutzerdefinierten Hinweis-Typen kann auch ein Icon aus der Liste gewählt und die Farbe angepasst werden. Bei vordefinierten Typen sind diese Dinge vordefiniert.

## Inhaltsblöcke - Inhalt hinzufügen

Über "Inhalt hinzufügen" werden die konkreten Inhaltselemente wie Texte, Bilder oder sonstige Medien hinzugefügt. Folgende Inhaltselemente stehen zur Wahl:

![Dialog Inhalt hinzufügen mit den Inhaltselementen in den Gruppen Text, Medien sowie Andere und Design und dem Button Media Center](assets/Inhalt_hinzufuegen_portfolio_19.png){ class="shadow lightbox" }

### Titel

Nutzen Sie dieses Element, um schnell und einfach eine Überschrift hinzuzufügen.

Im Inspektor kann eine Grösse von h1 bis h6 eingestellt werden, wobei h1 der "Überschrift 1" entspricht und somit am grössten und h6 der "Überschrift 6" und somit am kleinsten ist. Im Tab "Layout" kann ferner, wie bei den meisten Inhaltselementen, der Abstand zum Text definiert werden.

![Titelelement mit geöffnetem Inspektor, Tab Style, Auswahlliste Grösse mit dem Wert h3](assets/Titel_Portfolio.png){ class="shadow lightbox" }

### Text

Nutzen Sie dieses Element, um beliebige Textpassagen einzufügen. Der Text kann mit Hilfe des Editors passend formatiert werden, z.B. für Fettdruck, Verlinkungen, Schriftfarbe usw.

### Tabelle

Verwenden Sie dieses Inhaltselement, wenn Sie Ihrem Portfolio eine Tabelle hinzufügen möchten. Definieren Sie die Anzahl der Zeilen und Spalten einer Tabelle und fügen Sie eine Kopfzeile hinzu. Anschliessend befüllen Sie die jeweiligen Tabellenfelder. Im Inspektor legen Sie zudem Kopfspalte und Kopfzeile, die Optionen "Gestreift" und "Umrandet" sowie die Farbe fest; eine Tabellenunterschrift ist optional.

![Tabellenelement mit Titel, Kopfspalte und Beschriftungsfeld; im Inspektor die Felder Zeile und Spalte, die Optionen Kopfspalte, Kopfzeile, Striped und Bordered sowie die Farbwahl](assets/Editor_Tabelle_Portfolio.png){ class="shadow lightbox" }

### Mathematische Formel

Klicken Sie in das Bearbeitungsfeld und Sie erhalten Zugriff auf einen speziellen Formel-Editor. Sie können entweder die Formel im grafischen Editor oder im LaTeX Editor eingeben.

![Formelelement mit der Formel 7 hoch 2 und dem grafischen Formel-Editor mit Tastenfeld für Zahlen, Funktionen, Symbole und griechische Buchstaben](assets/Mathe_Formeln_Portfolio.png){ class="shadow lightbox" }

### Code-Beispiel

Element zum Einfügen von Programmiercode. Der Inhalt wird als Code angezeigt und nicht ausgeführt. Diverse Code-Sprachen stehen zur Auswahl. Auch Zeilennummern können für die Übersicht eingeblendet werden.

![Code-Beispiel mit HTML-Quelltext und Zeilennummern; im Inspektor die Sprache des Codes HTML, XML, der Schalter Zeilennummern und die Anzahl der anzuzeigenden Zeilen](assets/Code-Beispiel_Editor_19.png){ class="shadow lightbox" }

### Zitat

Hier können Sie neue Zitate erstellen (Zitat hinzufügen) oder auf bereits im Media Center hinterlegte Zitate zurückgreifen und diese einbinden. Einem neuen Zitat können diverse Informationen hinzugefügt werden, z.B. Quelle, Sprache, Autor, URL.

### Bild

Fügen Sie Bildelemente hinzu, indem Sie eine Grafikdatei hochladen oder auf eine Grafik Ihres Media Centers zugreifen. Anschliessend können Sie die Datei weiter konfigurieren, z.B. einen Titel oder Untertitel platzieren und auch die Grösse, Platzierung oder Umrandung definieren. Nutzen Sie hierfür den Inspektor.

!!! tip "Tipp"

    Um die Positionierung einer Grafik zu optimieren, verwenden Sie am besten ein passendes, z.B. mehrspaltiges Layout. Je nach Art der Grafiken gilt dieser Tipp auch für das Inhaltselement "Galerie".

### Galerie [:octicons-tag-16:{ title="ab Release 19.0.0 (OO-7142)" }](https://track.frentix.com/issue/OO-7142){:target="_blank"}

Mit dem Inhaltselement "Galerie" fügen Sie eine Bildergalerie hinzu. Mit einem Klick auf den Button "Hinzufügen" öffnet sich das Media Center, in dem mehrere Bilder ausgewählt werden können. Die Anzeigeart (Vorschau, Raster oder Slideshow) lässt sich im Inspektor festlegen. Das gezeigte Beispiel präsentiert eine Galerie mit Vorschau aus der Perspektive der Lesenden.

![Galerieelement in der Anzeigeart Vorschau: grosses Bild mit Titel, Pfeilen zum Blättern und drei Vorschaubildern darunter](assets/Editor_Galerie_Portfolio.png){ class="shadow lightbox" }

### Bildvergleich [:octicons-tag-16:{ title="ab Release 19.0.0 (OO-7143)" }](https://track.frentix.com/issue/OO-7143){:target="_blank"}

Mit dem Inhaltselement "Bildvergleich" stellen Sie 2 Bilder aus dem Media Center nebeneinander, z.B. zwei Versionen desselben Bildes. Die Auswahl der Bilder erfolgt über den Inspektor. Neben dem Standardtyp kann der Bildvergleich auch für die Gegenüberstellung von einem richtigen und einem falschen Bild verwendet werden.

![Bildvergleich mit zwei Bildern nebeneinander, Schieberegler in der Mitte und den Beschriftungen Icon Vorschlag 1 und Icon Vorschlag 2; links der Inspektor mit den Einstellungen für Bild 2](assets/Editor_Bildervergleich_Portfolio.png){ class="shadow lightbox" }

Lesende können mit einem Schieberegler den Ansichtsbereich der Bilder justieren.

### Video

Sie haben folgende Möglichkeiten, ein Video in den Editor zu laden und bereitzustellen:

* Video hinzufügen: Eine mp4 Videodatei hochladen
* Video per URL hinzufügen
* Video aufnehmen: Eine Videoaufnahme mit der Webcam erstellen
* Eine Videodatei, die sich im Media Center befindet, auswählen und hinzufügen.

![Dialog Video auswählen im Media Center mit dem Button Video hinzufügen und dem geöffneten Menü Video per URL hinzufügen und Video aufzeichnen, darunter die Tabs, Filter und vorhandenen Videos](assets/Video_Portfolio_Editor19.png){ class="shadow lightbox" }

### Audio

Sie haben folgende Möglichkeiten, ein Audio in den Editor zu laden und bereitzustellen:

* Nutzen Sie den integrierten Audio-Editor und erstellen Sie eine Tonaufnahme (Audio aufzeichnen)
* Laden Sie eine Audiodatei hoch (Audio hinzufügen)
* Verbinden Sie eine Audiodatei aus Ihrem Media Center (Auswahl aus der Liste).

![Dialog Audio auswählen mit den Buttons Audio aufzeichnen und Audio hinzufügen, den Tabs von Alle bis Suche, den Filtern und einer vorhandenen Testaufnahme](assets/Audio_Portfolio_19.jpg){ class="shadow lightbox" }

### Dokument

Sie haben folgende Möglichkeiten, ein Dokument in den Editor zu laden und bereitzustellen:

* Erstellen Sie ein neues Dokument, entsprechend der angegebenen Dateitypen (Dokument erstellen)
* Laden Sie ein neues Dokument hoch (Dokument hinzufügen) oder
* Verbinden Sie ein Dokument aus Ihrem Media Center (Auswahl aus der Liste).

Ist ein externer Dokumenteneditor aktiviert und liegen die Dateien in einem Format vor, das von diesem unterstützt wird, können die Dateien auch direkt online in OpenOlat weiterbearbeitet werden.

!!! info "Wichtig"

    Die Inhalte der Dateien werden hier nicht direkt dargestellt, sondern müssen per Klick auf den Link geöffnet werden.

### Diagramm

Sie können ein neues draw.io Diagramm anlegen oder Sie fügen ein existierendes draw.io Diagramm aus Ihrem Media Center hinzu. Die konkrete Ausgestaltung des Diagramms erfolgt über den Klick auf den "Bearbeiten" Link im Eintrag.

![Diagrammelement mit einem draw.io Diagramm und dem Link Bearbeiten; rechts der Inspektor im Tab Titel mit den Feldern Titel, Wo mit dem Wert Über Bild und Titelstil](assets/Editor_Diagramm_Portfolio.png){ class="shadow lightbox" }

Beim Erstellen eines Diagramms kann auch definiert werden, ob bzw. wer das Diagramm bearbeiten darf.

### Separator

Hinzufügen einer Trennlinie.

### HTML-Textcode

Hier erscheint ein ähnlicher, aber etwas erweiterter Text-Editor wie beim Inhaltselement "Text".

### Media Center

Anstatt ein spezielles Inhaltselement zu wählen, können Sie auch direkt in Ihr [Media Center](../personal_menu/Media_Center.de.md) wechseln und dort hinterlegte Elemente auswählen oder Mediendateien hochladen bzw. hinzufügen.

Die Such- und Filteroptionen helfen, die gewünschte(n) Datei(en) schnell zu finden.

![Dialog Mein Medien Center mit dem Button Mediendatei hinzufügen und dem Menü für Dokument, draw.io Diagramm, Text, Video per URL, Video- und Audioaufnahme und Zitat, darunter die Medienliste](assets/Medien_Center_Portfolio.png){ class="shadow lightbox" }

## Weiterführende Informationen {: #further_information}

[Persönliche Werkzeuge: Das Media Center >](../personal_menu/Media_Center.de.md)

[Zum Seitenanfang ^](#portfolio_editor)
