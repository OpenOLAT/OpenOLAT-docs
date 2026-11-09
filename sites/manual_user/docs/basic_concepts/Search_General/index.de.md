# :o_icon_o_icon_search: Allgemeines zur Suche {: #search_general}

Was eine Suche findet, hängt davon ab, wo Sie sie starten. Je nach Ausgangspunkt

* sucht OpenOlat nur in einem bestimmten Bereich
* sucht OpenOlat nur nach bestimmten Objekttypen
* arbeitet die Suche mit einem anderen Suchverfahren

:octicons-device-camera-video-24: **Video-Einführung**: [Suchfunktion](<https://www.youtube.com/embed/GlUCyVl11ic>){:target="_blank"}

[Globale Suche >](../Search_Global.de.md)

[Lokale Suche >](../Search_Local.de.md)

[Personensuche >](../Search_Person.de.md)

[Suche in Kursen >](../Search_in_Course.de.md)

[Suche im File Hub >](../Search_in_FileHub.de.md)

---

## Volltextsuche [:octicons-tag-16:{ title="ab Release 20.1 (OO-8767)" }](https://track.frentix.com/issue/OO-8767) {: #full_text_search}

Mit der Volltextsuche finden Sie einen Begriff in ganz OpenOlat, auch im Text von Dokumenten. Sie sucht in den Inhalten von Kursen, Gruppen und Lernressourcen, beispielsweise in Forumsbeiträgen, Wiki-Seiten und in Dateien aus Ordnern. Die globale Suche arbeitet mit der Volltextsuche: Klicken Sie oben rechts in der Hauptnavigation auf das Lupen-Symbol, geben Sie einen Suchbegriff ein und bestätigen Sie mit der Eingabetaste. Die Treffer erscheinen im Dialog "Volltextsuche". Die Volltextsuche erfasst die Dateiformate PDF, HTML, TXT, Word, PowerPoint und Excel. Personendaten wie Profile oder Visitenkarten indexiert sie nicht.

Das Lupen-Symbol erscheint, wenn die Suche für Ihre OpenOlat-Instanz eingeschaltet ist, siehe [Globale Suche](../Search_Global.de.md#activation).

Liegt ein Treffer in einem Kurs, nennt die Zeile "in:" unter seinem Titel den Kurs als Fundort. Mit "mehr Details..." unter einem Treffer klappen Sie weitere Angaben auf, etwa Autor:in, letzte Änderung, Typ und Beschreibung. Über der Trefferliste blendet der Link "Ohne Suchbegriffe" die Textausschnitte mit den hervorgehobenen Suchbegriffen aus, der Link "Mit Suchbegriffen" blendet sie wieder ein.

![Trefferliste im Dialog Volltextsuche zum Suchbegriff Handbuch, markiert ist ein Treffer, dessen Zeile in: den Kurs als Fundort nennt](../assets/search_general_full_text_results_v1_de.png){ class="shadow lightbox" title="Dialog Volltextsuche · 2026.11.06" }

!!! info "Wichtig"

    Sie finden über die Volltextsuche immer nur diejenigen Kursinhalte, auf die Sie eine Zugriffsberechtigung haben.

Nur innerhalb eines Kurses suchen Sie mit der Kurssuche in der Toolbar des Kurses, siehe [Suche in einem Kurs](../Search_in_Course.de.md).

[zum Seitenanfang ^](#search_general)

---

## Erweiterte Suche {: #advanced_search}

Liefert die Volltextsuche zu viele Treffer, verfeinern Sie die Suche mit der erweiterten Suche. Sie öffnen sie im Dialog "Volltextsuche" mit dem Link "Erweiterte Suche" unter dem Suchfeld.

![Suchfeld im Dialog Volltextsuche und direkt darunter der Link Erweiterte Suche, beide markiert](../assets/search_general_advanced_search_link_v1_de.png){ class="shadow lightbox" title="Dialog Volltextsuche · 2026.11.06" }

![Formular der erweiterten Suche mit allen Feldern von Volltextsuche bis Metadaten, ausgefüllt sind Volltextsuche und Titel](../assets/search_general_advanced_search_form_v1_de.png){ class="shadow lightbox" title="Erweiterte Suche im Dialog Volltextsuche · 2026.11.06" }

In der erweiterten Suche stehen die Felder "Volltextsuche", "Autor:in", "Titel", "Beschreibung", "Erstellungsdatum", "Letzte Änderung", "Dokumententyp", "Lizenz" und "Metadaten" zur Verfügung. Das Feld "Lizenz" erscheint, wenn auf Ihrer OpenOlat-Instanz Lizenzen eingeschaltet sind. Im Feld "Dokumententyp" wählen Sie einen oder mehrere Typen aus, zum Beispiel "PDF-Datei" oder "Forum". Steht dort "alle", sucht die erweiterte Suche in allen Typen.

Die Suchfelder sind mit dem booleschen AND-Operator verknüpft. Füllen Sie zum Beispiel die Felder "Titel" und "Autor:in" aus, findet die Suche nur Dokumente, die beide Begriffe im jeweiligen Feld enthalten.

Ausnahme: Das Feld "Volltextsuche" sucht über alle Felder.

Aus der Ergebnisliste können Sie direkt auf den Lerninhalt mit dem gefundenen Suchbegriff springen.

Mit dem Link "Einfache Suche" unter dem Formular wechseln Sie zurück zum einzelnen Suchfeld.

[zum Seitenanfang ^](#search_general)

---

## Massensuche [:octicons-tag-16:{ title="ab Release 15.4 (OO-5233)" }](https://track.frentix.com/issue/OO-5233) {: #bulk_search}

Wenn Sie viele Personen auf einmal suchen, etwa mit einer Liste von E-Mail-Adressen aus einem Office-Dokument, schalten Sie auf die Massensuche um. Manche Suchformulare bieten dafür den Link "Massensuche". Statt des Suchformulars mit einzelnen Eingabefeldern erscheint dann ein einzelnes grosses Feld. Dort fügen Sie die Werte aus der Zwischenablage ein, einen pro Zeile, und klicken auf "Suchen". Mit dem Link "Suchformular" wechseln Sie zurück.

![Markierter Link Massensuche neben dem Titel Kontosuche: Suchformular](../assets/search_general_bulk_search1_v2_de.png){ class="shadow lightbox" title="Kontosuche in der Benutzerverwaltung · 2026.10.22" }

![Grosses Eingabefeld mit Zeilennummern für mehrere Anmeldenamen, E-Mail-Adressen oder Institutionsnummern und der Link Suchformular zum Zurückschalten](../assets/search_general_bulk_search2_v2_de.png){ class="shadow lightbox" title="Massensuche in der Benutzerverwaltung · 2026.10.22" }

[zum Seitenanfang ^](#search_general)

---

## Suche zurücksetzen [:octicons-tag-16:{ title="ab Release 21.1 (OO-9627)" }](https://track.frentix.com/issue/OO-9627) {: #search_reset}

Einen Suchbegriff entfernen Sie mit einem Klick, ohne das Feld von Hand zu leeren. Sobald im Suchfeld etwas steht, erscheint rechts im Feld eine runde Schaltfläche mit einem Kreuz und dem Tooltip "Suche zurücksetzen". Ein Klick darauf leert das Feld.

Was danach geschieht, hängt vom Ort des Suchfelds ab:

* **In Tabellen** zeigt die Tabelle sofort wieder die Einträge ohne Einschränkung durch den Suchbegriff.
* **Im grossen Suchfeld auf den Einstiegsseiten von Coaching und Course Planner** leert der Klick nur das Feld. Eine neue Suche startet erst, wenn Sie wieder auf "Suchen" klicken oder die Eingabetaste drücken.
* **Im grossen Suchfeld des Katalogs** leert der Klick ebenfalls nur das Feld, solange noch keine Suche gelaufen ist. Stehen darunter bereits Suchergebnisse, zeigt der Katalog sofort wieder die Angebote ohne Einschränkung durch den Suchbegriff.

[zum Seitenanfang ^](#search_general)

---

## Suchsyntax {: #syntax}

Mit der folgenden Syntax grenzen Sie Ihre Suchanfrage genauer ein.

**Einzelne Begriffe**, z.B. _OpenOlat_

**Mehrere Begriffe** im Suchfeld sind immer mit dem ODER-Operator verknüpft.

**Suche mittels Wildcards (Platzhalter):** Um nach bestimmten Wortfragmenten zu suchen, verwenden Sie Wildcards.

  * Das Fragezeichen in einem Suchbegriff steht für einen beliebigen, einzelnen Buchstaben. Mit der Sucheingabe _te?t_ finden Sie zum Beispiel alle Dokumente, die die Wörter "test", "text" usw. enthalten.
  * Der Stern in einem Suchbegriff steht für eine beliebige Anzahl von beliebigen Buchstaben. Mit der Sucheingabe _Test*_ finden Sie zum Beispiel alle Dokumente, die Wörter enthalten, die mit "Test" beginnen. Der Stern kann auch innerhalb eines Suchbegriffes stehen: _Te*t_

**Erweiterte Suche:** In der erweiterten Suche sind die verschiedenen Suchfelder mit dem AND-Operator verknüpft.

[zum Seitenanfang ^](#search_general)

---

## Metadaten {: #metadata}

Metadaten helfen, ein Dokument zu erkennen und in der Suche zu finden. Metadaten oder _Metainformationen_ sind Daten, die Informationen über Merkmale anderer Daten enthalten, aber nicht diese Daten selbst. Sie beschreiben eine Datei mit ergänzenden Informationen wie zum Beispiel einem Titel, dem Urheber oder dem Herausgeber. So ist besser erkennbar, um was für ein Dokument es sich handelt. Das ist besonders nützlich, wenn der Titel eines Dokuments nicht in den Dateinamen passt, weil er zu lang ist oder spezielle Zeichen enthält.

Sie können jede Datei und auch ganze Lernressourcen mit Metadaten versehen. Die Metadaten sind optional und müssen nicht ausgefüllt werden. Sie orientieren sich am [Dublin Core Simple Standard](https://de.wikipedia.org/wiki/Dublin_Core). Einige Metadaten lassen sich nicht ändern: der Name der Person, die das Dokument hochgeladen hat, die Grösse des Dokuments, der Zeitpunkt, zu dem das Dokument hochgeladen wurde, und der Dateityp. Informationen wie z.B. den ursprünglichen Verfasser, den Titel, eine Beschreibung, die Quelle oder die Sprache können Sie manuell eingeben.

Die Volltextsuche indexiert die Metadaten. Sie finden Dokumente deshalb auch über die Begriffe, die in ihren Metadaten stehen.

**Datei sperren:** Wählen Sie in den Metadaten einer Datei beim Feld "Gesperrt" die Option "Gesperrt", damit andere Benutzer:innen die Datei weder überschreiben noch löschen oder verschieben können. Gesperrte Dateien tragen in der Dateiliste in der Spalte "Dateistatus" die Markierung "Gesperrt" mit einem Schloss. Für Ordner gibt es diese Option nicht.

![Dateiliste eines Ordners, bei der gesperrten Datei ist in der Spalte Dateistatus die Markierung Gesperrt mit Schloss markiert](../assets/search_general_folder_locked_file_v1_de.png){ class="shadow lightbox" title="Dateiliste eines Ordners · 2026.11.03" }

Das Feld "Externer Link zu dieser Ressource" in den Metadaten zeigt einen Link, mit dem Sie auch ausserhalb von OpenOlat direkt auf die Datei verlinken.

**Anzahl Ansichten:** Das Feld "Anzahl Ansichten" zeigt, wie oft eine Datei aus einem Ordner heruntergeladen wurde. Trotz des Namens zählt OpenOlat Downloads, nicht die Anzeige im Browser. Die Zahl steigt um 1, wenn jemand die Datei mit "Herunterladen" speichert, sie in einer ZIP-Datei mit anderen Dateien herunterlädt, sie über WebDAV öffnet oder auf den Dateinamen klickt und die Datei dabei heruntergeladen wird. Öffnet sich die Datei beim Klick dagegen im Browser oder in einem Editor, zum Beispiel ein PDF oder ein Word-Dokument, bleibt die Zahl gleich.

OpenOlat zählt jeden Abruf, nicht jede Person: Lädt dieselbe Person eine Datei dreimal herunter, steigt die Zahl um drei, und auch Downloads von Besitzer:innen und Betreuer:innen zählen mit. Wann und von wem eine Datei heruntergeladen wurde, zeigt das Feld nicht. Lesen Sie die Zahl deshalb als groben Hinweis, nicht als Nutzungsauswertung. Das Feld sehen alle, die die Metadaten einer Datei öffnen können, auch Teilnehmer:innen; sie erhalten die Metadaten in einer Nur-Lese-Ansicht. Wie oft Teilnehmende einen Kursbaustein aufgerufen haben, zeigen die [Kursstatistiken](../../learningresources/Statistics_Course.de.md).

![Vier Wege erhöhen die Anzahl Ansichten um 1: Herunterladen, als ZIP herunterladen, Abruf über WebDAV, Klick auf einen Dateinamen, der herunterlädt; Öffnen im Viewer zählt nicht](../assets/folder_metadata_number_of_views_v1_de.svg){ class="shadow lightbox" title="Was die Anzahl Ansichten erhöht · 2026.11.03" }

!!! info "Wichtig"

    Ob ein Klick auf den Dateinamen die Datei herunterlädt, hängt vom Dateiformat und von der Konfiguration der Instanz ab. HTML-Dateien werden zum Beispiel heruntergeladen, wenn die Sicherheitsfunktion ["Dateidownload in Ordner erzwingen"](../../../manual_admin/administration/Login_Security.de.md#files) eingeschaltet ist.

[zum Seitenanfang ^](#search_general)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Globale Suche >](../Search_Global.de.md)<br>
[Lokale Suche >](../Search_Local.de.md)<br>
[Personensuche >](../Search_Person.de.md)<br>
[Suche in einem Kurs >](../Search_in_Course.de.md)<br>
[Suche im File Hub >](../Search_in_FileHub.de.md)<br>
[Dublin Core (Wikipedia) >](https://de.wikipedia.org/wiki/Dublin_Core)<br>
[Kursstatistiken >](../../learningresources/Statistics_Course.de.md)<br>
[Sicherheit >](../../../manual_admin/administration/Login_Security.de.md)

**Weiterführend**<br>
[Kontosuche >](../../../manual_admin/usermanagement/Search_Users.de.md)<br>
[Coaching - Personensuche >](../../area_modules/Coaching_User_Search.de.md)<br>
[Katalog 2.0: Übersicht >](../../area_modules/catalog2.0/index.de.md)<br>
[Course Planner: Übersicht >](../../area_modules/Course_Planner/index.de.md)

**youtube**<br>
[Suchfunktion](<https://www.youtube.com/embed/GlUCyVl11ic>)

[Zum Seitenanfang ^](#search_general)
