# Media Center: Informationen und Einstellungen zu Einzelmedien {: #media_center_items}

Zu jedem im Media Center abgelegten Einzelmedium können Informationen und Einstellungen eingegeben werden. Öffnen Sie dazu das Media Center und klicken Sie das gewünschte Medienelement an:<br>
`Persönliches Menü > Media Center > "Medienelement"`

Es öffnet sich eine Ansicht mit den nachfolgend beschriebenen Tabs:

* Übersicht
* Metadaten
* Verwendungen
* Freigaben


## Tab Übersicht {: #media_center_overview}

Der Tab "Übersicht" zeigt die Details Typ, Autor:in, Datum und Grösse. Es besteht ausserdem die Möglichkeit, den Aktivitätslog anzuzeigen und eine neue Version zu erstellen bzw. das Bild zu ersetzen.

![Tab Übersicht eines Bildes mit Typ, Autor:in, Datum und Grösse, den Buttons Neue Version erstellen und Bild ersetzen sowie dem eingeklappten Aktivitätslog](assets/media_center_items_tab_overview_v1_de.png){ class="shadow lightbox" title="Tab Übersicht eines Medienelements" }


### Aktivitätslog {: #media_center_activitylog}

Im Aktivitätslog kann nachverfolgt werden, wann das Medienelement von wem bearbeitet wurde.

![Markierter, aufgeklappter Aktivitätslog mit den Zeitraum-Tabs Letzte 7 Tage bis Alle und einem Eintrag Hochgeladen mit Datum, Version und Autor](assets/media_center_items_tab_overview_activity_v1_de.png){ class="shadow lightbox" title="Aktivitätslog im Tab Übersicht" }


### "Neue Version erstellen" und "Bild ersetzen" [:octicons-tag-16:{ title="ab Release 18.0.0 (OO-6986)" }](https://track.frentix.com/issue/OO-6986){:target="_blank"} {: #media_center_versioning}

Möchten Sie Arbeitsschritte oder Zwischenstufen eines Medienelements sichern, erstellen Sie mit "Neue Version erstellen" eine neue Version. Zu einer älteren Version wechseln Sie jederzeit zurück.

Mit "Bild ersetzen" tauschen Sie dagegen das Bild in der aktuellen Version aus. Alle sonstigen eingegebenen Metadaten und Einstellungen (z.B. Freigaben) bleiben dabei erhalten.


![Markierte Buttons Neue Version erstellen und Bild ersetzen oben rechts im Tab Übersicht eines Bildes](assets/media_center_items_tab_overview_new_version_v1_de.png){ class="shadow lightbox" title="Tab Übersicht eines Bildes" }



### Herunterladen oder Löschen {: #media_center_download}

Über das 3-Punkte-Menü rechts oben können Sie einzelne Medien aus dem Media Center herunterladen. Sind Sie Besitzer:in, können Sie Ihr Medienelement auch löschen.

![Markiertes, geöffnetes 3-Punkte-Menü mit Herunterladen und Löschen oben rechts über den Tabs eines Medienelements](assets/media_center_items_tab_overview_download_v1_de.png){ class="shadow lightbox" title="3-Punkte-Menü eines Medienelements" }


[Zum Seitenanfang ^](#media_center_items)

---


## Tab Metadaten [:octicons-tag-16:{ title="ab Release 18.0.0 (OO-7060)" }](https://track.frentix.com/issue/OO-7060){:target="_blank"} {: #media_center_metadata}

Folgende Informationen können einem Medienelement hinzugefügt werden:

* ein vom Dateinamen abweichender Titel
* Tags zur Verschlagwortung und für eine bessere Übersicht
* eine Zuordnung zu Themen und Fachbereichen (Taxonomie)
* eine Beschreibung
* ein "Alt-Text" bei draw.io Dateien oder Bildern/Grafiken. Er ist besonders relevant für Screenreader.
* eine Lizenzangabe, wie z.B. "CC BY-NC-SA"
* eine Quellenangabe

Je nach Art des Medientyps variieren die Informationen und Möglichkeiten der Metadaten. Alle Informationen können später geändert werden.

![Metadaten-Formular eines Bildes mit den Feldern Titel, Dateiname, Tags, Themen/Fachbereiche, Beschreibung, Alt-Text, Lizenz und Quelle](assets/media_center_items_tab_metadata_v1_de.png){ class="shadow lightbox" title="Tab Metadaten eines Bildes" }


### Metadaten mit KI generieren [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9355)" }](https://track.frentix.com/issue/OO-9355){:target="_blank"} {: #metadata_ai}

Die KI schlägt Ihnen Metadaten für ein Bild vor, auf zwei Wegen: Sie lösen die Vorschläge selbst mit einem Button aus, oder OpenOlat ergänzt sie beim Hochladen eines neuen Bildes im Hintergrund. Beide Wege setzen voraus, dass im [KI-Modul](../../manual_admin/administration/External_Tools_AI.de.md) die KI-Funktion "Bildbeschreibungs-Generator" eingeschaltet ist.

Beim Hochladen von Bildern und im Metadaten-Dialog steht der Button "Metadaten mit KI generieren" zur Verfügung, unabhängig von Ihren persönlichen KI-Einstellungen. Ein Klick darauf befüllt Titel, Beschreibung, Alt-Text und Tags mit KI-generierten Vorschlägen. Erkennt die KI, wovon das Bild handelt, ordnet sie dem Medium auch einen Fachbereich (Taxonomie) zu. Ist die [automatische Zuordnung per KI](../../manual_admin/administration/Modules_Taxonomy.de.md#ai_matching) eingerichtet, findet sie den inhaltlich passenden Fachbereich auch ohne Wortgleichheit. Ohne diese Einrichtung trifft die Zuordnung nur bei einem wortgleichen Fachbereich. Wenn das Feld "Themen/Fachbereiche" nach "Metadaten mit KI generieren" leer bleibt, hat das Media Center keine Taxonomie zur Auswahl. Die KI wählt den Fachbereich nur aus den Taxonomien, die das Media Center verwendet. Das sind die Taxonomien, die in der Konfiguration des Media Centers unter "Verknüpfte Taxonomien" ausgewählt sind. Ist dort keine ausgewählt, verwendet das Media Center die Taxonomien der Lernressourcen. Ein Hinweis im Formular zeigt an, dass die Metadaten mit KI generiert wurden. Prüfen Sie die Vorschläge vor dem Speichern und passen Sie sie bei Bedarf an. Für SVG-Bilder steht die KI-Bildanalyse nicht zur Verfügung.

Bereits ausgefüllte Felder bleiben bei der Generierung erhalten; der Titel wird nur ersetzt, wenn er leer ist oder einem Dateinamen entspricht.

![Fachbereich Astronomy von der KI gesetzt, dazu Hinweis und auslösender Button](assets/media_center_items_ai_v2_de.png){ class="shadow lightbox" title="Dialog Mediendatei hinzufügen" }

Beim Hochladen eines neuen Bildes, im Media Center mit "Mediendatei hinzufügen" wie im Element [Bild](Content_Editor.de.md#image) des Content Editors, ergänzt OpenOlat fehlende Metadaten zusätzlich im Hintergrund mit KI. Nach dem Speichern meldet OpenOlat: "Die Bild-Metadaten werden im Hintergrund mit KI generiert und in wenigen Augenblicken automatisch ergänzt." Dieser Weg läuft nur, wenn die KI-Bildbeschreibungen für Sie eingeschaltet sind, siehe [Tab KI-Einstellungen](../personal_menu/Settings.de.md#tab_ai_settings). Er entfällt, wenn Sie im selben Formular schon den Button "Metadaten mit KI generieren" benutzt haben [:octicons-tag-16:{ title="ab Release 21.1 (OO-9784)" }](https://track.frentix.com/issue/OO-9784){:target="_blank"}.

Beim [Markdown-Import in den Content Editor](Content_Editor.de.md#import_images) entscheiden Sie mit dem Schalter "Bild-Metadaten mit KI generieren" im Import-Dialog, ob OpenOlat die Metadaten der importierten Bilder im Hintergrund mit KI erzeugt [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9356)" }](https://track.frentix.com/issue/OO-9356){:target="_blank"}.

[Zum Seitenanfang ^](#media_center_items)

---


## Tab Verwendungen {: #media_center_uses}

Im Tab "Verwendungen" können Sie nachvollziehen, wo das Medienelement verwendet wird.<br>
Durch Klick auf die Verwendungsangabe können Sie direkt an die Stelle in diesem Kurs springen.

![Tabelle im Tab Verwendungen mit einem Eintrag: Verwendung Seite, Ressource Obstbau, Benutzer:in, Version Letzte, Status Gültig](assets/media_center_items_tab_uses_v1_de.png){ class="shadow lightbox" title="Tab Verwendungen eines Medienelements" }

[Zum Seitenanfang ^](#media_center_items)

---


## Tab Freigaben [:octicons-tag-16:{ title="ab Release 18.0.0 (OO-7061)" }](https://track.frentix.com/issue/OO-7061){:target="_blank"} {: #media_center_share}

Hier kann festgelegt werden, durch wen ein Medienelement verwendet werden darf. Teilnehmende können nur Gruppen definieren. Autor:innen haben mehr Möglichkeiten und können spezifische OpenOlat-Benutzer:innen, Gruppen, oder Kurse angeben. Durch die Freigabe können Dateien auch kollaborativ genutzt werden, wenn die Bearbeitung erlaubt wird.


![Markierter Button Freigabe hinzufügen mit den Zielen Benutzer:in, Gruppe, Kurs und Organisation sowie markierte Freigabezeile mit Schalter Bearbeitbar freigeben im Tab Freigaben](assets/media_center_items_tab_share_v1_de.png){ class="shadow lightbox" title="Tab Freigaben eines Medienelements" }


[Zum Seitenanfang ^](#media_center_items)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Externe Werkzeuge: KI-Modul >](../../manual_admin/administration/External_Tools_AI.de.md)<br>
[Modul Taxonomie >](../../manual_admin/administration/Modules_Taxonomy.de.md)<br>
[Content Editor >](Content_Editor.de.md)<br>
[Persönliche Konfiguration: Einstellungen >](../personal_menu/Settings.de.md)

**Weiterführend**<br>
[Media Center: Konzept >](Media_Center_Concept.de.md)<br>
[Persönliche Werkzeuge: Das Media Center >](../personal_menu/Media_Center.de.md)<br>
[Modul Media Center >](../../manual_admin/administration/Modules_Media_Center.de.md)<br>
[Arbeiten mit Mediendateien >](Working_with_Media_Files.de.md)

[Zum Seitenanfang ^](#media_center_items)
