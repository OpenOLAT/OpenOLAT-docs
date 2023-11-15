# Modules: Taxonomie

!!! info "Was ist eine Taxonomie?"

    Im OpenOlat ist eine Taxonomie eine hierarchische Verschlagwortung,
    üblicherweise mit einem Kompetenzansatz.

    Taxonomie kann in mehreren OpenOlat Bereichen aktiviert und eingesetzt werden:

    * [Dokumentenpool](Modules_Document_pool.de.md)
    * [Fragenpool](../../manual_user/area_modules/Question_Bank.de.md)
    * [ePortfolio](eAssessment_ePortfolio.de.md)
    * Verknüpfung mit Lernressourcen

 Die Verwendung der Taxonomie in OpenOlat wird laufend erweitert.

 Zum einen können also Taxonomiestrukturen beispielsweise in Form einer
 Fächer-, Handlungsfeld- oder Kompetenzstruktur abgebildet werden. Zum anderen
 können den Benutzern Kompetenzen zugeordnet werden, welche ihnen den Zugriff
 auf die Taxonomie erlauben.

Beispiel einer Taxonomiestruktur nach Fächern für den Dokumentenpool:

![Taxonomie Struktur](assets/Taxonomie_Struktur_DE.png){ class="shadow lightbox" }

Direkt auf der Übersichtsseite kann eine neue Taxonomie erstellt werden.
Sofern Sie im Fragenpool bereits eine Fachbereichsstruktur angelegt haben,
wird diese hier mit dem Titel "Question Pool" angezeigt.

Es können mehrere Taxonomiestrukturen erstellt und für verschiedene Zwecke
(Fragenpool oder Dokumentenpool) aktiviert werden.

![Taxonomie](assets/Taxonomy overview DE.png){ class="shadow lightbox" }

Lässt man sich eine Taxonomie anzeigen gelangt man zur folgenden Übersicht:

![](assets/Tax Metatdata DE.png){ class="shadow lightbox" }

## Metadaten

Beim Erstellen werden die Metadaten Kennzeichen und Name, und falls gewünscht
die Beschreibung eingetragen. Diese Daten können anschliessend im Tab
"Metadaten" bearbeitet werden. Hier wird zudem automatisch eine ID erstellt
und sofern ein externes Verwaltungssystem die Ebenen angelegt hat, wird die
Externe ID erstellt.

## Ebenentypen

Ebenentypen werden gebraucht, um der Taxonomiestruktur eine Bedeutung zu
geben. So können beispielsweise die Ebenentypen Kompetenz → Handlungsfeld →
Fach erstellt und untereinander als Unterkategorien angelegt werden. Es ist
dabei nicht notwendig, dass ein Ebenentyp immer an derselben Stelle oder auf
demselben Leven der Taxonomiestruktur vorzufinden ist.

Zu Ebenentypen werden gewisse Konfigurationen hinzugefügt.

Im Tab "Ebenentypen" kann mit "Neuer Ebenentyp erstellen" ein neuer Typ
erstellt werden.

* **Kennzeichen:** ist eine  Kennung für die Taxonomieebene. Dieses Kennzeichen wird in der Tabelle im Tab "Taxonomie" in der Spalte "Ebenentyp" angezeigt. Wählen Sie ein eindeutiges und logisches Kennzeichen.
* **Anzeigename:** Der Anzeigename ist sprachabhängig und wird an unterschiedlichen Stellen verwendet: Katalog 2.0, Dokumentenpool, e-Portfolio
* **CSS class:** Sofern eine entsprechende css class im Theme hinterlegt ist, können Sie diese hier ausgewählen. Es können so nur Icons hinterlegt werden.
* **Sichtbar:** Hier wird definiert, ob alle Taxonomieebenen von diesem Typ sichtbar sein sollen.
* **Kompetenzen:** Wenn aktiviert, steht dieser Ebenentyp als Kompetenz zur Verfügung und kann z.B. zur kompetenzbasierten Verschlagwortung in ePortfolio-Einträgen genutzt werden.
* **Leistungsnachweise:** Hier können Taxonomieebenen mit diesem Leveltyp für die Gruppierung von Leistungsnachweisen freigeschaltet werden.
* **Beschreibung:** Eine kurze Beschreibung des Ebenentyps (optional)
* **Sub types:** Aus den bereits bestehenden Ebenentypen kann nun ein Untertyp ausgewählt werden. So ist es möglich, eine hierarchische Struktur zu schaffen. Diese wird dann beim Erstellen der Taxonomieebenen sichtbar.

![Übersicht über die Taxonomy leveltypen](assets/taxonomy-leveltypes.de.jpg){ class="shadow lightbox" }

## Taxonomie

In diesem Tab werden nun die einzelnen Taxonomieebenen erstellt, importiert, exportiert und angezeigt.

### Taxonomie erstellen

Beim Erstellen werden folgende Angaben benötigt:

* **Pfad**: Mit dem Pfad kann direkt die Position der neuen Taxonomieebene definiert werden.
* **Kennzeichen**: Als Kennzeichen kann wiederum ein Kürzel für die Ebene verwendet werden.
* **Typ**: Beim Typ wird nun der zuvor definierte Ebenentyp ausgewählt. 
* **Sortierung**: ::octicons-tag-24: *aktuell Beta Feature* Hier können Zahlen eingetragen werden, nach dem die Taxonomien sortiert werden. ( z.B. 1, 2, 3, 4, .. / 01, 02,03,04,...)
* **Teaser Bild**
* **Hintergrund bild**
* **Anzeigename**: Der Anzeigename ist sprachabhängig und wird an unterschiedlichen Stellen verwendet: Katalog 2.0, Dokumentenpool, e-Portfolio.
* **Beschreibung**: Beschreibung der Taxonomieebene. Wird im Katalog unter der Ebene angezeigt.

![Taxonomie-Ebenen](assets/Taxebenen.png){ class="shadow lightbox" }

In der Übersicht ist nun die hierarchische Struktur sichtbar.

![Ausgeklappte Treetable der Taxonomie](assets/taxonomy-overview-hierarchy.de.jpg){ class="shadow lightbox" }

In der Detailansicht können anschliessend Kompetenzen hinzugefügt werden. So
erhalten Benutzer die Zugriffsrechte für die einzelnen Taxonomieebenen. 

Es werden 4 verschiedene Kompetenzen unterschieden. Diese werden im Folgenden
kurz umrissen:

* **Dozieren**: Ein Benutzer mit einer Dozierkompetenz ist in dieser Kompetenz befähigt. Meist bedeutet dies, er hat ein gewisses Fachwissen, das er weitergeben kann. Die Dozierkompetenz wird dem Benutzer entweder manuell oder durch ein externes Verwaltungssystem hinzugefügt. Diese Kompetenz steuert den Zugriff sowohl im [Dokumentenpool](Modules_Document_pool.de.md) als auch im Fragenpool.
* **Verwalten**: Benutzer können für gewisse Bereiche in der Taxonomie eine verwaltende Funktion haben. Dabei müssen Sie nicht zwingend auch die Dozierkompetenz haben. Diese Kompetenz wird vor allem im Fragenpool benutzt.
* **Haben**: Diese Kompetenz wird momentan im OpenOlat noch nicht verwendet. Diese Kompetenz sollen zukünftig Lernende durch eine Lernaktivität im OpenOlat (z.B. absolvierter Test) erhalten. Diese Kompetenz wird auch ein Verfallsdatum haben.
* **Ziel**: Diese Kompetenz wird momentan im OpenOlat noch nicht verwendet. Ein Lernender hat ein Ziel, das er erreichen möchte. Sein Ziel ist es, diese Kompetenz zu erwerben.

![taxonomy overview](assets/taxonomy-overview.de.jpg){ class="shadow lightbox" }

### Taxonomie exportieren

![Taxonomie exportieren](assets/Taxonomie_exportieren.png)

Die Taxonomie wird mit Klick auf den Menüpunkt als .zip Archiv heruntergeladen. Darin enthalten ist eine EXCEL-Tabelle mit der hierarchischen Struktur der Taxonomieebenen und eine Ordnerstruktur (media/ebene1/background;media/ebene1/teaser;) mit Teaser- und Hintergrundbildern der Taxonomie, wenn welche vorhanden sind. (mehr unter -> [Katalog 2.0](../../manual_user/area_modules/catalog2.0.de.md))

### Taxonomie importieren

**Daten Einfügen**

![Schritt eins des Wizards - taxonomie importieren](assets/taxonomy-import-overview.de.jpg){ class="shadow lightbox" }

Man kann die verschiedene Teile der Taxonomie importieren. Möglich ist, nur die Struktur zu importieren (**A**), Bilder zu einer vorhandenen Struktur hinzufügen (**B**) oder eine neue Struktur inkl. Bilder importieren (**A+B**).

**Änderungen überprüfen**

![Taxonomieimportdialog Schritt 2 Überprüfung](assets/taxonomy-import-step2.de.jpg){ class="shadow lightbox" }

Nach dem Import werden im zweiten Schritt die Taxonomie und die hinzugefügten Bilder nochmals überprüft. Ein Icon zeigt an, ob die Taxonomieebene bereits vorhanden ist und mit den Dateien und hochgeladen Informationen ergänzt und überschrieben werden soll.

**Updatemodus auswählen**

![Taxonomieimportdialog Schritt 3 - Überschreiben](assets/taxonomy-import-step3.de.jpg){ class="shadow lightbox" }

Hier kann man entscheiden, ob man die existierenden Taxonomieebenen überschreiben lassen will oder nur neue Taxonomieebenen hinzufügen. Falls man Medien hinzufügen möchte, _müssen_ hier die Änderungen überschrieben werden.

### Nur Taxonomie Struktur importieren/hinzufügen

1. Laden Sie die aktuelle Taxonomie herunter oder nutzen Sie die Vorlage unter dem entsprechenden Punkt

![Tabellenvorlage-taxonomiestruktur](assets/taxonomystructure-import.jpg){ class="shadow lightbox" }

2. In der Excel fügen Sie die neuen Ebenen hinzu oder verändern bestehende. Der Pfad muss vollständig angegeben werden. Ist dieser fehlerhaft, können gewisse Ebenen nicht importiert werden.
 Hat man verschieden Sprachen in OpenOlat aktiviert und benutzt den [Katalog 2.0](../../manual_user/area_modules/catalog2.0.de.md), ist es ratsam Anzeigename und Beschreibung sprachabhängig zu gestalten. Zusätzliche Sprachen fügen Sie hinzu, indem Sie die Spalten "Länderkürzel", "Anzeigename" & "Beschreibung" kopieren, diese damit hinten anhängt und ein neues, existierendes Länderkürzel, Anzeigename + Beschreibung für jede Taxonomieebene ergänzt.

3. Die geänderte Tabelle wird _ohne_ die Kopfzeile markiert und in das Eingabefeld kopiert. Im Schritt "Änderungen überprüfen" werden die Zellen auf Richtigkeit überprüft. Bei Fehlern erscheinen die Fehlermeldungen direkt am Eingabefeld.

### Nur Hintergrund-/Teaserbild importieren/hinzufügen

![finderimage of fodlerstructure provided for media images](assets/taxonomy-media-folder-structure.jpg)

1. Will man Hintergrundbilder zu einer existierenden Taxonomie hinzufügen, sollte man im ersten Schritt diejenige exportieren. 
2. Das Archiv entzippen und dort im Ordner "media" die betreffenden Bilder hineinlegen. 
3. Wieder das gesamte Archiv zippen und unter Absatz B im Wizard einfügen.

Alternativ ist es auch möglich, die vorhandene Vorlagen unter den jeweiligen Links herunterzuladen und diese entsprechend anzupassen.


## Lost+Found

Hier werden alle gelöschten Elemente aus dem Tab "Taxonomie" abgelegt. Momentan können diese jedoch nicht wiederhergestellt werden.