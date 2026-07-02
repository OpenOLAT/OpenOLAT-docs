# Katalog 2.0 - Sortierung/Reihenfolge {: #catalog_sort}

Im Katalog 2.0 können die Angebote manuell oder dynamisch zusammengestellt werden. Wenn Kursbesitzer:innen beim Konfigurieren den Wunsch angegeben haben, dass ihr Kurs im Katalog erscheinen soll, werden dynamisch Einträge in den Katalog eingefügt.

Dadurch stellt sich die Frage, an welcher Stelle im Katalog die Angebote angezeigt werden.


## Sortierung/Reihenfolge auf der Startseite des Katalogs {: #sorting_startpage}

Auf der **Startseite** des Katalogs wird die Reihenfolge der Objekte durch die Launcher bestimmt. Als Launcher werden die Abschnitte bezeichnet.

![catalog20_sort_offers_startpage_v1_de.png](assets/catalog20_sort_offers_startpage_v1_de.png){ class="shadow lightbox" }

!!! info "Wie zeige ich meine Kurse im Katalog?"
    Anleitung zum Anzeigen von Kursen im Katalog.<br>
    [Wie zeige ich meine Kurse im Katalog? >](../../manual_how-to/catalog/catalog.de.md)


### Reihenfolge der Launcher festlegen {: #sorting_startpage_launcher}

Die Reihenfolge der Launcher (Abschnitte auf der Startseite) wird festgelegt unter:<br>
`Administration > Module > Katalog > Tab "Startseite"`

Die Reihenfolge kann durch Klick auf die Doppelpfeile zu Beginn der Zeilen festgelegt werden.

![catalog20_sort_offers_startpage_launchers_v1_de.png](assets/catalog20_sort_offers_startpage_launchers_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#catalog_sort)

---


### Sortierung innerhalb eines Launchers {: #sorting_startpage_inside_launcher}

Innerhalb eines Launcher hängt die Reihenfolge der Angebote vom Launchertyp ab:

!!! info "Launchertyp"
    Konfiguration der Launchertypen in der Administration.<br>
    [Launchertyp >](../../manual_admin/administration/Modules_Catalog_2.0.de.md#tab_start_page)


**Launchertyp "Statischer Text":**<br>
Es erfolgt keine automatische Sortierung.

**Launchertyp "Beliebte Kurse":**<br>
Die Reihenfolge der Angebote wird durch die Anzahl der Klicks auf Kursbausteine während den letzten 28 Tage bestimmt. 
Dabei werden nur Kurse mit Status "Publiziert" berücksichtigt.

**Launchertyp "Zuletzt veröffentlicht":**<br>
Die Angebote sind nach Veröffentlichungsdatum geordnet.

**Launchertyp "Zufallsgenerator":**<br>
Zufallsreihenfolge

**Launchertyp "Taxonomieebene":**<br>
In einem Launcher vom Typ "Taxonomielevel" werden keine Kurse und Lernressourcen direkt angezeigt, die angezeigten Taxonomielevel entsprechen vielmehr Ordnern, in denen dann erst die Kurse und Lernressourcen zu finden sind.<br> 
Die Angebote werden nach der Taxonomie automatisch ausgewählt und dann alphabetisch geordnet in einer Microsite aufgelistet,  die sich beim Klick auf einen der Taxonimielevel in einem Taxonomie-Launcher öffnet.

**Launchertyp "Ausgewählte Lernressourcen":**<br>
Die manuell hinzugefügten Lernressourcen können durch Klick auf Doppelpfeile vor den Einträgen geordnet werden.  

**Launchertyp "Ausgewählte Durchführungen":**<br>
Die manuell hinzugefügten Durchführungen können durch Klick auf Doppelpfeile vor den Einträgen geordnet werden.

[Zum Seitenanfang ^](#catalog_sort)

---


### Reihenfolge der Unterseiten/Kategorien festlegen {: #sorting_startpage_categories}

Soll ein Launcher Unterkategorien anzeigen, wird ein Launcher vom Typ "Taxonomieebene" verwendet.

![catalog20_sort_offers_microsites_taxonomy1_v1_de.png](assets/catalog20_sort_offers_microsites_taxonomy1_v1_de.png){ class="shadow lightbox" }

Die Reihenfolge der Einträge innerhalb des Taxonomie-Launchers (Reihenfolge der Unterseiten/Kategorien im Katalog) wird durch die Struktur der Taxonomie bestimmt und muss deshalb via Taxonomie geändert werden.<br>
`Administration > Module > Taxonomie > Aktivierung einer Taxonomie für Lernressourcen/Katalog`

Beispiel: Taxonomiestruktur für den vorstehend angezeigten Taxonomie-Launcher: 
![catalog20_sort_offers_microsites_taxonomy2_v1_de.png](assets/catalog20_sort_offers_microsites_taxonomy2_v1_de.png){ class="shadow lightbox" }

* Wählen Sie unter den 3 Punkten die Option zum Bearbeiten einer Taxonomieebene.<br> 
* Im Tab "Metadaten" finden Sie das Feld zur Angabe der Sortierung.<br> 
* Die hier für die Taxonomie angegebene Zahl bestimmt auch die Position innerhalb des Launchers. (Im oben gezeigten Beispiel: 0 = 1. Unterseite/Kategorie, 1 = 2. Unterseite/Kategorie, 2 = 3. Unterseite/Kategorie => im Katalog an dritter Position)

![catalog20_sort_offers_microsites_taxonomy3_v1_de.png](assets/catalog20_sort_offers_microsites_taxonomy3_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Eine Änderung der Taxonomiestruktur hat nicht nur im Katalog Auswirkungen, sondern auch überall dort, wo diese Taxonomie ebenfalls für eine Auswahl verwendet wird. 


[Zum Seitenanfang ^](#catalog_sort)

---


## Sortierung/Reihenfolge innerhalb der Kategorien (Microsites) des Katalogs {: #sorting_microsites}


### Manuelle Sortierung der Listen durch Benutzer:innen [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9218)" }](https://track.frentix.com/issue/OO-9218){:target="_blank"} {: #sorting_microsites_lists}

Wie in allen Listen in OpenOlat, können auch die Angebote des Katalogs durch **Klick auf einen Spaltentitel**  sortiert werden.

![catalog20_sort_offers_microsites_table_title_v1_de.png](assets/catalog20_sort_offers_microsites_table_title_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"
    Die Spalte "Durchführungszeitraum" sortiert chronologisch nach dem Zeitrahmen (zuerst nach Beginndatum, ohne Beginndatum nach Enddatum) und nicht alphabetisch nach der Bezeichnung. Einträge ohne Durchführungszeitraum erscheinen immer am Ende der Liste.

[Zum Seitenanfang ^](#catalog_sort)

---


### Sortierung nach Priorität {: #sorting_microsites_by_priority}

Wenn die "Sortierung nach Priorität" durch eine:n Administrator:in aktiviert worden ist (`Administration > Module > Katalog > Tab "Einstellungen" > Toggle-Button "Sortierung nach Priorität"`), erscheint rechts oben über einer Auflistung der **Button "Relevanz"**.
 
![catalog20_sort_offers_microsites_button_relevance_v1_de.png](assets/catalog20_sort_offers_microsites_button_relevance_v1_de.png){ class="shadow lightbox" }

Bei gewählter "Sortierung nach Relevanz" findet eine mehrstufige Sortierung statt:<br>
1. Kriterium: Sortierung nach Priorität<br>
2. Kriterium: Sortierung nach Beginndatum<br>
3. Kriterium: Sortierung nach Enddatum<br>
4. Kriterium: Sortierung nach Titel (alphabetisch)

Ist kein Datum angegeben, werden die Einträge ohne Datum nach denen mit Datum angezeigt.

[Zum Seitenanfang ^](#catalog_sort)

---


### Wo kann die Priorität eingestellt werden? {: #sorting_microsites_define_priority}

**Im Kurs:**<br>
`Kurs > Administration > Einstellungen > Abschnitt "Angebot Übersicht" > Klick auf "anpassen"`

**Im Course Planner:**<br>
`Course Planner > Durchführung > Tab Katalog > Button "Angebote" > Abschnitt "Angebot Übersicht" > Klick auf "anpassen"`

Beispiel Course Planner:
![catalog20_sort_offers_microsites_cp_change_priority_v1_de.png](assets/catalog20_sort_offers_microsites_cp_change_priority_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#catalog_sort)

---


### Welche Prioritäten können gesetzt werden? {: #sorting_microsites_priorities}

Als Priorität kann ein voreingestellter Boost-Wert gewählt oder ein eigener Bostwert eingegeben werden.
Je höher der Boost-Wert, umso weiter vorne wird ein Angebot im Katalog angezeigt. Mit eigenen benutzerdefinierten Boost-Werten kann eine Feinjustierung in der Anzeigereihenfolge vorgenommen werden.

- Normal (Boost-Wert 0)
- Mittel (Boost-Wert 1000)
- Hoch (Boost-Wert 2000)
- Sehr hoch (Boost-Wert 3000)
- Ultimativ (Boost-Wert 4000)
- Benutzerdefiniert (eigener Boost-Wert)

![catalog20_sort_offers_microsites_boost_v1_de.png](assets/catalog20_sort_offers_microsites_boost_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Die Sortierung nach Prioritäten hat keinen Einfluss auf die Sortierung auf der Startseite. Dort wird die Reihenfolge der Angebote durch die jeweiligen Launchertypen und die manuelle Anordnung in der Administration festgelegt.
    

[Zum Seitenanfang ^](#catalog_sort)

---


## Weiterführende Informationen  {: #further_information}

[Wie zeige ich meine Kurse im Katalog? >](../../manual_how-to/catalog/catalog.de.md)<br>
[Angebote >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>
[Design >](../../manual_user/area_modules/catalog2.0_design.de.md)<br>
[Externer Katalog >](../../manual_user/area_modules/catalog2.0_web.de.md)<br>
[Aktivierung der Prioritäten in der Administration >](../../manual_admin/administration/Modules_Catalog_2.0.de.md)<br>

[Zum Seitenanfang ^](#catalog_sort)