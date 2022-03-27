# Release Notes 16.2

![Release Grafik](assets/162/press-release-16.2.png)

Mit OpenOlat 16.2 geben wir unseren nächsten Major Release frei.

...

![Anzahl Features Vervbesserungen Bugs](assets/162/Features_Improvements_Labels_DE.png)

Seit Release 16.1 wurden über XX neue Funktionen und Verbesserungen zu OpenOlat hinzugefügt. Hier finden Sie die wichtigsten neuen Funktionen und Änderungen. Zusätzlich zu wurden mehr als 100 Bugs behoben. Die komplette Liste der Änderungen in 16.1 – 16.1.8 finden Sie [hier](Release_notes_16.1.md).

* * *

:material-calendar-month-outline: **Releasedatum: 01.04.2022 • Letztes Update: 01.04.2022**

* * *

## Noten (Epic 5987)

* Integration Notensystem (6007)
* Implementation einer Skala für Noten
    * Aktivierung in der Administration
    * Noten, Textbewertung, Smileys
* Anzeige: Coaching Tool / Bewertungswerkzeug (6008)

Die Übertragung der Punkte in Noten kann für alle bewertbaren Kursbausteine vorgenommen werden. Dazu muss am Baustein die entsprechende Notenskala ausgewählt werden.

## Prüfungschat (Epic 5212)

Bei Prüfungen, die von den Prüflingen zu Hause geschrieben werden (z.B. Open-Book Prüfung, Take-Home Exam), müssen die Aufsichtspersonen in der Lage sein, mit den Prüflingen zu kommunizieren. Ebenso müssen Prüflinge die Prüfungsaufsicht kontaktieren können, sollten z.B. Fragen zur Prüfung oder technische Probleme auftreten.

In OpenOlat wurde für diese Anforderungen eine entsprechende Infrastuktur geschaffen:

* Für Aufsichtspersonen (Betreuende) steht am Kursbaustein "Test" ein neuer Bereich "Kommunikation" zur Verfügung.
* Aufsichtspersonen können Nachrichten an alle Prüflinge senden (einseitige Broadcast-Nachticht)
* Der integrierte Prüfungs-Chat ermöglicht einen direkter Austausch zwischen Aufsichtsperson und Prüfling. Der Chat kann von beiden Seiten gestartet werden.
* Aufsichtspersonen können bei Bedarf eine BigBlueButton-Videokonferenz mit dem Prüfling starten und dort die Bildschirmfreigabe nutzen.

## Safe Exam Browser Konfiguration

Für die Verwendung des Safe Exam Browsers bei Online-Prüfungen konnten bisher die im Safe Exam Browser erstellten Konfigurations-Keys in OpenOlat hinterlegt werden.

Ergänzend wurden nun die gängigen Safe Exam Browser Konfigurationen ebenfalls in OpenOlat integriert, so dass Standard-Konfigurationen direkt in OpenOlat vorgenommen werden können. Die Konfigurationsdatei kann je nach ausgewählter Option vom Betreuenden oder auch von den Prüflingen selbst vor der Prüfung herunterlgeladen werden.

* * *

## Features im Bereich eAssessment, Tests und Bewertung

### Kursbaustein "Test"

Zusätzlich zur HTMl-Variante und den Rohdaten im Excel können Testresultate nun auch inklusive der PDF-Version exportiert werden.

Da der Export von Testresultaten im PDF-Format für viele Teilnehmer viel Zeit in Anspruch nimmt, werden Testresultat-Exporte nun asynchron durchgeführt. Das heisst, ausgelöste Exporte werden zunächst in OpenOlat generiert und können nach Fertigstellung heruntergeladen werden. Man kann also in der Zwischenzeit weiter in OpenOalt arbeiten. Sobald der Export zum Download verfügbar ist, erhält man eine E-Mail-Benachrichtigung mit dem Link zum Download. Die einzelnen Exporte können in einem eigenen Exportbereich am Kursbaustein "Test" verwaltet werden.

### Bewertungswerkzeug

Die Übersichtsseite des Bewertungswerkzeugs und die Dartellung der Daten wurde komplett überarbeitet.

* Erneuerung der Datenanzeige auf der Übersichtsseite (5891)

### Sonstiges

* Fragetyp "Formeleditor" (6071)
* Teststatistiken waren bisher nur auf der obersten Ebene des Tests bzw. zu den einzelnen Fragen verfügbar. Ab sofort stehen die Statistiken auch auf Sektionsebene zur Verfügung.

* * *

## Weitere Verbesserungen rund um Kurse

### Für Autoren

* Quick-Add Aktion um neue Kursbausteine hinzuzufügen
* Kurs Kopier-Wizard:
    * Anzeige der Standardoptionen
    * Optionen für Test-Kusbaustein
    * Optionen für Dokumenten- und Betreuer-Ordner
    * Anpassung beim Verschieben von spezifischen Datumsangaben bei Kursbausteinen (5832)
    * Kurslayout: verbessertes Verhalten bei Wechsel der Hintergrundfarbe (5867)
    * Verbessertes Hervorheben der Kursbausteintypen im Editor (5994)

### Für Teilnehmende

 ...

* * *

## Weiteres, kurz notiert

* MathLive Editor Integration im HTML-Editor
    * Vorschau mathematischer Formeln im HTML-Editor
    * Formel-Element im Formular-Editor (Content-Editor)
* Steuerung der Veröffentlichung von Informations- und Wartungsmeldungen
* Lernpfad: Lesesbestätigung von Teilnehmenden durch Betreuer zurücksetzen
* Scorm-Module im Vollbildmodus öffnen
* Standard-Dokumenteneditor individuell konfigurieren
* Platzhalter für Autovervollständigung in Suchfeldern
* Trennung der Module "Lektionen" und "Abmeldungserfassung" (5853)
* Allgemeine Verbesserungen im Sinne der Barrierefreiheit (6025)

...

* * *

## Technisches

* Handbuch-Migration von Confluence zu MKDocs
* Upgrade TinyMCE von Version 4 auf Version 5
* Upgrade Mathjax von Version 2 auf Version 3
* Bibliotheken von Drittanbietern aktualisiert
* Stabilisierung der Selenium-Tests

* * *

## Weitere Informationen

* [Jira Release notes 16.2](https://jira.openolat.org/secure/ReleaseNote.jspa?projectId=10000&version=17802)
