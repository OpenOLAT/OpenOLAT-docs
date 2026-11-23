# :o_icon_o_mi_qtiessay: Freitext* {: #essay}

Mit einer Freitext-Frage lassen Sie die Teilnehmenden eine Antwort frei formulieren, etwa einen Aufsatz. Die Teilnehmenden schreiben ihre Antwort in ein Textfeld beliebiger Grösse. Freitext-Antworten korrigieren Sie nach der Abgabe von Hand, darauf weist der * im Namen des Fragetyps hin.

Im Testeditor fügen Besitzer:innen des Tests, Administrator:innen und Lernressourcenverwalter:innen die Frage unter `Test > Administration > Testeditor > Elemente hinzufügen > Freitext` hinzu. Im [Fragenpool](../../area_modules/Question_Bank_Create_Questions.de.md) wählen Sie den Typ unter `Fragenpool > Meine Fragen > Frage erstellen` im Feld "Fragetyp".

![Freitext-Frage mit einer per Tabulator formatierten Preisliste im Antwortfeld](../assets/Essay_Beispiel_DE.png){ class="shadow lightbox" title="Freitext aus Sicht der Teilnehmenden" }

Geben Sie zuerst unter "Titel" einen kurzen Titel und unter "Frage" die Frage ein.

Danach stehen folgende Optionen zur Wahl:

* "Modus": Mit "Standard" schreiben die Teilnehmenden in ein einfaches Textfeld. Mit "Rich Text Formatierung" schreiben sie in einem Editor mit Textformatierung, der auch mathematische Formeln unterstützt. [:octicons-tag-16:{ title="ab Release 16.2 (OO-6071)" }](https://track.frentix.com/issue/OO-6071)
* "Platzhalter": Hier tragen Sie bei Bedarf einen Text ein, den die Teilnehmenden im leeren Textfeld sehen.
* "Höhe (Anzahl Zeilen)": Hier legen Sie die Höhe des Textfelds fest. Die Zeilenzahl begrenzt die Antwort nicht: Das Feld scrollt weiter, wenn die Teilnehmenden mehr Zeilen schreiben.
* "Min Anzahl Wörter": So viele Wörter müssen die Teilnehmenden mindestens schreiben, damit sie die Antwort abgeben können.
* "Max Anzahl Wörter": So viele Wörter dürfen die Teilnehmenden höchstens schreiben, damit sie die Antwort abgeben können. Damit begrenzen Sie die Länge der Antwort.
* "Copy/paste erlauben": Hier legen Sie fest, ob die Teilnehmenden Inhalte per Copy and Paste oder per Drag and Drop aus einer externen Quelle einfügen dürfen. Text innerhalb desselben Felds verschieben sie in jedem Fall. [:octicons-tag-16:{ title="ab Release 20.3.2 (OO-9472)" }](https://track.frentix.com/issue/OO-9472)

Im Modus "Standard" verwendet das Antwortfeld eine Schrift mit fester Zeichenbreite und unterstützt die Tabulatortaste. So formatieren die Teilnehmenden ihre Antworten übersichtlich und bilden zum Beispiel Spalten ab.

Die Antworten korrigieren Betreuer:innen und Besitzer:innen des Kurses im Kursbaustein Test mit dem [Korrekturwerkzeug](../Assessing_tests.de.md#correction_tool), Korrektor:innen über den [Korrektur-Workflow](../Test_correction_workflow.de.md). Wer korrigiert und wann die Teilnehmenden ihre Bewertung sehen, legen Sie im Kursbaustein Test mit der Einstellung [Korrektur](../Course_Element_Test/Test_Setup.de.md#section_correction) fest. Die höchste Punktzahl, die bei der Korrektur zu vergeben ist, legen Sie im [Tab Punkte](../Configure_test_questions.de.md#score) unter "Maximal erreichbare Punktzahl" fest.

!!! info "Autosave"

    Mit dem Fragetyp Freitext schreiben die Teilnehmenden oft Aufsätze. Deshalb speichert eine Autosave-Funktion den geschriebenen Text jede Minute. Wie Sie Aufsätze konfigurieren, beschreibt der folgende Exkurs "Aufsatz schreiben".

??? abstract "Exkurs: Aufsatz schreiben"

    Mit der Lernressource Test und dem Fragetyp Freitext schreiben die Teilnehmenden in OpenOlat Aufsätze. Damit dabei kein Text verloren geht, beachten Sie folgende Punkte:

    * Die Autosave-Funktion speichert den geschriebenen Text jede Minute. Nach der ersten Speicherung steht links unter dem Antwortfeld "Zuletzt gespeichert um:" mit der Uhrzeit. So bleibt der Text auch erhalten, wenn beispielsweise die Internetverbindung abbricht oder die Anmeldung nach einer Zeit ohne Aktivität abläuft. Abgegeben ist die Antwort aber erst mit "Antwort speichern". Haben die Teilnehmenden die Antwort nicht mit "Antwort speichern" abgegeben, zeigt OpenOlat bei der Korrektur den per Autosave gespeicherten Inhalt mit einem entsprechenden Hinweis an.
    * Nach einem technischen Unterbruch, zum Beispiel einem Absturz des Browsers oder einem Abbruch der Internetverbindung, öffnen die Teilnehmenden den Kursbaustein erneut und setzen den Test fort. OpenOlat zeigt den Text im Stand der letzten Speicherung. Kleine Textverluste sind also möglich. Für die Fortsetzung braucht es keine besondere Einstellung:
        * Ein Versuch zählt erst, wenn die Teilnehmenden den Test beenden. Ein technischer Unterbruch verbraucht keinen Versuch. Für eine Prüfung können Sie deshalb "Max. Anzahl Versuche" auf 1 setzen (siehe [Anzahl der Testversuche einschränken](../Test_settings.de.md#limit_attempts)). Nach dem Beenden lässt sich der Test dann nicht nochmals starten.
        * Die Option [Unterbrechen erlauben](../Test_settings.de.md#allow_suspend) ist für die Fortsetzung nicht nötig. Mit dieser Option verlassen die Teilnehmenden den Test freiwillig und setzen ihn später fort. Bei einer Präsenzprüfung lassen Sie die Option deshalb meist ausgeschaltet.
    * Ist die Anzahl Versuche für die Freitext-Frage unbeschränkt ("Anzahl Versuche einschränken" im [Tab Punkte](../Configure_test_questions.de.md#score)), schicken die Teilnehmenden den Text mit "Antwort speichern" immer wieder ab und schreiben danach weiter. Das regelmässige Abschicken gibt ihnen Sicherheit.
    * Hat der Test eine Zeitbeschränkung (im [Testeditor](../Configure_tests.de.md) oder im [Kursbaustein](../Test_settings.de.md)), beendet OpenOlat ihn beim Ablauf der Zeit und übernimmt den Stand der letzten automatischen Speicherung. Verloren geht nur Text, den die Teilnehmenden danach geschrieben haben, also höchstens der Text der letzten Minute. Erinnern Sie die Teilnehmenden kurz vor Schluss daran, die Antwort mit "Antwort speichern" nochmals abzugeben.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Fragenpool: Fragen erstellen >](../../area_modules/Question_Bank_Create_Questions.de.md)<br>
[Tests bewerten >](../Assessing_tests.de.md)<br>
[Test: Korrektur-Workflow >](../Test_correction_workflow.de.md)<br>
[Test einrichten >](../Course_Element_Test/Test_Setup.de.md)<br>
[Test: Einstellungen >](../Test_settings.de.md)<br>
[Prüfungsverwaltung: Prüfungsmodus >](../Assessment_mode.de.md)<br>
[Testfragen konfigurieren >](../Configure_test_questions.de.md)<br>
[Test konfigurieren >](../Configure_tests.de.md)

**Weiterführend**<br>
[Fragetypen >](index.de.md)<br>
[Testeditor >](../Test_editor_QTI_2.1/index.de.md)

[Zum Seitenanfang ^](#essay)
