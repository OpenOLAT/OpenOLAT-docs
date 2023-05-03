# Volltextsuche

![](assets/search.png)

:octicons-device-camera-video-24: **Video-Einführung**: [Suchfunktion](<https://www.youtube.com/embed/GlUCyVl11ic>){:target="_blank”}

Die Suche ist nur dann sichtbar und nutzbar, wenn sie in der Administration
aktiviert ist. Sollte dies bei Ihnen nicht der Fall sein, wenden Sie sich
bitte an den System Administrator Ihrer OpenOlat Instanz.

Das Suchfeld für die Volltextsuche ist oben rechts in der Menüzeile platziert.
Die Volltextsuche sucht in verschiedenen Kurs- und Gruppeninhalten nach
Suchbegriffen, beispielsweise auch in Forumsbeiträgen, PDF- und Word-Dateien.
Weiter können Sie auch nach Benutzern, nach Portfoliomappen und Artefakten
sowie nach Dokumenten in den [Benutzerordnern
](Personal_folders.de.md)suchen. Eine
Ausnahme ist der private Ordner, welcher nicht indexiert wird.

![](assets/generelle_Suche.png)

Sie finden über die Volltextsuche immer nur diejenigen Kursinhalte, auf die
Sie Zugriff haben.

## Erweiterte Suche

Um die Suche zu verfeinern, benutzen Sie die erweiterte Suche.

![](assets/Volltextsuche_erweitert.png)![](assets/Volltextsuche_erweitert2.png)

Im Modus _Erweiterte Suche_ können Sie Ihre Sucheingabe verfeinern. Beachten
Sie, dass die verschiedenen Suchfelder mit dem boolschen AND-Operator
verknüpft werden. D.h. wenn Sie zum Beispiel die Felder _Titel_ und _Autor_
ausfüllen, werden nur Dokumente gefunden, bei denen die Begriffe in den
jeweiligen Feldern gleichzeitig vorkommen.

Ausnahme: Das Feld Volltextsuche sucht über alle Felder.

Aus der Ergebnisliste können Sie direkt auf den Lerninhalt mit dem gefundenen
Suchbegriff springen.

!!! Info

    Neben der Volltextsuche über das gesamte OpenOlat gibt es auch eine
    [Kurssuche](../course_create/Course_Settings.de.md#Kurseinstellungen-Optionen), welche pro
    Kurs in der Toolbar aktiviert werden kann. Die Einstellung wird unter "Administration" -> "Einstellungen" im Tab "Toolbar" aktiviert. Die Kurssuche durchsucht nur den entsprechenden Kurs.

  

##  Suchsyntax {: #syntax}

Sie können Ihre Suchanfrage mit folgender Syntax modifizieren.  
  
**Einzelne Begriffe:** z.B. _OpenOlat_

 **Phrasen:** werden in doppelte Anführungszeichen gesetzt, z.B.
_"kohlensäurehaltiges Mineralwasser"_

 **Boolsche Operatoren:** Einzelne Begriffe sowie Phrasen können mittels
Boolschen Operatoren verknüpft werden. Achtung Boolsche Operatoren müssen mit
Grossbuchstaben geschrieben werden.

  *  **OR:** Wenn Sie keine Boolschen Operatoren zwischen Suchbegriffen verwenden, wird der OR-Operator verwendet. Z.B. _"Analyse des Wassers" Kalzium_ und _"Analyse des Wassers" OR Kalzium_ ergeben das gleiche Suchergebnis, nämlich alle Dokumente, die entweder "Analyse des Wassers" oder "Kalzium" enthalten.
  * **AND:** Mit dem AND-Operator finden Sie Dokumente, die alle Suchbegriffe enthalten. Z.B. _"Analyse des Wassers" AND "Kalzium"_ findet die Dokumente, die sowohl "Analyse des Wassers" wie auch "Kalzium" enthalten. 
  * **NOT:** Mit dem NOT-Operator können Sie Dokumente mit bestimmten Begriffen ausschliessen. Z.B. _"Analyse des Wassers" AND "Kalzium" NOT "Leitungswasser"_ findet die Dokumente, die "Analyse des Wassers" und "Kalzium", jedoch nicht "Leitungswasser" enthalten.

 **Suche mittels Wildcards:** Sie können zwischen zwei Arten von Wildcards
wählen, um nach bestimmten Wortfragmenten zu suchen.

  * Das Fragezeichen in einem Suchbegriff steht für einen beliebigen, einzelnen Buchstaben. Z.B. Mit der Sucheingabe _te?t_ finden Sie alle Dokumente, die die Wörter "test", "text" usw. enthalten.
  * Der Stern in einem Suchbegriff steht für eine beliebige Anzahl von beliebigen Buchstaben. Z.B. Mit der Sucheingabe _Test*_ finden Sie alle Dokumente, die Wörter enthalten, die mit "Test" beginnen. Der Stern kann auch innerhalb eines Suchbegriffes stehen: _Te*t_ ****

**Fuzzy-Suche:** Mittels der Tilde ~ können Sie nach Wörtern suchen, die
ähnlich in der Schreibweise sind. Z.B. finden Sie mit der Sucheingabe
_Traube~_ Dokumente, die Wörter wie "Trauma", "Glaube" oder "Taube" enthalten.

 **Sonderzeichen:** Die folgenden Zeichen sind Bestandteil der Suchsyntax in OpenOlat:

 **\+ - && | ! ( ) { } [ ] ^ " ~ * ? : \**

Wenn Ihre Sucheingabe eines dieser Zeichen enthält, müssen Sie es mittels dem
\ Zeichen (Backslash) maskieren. Z.B. Wenn Sie nach der Gleichung _{1+1}:2=?_
suchen, müssen Sie _\\{1\\+1\\}\:2=\?_ eingeben.

 **Suche in Feldern:** Um in verschiedenen Feldern zu suchen, können Sie
einerseits den Modus _Erweiterte Suche_ wählen, wo die verschiedenen
Suchfelder mit dem AND-Operator verknüpft werden. Anderseits können Sie mit
einer eigenen boolschen Verknüpfung in den jeweiligen Feldern suchen.
Verwenden Sie hierzu im Modus _Einfache Suche_ folgende Feldnamen:

  *  _title_ (=Titel)
  *  _description_ (=Beschreibung)
  *  _content_ (=Suche im Textkörper)
  *  _documenttype_ (=Dokumententyp)
  *  _filetype_ (=Dateityp)
  *  _author_ (=Autor) 
  * _created_ (=Erstellungsdatum) 
  * _changed_ (=Letzte Änderung)

Beispiel: _description:Kalzium_ sucht ausschliesslich im Feld _Beschreibung_.

Die vollständige Referenz der in OLAT verwendeten Suchsyntax finden Sie auf
der Webseite von [Apache
Lucene](http://lucene.apache.org/core/7_2_0/queryparser/org/apache/lucene/queryparser/classic/package-
summary.html#package.description) (Webseite in Englisch).

##  Metadaten {: #metadata}

Metadaten oder  _Metainformationen_  sind Daten, die Informationen über
Merkmale anderer Daten enthalten, aber nicht diese Daten selbst. Metadaten,
also Daten  **über**  Daten, beschreiben eine Datei mit ergänzenden
Informationen wie zum Beispiel einem Titel, dem Urheber oder den Herausgeber.
Sie sind dazu da, dass besser erkennbar wird, um was für ein Dokument es sich handelt. Dies ist besonders sinnvoll, wenn der Titel eines Dokumentes nicht in den Dateinamen geschrieben werden kann, weil dieser viel zu lange ist oder spezielle Zeichen enthält.

Jede Datei aber auch komplette Lernressourcen können mit Metadaten versehen werden. Die Metadaten sind optional und
müssen nicht ausgefüllt werden. Sie orientieren sich am [Dublin Core Simple
Standard](https://de.wikipedia.org/wiki/Dublin_Core). Einige Metadaten können
nicht verändert werden. Es sind dies der Name der Person die das Dokument
hochgeladen hat, die Grösse des Dokuments, der Zeitpunkt zu dem das Dokument
hochgeladen wurde und der Dateityp. Informationen wie z.B. den ursprünglichen
Verfasser, den Titel, eine Beschreibung, die Quelle oder die Sprache können
Sie manuell eingeben.

Die Metadaten werden von der Volltextsuche indexiert. Dies bedeutet, dass man
in der Suche nach den verschlagworteten Metadaten suchen kann und so die
relevanten Dokumente besser auffindet.

**Datei sperren:** In den Metadaten können Sie eine Datei als gesperrt
markieren. Gesperrte Dateien sind mit einem Schloss versehen und können von
anderen Benutzern nicht mehr überschrieben, gelöscht oder verschoben werden.
Diese Option ist für Ordner nicht vorhanden.

![](assets/Datei_gesperrt_DE_Detail.png)

Mit Hilfe des verfügbaren externen Links können Sie auch ausserhalb von
OpenOlat direkt auf eine bestimmte Datei verlinken.

