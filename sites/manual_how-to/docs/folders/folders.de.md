# Mit welchen Ordnern kann ich Dokumente anbieten? {: #folders}


??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie möchten Dokumente in OpenOlat ablegen oder ablegen lassen? Diese Seite zeigt ihnen, welchen Ordner Sie für welchen Zweck verwenden können.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)



OpenOlat kennt nicht „den einen" Ordner, sondern rund ein Dutzend Ordnertypen für unterschiedliche Zwecke, vom Kursmaterial über Abgaben bis zur kursübergreifenden Dateipflege. Diese Übersicht ordnet sie **aus Autor:innen-Sicht** 

- wozu jeder Ordnertyp dient,
- wo Sie ihn einrichten,
- wer Zugriff darauf hat 
- und wie Sie mit Dateien darin arbeiten.

Am Ende dieses Artikels finden Sie [Entscheidungshilfen](#decision_aid) und mögliche [Stolpersteine](#stumbling_stones).

---


## Ordnertypen nach Kontext

Jeder Ordnertyp gehört zu einem Kontext: 

- **Persönlich** — Persönlicher Ordner (darin befindet sich ein privater und ein öffentlicher Bereich).
- **Kurs** — Ablageordner · Kursbaustein „Ordner" · Teilnehmer:innen-Ordner · Ordner im Baustein „Aufgabe" · Betreuer:innen-Ordner · Kursarchiv.
- **Gruppe** — Gruppenordner (Zugriff ist an Gruppenmitgliedschaft gebunden)
- **Kursübergreifend** — Ressourcenordner (Shared Folder): einmal pflegen, überall aktuell.
- **Systemweit** — Dokumentenpool (mit Taxonomie und Kompetenzsteuerung)


---

## Auf einen Blick: Welcher Ordner wofür?

| Ordner | Zweck | Wo einrichten / öffnen | Sichtbar für | Upload durch TN | Kursübergreifend |
|--------|-------|------------------------|--------------|-----------------|------------------|
| **Kursbaustein „Ordner"** | Dateien zum Download bereitstellen; optional Sammel-Upload | Kurseditor → Baustein „Ordner" | alle Kursteilnehmenden | optional | nein |
| **Teilnehmer:innen-Ordner** | Abgabe & Rückgabe von Dateien je Teilnehmer:in | Kurseditor → Baustein „Teilnehmer:innen Ordner" | je TN nur eigener Ordner + Betreuende | ja | nein |
| **Ordner im Baustein „Aufgabe"** | Dateien im Aufgaben-Workflow (Abgabe, Rückgabe, Lösung …) | Kurseditor → Baustein „Aufgabe"/„Gruppenaufgabe" | nur innerhalb des Bausteins | ja | nein |
| **Betreuer:innen-Ordner** | Nur für Betreuende/Besitzende zugänglicher Ablagebereich | Kurs → Einstellungen → Optionen | nur Betreuer:innen & Besitzer:innen | nein | nein |
| **Ablageordner** | Hintergrund-Ablage aller im Kurs verwendeten Dateien | Kurs → Administration → Dateien | nur Kursbesitzer:innen (TN nur indirekt) | nein | nein |
| **Ressourcenordner** | Zentrale Dateien für mehrere Kurse (Shared Folder) | Autorenbereich + Kurs → Einstellungen → Optionen | je nach Kurs-/Freigabeberechtigung | nein | ja |
| **Gruppenordner** | Gemeinsamer Dateiaustausch in einer Gruppe | Gruppe → Werkzeuge → „Ordner" aktivieren | alle Gruppenmitglieder | ja | an Gruppe gebunden |
| **Persönlicher Ordner** | Individuelle Dateiablage (privat / öffentlich) | Persönliches Menü → File Hub | nur die Person selbst | — | personenbezogen |
| **Dokumentenpool** | Dokumentenverwaltung mit Taxonomie & Kompetenzen | Administration (Modul) + File Hub | kompetenz-/rechtegesteuert | — | systemweit |
| **Kursarchiv** | Archivierte Kurs-/Teilnehmerdaten (ZIP) | File Hub → „Kursarchiv" | Kursbesitzer:innen | — | nein |

[zum Seitenanfang ^](#folders)

---


## Zugriffswege {: #access_path}

Auf die Ordner kann von verschiedenen Stellen aus zugegriffen werden. Überlegen Sie, was beim geplanten Ordnerinhalt für Ihre Teilnehmer:innen Sinn macht.  

Zugriffsweg kursspezifisch:

- via Aufruf eines Kursbausteins
- via Administrationsmenü (als Autor:in oder Betreuer:in)
- via Icon in der Werkzeugleiste

Zugriffsweg kontextübergreifend, je nach Berechtigung:

- via FileHub
- via WebDAV


### Öffnen eines Ordners im Kurs

Wählen Sie im Kurs einen Kursbaustein "Ordner", "Teilnehmer:innen Ordner" oder Aufgabe.

### Öffnen eines Ordners in der Autor:innen oder Betreuer:innen-Rolle

Der Betreuer:innen Ordner ist in der Kursadministration zu finden, die nur den Kursbesitzer:innen und - betreuer:innen angezeigt wird. Ebenso befindet sich in der Kursadministration unter "Dateien" auch der Ablageordner zum Kurs.

### Öffnen via Icon in der Werkzeugleiste

Ein Dokumentenordner zu einem Kurs kann von Autor:innen oben in der Werkzeugleiste als Icopn angezeigt werden. 

### Öffnen via persönlichem Menü

Der persönliche Ordner (mit den Unterordnern privat und öffentlich) ist im persönlichen Menü zu finden.


### File Hub {: #file_hub}

*Ab Release 19 · globaler Dateibrowser*

Zentraler Einstiegspunkt im persönlichen Menü, der alle Ordner auflistet, auf die Sie berechtigt sind: Kurs-, Gruppen-, Archiv- und persönliche Ordner, Ressourcenordner und Dokumentenpool.

- **Öffnen:** Persönliches Menü; ausserdem Kurs → Administration → `Dateien`.
- **Merkmal:** Dateien werden beim Übernehmen **kopiert** (anders als das verlinkende Media Center).
- **Sichtbarkeit:** Nur berechtigte Ordner; die Berechtigung wird jeweils in der Quelle vergeben.
- **Komfort:** Multi-File-Upload per Drag & Drop.

### WebDAV {: #webdav}

*Netzlaufwerk-Zugriff*

Bindet OpenOlat-Ordner als Netzlaufwerk auf dem eigenen Rechner ein. Dies ist ideal, um ganze Ordnerstrukturen oder viele Dateien auf einmal zu übertragen.

- **Ordner:** `coursefolders`, `groupfolders`, `home`, `sharedfolders`.
- **Zugang:** WebDAV-Link + Benutzername/E-Mail + (WebDAV-)Passwort.
- **WebDAV-fähig:** Persönliche Dateien, Gruppen-, Ablage-, Baustein-„Ordner", Ressourcenordner.
- **Grenzen:** von OpenOlat-Administrator:innen eingestellte Quota; Dateinamen max. 100 Zeichen Länge; Umlaute in Ordnernamen sind meiden; > 50 MB sind unter Windows heikel.

[zum Seitenanfang ^](#folders)

---


## Bedienungsweisen, die in allen Ordnern gleich sind

Seit Release 19 nutzen alle Ordner dieselbe überarbeitete Komponente. Diese Funktionen finden Sie im Ablageordner, in Kurs- und Gruppenordnern, im Kursarchiv, in Bibliothek, Projekt und weiteren Bereichen.

- **Zwei Ansichten** — Hierarchisch mit Ordnern oder nur Dateien; zusätzlich Kachel- und Tabellenansicht mit wählbaren Spalten. Der Krümelpfad zeigt die aktuelle Ebene.
- **Suche** — Nach Dateiname, Beschreibung und Ersteller:in im aktuellen Ordner samt Unterordnern (keine Volltextsuche in Dateien).
- **Dateistatus** — „Wird bearbeitet", „gesperrt" (über Metadaten) und ein „Neu"-Label direkt nach dem Upload.
- **Aktionen** — Im 3-Punkte-Menü: verschieben, kopieren, herunterladen, zippen und löschen je Datei.
- **Drag & Drop + Multi-Upload** — Mehrere Dateien gleichzeitig per Maus auf das Zielfeld ziehen.
- **Massen-Aktionen** — Über Checkboxen mehrere Einträge auswählen und gemeinsam bearbeiten.
- **Erstellen im Ordner** — Dokumente (OnlyOffice: Word/Excel/PowerPoint, Diagramme, Whiteboard, HTML …), Unterordner, Video- und Audioaufnahmen.
- **Metadaten & Lizenzen** — Beschreibung, Sperre, Lizenzangaben (z. B. Creative Commons), Aufrufzähler und Direktlink je Datei.
- **Papierkorb** — Gelöschtes wandert in den Papierkorb; die automatische Löschfrist setzen Administrator:innen.
- **Quota / Speicherlimit** — Begrenzung pro Datei und pro Ordner (Admin). Gilt auch bei WebDAV-Upload.

[zum Seitenanfang ^](#folders)

---


## Speicherplatz (Quota) {: #quota}

Jeder Upload-Bereich unterliegt einer Quota (pro Datei und gesamt). 
- **Quota / Speicherlimit** — Begrenzung pro Datei und pro Ordner (Admin). Gilt auch bei WebDAV-Upload.

Der **Papierkorbinhalt** zählt ebenfalls zur Quota. Fehlt einmal Speicherplatz, löschen Sie bitte zuerst den Papierkorb.

Eine **Anpassung des verfügbaren Speicherplatzes** kann durch Administrator:innen vorgenommen werden. Die Quota kann sowohl für bestimmte Rollen (z.B. alle Autor:innen bekommen mehr Speicherplatz) als auch für Einzelpersonen eingestellt werden (z.B. eine bestimmte Person muss viele Videos speichern).  

Nutzen Sie **Ressourcenordner** für mehrfach verwendete Dateien, statt sie in jeden Kurs zu kopieren. Das spart Speicherplatz und hält Inhalte konsistent.

[zum Seitenanfang ^](#folders)

---


## Die Ordnertypen im Detail

## Welche Ordner gibt es?

Siehe auch [Ordnerkonzept >](../../manual_user/basic_concepts/Folder_Concept.de.md)

### 1. Kursbaustein „Ordner"

*Kurs · Wissensvermittlung*

Der klassische Weg, um Material zum Download bereitzustellen (Folien, Skripte). Auf Wunsch auch kollaborativ mit Upload-Recht für Lernende.

- **Ablageort:** Tab „Ordnerkonfiguration": automatisch generierter Ordner unter `_courseelementdata` oder ein Ordner aus dem Ablage- bzw. Ressourcenordner.
- **Rechte:** Standard: Besitzer + Betreuende dürfen hochladen; erweiterbar auf Gruppen oder einzelne Personen.
- **Sichtbar:** Inhalte für alle Kursteilnehmenden.
- **Extras:** Dokumente erstellen, Metadaten/Lizenzen, Abonnement, WebDAV-Link im 3-Punkte-Menü.

Mehr zum [Kursbaustein Ordner >](../../manual_user/learningresources/Course_Element_Folder.de.md)


### 2. Kursbaustein Teilnehmer:innen-Ordner

*Kurs · Kommunikation & Kollaboration*

Dateiaustausch 1:1 zwischen Teilnehmenden und Betreuenden über zwei Unterordner — einen Abgabe- und einen Rückgabeordner. Jede:r sieht nur den eigenen Ordner. Bewertbar.

- **Einrichten:** Kurseditor → Tab „Ordner Einstellungen".
- **Optionen:** Löschen/Überschreiben sperren, Abgabezeitfenster, maximale Dokumentanzahl.
- **Struktur:** Tab „Template Einstellungen": einheitliche Unterordner für alle Teilnehmenden.
- **Achtung:** Template-Unterordner lassen sich später nicht umbenennen (nur löschen/neu anlegen).

Mehr zum [Kursbaustein Teilnehmer:innen Ordner >](../../manual_user/learningresources/Course_Element_Participant_Folder.de.md)


### 3. Ordner im Kursbaustein „Aufgabe"

*Kurs · Aufgaben-Workflow*

Innerhalb der Bausteine „Aufgabe" und „Gruppenaufgabe" stehen mehrere Ordner für den Workflow bereit: Aufgabenstellung, abgegebene, zurückgegebene und überarbeitete Dokumente sowie Musterlösung — nur im Baustein zugänglich.

- **Einrichten:** Kurseditor → Baustein „Aufgabe" / „Gruppenaufgabe".
- **Wann:** Für komplexere Abgabe-Prozesse als beim Teilnehmer:innen-Ordner.

Mehr zum [Kursbaustein Aufgabe >](../../manual_user/learningresources/Course_Element_Task.de.md)<br>
Mehr zum [Kursbaustein Gruppenaufgabe >](../../manual_user/learningresources/Course_Element_Grouptask.de.md)


### 4. Betreuer:innen-Ordner

*Kurs · nur intern*

Ein Ordner ausschliesslich für Betreuende und Besitzende — z. B. für interne Unterlagen, die Teilnehmenden nicht zugänglich sein sollen.

- **Einrichten:** Einstellungen → Optionen → „Einstellungen Betreuer:innen".
- **Quelle:** Bestehender Unterordner aus dem Ablageordner oder neu `_coachdocuments`.
- **Öffnen:** Administration → „Unterlagen Betreuer:innen" oder über den File Hub.

Mehr zum [Betreuer:innen Ordner >](../../manual_user/learningresources/Course_Settings_Options.de.md#einstellungen-betreuerinnen)


### 5. Ablageordner

*Kurs · Fundament*

Die zentrale Hintergrund-Ablage eines Kurses: hier liegen physisch alle im Kurs verwendeten Dateien (HTML-Seiten, Grafiken, Materialien der Ordner-Bausteine). Teilnehmende greifen nur indirekt über publizierte Bausteine darauf zu.

- **Öffnen:** Administration → `Dateien` (früher „Ablageordner")
- **Auto-Ordner:** `_courseelementdata`, `_sharedfolder`, `_documents`, `_coachdocuments`
- **Struktur:** Unterordner frei anlegbar; sinnvoll strukturieren.
- **Achtung:** Quota pro Datei und gesamt — gilt auch bei Upload via WebDAV.

Mehr zum [Ablageordner >](../../manual_user/learningresources/Storage_folder.de.md)

### 6. Ressourcenordner

*Kursübergreifend · Lernressource*

Der einzige Ordnertyp, der über mehrere Kurse hinweg dieselben Dateien liefert. Zentral einmal pflegen — Änderungen wirken in allen verknüpften Kursen.

- **Erstellen:** Im Autorenbereich als eigene Lernressource (mit eigenen Besitzer:innen).
- **Einbinden:** Kurs → Einstellungen → Optionen; max. 1 pro Kurs; erscheint als `_sharedfolder`.
- **Modus:** Schreibgeschützt (nur referenziert) oder ohne Schreibschutz — dann schlagen Änderungen in allen Kursen durch.
- **Standalone:** Über den Tab „Freigabe" auch kursunabhängig nutzbar.

Mehr zum [Ressourcenordner >](../../manual_user/learningresources/Resource_Folderde.de.md)


### 7. Gruppenordner

*Gruppe · Kollaboration*

Gemeinsamer Ordner der Mitglieder einer Lern- oder Arbeitsgruppe zum Austausch von Dokumenten, inkl. Unterordnern. Zugriff strikt an die Gruppenmitgliedschaft gebunden.

- **Aktivieren:** Gruppenbetreuende schalten das Werkzeug „Ordner" frei.
- **Zugriff:** Alle Gruppenmitglieder; auch via File Hub, sofern Mitglied.
- **Extras:** Abonnierbar; Quota pro Gruppe anpassbar.

Mehr zum [Gruppenordner >](../../manual_user/groups/Using_Group_Tools.de.md)


### 8. Persönlicher Ordner

*Persönlich · pro Person*

Die individuelle Dateiablage jeder Person, unabhängig von Kursen. Unterteilt in einen privaten und einen öffentlichen Bereich (letzterer über die Visitenkarte einsehbar).

- **Öffnen:** Persönliches Menü → File Hub.
- **Bereiche:** `private` (nur ich) · `public` (via Visitenkarte lesbar).

Den persönlichen Ordner finden Sie seit Release 19 im [persönlichen Menü >](../../manual_user/personal_menu.de.md) im [File Hub >](../../manual_user/personal_menu/File_Hub.de.md).

### 9. Dokumentenpool

*Systemweit · verwaltet*

Keine reine Dateiablage, sondern eine Dokumentenverwaltung: Dokumente werden mit Taxonomie/Metadaten versehen, der Zugriff kann an Kompetenzen gebunden werden. Dokumente lassen sich nicht direkt in einen Kurs einbinden.

- **Sichtbar:** Im File Hub als Ordner; optional als Site in der Hauptnavigation.
- **Zugriff:** Kompetenz-/rechtegesteuert; WebDAV möglich.

Mehr zum [Dokumentenpool >](../../manual_admin/administration/Modules_Document_pool.de.md)


### 10. Kursarchiv

*Kurs · Archiv*

Beim Archivieren eines ganzen Kurses oder einzelner Bausteine landen die Daten als ZIP im Ordner „Kursarchiv". Inhalte lassen sich im File Hub anzeigen.

- **Öffnen:** File Hub → „Kursarchiv".
- **Inhalt:** Teilnehmerdaten separat vom Kurs, als ZIP aufbewahrt.

Mehr zum [Kursarchiv >](../../manual_user/learningresources/Course_Archiving.de.md#wo-finde-ich-kursarchiv-dateien)

[zum Seitenanfang ^](#folders)

---


## Entscheidungshilfe {: #decision_aid}

| Ich möchte … | Dazu verwende ich … |
|--------------|-----------|
| Material zum Download bereitstellen | **→ Kursbaustein „Ordner"** |
| Abgaben einsammeln und individuell zurückgeben | **→ Kursbaustein Teilnehmer:innen-Ordner** (wenn komplex: Kursbaustein „Aufgabe") |
| in mehreren Kursen verwendete Dateien gemeinsam pflegen | **→ Ressourcenordner** |
| als Autor:in alle in einem Kurs verwendeten Dateien verwalten | **→ Ablageordner** |
| Interne Unterlagen nur für Betreuende ablegen | **→ Betreuer:innen-Ordner** |
| In einer Gruppe gemeinsam Dateien austauschen | **→ Gruppenordner** |
| Eigene Dateien unabhängig vom Kurs ablegen | **→ Persönlicher Ordner** |
| Grosse Mengen / ganze Ordnerbäume hochladen | **→ WebDAV** |
| Alle meine Ordner an einer Stelle überblicken | **→ File Hub** |


[zum Seitenanfang ^](#folders)

---


## Stolpersteine {: #stumbling_stones}

* Unterordner innerhalb eines Ordnerbausteins sind nur dort (innerhalb dieses Kursbausteins) vorhanden. Denken Sie daran, wenn Sie gleichartige Strukturen aufbauen.

* Werden im Kursmenü unterhalb eines Ordner-Kursbausteins weitere Ordner-Kursbausteine eingefügt, werden diese Unterordner nicht innerhalb des übergeordneten Ordners angezeigt. Das liegt daran, dass die separaten Ordner-Kursbausteine untereinander nicht kommunizieren.

* Auf Unterordner innerhalb eines Ordner_Kursbausteins besteht kein WebDAV-Zugriff. 

* Auch der Papierkorbinhalt zählt zur Quota.

* Verwechseln Sie bitte auch nicht den Strukturbaustein mit einem Ordner-Kursbaustein (KB Ordner statt KB Struktur).

[zum Seitenanfang ^](#folders)

---

## Dateien einfügen {: #insert_files}

Sind die gewünschten Ordner vorhanden, können Sie dort 

- Dokmente hochladen
- Dokumente direkt im Ordner erstellen
- Dokumente per WebDAV übertragen

Welche Personen (OpenOlat-Rollen) in welchem Ordner Dokumente hochladen oder erstellen dürfen, hängt von den jeweiligen Konfigurationen (vergebenen Berechtigungen) durch Autor:innen oder Administrator:innen ab.

Welche Dokument-Formate direkt erstellt werden können, hängt davon ab, welche Tools installiert sind. Z.B. ob Lizenzen für Microsoft Word und Excel für die Nutzung in OpenOlat vorhanden sind. Wenden Sie sich gegebenenfalls an Ihr Administrator:innen.

Denken Sie auch daran, dass die Grösse der einzelnen Dateien und der Gesamtspeicher eines Ordner durch Quotas festgelegt sind.

[zum Seitenanfang ^](#folders)

---


## Weiterführende Informationen {: #further_information}

[Ordnerkonzept >](../../manual_user/basic_concepts/Folder_Concept.de.md)<br>
[Kursbaustein Ordner >](../../manual_user/learningresources/Course_Element_Folder.de.md)<br>
[Kursbaustein Teilnehmer:innen Ordner >](../../manual_user/learningresources/Course_Element_Participant_Folder.de.md)<br>
[Kursbaustein Aufgabe >](../../manual_user/learningresources/Course_Element_Task.de.md)<br>
[Kursbaustein Gruppenaufgabe >](../../manual_user/learningresources/Course_Element_Grouptask.de.md)<br>
[Betreuer:innen Ordner >](../../manual_user/learningresources/Course_Settings_Options.de.md#einstellungen-betreuerinnen)<br>
[Ablageordner >](../../manual_user/learningresources/Storage_folder.de.md)<br>
[Ressourcenordner >](../../manual_user/learningresources/Resource_Folderde.de.md)<br>
[Gruppenordner >](../../manual_user//groups/Using_Group_Tools.de.md)<br>
[Dokumentenpool >](../../manual_admin/administration/Modules_Document_pool.de.md)<br>
[Kursarchiv >](../../manual_user/learningresources/Course_Archiving.md#wo-finde-ich-kursarchiv-dateien)<br>
[File Hub >](../../manual_user/personal_menu/File_Hub.de.md)<br>

[zum Seitenanfang ^](#folders)

