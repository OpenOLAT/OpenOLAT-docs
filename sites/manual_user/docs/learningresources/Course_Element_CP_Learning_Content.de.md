# Kursbaustein "CP-Lerninhalt" {: #CP_learning_content}


## Steckbrief

Name | CP-Lerninhalt
---------|----------
Icon | :o_icon_o_cp_icon:
Verfügbar seit | Neuauflage mit Release 16.2
Funktionsgruppe | Wissensvermittlung
Verwendungszweck | Anzeige von Lerninhalt im IMS-CP-Format
Bewertbar | nein
Spezialität / Hinweis |

Nutzen Sie den Kursbaustein "CP-Lerninhalt", um ein Content Package (CP) in Ihren Kurs einzubinden: ein Paket aus Lernseiten mit eigener Struktur im Format IMS Content Packaging (IMS-CP, Version 1.1.2). Das CP erstellen Sie entweder direkt in OpenOlat, wie es die Anleitung "[Wie erstelle ich ein Content Package?](../../manual_how-to/content_package/content_package.de.md)" erklärt, oder mit einem anderen Werkzeug ausserhalb von OpenOlat. Ein extern erstelltes CP laden Sie im Tab "Lerninhalt" als ZIP-Datei hoch, die die Datei "imsmanifest.xml" enthält.

Den Kursbaustein konfigurieren Sie im Kurseditor in den Tabs "Lerninhalt" und "Anzeige Inhalt":<br>
`Kurs > Administration > Kurseditor > Kursbaustein "CP-Lerninhalt"`

## Tab Lerninhalt :octicons-tag-16:{ title="Neuauflage ab Release 16.2" } {: #tab_learning_content}

Im Kurseditor erscheint der Kursbaustein "CP-Lerninhalt" als ein einziger Eintrag, auch wenn das CP aus vielen Seiten besteht. Seinen Inhalt, das Content Package, legen Sie im Tab "Lerninhalt" fest. Ein CP ist in OpenOlat eine eigene Lernressource, die Sie in mehreren Kursen verwenden können. Mit "CP-Lerninhalt wählen, erstellen oder importieren" wählen Sie ein CP aus, das als Lernressource schon besteht, erstellen ein neues oder laden eines aus einer Datei hoch. Ist ein CP eingebunden, öffnet ein Klick auf seinen Namen die Vorschau, und "CP-Lerninhalt auswechseln" ersetzt es durch ein anderes. Mit "Bearbeiten" ändern Sie den Inhalt des CP. Die Änderung gilt für die Lernressource und damit in allen Kursen, die sie einbinden. Den Button sehen Besitzer:innen des CP, Lernressourcenverwalter:innen und Administrator:innen.

![Gewählter CP-Lerninhalt mit den Buttons CP-Lerninhalt auswechseln und Bearbeiten, darunter die eingeschaltete Checkbox CP-Navigation im Kursmenü integrieren](assets/course_element_cp_learning_content_tab_content1_v2_de.png){ class="shadow lightbox" title="Tab Lerninhalt des Kursbausteins im Kurseditor · 2026.11.09" }

Ein Content Package besteht meist aus mehreren Seiten. Ist die Option "CP-Navigation im Kursmenü integrieren" eingeschaltet, zeigt OpenOlat die Struktur dieser Seiten direkt im Kursmenü. Bei einem neuen Kursbaustein ist sie eingeschaltet.<br>
Ohne diese Option sehen Teilnehmer:innen die Struktur nicht. Nach dem Öffnen des Kursbausteins blättern sie mit den Pfeilen rechts oben im Inhalt durch die Seiten des CP.

![CP-Seiten als eigene Einträge im Kursmenü, weil CP-Navigation integriert ist](assets/course_element_cp_learning_content_tab_content2_v1_de.png){ class="shadow lightbox" title="Kursmenü mit integrierter CP-Navigation" }

![Pfeile zum Navigieren durch die CP-Seiten, ohne Struktur im Kursmenü](assets/course_element_cp_learning_content_tab_content3_v1_de.png){ class="shadow lightbox" title="Kursbaustein CP-Lerninhalt ohne CP-Navigation im Kursmenü" }

[Zum Seitenanfang ^](#CP_learning_content)


## Tab Anzeige Inhalt [:octicons-tag-16:{ title="ab Release 9.0.0 (OO-619)" }](https://track.frentix.com/issue/OO-619){:target="_blank"} {: #tab_display_content}

Im Tab "Anzeige Inhalt" legen Sie fest, wie OpenOlat die Seiten des Content Packages im Kurs anzeigt, zum Beispiel ob das Layout des Kurses auf die Seiten angewendet wird und wie hoch die Anzeigefläche ist. So passt der CP-Lerninhalt optisch zum Kurs, oder er erscheint unverändert so, wie er erstellt wurde.

Ist eine [Inhaltsdomäne](../basic_concepts/Content_Domain.de.md) (separate Adresse für Inhalte) eingerichtet, liefert OpenOlat den Inhalt darüber aus. Skripte im Inhalt erhalten so keinen Zugriff auf die OpenOlat-Sitzung. [:octicons-tag-16:{ title="ab Release 21.0 (OO-7612)" }](https://track.frentix.com/issue/OO-7612){:target="_blank"}

#### Standardwerte übernehmen {: #use_standard_configuration}

Die Anzeige eines CP-Lerninhalts legen Sie an zwei Orten fest: in den Einstellungen der Lernressource im [Tab "Layout"](CP_Administration/index.de.md#tab_layout) und hier im Kursbaustein. Mit "Standardwerte übernehmen" wählen Sie, welche Einstellungen im Kurs gelten:

* **Aus Layouteinstellungen der Lernressource übernehmen:** Der Kursbaustein zeigt den CP-Lerninhalt so, wie es in den Einstellungen der Lernressource festgelegt ist. Die Felder darunter zeigen diese Werte und lassen sich hier nicht ändern.
* **Anpassen:** Sie legen die Felder darunter für diesen Kursbaustein selbst fest. Die Einstellungen gelten nur hier, die Lernressource und andere Kurse, die sie verwenden, bleiben unverändert.

Sieht ein CP-Lerninhalt im Kurs anders aus als beim direkten Öffnen der Lernressource, prüfen Sie diese Auswahl: Mit "Anpassen" gelten im Kurs eigene Werte. Das Feld "Standardwerte übernehmen" erscheint, sobald der Kursbaustein einen CP-Lerninhalt eingebunden hat.

#### Weitere Felder {: #display_fields}

Darunter folgen dieselben Felder wie im Tab "Anzeige Inhalt" des Kursbausteins "HTML-Seite": "Anzeigemodus", "JavaScript hinzufügen", "Glossarbegriffe einbinden", "Höhe Anzeigefläche", "Layout anpassen", "Zeichensatz Inhalt" und "Zeichensatz Javascript". Die Felder beschreibt der Abschnitt [Tab Anzeige Inhalt](Course_Element_HTML_Page.de.md#layout).

[Zum Seitenanfang ^](#CP_learning_content)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Wie erstelle ich ein Content Package? (Schritt-für-Schritt-Anleitung) >](../../manual_how-to/content_package/content_package.de.md)<br>
[Inhaltsdomäne >](../basic_concepts/Content_Domain.de.md)<br>
[CP-Lerninhalt: Administration >](CP_Administration/index.de.md)<br>
[Kursbaustein "HTML-Seite" >](Course_Element_HTML_Page.de.md)

**Weiterführend**<br>
[Erstellen und Bearbeiten eines Content Packages >](../learningresources/CP_Editor.de.md)

[Zum Seitenanfang ^](#CP_learning_content)
