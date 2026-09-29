# Toolbar: Infoseite {: #toolbar_infopage}

![Link Infoseite mit Info-Symbol als erstes Werkzeug der Kurstoolbar markiert](assets/general_functions_infopage_access_toolbar_v2_de.png){ class="shadow lightbox" title="Toolbar eines geöffneten Kurses · 2026.09.29" }

Wer in einem Kurs nachsehen möchte, worum es geht, wann die Termine sind oder wie weit man schon ist, öffnet die Infoseite über den Link **Infoseite** in der Toolbar. Jeder Kurs und jede andere Lernressource hat eine Infoseite. Sie zeigt dieselben Angaben, die Interessierte schon vor dem Buchen sehen: Beschreibung, Fakten, Lernziele, Dozent:innen und Termine. Wer bereits Mitglied ist, findet dort zusätzlich den Bereich "Mein Kurs" mit Fortschritt, Status, Punkten und Gruppen. Ist das Verlassen des Kurses erlaubt, steht dort auch die Aktion "Kurs verlassen".

Ist der Kurs die einzige Lernressource einer Durchführung im Course Planner, öffnet der Link die Infoseite dieser Durchführung. [:octicons-tag-16:{ title="ab Release 20.0 (OO-8511)" }](https://track.frentix.com/issue/OO-8511){:target="_blank"}

Welche Elemente die Infoseite zeigt und wo Sie sie einstellen, beschreibt [Allgemeine Funktionen: Infoseite](../learningresources/General_Functions_Infopage.de.md#content).

[Zum Seitenanfang ^](#toolbar_infopage)

---


## Infoseite drucken [:octicons-tag-16:{ title="ab Release 21.1 (OO-9299)" }](https://track.frentix.com/issue/OO-9299){:target="_blank"} {: #print}

Die Infoseite lässt sich drucken, etwa um eine Kursbuchung von der vorgesetzten Person bewilligen zu lassen. Klicken Sie im Kopf der Infoseite auf **Als PDF herunterladen**. OpenOlat erzeugt einen einspaltigen Flyer ohne Schaltflächen, mit einem QR-Code, der zum Angebot führt. Den gleichen Ausdruck erhalten Sie über den Befehl "Drucken" Ihres Browsers. Die Schaltfläche erscheint nur, wenn Administrator:innen einen PDF-Dienst eingerichtet haben; das Drucken über den Browser funktioniert immer.

Was der Ausdruck enthält und was er weglässt: [Infoseite drucken oder als PDF herunterladen](../learningresources/General_Functions_Infopage.de.md#print)

[Zum Seitenanfang ^](#toolbar_infopage)

---


## Über diesen Kurs [:octicons-tag-16:{ title="ab Release 21.1 (OO-9760)" }](https://track.frentix.com/issue/OO-9760){:target="_blank"} {: #about}

Wer einen Kurs verwaltet und die ID, den externen Link oder die Besitzer:innen nachschlagen möchte, findet diese Angaben nicht auf der Infoseite, sondern im Fenster "Über diesen Kurs". Sie öffnen es unter:<br>
`Kurs > Administration > Über diesen Kurs`

Bei anderen Lernressourcen heisst der Menüpunkt nach deren Typ, zum Beispiel "Über diesen Test" oder "Über dieses Formular", sonst "Über diese Lernressource". Den Menüpunkt sehen Besitzer:innen der Lernressource, Lernressourcenverwalter:innen und Administrator:innen. Teilnehmende und Betreuer:innen sehen ihn nicht.

![Bereiche Technische Informationen mit Id, Titel, Typ, Technischer Typ, Administrative Freigabe, Externer Link und Produkte sowie Verantwortliche mit Ersteller:in und Besitzer:innen](assets/info_page_about_dialog_v1_de.png){ class="shadow lightbox" title="Fenster Über diesen Kurs · 2026.09.29" }

### Technische Informationen {: #technical_information}

Der Bereich "Technische Informationen" zeigt die Angaben, die OpenOlat zur Lernressource führt:

- **Id**: die automatisch vergebene Nummer der Lernressource. Mit ihr finden Sie die Lernressource über die Suche.
- **Titel** und **Kennzeichen**: wie im Tab "Metadaten" der Einstellungen eingetragen.
- **Erstellungsdatum** und **Zuletzt geändert**
- **Typ** und **Technischer Typ**: bei Kursen zum Beispiel "Kurs" und "Lernpfad".
- **Administrative Freigabe**: die Organisationen, für welche die Lernressource freigegeben ist.
- **Externer Link**: der Link für den direkten Zugang. Ist ein Login oder eine Registrierung nötig, kommen diese Schritte vor dem Aufruf. Ist der Gastzugang erlaubt, steht darunter auch der **Externe Link - Gast**.
- **Produkte**: die Produkte und Durchführungen im Course Planner, in denen der Kurs eingebunden ist.

### Verantwortliche {: #responsible_persons}

Der Bereich "Verantwortliche" nennt die **Ersteller:in** der Lernressource und alle **Besitzer:innen**.

### Information zur Verwendung {: #usage}

Ist eine andere Lernressource, zum Beispiel ein Formular oder ein Test, in Kurse eingebunden, zeigt das Fenster zusätzlich den Bereich "Information zur Verwendung".

![Bereich Information zur Verwendung markiert, mit Referenz auf einen Kurs, letztem Zugriff, momentanen Benutzer:innen, Anzahl Aufrufe und Anzahl Exporte](assets/general_functions_infopage_usage_v2_de.png){ class="shadow lightbox" title="Fenster Über dieses Formular · 2026.09.29" }

**Referenzen**: Hier sehen Sie, welche Kurse diese Lernressource verwenden. Solange die Lernressource in einem Kurs verwendet wird, kann sie nicht gelöscht werden.

**Letzter Zugriff**: Gibt an, wann die Lernressource das letzte Mal gestartet wurde.

**Momentane Benutzer:innen**: Gibt an, wie viele Benutzer:innen diese Lernressource zurzeit in OpenOlat gestartet haben.

**Anzahl Aufrufe**: Zählt automatisch, wie oft die Lernressource insgesamt gestartet wurde.

**Anzahl Exporte**: Zählt automatisch, wie oft die Lernressource insgesamt heruntergeladen wurde.

[Zum Seitenanfang ^](#toolbar_infopage)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Allgemeine Funktionen: Infoseite >](../learningresources/General_Functions_Infopage.de.md)

**Weiterführend**<br>
[Kurseinstellungen >](../learningresources/Course_Settings.de.md)<br>
[Course Planner: Durchführungen >](../area_modules/Course_Planner_Implementations.de.md)<br>
[Zugangskonfiguration / Freigabe >](../learningresources/Access_configuration.de.md)

[Zum Seitenanfang ^](#toolbar_infopage)
