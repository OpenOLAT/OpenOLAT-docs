# Formular-Elemente {: #form_elements} 

Ein Formular bauen Sie im [Formulareditor](../Form_Editor/index.de.md) aus Elementen auf. Über "Inhalt hinzufügen" fügen Sie einem Layout die folgenden Elemente hinzu:

![Inhaltselemente des Formulareditors, gruppiert nach Text, Fragetypen, Organisatorisch, Medien sowie Andere und Design](../assets/form_content_types_v1_de.png){ class="shadow lightbox" title="Popup Inhalt hinzufügen in einem Formular" }

Die Elemente der Gruppe "Fragetypen" stellen Sie auf "Obligatorisch" oder "Freiwillig". Ein obligatorisches Element füllen die Teilnehmenden aus, bevor sie das Formular abschliessen. Ein freiwilliges Element darf leer bleiben.

Viele Elemente stellen Sie im Tab "Stil" in eine [Hinweis-Box](#form_element_alert_box). Im Tab "Layout" legen Sie den Abstand zu den übrigen Elementen fest.

---

## Titel {: #form_element_title} 

Mit dem Element "Titel" gliedern Sie das Formular mit Überschriften. Die Grösse wählen Sie in den Stufen h1 bis h6.

![Inspektor des Titel-Elements mit dem Tab "Style" und der Auswahl der Schriftgrösse](../assets/form_content_title_v1_de.png){ class="shadow lightbox" title="Element Titel mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Text {: #form_element_text} 

Mit dem Element "Text" fügen Sie dem Formular Informationen oder Fragestellungen hinzu. Ein kleiner Editor formatiert den Text und fügt Links und Aufzählungen ein.

![Text-Element mit Editor-Symbolleiste im Formular sowie dem Inspektor mit Spaltenzahl und Hinweis-Box](../assets/form_content_text_v1_de.png){ class="shadow lightbox" title="Element Text mit Inspektor" }


[Zum Seitenanfang ^](#form_elements)

---


## Tabelle [:octicons-tag-16:{ title="ab Release 13.2 (OO-3856)" }](https://track.frentix.com/issue/OO-3856) {: #form_element_tabelle} 

Mit dem Element "Tabelle" stellen Sie Angaben übersichtlich in Zeilen und Spalten dar. Im Inspektor legen Sie unter anderem Zeilen, Spalten, Kopfzeile und Kopfspalte fest.

![Tabellen-Element im Formular mit dem Inspektor zur Konfiguration von Zeilen, Spalten, Kopfspalte, Kopfzeile und Rahmenstil](../assets/form_content_table_v1_de.png){ class="shadow lightbox" title="Element Tabelle mit Inspektor" }


[Zum Seitenanfang ^](#form_elements)

---

## Rubrik {: #form_element_rubric}

Mit einer Rubrik bewerten Personen mehrere Kriterien oder Aussagen auf derselben Skala. Die Zeilen tragen die Kriterien oder Aussagen, die Spalten die Stufen der Bewertungsskala. In Kursen dient die Rubrik zum Beispiel Betreuer:innen als Bewertungsraster oder Teilnehmenden für [Peer-Reviews](../Course_Element_Task/index.de.md) im Kursbaustein "Aufgabe".

Wie Sie eine Rubrik konfigurieren, beschreibt die Seite [Das Formular-Element Rubrik](../Form_Element_Rubric.de.md).

![Rubrik-Element mit Statements in den Zeilen und einer fünfstufigen Bewertungsskala in den Spalten](../assets/Rubrik.jpg){ class="shadow lightbox" title="Element Rubrik mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Einzelauswahl [:octicons-tag-16:{ title="ab Release 13.0 (OO-3678)" }](https://track.frentix.com/issue/OO-3678) {: #form_element_sc}

In einer Einzelauswahl (Single Choice) wählen die Teilnehmenden genau eine Option aus einer Liste.

* Mit dem Button "Eintrag hinzufügen" ergänzen Sie weitere Optionen.
* Mit den Pfeilen verschieben Sie einen Eintrag nach oben oder unten.
* Unter "Darstellung" wählen Sie, ob die Optionen "Untereinander", "Nebeneinander" oder als "Auswahlliste" erscheinen.

!!! tip "Tipp"

    Die Fragestellung zur Auswahl schreiben Sie in ein eigenes Element "Text". Gleiches gilt für die Mehrfachauswahl.

Die Einzelauswahl kann die Bedingung einer [Frageregel](../Form_Question_Rules.de.md) sein. Je nach gewählter Antwort zeigt das Formular dann bestimmte Container mit ihren Inhalten an.

Geben Sie dem Element im Inspektor unter "Name" einen sprechenden Namen, damit Sie es in den Frageregeln wiederfinden.

![Einzelauswahl-Element mit Antwortliste im Formular sowie dem Inspektor für Name, Darstellung und Pflichtangabe](../assets/form_content_sc_v1_de.png){ class="shadow lightbox" title="Element Einzelauswahl mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Mehrfachauswahl [:octicons-tag-16:{ title="ab Release 13.0 (OO-3679)" }](https://track.frentix.com/issue/OO-3679) {: #form_element_mc}

In einer Mehrfachauswahl (Multiple Choice) wählen die Teilnehmenden eine oder mehrere Optionen aus einer Liste.

* Mit dem Button "Eintrag hinzufügen" ergänzen Sie weitere Optionen.
* Mit den Pfeilen verschieben Sie einen Eintrag nach oben oder unten.
* Unter "Darstellung" wählen Sie, ob die Optionen "Untereinander", "Nebeneinander" oder als "Auswahlliste" erscheinen.
* Mit der Option "Teilnehmer:in kann weitere Werte erfassen" ergänzen die Teilnehmenden eigene Antworten.

Die Mehrfachauswahl kann die Bedingung einer [Frageregel](../Form_Question_Rules.de.md) sein. Je nach gewählter Antwort zeigt das Formular dann bestimmte Container mit ihren Inhalten an.

Geben Sie dem Element im Inspektor unter "Name" einen sprechenden Namen, damit Sie es in den Frageregeln wiederfinden.

![Mehrfachauswahl-Element mit Antwortliste im Formular sowie dem Inspektor für Name, Darstellung und die Option "weitere Werte erfassen"](../assets/form_content_mc_v1_de.png){ class="shadow lightbox" title="Element Mehrfachauswahl mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Textblock {: #form_element_text_input}

Im Element "Textblock" tragen die Teilnehmenden eigenen Text in ein Freitextfeld ein.

* Unter "Erlaubte Werte" legen Sie fest, ob "Text", eine "Zahl", ein "Datum" oder "Datum / Zeit" eingegeben wird.
* Unter "Zeilentyp" wählen Sie "Eine Zeile" oder "Mehrere Zeilen".

![Texteingabe-Element im Formular mit dem Inspektor für erlaubte Werte, Zeilentyp und Anzahl Zeilen](../assets/form_content_text_input_v1_de.png){ class="shadow lightbox" title="Element Texteingabe mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Datei hochladen [:octicons-tag-16:{ title="ab Release 12.4 (OO-3181)" }](https://track.frentix.com/issue/OO-3181) {: #form_element_file_upload}

Mit dem Element "Datei hochladen" laden die Teilnehmenden eine Datei in das Formular hoch.

* Unter "Maximale Dateigrösse" begrenzen Sie die Grösse der Datei.
* Unter "Dateityp" erlauben Sie nur bestimmte Dateitypen, zum Beispiel "PDF" oder "Bilder".

![Datei-hochladen-Element im Formular mit dem Inspektor für maximale Dateigrösse und erlaubten Dateityp](../assets/form_content_file_upload_v1_de.png){ class="shadow lightbox" title="Element Datei hochladen mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Angaben zur befragten Person {: #form_element_info}

Mit dem Element "Angaben zur befragten Person" fragen Sie Angaben zur Person ab, die das Formular ausfüllt, zum Beispiel Vorname, Nachname oder E-Mail. Unter "Informationen" kreuzen Sie die gewünschten Angaben an. Ein Formular enthält das Element höchstens einmal.

Unter "Pflicht" wählen Sie eine von drei Varianten:

* **Optional - kann leer gelassen werden**: Die Teilnehmenden füllen die Angaben freiwillig aus.
* **Obligatorisch - bearbeitbar**: Die Teilnehmenden füllen die Angaben zwingend aus.
* **Obligatorisch - nicht bearbeitbar**: OpenOlat trägt die Angaben aus dem Benutzerprofil ein, die Teilnehmenden können sie nicht ändern.

!!! info "Wichtig"

    Mit diesem Element ordnet das Formular die Antworten der befragten Person zu. Das Formular ist damit nicht mehr anonym.

![Informationen-Element im Formular mit den ankreuzbaren Angaben wie Vorname und E-Mail sowie der Auswahl "Obligatorisch, automatisch ausgefüllt und nicht bearbeitbar"](../assets/form_content_info_v1_de.png){ class="shadow lightbox" title="Element Informationen mit Inspektor" }

[Zum Seitenanfang ^](#form_elements)

---

## Nutzungsbedingungen [:octicons-tag-16:{ title="ab Release 13.0 (OO-3674)" }](https://track.frentix.com/issue/OO-3674) {: #form_element_terms_of_use}

Mit dem Element "Nutzungsbedingungen" fügen Sie dem Formular eine Einverständniserklärung mit Checkbox hinzu. Die Teilnehmenden haken sie an, bevor sie das Formular abschliessen. Zwischenspeichern können sie das Formular auch vorher.

![Nutzungsbedingungen-Element im Formular mit Einverständniserklärung und Beschriftung der Checkbox](../assets/form_content_terms_of_use_v1_de.png){ class="shadow lightbox" title="Element Nutzungsbedingungen in einem Formular" }

[Zum Seitenanfang ^](#form_elements)

---

## Bild [:octicons-tag-16:{ title="ab Release 13.2 (OO-3857)" }](https://track.frentix.com/issue/OO-3857) {: #form_element_picture}

Mit dem Element "Bild" zeigen Sie im Formular ein Bild. Wählen Sie unter "Inhalt hinzufügen" das Element "Bild", fordert OpenOlat Sie zuerst auf, eine Bilddatei hochzuladen. Danach zeigt der Formulareditor das Bild mit dem Inspektor.

![Bild-Element im Formular mit hochgeladenem Bild sowie dem Inspektor für Ausrichtung, Bildgrösse und Stil im Tab "Stil"](../assets/form_content_picture_v1_de.png){ class="shadow lightbox" title="Element Bild mit Inspektor" }


Im Inspektor legen Sie fest, wie das Bild erscheint:

**Tab "Stil"**

* **Ausrichtung**: Lage des Bildes im Layoutbereich
* **Bildgrösse**: Skalierung des Bildes
* **Stil**: Darstellung, zum Beispiel mit Rahmen oder Schatten
* **Hinweis-Box**: Darstellung in einer [Hinweis-Box](#form_element_alert_box)

**Tab "Titel"**

* **Titel**: Titel zum Bild
* **Wo**: Position des Titels, zum Beispiel über dem Bild oder auf dem Bild in der Mitte
* **Titelstil**: "Hell" für dunkle Bilder, "Dunkel" für helle Bilder

**Tab "Anzeige"**

* **Beschreibung**: Text zum Bild, den die Teilnehmenden über ein kleines Fragezeichensymbol öffnen
* **Bildunterschrift**: Text in kleinerer Schrift unter dem Bild

**Tab "Layout"**

* **Abstand**: Abstand des Bildes zu den übrigen Elementen


[Zum Seitenanfang ^](#form_elements)

---

## Separator

Der Separator ist eine feine Trennlinie zum Gliedern Ihres Formulars in Bereiche.


![Separator als Trennlinie zwischen zwei Text-Elementen im Formular](../assets/form_content_separator_v1_de.png){ class="shadow lightbox" title="Element Separator in einem Formular" }

[Zum Seitenanfang ^](#form_elements)


## Hinweis-Box [:octicons-tag-16:{ title="ab Release 18.2.3 (OO-7138)" }](https://track.frentix.com/issue/OO-7138) {: #form_element_alert_box}

Mit der Hinweis-Box heben Sie ein Element hervor, zum Beispiel einen wichtigen Text oder eine Rubrik. Die Hinweis-Box ist kein eigenes Element, sondern eine Einstellung im Tab "Stil" vieler Elemente wie Text, Tabelle, Bild, Rubrik und Nutzungsbedingungen.

![Hinweis-Box um ein Text-Element aktiviert, mit dem Inspektor für Typ, Titel, Icon und Farbe der Box](../assets/form_content_text_box_v1_de.png){ class="shadow lightbox" title="Hinweis-Box mit Inspektor" }

Ist der Schalter "Hinweis-Box" eingeschaltet, legen Sie die folgenden Einstellungen fest.

#### Typ {: #alert_box_type}

Der Typ bestimmt, welche vorformatierte Box erscheint oder ob Sie die Box selbst gestalten. Zur Auswahl stehen:

* Notiz
* Information
* Tipp
* Wichtig
* Warnung
* Fehler
* Erfolg
* Benutzerdefiniert: Sie wählen selbst ein Icon und die Hintergrundfarbe der Box.

#### Titel {: #alert_box_title}

Der Titel erscheint in der Kopfzeile der Hinweis-Box.

#### Mit Icon {: #alert_box_icon}

Ist die Option eingeschaltet, zeigt die Hinweis-Box oben links ein Icon, zum Beispiel ein "i" beim Typ "Information".

#### Einklappbar {: #alert_box_collapsible}

Ist die Option eingeschaltet, klappen die Teilnehmenden die Box mit dem Symbol oben rechts ein. Dann ist nur noch die Titelzeile sichtbar. Ein weiterer Klick auf das Symbol öffnet die Box wieder.


---

## Weiterführende Informationen {: #further_information}

[Wie erstelle ich eine Formular-Lernressource?](../../../manual_how-to/create_a_form/create_a_form.de.md)<br>
[Der Formulareditor](../Form_Editor/index.de.md)<br>
[Das Formular-Element Rubrik](../Form_Element_Rubric.de.md)<br>
[Frageregeln in Formularen](../Form_Question_Rules.de.md)

[Zum Seitenanfang ^](#form_elements)

