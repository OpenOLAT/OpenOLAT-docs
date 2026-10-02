# Wie kann ich eigenes CSS für das Kursdesign erstellen? {: #custom_css}

??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie sollen wissen, dass in OpenOlat selbst erstellte CSS-Dateien für das Kursdesign verwendet werden können. Es würde jedoch zu weit führen, hier im Handbuch Details zur CSS-Erstellung zu erklären. Bitte informieren Sie sich dazu anderweitig, zum Beispiel im [CSS-Tutorial von W3Schools](http://www.w3schools.com/css/default.asp).

??? abstract "Zielgruppe"

    [ ] Autor:innen [ ] Betreuer:innen  [ ] Teilnehmer:innen  [x] Administrator:innen

    [ ] Anfänger:innen [ ] Fortgeschrittene  [x] Expert:innen


??? abstract "Erwartete Vorkenntnisse"

    * Erfahrung als Administrator:in
    * Erfahrung mit HTML und CSS-Programmierung


!!! warning "Nur für Expert:innen!"

    Für normale Setups und ohne vertiefte CSS-Kenntnisse ist die Verwendung eines eigenen Kurs-Designs nicht empfohlen!

    Beachten Sie, dass das Ändern des OpenOlat-Layouts durch Manipulation des System-CSS nicht versionsübergreifend unterstützt wird. Das bedeutet, dass das Erstellen eines Kurslayouts nach einem Systemupdate zu einem defekten Kursdesign führen kann.

    Verwenden Sie eigene CSS nur

    * mit Vorsicht,
    * nur, wenn es absolut notwendig ist
    * und wenn Sie die Kontrolle über den Aktualisierungszyklus Ihrer OpenOlat-Installation haben.

!!! tip "Tipp"

    Bitten Sie Ihren Systemanbieter, Layoutvorlagen auf Systemebene einzurichten. Sie erscheinen in der Auswahl als "Systemvorlage", werden nach jeder OpenOlat-Aktualisierung neu kompiliert und funktionieren somit garantiert auch nach Aktualisierungen.

## Welche Voraussetzungen muss ich mitbringen? {: #requirements}

  * Vertiefte CSS-Kenntnisse
  * Erfahrungen mit Browser-Entwicklerwerkzeugen
  * evtl. HTML Grundkenntnisse

## Welche Werkzeuge benötige ich, um das OpenOlat Design zu ändern? {: #customize}

Sie benötigen:

* einen **Editor** (z.B. [Notepad++](https://notepad-plus-plus.org/)) um die CSS Datei zu erstellen
* und ein Werkzeug um das CSS von OpenOlat zu analysieren, bzw. die entsprechenden Selektoren, die verändert werden sollen, zu identifizieren.

Möglich ist dies z.B. über die **Browser Option "Element untersuchen"**. In Firefox und Chrome ist dieses Werkzeug bereits integriert.
Klicken Sie mit der rechten Maustaste in die Webseite und wählen Sie dann "Element untersuchen (Q)" bzw. "Untersuchen (Strg+Shift+I)". Wenn Sie z.B. auf die obere Navigationsleiste klicken, zeigt Ihnen die Information den Namen des Selektors an, in diesem Fall "#o_navbar_container".

## Was ist möglich? {: #possibilities}

Sie möchten das Kursdesign individuell gestalten und Ihren Kurs optisch aufwerten oder an Ihr Corporate Design der Organisation anpassen?

Das Standard OpenOlat Layout lässt sich mit Hilfe von CSS beliebig anpassen und verändern. So ist es möglich, einem Kurs einen individuellen Wiedererkennungswert zu geben. Auch ein Bezug zum Kursinhalt, eine bestimmte Farbharmonie oder die optische Gestaltung für gamebasierte Kurse kann auf diesem Weg umgesetzt werden.

!!! warning "Aber Vorsicht!!"

    Einige generelle Selektoren (z.B. h2, p) werden in OpenOlat mehrfach verwendet und so können Änderungen sehr weitreichend, jedoch nicht immer in der ganzen Tragweite ersichtlich sein. Wird z.B. die Schriftfarbe in Blau geändert, kann es sein, dass die Schrift auf blauen Buttons nicht mehr lesbar ist (z.B. in einem Test). Überdenken Sie also vorab ihre Handlung und halten Sie sich immer an die Grundlagen des Webdesigns, wie beispielsweise ausreichenden Kontrast zwischen Schriftfarbe und Hintergrund.

## Wo wird die CSS-Datei gespeichert und eingebunden? {: #storing}

Um Ihre CSS-Datei für die Gestaltung Ihres OpenOlat Kurses nutzen zu können, müssen Sie im **[Ablageordner](../../manual_user/learningresources/Storage_folder.de.md)** des Kurses einen **Unterordner "courseCSS"** anlegen und dort die erstellte Kurs-CSS-Datei ablegen.

Damit die Datei auch verwendet wird, wählen Kursbesitzer:innen sie in den [Kurseinstellungen](../../manual_user/learningresources/Course_Settings.de.md#layout) unter `Kurs > Administration > Einstellungen > Tab "Layout"` im Feld "Layoutvorlage für Kurs wählen" aus. Die Datei erscheint dort als "Aus Kursablageordner" mit ihrem Dateinamen. Wenn Sie später doch wieder zu dem Standard OpenOlat Layout zurückkehren möchten, wählen Sie die Option "Standard" aus, oder löschen einfach ihre CSS aus dem Ablageordner.

## Beispiele für individuelle Gestaltung {: #design}

Die Änderungsmöglichkeiten sind vielfältig.

!!! warning "Achtung"

    Das Ändern von OpenOlat-CSS-Klassen kann zu unerwartetem Verhalten beim Aktualisieren des System führen. Die unten aufgeführten Klassennamen und Element-IDs sind nicht garantiert verfügbar und können sich mit OpenOlat-Updates ändern. Auch die zugrunde liegende DOM-Struktur von OpenOlat kann sich ändern. Es wird daher nicht empfohlen, CSS-Regeln zu erstellen, die die Stile im OpenOlat-DOM oder CSS-Namensraum ändern.

## Beispiel: Hintergrund ändern {: #background}

Um den Hintergrund mit CSS zu ändern, muss man erst den ID-Selektor `#o_body` benutzen und die Eigenschaft `background`, `background-color` oder `background-image` deklarieren. Sie können also sowohl das Hintergrundbild als auch die Hintergrundfarbe auf diesem Weg definieren. Das gewünschte Hintergrundbild können Sie einfach im Ablageordner des Kurses hinterlegen und passend verlinken.

Der Code für die genannten Selektoren kann dann folgendermassen aussehen:

```css
#o_body {
	background-color: red; /*erzeugt einen roten Hintergrund */
	background-image: url(bild.svg); /* verlinkt zu einem Bild, das als
	Hintergrund verwendet wird*/
	background-position: center; /* setzt das Bild mittig */
}
```

Meist macht es Sinn entweder eine Hintergrundfarbe oder ein Hintergrundbild zu verlinken. Hinterlegen Sie das Bild an einer geeigneten Stelle im Ablageordner des Kurses.

Es wird weiterhin empfohlen, folgende CSS-Einstellungen zu übernehmen, um andere Abschnitte transparent zu machen, um den gefärbten Hintergrund zu sehen:

```css
#o_main_wrapper, #o_main_wrapper #o_main_container {
	background: transparent;
}

#o_main_wrapper #o_main_container #o_main_left {
	background:transparent; margin-right: 15px;
}

#o_main_wrapper #o_main_container #o_main_center {
	background:transparent;
}

#o_footer_wrapper, #o_footer_container {
	background: transparent;
}
```

## Beispiel: Kursbaustein HTML-Seite  {: #single_page}

Oft kann es nötig sein den Hintergrund einer einzelnen HTML-Seite dem Gesamtdesign anzupassen. Auch in diesem Fall wird das Gewünschte mit CSS-Code realisiert.

Um die HTML-Seite beispielsweise transparent zu machen (damit der Hintergrund der Seite durchscheint) wird in der HTML-Seite des [Kursbausteins "HTML-Seite"](../../manual_user/learningresources/Course_Element_HTML_Page.de.md) der body transparent gemacht:

```css
body {
	background-color: transparent;
}
```

## Beispiel: Klassen- und ID-Selektoren {: #example}

Im Folgenden sind einige Bereiche eines OpenOlat Kurses mit den entsprechenden
Klassen und/oder ID-Selektoren aufgeführt, die häufig angepasst werden. Die Nummern entsprechen den Nummern im Bild.

![Fünf nummerierte Bereiche eines Kurses: obere Menüleiste, Kursmenüleiste, linke Menüleiste, Fusszeile und Benutzermenü rechts](assets/css_struktur_v1_de.png){ class="shadow lightbox" title="Kursansicht mit geöffnetem Benutzermenü" }

| Nr. im Bild | Bereich | CSS-Selektor |
|---|---|---|
| 1 | Obere Menüleiste | ID-Selektor `#o_navbar_container` |
| 2 | Kursmenüleiste | Klassen-Selektoren `.o_toolbar .o_tools_container` |
| 3 | Linke Menüleiste | ID-Selektor `#o_main_left_content` |
| 4 | Fusszeile | ID-Selektoren `#o_footer_container` und `#o_footer_wrapper` |
| 5 | Benutzermenü (rechtes Ausklappmenü) | ID-Selektor `#o_offcanvas_right` |

**Logo austauschen**

Mit `.o_navbar-brand` kann das Logo in der oberen Menüleiste (Nr. 1) ausgetauscht oder
angepasst werden:

  * `display: none;` blendet das Logo aus `.o_navbar-brand {display: none;}`
  * `background: rgba(0, 0, 0, 0) url("logo-k-town.png");` ersetzt das bestehende Logo durch die Grafik logo-k-town.png

Sollen die Überschriften angepasst werden, wählen Sie das Element **h2**. Auch hier können alle Eigenschaften mit CSS-Befehlen den eigenen Ansprüchen entsprechend angepasst werden. Dasselbe gilt auch für das Element **p** oder auch für die Links **a**. Vorstellbar wären für diese Elemente beispielsweise folgende CSS-Eigenschaften:

  *  `color: red;` Änderung der Schriftfarbe. Hier kann der Hex Code `#ffffff` (=weiss) oder auch ein RGB Wert `rgb(87 , 53, 4)` angegeben werden.
  *  `font-family: verdana;` so lässt sich die Schriftart anpassen
  *  `font-weight: bold;` definiert die Schriftstärke (`bold` = fett)
  *  `text-transform: uppercase;` beschreibt das Verhalten der Schrift (`uppercase` = nur Grossbuchstaben)
  *  `text-decoration: underline;` der Text wird unterstrichen dargestellt

## Weiterführende Informationen {: #further_information}

[W3Schools: CSS Tutorial >](http://www.w3schools.com/css/default.asp)<br>
[Notepad++ >](https://notepad-plus-plus.org/)<br>
[Ablageordner >](../../manual_user/learningresources/Storage_folder.de.md)<br>
[Kurseinstellungen >](../../manual_user/learningresources/Course_Settings.de.md)<br>
[Kursbaustein "HTML-Seite" >](../../manual_user/learningresources/Course_Element_HTML_Page.de.md)<br>
[Customizing: Übersicht >](../../manual_admin/administration/Customizing.de.md)

[Zum Seitenanfang ^](#custom_css)
