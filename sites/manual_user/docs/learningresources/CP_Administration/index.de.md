# CP-Lerninhalt: Administration {: #cp_administration}

Einen CP-Lerninhalt erstellen Sie einmal und binden ihn danach in beliebig viele Kurse ein. Im Menü "Administration" des CP-Lerninhalts bearbeiten Sie seine Seiten, legen fest, wie OpenOlat sie anzeigt, und kopieren, exportieren oder löschen den Lerninhalt. Das Menü sehen Besitzer:innen der Lernressource, Lernressourcenverwalter:innen und Administrator:innen.

Das Menü "Administration" enthält diese Einträge:

* **Einstellungen**: siehe [Einstellungen](#settings).
* **Mitgliederverwaltung**: Hier tragen Sie weitere Besitzer:innen ein. Bei eigenständiger Verwendung verwalten Sie hier auch Betreuer:innen und Teilnehmer:innen, siehe [Mitgliederverwaltung](../Members_management.de.md).
* **Inhalt editieren**: öffnet den CP Editor, siehe [Inhalt editieren](#edit_content).
* **Angebotsarten**: nur aktiv, wenn der CP-Lerninhalt buchbar konfiguriert ist, siehe [Angebotsarten](../Offer_Types.de.md).
* **Weitere Einträge**: "Kopieren", "Inhalt exportieren", "Über diesen CP-Lerninhalt" und "Löschen" funktionieren wie bei allen Lernressourcen, siehe [Detailansicht einer Lernressource](../Detailed_View_of_Learning_Resources.de.md). "Inhalt exportieren" lädt den CP-Lerninhalt als ZIP-Datei herunter.

[Zum Seitenanfang ^](#cp_administration)

---


## Inhalt editieren {: #edit_content}

Die Seiten und die Struktur des CP-Lerninhalts bearbeiten Sie im CP Editor. Sie öffnen ihn unter:<br>
`CP-Lerninhalt > Administration > Inhalt editieren`

Wie Sie im CP Editor Seiten hinzufügen, importieren, verschieben und bearbeiten, beschreibt die Seite [CP Editor](../CP_Editor.de.md). Verwaltet ein externes System den Inhalt, ist der Eintrag nicht anwählbar.

[Zum Seitenanfang ^](#cp_administration)

---


## Einstellungen {: #settings}

Die Einstellungen öffnen Sie unter:<br>
`CP-Lerninhalt > Administration > Einstellungen`

Die Tabs erscheinen in dieser Reihenfolge:

* **Metadaten**: siehe [Kurseinstellungen - Tab Metadaten](../Course_Settings_Metadata.de.md).
* **Info**: siehe [Kurseinstellungen - Tab Info](../Course_Settings_Info.de.md).
* **Freigabe**: siehe [Kurseinstellungen - Tab Freigabe](../Course_Settings_Share/index.de.md).
* **Katalog**: nur wenn der Katalog in der Version 1 eingeschaltet ist und der CP-Lerninhalt den Verwendungszweck "Eigenständig" hat, siehe [Kurseinstellungen, Tab Katalog](../Course_Settings/index.de.md#catalog).
* **Quota**: siehe [unten](#tab_quota).
* **Layout**: siehe [unten](#tab_layout).
* **Optionen**: der Zugriff für Teilnehmende im Status "Beendet", siehe [Kurseinstellungen - Tab Optionen](../Course_Settings_Options.de.md). Der Tab fehlt, wenn im Tab "Freigabe" der Verwendungszweck "Einbindung" gewählt ist.

Die Seiten zu den Kurseinstellungen gelten für alle Lernressourcen. Einzelne Felder dort gibt es nur bei Kursen, das steht jeweils beim Feld.

### Tab "Quota" {: #tab_quota}

Bilder, Videos und PDF-Dateien lassen einen CP-Lerninhalt schnell wachsen. Im Tab "Quota" legen Sie fest, wie viel Speicherplatz er höchstens belegen darf: "Quota (KB)" begrenzt den ganzen Lerninhalt, "Upload Limite (KB)" eine einzelne hochgeladene Datei.

Unter den Feldern listet der Tab die systemweiten "Default Quotas" und hebt die Zeile "Lernressourcen" hervor. Dieser Standardwert gilt, solange der CP-Lerninhalt keine eigene Quota hat. Mit "Auf Default Quota zurücksetzen" gilt wieder der Standardwert. Die Standardwerte legen Systemadministrator:innen fest, siehe [Dateien und Ordner](../../../manual_admin/administration/Files_and_Folders.de.md#files_and_folders_quotas).

Den Tab "Quota" sehen nur Administrator:innen, Systemadministrator:innen, Lernressourcenverwalter:innen, Benutzerverwalter:innen und Rollenverwalter:innen.

### Tab "Layout" {: #tab_layout}

Im Tab "Layout" legen Sie fest, wie OpenOlat die Seiten des CP-Lerninhalts anzeigt, zum Beispiel ob das Layout von OpenOlat auf die Seiten angewendet wird und wie hoch die Anzeigefläche ist. Die Einstellungen gelten, wenn Sie den CP-Lerninhalt direkt öffnen. Ausserdem übernimmt sie der Kursbaustein "CP-Lerninhalt", wenn dort im Tab "Anzeige Inhalt" unter "Standardwerte übernehmen" die Option "Aus Layouteinstellungen der Lernressource übernehmen" gewählt ist.

Der Tab zeigt dieselben Felder wie der Tab "Anzeige Inhalt" im Kursbaustein "HTML-Seite": "Anzeigemodus", "JavaScript hinzufügen", "Glossarbegriffe einbinden", "Höhe Anzeigefläche", "Layout anpassen", "Zeichensatz Inhalt" und "Zeichensatz Javascript". Die Felder beschreibt der Abschnitt [Tab Anzeige Inhalt](../Course_Element_HTML_Page.de.md#layout).

[Zum Seitenanfang ^](#cp_administration)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Mitgliederverwaltung >](../Members_management.de.md)<br>
[Angebotsarten >](../Offer_Types.de.md)<br>
[Detailansicht einer Lernressource >](../Detailed_View_of_Learning_Resources.de.md)<br>
[CP Editor >](../CP_Editor.de.md)<br>
[Kurseinstellungen - Tab Metadaten >](../Course_Settings_Metadata.de.md)<br>
[Kurseinstellungen - Tab Info >](../Course_Settings_Info.de.md)<br>
[Kurseinstellungen - Tab Freigabe >](../Course_Settings_Share/index.de.md)<br>
[Kurseinstellungen >](../Course_Settings/index.de.md)<br>
[Kurseinstellungen - Tab Optionen >](../Course_Settings_Options.de.md)<br>
[Dateien und Ordner >](../../../manual_admin/administration/Files_and_Folders.de.md)<br>
[Kursbaustein "HTML-Seite" >](../Course_Element_HTML_Page.de.md)

**Weiterführend**<br>
[Kursbaustein "CP-Lerninhalt" >](../Course_Element_CP_Learning_Content.de.md)<br>
[Wie erstelle ich ein Content Package? >](../../../manual_how-to/content_package/content_package.de.md)

[Zum Seitenanfang ^](#cp_administration)
