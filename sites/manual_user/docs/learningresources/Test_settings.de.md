# Test Einstellungen - Administration {: #test_settings}

Im Bereich `Test > Administration` finden Sie, ähnlich wie bei anderen Lernressourcen, weitere Menüs. Hier konfigurieren Sie den Test näher. Besonders wichtig sind dabei die Menüs "Einstellungen" und "Inhalt editieren". Den Bereich sehen Besitzer:innen der Lernressource, Lernressourcenverwalter:innen und Administrator:innen.

![Zehn Einträge von "Einstellungen" bis "Test löschen", davon "Angebotsarten" ausgegraut, im aufgeklappten Menü Administration einer veröffentlichten Test-Lernressource.](assets/test_administration_menu_v1_de.png){ class="shadow lightbox" }

Die grundsätzliche Konfiguration des gesamten Tests erfolgt grösstenteils in den **"Einstellungen"**, besonders im Tab "Optionen" (siehe unten).

Das Menü **"Mitgliederverwaltung"** ist besonders dann relevant, wenn der Test kursunabhängig verwendet werden soll, ansonsten erfolgt die Mitgliederverwaltung der Test-Teilnehmenden über den verbundenen Kurs. 

Unter "Inhalt editieren" gelangen Sie in den Testeditor. Hier legen Sie den eigentlichen Test an.

!!! note "Testeditor QTI 2.1"
    Übersicht zum Testeditor.<br>
    [Inhalt editieren](Test_editor_QTI_2.1.de.md)

Das **"Bewertungswerkzeug"** des Tests erscheint nur, wenn der Test kursunabhängig verwendet werden soll: `Test > Administration > Einstellungen > Tab "Freigabe"`, Verwendungszweck "Eigenständige".

Im Menü **"Korrektur-Workflow"** können für den Test Korrektor:innen hinzugefügt werden (siehe unten). 

Das Menü **"Test Statistiken"** erscheint nur bei unabhängigen Tests, ansonsten werden die Test Statistiken im jeweiligen Kursmenü angezeigt.

Das Menü **"Angebotsarten"** ist nur aktiv, wenn der Test buchbar konfiguriert wurde.

Mit Hilfe eines Wizards können basierend auf dem Online-Test unter **"Handschriftliche Prüfungen generieren"** Prüfungen für den Druck erzeugt werden (siehe unten). Der Eintrag erscheint nur, wenn der PDF Generator eingeschaltet ist. Sie finden ihn in der System-Administration unter: `Administration > Externe Werkzeuge > PDF Generator`.

Über die Menüs "Kopieren", "Inhalt exportieren" und "Als Worddatei exportieren" können die Tests kopiert bzw. gespeichert werden. 

**"Test löschen"** löscht die Lernressource Test. Sie finden sie anschliessend im Autorenbereich im Tab "Gelöscht".

Auf dieser Seite finden Sie nähere Erläuterungen zu folgenden Administrationsmenüs der Lernressource Test:

* Einstellungen
* Korrektur-Workflow
* Handschriftliche Prüfungen generieren
* Als Worddatei exportieren

[zum Seitenanfang ^](#test_settings)

---


## "Einstellungen" eines Tests {: #settings}

Wichtig für Tests ist vor allem der Tab "Optionen". Hier konfigurieren Sie den gesamten Test.  

![Fünf Tabs "Info", "Metadaten", "Freigabe", "Katalog" und "Optionen", davon "Optionen" aktiv, rechts vom angewählten Eintrag Einstellungen im Menü Administration einer Test-Lernressource.](assets/Test_menu_settings_DE.png){ class="shadow lightbox" }

Darüber hinaus können in den weiteren Tabs "Info", "Metadaten", "Freigabe" und "Katalog" weitere Einstellungen der Lernressource vorgenommen werden. Achten Sie hier besonders darauf, dass die eingestellte Lizenzangabe unter "Metadaten" Ihren Vorstellungen entspricht.

### Tab Optionen [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-8321)" }](https://track.frentix.com/issue/OO-8321)

Im Tab "Optionen" legen Sie fest, wie Teilnehmende den Test durchlaufen: wie viele Versuche sie haben, was ihnen während des Tests angezeigt wird und was sie nach dem Abschluss zu sehen bekommen.

!!! info "Wichtig"
    Die Einstellungen, welche unter Optionen vorgenommen werden, werden beim Einbinden des Tests in einen [Kurs](Tests_at_course_level.de.md) automatisch übernommen und können falls gewünscht im jeweiligen Kursbaustein Test im Kurseditor in den Tabs "Test-Konfiguration" bzw. "Optionen" angepasst werden.

    Ob die Ergebnisse auf der Test-Startseite im Kurs dargestellt werden, wird ebenfalls direkt im Kurs konfiguriert.

#### Standardeinstellungen {: #default_settings}

Hier wählen Sie eine vorkonfigurierte Auswahl von typischen Einstellungen für unterschiedliche Nutzungssituationen von Tests.

Entscheiden Sie z. B., ob es sich um einen summativen oder formativen Test handelt, oder verwenden Sie eine andere voreingestellte Konfiguration. Das erleichtert es gerade unerfahrenen Autoren schnell zu einer passenden Einstellung zu gelangen. Spätere Änderungen und individuelle Anpassungen sind aber weiterhin möglich.

![Auswahlliste mit "Profil wählen...", "Summativ (scharfe Prüfung)" und "Formativ (Übungstest)" sowie der Button "Konfiguration übernehmen", im Feld Standardeinstellungen des Tabs Optionen.](assets/Test_Standardeinstellungen_DE.png){ class="shadow lightbox" }

#### Anzahl der Testversuche einschränken {: #limit_attempts}

Aktivieren Sie diese Option, um die Anzahl der möglichen Lösungsversuche für einen Test zu limitieren. Tragen Sie im Feld "Max. Anzahl Versuche" die gewünschte Anzahl ein. Der Wert kann maximal 20 betragen.

#### Erster bestandener Lösungsversuch zählt {: #block_after_success}

Sobald das Ergebnis "bestanden" erreicht wird, können Teilnehmende den Test nicht noch einmal durchführen.

#### Anonyme Benutzer:innen (Gäste) erlauben {: #guest}

Personen ohne OpenOlat Account können ebenfalls den Test absolvieren. Gäste können den Test jedoch nicht unterbrechen. Es werden nur abgeschlossene Tests gezählt. Die Resultate stehen ebenfalls in der Teststatistik zur Verfügung.

#### Nur Modul anzeigen, LMS ausblenden {: #hide_lms}

Diese Auswahl wird gewählt, um zu verhindern, dass Teilnehmende während eines Tests auf andere OpenOlat-Funktionen Zugriff haben. OpenOlat wird dabei ausgeblendet und erst wieder nach Beenden des Tests angezeigt.

#### Fragetitel anzeigen {: #show_question_titles}

Markieren Sie die Checkbox, um den Teilnehmenden die Titel der Fragen anzuzeigen. Wenn die Titel nicht angezeigt werden sollen, aber die Navigation aktiviert ist, dann erscheint in der Menü-Navigation ein anonymisierter Titel.  

#### Menu-Navigation anzeigen {: #show_menu}

Wenn Sie die Menu-Navigation _nicht_ erlauben:

* ist am Test "nicht lineare Navigation" eingestellt, kann die Navigation unterhalb der Frage über einen Button aufgerufen werden, um eine andere Frage auszuwählen.
* ist am Test "lineare Navigation" eingestellt, erscheint nach dem Abschicken einer Antwort automatisch die nächste Frage und Teilnehmende können nicht zu anderen Fragen navigieren.

#### Persönliche Notizen {: #notes}

Sie können den Teilnehmenden erlauben, während des Tests persönliche Notizen zu erstellen, die nach Abschluss des Tests nicht mehr zur Verfügung stehen.

#### Anzahl Fragen und Fortschritt im Test anzeigen {: #question_progress}

Markieren Sie die Checkbox, um den Teilnehmenden die Anzahl Fragen anzuzeigen.

#### Anzahl Punkte und Punktestand im Test anzeigen {: #score_progress}

Markieren Sie die Checkbox, um den Teilnehmenden ihre momentane Punktezahl im Testverlauf anzuzeigen.

#### Max. Punkte der Frage anzeigen {: #max_score_question}

Ist die Checkbox markiert, werden die maximal erreichbaren Punkte pro Frage im Test angezeigt.

#### Unterbrechen erlauben {: #allow_suspend}

Das Ankreuzen der Checkbox bewirkt, dass Teilnehmende den Test unterbrechen können. Hierbei werden die bisherigen Antworten gespeichert und sie haben die Möglichkeit zu einem späteren Zeitpunkt mit der Beantwortung der Fragen fortzufahren.

#### Abbrechen erlauben {: #allow_cancel}

Mit dem Ankreuzen der Checkbox erlauben Sie den Teilnehmenden den Test abzubrechen, ohne dass die Antworten gespeichert werden.

#### Testquittung erstellen {: #digital_signature}

Wenn diese Option angewählt wird, wird nach Beenden des Tests eine Testquittung erstellt, welche als XML-File heruntergeladen werden kann. Es dient der Verifizierung des Tests.

![Markierte Zeile "Testquittung" mit dem Link "Herunterladen" und dem Erstellungsdatum, darüber Anzahl Versuche, Punktzahl und Status, in der Leistungsübersicht eines abgeschlossenen Tests.](assets/Testquittung_DE.png){ class="shadow lightbox" }

Wenn die Option "Testquittung erstellen" ausgewählt ist, kann die Option "Testquittung per Mail schicken" zusätzlich aktiviert werden. Das erstellte XML-File wird dann zusätzlich per Mail an die Teilnehmenden verschickt.

#### Feedbacks anzeigen {: #show_feedbacks}

Solange diese Checkbox ausgewählt ist, werden die Feedbacks im Testverlauf angezeigt. Wenn die Checkbox nicht mehr ausgewählt ist, werden keine Feedbacks mehr angezeigt. Dies betrifft die Feedbacks aller Frageitems und auch das Feedback, welches auf der Ebene Test hinzugefügt werden kann. Die einzelnen Feedbacks werden im Testeditor konfiguriert.

#### Resultate nach Abgabe des Tests anzeigen {: #results}

Wenn diese Checkbox ausgewählt ist, wird das Resultat nach Beenden des Tests angezeigt. Was genau angezeigt wird, wählen Sie darunter unter "Übersicht Resultate":

* **Testzusammenfassung**: Die Metadaten des gesamten Tests werden als Zusammenfassung angezeigt (inkl. Punkte und Bestanden/Nicht bestanden).
* **Sektionszusammenfassung**: Die Metadaten der Sektion werden als Zusammenfassung angezeigt.
* **Fragezusammenfassung**: Die Metadaten jeder einzelnen Frage werden angezeigt.
* **Antwort, von Teilnehmer:in abgegeben**: Es wird die Fragestellung zusammen mit der Antwort der teilnehmenden Person angezeigt.
* **Lösung**: Es wird die Fragestellung zusammen mit der korrekten Lösung angezeigt. Wenn im Tab Feedback eine korrekte Lösung hinterlegt ist, wird diese in der Resultatansicht mit dieser Option auch angezeigt.

## Korrektur-Workflow [:octicons-tag-16:{ title="ab Release 15.0 (OO-4442)" }](https://track.frentix.com/issue/OO-4442) {: #correction-workflow}

Um einem Test weitere, auch kursübergreifende, Korrektor:innen hinzufügen zu können, muss unter `Test > Administration > Korrektur-Workflow` die Korrektur eingeschaltet werden. Anschliessend können die Korrektor:innen hinzugefügt, Korrekturaufträge vergeben und weitere Einstellungen vorgenommen werden.

### Tab "Konfiguration"

Hier wird die externe Korrektur grundsätzlich eingeschaltet. Anschliessend kann definiert werden ob die Prüflinge anonym oder mit sichtbarem Namen bewertet werden. Der Korrekturzeitraum gibt die maximale Zeit an, die der Korrektor:in zur Verfügung steht.

Die jeweiligen Korrektor:innen werden automatisch benachrichtigt, wenn neue Bearbeitungen des Tests vorliegen. Die Benachrichtigung kann entweder direkt nach Testabschluss oder einmal pro Tag verschickt werden. Hierfür kann ein passender Mailtext hinterlegt werden oder eine Vorlage ("Vorlage Sprache wählen") verwendet werden. Nach der ersten Mailbenachrichtigung können noch zwei Erinnerungsmails in selbst definierten Abständen (Tagen) verschickt werden.

### Tab "Korrektor:innen"

![Button "Korrektor:in hinzufügen" sowie die Tabs "Konfiguration" und "Korrekturaufträge" im geöffneten Tab "Korrektor:innen" des Menüs Korrektur-Workflow einer Test-Lernressource.](assets/grading_workflow_tab_correctors_v1_de.png){ class="shadow lightbox" }

Hier werden die Personen hinzugefügt, die einen Test bewerten sollen. Dabei ist es egal, welche Rolle die Person in OpenOlat besitzt. Auch Personen mit der Rolle "Benutzer:in" können als Korrektor:in hinzugefügt werden. Über das Zeilenmenü einer Korrektor:in stehen weitere Aktionen bereit: "Zuweisungen anzeigen", "Korrektor:in kontaktieren", "Report herunterladen", "Deaktivieren" beziehungsweise "Aktivieren", "Abwesenheit erfassen" und "Entfernen".

Die eingetragenen Korrektor:innen finden ihre Aufträge unter `Coaching > Bewertungsaufträge` im Tab [Korrekturaufträge](../area_modules/Coaching_Assessment_Orders.de.md#tab_grading_assignments). Dafür braucht es zwei weitere Schritte: Am Kursbaustein Test steht die Korrektur auf "Manuell durch Korrektor:innen", und eine teilnehmende Person schliesst den Test ab. Erst damit ist der Auftrag erstellt.

Ist zu diesem Zeitpunkt keine Korrektor:in verfügbar, trägt der Auftrag den Status "Nicht zugeordnet" und wartet in der [Auftragsverwaltung](../area_modules/Coaching_Order_Management.de.md). Dort weisen ihn Lernressourcenverwalter:innen einer Person zu, und er erscheint in deren Liste.

### Tab "Korrekturaufträge"

Hier kann der Bearbeitungsstand der Korrekturaufträge der unterschiedlichen Korrektor:innen angezeigt und nach verschiedenen Kriterien gefiltert werden.

### Report / Excel-Export [:octicons-tag-16:{ title="ab Release 21.0 (OO-9569)" }](https://track.frentix.com/issue/OO-9569)

Den Report ziehen Besitzer:innen der Test-Lernressource, Lernressourcenverwalter:innen und Administrator:innen, entweder hier oder kursübergreifend unter `Coaching > Auftragsverwaltung`. Korrektor:innen sehen ihre eigenen Aufträge unter `Coaching > Bewertungsaufträge` und laden dort keinen Report herunter.

Im Tab "Korrektor:innen" öffnen Sie im Zeilenmenü einer Korrektor:in den Eintrag "Report herunterladen". OpenOlat erzeugt daraus eine Excel-Datei mit dem Stand der Korrekturaufträge dieser Korrektor:in. Vor dem Download legen Sie den Umfang fest:

* Der Schalter "Nur erledigte Aufträge" ist eingeschaltet und beschränkt den Report auf abgeschlossene Korrekturaufträge. Schalten Sie ihn aus, umfasst der Report alle Korrekturaufträge ohne Einschränkung auf einen Zeitraum.
* Solange der Schalter eingeschaltet ist, grenzen Sie den Zeitraum über die "Vordefinierten Zeiträume" "Letzter Monat" und "Letztes Jahr" oder über das Pflichtfeld "Erledigt am" ein. Beide Datumsfelder müssen gefüllt sein.

![Schalter "Nur erledigte Aufträge" eingeschaltet, die Buttons "Letzter Monat" und "Letztes Jahr" und das Pflichtfeld "Erledigt am" mit zwei Datumsfeldern, vor dem Herunterladen des Reports.](assets/grading_report_export_dialog_v1_de.png){ class="shadow lightbox" }

Im Tab "Korrekturaufträge" erzeugt der Button "Bericht" denselben Report über die dort angezeigten Korrekturaufträge.

Der Report weist zu jedem Korrekturauftrag den Status ("Nicht zugeordnet", "Zugeteilt", "Erledigt"), das "Fälligkeitsdatum", das Datum "Erledigt am" sowie die Kennzeichnung "Frist abgelaufen" aus.

Die erzeugte Excel-Datei enthält die Worksheets "Korrektoren", "Assignments" und "Archive". Das Worksheet "Archive" führt archivierte Korrekturauftrag-Einträge auf, deren Auftragsdatensatz inzwischen entfernt wurde (etwa weil ein Prüfling, ein Korrektor:in oder die Test-Lernressource gelöscht wurde), inklusive Korrekturzeit und dem Datum "Erledigt am" für die Abrechnung. [:octicons-tag-16:{ title="ab Release 21.0 (OO-6914)" }](https://track.frentix.com/issue/OO-6914)

![Spalten "Kurs", "Kennzeichen", "Korrektur (Minuten)", "Korrektur (echte Minuten)" und "Erledigt am", davor Name und Anmeldename von Korrektor:in und Prüfling, im Worksheet "Archive".](assets/grading_report_archive_v1_de.png){ class="shadow lightbox" }

!!! note "Coaching Tool"
    Weitere Informationen zur kursübergreifenden Korrektur.<br>
    [Coaching Tool](../area_modules/Coaching.de.md)

[zum Seitenanfang ^](#test_settings)

---


## Handschriftliche Prüfungen generieren {: #create_paper_pencil}

Wenn Sie offline eine Prüfung durchführen wollen, können Sie in diesem Wizard ein Deckblatt und verschiedene Versionen von Ihrer Testressource mit zufällig gewählten Antworten generieren lassen.

1. In den Optionen wählen Sie die Sprache und die Anzahl der Tests sowie einen Präfix für die Dateinamen aus. Sie können auch bestimmen, ob Sie ein Deckblatt oder auch eine zusätzliche Seite mitgenerieren wollen.

    ![Felder "Anzahl der Tests", "Ausgangsprache" und "Seriennummer" sowie die Auswahl von Deckblatt und zusätzlicher Seite, im Schritt Optionen des Wizards "Handschriftliche Prüfungen generieren".](assets/Test_offline_options_DE.png){ class="shadow lightbox" }

2. Im zweiten Schritt wählen Sie die Attribute, die auf das Deckblatt kopiert werden sollen. Manche Attribute, wie die Beschreibung der Testressource, sind noch anpassbar.

    ![Attributgruppen Allgemeines und Testparameter zur Auswahl für das Deckblatt, im Schritt Deckblattattribute des Wizards "Handschriftliche Prüfungen generieren".](assets/Test_offline_Deckblattattribute_DE.png){ class="shadow lightbox" }

3. Hier ist die Möglichkeit, bestimmte Felder zu markieren und zu überschreiben. Das Beschreibungsfeld wird von der Testressource herüberkopiert und lässt sich hier nochmals anpassen.

    ![Die Felder "Titel" und "Verfahren" sowie das Beschreibungsfeld mit HTML-Editor, überschreibbar für das Deckblatt, im Schritt Deckblattfelder des Wizards "Handschriftliche Prüfungen generieren".](assets/Test_offline_Deckblattfelder_DE.png){ class="shadow lightbox" }

4. Haben Sie im Schritt "Optionen" die Option "Zusätzliche Seite" aktiviert, erscheint hier der Schritt "Zusätzliche Seite".

5. Die Zusammenfassung beinhaltet eine Übersicht aller getätigten Einstellungen sowie eine Vorschau der zu generierenden Tests. Bitte beachten Sie, dass eine grössere Anzahl von Generierungen etwas dauern kann und der Browser möglicherweise nicht immer reagiert.

    ![Anzahl Tests, Dateiformat, Ausgabesprache und Seriennummer sowie die Buttons "Vorschau" und "Vorschau mit Lösungen", im Schritt Zusammenfassung des Wizards "Handschriftliche Prüfungen generieren".](assets/Test_offline_Zusammenfassung_DE.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#test_settings)

---


## Als Worddatei exportieren {: #export_word}

Der Test wird dann im Zip-Format mit zwei Word-Dateien heruntergeladen, von denen eine Datei nur die Fragen, die andere zusätzlich noch die Lösungen enthält. Die exportierte Datei enthält alle wichtigen Informationen zum Test inklusive der Punktzahl, so dass Sie das Dokument direkt auch weiterverwenden können.

[zum Seitenanfang ^](#test_settings)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Testeditor >](Test_editor_QTI_2.1.de.md)<br>
[Tests auf Kursebene >](Tests_at_course_level.de.md)<br>
[Coaching - Bewertungsaufträge >](../area_modules/Coaching_Assessment_Orders.de.md)<br>
[Coaching - Auftragsverwaltung >](../area_modules/Coaching_Order_Management.de.md)<br>
[Coaching - Übersicht >](../area_modules/Coaching.de.md)

**Weiterführend**<br>
[Wie gehe ich vor, wenn ich einen Test erstelle? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md)<br>
[Wie bewerte ich einen Test? >](../../manual_how-to/assessing_tests/assessing_tests.de.md)<br>
[Wie macht man in OpenOlat eine anonyme Test-Korrektur? >](../../manual_how-to/assessing_tests_anonymously/assessing_tests_anonymously.de.md)<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview.de.md)

[zum Seitenanfang ^](#test_settings)