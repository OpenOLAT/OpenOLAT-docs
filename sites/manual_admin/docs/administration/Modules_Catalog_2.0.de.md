# Modul Katalog {: #modul_catalog}

## Tab Einstellungen [:octicons-tag-16:{ title="ab Release 17.0 (OO-6145)" }](https://track.frentix.com/issue/OO-6145) {: #tab_settings}

Administrator:innen legen hier fest, ob Benutzer:innen einen Katalog sehen und welchen. Sie finden die Einstellung in der System-Administration unter:<br>
`Administration > Module > Katalog > Tab "Einstellungen"`

Unter Modul "Katalog" stehen drei Optionen zur Wahl: "Kein Katalog", "Katalog V1" und "Katalog V2". Je nach Wahl erscheinen unterschiedliche weitere Tabs.

Bei einer neuen Installation ist der Katalog V2 voreingestellt, der Katalog V1 samt seiner Katalogverwaltung ist ausgeschaltet. Bei einem Update aus einer älteren Version bleibt die vorhandene Einstellung bestehen. [:octicons-tag-16:{ title="ab Release 21.0 (OO-9562)" }](https://track.frentix.com/issue/OO-9562)

Ist der [Katalog V2](#config_catalog_v2) aktiviert, erscheinen zusätzliche Einstellungen: die Auswahl der [Taxonomie](Modules_Taxonomy.de.md) für den Katalog, die Option "Taxonomie bearbeitbar von" mit der Rolle Lernressourcenverwalter:in, der Schalter "Sortierung nach Priorität" und der Schalter [Web-Katalog](#config_web-catalog).

Der Schalter "Sortierung nach Priorität" blendet in den Auflistungen des Katalogs einen Sortier-Button ein. Sein Standardkriterium "Relevanz" ordnet die Angebote zuerst nach ihrer Priorität, dann nach Beginndatum, Enddatum und Titel. Die Wirkung beschreibt die Seite [Katalog 2.0: Sortierung/Reihenfolge](../../manual_user/area_modules/catalog2.0_sort_offers.de.md#sorting_microsites_by_priority). [:octicons-tag-16:{ title="ab Release 20.2 (OO-9039)" }](https://track.frentix.com/issue/OO-9039)

![Markierter Schalter Sortierung nach Priorität bei aktivem Katalog V2, Web-Katalog eingeschaltet](assets/modules_catalog_tab_settings_v2_de.png){ class="shadow lightbox" title="Tab Einstellungen im Modul Katalog" }

### Migration von Katalog V1 zu V2 [:octicons-tag-16:{ title="ab Release 17.0 (OO-6148)" }](https://track.frentix.com/issue/OO-6148) {: #migration_v1_v2}

Wer vom Katalog V1 auf den Katalog V2 umstellt, muss die bestehende Katalogstruktur nicht neu aufbauen. Solange die Migration noch nicht gelaufen ist, zeigt der Tab "Einstellungen" bei aktivem Katalog V2 unterhalb der Einstellungen einen zweiten Abschnitt mit dem Titel "Migration". Er besteht aus einem Erklärtext, der die zu überführenden Objekte aufzählt, und dem Button "Migration starten".

Der Button öffnet den Bestätigungsdialog "Katalog 2.0 Migration" mit der Frage "Wollen Sie die Migration wirklich starten?" und den Buttons "Ja" und "Nein". Nach "Ja" überführt OpenOlat im Hintergrund:

- Die Katalogstruktur wird zu einer neuen Taxonomie: Titel, Kurztitel und Beschreibung des Katalogs werden zur Taxonomie, jede Kategorie zu einer Taxonomieebene. Die Taxonomie erscheint danach im Tab "Einstellungen" unter "Taxonomie" und in der System-Administration unter `Administration > Module > Taxonomie`.
- Titel, Kurztitel und Beschreibungen der Unterkategorien stehen auf den neu gestalteten Unterseiten.
- Katalogbilder werden als rechteckige Kacheln im Format 2:1 dargestellt; die Form lässt sich im Tab "Layout" ändern.
- Das Bild der obersten Katalogebene wird zum Hintergrundbild des Headers der Startseite.
- Auf der Startseite entstehen Launcher: ein Launcher "Taxonomieebene" für die neue Taxonomie, ein Launcher "Statischer Text" mit der Beschreibung der obersten Katalogebene und, falls Lernressourcen direkt auf der obersten Ebene lagen, ein Launcher "Ausgewählte Lernressourcen" mit diesen Lernressourcen.
- Im Tab "Filter" wird der Filter für die Taxonomieebenen angelegt, falls er noch fehlt.

Während die Migration läuft, ersetzt der Hinweis "Die Migration wurde gestartet." den Button. Nach Abschluss verschwindet der Abschnitt "Migration" dauerhaft; die Migration lässt sich nur einmal ausführen.

[Zum Seitenanfang ^](#modul_catalog)

---


## Konfiguration des Katalogs V1 {: #config_catalog_v1}

Wer mit dem Katalog V1 arbeitet, legt im Tab "Konfiguration" fest, wo der Katalog erscheint und wie neue Kategorien und Einträge eingereiht werden. Der Tab erscheint, sobald im Tab "Einstellungen" der Katalog V1 gewählt ist:

- **Katalog in eigenem Bereich:** Der Katalog erscheint als eigener [Bereich](../../manual_user/area_modules/index.de.md) in der Hauptnavigation.
- **Mehrere Einträge zusammen hinzufügen:** Beim Hinzufügen von Lernressourcen zu einer Kategorie lassen sich mehrere Lernressourcen auf einmal auswählen.
- **Neue Kategorien hinzufügen** und **Neue Einträge hinzufügen:** Diese Auswahllisten legen fest, wo neue Kategorien und neue Einträge eingereiht werden. "Automatische Sortierung - Alphabetisch" sortiert sie alphabetisch, "Manuelle Sortierung - Am Anfang" und "Manuelle Sortierung - Am Ende" setzen sie an den Anfang oder ans Ende. Bei manueller Sortierung lässt sich die Reihenfolge danach von Hand ändern. Eine einzelne Kategorie kann in ihren eigenen Einstellungen von diesem Standard abweichen.

[Zum Seitenanfang ^](#modul_catalog)

---


## Konfiguration des Katalogs V2 {: #config_catalog_v2}

### Tab Startseite {: #tab_start_page}

Was Personen auf der Startseite des Katalogs zuerst sehen, stellen Sie im Tab "Startseite" aus Launchern zusammen. Launcher sind die konfigurierbaren Abschnitte der Startseite, zum Beispiel eine Reihe mit den zuletzt veröffentlichten Kursen. Mit "Launcher hinzufügen" wählen Sie den Launchertyp.

Welche Inhalte ein Launcher zeigt, wählt OpenOlat automatisch nach dem Launchertyp aus. Die verfügbaren Launchertypen sind nachstehend beschrieben. Standardmässig ist ein Launcher vom Typ "Zuletzt veröffentlicht" aktiviert.

Allen Launchern kann ein Name in verschiedenen Sprachen gegeben werden. Der Name erscheint dann als Kopfzeile über den Kacheln. Launcher können auch nur für spezifische Organisationen freigegeben werden. Wählen Sie dazu "Einschränkung auf Organisationen". Ausserdem kann separat bestimmt werden, ob ein Launcher im internen und/oder externen Katalog angezeigt wird.

![Dropdown-Menü Launcher hinzufügen mit allen verfügbaren Launchertypen, darunter eine Liste mit drei bereits konfigurierten Launchern](assets/modules_catalog_tab_settings_add_launcher_v1_de.png){ class="shadow lightbox" title="Tab Startseite im Modul Katalog" }


#### Launchertyp "Statischer Text"

In diesem Launcher kann manuell statischer Text hinzugefügt werden.


#### Launchertyp "Beliebte Kurse"

Die Reihenfolge der Angebote in diesem Launcher wird durch die Anzahl der Klicks auf Kursbausteine während der letzten 28 Tage bestimmt. Dabei werden nur Kurse mit Status "Publiziert" berücksichtigt.


#### Launchertyp "Zuletzt veröffentlicht"

Die Angebote sind nach Veröffentlichungsdatum geordnet.


#### Launchertyp "Zufallsgenerator"

In diesem Launcher angezeigte Angebote werden in zufälliger Reihenfolge angezeigt.


#### Launchertyp "Taxonomieebene"

Taxonomie-Launcher nutzen die Fachbereiche des Katalogs, um die verschiedenen Taxonomieebenen anzuzeigen. In einem Taxonomie-Launcher werden keine Kurse und Lernressourcen direkt angezeigt, die angezeigten Taxonomieebenen entsprechen vielmehr Ordnern, in denen dann erst die Lernressourcen zu finden sind.

Klickt man in einem Taxonomie-Launcher auf eine der angezeigten Kategorien (Taxonomieebene), gelangt man auf eine Microsite. Hier werden alle Kurse angezeigt, die unter dieser Taxonomieebene eingeordnet wurden. Hat die Taxonomie darunter weitere Ebenen, werden auch diese angezeigt.

Die Angebote werden entsprechend der definierten Taxonomieebene automatisch ausgewählt und dann alphabetisch geordnet angezeigt.

Beim Konfigurieren dieses Launchers wählen Sie über das Feld "Typ" [:octicons-tag-16:{ title="ab Release 21.0 (OO-9431)" }](https://track.frentix.com/issue/OO-9431){:target="_blank"}, worauf sich der Launcher bezieht:

* **Taxonomie:** Auswahl einer Taxonomie aus den für den Katalog verfügbaren Taxonomien.
* **Taxonomieebene:** Auswahl einer bestimmten Taxonomieebene.


#### Launchertyp "Ausgewählte Lernressourcen"

Die manuell hinzugefügten Lernressourcen können durch Klick auf Doppelpfeile vor den Einträgen geordnet werden.


#### Launchertyp "Ausgewählte Durchführungen"

Die manuell hinzugefügten Durchführungen können durch Klick auf Doppelpfeile vor den Einträgen geordnet werden.

[Zum Seitenanfang ^](#modul_catalog)

---


### Tab Filter [:octicons-tag-16:{ title="ab Release 17.2 (OO-6326)" }](https://track.frentix.com/issue/OO-6326) {: #tab_filter}

Damit Personen in einer langen Angebotsliste schnell das Passende finden, verfeinern sie die Liste mit Filtern oder der Suche. Im Tab "Filter" legen Sie fest, welche Filter auf den Microsites und der Suchergebnisseite zur Wahl stehen. Filter können z.B. Fachbereiche, Taxonomieebene, Angebotsart, Durchführungsformat, Semester, Lizenz, Hauptsprache, Lernressourcentyp, Autor usw. sein.

### Tab Layout {: #tab_layout}

Dieser Tab beinhaltet alles, was das Erscheinungsbild des Katalogs V2 angeht. Man kann den Anzeigetitel des Katalogs anpassen und ein Hintergrundbild für den Header der Startseite auswählen.

Unter "Kacheln Taxonomieebenen Launcher" wählen Sie die Form der Kacheln der Microsites.

Unter "Angezeigte Informationen in Karte" wählen Sie, welche Angaben aus den Metadaten auf den Karten der Startseite erscheinen. Die Metadaten müssen in der jeweiligen Lernressource unter `Einstellungen > Metadaten` ausgefüllt werden.


![Header mit Titel Katalog und Hintergrundbild-Upload (1324 x 240 px, maximal 2.0 MB), Formwahl der Taxonomiekacheln und Checkliste der Karteninformationen](assets/modules_catalog_tab_layout_v1_de.png){ class="shadow lightbox" title="Tab Layout im Modul Katalog" }

[Zum Seitenanfang ^](#modul_catalog)

---


### Verwalten des Kataloges [:octicons-tag-16:{ title="ab Release 17.1 (OO-6201)" }](https://track.frentix.com/issue/OO-6201) {: #v2_admin}

Der Katalog V2 ist nach den Fachbereichen einer Taxonomie gegliedert. Wer diese Gliederung pflegt, öffnet sie auf der Startseite des Katalogs mit dem Link "Katalog-Verwaltung". Den Link sehen Administrator:innen und Personen mit dem Verwaltungsrecht für einen Fachbereich. Personen mit der Rolle [Lernressourcenverwalter:in](../../manual_user/basic_concepts/Roles_Rights.de.md) sehen ihn, wenn im Tab "Einstellungen" unter "Taxonomie bearbeitbar von" die Rolle Lernressourcenverwalter:in gewählt ist. Voraussetzung ist in jedem Fall das eingeschaltete [Modul Taxonomie](Modules_Taxonomy.de.md). In der Katalog-Verwaltung wählen Sie die aktuelle Taxonomie, erstellen und importieren neue Taxonomieebenen und löschen Ebenen.

Das Löschen der Ebenen löscht nur die Verschlagwortung, keine verknüpften Lernressourcen. Ist diese gelöscht, taucht eine Lernressource nicht mehr im Katalog auf.

!!! warning "Achtung"

    Die Fachbereiche, Verschlagwortung, Taxonomie die man als Lernressourcenverwalter:in bearbeiten kann, kann auch andere Bereiche betreffen, in denen die Taxonomie benutzt wird. Diese können sein: ePortfolio Einträge, Curriculum Einträge, Dokumentenpool.

![Liste der Fachbereiche mit Kennzeichen, Erstelldatum und Anzahl Unterebenen](assets/modules_catalog_management2_v1_de.png){ class="shadow lightbox" title="Seite Katalog-Verwaltung" }

Das Recht zur Verwaltung eines Katalog- bzw. Fachbereichteils kann verschiedenen Personen gegeben werden. Initial vergeben Administrator:innen dieses Recht. Wählen Sie den gewünschten (Teil-)Fachbereich und dann den Tab "Verwaltung". [:octicons-tag-16:{ title="ab Release 20.1 (OO-8544)" }](https://track.frentix.com/issue/OO-8544)

![Tab Verwaltung und Button Verwalter:in hinzufügen hervorgehoben, keine Verwalter:innen eingetragen](assets/modules_catalog_management4_v1_de.png){ class="shadow lightbox" title="Taxonomieebene Ski Jumping in der Katalog-Verwaltung" }


Für Benutzer:innen mit diesem Recht gilt:

- **Bearbeiten:** Sie können Elemente innerhalb der Taxonomieebenen bearbeiten, verschieben, löschen oder neue Unterebenen erstellen.
- **Vererbung:** Wer auf einer höheren Ebene Rechte hat (z. B. auf Institutsebene), darf automatisch auch die darunter liegenden Ebenen (z.B. Studiengänge) bearbeiten.
- **Weitergabe:** Diese Rechte können von oben nach unten weitergegeben werden.<br>
Beispiel: Eine Administrator:in gibt einer Person die Rechte für eine Taxonomieebene darunter (z.B. Fakultät). Diese Person kann dann selbst anderen innerhalb dieser Fakultät ähnliche Rechte geben: auch für untergeordnete Bereiche.

Benutzer:innen mit diesem Recht können nicht:

- Taxonomien erstellen / bearbeiten / löschen
- Ebenentypen erstellen / bearbeiten / löschen
- Ziel-, Kredit- und Dozentenkompetenzen erstellen / bearbeiten / löschen

[Zum Seitenanfang ^](#modul_catalog)

---


### Erstellung von passendem Bildmaterial für den Katalog {: #pictures_for_the_catalog}

Damit Bilder im Katalog nicht an der falschen Stelle beschnitten werden, wählen Sie Grösse und Ausschnitt passend zu ihrem Platz. Die folgenden Abschnitte nennen die Bildgrössen und zeigen, was OpenOlat bei anderen Dimensionen tut. Die Schemata legen Sie im Grafikprogramm als Richtlinie über Ihr Bild, um den passenden Ausschnitt zu wählen.

#### Hintergrundbilder

Für die Hintergründe der Taxonomieunterseiten sowie der Startseite werden Bilddimensionen von 1324 x 240 px empfohlen, die maximale Dateigrösse für den Upload beträgt 2.0 MB. Ist das Bild höher als 240 px, nimmt OpenOlat einen passenden Ausschnitt aus der Mitte. Das Hintergrundbild einer Taxonomieebene laden Sie in der Katalog-Verwaltung bei der Ebene im Tab "Metadaten" im Feld "Hintergrund Bild" hoch. Das Hintergrundbild für die Startseite finden Sie im Tab "Layout".

So wählt OpenOlat den Ausschnitt bei kleineren Bildgrössen:

![Vergleich der Kachelgrössen auf Mobile und Laptop: Teaser-Bilder 240x120 px, Kursbilder 570x380 px](assets/catalog_cropping.png){ class="shadow lightbox" title="Bildausschnitte im Katalog auf Mobile und Laptop" }

**Hintergrund für den Start**

![Schnittmaske für das Hintergrundbild: Vollbild 1324x240 px, Mobile-Ausschnitt 340x240 px, Laptop-Ausschnitt 1024x240 px, Textzone Suche und Titel ca. 500x60 px](assets/catalog_background_start.png){ class="shadow lightbox" title="Hintergrundbild der Startseite" }

**Hintergrund für die Taxonomieebenen**

![Schnittmaske für das Taxonomie-Hintergrundbild: Vollbild 1324x240 px, Mobile-Ausschnitt 340x240 px, Laptop-Ausschnitt 1024x240 px, halbtransparenter Textbalken oben links](assets/catalog_background_taxonomy.png){ class="shadow lightbox" title="Hintergrundbild einer Taxonomieebene" }

#### Taxonomie-Launcher-Bilder

Ob die Kacheln eines Taxonomie-Launchers rechteckig oder quadratisch sind, legen Sie im Tab "Layout" unter "Kacheln Taxonomieebenen Launcher" fest. Rechteckige Kacheln haben ein Seitenverhältnis von 2,4 zu 1, die besten Resultate ergibt ein Bild mit 240 x 100 px. Quadratische Kacheln haben ein Seitenverhältnis von 1 zu 1. Das Bild einer Taxonomieebene laden Sie in der Katalog-Verwaltung bei der Ebene im Tab "Metadaten" im Feld "Teaser Bild" hoch. Über dem unteren Rand des Bildes liegt ein halbtransparenter Balken mit dem Titel der Ebene.

**Rechteckig**

![Schema des rechteckigen Teasers mit halbtransparentem Textbalken am unteren Rand](assets/catalog_taxteaser.png){ class="shadow lightbox" title="Rechteckige Kachel einer Taxonomieebene" }

**Quadratisch**

![Schema des quadratischen Teasers mit halbtransparentem Textbalken am unteren Rand](assets/catalog_taxteaser_square.png){ class="shadow lightbox" title="Quadratische Kachel einer Taxonomieebene" }

#### Kursbilder

Kursbilder legen Sie direkt im Kurs fest. Sie sollten die Dimensionen 570 x 380 px nicht überschreiten, sonst nimmt OpenOlat auch hier einen passenden Ausschnitt aus der Mitte.

![Schema des Kursbilds mit den empfohlenen Massen 570x380 px](assets/catalog_course.png){ class="shadow lightbox" title="Kursbild im Katalog" }

[Zum Seitenanfang ^](#modul_catalog)

---

## Konfiguration des Web-Katalogs [:octicons-tag-16:{ title="ab Release 20.0 (OO-8002)" }](https://track.frentix.com/issue/OO-8002) {: #config_web-catalog}

Wurde im Tab "Einstellungen" der Katalog V2 gewählt, steht als weitere Option die Aktivierung des Web-Katalogs zur Auswahl.

Der Web-Katalog ist ein nach aussen gespiegelter Katalog, auf den auch Personen zugreifen können, die noch nicht in OpenOlat registriert sind. Deshalb kann auch ein Link auf der Login-Seite eingerichtet werden, so dass der Web-Katalog ohne Login aufgerufen werden kann. Erst bei Buchung eines Kurses werden die Besucher:innen dann durch den Registrierungsprozess geführt.

Der Web-Katalog kann auch vorübergehend deaktiviert werden.

![Markierte Schalter Web-Katalog, Web-Katalog vorübergehend deaktiviert und Link auf Login-Seite bei aktiviertem Katalog V2](assets/modules_catalog_web-catalog_v1_de.png){ class="shadow lightbox" title="Tab Einstellungen im Modul Katalog" }

[Zum Seitenanfang ^](#modul_catalog)


---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Modul Taxonomie](Modules_Taxonomy.de.md)<br>
[Katalog 2.0: Sortierung/Reihenfolge](../../manual_user/area_modules/catalog2.0_sort_offers.de.md)<br>
[Bereiche und Module](../../manual_user/area_modules/index.de.md)<br>
[Rollen und Rechte: Übersicht](../../manual_user/basic_concepts/Roles_Rights.de.md)

**Weiterführend**<br>
[Katalog 2.0: Übersicht](../../manual_user/area_modules/catalog2.0.de.md)<br>
[Modul Lernressource](Modules_Learning_Resource.de.md)

[Zum Seitenanfang ^](#modul_catalog)


