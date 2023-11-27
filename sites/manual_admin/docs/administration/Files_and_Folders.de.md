# Dateien und Ordner

In der Administration im Bereich "[Core Konfiguration](Core_functions.de.md)" können auch Einstellungen bezüglich
der Dateiein, inklusive Versionen und Quotas vorgenommen werden.

Im Tab Überblick erhalten Administratoren einen schnellen Gesamtüberblick über
die Anzahl und die Größe von OpenOlat Dateien, Versionen, gelöschten Dateien
und Miniaturansichten und können diesbezüglich Aktionen vornehmen.

## Versionen

Im **Tab "Versionen"** kann die maximale Anzahl von Versionen für eine Datei
definiert werden.

Bei eingeschalteter Versionierung werden Dateien nicht überschrieben, sondern
als neue Version (auch Revision genannt) angelegt. Ältere Versionen eines
Dokumentes können heruntergeladen und bei Bedarf wiederhergestellt werden.
Werden Dateien gelöscht, so erscheinen Sie in der Liste der gelöschten Dateien
und können wiederhergestellt werden. Ist die Versionierungsfunktion
eingeschaltet, so können Dateien auch gesperrt werden, z.B. wenn eine Person
an einem Dokument arbeitet und verhindern möchte, dass eine andere Person
zwischenzeitlich eine neue Version erstellt.

Die Versionierung ist in allen Ordnern des Systems vorhanden: persönliche
Ordner, Gruppenordner, Kursordner, Ressourcenordner und Kursbausteine
"Ordner".

## Quotas

Im Tab **"Quotas"** kann die maximale Speichergröße und das Upload-Limit für
bestimmte Pfade definiert und angepasst werden.

Folgende Standardwerte gelten systemweit:

Systemweite Quotas | Anwendungsbereich
---------|----------
::DEFAULT::BLOGSPODCASTS | Lernressourcen Blog und Podcast
::DEFAULT::COACHFOLDER | Betreuer-Ordner im Kurs
::DEFAULT::COURSEDOCUMENTS | KursTool "Dokumente" (Kursmenü)
::DEFAULT::COURSEFOLDERS | Kurs-Ablageordner (ohne Kurselement-Unterordner) und Ressourcenordner (Shared Folder)
::DEFAULT::GROUPS | Ordner in Gruppen
::DEFAULT::NODEFOLDERS | Kursbaustein "Ordner"
::DEFAULT::NODEPARTFOLDERS | Kursbaustein "Teilnehmer-Ordner"
::DEFAULT::POWERUSERS | Persönlicher Ordner von Autoren
::DEFAULT::REPOSITORY | Lernressourcen wie Content Package oder Tests
::DEFAULT::USERS | Persönlicher Ordner von Benutzern ohne zusätzliche Systemrechte

Es können auch individuelle Quotas ergänzt werden. Diese übersteuern den Standardwert und gelten beispielsweise nur für einen ganz bestimmten Kursordner oder den persönlichen Ordner eines ganz bestimmten Benutzers / einer bestimmten Benutzerin.

Spezifische Quotas | Anwendungsbereich
---------|----------
/course/101032323838456/coursefolder | Kursbaustein "Ordner" in einem bestimmten Kurs
/cts/folders/BusinessGroup/414156565 | Ordner in einer bestimmten Gruppen
/homes/mmusterfrau | Persönlicher Ordner von der Benutzerin M. Musterfrau

## Grosse Dateien

Im Tab "**Grosse Dateien**" können Administratoren gezielt nach grossen
Dateien suchen und sich weitere Details zu diesen Dateien anzeigen lassen.

## Gelöschte Dateien

Im Tab "**Gelöschte Dateien**" können von bestimmten Pfaden endgültig
gelöscht werden.

### Orphan Versionen löschen:

Alle Dokumente, welche manuell gelöscht werden oder für welche keine
Versionierung mehr zur Verfügung steht, werden in eine Art Papierkorb gelegt.
Von dort könnten sie wiederhergestellt werden, benötigen jedoch auch nach wie
vor dieselbe Speichermenge. Mit Orphan Versionen löschen wird dieser
Papierkorb gelöscht. Die Versionen können nicht mehr wiederhergestellt werden,
benötigen jedoch auch keinen Speicher mehr.  

### Versionen aufräumen:

Die Versionierung kann von der Anzahl her angepasst werden. Wird jetzt
beispielsweise von 5 Versionen auf 2 Versionen geändert, sind pro Dokument 3
Versionen überflüssig. Diese werden jedoch nicht direkt gelöscht. Wenn Sie die
Anzahl wieder auf 5 Versionen stellen, werden sie wieder sichtbar. Um jedoch
diese Versionen ganz zu löschen, klicken Sie auf Versionen aufräumen.
Anschliessend können die Versionen nicht mehr wiederhergestellt werden.

  

  

  

  

