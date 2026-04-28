# Katalog 2.0 - Verwaltung {: #catalog_mgmt}


## Kurzbeschreibung der Katalog-Verwaltung {: #description}

Die Katalogverwaltung des Katalogs V2 ist kein Aufgabenbereich, der einer eigenen Rolle zugeordnet wäre. Es ist vielmehr ein Feature zur Bearbeitung derjenigen Taxonomien, die im Katalog verwendet werden. Wer dieses Recht (Kompetenz "Verwalten") besitzt, kann diese Taxonomien und Teile davon bearbeiten, ohne Administrator zu sein.


## Wo wird die Katalog-Verwaltung aufgerufen? {: #access}

Der Zugriff auf die Katalogverwaltung erfolgt über einen Link im Katalog.
Im Katalog finden Berechtigte rechts oben unter dem Header zusätzlich die Links

- **Katalog-Verwaltung**
- **Zur Administration**

![catalog20_mgmt_access_v1_de.png](assets/catalog20_mgmt_access_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#catalog_mgmt)

---


## Wer sieht im Katalog die beiden Links? {: #access_links}

Den Link **"Katalog-Verwaltung"** haben

- Lernressourcenverwalter:innen
- Administrator:innen
- Systemadministrator:innen

Den Link **"Zur Administration"** haben
 
- Systemadministrator:innen

[Zum Seitenanfang ^](#catalog_mgmt)

---


## Wie bekommt man das Recht (die Kompetenz) zur Katalogverwaltung? {: #competence}

Die Kompetenz "Verwalten" (das Recht zur Bearbeitung der im Katalog verwendeten Taxonomien) kann auf 2 Arten erteilt werden:

**Möglichkeit 1:**<br>
Durch Systemadministrator:innen:<br>
Administration > Module > Taxonomie > Klick auf "anzeigen/bearbeiten" in einer Taxonomie, die für den Katalog aktiviert ist > Wahl einer Taxonomieebene > Tab "Verwaltung" > Button "Verwalter:in hinzufügen"

**Möglichkeit 2:**<br>
Durch Benutzerverwalter:innen:<br>
Benutzerverwaltung > Wahl einer Person > Tab Kompetenzen > Button "Kompetenz 'Verwalten' hinzufügen"

Sobald die Kompetenz erteilt wurde erscheint für diese Person der Link "Katalog-Verwaltung" rechts oben unter dem Katalog-Header.

!!! hint "Hinweis"

    Die Katalogverwaltung ist nicht auf eine bestimmte Organisationseinheit eingeschränkt, obwohl die Rolle Lernressourcenverwalter:in auf eine Organisatineinheit eingeschränkt sein kann. (Taxonomien sind ebenfalls nicht auf Organisationseinheiten beschränkt.)

[Zum Seitenanfang ^](#catalog_mgmt)

---


## Welche Bearbeitungen sind in der Katalogverwaltung möglich? {: #functions}

### Tab Ebenen  {: #tab_level}
Die Bearbeitungsmöglichkeiten der Fachbereiche (Taxonomieebenen) umfassen:

- Verschieben
- Löschen von Elementen der Taxonomieebene / Untertaxonomien
- Erstellen neuer Unterebenen

Unter den 3 Punkten rechts neben dem Button "Neue Taxonomieebene erstellen" finden Sie auch eine Möglichkeit, Taxonomieebenen zu importieren oder alle zu exportieren. Ein Export kann als zip-Archiv heruntergeladen werden. Darin enthalten ist eine Excel-Tabelle mit der hierarchischen Struktur der Taxonomieebenen.

![catalog20_mgmt_edit_v1_de.png](assets/catalog20_mgmt_edit_v1_de.png){ class="shadow lightbox" }


!!! hint "Hinweis"

    Das Gestalten der Launcher, Bereiche, usw. ist den Systemadministrator:innen vorbehalten.


[Zum Seitenanfang ^](#catalog_mgmt)

---


### Tab Metadaten {: #tab_metadata}

![catalog20_mgmt_tab_metadata_v1_de.png](assets/catalog20_mgmt_tab_metadata_v1_de.png){ class="shadow lightbox" }


**ID:** Die ID wird automatisch erstellt und ermöglicht die eindeutige Identifikation des Objekts.

**Externe ID:** Falls ein externes Verwaltungssystem die Ebenen angelegt hat, wird zusätzlich zur automatisch erstellten ID die externe ID erstellt.

**Kennzeichen:** (Pflichtfeld) Wählen Sie ein eindeutiges und logisches Kennzeichen als Kennung für die Taxonomieebene. Dieses Kennzeichen wird in der Tabelle im Tab "Taxonomie" in der Spalte "Ebenentyp" angezeigt und ist für viele Zwecke praktikabler als der ausführliche Titel (der dafür verständlicher, umgangssprachlicher sein kann).

**Titel:** (Pflichtfeld) Der Titel wird an unterschiedlichen Stellen verwendet (Katalog 2.0, Dokumentenpool, e-Portfolio, Fragenpool). Er sollte die Taxonomieebene kurz und zutreffend beschreiben.

**Beschreibung:** Die Eingabe einer etwas ausführlicheren Beschreibung der Ebene ist optional.

[Zum Seitenanfang ^](#catalog_mgmt)

---


### Tab Ebenentypen {: #tab_leveltype}


![catalog20_mgmt_tab_leveltype_v1_de.png](assets/catalog20_mgmt_tab_leveltype_v1_de.png){ class="shadow lightbox" }

![catalog20_mgmt_tab_leveltype_edit_v1_de.png](assets/catalog20_mgmt_tab_leveltype_edit_v1_de.png){ class="shadow lightbox" }


**Identifier:** Zusätzlich zum Titel muss ein Identifier angegeben werden.

**Titel:** Formulieren Sie einen zutreffenden Titel zur Beschreibung des Ebenentyps.

**CSS class:** Sofern eine entsprechende CSS class im Theme hinterlegt ist, kann sie hier ausgewählt werden.

**Sichtbar:** Hier wird definiert, ob alle Taxonomieebenen dieses Typs sichtbar sein sollen.

**Kompetenzen:** Benutzer:innen können in der Benutzerverwaltung Kompetenzen zugeteilt werden. Mit Wahl dieser Option werden Taxonomieebenen mit diesem Leveltyp für die Nutzung als Kompetenz freigeschaltet.

**Leistungsnachweise:** Mit Wahl dieser Option werden Taxonomieebenen mit diesem Leveltyp für die Gruppierung von Leistungsnachweisen freigeschaltet.

**Beschreibung:** Eine ausführlichere Beschreibung des Ebenentyps ist optional.

**Untertypen:** Aus den bereits bestehenden Ebenentypen kann ein Untertyp ausgewählt werden. So ist es möglich, eine hierarchische Struktur zu schaffen. Sie wird dann beim Erstellen der Taxonomieebenen sichtbar.


[Zum Seitenanfang ^](#catalog_mgmt)

---


### Tab Lost & Found {: #tab_lost_found}

Hier werden alle Elemente aus dem Tab "Ebenen" abgelegt.

![catalog20_mgmt_tab_lost_found_v1_de.png](assets/catalog20_mgmt_tab_lost_found_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#catalog_mgmt)

---


## Weitere Informationen {: #further_information}

[Taxonomie (Administrationshandbuch) > ](../../manual_admin/administration/Modules_Taxonomy.de.md)<br>
[Wie zeige ich meine Kurse im OpenOlat-Katalog? >](../../manual_how-to/catalog/catalog.de.md)<br>
[Angebote erstellen >](../area_modules/catalog2.0_angebote.de.md)<br>
[Katalog-Design >](../area_modules/catalog2.0_design.de.md)<br>
[Der Web-Katalog >](../area_modules/catalog2.0_web.de.md)<br>
[Katalog einrichten (Administrationshandbuch) >](../../manual_admin/administration/Modules_Catalog_2.0.de.md#config_web-catalog)<br>

[Zum Seitenanfang ^](#catalog_mgmt)

