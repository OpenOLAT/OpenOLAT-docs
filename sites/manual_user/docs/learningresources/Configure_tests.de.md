# Test konfigurieren

Im Testeditor gliedern Sie einen Test und legen fest, wie Teilnehmende ihn bearbeiten: ob er bestanden werden kann, wie viel Zeit sie haben, ob sie zwischen den Fragen springen und ob sie ihre Antworten danach ansehen. Jeder Test besteht mindestens aus einer Sektion und einer Frage. Deshalb finden Sie beim Erstellen eines neuen Tests bereits eine Sektion ("Sektion") und eine Single-Choice-Frage ("Single Choice"). Falls in Ihrem Test keine Single-Choice-Frage vorkommt, können Sie die standardmässig angelegte Single-Choice-Frage löschen, sobald Sie eine andere Frage hinzugefügt haben.

Alle hier beschriebenen Einstellungen legen Sie im Testeditor fest: `Test > Administration > Testeditor`. Den Testeditor öffnen Besitzer:innen des Tests, Administrator:innen und Lernressourcenverwalter:innen.

Die Einstellungen gelten auf drei Ebenen:

* auf Ebene Test: Einstellungen für den gesamten Test
* auf Ebene Test-Part: Einstellungen für einen Block aus Sektionen, den Teilnehmende als Ganzes bearbeiten und beenden
* auf Ebene Sektion: Einstellungen für einzelne Sektionen

Die Einstellungen der einzelnen Fragen beschreibt die Seite [Testfragen konfigurieren](Configure_test_questions.de.md).

Die Test-Ebene ist die oberste Ebene. Der Test kann mehrere Test-Parts enthalten, die wiederum verschiedene Sektionen enthalten. Enthält ein Test nur einen Test-Part, kann dieser Test-Part trotzdem mehrere Sektionen umfassen. Teilen Sie einen Test in mehrere Test-Parts, wenn Teile des Tests unterschiedlichen Regeln folgen sollen, siehe [Test-Part-Ebene](#testpart).

![Hierarchie Test, Test-Part, Sektion und Frage mit den Einstellungen, die auf jeder Ebene gelten](assets/test_structure_levels_v1_de.svg){ class="shadow lightbox" title="Ebenen eines Tests · 2026.10.07" }

Mit Sektionen gliedern Sie Ihren Test. Häufig stehen zum Beispiel einleitende Fragen am Anfang, gesammelt in einer Sektion "Allgemeines". Ihr Test kann aus beliebig vielen Sektionen bestehen, und Sektionen lassen sich ineinander verschachteln.

Wenn Sie eine neue Sektion oder einen weiteren Test-Part hinzufügen möchten, wählen Sie oben im Dropdown-Menü `Elemente hinzufügen > Sektion` bzw. `Test-Part`. Anschliessend können Sie der Sektion konkrete Fragen zuordnen.

## Test-Ebene

Auf Ebene des Tests legen Sie den Titel fest, der in der Navigation erscheint, und die Einstellungen in den Tabs "Test Konfiguration", "Feedback" und "Expert".

### Tab Test Konfiguration

Im Tab "Test Konfiguration" legen Sie fest, wie viele Punkte der Test vergibt, ob er bestanden werden kann und wie viel Zeit Teilnehmende haben.

![Bestanden / Nicht bestanden ausgegeben mit Punkteschwelle und Zeitbeschränkung](assets/test_editor_tab_test_configuration_v1_de.png){ class="shadow lightbox" title="Tab Test Konfiguration im Testeditor" }

* **Maximal erreichbare Punktzahl:** OpenOlat berechnet diese Punktzahl automatisch aus den Punkten der einzelnen Fragen im Test.
* **Bestanden / Nicht bestanden ausgegeben:** Aktivieren Sie das Feld, wenn für den Test ein "bestanden" bzw. "nicht bestanden" angezeigt werden soll.
* **Art der Ausgabe:** Ist "Bestanden / Nicht bestanden ausgegeben" aktiviert, legen Sie hier fest, wie das Ergebnis zustande kommt: "Automatisch durch Punkteschwelle" oder "Manuell durch Betreuer:in". Diese Einstellung und die Punkteschwelle gelten auch, wenn Sie den Test in einen Kurs einbinden. Ausnahme: Aktivieren Sie im Kursbaustein "Test" die Option "Bewertung mit Einstufung/Noten", rechnet die Bewertungsskala die erreichten Punkte in eine Note oder Stufe um, zum Beispiel 0 bis 100 Punkte in Schweizer Noten von 1 bis 6. Ob der Test bestanden ist, entscheidet dann die Note: Die Bewertungsskala legt mit "Bestanden mit" fest, ab welcher Note der Test bestanden ist, zum Beispiel ab Note 4. Die Punkteschwelle des Tests wird dabei nicht umgerechnet und zählt nicht mehr, siehe [Test einrichten](Course_Element_Test/Test_Setup.de.md#section_test) und [Einstufung/Noten](Assessment_translate_points_in_grades.de.md).

    ![Bestanden im Kurs: ohne Einstufung/Noten entscheidet die Punkteschwelle des Tests, mit Einstufung/Noten die umgerechnete Note](assets/test_passed_decision_v1_de.svg){ class="shadow lightbox" title="Bestanden im Kurs mit und ohne Einstufung/Noten" }
* **Punkteschwelle für Bestanden:** Geben Sie hier die Punktzahl ein, die mindestens notwendig ist, damit der Test als bestanden gilt.
* **Zeitbeschränkung:** Die Zeitbeschränkung gilt für den gesamten Test, in Stunden und Minuten. Oberhalb des Tests sehen Teilnehmende, wie viel Zeit ihnen noch bleibt. Gegen Ende hebt OpenOlat die Anzeige farbig hervor. Eine Zeitbeschränkung für eine Sektion oder einzelne Fragen ist nicht möglich.

    Sobald die Zeit abgelaufen ist, beendet OpenOlat den Test automatisch. Im Kurs kündigt der Kursbaustein "Test" das vor dem Start mit "wird automatisch eingezogen" an. Antworten, die Teilnehmende noch nicht mit "Antwort speichern" gesendet haben, zählen als unbeantwortet und geben keine Punkte. Eine Rückfrage, ob die Antworten gespeichert werden sollen, erscheint nicht. Auch das Feedback zum gesamten Test und der Rückblick fallen unter die Zeitbeschränkung.

!!! note "Hinweis"

    Eine Zeitbeschränkung richten Sie entweder direkt im Testeditor ein, wie hier beschrieben, oder nach dem Einbinden des Tests in einen Kurs im Kursbaustein "Test":<br>
    `Kurs > Administration > Kurseditor > "Titel des Kursbausteins" > Tab "Optionen"`<br>
    Mit "Konfiguration von Lernressource übernehmen" gilt dort die Zeitbeschränkung aus dem Testeditor. Mit "Konfiguration anpassen" gilt die Zeitbeschränkung des Kursbausteins; ist dort keine aktiviert, gilt die des Tests. Wenn nötig verlängern Sie die Testzeit für einzelne Personen im [Bewertungswerkzeug](Assessment_tool_overview/index.de.md).

### Tab Feedback

* **Feedback, wenn notwendige Punktzahl für "Bestanden" erreicht:** Geben Sie hier ein Gesamtfeedback ein, wenn die Punktzahl für bestanden erreicht ist.
* **Feedback, wenn notwendige Punktzahl für "Bestanden" _nicht_ erreicht:** Tragen Sie hier ein Gesamtfeedback ein, wenn die Punktzahl nicht ausreicht.

### Tab Expert {: #expert} [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-8321)" }](https://track.frentix.com/issue/OO-8321)

Im Tab "Expert" legen Sie fest, wie sich Teilnehmende durch die Fragen bewegen, wie oft sie den Test lösen dürfen und ob sie ihre Antworten nach dem Test ansehen. Hat der Test mindestens zwei Test-Parts, stehen dieselben Einstellungen im Formular "Test part" des jeweiligen Test-Parts, und die Test-Ebene hat keinen Tab "Expert", siehe [Test-Part-Ebene](#testpart).

![Alle Einstellungen des Tabs Expert auf einen Blick, darunter Anzahl Versuche einschränken mit maximal 2 Versuchen und Persönliche Notizen erlauben](assets/test_editor_tab_expert_v2_de.png){ class="shadow lightbox" title="Tab Expert im Testeditor · 2026.11.10" }

* **Navigation:**

    * Linear: Teilnehmende beantworten alle Fragen der Reihe nach und springen nicht zwischen den Fragen hin und her.
    * Nicht linear: Teilnehmende beantworten die Fragen in der Reihenfolge, die sie selbst wählen.

* **Anzahl Versuche einschränken:** Legen Sie hier fest, wie oft Teilnehmende ihre Antwort auf eine Frage abgeben dürfen. Bei "Ja" geben Sie die Zahl unter "Max. Anzahl Versuche" ein. Die Grenze gilt für jede Frage einzeln, nicht für den Testdurchlauf: Jede Abgabe mit "Antwort speichern" zählt als ein Versuch, und unter der Frage steht zum Beispiel "Noch 1 Versuch (1/2)". Sind alle Versuche verbraucht, lässt sich die Antwort auf diese Frage nicht mehr ändern. In einem neuen Testdurchlauf beginnt die Zählung von vorn. Die Anzahl Lösungsversuche für den gesamten Test schränken Sie im Kursbaustein "Test" oder in den Einstellungen des Tests ein: `Test > Administration > Einstellungen > Tab "Optionen"`.

    Wenn die Anzahl Lösungsversuche auf Ebene Test oder Test-Part eingeschränkt wird, vererbt sich diese Einschränkung auf alle darunter liegenden Sektionen und Fragen.

* **Fragen überspringen erlauben:** Wenn diese Option gewählt ist, kann der Test beendet werden, bevor alle Fragen beantwortet sind.

* **Persönliche Notizen erlauben:** Die Teilnehmenden können sich persönliche Notizen machen, welche nach dem Beenden des Tests nicht mehr zur Verfügung stehen und nicht ausgewertet werden. Diese Funktion kann nur gewählt werden, wenn in den Einstellungen des Tests "Persönliche Notizen" ausgewählt ist: `Test > Administration > Einstellungen > Tab "Optionen"`.

* **Rückblick erlauben:** Nach dem Beenden des Tests können Teilnehmende den Test und ihre Antworten nochmals ansehen, aber nicht mehr korrigieren.

* **Lösung anzeigen:** Beim Rückblick werden zusätzlich die Lösungen angezeigt. Diese Funktion ist nur möglich, wenn "Rückblick erlauben" ausgewählt ist.

## Test-Part-Ebene {: #testpart}

Sollen Teile eines Tests unterschiedlichen Regeln folgen, etwa ein Pflichtteil ohne Zurückblättern vor einem frei bearbeitbaren Teil, teilen Sie den Test in Test-Parts. Ein Test-Part ist die oberste Gliederungsebene eines Tests. Er fasst Sektionen zusammen und legt für sie gemeinsam fest, wie sich Teilnehmende durch die Fragen bewegen ("Navigation": "Linear" oder "Nicht linear") und welche Einstellungen des Tabs "Expert" gelten.

Teilnehmende bearbeiten die Test-Parts nacheinander. Wer einen Test-Part beendet, gibt ihn ab: OpenOlat speichert die Antworten, und der Test-Part lässt sich danach nicht mehr öffnen. Das ist der Grund, einen Test zu teilen, und zugleich das, was Sie beim Planen bedenken.

Ein Beispiel: Test-Part 1 enthält Grundlagenfragen mit "Navigation" "Linear" und eingeschränkter Anzahl Versuche, die Teilnehmenden lösen die Fragen der Reihe nach. Test-Part 2 enthält Fragen mit "Navigation" "Nicht linear", deren Reihenfolge die Teilnehmenden selbst wählen. Wer Test-Part 2 betritt, kann die Antworten aus Test-Part 1 nicht mehr ändern.

Im Testeditor gelten für Test-Parts folgende Regeln:

* Jeder neue Test enthält einen Test-Part. Solange es nur einen gibt, erscheint er nicht im Menü des Testeditors, und seine Einstellungen stehen im Tab "Expert" der Test-Ebene.
* `Elemente hinzufügen > Test-Part` legt einen weiteren Test-Part am Ende des Tests an, mit einer leeren Sektion "Sektion". Ein neuer Test-Part startet mit "Navigation" "Nicht linear", "Fragen überspringen erlauben" und "Persönliche Notizen erlauben" auf "Ja" und "Rückblick erlauben" auf "Nein".
* Ab zwei Test-Parts erscheint jeder Test-Part als eigener Eintrag im Menü, zum Beispiel "1. Test part" und "2. Test part". Ein Klick darauf öffnet das Formular "Test part" mit "Navigation" und den Einstellungen des Tabs "Expert": "Anzahl Versuche einschränken" mit "Max. Anzahl Versuche", "Fragen überspringen erlauben", "Persönliche Notizen erlauben", "Rückblick erlauben" und "Lösung anzeigen". Die Test-Ebene hat dann keinen Tab "Expert".
* "Löschen" erscheint bei einem Test-Part erst, wenn der Test mindestens zwei Test-Parts hat. Nach der Rückfrage "Wollen Sie den Test-Part mit allen Fragen wirklich löschen?" entfernt OpenOlat den Test-Part mit allen seinen Fragen.
* Ein Test-Part enthält immer mindestens eine Sektion. Die letzte Sektion lässt sich nicht löschen, OpenOlat meldet "Diese Sektion kann nicht gelöscht werden. Ein Test oder ein Test-Part muss mindestens eine Sektion enthalten."
* Sobald der Test durchgeführt wurde, zeigt der Testeditor "Die Ressource wird bereits für die Auswertung verwendet. Die Bearbeitung ist begrenzt." Alle Einstellungen der Test-Parts sind dann gesperrt, "Löschen" und "Elemente hinzufügen" fehlen.

![Zwei Test-Parts im Menü des Testeditors, rechts das Formular Test part des zweiten Test-Parts mit Navigation und den Einstellungen des Tabs Expert](assets/test_editor_testpart_v1_de.png){ class="shadow lightbox" title="Formular Test part im Testeditor · 2026.10.07" }

Die Einstellungen eines Test-Parts steuern auch, was Teilnehmende beim Beenden erleben:

* Bei "Navigation" "Linear" ohne "Fragen überspringen erlauben" erscheint der Button "Test Part beenden" erst, wenn alle Fragen des Test-Parts beantwortet sind. Mit "Fragen überspringen erlauben" steht er ab der ersten Frage bereit.
* Mit "Rückblick erlauben" zeigt OpenOlat nach dem Beenden die Seite "Test Part abgeschlossen", auf der Teilnehmende ihre Antworten ansehen, aber nicht mehr ändern. Ohne Rückblick geht es direkt in den nächsten Test-Part.

!!! warning "Im linearen Test-Part führt «Nächste Frage» nur vorwärts"

    Erlaubt ein Test-Part mit "Navigation" "Linear" das Überspringen von Fragen, stehen "Nächste Frage" und "Test Part beenden" nebeneinander. "Nächste Frage" ohne Antwort lässt die Frage unbeantwortet, und Teilnehmende erreichen sie in diesem Test-Part nicht mehr. Auf der letzten Frage beendet "Nächste Frage" den Test-Part ohne Rückfrage. Weisen Sie Ihre Teilnehmenden vor dem Test darauf hin.

Eine Zeitbeschränkung gibt es nur für den ganzen Test (Tab "Test Konfiguration"), nicht je Test-Part.

!!! info "Wichtig"

    Ein Test aus einem anderen Werkzeug als OpenOlat kann beim Import mehrere Test-Parts mitbringen. Für einen solchen Test meldet der Testeditor "Dieser Test kann nicht mit dem OpenOlat-Editor bearbeitet werden." Im Formular "Test part" lässt sich nur "Navigation" ändern, die übrigen Einstellungen sind gesperrt. Die Fragen öffnen sich im Tab "Unbekannt", über "Konvertieren" wandeln Sie eine Frage in einen Fragetyp des Testeditors um. Ein Test, den Sie aus OpenOlat exportiert und wieder importiert haben, bleibt vollständig bearbeitbar.

Was Teilnehmende während der Durchführung sehen, beschreibt die Seite [Kursbaustein "Test"](Course_Element_Test/index.de.md#participate_as_learner).

## Sektionsebene {: #section}

Einem Test-Part ordnen Sie eine oder mehrere Sektionen unter. Im Test sehen Teilnehmende verschachtelte Sektionen mit Beschreibung untereinander und blenden sie einzeln ein und aus. Sektionen können auch in zufälliger Reihenfolge erscheinen. Enthält ein Test nur einen Test-Part, stehen alle Sektionen im Menü des Testeditors direkt unter dem Test.

Im Tab "Sektion" tragen Sie eine Beschreibung der Sektion ein und legen mit "Anzahl Fragen in dieser Sektion" fest, ob alle Fragen der Sektion erscheinen oder nur eine Auswahl. Mit "Zufällige Reihenfolge der Fragen oder der Sektionen?" legen Sie fest, ob die Fragen oder die untergeordneten Sektionen in zufälliger Reihenfolge erscheinen.

Im Tab "Expert" einer Sektion überschreiben Sie die Einstellungen des Tabs "Expert" der Test- oder Test-Part-Ebene. So verhält sich eine einzelne Sektion anders als der restliche Test.

Ist im Tab "Expert" der Sektion "Sektionstitel sichtbar in Test" aktiviert, zeigt OpenOlat auch die Sektionsbeschreibung an folgenden Stellen an:

* Im Test, wenn eine zur Sektion zugehörige Frage aufgerufen wird. Die Sektionsbeschreibung kann von den Teilnehmenden aus- und eingeblendet werden.
* In den Testresultaten.
* Im [Korrektur-Workflow](Test_correction_workflow.de.md), in dem Korrektor:innen die Antworten bewerten, an den zu dieser Sektion gehörenden Fragen.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Testfragen konfigurieren >](Configure_test_questions.de.md)<br>
[Test einrichten >](Course_Element_Test/Test_Setup.de.md)<br>
[Einstufung/Noten >](Assessment_translate_points_in_grades.de.md)<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview/index.de.md)<br>
[Kursbaustein "Test" >](Course_Element_Test/index.de.md)<br>
[Test: Korrektur-Workflow >](Test_correction_workflow.de.md)

**Weiterführend**<br>
[Testeditor >](Test_editor_QTI_2.1/index.de.md)<br>
[Test: Einstellungen >](Test_settings.de.md)

[Zum Seitenanfang ^](#test-konfigurieren)
