# Bewertungswerkzeug - Übersicht {: #assessment_tool_overview}

Das Bewertungswerkzeug ist die zentrale Stelle für die Bewertungen eines Kurses. Kursbesitzer:innen, Betreuende und Mitglieder mit dem Recht ["Bewertungs-Werkzeug"](../Members_management.de.md#right_assessment_tool) sehen hier alle bewertbaren Kursbausteine des Kurses und bewerten die Teilnehmenden.

Sie öffnen das Bewertungswerkzeug unter `Kurs > Administration > Bewertungswerkzeug`. Zuerst erscheint die Übersicht: Sie zeigt, wie der Kurs steht und welche Bewertungen und Aktionen anstehen. So sehen Sie schnell, was zu tun ist. Von der Übersicht aus gelangen Sie zu den Bewertungen der einzelnen Kursbausteine und Personen.

![Startseite des Bewertungswerkzeugs, die auf einen Blick zeigt, wie der Kurs steht, welche Prüfung ansteht und was noch zu bewerten oder freizugeben ist](../assets/assessment_tool_overview_v1_de.png){ class="shadow lightbox" title="Übersicht des Bewertungswerkzeugs · 2026.11.27" }

Die folgenden Abschnitte beschreiben zuerst die Bereiche der Übersicht, danach die weiteren Einträge im Menü links und die Buttons oben rechts.

## Steckbrief

Name | Bewertungswerkzeug
---------|----------
Verfügbar seit | Release 7.1 oder früher

## "Übersicht" des Bewertungswerkzeugs

### "Offene Bewertungen" (Übersicht)

Hier sehen Sie auf einen Blick, für wen Bewertungen offen sind und wie viele Kursbausteine bei der jeweiligen Person noch zu bewerten sind. Ist nur ein Kursbaustein offen, steht er direkt in der Liste. Ein Klick auf den Kursbaustein öffnet die Bewertung.

![28 offene Bewertungen, je Kursbaustein mit dem Namen der Person oder der Anzahl Teilnehmer:innen](../assets/offene_Bewertungen.jpg){ class="shadow lightbox" title="Bereich Offene Bewertungen" }

Die Übersicht zeigt nur die offenen Bewertungen, erledigte Bewertungen erscheinen hier nicht.

### "Freizugebende Bewertungen" (Übersicht)

Gibt es im Kurs Bewertungen, die für die Teilnehmenden noch nicht sichtbar sind, erscheinen sie hier.

![Zwei Bewertungen in einem Test und einer Portfolioaufgabe, welche die Teilnehmerin noch nicht sieht](../assets/freizugebende_Bewertungen.png){ class="shadow lightbox" title="Bereich Freizugebende Bewertungen" }

### "Teilnehmer:innen" (Übersicht)

Dieser Bereich zeigt, wie viele Teilnehmende, Gruppen und Curriculumelemente der Kurs hat.

Ist für den ganzen Kurs ein "Bestehen" konfiguriert, zeigt der Bereich, wie viele Kursmitglieder den Kurs bestanden und nicht bestanden haben. Sind im Kurs Punkte aktiviert, sehen Sie auch die Verteilung der Punkte.

![Anteil bestanden und Punkteverteilung der Teilnehmer:innen, darunter Mitglieder, Durchschnittspunkte und Bestanden je Gruppe und Curriculumelement](../assets/Uebersicht_Bewertungswerkzeug.jpg){ class="shadow lightbox" title="Bereich Teilnehmer:innen" }

### Prüfungsmodus (Übersicht)

Ist für den Kurs eine Prüfung im [Prüfungsmodus](../Assessment_mode.de.md) geplant oder läuft gerade eine Prüfung, zeigt das Bewertungswerkzeug sie in diesem Bereich an. Den Bereich gibt es, solange der Kurs eine Prüfung hat, die noch nicht beendet ist, und wenn Systemadministrator:innen den Prüfungsmodus in der System-Administration eingeschaltet haben: `Administration > e-Assessment > Prüfungsverwaltung > Segment "Prüfungsverwaltung Konfiguration"`, Schalter "Prüfungsmodus einschalten".

![Laufende Prüfung mit dem Button "Prüfung beenden" im Banner und im Bereich, darunter zwei geplante Prüfungen mit Beginn und Ende](../assets/Pruefng1_Bewertungswerkzeug1.jpg){ class="shadow lightbox" title="Bereich Prüfungsmodus" }

Ab dem Prüfungstag oder ab der Vorlaufzeit zeigt bei der Prüfung eine Zeile, wie viele der Personen, für die die Prüfung gilt, schon in OpenOlat sind, zum Beispiel "1 von maximal 2 Teilnehmer:innen warten auf Prüfungsstart." Was die beiden Zahlen zählen und wann die Zeile erscheint, beschreibt der Abschnitt [Wie viele Teilnehmende schon da sind](../Assessment_mode.de.md#participant_count).

Hat die Prüfung einen manuellen Start, zeigt der Bereich ab dem Prüfungstag den Button "Prüfung starten" und nach dem Start den Button "Prüfung beenden". Betreuer:innen sehen diese Buttons nur mit einem zusätzlichen Recht. Wer die Buttons sieht, beschreibt der Abschnitt [Wer eine Prüfung manuell starten und beenden kann](../Assessment_mode.de.md#start_stop_rights).

![Geplante Prüfung mit manuellem Start, eine von zwei Personen wartet, darunter der Button "Prüfung starten"](../assets/Pruefung_starten.jpg){ class="shadow lightbox" title="Bereich Prüfungsmodus vor dem Start" }

### "Benachrichtigungen"

Hier abonnieren Betreuende mit dem Schalter "Abonnieren" Benachrichtigungen per E-Mail: "Neue Testresultate" meldet neue Resultate in bewertbaren Kursbausteinen, "Neue Zertifikate" neu ausgestellte Zertifikate, sofern im Kurs Zertifikate aktiviert sind.

![Die Glocke bei "Neue Testresultate" öffnet das Abonnement mit dem Schalter "Abonnieren"](../assets/Benachrichtigungen_Bewertungswerkzeug20.jpg){ class="shadow lightbox" title="Benachrichtigungen im Bewertungswerkzeug" }

## Aufträge {: #orders}

Unter "Aufträge" sammelt das Bewertungswerkzeug alle Bewertungen, die im Kurs noch zu erledigen sind. So arbeiten Sie die anstehenden Bewertungen ab, ohne jeden Kursbaustein einzeln zu öffnen. Sie finden "Aufträge" im Menü links direkt unter "Übersicht". Drei Segmente teilen sie auf:

* **Offene Bewertungen:** Bewertungen im Status "Korrigieren": Die Person hat zum Beispiel eine Aufgabe abgegeben, und die Bewertung durch Sie steht noch aus. Mit "Bewerten" öffnen Sie die Bewertung der Person.
* **Offene Einstufungen/Noten:** Kursbausteine mit einer [Bewertungsskala](../Assessment_translate_points_in_grades.de.md), bei denen die Note von Hand zugewiesen wird und noch fehlt. Mit "Zuweisen" vergeben Sie die Note.
* **Freizugebende Bewertungen:** abgeschlossene Bewertungen, die noch nicht freigegeben sind. Erst mit der Freigabe sieht die Person ihre Bewertung. Mit "Freigeben" machen Sie ausgewählte Bewertungen für die Teilnehmenden sichtbar.

Im Segment "Offene Bewertungen" zeigt der Filter "Mir zugewiesen" nur die Personen, die Ihnen als Betreuer:in zugewiesen sind, etwa in einer Aufgabe mit eingeschalteter Option "Zuweisung Betreuende/Teilnehmende". In jedem Segment schreiben Sie den ausgewählten Personen mit "E-Mail". Kursübergreifend zeigt der Bereich "Coaching" in der Hauptnavigation dieselben Segmente unter [Bewertungsaufträge](../../area_modules/Coaching_Assessment_Orders.de.md).

![Menüeintrag Aufträge und die Segmente Offene Bewertungen, Offene Einstufungen/Noten und Freizugebende Bewertungen, geöffnet ist die Liste der offenen Bewertungen mit dem Link Bewerten](../assets/assessment_tool_overview_orders_v1_de.png){ class="shadow lightbox" title="Bereich Aufträge des Bewertungswerkzeugs · 2026.11.09" }

## Prüfungseinsicht [:octicons-tag-16:{ title="ab Release 18.2 (OO-7425)" }](https://track.frentix.com/issue/OO-7425)

Diesen Eintrag im Menü links sehen Sie, wenn für den Kurs eine Prüfungseinsicht konfiguriert ist, unter `Kurs > Administration > Prüfungsverwaltung > Segment "Konfiguration Prüfungseinsicht"`. Voraussetzung ist, dass die Prüfungseinsicht in der System-Administration unter `Administration > e-Assessment > Prüfungsverwaltung` eingeschaltet ist.

Betreuende fügen hier Teilnehmende hinzu und legen fest, auf welche Prüfung sich die Einsicht bezieht und wann die Einsicht möglich ist. Bei Bedarf vergeben sie einen Zugangscode und verschicken eine Infomail.

![Teilnehmende mit Test-Status, Einsichtszeitraum, Einsichtsdauer und Status Geplant, dazu der Button "Teilnehmer:in hinzufügen"](../assets/Pruefungseinsicht_Baustein1.jpg){ class="shadow lightbox" title="Segment Prüfungseinsicht eines Tests" }

Nähere Informationen finden Sie auf der Seite [Prüfungsverwaltung: Prüfungseinsicht](../Assessment_inspection.de.md).


## Übersicht der Bewertungsbausteine des Kurses

Im Menü links des Bewertungswerkzeugs stehen alle bewertbaren Kursbausteine. Wählen Sie dort einen Kursbaustein, stehen über seiner Ansicht zwei Schaltflächen nebeneinander, die Segmente "Übersicht" und "Teilnehmer:innen". Das aktive Segment ist hervorgehoben, ein Klick auf das andere wechselt die Ansicht darunter.

![Links das Menü mit Übersicht, Aufträge und den Kursbausteinen, rechts beim gewählten Test das aktive Segment Teilnehmer:innen mit der Liste der Teilnehmenden](../assets/assessing_tests_participants_buttons_v1_de.png){ class="shadow lightbox" title="Segment Teilnehmer:innen eines Tests im Bewertungswerkzeug" }

Das Segment "Übersicht" zeigt ähnliche Angaben wie die Übersicht des Bewertungswerkzeugs, aber für den einzelnen Kursbaustein, zum Beispiel die Punkteverteilung, die Anzahl der Bewertungen und das Bestehen.

### Segment Teilnehmer:innen {: #segment_participants}

Im Segment "Teilnehmer:innen" bewerten Sie: Sie wählen eine Person, erfassen Punkte und Feedback und geben die Bewertung frei. Die Tabelle zeigt den Bearbeitungsstand aller Teilnehmenden des Kursbausteins.<br>
Bei Aufgaben laden Sie im Segment "Teilnehmer:innen" auch alle abgegebenen Dokumente herunter.

Der oberste Kursbaustein steht im Menü links mit dem Titel des Kurses über den übrigen Kursbausteinen. Er zählt ebenfalls als bewertbarer Kursbaustein und entspricht einem Kursbaustein ["Struktur"](../Course_Element_Structure.de.md).<br>
Ein Klick auf eine Person beim obersten Kursbaustein zeigt den Bearbeitungsstand aller bewertbaren Kursbausteine dieser Person. Von dort öffnen Sie auch ihren [Leistungsnachweis](../../personal_menu/Evidence_of_Achievements.de.md), die Zusammenstellung ihrer Bewertungen im Kurs.

In dieser Ansicht laden Sie den Bearbeitungsstand der Person als PDF-Datei herunter: Der Button "PDF exportieren" oben rechts erzeugt die Datei jedes Mal neu, ihr Name beginnt mit "Leistungsnachweis". Den Button zeigt OpenOlat nur, wenn Systemadministrator:innen in der System-Administration den [PDF-Dienst](../../../manual_admin/administration/External_Tools_-_Administration/index.de.md#pdf_generator) eingerichtet haben: `Administration > Externe Werkzeuge > PDF Generator`.

Ist im Kurs ein [Zertifikat](../Course_Settings_Assessment_Certificate.de.md#certificate_issuer) eingeschaltet, zeigt dieselbe Ansicht den Abschnitt "Zertifikate" mit den Zertifikaten der Person. Dort stellen Sie mit dem Button "Zertifikat erzeugen" ein neues Zertifikat aus. Den Button gibt es, wenn beim Feld "PDF Zertifikat erzeugen" die Option "Manuell durch Betreuer:in" gewählt ist: `Kurs > Administration > Einstellungen > Tab "Bewertung"`, Abschnitt "Zertifikat". Fehlt bei einem ausgestellten Zertifikat die PDF-Datei, erzeugen nur Systemadministrator:innen sie neu, in der System-Administration unter `Administration > e-Assessment > Zertifikate > Segment "Wartung"`. Wie das geht, steht im [Administrationshandbuch](../../../manual_admin/administration/e-Assessment_Certificates.de.md#tab_maintenance).

Ist auf dem obersten Kursbaustein eine [Punkteberechnung](../Course_Settings_Assessment/index.de.md#section_assessment_settings) eingerichtet, zeigt die oberste Ebene die Gesamtpunkte des Kurses. Mit dem Symbol "Herunterladen" über der Tabelle laden Sie die Tabelle mit den Gesamtpunkten aller Teilnehmenden als Excel-Datei herunter.

!!! tip "Tipp"

    Mit den Filtern zeigen Sie nur bestimmte Teilnehmende in der Tabelle. Über das Zahnrad wählen Sie die Spalten, die Sie brauchen.

Wie Sie bewerten, beschreiben die Seiten ["Bewertung von Kursbausteinen"](../Assessment_of_course_modules.de.md) und ["Lernende bewerten"](../Assessment_of_learners.de.md).

!!! info "Wichtig"

    Ist für Teilnehmende eine Prüfungseinsicht aktiviert, hat der betreffende Kursbaustein zusätzlich das Segment "Prüfungseinsicht".

Das Segment "Teilnehmer:innen" beschreibt die Seite ["Bewertungswerkzeug: Teilnehmer:innen"](../Assessment_tool_tab_Users.de.md) im Detail.

## Daten zurücksetzen [:octicons-tag-16:{ title="ab Release 17.2.4 (OO-6792)" }](https://track.frentix.com/issue/OO-6792) {: #course_reset}

Mit dem Button "Daten zurücksetzen" oben rechts setzen Sie die Daten von Teilnehmer:innen zurück. Ein Wizard führt Sie durch die Auswahl: den ganzen Kurs oder einzelne Kursbausteine, alle oder ausgewählte Teilnehmer:innen.

[Mehr dazu >](../Assessment_tool_reset_data.de.md)


## Massenbewertung [:octicons-tag-16:{ title="ab Release 9.2 (OO-852)" }](https://track.frentix.com/issue/OO-852) {: #mass_assessment}

Müssen Sie viele Teilnehmer:innen auf einmal bewerten, etwa nach einer Prüfung auf Papier, nehmen Sie die Massenbewertung. Sie übermitteln Punkte, Status, Kommentare und Rückgabedateien für mehrere Teilnehmer:innen in einem Schritt, statt jede Person einzeln zu öffnen.

Sie öffnen die Massenbewertung mit dem Button "Massenbewertung" oben rechts im Bewertungswerkzeug. Die Seite "Geplante Massenbewertungen" listet die Massenbewertungen, die noch ausgeführt werden. Mit "Neue Massenbewertung starten" öffnen Sie den Wizard. Im Wizard wählen Sie den Kursbaustein, laden die Daten hoch und legen fest, ob OpenOlat die Bewertung "Sofort" oder "Später, nach Datum" ausführt. Zur Auswahl stehen die Kursbausteine "Bewertung", "Aufgabe", "Gruppenaufgabe" und "Videoaufgabe", wenn sie Punkte, Bestanden, einen Kommentar oder Rückgabedateien vorsehen.

Im Schritt "Bewertungsdaten" fügen Sie die Werte zeilenweise ein, getrennt durch Tabulator oder Komma, zum Beispiel aus Excel kopiert. Rückgabedateien sind Dateien, die Teilnehmende bei einer Aufgabe als Korrektur zurückerhalten. Sie laden sie als ZIP-Archiv mit einem Unterordner je Person hoch.

Den Button sehen alle Personen, die das Bewertungswerkzeug öffnen. Ausgenommen sind Personen, die den Kurs nur in der Rolle [Principal](../../basic_concepts/Roles/index.de.md#org) öffnen, also nur lesend, ohne Mitglied zu sein oder den Kurs zu administrieren.

![Erster Schritt "Kursbaustein auswählen" mit den bewertbaren Kursbausteinen des Kurses und dem Link "Wählen"](../assets/Massenbewertung_wizard.png){ class="shadow lightbox" title="Assistent Massenbewertung" }

Schritt für Schritt beschreibt die Anleitung ["Wie und wo kann ich eine Massenbewertung vornehmen?"](../../../manual_how-to/bulk_assessment/bulk_assessment.de.md) die Massenbewertung.

## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Prüfungsverwaltung: Übersicht >](../Assessment_Management/index.de.md)<br>
[Mitgliederverwaltung >](../Members_management.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../../basic_concepts/Roles/index.de.md)

[Zum Seitenanfang ^](#assessment_tool_overview)