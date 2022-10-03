# Katalog 2.0

:octicons-tag-24: Release 17.0 

Der Katalog 2.0 gliedert sich in unterschiedliche Bereiche auf.

!!! note "Unterschiede zum Katalog v.10 vor 17.0"

    Katalog 2.0 besitzt keine manuelle Sortierung auf Kursebene.
    Dieser Katalog ist ein dynamischer Katalog. D.h. alles, was die Fachbereiche und ein Angebot besitzt wird __automatisch__ im Katalog angezeigt und aggregiert.

## Bestandteile des Katalogs

### Startseite

Die Startseite ist durch Kategorie-Launcher anpassbar und bietet ein prominentes Sucheingabefeld. Zusätzlich anpassbar ist auch das Hintergrundbild. Der Titel ist durch ein i18n auch anpassbar. In der Suche kann nach Lernressourcen gesucht werden. Indexiert ist dabei der Titel, Teasertext, Taxonomie.

### Launcher

Launcher sind die konfigurierbaren Zeilen der Startseite. Diese können in der Administration beliebig hinzugefügt in der Reihenfolge verändert werden. Standardmässig ist ein Launcher vom Typ "Zuletzt hinzugefügt" aktiviert. Die Launcher kommen in 3 Typen: Statischer Text, Statisch (Manuell auswählen), Taxonomie-Ebenen.
Allen Launcher kann ich einen sprachabhängigen Namen geben. Dieser Name erscheint dann als Headline über den Kacheln.
Die Launcher können auch nur für spezifische Organisationen freigegeben werden.

### Taxonomie Launcher

Taxonomie Launcher nutzen die Katalogfachbereichsstruktur, um die verschiedenen Taxonomielevel als Baum anzuzeigen. 

### (Taxonomie-) Microsite

Klickt man auf einen Level bei einem Launcher kommt man auf die Taxonomie Microsite. Hier werden alle Kurse angezeigt, die unter diesem Level eingeordnet wurden. Hat die Fachbereichstaxonomie mehrere Level in diesem Strang werden die weiteren Level angezeigt.

Man kann die Kursliste weiter durch Filter oder Suche verfeinern.

### Suchergebnisseite & Filter

**Suchergebnissseite**
Bei einer Suche kommt man auf diese Seite. Hier lassen sich durch verschiedene Filter die Suche verfeinern.

**Filter**
Die Filter der Suchergebnissseite lassen sich unter `Administration > Module > Katalog > Filter` einstellen. Hier kann gewählt werden, welche Filter für Teilnehmer verfügbar sein sollen.

## Einrichten und Freigeben neuer Kurse für den Katalog 2.0

### Vorraussetzungen

* Der Katalog 2.0 muss aktiviert sein und eine Taxonomie sollte angelegt werden.
* Mindestens 1 Kurs muss existieren.

### Startseite einrichten

Die Startseite kann unter `Administration > Module > Katalog > Startseite` eingerichtet werden. Hier gibt es die Option rechts oben Launcher hinzuzufügen, um die Startseite anzupassen und zu erweitern

### Kurs einem Fachbereich hinzufügen

Auf `Autorenbereich > Kurs > Metadaten` unter "Subjects/Katalog" die gewünschten Bereiche auswählen, in welchen der Katalog erscheinen soll und speichern.

### Angebot erstellen

Auf `Autorenbereich > Kurs > Freigabe` Angebote aktivieren und ein Angebot erstellen. Dies für die gewünschten Organisations Einheiten freigeben.

## Migration von V1.0 zu V2.0

Existiert schon ein Katalog inklusivie Struktur, kann dieser einfach in die neue Version migriert werden.
Bei Wechsel auf die neue Version, erscheint ein Dialog, der die die Migration anschiebt.

Die folgenden Objekte werden in den neuen Katalog übertragen:

* Titel & Kurztitel
* Katalogbilder werden konvertiert. Als neues Bildformat wird eine rechteckige Darstellung mit dem Format 2:1 empfohlen.
* Die Katalogstruktur wird als neue Katalogtaxonomie angelegt und ist dann unter Abteilungen/Katalog verfügbar.
* Unterkategorietitel, Kurztitel & Beschreibungen sind auf neu gestalteten Unterseiten verfügbar.
