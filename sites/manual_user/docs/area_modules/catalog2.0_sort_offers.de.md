# Katalog 2.0 - Sortierung/Reihenfolge {: #catalog_sort}

Im Katalog 2.0 können die Angebote manuell oder dynamisch zusammengestellt werden. Wenn Kursbesitzer:innen beim Konfigurieren den Wunsch angegeben haben, dass ihr Kurs im Katalog erscheinen soll, werden dynamisch Einträge in den Katalog eingefügt.

Dadurch stellt sich die Frage, an welcher Stelle im Katalog die Angebote angezeigt werden.


## Sortierung/Reihenfolge auf der Startseite des Katalogs {: #sorting_startpage}

Auf der **Startseite** des Katalogs wird die Reihenfolge der Objekte durch die Launcher bestimmt. Als Launcher werden die Abschnitte bezeichnet.

![Vier nummerierte Launcher bestimmen die Reihenfolge auf der Katalog-Startseite: Begrüssungstext, Kategorien, Beliebte Kurse, Zuletzt veröffentlichte Ressourcen](assets/catalog20_sort_offers_startpage_v1_de.png){ class="shadow lightbox" }

!!! note "Wie zeige ich meine Kurse im Katalog?"
    Anleitung zum Anzeigen von Kursen im Katalog.<br>
    [Wie zeige ich meine Kurse im Katalog? >](../../manual_how-to/catalog/catalog.de.md)


### Reihenfolge der Launcher festlegen {: #sorting_startpage_launcher}

Die Reihenfolge der Launcher (Abschnitte auf der Startseite) wird in der System-Administration festgelegt unter:<br>
`Administration > Module > Katalog > Tab "Startseite"`

Die Reihenfolge kann durch Klick auf die Doppelpfeile zu Beginn der Zeilen festgelegt werden.

![Vier Launcher mit Doppelpfeilen in der Spalte Position zum Umsortieren, Tab Startseite im Katalog-Modul](assets/catalog20_sort_offers_startpage_launchers_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#catalog_sort)

---


### Sortierung innerhalb eines Launchers {: #sorting_startpage_inside_launcher}

Innerhalb eines Launcher hängt die Reihenfolge der Angebote vom Launchertyp ab:

!!! note "Launchertyp"
    Konfiguration der Launchertypen in der Administration.<br>
    [Launchertyp >](../../manual_admin/administration/Modules_Catalog_2.0.de.md#tab_start_page)


**Launchertyp "Statischer Text":**<br>
Es erfolgt keine automatische Sortierung.

**Launchertyp "Beliebte Kurse":**<br>
Die Reihenfolge der Angebote wird durch die Anzahl der Klicks auf Kursbausteine während der letzten 28 Tage bestimmt. Dabei werden nur Kurse mit Status "Veröffentlicht" berücksichtigt.

**Launchertyp "Zuletzt veröffentlicht":**<br>
Die Angebote sind nach Veröffentlichungsdatum geordnet.

**Launchertyp "Zufallsgenerator":**<br>
Zufallsreihenfolge

**Launchertyp "Taxonomieebene":**<br>
In einem Launcher vom Typ "Taxonomielevel" werden keine Kurse und Lernressourcen direkt angezeigt, die angezeigten Taxonomielevel entsprechen vielmehr Ordnern, in denen dann erst die Kurse und Lernressourcen zu finden sind.<br>
Die Angebote werden nach der Taxonomie automatisch ausgewählt und dann alphabetisch geordnet in einer Microsite aufgelistet, die sich beim Klick auf einen der Taxonomielevel in einem Taxonomie-Launcher öffnet.

**Launchertyp "Ausgewählte Lernressourcen":**<br>
Die manuell hinzugefügten Lernressourcen können durch Klick auf Doppelpfeile vor den Einträgen geordnet werden.

**Launchertyp "Ausgewählte Durchführungen":**<br>
Die manuell hinzugefügten Durchführungen können durch Klick auf Doppelpfeile vor den Einträgen geordnet werden.

[Zum Seitenanfang ^](#catalog_sort)

---


### Reihenfolge der Unterseiten/Kategorien festlegen {: #sorting_startpage_categories}

Soll ein Launcher Unterkategorien anzeigen, wird ein Launcher vom Typ "Taxonomieebene" verwendet.

![Launcher Kursangebote mit neun Kategorie-Kacheln als Unterseiten, Startseite des Katalogs](assets/catalog20_sort_offers_microsites_taxonomy1_v1_de.png){ class="shadow lightbox" }

Die Reihenfolge der Einträge innerhalb des Taxonomie-Launchers (Reihenfolge der Unterseiten/Kategorien im Katalog) wird durch die Struktur der Taxonomie bestimmt und muss deshalb via Taxonomie geändert werden.<br>
`Administration > Module > Taxonomie > Aktivierung einer Taxonomie für Lernressourcen/Katalog`

Beispiel: Taxonomiestruktur für den vorstehend angezeigten Taxonomie-Launcher:

![Taxonomieebenen des Katalogs mit dem offenen Zeilenmenü und der Option Bearbeiten, Tab Ebenen der Taxonomie](assets/catalog20_sort_offers_microsites_taxonomy2_v1_de.png){ class="shadow lightbox" }

* Wählen Sie unter den 3 Punkten die Option zum Bearbeiten einer Taxonomieebene.<br>
* Im Tab "Metadaten" finden Sie das Feld zur Angabe der Sortierung.<br>
* Die hier für die Taxonomie angegebene Zahl bestimmt auch die Position innerhalb des Launchers. (Im oben gezeigten Beispiel: 0 = 1. Unterseite/Kategorie, 1 = 2. Unterseite/Kategorie, 2 = 3. Unterseite/Kategorie => im Katalog an dritter Position)

![Feld Sortierung mit dem Wert 2 bestimmt die Position der Unterseite, Tab Metadaten einer Taxonomieebene](assets/catalog20_sort_offers_microsites_taxonomy3_v1_de.png){ class="shadow lightbox" }

!!! info "Wichtig"

    Eine Änderung der Taxonomiestruktur hat nicht nur im Katalog Auswirkungen, sondern auch überall dort, wo diese Taxonomie ebenfalls für eine Auswahl verwendet wird. 


[Zum Seitenanfang ^](#catalog_sort)

---


## Sortierung/Reihenfolge innerhalb der Kategorien (Microsites) des Katalogs {: #sorting_microsites}


### Sortierreihenfolge selbst wählen {: #sorting_microsites_button}

Über der Liste einer Kategorie sitzt rechts oben der Sortier-Button. Er trägt immer das aktive Kriterium als Beschriftung, das Pfeilsymbol zeigt die Richtung. Ein Klick öffnet die Liste **"Sortierreihenfolge"**.

![Sortier-Button Relevanz und offene Liste Sortierreihenfolge mit allen Kriterien, Tabellenansicht einer Katalogkategorie](assets/catalog20_sort_offers_microsites_sort_button_v1_de.png){ class="shadow lightbox" }

Zur Auswahl stehen "Relevanz" sowie alle sortierbaren Spalten der Liste, darunter "Zeitabschnitt" und "Zeitabschnitt Beschr.".

!!! info "Wichtig"
    Der Sortier-Button erscheint nur, wenn die "Sortierung nach Priorität" aktiviert ist. Ohne diese Einstellung ist die Liste fest nach dem Titel aufsteigend sortiert und lässt sich nur über die Spaltentitel umsortieren. Die Aktivierung beschreibt der Abschnitt [Sortierung nach Priorität](#sorting_microsites_by_priority).

!!! note "Modul Zeitabschnitte"
    Die Spalte "Zeitabschnitt" erscheint in der Liste, sobald die Systemadministration das Modul "Zeitabschnitte" eingeschaltet hat.<br>
    [Modul Zeitabschnitte >](../../manual_admin/administration/Modules_Time_Period.de.md)

[Zum Seitenanfang ^](#catalog_sort)

---


### Sortierung über die Spaltentitel [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9218)" }](https://track.frentix.com/issue/OO-9218){:target="_blank"} {: #sorting_microsites_lists}

Wie in allen Listen in OpenOlat, können auch die Angebote des Katalogs durch **Klick auf einen Spaltentitel** sortiert werden.

!!! note "Hinweis"
    Die Spalte "Zeitabschnitt" sortiert chronologisch nach dem Zeitrahmen und nicht alphabetisch nach der Kurzbezeichnung: zuerst nach dem Beginndatum, dann nach dem Enddatum, zuletzt nach dem Titel. Einträge ohne Zeitabschnitt erscheinen immer am Ende der Liste.

    Das Kriterium "Zeitabschnitt Beschr." sortiert alphabetisch nach der Beschreibung. Einträge ohne Beschreibung erscheinen am Ende der Liste.

[Zum Seitenanfang ^](#catalog_sort)

---


### Sortierung nach Priorität [:octicons-tag-16:{ title="ab Release 20.2.0 (OO-9039)" }](https://track.frentix.com/issue/OO-9039){:target="_blank"} {: #sorting_microsites_by_priority}

Die "Sortierung nach Priorität" aktivieren Administrator:innen in der System-Administration unter:<br>
`Administration > Module > Katalog > Tab "Einstellungen" > Toggle-Button "Sortierung nach Priorität"`

Danach erscheint der Sortier-Button rechts oben über einer Auflistung. Sein Standardkriterium ist "Relevanz".

![Sortier-Button mit dem Standardkriterium Relevanz über einer Angebotsliste, Kachelansicht einer Katalogkategorie](assets/catalog20_sort_offers_microsites_button_relevance_v1_de.png){ class="shadow lightbox" }

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

![Zeile Katalog Priorität bei Sortierung mit dem Link anpassen, Tab Katalog einer Durchführung im Course Planner](assets/catalog20_sort_offers_microsites_cp_change_priority_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#catalog_sort)

---


### Welche Prioritäten können gesetzt werden? {: #sorting_microsites_priorities}

Als Priorität kann ein voreingestellter Boost-Wert gewählt oder ein eigener Boost-Wert eingegeben werden.
Je höher der Boost-Wert, umso weiter vorne wird ein Angebot im Katalog angezeigt. Mit eigenen benutzerdefinierten Boost-Werten kann eine Feinjustierung in der Anzeigereihenfolge vorgenommen werden.

- Normal (Boost-Wert 0)
- Mittel (Boost-Wert 1000)
- Hoch (Boost-Wert 2000)
- Sehr hoch (Boost-Wert 3000)
- Ultimativ (Boost-Wert 4000)
- Benutzerdefiniert (eigener Boost-Wert)

![Auswahl Priorität Hoch mit dem zugehörigen Boost-Wert 2000, Dialog Priorität anpassen](assets/catalog20_sort_offers_microsites_boost_v1_de.png){ class="shadow lightbox" }

!!! info "Wichtig"

    Die Sortierung nach Prioritäten hat keinen Einfluss auf die Sortierung auf der Startseite. Dort wird die Reihenfolge der Angebote durch die jeweiligen Launchertypen und die manuelle Anordnung in der Administration festgelegt.


[Zum Seitenanfang ^](#catalog_sort)

---


## Weiterführende Informationen {: #further_information}

[Wie zeige ich meine Kurse im Katalog? >](../../manual_how-to/catalog/catalog.de.md)<br>
[Angebote >](../../manual_user/area_modules/catalog2.0_angebote.de.md)<br>
[Design >](../../manual_user/area_modules/catalog2.0_design.de.md)<br>
[Externer Katalog >](../../manual_user/area_modules/catalog2.0_web.de.md)<br>
[Aktivierung der Prioritäten in der Administration >](../../manual_admin/administration/Modules_Catalog_2.0.de.md)<br>
[Modul Zeitabschnitte >](../../manual_admin/administration/Modules_Time_Period.de.md)

[Zum Seitenanfang ^](#catalog_sort)