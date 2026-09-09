# :o_icon_o_icon_search: Volltextsuche {: #full_text_search}

:octicons-device-camera-video-24: **Video-Einführung**: [Suchfunktion](<https://www.youtube.com/embed/GlUCyVl11ic>){:target="_blank"}

Die Suche ist nur dann sichtbar und nutzbar, wenn sie in der Administration aktiviert ist. Sollte dies bei Ihnen nicht der Fall sein, wenden Sie sich bitte an den System Administrator Ihrer OpenOlat Instanz.

Das Suchfeld für die Volltextsuche ist oben rechts in der Menüzeile platziert. Die Volltextsuche sucht in verschiedenen Kurs- und Gruppeninhalten nach Suchbegriffen, beispielsweise auch in Forumsbeiträgen, PDF- und Word-Dateien. Weiter können Sie auch nach Teilnehmenden, nach Portfoliomappen und Artefakten sowie nach Dokumenten in den [persönlichen Dateien](../personal_menu/File_Hub.de.md#personal_files) suchen. Eine Ausnahme ist der private Ordner, welcher nicht indexiert wird.

![Trefferliste zum Suchbegriff e-learning mit hervorgehobenen Fundstellen und Angabe des Fundorts je Treffer, im Dialog Volltextsuche](assets/generelle_Suche.png){ class="shadow lightbox" }

Sie finden über die Volltextsuche immer nur diejenigen Kursinhalte, auf die Sie Zugriff haben.

## Erweiterte Suche {: #advanced_search}

Um die Suche zu verfeinern, benutzen Sie die erweiterte Suche.

![Link Erweiterte Suche unterhalb des Suchfelds, im Dialog Volltextsuche](assets/full_text_search_advanced_link_DE.png){ class="shadow lightbox" }

![Formular der erweiterten Suche mit den Feldern Volltextsuche, Autor, Titel, Beschreibung, Erstellungsdatum, Letzte Änderung, Dokumententyp, Lizenz und Metadaten, im Dialog Volltextsuche](assets/full_text_search_advanced_DE.png){ class="shadow lightbox" }

Im Modus _Erweiterte Suche_ können Sie Ihre Sucheingabe verfeinern. Beachten Sie, dass die verschiedenen Suchfelder mit dem booleschen AND-Operator verknüpft werden. D.h. wenn Sie zum Beispiel die Felder _Titel_ und _Autor_ ausfüllen, werden nur Dokumente gefunden, bei denen die Begriffe in den jeweiligen Feldern gleichzeitig vorkommen.

Ausnahme: Das Feld Volltextsuche sucht über alle Felder.

Aus der Ergebnisliste können Sie direkt auf den Lerninhalt mit dem gefundenen Suchbegriff springen.

!!! info "Wichtig"

    Neben der Volltextsuche über das gesamte OpenOlat gibt es auch eine
    [Kurssuche](../learningresources/Course_Settings.de.md#toolbar), welche pro
    Kurs in der Toolbar aktiviert werden kann. Die Einstellung aktivieren Sie unter `Kurs > Administration > Einstellungen` im Tab "Toolbar". Die Kurssuche durchsucht nur den entsprechenden Kurs.

## Suchsyntax {: #syntax}

Sie können Ihre Suchanfrage mit folgender Syntax modifizieren.

**Einzelne Begriffe:** z.B. _OpenOlat_

**Mehrere Begriffe:** im Suchfeld sind immer mit dem ODER-Operator verknüpft

**Suche mittels Wildcards:** Um nach bestimmten Wortfragmenten zu suchen, können Wildcards verwendet werden.

  * Das Fragezeichen in einem Suchbegriff steht für einen beliebigen, einzelnen Buchstaben. Z.B. Mit der Sucheingabe _te?t_ finden Sie alle Dokumente, die die Wörter "test", "text" usw. enthalten.
  * Der Stern in einem Suchbegriff steht für eine beliebige Anzahl von beliebigen Buchstaben. Z.B. Mit der Sucheingabe _Test*_ finden Sie alle Dokumente, die Wörter enthalten, die mit "Test" beginnen. Der Stern kann auch innerhalb eines Suchbegriffes stehen: _Te*t_

**Erweiterte Suche:** Im Modus _Erweiterte Suche_ werden die verschiedenen Suchfelder mit dem AND-Operator verknüpft.

## Metadaten {: #metadata}

Metadaten oder  _Metainformationen_  sind Daten, die Informationen über Merkmale anderer Daten enthalten, aber nicht diese Daten selbst. Metadaten, also Daten **über**  Daten, beschreiben eine Datei mit ergänzenden Informationen wie zum Beispiel einem Titel, dem Urheber oder den Herausgeber. Sie sind dazu da, dass besser erkennbar wird, um was für ein Dokument es sich handelt. Dies ist besonders sinnvoll, wenn der Titel eines Dokumentes nicht in den Dateinamen geschrieben werden kann, weil dieser viel zu lange ist oder spezielle Zeichen enthält.

Jede Datei aber auch komplette Lernressourcen können mit Metadaten versehen werden. Die Metadaten sind optional und müssen nicht ausgefüllt werden. Sie orientieren sich am [Dublin Core Simple Standard](https://de.wikipedia.org/wiki/Dublin_Core). Einige Metadaten können nicht verändert werden. Es sind dies der Name der Person die das Dokument hochgeladen hat, die Grösse des Dokuments, der Zeitpunkt zu dem das Dokument hochgeladen wurde und der Dateityp. Informationen wie z.B. den ursprünglichen Verfasser, den Titel, eine Beschreibung, die Quelle oder die Sprache können Sie manuell eingeben.

Die Metadaten werden von der Volltextsuche indexiert. Dies bedeutet, dass man in der Suche nach den verschlagworteten Metadaten suchen kann und so die relevanten Dokumente besser auffindet.

**Datei sperren:** In den Metadaten können Sie eine Datei als gesperrt
markieren. Gesperrte Dateien sind mit einem Schloss versehen und können von anderen Teilnehmenden nicht mehr überschrieben, gelöscht oder verschoben werden. Diese Option ist für Ordner nicht vorhanden.

![Gesperrte Datei mit rot umrahmtem Schloss-Symbol in der Spalte Gesperrt, in der Dateiliste eines Ordners](assets/Datei_gesperrt_DE_Detail.png){ class="shadow lightbox" }

Mit Hilfe des verfügbaren externen Links können Sie auch ausserhalb von
OpenOlat direkt auf eine bestimmte Datei verlinken.

## Suchergebnisse {: #search_results}

In den eigenen Suchergebnissen erscheinen:

* Daten, die in Visitenkarten von Benutzer:innen freigegeben sind
* Daten / Dokumente aus “öffentlichen Ordnern” von Benutzer:innen
* Daten / Dokumente aus Kursen, in denen man selbst Mitglied ist und auf die man als Kursmitglied auch Zugriff hat
* Daten / Dokumente aus Kursen, die unter Einstellungen > Freigabe wie folgt konfiguriert sind: "Ohne Buchung" oder "Frei verfügbar"

## Weiterführende Informationen {: #further_information}

[Persönliche Dateien >](../personal_menu/File_Hub.de.md)<br>
[Kurssuche >](../learningresources/Course_Settings.de.md)<br>
[Dublin Core Simple Standard (Wikipedia) >](https://de.wikipedia.org/wiki/Dublin_Core)

**youtube**<br>
[Suchfunktion](<https://www.youtube.com/embed/GlUCyVl11ic>)

[zum Seitenanfang ^](#full_text_search)
