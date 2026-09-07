# Persönliche Werkzeuge: File Hub {: #file_hub}

![Menü der persönlichen Werkzeuge mit dem Eintrag File Hub, dem Einstieg zum globalen Dateibrowser für alle zugänglichen Ordner in OpenOlat](assets/pers_menu_file_hub_v3_de.png){ class="aside-right lightbox"}

![Symbol File Hub](assets/icon_file_hub.png)



Der File Hub ist der **globale Dateibrowser** von OpenOlat. Er listet **alle in OpenOlat vorhandenen Ordner** auf: Kursordner, Gruppenordner, Archivordner und weitere.

Der File Hub zeigt nur Ordner an, auf die die eingeloggte Person Zugriffsberechtigung hat.

![Sechs Ablageorte auf der Startseite des File Hub: Persönliche Dateien, Gruppen, Kurse, Dokumentenpool, Kursarchiv und Ressourcenordner, darüber das Suchfeld; File Hub in den persönlichen Werkzeugen](assets/pers_menu_file_hub_storage_locations_v1_de.png){ class="shadow lightbox"}

[Zum Seitenanfang ^](#file_hub)

---


## Merkmale des File Hubs [:octicons-tag-16:{ title="ab Release 19.0.0 (OO-7700)" }](https://track.frentix.com/issue/OO-7700) {: #features}

* **Multi-File-Upload** per Drag & Drop
* Werden im File Hub Dateien an einen anderen Ort übernommen, werden sie jeweils **kopiert**.<br>
(Im Unterschied zum [Media Center](../personal_menu/Media_Center.de.md): Dort werden z.B. Logos, AGB und ähnliche Dateien zentral verwaltet, aktualisiert und allen Autor:innen zur Verfügung gestellt. Deshalb werden die Dateien dort verlinkt.)
* Es werden nur Ordner im File Hub angezeigt, auf die die aktuell eingeloggte Person **Zugriffsberechtigungen** hat.

Siehe auch [File Hub (Basiskonzept)](../basic_concepts/File_Hub_Concept.de.md)

[Zum Seitenanfang ^](#file_hub)

---


## Wo wird der File Hub verwendet? {: #where_used}

Die Ordner und Dateien werden im File Hub entsprechend den individuellen, persönlichen Berechtigungen angezeigt. Deshalb gehört der File Hub zu den **persönlichen Werkzeugen** und ist im **persönlichen Menü** zu finden.

Der File Hub wird aber auch an vielen weiteren Stellen angezeigt, wenn **aus Dateien ausgewählt** werden soll.

Zur **Anzeige eines Ordnerinhalts** finden Sie den File Hub zum Beispiel in der Kursadministration: `Kurs > Administration > Dateien`.

[Zum Seitenanfang ^](#file_hub)

---


## Umschaltung Kachelansicht - Listenansicht {: #views}

Die Ansicht des File Hubs können Sie zwischen Kachel- und Listenansicht umschalten. In beiden Ansichten finden Sie die weiteren Optionen (Datei öffnen, Datei herunterladen) im Menü mit den drei Punkten.

![Kachelansicht eines Kursordners im File Hub mit markiertem Umschalter für die Kachelansicht und geöffnetem Drei-Punkte-Menü mit den Optionen Öffnen und Herunterladen](assets/pers_menu_file_hub_tiles_v1_de.png){ class="shadow lightbox" }

![Listenansicht desselben Ordners mit markiertem Umschalter für die Listenansicht und markiertem Drei-Punkte-Menü am Zeilenende; Spalten Titel, Erstellt von, Typ, Grösse und Dateistatus](assets/pers_menu_file_hub_list_v1_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#file_hub)

---


## Allgemeines zum Ordner {: #general_info}

Ordner dienen dazu, Dokumente abzulegen, Dateien zum Download bereitzustellen oder Dateien mit anderen Benutzer:innen auszutauschen.

Wenn Sie über Lese- **und** Schreibrechte verfügen, die Ihnen in Kursen oder Gruppen von den Betreuer:innen erst zugewiesen werden müssen, können Sie in diesen Ordnern Dateien hochladen, erstellen, kopieren, verschieben und löschen. In den persönlichen Ordnern haben Sie automatisch Schreib- und Leserechte.

Dateien, die Sie in OpenOlat hochladen wollen, sollten nur folgende Bestandteile im Dateinamen enthalten:

a-z, A-Z, 0-9, sowie "-", ".", "_" oder Leerschläge

Zudem können Sie Dateien zippen und entzippen. Alle Aktionen lassen sich auf einzelne oder mehrere ausgewählte Dateien und Ordner anwenden. Wenn Sie viele Dateien auf einmal hochladen wollen, gibt es zwei Wege.

Zum einen können Sie Ihre Dateien auf Ihrem Rechner zippen, die ZIP-Datei hochladen und im OpenOlat-Ordner entzippen. Zum anderen können Sie mehrere Dateien per WebDAV übertragen und organisieren. Alle Ordner sind WebDAV-fähig, d.h. Ordner in OpenOlat stehen Ihnen als gewöhnliches Netzlaufwerk zur Verfügung, über welches Sie Dateien einfach kopieren, verschieben und löschen können. Weitere Infos finden Sie im Kapitel "[Einsatz von WebDAV](../basic_concepts/Using_WebDAV.de.md)".

!!! info "Wichtig"

    Damit der Zugriff via WebDAV auf OpenOlat funktioniert, muss WebDAV von Ihren OpenOlat-Administrator:innen aktiviert werden.

[Zum Seitenanfang ^](#file_hub)

---


## Quota {: #quota}

Der Speicherplatz pro Ordner ist begrenzt. Administrator:innen legen den zur Verfügung stehenden Speicherplatz fest. Die Grundeinstellung für den privaten und öffentlichen Ordner liegt bei 200 MB. Für die Erhöhung dieser Quota ist Ihre jeweilige OpenOlat-Supportstelle zuständig. Wenden Sie sich gegebenenfalls an die zuständigen Ansprechpersonen.

[Zum Seitenanfang ^](#file_hub)

---


## Persönliche Dateien {: #personal_files}

Im File Hub finden Benutzer:innen auch ihre "Persönlichen Dateien". Diese unterteilen sich in die Ordner "private" und "public".

_Private_

Hier können Benutzer:innen alle unterstützten Dateien hochladen. Dieser Ordner dient als Zwischenspeicher und ermöglicht den Zugriff auf Dokumente von verschiedenen Rechnern. OpenOlat funktioniert hier wie eine Cloud.

Zudem werden im privaten Ordner Dateien abgelegt, die über die Datenarchivierung gespeichert werden.

_Public_

In diesem Ordner können Dateien abgelegt werden, die anderen OpenOlat-Benutzer:innen zur Verfügung stehen sollen. Der Ordner "public" ist in der Visitenkarte sichtbar. In den persönlichen Werkzeugen kann unter "Personensuche" nach der Person gesucht werden, die ein Dokument dort hochgeladen hat. Dies vereinfacht den Datenaustausch zwischen OpenOlat-Benutzer:innen.

In OpenOlat gibt es mehrere Varianten von Ordnern. Neben den beiden Ordnern im persönlichen Menü existieren folgende Ordner-Varianten mit unterschiedlicher Ausrichtung:

* [Ablageordner >](../learningresources/Storage_folder.de.md) (in Kursen)
* [Kursbaustein Ordner >](../learningresources/Course_Element_Folder.de.md) (in Kursen)
* [Teilnehmer:innen Ordner >](../learningresources/Course_Element_Participant_Folder.de.md) (in Kursen)
* [Ressourcenordner >](../learningresources/index.de.md#resource_folder) (Lernressource)
* [Werkzeug: Ordner >](../groups/Using_Group_Tools.de.md) (in Gruppen, ähnlich dem Kursbaustein Ordner in Kursen)

[Zum Seitenanfang ^](#file_hub)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Media Center >](../personal_menu/Media_Center.de.md)<br>
[Konzept des File Hub >](../basic_concepts/File_Hub_Concept.de.md)<br>
[Einsatz von WebDAV >](../basic_concepts/Using_WebDAV.de.md)<br>
[Ablageordner >](../learningresources/Storage_folder.de.md)<br>
[Kursbaustein "Ordner" >](../learningresources/Course_Element_Folder.de.md)<br>
[Kursbaustein "Teilnehmer:innen Ordner" >](../learningresources/Course_Element_Participant_Folder.de.md)<br>
[Lernressourcen >](../learningresources/index.de.md)<br>
[Gruppenwerkzeuge nutzen >](../groups/Using_Group_Tools.de.md)

[Zum Seitenanfang ^](#file_hub)
