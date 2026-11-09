# SCORM 1.2: Administration {: #scorm_administration}

Ein SCORM-Paket importieren Sie einmal als Lernressource "SCORM 1.2" und binden es danach in Kurse ein. Im Menü "Administration" der Lernressource ersetzen Sie das Paket durch eine neue Fassung, legen fest, wie OpenOlat es anzeigt, und kopieren, exportieren oder löschen die Lernressource. Das Menü sehen Besitzer:innen der Lernressource, Lernressourcenverwalter:innen und Administrator:innen.

Das Menü "Administration" enthält diese Einträge:

* **Einstellungen**: siehe [Einstellungen](#settings).
* **Mitgliederverwaltung**: Hier tragen Sie weitere Besitzer:innen ein. Bei eigenständiger Verwendung verwalten Sie hier auch Betreuer:innen und Teilnehmer:innen, siehe [Mitgliederverwaltung](Members_management.de.md).
* **Angebotsarten**: nur aktiv, wenn die Lernressource buchbar konfiguriert ist, siehe [Angebotsarten](Offer_Types.de.md).
* **SCORM ersetzen**: siehe [SCORM ersetzen](#replace_scorm).
* **Weitere Einträge**: "Kopieren", "Inhalt exportieren", "Über dieses SCORM 1.2" und "Löschen" funktionieren wie bei allen Lernressourcen, siehe [Detailansicht einer Lernressource](Detailed_View_of_Learning_Resources.de.md). "Inhalt exportieren" lädt das SCORM-Paket als ZIP-Datei herunter.

Einen Editor hat die Lernressource "SCORM 1.2" nicht. Ein SCORM-Paket ändern Sie ausserhalb von OpenOlat und laden die neue Fassung mit "SCORM ersetzen" hoch.

[Zum Seitenanfang ^](#scorm_administration)

---


## SCORM ersetzen [:octicons-tag-16:{ title="ab Release 18.1.1 (OO-7096)" }](https://track.frentix.com/issue/OO-7096) {: #replace_scorm}

Haben Sie ein SCORM-Paket überarbeitet, ersetzen Sie es in der bestehenden Lernressource. Die Lernressource bleibt dieselbe, die Kurse, die sie einbinden, zeigen danach das neue Paket. Sie öffnen den Dialog unter:<br>
`SCORM 1.2 > Administration > SCORM ersetzen`

Wählen Sie im Feld "SCORM Datei Upload" die ZIP-Datei des neuen SCORM-Pakets aus. OpenOlat prüft die Datei gleich nach der Auswahl. Ist sie ein gültiges SCORM-Paket, wird der Button "SCORM ersetzen" aktiv, und ein Klick darauf ersetzt das bisherige Paket. Erkennt OpenOlat die Datei nicht, meldet der Dialog, dass das Format oder die Version nicht unterstützt wird.

Ist die Lernressource bereits in Kursen eingebunden, nennt der Dialog die Anzahl dieser Kurse. Das Ersetzen eines bereits verwendeten Pakets kann zu Inkonsistenzen führen. Prüfen Sie danach die Konfiguration der Kursbausteine "SCORM 1.2", die das Paket einbinden, siehe [Kursbaustein "SCORM 1.2"](Course_Element_SCORM_Learning_Content.de.md#editor_tab_learning_content).

[Zum Seitenanfang ^](#scorm_administration)

---


## Einstellungen {: #settings}

Die Einstellungen öffnen Sie unter:<br>
`SCORM 1.2 > Administration > Einstellungen`

Die Tabs erscheinen in dieser Reihenfolge:

* **Metadaten**: siehe [Kurseinstellungen - Tab Metadaten](Course_Settings_Metadata.de.md).
* **Info**: siehe [Kurseinstellungen - Tab Info](Course_Settings_Info.de.md).
* **Freigabe**: siehe [Kurseinstellungen - Tab Freigabe](Course_Settings_Share/index.de.md).
* **Katalog**: nur wenn der Katalog in der Version 1 eingeschaltet ist und die Lernressource den Verwendungszweck "Eigenständig" hat, siehe [Kurseinstellungen, Tab Katalog](Course_Settings/index.de.md#catalog).
* **Layout**: siehe [unten](#tab_layout).
* **Optionen**: der Zugriff für Teilnehmende im Status "Beendet", siehe [Kurseinstellungen - Tab Optionen](Course_Settings_Options.de.md). Der Tab fehlt, wenn im Tab "Freigabe" der Verwendungszweck "Einbindung" gewählt ist.

Die Seiten zu den Kurseinstellungen gelten für alle Lernressourcen. Einzelne Felder dort gibt es nur bei Kursen, das steht jeweils beim Feld.

### Tab "Layout" {: #tab_layout}

Im Tab "Layout" legen Sie fest, wie OpenOlat das SCORM-Paket anzeigt, zum Beispiel unverändert im Anzeigemodus "Standard" oder mit dem Layout von OpenOlat. Die Einstellungen gelten, wenn Sie die Lernressource direkt öffnen. Ausserdem übernimmt sie der Kursbaustein "SCORM 1.2", wenn dort im Tab "Anzeige Inhalt" unter "Standardwerte übernehmen" die Option "Aus Layouteinstellungen der Lernressource übernehmen" gewählt ist.

Der Tab zeigt dieselben Felder wie der Tab "Anzeige Inhalt" des Kursbausteins: "Anzeigemodus", "JavaScript hinzufügen", "Glossarbegriffe einbinden", "Höhe Anzeigefläche", "Layout anpassen", "Zeichensatz Inhalt" und "Zeichensatz Javascript". Die Felder beschreibt der Abschnitt [Tab "Anzeige Inhalt"](Course_Element_SCORM_Learning_Content.de.md#editor_tab_display_content). Für SCORM-Pakete ist der Anzeigemodus "Standard" empfohlen, weil OpenOlat auf die Gestaltung des Pakets keinen Einfluss hat.

[Zum Seitenanfang ^](#scorm_administration)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Mitgliederverwaltung >](Members_management.de.md)<br>
[Angebotsarten >](Offer_Types.de.md)<br>
[Detailansicht einer Lernressource >](Detailed_View_of_Learning_Resources.de.md)<br>
[Kursbaustein "SCORM 1.2" >](Course_Element_SCORM_Learning_Content.de.md)<br>
[Kurseinstellungen - Tab Metadaten >](Course_Settings_Metadata.de.md)<br>
[Kurseinstellungen - Tab Info >](Course_Settings_Info.de.md)<br>
[Kurseinstellungen - Tab Freigabe >](Course_Settings_Share/index.de.md)<br>
[Kurseinstellungen >](Course_Settings/index.de.md)<br>
[Kurseinstellungen - Tab Optionen >](Course_Settings_Options.de.md)

**Weiterführend**<br>
[CP-Lerninhalt: Administration >](CP_Administration/index.de.md)<br>
[Bewertung von Kursbausteinen >](Assessment_of_course_modules.de.md)

[Zum Seitenanfang ^](#scorm_administration)
