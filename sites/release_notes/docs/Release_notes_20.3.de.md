# Release Notes 20.3

![Release Grafik 20.3](assets/203/press-release-20.3.png)

* * *

:material-calendar-month-outline: **Releasedatum: 25.03.2026 • Letztes Update: 25.03.2026**

* * *

Mit **OpenOlat 20.3** wurden zentrale Bereiche der Plattform gezielt weiterentwickelt. Im Fokus standen die flexible Gestaltung und Erweiterungen der **persönlichen Dashboards**, der neue **Master Import** im Course Planner sowie zahlreiche Verbesserungen für eine effizientere Nutzung im Alltag.

Das persönliche Dashboard wurde neu individualisierbar gestaltet – Widgets können nun frei angeordnet, ein- oder ausgeblendet werden. Zudem wurde im Course Planner mit dem neuen Master Import das effiziente Anlegen und Ergänzen von Durchführungen, Terminen und Mitgliedschaften per Excel ermöglicht.

## Highlights

**Dasbhboards und Widgets** – Die Dashboards un Coachtig Tool und dem Course Planner wurden um neue und erweiterte Widgets ergänzt. Das persönliche Dashboard kann individuell gestaltet werden und der Course Planner bietet eine kompakte Übersicht über laufende Durchführungen. Das Coaching Tool wurde um ein Ereignis- und ein Kalender-Widget erweitert, die bevorstehende Termine übersichtlich anzeigen. Kennzahlen und Standardeinstellungen im Kurs-Widget wurden überarbeitet.

**Markdown-Import im Content Editor** – Seiten können nun direkt aus Markdown-Dateien importiert werden. Inhalte aus externen Quellen oder mit KI unterstützt erzeugte Inhalte lassen sich so mit wenigen Klicks übernehmen und strukturiert darstellen – eine effiziente Grundlage für die Erstellung und Weiterentwicklung von Kursinhalten.

**KI-Funktionen** – Das KI Modul unterstützt neu verschiedene KI-Anbieter (OpenAI, Anthropic, allgemeine OpenAI-kompatible Dienste). Beim Hochladen von Bildern werden Metadaten wie Alt-Text, Titel und Schlagwörter automatisch generiert. Die Erstellung von Multiple-Choice-Fragen wurde qualitativ verbessert und unterstützt beliebige Sprachen. 

**Course Planner – Master Import** – Durchführungen, Termine und Mitgliedschaften können per Excel-Import effizient angelegt und nachträglich ergänzt werden. Ein integrierter Assistent prüft die Daten vor dem Import und unterstützt mit klaren Rückmeldungen.


![Anzahl Features und Bugs in Release 20.3](assets/203/Features_Improvements_Labels_20.3_DE.png)

Seit Release 20.2 wurden über 105 neue Funktionen und Verbesserungen zu OpenOlat hinzugefügt. Hier finden Sie die wichtigsten Neuerungen zusammengefasst. Zusätzlich wurden zahlreiche Bugs behoben. Die komplette Liste der Änderungen in 20.2.x finden Sie [hier](Release_notes_20.2.de.md){:target="_blank"}.

* * *

## Widgets

### Dashboard personalisieren

Widgets wurden funktional erweitert und vereinheitlicht: Das persönliche **Dashboard** kann individuell gestaltet werden, indem Widgets frei angeordnet sowie ein- oder ausgeblendet werden. Gleichzeitig bieten Widgets wie das Tabellen- und Mitglieder-Widget erweiterte Konfigurationsmöglichkeiten bei einheitlicher Bedienung.

### Course Planner

Im **Course Planner** sorgen neue Übersichts-Widgets dafür, dass relevante Informationen – wie laufende Durchführungen – direkt auf der Startseite sichtbar sind. Über die Einstellungen lassen sich Kennzahlen, Status und die Anzahl der angezeigten Einträge flexibel anpassen.

![Dashboard Widget Konfiguration](assets/203/Dashboard_widget_config_DE.png){ class="shadow lightbox" title="Dashboard: Individuelle Widget-Konfiguration" }

### Coaching Tool

#### Ereignis-Widget

Das Coaching Tool wurde um ein neues **Ereignis-Widget** erweitert, das bevorstehende Termine übersichtlich anzeigt – mit direkten Links zu den jeweiligen Kursen. Kennzahlen und Standardeinstellungen im Kurs-Widget wurden überarbeitet.

![Coaching Tool Event Widget](assets/203/CoachingTool_event_widget_DE.png){ class="shadow lightbox" title="Coaching Tool: Ereignis-Widget" }

#### Kalender-Widget

Das **Kalender-Widget** im Coaching Tool bietet eine übersichtliche Darstellung aller anstehenden Termine und erleichtert die zeitliche Orientierung im Arbeitsalltag. Relevante Veranstaltungen werden direkt im Kontext des Kalenders angezeigt, inklusive Datum, Uhrzeit und – falls vorhanden – Ort.

Die Farbcodierung unterstützt die schnelle Einordnung: Orange markiert aktuell laufende Termine, während Blau den nächsten anstehenden Termin hervorhebt. So lassen sich Prioritäten auf einen Blick erkennen und Termine effizient planen.

![Coaching Tool Event Widget](assets/203/CoachingTool_kalender_widget_DE.png){ class="shadow lightbox" title="Coaching Tool: Kalender-Widget" }

* * *

## Content Editor

### Markdown-Import

Markdown-Dateien können nun in einer ersten Version direkt im Content Editor importiert werden, wodurch sich Inhalte aus externen Werkzeugen oder einfachen Textdateien ohne manuelles Nachformatieren übernehmen lassen. Der Inhalt wird automatisch in das strukturierte Seitenformat überführt und bildet so eine effiziente Grundlage, um Kursseiten schneller und einfacher mit Inhalten zu befüllen. Die Inhalte werden dabei automatisch in die Funktionsblöcke wie Titel, Tabelle, Info-Box etc. des Content Editors überführt. 

Bilder werden direkt in die Mediathek eingebunden, wobei eine Duplikats-Prüfung verhindert, dass das selbe Bild mehrfach in der Mediathek abgelegt wird. So wird Platz gespart und automatisch aufgeräumt, ohne dass man sich als Autor:in darum kümmern muss. 

!!! Info Markdown

	Markdown ist ein weit verbreitetes Textformat, das in vielen Tools und KI-Anwendungen ausgegeben wird, und ermöglicht die nahtlose Übernahme und Weiterverwendung bestehender Inhalte ohne zusätzlichen Formatierungsaufwand. Gleichzeitig unterstützt es eine klare Struktur und erleichtert die kontinuierliche Weiterentwicklung von Lerninhalten.

![Content Editor Markdown Import](assets/203/ContentEditor_markdown_import_DE.png){ class="shadow lightbox" title="Content Editor: Markdown-Import" }

### Unterstützung für SVG-Grafiken

Neu werden in der Mediathek und dem Content Editor SVG Grafiken nicht mehr als Dateien behandelt sondern als Grafik Medienformat unterstützt. KI wird insbesondere bei KI unterstützter Inhaltserstellung oft als Format für Diagramme und Grafiken verwendet. 

* * *

## KI-Funktionen

### KI Modul: Multi-Provider-Unterstützung

Das **KI Modul** wurde grundlegend überarbeitet und unterstützt neu verschiedene KI-Anbieter und Modelle. Neben OpenAI können nun auch **Anthropic** sowie beliebige **OpenAI-API-kompatible Dienste** (z.B. Ollama, vLLM) eingebunden werden. Die Konfiguration erfolgt pro Funktion: Für jede KI-gestützte Funktion kann individuell ein Anbieter und ein Modell ausgewählt werden. Verfügbare Modelle werden direkt vom Anbieter geladen, und eine integrierte Validierung prüft die API-Verbindung beim Einrichten.

### Automatische Bild-Metadaten

Beim **Hochladen von Bildern** im Media Center werden Metadaten wie Titel, Beschreibung, Alt-Text und Schlagwörter nun **automatisch per KI generiert**. Dies verbessert die Barrierefreiheit und erleichtert das Wiederfinden von Medien. Die Metadaten-Generierung funktioniert auch beim **Markdown-Import**: Enthaltene Bilder erhalten ihre Metadaten automatisch im Hintergrund. Sind die generierten Metadaten ungeüngend oder nicht passend können diese wie gewohnt angepasst und jederzeit verändert werden. 

### Verbesserte Multiple-Choice-Generierung

Die automatische Erstellung von **Multiple-Choice-Fragen** wurde qualitativ verbessert – mit valideren Antwortoptionen und besseren Distraktoren. Zudem werden neu **beliebige Sprachen** unterstützt, nicht nur Deutsch und Englisch.

Mit der neuen Multi-Provider-Architektur und der funktionsspezifischen Konfiguration ist die Grundlage geschaffen, um in den kommenden Releases zahlreiche weitere KI-unterstützte Funktionen in OpenOlat zu integrieren. Von der Unterstützung weiterer Fragetypen bis hin zu KI unterstützten Lernsystemen sind viele Projekte in der Planung und Umsetzung. 

* * *

## Course Planner: Master Import

Der Course Planner erhält mit dem **Master Import** eine zentrale Funktion für die effiziente Verwaltung von Durchführungen: Über strukturierte Excel-Dateien lassen sich Durchführungen, Termine und Mitgliedschaften in einem Schritt anlegen. Ebenso können bestehende Strukturen nachträglich ergänzt werden – etwa um weitere Termine oder zusätzliche Teilnehmende hinzuzufügen.

**Was lässt sich importieren?** Produkte, Durchführungen, Kurse und Termine – sowie Teilnehmer:innen und Benutzer:innen. Neue Personen können direkt beim Import angelegt werden. Ein Assistent führt durch den Prozess und zeigt vor dem Import klar an, was neu angelegt, aktualisiert oder übersprungen wird.

**Typische Anwendungsfälle:** Neue Durchführungen mit Terminen und Teilnehmenden effizient anlegen, nachträglich weitere Termine zu bestehenden Durchführungen hinzufügen oder zusätzliche Mitgliedschaften ergänzen.

![CPL Master Import](assets/203/CPL_master_import_DE.png){ class="shadow lightbox" title="Course Planner: Master Import" }

## Course Planner: Weitere Verbesserungen

### Mitgliedschaften & Zugriffssteuerung

Neue Funktionen ermöglichen es, dass Teilnehmende Mitgliedschaften selbstständig bestätigen oder ablehnen. Angebote können zeitlich über Durchführungszeiträume gesteuert werden. Erweiterte Zugriffsberechtigungen sorgen für mehr Transparenz und Kontrolle beim Zugriff auf Produktdaten und öffnen den Berichtszugriff für zusätzliche Rollen.

### Aktivitäts-Log im Zertifikatsprogramm

Mit dem neuen **Aktivitäts-Log** werden alle relevanten Vorgänge im Zertifikatsprogramm zentral erfasst – darunter Mitgliedschaften, Benachrichtigungen, Zertifikate und Einstellungen. Die Einträge sind vollständig einsehbar und lassen sich gezielt filtern.

* * *

## SEO & Seitenvorschau

Mit OpenOlat 20.3 wird die Auffindbarkeit öffentlicher Kursseiten und InfoPages gezielt verbessert. Beim Teilen von Links in sozialen Netzwerken und Messenger-Diensten werden automatisch ansprechende Vorschauen mit Titel, Beschreibung und Bild angezeigt. Gleichzeitig wurde die Darstellung für Suchmaschinen optimiert, und Keywords können individuell pro Seite oder Lernangebot definiert werden.

![SEO Einstellungen](assets/203/SEO_settings_DE.png){ class="shadow lightbox" title="SEO: Open Graph und Metadaten-Konfiguration" }

* * *

## Layout Refresher

Das OpenOlat Layout wurde an diversen Stellen mit kleinen Anpassungen optimiert. Leichte Animationen bei der Interaktion mit der Maus lassen die Applikation frischer und attraktiver erscheinen. 

Das Überblenden der Hintergrundbilder auf der Login Seite wurde vollständig überarbeitet und ist nun flüssiger und ruhiger. Ein optionaler neuer Zoom Effekt erlaubt eine weitere Individualisierung und Erhöung des Nutzererlebnisses. 


## Weiteres, kurz notiert

- **Kurs:** Ein neuer Filter «Relevant» zeigt Kursmitgliedern direkt ihre aktiven Kurse an. Kurse können nach Zeitraum sortiert werden und der Dialog zum Verlassen eines Kurses wurde vereinheitlicht.

- **Tests, E-Assessment & Safe Exam Browser:** Die Statusanzeige in Tests wurde vereinfacht und die Anzahl der Versuche ist direkt bei der Frage sichtbar. Für den Safe Exam Browser können mehrere benannte Konfigurationsvorlagen erstellt und bei der Prüfung ausgewählt werden.

- **Blog/Podcast:** Die Tabellenansicht wurde für den Read-Only-Modus verbessert.

- **Video:** Die Videotranskodierung erfolgt neu standardmässig in 1080p.

- **Benutzerverwaltung:** Einladungslinks können deaktiviert werden. Der Prozess zum Zurücksetzen des Passworts wurde datenschutzrechtlich optimiert.

- **Filter & Suche:** Der Autor:innen- bzw. Besitzer:innen-Filter unterstützt neu die Suche über E-Mail-Adressen.

- **Projekt-Tool:** Neu können persönliche Filter gespeichert werden und Dateien lassen sich über einen externen Link direkt referenzieren.

- **Framework & Usability:** Der Login-Screen wurde visuell modernisiert und sorgt für einen zeitgemässen ersten Eindruck. Leere Ansichten wurden vereinheitlicht und bieten eine klarere Orientierung bei fehlenden Inhalten. Zudem wurde veralteter Code entfernt, um Stabilität und Wartbarkeit zu verbessern.

- **Barrierefreiheit:** Die Navigation per Tab in Dialogen mit Datumsauswahl sowie die Anzeige der Datepicker wurden verbessert.

- **Internes Sicherheitsaudit:** Im Rahmen der Qualitätssicherung für Release 20.3 wurde ein internes Sicherheitsaudit durchgeführt und gezielte Verbesserungen im Bereich Sicherheit umgesetzt.

* * *

## Administratives / Technisches
<mark style="background:#fff88f">@Mandy</mark>

* Dependency-Updates:
    * commons-collections von 3.x auf 4.x migriert
    * TinyMCE von 6.8.6 auf 7.x aktualisiert
    * Fabric.js von 4.4.0 auf 6.4.0+ aktualisiert (CVE-2024-23634 behoben)
    * Bootstrap-Migration von 3.x auf 5.x
    * Prototype.js 1.7 entfernt
    * Apache Lucene von 7.7.0 auf 9.x+ aktualisiert
    * Apache HttpClient von 4.x auf 5.x migriert
    * BeanShell in SCORM evaluiert und adressiert (CVE-2016-2510)
    * Allgemeines Bibliotheks-Update
* Sicherheits-Konfiguration:
    * Content Security Policy wurde verschärft – nach dem Update sollte geprüft werden, ob eigene Konfigurationen und integrierte externe Tools kompatibel sind
    * REST-API-Tokens werden neu gehasht gespeichert – bestehende Tokens behalten ihre Gültigkeit

* * *

## Systemadministratoren: Neue Funktionen aktivieren / konfigurieren
<mark style="background:#fff88f">@Mandy</mark>

!!! note "Checkliste nach Update auf 20.3"

    Folgende Funktionen müssen nach einem Update auf Release 20.3 in der `Administration` aktiviert bzw. konfiguriert werden:

    * [x] SEO & Seitenvorschau konfigurieren: `Module > Katalog / InfoPages > SEO`
    * [x] Dashboard-Widget-Konfiguration durch Nutzer:innen aktivieren/deaktivieren: `Module > Dashboard`
    * [x] SEB-Konfigurationsvorlagen erstellen und freigeben: `Administration > e-Assessment > Safe Exam Browser`
    * [x] Content Security Policy nach Update auf Kompatibilität prüfen
    * [x] Aktivieren von neuen KI Funktionen    
    * [x] Animationen Loginscreen und Zoom Effekt

* * *

## Weitere Informationen
<mark style="background:#fff88f">@Mandy</mark>

* [YouTrack Release Notes 20.3.0](https://track.frentix.com/releaseNotes/OO?q=fix%20version:%2020.3.0&title=Release%20Notes%2020.3.0){:target="_blank"}
