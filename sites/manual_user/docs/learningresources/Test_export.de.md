# Tests exportieren {: #test_export}


Beim Exportieren von Tests ist zu unterscheiden zwischen

- Test-**Kurs** (Prüfungskurs) exportieren
- Test-**Lernressource** exportieren
- einzelne **Fragen** exportieren
- Test-**Ergebnisse** exportieren


## Kurs exportieren {: #export_course}

Ein gesamter Kurs, z.B. ein Prüfungskurs, kann als zip-Datei exportiert werden in der Kurs-Administration unter:<br>`Kurs > Administration > Inhalt exportieren`

![Menüpunkt Inhalt exportieren im geöffneten Menü Administration markiert, damit wird der ganze Kurs als zip-Datei exportiert](assets/test_export_course_content_v1_de.png){ class="shadow lightbox" title="Menü Administration eines Kurses" }

[Zum Seitenanfang ^](#test_export)

---


## Test-Lernressource exportieren {: #export_learning_resource}

Test-Lernressourcen enthalten ganze Fragenbündel und können als Fragenpäckchen inklusive Konfiguration (Gesamtpunktzahl usw.) in Test-Kursbausteine eingebunden werden.
Auch eine Test-Lernressource kann exportiert werden in der Administration der Lernressource unter:<br>`Test > Administration > Inhalt exportieren`

![Menüpunkt Inhalt exportieren im geöffneten Menü Administration markiert, damit wird die Test-Lernressource als zip-Datei exportiert](assets/test_export_resource_content_v1_de.png){ class="shadow lightbox" title="Menü Administration einer Test-Lernressource" }

!!! tip "Tipp"

    Achten Sie darauf, ob Sie sich in der Administration eines Kurses oder einer Test-Lernressource befinden. Im Kurs heisst der Eintrag zum Editor **Kurseditor**, in der Test-Lernressource **Testeditor**.


[Zum Seitenanfang ^](#test_export)

---


### Als Worddatei exportieren {: #word}

Test-Lernressourcen können als Word-Dokument exportiert werden. Oft werden solche Dateien für Review-Zwecke vor Durchführung eines Tests erstellt, damit man darin auf einfache Art Ergänzungen und Korrekturen notieren kann.

![Menüpunkt Als Worddatei exportieren im geöffneten Menü Administration markiert](assets/test_export_resource_word_v1_de.png){ class="shadow lightbox" title="Menü Administration einer Test-Lernressource" }

[Zum Seitenanfang ^](#test_export)

---


### Handschriftliche Prüfungen generieren

Die Word-Dokumente, die mit dieser Option unter `Test > Administration > Handschriftliche Prüfungen generieren` einer Test-Lernressource erstellt werden, unterscheiden sich von einem einfachen Word-Export.

![Menüpunkt Handschriftliche Prüfungen generieren im geöffneten Menü Administration markiert](assets/test_export_resource_test_manually1_v1_de.png){ class="shadow lightbox" title="Menü Administration einer Test-Lernressource" }

Jedes Dokument erhält ein Deckblatt, sowie eine Seriennummer, so dass nach dem handschriftlichen Ausfüllen des Tests durch die Teilnehmenden eine klare Zuordnung möglich ist.

Sie müssen deshalb zwingend eine Anzahl für die zu erzeugenden Word-Dateien angeben.

![Felder Anzahl der Tests, Ausgangssprache für Export, Seriennummer mit Präfix und Deckblatt mit erster und zusätzlicher Seite](assets/test_export_resource_test_manually2_v1_de.png){ class="shadow lightbox" title="Schritt Optionen im Dialog Handschriftliche Prüfungen generieren" }

Für das Deckblatt können verschiedene Attribute ausgewählt werden.

![Kontrollkästchen für Seriennummer, Platzhalter für Name, Kandidatennummer und Datum sowie die Testparameter Zeit, Anzahl Fragen, Punktzahl, Punkteschwelle und Beschreibung](assets/test_export_resource_test_manually3_v1_de.png){ class="shadow lightbox" title="Schritt Deckblattattribute im Dialog Handschriftliche Prüfungen generieren" }

Auch ein Beschreibungstext kann angegeben werden.

![Felder Titel, Verfahren und Informationen mit Texteditor für den Hinweistext auf dem Deckblatt](assets/test_export_resource_test_manually4_v1_de.png){ class="shadow lightbox" title="Schritt Deckblattfelder im Dialog Handschriftliche Prüfungen generieren" }

**Deckblatt Beispiel:**

![Seriennummer, Titel, leere Felder für Vorname, Nachname, Kandidatennummer und Datum, darunter die Testparameter und die Hinweise zur Prüfung](assets/test_export_resource_test_manually6_v1_de.png){ class="shadow lightbox" title="Erzeugtes Deckblatt einer handschriftlichen Prüfung" }


[Zum Seitenanfang ^](#test_export)

---


## Einzelne Fragen exportieren

In OpenOlat erstellte Fragen entsprechen dem QTI-Standard. Sie können dadurch auch in andere LMS übertragen werden, die Fragen im QTI-Standard verwenden. Umgekehrt kann OpenOlat auch Fragen im QTI-Format importieren. 

### Zum Pool exportieren

Befinden Sie sich im Editor einer Test-Lernressource, wählen Sie die gewünschte Frage aus und klicken auf das Icon mit den 3 Punkten rechts oben um die Frage in den Pool zu exportieren.

![Menü mit drei Punkten rechts oben bei der Frage mit dem Eintrag Zum Pool exportieren markiert](assets/test_export_question_to_pool_v1_de.png){ class="shadow lightbox" title="Frage im Testeditor" }

!!! tip "Tipp"

    Auf diese Art können Sie auch eine ganze Sektion mit mehreren Fragen in den Fragenpool exportieren. Wählen Sie einfach links die Sektion aus und klicken Sie dann auf die 3 Punkte.


[Zum Seitenanfang ^](#test_export)


---

### Einzelne Frage aus dem Pool exportieren

Haben Sie eine einzelne Frage im Frageneditor geöffnet, finden Sie unter dem Icon "Freigeben" eine Möglichkeit zum Export dieser Einzelfrage in eine zip-Datei. Da die Fragen in OpenOlat dem QTI-Standard entsprechen, kann die zip-Datei in einem anderen OpenOlat oder einem anderen LMS, das ebenfalls den QTI-Standard benutzt, wieder importiert werden.  

![Icon Freigeben mit dem geöffneten Eintrag Export markiert, damit wird die Frage als zip-Datei exportiert](assets/test_export_single_question_from_pool_v1_de.png){ class="shadow lightbox" title="Frage im Fragenpool" }

[Zum Seitenanfang ^](#test_export)

---


### Mehrere ausgewählte Einzelfragen aus dem Pool exportieren

Haben Sie mehrere Fragen im Fragenpool ausgewählt, können diese Fragen gemeinsam in einer Word-Datei für die offline Prüfung, in einer QTI-2.1-Testdatei für den Austausch mit anderen kompatiblen LMS oder in einer zip-Datei für den Austausch mit anderen OpenOlat-Systemen oder zur Archivierung exportiert werden.

![Drei ausgewählte Fragen und der Button Export über der Liste markiert](assets/test_export_several_questions_from_pool1_v1_de.png){ class="shadow lightbox" title="Liste Alle Fragen im Fragenpool" }


![Auswahlliste Typ mit Word-Datei für offline Prüfung, QTI 2.1 Testdatei für andere LMS und ZIP-Datei für andere OpenOlat-Systeme oder die Archivierung](assets/test_export_several_questions_from_pool2_v1_de.png){ class="shadow lightbox" title="Schritt Typ im Dialog Export" }

[Zum Seitenanfang ^](#test_export)

---


## Testergebnisse exportieren {: #export_results}

### Teststatistiken

Eine Möglichkeit zur Auswertung der Testergebnisse, ist die in Statistiken aufbereitete Form. Verwenden Sie dazu den **Button "Test Statistiken"** innerhalb des Tab "Teilnehmer:innen". Der Button steht Betreuer:innen und Besitzer:innen zur Verfügung, wenn sie einen Kursbaustein "Test" im Run-Mode anwählen.

![Button Test Statistiken über der Liste der Teilnehmenden markiert](assets/test_export_statistics1_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen des Kursbausteins Test" }

* Sie können die verschiedenen Statistiken zu den Testergebnissen ausdrucken (evtl. auch in eine PDF-Datei "drucken") oder die Rohdaten als Excel-Datei herunterladen.
* Wenn Sie die Sektionen eines Tests aufklappen, können Sie detaillierte Statistiken zu jeder einzelnen Frage abrufen. 

![Buttons Drucken und Rohdaten herunterladen, links die aufklappbare Sektion, rechts die Kennzahlen des Tests und das Diagramm Punkteverteilung](assets/test_export_statistics2_v1_de.png){ class="shadow lightbox" title="Test Statistiken im Kursbaustein Test" }


### Testresultate der Teilnehmenden [:octicons-tag-16:{ title="ab Release 16.2 (OO-5974)" }](https://track.frentix.com/issue/OO-5974)

Mit dem **Button "Resultate exportieren"** wird eine zip-Datei erstellt, die sämtliche Testresultate aller Teilnehmenden im ausgewählten Kursbaustein enthält.

![Button Resultate exportieren über der Liste der Teilnehmenden markiert](assets/test_export_results1_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen des Kursbausteins Test" }

Haben Sie sich für das Erstellen der zip-Datei entschieden, können Sie einen Namen für die zip-Datei angeben und eine der angebotenen Varianten für ihren Inhalt wählen.
Es können 2 Varianten der zip-Datei erstellt werden:

* Der **Standardexport** enthält detaillierte Testresultate für jede:n Teilnehmer:in in Form eines HTML-Dokuments und einer Excel-Datei mit den Rohdaten.
* Die Option **"Erweitert – mit PDF"** erzeugt die gleiche zip-Datei, es werden jedoch zusätzlich noch PDF-Dateien mit den detaillierten Ergebnissen für jede:n Teilnehmer:in ergänzt. 

![Feld Name, die Optionen Standard und "Erweitert – mit PDF" und der Button Export starten markiert, darunter der leere Exportverlauf](assets/test_export_results2_v1_de.png){ class="shadow lightbox" title="Seite Export Resultate im Kursbaustein Test" }

Enthält der Test Freitextfragen und wurde die Option **"Erweitert – mit PDF"** gewählt, erscheint darunter unter **"Zusätzliche Option"** die Auswahl **"Separate PDF-Datei für jede Freitextfrage"**. Ist sie aktiviert, wird die Antwort jeder Freitextfrage zusätzlich als eigene PDF-Datei in die zip-Datei gelegt.

Klicken Sie auf den **Button "Export starten"** um die zip-Datei mit den Testresultaten zu erzeugen. 

Erstellte zip-Dateien werden im unteren Bereich unter **"Exportverlauf"** aufgelistet und stehen dort nur für einen begrenzten Zeitraum von 10 Tagen zur Verfügung.

Öffnen bzw. entpacken Sie dann die erstellte zip-Datei, um auf die benötigten Dateien zuzugreifen.

#### Punktespalten in der Excel-Datei [:octicons-tag-16:{ title="ab Release 21.1 (OO-9599)" }](https://track.frentix.com/issue/OO-9599) {: #score_columns}

Wer die Resultate auswertet, sieht in der Excel-Datei mit den Rohdaten, welcher Teil der Punkte aus der Antwort stammt und welcher aus einer nachträglichen Korrektur. Je Testversuch enthält die Datei diese Spalten:

* **Punkte**: das Ergebnis des Testversuchs.
* **Punkte (Auto)**: die Summe der automatisch errechneten Punkte.
* **Punkte (Anpassungen plus)**: die Summe aller Anpassungen, die Punkte dazugeben.
* **Punkte (Anpassungen minus)**: die Summe aller Anpassungen, die Punkte abziehen, als negativer Wert, zum Beispiel "-0.5".
* **Punkte (Manuell)**: die Summe der Punkte, die bei Fragen von Hand vergeben wurden.

Je Frage steht in der Spalte "Pkt" die Punktzahl der Frage. Bei automatisch korrigierten Fragen folgt die Spalte "Anpassung" mit dem Betrag, um den die Punkte angepasst wurden. Wie eine Anpassung entsteht, steht auf der Seite [Tests bewerten](../learningresources/Assessing_tests.de.md#adjust_score). Dieselbe Excel-Datei erhalten Sie in den Test Statistiken über "Rohdaten herunterladen".


!!! note "Hinweis"

    Auch in der Kursadministration gibt es eine Option zum Exportieren bzw. Archivieren von Testergebnissen. Mehr dazu unter [Testergebnisse archivieren](../learningresources/Course_Element_Test.de.md#archive).

[Zum Seitenanfang ^](#test_export)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Tests bewerten >](../learningresources/Assessing_tests.de.md)<br>
[Testergebnisse archivieren >](../learningresources/Course_Element_Test.de.md)

**Weiterführend**<br>
[Wie gehe ich vor, wenn ich einen Test erstelle? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md)<br>
[Allgemeines zu Tests >](../learningresources/Test.de.md)<br>
[Der Testeditor >](Test_editor_QTI_2.1.de.md)<br>
[Fragetypen >](../learningresources/Test_question_types.de.md)<br>
[Test-Fragen konfigurieren >](Configure_test_questions.de.md)<br>
[Test-Lernressourcen konfigurieren >](Configure_tests.de.md)<br>
[Test-Lernressourcen Einstellungen >](Test_settings.de.md)

[Zum Seitenanfang ^](#test_export)
