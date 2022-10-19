# Release Notes 17.1 - :construction: Under construction :construction

![Release Grafik 17.1](assets/171/press-release-17.1.png)

* * *

:material-calendar-month-outline: **Releasedatum: 14.10.2022 • Letztes Update: 14.10.2022**

* * *

Mit OpenOlat 17.1 geben wir unseren nächsten Major Release frei.

<!-- *EINLEITUNGSTEXT* -->

![Anzahl Features und Bugs in Release 17.1](assets/171/Features_Improvements_Labels_DE.png)

Seit Release 17.0 wurden über 70 neue Funktionen und Verbesserungen zu OpenOlat hinzugefügt. Hier finden Sie die wichtigsten Neuerungen zusammengefasst. Zusätzlich wurden mehr als 100 Bugs behoben. Die komplette Liste der Änderungen in 17.0 – 17.0.6 finden Sie [hier](Release_notes_17.0.de.md).

* * *

## Katalog 2.0 - Verbesserungen und Ergänzungen

Nach dem Start des Katalogs 2.0 im Release 17.0 wurde dieser weiter verfeinert und das Feedback unserer Community eingearbeitet. Folgende Neuerungen sind nun verfügbar:

* Die Katalog- und Taxonomieverwaltung wird vom Lernressourcenverwalter vorgenommen und kann direkt über den Katalog aufgerufen werden.

<!-- BILD -->

* Launcher für die Katalog-Statseite können auf Organisationseinheiten eingeschränkt und somit nur für User der entsprechenden Organisation freigegeben werden.
* Für den statischen Text-Launcher, der zum Beispiel als Beschreibung oder Einleitung für den Katalog dient, werden neu auch Media-Elemente wie Bilder und Videos unterstützt.
* "Leere" Launcher, die keine Lernressourcen-Angebote enthalten, werden ausgeblendet.
* Freigabe-Konfiguration von Lernressourcen: Die definierten Fachbereiche (= Taxonomie-Ebenen) für die Katalogfreigabe werden auch im Angebot entsprechend aufgeführt.
* Für die Darstellung der Lernressourcen auf der Katalog-Startseite (= Compact Card View) kann konfiguriert werden, welche zusätzlichen Informationen ausgegeben werden.
* Die Suche für mehrere Begriffe wurde optimiert.

<!-- BILD -->

## Authoring

#### Redesign des Wizards zur Erstellung von Kursen

Der Wizard zur Kurs-Erstellung wurde grundlegend überarbeitet, um die Autorenschaft noch besser zu unterstützen.

* Die Optimierung der Kurstypauswahl mit ergänzenden Informationen sowie Angabe geeigneter Szenarien erleichtert die Wahl des richtigen Kurstyps für das gewünschte Setup.
* Zusätzliche Eingabewerte ermöglichen es, bei der Kurserstellung bereits über den Wizard alle wichtigen Werte und Daten zu erfassen.
* Um Kurs-Duplikate zu vermeiden, wurden verschiedene Validierungen und Warnhinweise ergänzt.

#### Weitere Verbesserungen

* Über die Sammelaktion "Status ändern" kann der Publikationsstatus gleichzeitig für mehrere ausgewählte Lernressourcen gesetzt werden.
* Der "Didaktische Typ" heisst nun "Durchführungsformat".

## Optimierter und erweiterter Aufgabenbaustein

Der Aufgabenbaustein wartet mit einer visuellen Generalüberholung und neuen Funktionen auf.

#### Visuelles Redesign und Timer-Funktionalität

Die Strukturierung der einzelnen Schritte wurde klarer gestaltet und eine Status-Anzeige eingeführt, um einen besseren Überblick zum aktuellen Bearbeitungsstand zu gewährleisten. Zeiten und Fristen, wie zum Beispiel eine Abgabe-Deadline, werden deutlicher für Teilnehmende und Betreuende ausgewiesen.

zu gestalten und die Zeiten / Termine besser hervorzuheben. Sowohl der Teilnehmer als auch der Coach müssen die Fristen der jeweiligen Schritte auf einen Blick erkennen können.

#### Verspätete Abgabe

Für Aufgabenstellungen, die eine längere Bearbeitungsdauer vorsehen, wird oft nach Ablauf der Einreichungsfrist ein zusätzlicher späterer Abgabetermin eingeräumt. So werden abgegebene Lösungen auch nach der offiziellen Einreichungsfrist akzeptiert, meist in Verbindung mit einem Punkteabzug.

Im Aufgabenbaustein wurde die Möglichkeit ergänzt, eine solche verspätete Abgabe zu konfigurieren. Diese Nachfrist wird den Teilnehmenden transparent bei der Bearbeitung der Aufgabe angezeigt. Für Betreuende ist ebenfalls ersichtlich, wenn Teilnehmende ihre Dokumente erst in der Nachfrist eingereicht haben.

####  Video Recorder

Bisher konnten im Aufgabenbaustein Dokumente verschiedener Formate sowie Videos hochgeladen werden. Für einen noch flexibleren Einsatz des Bausteins können neu auch Videos direkt im Baustein erstellt und eingereicht werden. Ein generischer Videoaufnahme-Controller bietet dabei die Funktionalität, eine Live-Aufnahme im Browser über die lokale Computer-Kamera oder separate Handy-Kamera anzufertigen und diese hochzuladen.

So können zum einen Betreuende schnell und unkompliziert Video-Aufgabenstellungen bereitstellen, zum anderen können Teilnehmende selbst erstellte Videos als Abgabeformat einreichen. Dies bietet vor allem für Aufgabenstellungen im Sprachbereich oder mit praktischem Anteil neue Möglichkeiten.

## Optimierungen für ePortfolio- und Formular-Editor

Der bestehende Editor zur Erstellung von Formularen und ePortfolio-Einträgen wurde neu gestaltet.

Die bisher verwendeten Container wurden durch eine neue Layout-Komponente ersetzt. So kann schnell und einfach aus den fertigen Vorlagen das gewünschte Layout zusammengesetzt und nachfolgend mit Inhalten gefüllt werden. Zudem wurde der Content Editor zum Hinzufügen von Inhalten und der "Inspector" zur Formatierung von Inhalten getrennt.

Mittelfristig soll der Editor standardmässig zur Erstellung von Kursinhalten zur Verfügung stehen und wird in den folgenden Releases immer weiter ausgebaut.

## Neuerungen im Kurs

#### Teilnehmeransicht: Kursvorschau für Autoren und Betreuende

Kursautoren und -betreuende mussten sich bisher manuell auch die Teilnehmer-Rolle zuwweisen (lassen), um den Kurs aus Sicht der Lernenden einzusehen. Als "echte" Teilnehmende wurden sie dadurch auch in der Liste der Kursmitglieder und im Bewertungswerkzeug aufgeführt.

Mit Release 17.1 wird die Teilnehmeransicht eingeführt. Dieses ist automatisch für Kursbesitzer und -betreuende verfügbar und ermöglicht eine Vorschau des Kurses aus der Teilnehmendenperspektive. Alle Aktivitäten, die in der Teilnehmeransicht durchgeführt werden, werden vom System gepeichert.

#### Template Ordnerstruktur im Teilnehmerordner

Mit dem Teilnehmerordner können Betreuende individuelle Handouts an Teilnehmende verteilen und auf die eingereichten Dokumente der Teilnehmenden zugreifen.

Neu können Betreuende bereits eine bestimmte Ordnerstruktur im Voraus für die Teilnehmenden anlegen, um die Strukturierung der eingereichten Dokumente zu vereinheitlichen und die Abgabe zu erleichtern.

#### UX / Usability im Kurs

* Einheitliche Benennung der Kurs-Tabs und optimierte Tab-Navigation beim Wechsel zwischen Kursbausteinen
* Optimierte Darstellung der Bewertungseinstellungen in Kursen
* Verbesserte Anzeige und Filterung von Mitgliedern / Nicht-Mitgliedern in der Übersicht und Teilnehmendenliste bewertbarer Bausteine
* Verbesserte Meldung und erweiterte Informationen für Teilnehmende, warum ein Kurs noch nicht zugänglich ist

#### Sonstige Neuerungen

* Tests:
    * Korrektur während Testdurchlauf gesperrt
    * Zusätzlicher Hinweis für Autoren, wenn manuelle Korrektur und sofortige Anzeige der Test-Resultate konfiguriert ist
    * Testarchivierung ohne PDF möglich
* Lernpfad-Kurs:
    * Neues Erledigungskriterium “alle Checkboxen”
    * Kursvorschau (Simulation) für Lernpfadkurse entfernt
* Anonyme Gäste in Bewertungswerkzeug nicht mehr anzeigen
* Manuelle Bewertung: Optimierte Bearbeitung von Rubric-Formularen
* E-Mail Baustein: Gesperrter Betreff für Versendende, wenn vorkonfiguriert
* Abspiel-Funktion für Audios im Ordner und Aufgabenbaustein sowie beim Upload als Lernressource

* * *

## Gender Neutralität

* Anreden in Mailtexten wie "Sehr geehrte/r", "Liebe/r" und ähnliches einheitlich auf “Guten Tag” geändert (betrifft nur deutsche Texte)

## Accessibility

* Alternativ-Texte bei Bildern
* Zusätzliche Aria-Tags bei Bildern

* * *

## Benutzerverwaltung

In der Benutzerverwaltung wurde vor allem Optimierungen aus UX- und Usability-Sicht umgesetzt:

* Überführung der Tabelle in neues Konzept mit verbesserten Filter
* Anzeige der Organisation(en) zu den Benutzern inklusive Filtermöglichkeit
* Optimierung der Sammelaktionen inklusive Ergänzung von Benutzerrolle und Organisation

* * *

## Sonstige UX- / Usability-Neuerungen

* Optimierungen für den Group Life Cycle:
    * Option zum Ausschluss einzelner Gruppen von den automatischen Methoden
    * Verbesserte Visualisierung pro Gruppe, ob das manuelle oder automatische Löschen greift
    * Ergänzende Informationen für Filtern und Tabellen und optimiertes Labeling
* Optimiertes Labeling zur besseren Unterscheidung von Test-Korrektur im Kurs, Korrektur mit Aufträgen und Noteneinstufung
* Verbesserte Meldung für anonyme Gäste bei Zugriff auf nicht zugängliche Bereiche in OpenOlat
* Kleinere kosmetische und funktionale Verbesserungen für den Taxonomy Chooser
* Optimiertes Dropdown-Menü zur Auswahl von Organisationen
* Optimierte Ausrichtung der zugeordneten Taxonomien in der Kursübersicht

* * *

## Weiteres, kurz notiert

* Externe Benutzer:
    * Einladung mehrerer externer Personen
    * Inaktivierung / Reaktivierung von Einladungen
    * Zahlreiche weitere Optimierungen in Anzeige und Workflow
* Big Blue Button: Automatisches Löschen von Meetings und Aufzeichnungen
* Zoom:
    * Option Kalendereinträge zu verhindern
    * Referenzliste, wo (Kursbaustein, Kurswerkzeug, Gruppenwerkzeug) das Zoom-Profil verwendet wird
* Content Package:
    * Systemweiter CSS Header / Footer für PDF-Export
    * Optionale Benachrichtigung bei inhaltlichen Änderungen an Mitglieder der Kurse, in denen das Content Package referenziert ist
* SEB Integration: Quit Link Unterstützung

* * *

## Technisches

* Bibliotheken von Drittanbietern aktualisiert und Code-Bereinigung
* Performance-Optimierung unter Kurse > "Meine Kurse"

* * *

## Weitere Informationen

* [Jira Release Notes 17.1.0](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=18900)
