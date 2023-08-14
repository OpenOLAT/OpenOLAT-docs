# Wie kann ich effizient viele Gruppen auf einmal erstellen?

??? abstract "Ziel und Inhalt dieser Anleitung"

    Die Erstellung einer grossen Anzahl Gruppen ist im Standardprozess aufwändig.
    Der hier beschriebene Beispiel zeigt, wie viele Gruppen mit unterschiedlichen Namen effizient erstellt werden können.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [ ] Anfänger:innen [x] Fortgeschrittene  [x] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * Erfahrung mit der Erstellung von Gruppen

---

## Use Case und Zielsetzung

Use Case von Karin Niffeler, Uni Zürich:

* In einem Kurs mit 600 Teilnehmer:innen sollen ca. 400 Gruppen gebildet werden.
* Die Gruppen sollen den Kursbaustein "Gruppenaufgabe" nutzen.
* Die Kursteilnehmer:innen bilden innerhalb eines Kurses selbst Gruppen mit jeweils 1 oder 2 Mitgliedern.
* Die Gruppen müssen voneinander unterscheidbar sein.


## Der Standardprozess

Als Kursbesitzer:in können Sie im Kurs Gruppen erstellen:<br>
**Administration > Mitgliederverwaltung > Gruppen > Gruppen erstellen**<br>Diese Gruppen können in den Kursbausteinen verwendet werden.

Mit Hilfe des Kursbausteins "Einschreibung" können Kursteilnehmer:innen sich dann selbst in eine dieser Gruppe einschreiben.

Unter dem Reiter "Gruppen" können auch die Kursteilnehmer:innen Gruppen erstellen und Mitglieder hinzufügen. Auch diese Gruppen können später mit einem Kurs verknüpft werden.


## Problem

Bei vielen Gruppen gibt es für den/die Kursbesitzer:in viel Aufwand um alles aufzusetzen.


## Lösung Schritt 1

Es ist möglich, mehrere Gruppen auf einmal zu erstellen: Im PopUp "Neue Gruppe erstellen" kann man mehrere Gruppennamen gleichzeitig eingeben, wenn sie durch ein Komma getrennt werden.

![many_groups_mehrere_neue_Gruppen_erstellen_v1_de.png](assets/many_groups_mehrere_neue_Gruppen_erstellen_v1_de.png){ class="shadow lightbox" }

<h3>Weiterhin bestehendes Problem:</h3>
Der/die Kursbesitzer:in muss immer noch die einzelnen Gruppennamen selbst definieren.
Auf diese Art 400 Gruppen zu erstellen ist sehr aufwändig.


## Lösung Schritt 2 mit einer Excel-Datei

Die kommaseparierte Liste mit den Gruppennamen kann mit Hilfe einer Excel-Datei erzeugt werden.

Ideal ist, wenn die Gruppennamen auch ein Prefix und/oder Suffix haben können.
Z.B. "DE Gruppe-001", "DE Gruppe-002", "DE Gruppe-003", "EN group-001", "EN group-002", "EN group-003"

1. Zuerst müssen in Excel die Gruppennamen erzeugt werden.
2. Die Gruppennamen werden dann zu einer kommaseparierten Textkette (String) zusammengefügt.
3. Die Textkette kann dann nach OpenOlat ins Feld "Name der Gruppe" kopiert werden.


<h3>1. Gruppennamen erzeugen</h3>

* Erstellen Sie ein neues Excel-Dokument.
* Definieren Sie alle Gruppennamen in Spalte A. Hier kann mit Prefixen und/oder Suffixen gearbeitet werden. Die Möglichkeiten von Excel können hier optimal verwendet werden um die Gruppennamen zu erzeugen.

<h3>2. Textkette erstellen</h3>

* In einer neuen Zelle in einer anderen Spalte fügen Sie die Formel hinzu:<br>
**=TEXTVERKETTEN(", ";WAHR;A1:A400)**<br>
(Englische Excel-Version: **= TEXTJOIN(", ",TRUE,A1:A400)**)
* Durch diesen Befehl wird in dieser Zelle eine Zeichenkette (String) mit den kommaseparierten Gruppennamen erzeugt.
* Kopieren Sie diesen String (Zeichenkette) in die Zwischenablage.

![many_groups_excel1_v1_de.png](assets/many_groups_excel1_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Ist die Zelle markiert, kopiert man durch Ctrl+C und Ctrl+V die **Formel**. Um die erzeugte **Zeichenkette** in die Zwischenablage zu kopieren, müssen Sie die **Inhalte einfügen** (Shift+Ctrl+V).


<h3>3. Übertrag in den OpenOlat-Kurs</h3>

* Öffnen Sie die Mitgliederverwaltung des Kurses: <br>
Administration > Mitgliederverwaltung > Gruppen > Button "Gruppe erstellen"

![many_groups_gruppen_erstellen1_v1_de.png](assets/many_groups_gruppen_erstellen1_v1_de.png){ class="shadow lightbox" }

* Fügen Sie im PopUp "Neue Gruppe erstellen" im Feld "Name der Gruppe" die Textkette (String) ein.

![many_groups_gruppen_erstellen2_v1_de.png](assets/many_groups_gruppen_erstellen2_v1_de.png){ class="shadow lightbox" }

* Falls bei allen Gruppen Eigenschaften gleich gelten sollen, definieren Sie evtl. noch eine Beschreibung, die vorgesehene Anzahl der Teilnehmer, usw.

* Mit Klick auf "Fertigstellen" werden alle Gruppen erstellt.
