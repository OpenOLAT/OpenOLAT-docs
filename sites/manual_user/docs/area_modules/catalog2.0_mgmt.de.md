# Katalog 2.0 - Verwaltung {: #catalog_mgmt}


## Kurzbeschreibung der Katalog-Verwaltung {: #description}

Mit der Katalog-Verwaltung pflegen Sie die Taxonomien, nach denen der Katalog 2.0 seine Angebote gliedert, ohne Administrator:in zu sein. Die Katalog-Verwaltung ist keine eigene Rolle, sondern ein Recht: die Kompetenz "Verwalten" auf einer Taxonomieebene.


## Wo wird die Katalog-Verwaltung aufgerufen? [:octicons-tag-16:{ title="ab Release 17.1 (OO-6201)" }](https://track.frentix.com/issue/OO-6201) {: #access}

Sie öffnen die Katalog-Verwaltung über einen Link im Katalog. Berechtigte finden rechts oben unter dem Header des Katalogs zusätzlich diese Links:

- **Katalog-Verwaltung**
- **Zur Administration**

![Markierte Links Katalog-Verwaltung und Zur Administration rechts unter dem Katalog-Header](assets/catalog20_mgmt_access_v1_de.png){ class="shadow lightbox" title="Übersicht des Katalogs" }

[Zum Seitenanfang ^](#catalog_mgmt)

---


## Wer sieht im Katalog die beiden Links? {: #access_links}

Den Link "Katalog-Verwaltung" sehen:

- Lernressourcenverwalter:innen
- Administrator:innen
- Systemadministrator:innen
- Personen mit der Kompetenz "Verwalten" auf einer Taxonomieebene

Ob Lernressourcenverwalter:innen den Link erhalten, legen Systemadministrator:innen in der System-Administration fest: `Administration > Module > Katalog > Tab "Einstellungen"`, Feld "Taxonomie bearbeitbar von". Voraussetzung für den Link ist in jedem Fall das eingeschaltete Modul Taxonomie.

Den Link "Zur Administration" sehen nur Systemadministrator:innen. Er öffnet das Modul Katalog in der System-Administration.

[Zum Seitenanfang ^](#catalog_mgmt)

---


## Wie bekommt man das Recht (die Kompetenz) zur Katalog-Verwaltung? [:octicons-tag-16:{ title="ab Release 20.1 (OO-8544)" }](https://track.frentix.com/issue/OO-8544) {: #competence}

Die Kompetenz "Verwalten" (das Recht zur Bearbeitung der im Katalog verwendeten Taxonomien) kann auf zwei Arten erteilt werden:

**Möglichkeit 1:**<br>
Durch Systemadministrator:innen in der System-Administration:<br>
`Administration > Module > Taxonomie > "Taxonomietitel" > "Taxonomieebene" > Tab "Verwaltung" > Button "Verwalter:in hinzufügen"`<br>
Die Taxonomie muss für den Katalog aktiviert sein. Öffnen Sie sie mit "anzeigen / bearbeiten".

**Möglichkeit 2:**<br>
Durch Benutzerverwalter:innen:<br>
`Benutzerverwaltung > "Person" > Tab "Kompetenzen" > Button "Verwalten" hinzufügen`

Sobald die Kompetenz erteilt wird, erscheint für diese Person der Link "Katalog-Verwaltung" rechts oben unter dem Katalog-Header.

!!! info "Wichtig"

    Die Katalog-Verwaltung ist nicht auf eine bestimmte Organisationseinheit eingeschränkt, obwohl die Rolle Lernressourcenverwalter:in auf eine Organisationseinheit eingeschränkt sein kann. (Taxonomien sind ebenfalls nicht auf Organisationseinheiten beschränkt.)

[Zum Seitenanfang ^](#catalog_mgmt)

---


## Was bearbeiten Sie in der Katalog-Verwaltung? {: #functions}

In der Katalog-Verwaltung bearbeiten Sie die Taxonomie des Katalogs, nicht die Lernressourcen. Kurse und andere Lernressourcen bearbeiten und löschen Sie [im Autorenbereich](../area_modules/Authoring.de.md), zum Beispiel wenn sie beendet sind.

Welche Tabs Sie sehen, hängt von Ihrem Recht ab:

- Systemadministrator:innen, Administrator:innen und berechtigte Lernressourcenverwalter:innen sehen die Tabs "Ebenen", "Metadaten", "Ebenentypen" und "Lost+found" und bearbeiten die ganze Taxonomie.
- Personen, die nur die Kompetenz "Verwalten" haben, sehen die Tabs "Ebenen" und "Metadaten". Sie bearbeiten nur die Taxonomieebenen, für die sie die Kompetenz haben, und sehen die Metadaten der Taxonomie ohne sie zu ändern.

### Tab Ebenen {: #tab_level}

Für die Fachbereiche (Taxonomieebenen) stehen diese Aktionen zur Verfügung:

- Bearbeiten
- Verschieben
- Zusammenführen
- Ebenentyp zuweisen
- Löschen
- Neue Unterebene erstellen

Unter den drei Punkten rechts neben dem Button "Neue Taxonomieebene erstellen" importieren Sie Taxonomieebenen oder exportieren alle. Den Export laden Sie als ZIP-Archiv herunter. Darin enthalten ist eine Excel-Tabelle mit der hierarchischen Struktur der Taxonomieebenen. Import und Export stehen nur mit dem Recht für die ganze Taxonomie zur Verfügung.

![Aktionen Ebenentyp zuweisen, Verschieben, Zusammenführen, Löschen und das Zeilenmenü einer Ebene](assets/catalog20_mgmt_edit_v1_de.png){ class="shadow lightbox" title="Tab Ebenen einer Taxonomie" }


!!! info "Wichtig"

    Startseite, Filter und Layout des Katalogs gestalten Systemadministrator:innen in der System-Administration unter `Administration > Module > Katalog`.


[Zum Seitenanfang ^](#catalog_mgmt)

---


### Tab Metadaten {: #tab_metadata}

Der Tab "Metadaten" enthält die Angaben zur Taxonomie selbst, nicht zu ihren Ebenen. Die Metadaten einer einzelnen Taxonomieebene öffnen Sie über deren Zeile im Tab "Ebenen".

![ID und Externe ID fest, Pflichtfelder Kennzeichen und Titel, dazu der Beschreibungseditor](assets/catalog20_mgmt_tab_metadata_v1_de.png){ class="shadow lightbox" title="Tab Metadaten einer Taxonomie" }


**ID:** Die ID wird automatisch erstellt und ermöglicht die eindeutige Identifikation des Objekts.

**Externe ID:** Falls ein externes Verwaltungssystem die Taxonomie angelegt hat, wird zusätzlich zur automatisch erstellten ID die externe ID erstellt.

**Kennzeichen:** (Pflichtfeld) Wählen Sie ein eindeutiges und logisches Kennzeichen als Kennung für die Taxonomie. Dieses Kennzeichen erscheint in der Kopfzeile über dem Titel und ist für viele Zwecke praktikabler als der ausführliche Titel (der dafür verständlicher, umgangssprachlicher sein kann).

**Titel:** (Pflichtfeld) Der Titel wird an unterschiedlichen Stellen verwendet (Katalog 2.0, Dokumentenpool, e-Portfolio, Fragenpool). Er sollte die Taxonomie kurz und zutreffend beschreiben.

**Beschreibung:** Die Eingabe einer etwas ausführlicheren Beschreibung der Taxonomie ist optional.

[Zum Seitenanfang ^](#catalog_mgmt)

---


### Tab Ebenentypen {: #tab_leveltype}

Mit dem Button "Neuer Ebenentyp erstellen" legen Sie einen weiteren Ebenentyp an. Im Bearbeitungsdialog stehen die folgenden Felder zur Verfügung.


![Liste der Ebenentypen mit Kompetenz- und Leistungsnachweis-Freigabe und der Button Neuer Ebenentyp erstellen](assets/catalog20_mgmt_tab_leveltype_v1_de.png){ class="shadow lightbox" title="Tab Ebenentypen einer Taxonomie" }

![Kennzeichen und Titel als Pflichtfelder, dazu CSS class, Sichtbar, Kompetenzen, Leistungsnachweise und Untertypen](assets/catalog20_mgmt_tab_leveltype_edit_v1_de.png){ class="shadow lightbox" title="Dialog Bearbeiten eines Ebenentyps" }


**Kennzeichen:** Zusätzlich zum Titel muss ein Kennzeichen angegeben werden.

**Titel:** Formulieren Sie einen zutreffenden Titel zur Beschreibung des Ebenentyps.

**CSS class:** Sofern eine entsprechende CSS class im Theme hinterlegt ist, kann sie hier ausgewählt werden.

**Sichtbar:** Hier wird definiert, ob alle Taxonomieebenen dieses Typs sichtbar sein sollen.

**Kompetenzen:** Benutzer:innen können in der Benutzerverwaltung Kompetenzen zugeteilt werden. Mit Wahl dieser Option werden Taxonomieebenen mit diesem Ebenentyp für die Nutzung als Kompetenz freigeschaltet.

**Leistungsnachweise:** Mit Wahl dieser Option werden Taxonomieebenen mit diesem Ebenentyp für die Gruppierung von Leistungsnachweisen freigeschaltet.

**Beschreibung:** Eine ausführlichere Beschreibung des Ebenentyps ist optional.

**Untertypen:** Aus den bereits bestehenden Ebenentypen kann ein Untertyp ausgewählt werden. So ist es möglich, eine hierarchische Struktur zu schaffen. Sie wird dann beim Erstellen der Taxonomieebenen sichtbar.


[Zum Seitenanfang ^](#catalog_mgmt)

---


### Tab Lost+found {: #tab_lost_found}

Hier liegen die Dokumente gelöschter Taxonomieebenen. Löschen Sie eine Ebene, ohne sie zusammenzuführen, kopiert OpenOlat deren Dokumente in einen Unterordner. Der Ordnername besteht aus dem Kennzeichen und der ID der gelöschten Ebene. Führen Sie die Ebene stattdessen mit einer anderen Ebene zusammen, wandern die Dokumente in die Zielebene.

![Ordner gelöschter Taxonomieebenen mit den Ansichten Ordner, Dateien und Papierkorb](assets/catalog20_mgmt_tab_lost_found_v1_de.png){ class="shadow lightbox" title="Tab Lost+found einer Taxonomie" }


[Zum Seitenanfang ^](#catalog_mgmt)

---


## Weiterführende Informationen {: #further_information}

[Autorenbereich - Übersicht >](../area_modules/Authoring.de.md)<br>
[Modul Taxonomie >](../../manual_admin/administration/Modules_Taxonomy.de.md)<br>
[Wie zeige ich meine Kurse im OpenOlat-Katalog? >](../../manual_how-to/catalog/catalog.de.md)<br>
[Katalog 2.0 - Angebote >](../area_modules/catalog2.0_angebote.de.md)<br>
[Katalog 2.0 - Design >](../area_modules/catalog2.0_design.de.md)<br>
[Extern verfügbarer Katalog >](../area_modules/catalog2.0_web.de.md)<br>
[Modul Katalog >](../../manual_admin/administration/Modules_Catalog_2.0.de.md)

[Zum Seitenanfang ^](#catalog_mgmt)

