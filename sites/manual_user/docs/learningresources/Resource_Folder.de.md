# Ressourcenordner {: #resource_folder}

Ressourcenordner zählen in OpenOlat zu den Lernressourcen und werden im Autorenbereich erstellt. Sie können eigenständig oder verknüpft mit Kursen verwendet werden. 

Um neben den normalen Kursdateien auch kursübergreifende Dateien für die Kurserstellung verwenden zu können, sollte ein Ressourcenordner verwendet werden.

## Ressourcenordner im Kurs verwenden

Mit einem Ressourcenordner lassen sich Dateien (z. B. Inhalte, Informationen, Grafiken) zentral organisieren und in mehreren Kursen nutzen.

Um einen Ressourcenordner mit einem Kurs zu verbinden, wählen Sie im Kurs unter `Administration > Einstellungen > Optionen` den gewünschten Ressourcenordner aus oder erstellen einen neuen. Pro Kurs kann nur ein Ressourcenordner verknüpft werden.

Bei der Einbindung gibt es zwei Varianten: schreibgeschützt oder ohne Schreibschutz.

![Auswahl des Ressourcenordners und der Schreibschutz-Option im Tab "Optionen" der Kurseinstellungen](assets/resource_folder_select_v1_de.png){ class="shadow lightbox" }

**Schreibgeschützt**: Die Dateien werden nur referenziert. Im Kurs können sie weder verändert noch gelöscht oder ergänzt werden. Damit ist sichergestellt, dass alle Kurse stets dieselben aktuellen Dateien nutzen.

**Ohne Schreibschutz**: Kursbesitzer:innen können Dateien ändern, löschen oder neue hinzufügen. Diese Anpassungen werden direkt im Ressourcenordner übernommen und wirken sich damit auf alle verknüpften Kurse aus, auch wenn die betreffenden Personen keine Besitzer:innen des Ressourcenordners sind.

Überlegen Sie daher sorgfältig, ob der Schreibschutz aufgehoben werden soll.

### Hier findet man die Dateien des Ressourcenordners
Wurde ein Ressourcenordner mit dem Kurs verbunden, erscheint er in der Kurs-Administration unter "Dateien" als "**_sharedfolder**" mit allen Dateien, die im Ressourcenordner hinterlegt wurden. 

![Ordner "_sharedfolder" in der Dateiübersicht des Kurses](assets/sharedfolder_20.png){ class="shadow lightbox" }

![Dateiliste im Ordner "_sharedfolder" mit den Dateien des Ressourcenordners](assets/sharedfolder_20_b.png){ class="shadow lightbox" }

In der Standardeinstellung sind die Dateien des Ressourcenordners schreibgeschützt und können nicht verändert werden. 

### Zugriff auf die Dateien
Die Dateien des Ressourcenordners können genau wie alle anderen Dateien des Ablageordners eines Kurses verwendet und auch mit unterschiedlichen Kursbausteinen verknüpft werden. 

So könnten zentrale Dateien z.B. für einheitliche Kurslayouts verwendet, oder Dokumente über den Kursbaustein Dokument bereitgestellt oder Bilder im Kursbaustein "HTML-Seite" integriert werden usw. Immer dann, wenn innerhalb des Kurses Zugriff auf den Ablageordner besteht können auch die Dokumente des verknüpften Ressourcenordners über "_sharedfolder" verwendet werden. 


## Kursunabhängige Nutzung
Um den Ressourcenordner eigenständig zu verwenden, muss im Ressourcenordner unter `Administration > Einstellungen` im Tab "Freigabe" die eigenständige Verwendung aktiviert und die Freigabe weiter konfiguriert werden, z.B. frei für Gäste oder mit einem Passwort. Ferner muss der Ressourcenordner dann auch veröffentlicht werden. Bei einer Verbindung mit einem Kurs ist das nicht nötig.

Genauere Informationen finden Sie unter ["Zugangskonfiguration/Freigabe"](../learningresources/Access_configuration.de.md).

!!! note "Hinweis"

    Eine weitere Möglichkeit der unabhängigen Nutzung besteht über [WebDAV](../basic_concepts/Using_WebDAV.de.md). In der WebDAV-Ansicht werden neben Kursen und Gruppen auch die Sharedfolders, bei denen man Besitzer:in ist, angezeigt.

## Weiterführende Informationen {: #further_information}

[Kurseinstellungen - Tab Optionen >](Course_Settings_Options.de.md)<br>
[Wie kann ich dieselben Dateien in mehreren Kursen einsetzen? >](../../manual_how-to/multiple_use/multiple_use.de.md)<br>
[Ablageordner >](Storage_folder.de.md)<br>

[Zum Seitenanfang ^](#resource_folder)



