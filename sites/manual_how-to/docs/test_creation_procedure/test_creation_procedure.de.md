# Wie gehe ich vor, wenn ich einen Test erstelle? {: #test_creation_procedure}

??? abstract "Ziel und Inhalt dieser Anleitung"

    Ob Sie einen neuen Kurs aufbauen, einen Test in einen bestehenden Kurs einbinden oder Fragen zuerst im Fragenpool sammeln: Für jede dieser Ausgangslagen zeigt diese Anleitung einen eigenen Weg zum fertigen Test. Vergleichen Sie die drei Wege und wählen Sie den, der zu Ihrer Situation passt.

    Alle drei Wege setzen die Rolle Autor:in voraus. Mit ihr zeigt die Hauptnavigation den Autorenbereich und den Fragenpool.

??? abstract "Zielgruppe"

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Expert:innen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)


---

## Das Zusammenwirken der Bestandteile

Ein Test in OpenOlat besteht aus mehreren Bestandteilen, die ineinandergreifen. Wenn Sie sie auseinanderhalten, finden Sie jede Einstellung am richtigen Ort.

![Kursbaustein vom Typ Test mit eingefügter Lernressource Test, deren Fragen mit dem Fragenpool ausgetauscht werden](assets/kurs-kursbaustein-lernressource-frage_v1_de.png){ class="lightbox" title="Kurs, Kursbaustein, Lernressource und Fragenpool" }

**Kurs:**<br> Sie setzen ihn im Kurseditor aus Kursbausteinen zusammen.

**Kursbaustein:** <br>Die meisten Kursbausteine sind Behälter, in die Sie eine Lernressource einfügen. In den Kursbaustein "Test" fügen Sie zum Beispiel eine Lernressource "Test" ein. Halten Sie diese beiden "Tests" auseinander: Den Kursbaustein konfigurieren Sie im Kurseditor, die Lernressource im Testeditor.

**Fragen:** <br>Eine Test-Lernressource besteht aus einzelnen Fragen verschiedener Fragetypen, zum Beispiel Single Choice oder Multiple Choice.

**Fragenpool:** <br>Im Fragenpool sammeln Sie einzelne Fragen, um sie in mehreren Tests zu verwenden. Beim Erstellen einer Test-Lernressource übernehmen Sie vorhandene Fragen aus dem Fragenpool, OpenOlat kopiert sie dabei in den Test. Weitere Fragen erstellen Sie bei Bedarf direkt in der Lernressource. <br>
Eine in der Lernressource erstellte Frage gibt es nur in dieser Test-Lernressource. Für die Mehrfachnutzung übernehmen Sie sie im Testeditor mit "Zum Pool exportieren" in den Fragenpool.

<br>

Jeder dieser Bestandteile hat eigene Einstellungen (Konfigurationen). Einen Test konfigurieren Sie deshalb auf vier Ebenen. Kurs und Test-Lernressource öffnen Sie im Autorenbereich, die Klickwege unten beginnen beim geöffneten Kurs oder Test.

![Vier ineinander liegende Ebenen mit je eigener Konfiguration: Kurs, Kursbaustein Test, Lernressource Test und Frage](assets/grafik_konfigurationsebenen_v1_de.png){ width=450px class="lightbox" title="Konfigurationsebenen eines Tests" }


**Konfiguration des Kurses:**<br>
`Kurs > Administration > Einstellungen`

**Konfiguration des Kursbausteins:**<br>
`Kurs > Administration > Kurseditor > "Kursbaustein" > Tabs des Kursbausteins`

**Konfiguration der Lernressource:**<br>
`Test-Lernressource > Administration > Einstellungen`

**Konfiguration einer Frage:**<br>
`Test-Lernressource > Administration > Testeditor > "Frage" in der Baumstruktur > Tabs der Frage`

<br>

:octicons-device-camera-video-24: **Video-Einführung**: [Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>){:target="_blank"}

<br>

---

## Vorgehen Möglichkeit 1

Beginnen Sie ganz von vorn, noch ohne Kurs und ohne Fragen, führt dieser Weg in vier Etappen vom neuen Kurs zum fertigen Test.<br>

<br>

![Vier Schritte vom Erstellen des Kurses bis zum Erstellen der Fragen in der Test-Lernressource](assets/flowchart_testerstellung1_v1_de.png){ class="lightbox" title="Vorgehen Möglichkeit 1" }

<br>

> <h3>Kurs erstellen</h3>

<br>

!!! note "Hinweis"

    Haben Sie noch keinen Kurs erstellt, führt Sie die Anleitung ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md) Schritt für Schritt durch.

1\. Erstellen Sie einen neuen Kurs über `Autorenbereich > Erstellen > Kurs`.

![Menü Erstellen geöffnet, Eintrag Kurs markiert](assets/testerstellung_1_1_v1_de.png){ class="lightbox" title="Autorenbereich" }

2\. Geben Sie im Dialog "Kurs erstellen" einen Titel ein und legen Sie erste Einstellungen des Kurses fest. Wählen Sie unter "Kursdesign" das passende Design, zum Beispiel "Mit Lernpfad".

![Titel des Kurses eingetragen und Kursdesign Mit Lernpfad gewählt, darunter der Button Erstellen](assets/testerstellung_1_2_v1_de.png){ class="lightbox" title="Dialog Kurs erstellen" }

3\. Soll ein Assistent Sie durch die weitere Einrichtung führen, klicken Sie statt auf "Erstellen" auf "Mit Kursassistent:in erstellen" und wählen "Einfacher Kurs" oder "Prüfungskurs".<br>
Ein Prüfungskurs ist ein normaler Kurs, wahlweise Lernpfadkurs oder herkömmlicher Kurs. Sein Assistent richtet in einem Durchgang die Prüfung mit dem Test ein, auf Wunsch auch Nachprüfung, Zertifikat, Betreuer:innen und Teilnehmer:innen. Das spart Ihnen später Arbeit.

![Button Mit Kursassistent:in erstellen geöffnet, mit den Einträgen Einfacher Kurs und Prüfungskurs](assets/testerstellung_1_3_v1_de.png){ class="lightbox" title="Dialog Kurs erstellen mit Kursassistent:in" }

4\. Klicken Sie auf "Erstellen". OpenOlat öffnet danach die Einstellungen des Kurses (Konfiguration des Kurses).

!!! tip "Tipp"

    Alle Angaben ausser dem Kursdesign passen Sie auch später unter `Kurs > Administration > Einstellungen` an.

![Eintrag Einstellungen im Menü Administration markiert, daneben die Tabs der Kurseinstellungen von Info bis Optionen](assets/testerstellung_1_4_v1_de.png){ class="lightbox" title="Einstellungen des Kurses" }

<br>

> <h3>Kursbaustein "Test" einfügen</h3>

<br>

5\. Öffnen Sie den Kurseditor über `Kurs > Administration > Kurseditor`. Klicken Sie auf "Kursbausteine einfügen" und wählen Sie den Typ "Test" oder "Selbsttest". OpenOlat fügt einen Kursbaustein dieses Typs in den Kurs ein.

![Eintrag Kurseditor im Menü Administration und Button Kursbausteine einfügen markiert](assets/testerstellung_1_5_v1_de.png){ class="lightbox" title="Kurseditor" }

<br>

> <h3>im Kursbaustein Test-Lernressource erstellen</h3>

<br>

6\. Klicken Sie links im Kursmenü auf den neuen Kursbaustein.

7\. Öffnen Sie rechts den Tab "Test-Konfiguration", beim Selbsttest "Selbsttest-Konfiguration", und klicken Sie auf "Erstellen". So entsteht eine neue Test-Lernressource, die direkt mit dem Kursbaustein verbunden ist.

![Kursbaustein Test im Kursmenü, Tab Test-Konfiguration und Button Erstellen markiert](assets/testerstellung_1_7_v1_de.png){ class="lightbox" title="Kursbaustein Test im Kurseditor" }

8\. Geben Sie im Dialog "Test erstellen" einen Titel für die Test-Lernressource ein und klicken Sie auf "Erstellen".

![Titel der neuen Test-Lernressource im Feld Titel eingetragen](assets/testerstellung_1_8_v1_de.png){ class="lightbox" title="Dialog Test erstellen" }

<br>

> <h3>Lernressource editieren und Fragen erstellen</h3>

<br>

9\. Der Tab "Test-Konfiguration" zeigt jetzt die neue Test-Lernressource. Mit "Lernressource bearbeiten" öffnen Sie sie, um Fragen zu ergänzen.

![Eingebundene Test-Lernressource im Tab Test-Konfiguration, markiert die Buttons Vorschau und Ersetzen und der Link Lernressource bearbeiten, mit dem Sie den Test zum Bearbeiten öffnen](assets/testerstellung_1_9_v2_de.png){ class="shadow lightbox" title="Tab Test-Konfiguration im Kursbaustein Test · 2026.11.10" }

10\. Eine neue Test-Lernressource enthält bereits eine Single-Choice-Frage. Verwenden Sie sie als Muster, passen Sie sie an oder löschen Sie sie.

![Neue Test-Lernressource mit einer Single-Choice-Frage und der Antwort Neue Antwort, in der Toolbar die Links Administration und Infoseite](assets/testerstellung_1_10_v2_de.png){ class="lightbox" title="Test-Lernressource · 2026.09.28" }

11\. Öffnen Sie den Testeditor über `Test-Lernressource > Administration > Testeditor`. Der Testeditor gehört zur Lernressource, den Kurs bearbeiten Sie weiterhin im Kurseditor.

![Eintrag Testeditor im Menü Administration markiert](assets/testerstellung_1_11_v2_de.png){ class="lightbox" title="Menü Administration einer Test-Lernressource · 2026.09.28" }

12\. Klicken Sie auf "Elemente hinzufügen" und wählen Sie den passenden Fragetyp, zum Beispiel "Multiple Choice".

![Button Elemente hinzufügen markiert, darunter eine neue Multiple-Choice-Frage im Tab Auswahl](assets/testerstellung_1_12_v1_de.png){ class="lightbox" title="Testeditor" }

13\. Geben Sie im Tab "Auswahl" den Titel der Frage, die Fragestellung und die möglichen Antworten ein. Weitere Antworten ergänzen Sie über das Pluszeichen.

14\. Im Tab "Punkte" legen Sie die Bewertungsmethode und die Punktzahl fest.

15\. Im Tab "Feedback" hinterlegen Sie bei Bedarf Rückmeldungen zur Frage. Im Tab "Vorschau" prüfen Sie die Frage.

Weitere Fragen fügen Sie nach demselben Prinzip hinzu, die Einstellungen unterscheiden sich je nach Fragetyp. Mit Sektionen oder [Test-Parts](../../manual_user/learningresources/Configure_tests.de.md#testpart) gliedern Sie den Test weiter.


!!! warning "Achtung"

    Überlegen Sie sich vor dem Erstellen, welcher Fragetyp Ihren Zweck am besten erfüllt. Den Fragetyp einer erstellten Frage können Sie nachträglich nicht mehr ändern.

!!! tip "Tipp"

    Brauchen Sie mehrere Fragen mit denselben Antworten, etwa einer Skala von 1 bis 5, kopieren Sie eine fertige Frage: Im Testeditor wählen Sie dazu im Menü mit den drei Punkten "Duplizieren". Danach passen Sie nur noch die Fragestellung an.

<br>

---

## Vorgehen Möglichkeit 2

Besteht der Kurs schon und kennen Sie sich als Autor:in etwas aus, beginnen Sie mit der Lernressource "Test" und binden sie danach in den Kurs ein.

<br>

![Fünf Schritte vom Erstellen der Test-Lernressource bis zum Einfügen in den Test-Kursbaustein](assets/flowchart_testerstellung2_v1_de.png){ class="lightbox" title="Vorgehen Möglichkeit 2" }

<br>

> <h3>Test-Lernressource erstellen</h3>

<br>

1\. Erstellen Sie eine Test-Lernressource über `Autorenbereich > Erstellen > Test`.

![Menü Erstellen im Autorenbereich geöffnet, Eintrag Test markiert](assets/testerstellung_2_1_v2_de.png){ class="shadow lightbox" title="Menü Erstellen im Autorenbereich · 2026.11.10" }

2\. Geben Sie im Dialog "Test erstellen" den Titel des Tests ein und klicken Sie auf "Erstellen".

![Dialog Test erstellen mit dem Titel E-Learning Grundlagen im Feld Titel, Button Erstellen markiert](assets/testerstellung_2_2_v2_de.png){ class="shadow lightbox" title="Dialog Test erstellen · 2026.11.10" }

3\. OpenOlat öffnet danach die Einstellungen der Test-Lernressource. Legen Sie in den Tabs bei Bedarf weitere Einstellungen fest.

Dieselben Einstellungen passen Sie auch später unter `Test-Lernressource > Administration > Einstellungen` an.

![Einstellungen der Test-Lernressource mit den Tabs Metadaten, Info, Freigabe und Optionen](assets/testerstellung_2_3_v2_de.png){ class="shadow lightbox" title="Einstellungen der Test-Lernressource · 2026.11.10" }

:octicons-device-camera-video-24: **Video-Einführung**: [Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>){:target="_blank"}

<br>

> <h3>Lernressource editieren und Fragen erstellen</h3>

<br>

4\. Öffnen Sie den Testeditor über `Test-Lernressource > Administration > Testeditor`.

![Eintrag Testeditor im Menü Administration markiert](assets/testerstellung_1_11_v2_de.png){ class="shadow lightbox" title="Menü Administration einer Test-Lernressource · 2026.09.28" }

5\. Klicken Sie auf "Elemente hinzufügen" und wählen Sie den passenden Fragetyp, zum Beispiel "Multiple Choice".

6\. Geben Sie im Tab "Auswahl" den Titel der Frage, die Fragestellung und die möglichen Antworten ein. Weitere Antworten ergänzen Sie über das Pluszeichen.

7\. Im Tab "Punkte" legen Sie die Bewertungsmethode und die Punktzahl fest.

8\. Im Tab "Feedback" hinterlegen Sie bei Bedarf Rückmeldungen zur Frage. Im Tab "Vorschau" prüfen Sie die Frage.

Weitere Fragen fügen Sie nach demselben Prinzip hinzu, die Einstellungen unterscheiden sich je nach Fragetyp. Mit Sektionen oder [Test-Parts](../../manual_user/learningresources/Configure_tests.de.md#testpart) gliedern Sie den Test weiter.

:octicons-device-camera-video-24: **Video-Einführung**: [Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>){:target="_blank"}

!!! info "Wichtig"

    Eine neue Test-Lernressource enthält bereits eine Single-Choice-Frage. Bearbeiten oder löschen Sie diese Frage, damit sie nicht ungewollt im Test bleibt.

!!! warning "Achtung"

    Überlegen Sie sich vor dem Erstellen, welcher Fragetyp Ihren Zweck am besten erfüllt. Den Fragetyp einer erstellten Frage können Sie nachträglich nicht mehr ändern.

!!! tip "Tipp"

    Brauchen Sie mehrere Fragen mit denselben Antworten, etwa einer Skala von 1 bis 5, kopieren Sie eine fertige Frage: Im Testeditor wählen Sie dazu im Menü mit den drei Punkten "Duplizieren". Danach passen Sie nur noch die Fragestellung an.

<br>

> <h3>Test-Lernressource konfigurieren</h3>

<br>

9\. Klicken Sie im Testeditor links auf das oberste Element, den Titel des Tests. Rechts erscheinen die Tabs mit den Einstellungen für den ganzen Test.

![Oberstes Element des Testeditors gewählt, im Tab Test Konfiguration maximal 5 Punkte, Bestanden automatisch ab einer Punkteschwelle von 3 und eine Zeitbeschränkung von 30 Minuten](assets/testerstellung_2_9_v2_de.png){ class="shadow lightbox" title="Tab Test Konfiguration im Testeditor · 2026.11.10" }

10\. **Test Konfiguration:** Legen Sie fest, ab wie vielen Punkten der Test bestanden ist und ob eine Zeitbeschränkung gilt.

Im Tab "Feedback" hinterlegen Sie bei Bedarf eine allgemeine Rückmeldung für bestandene und für nicht bestandene Tests. Sie gilt, wenn OpenOlat das Bestehen automatisch über die Punkteschwelle ausgibt.

11\. **Expert:** Legen Sie weitere Details des Testablaufs fest, zum Beispiel die Navigation oder die Anzeige von Lösungen.

12\. Zum Schluss verlassen Sie den Testeditor mit einem Klick auf den Titel des Tests in der Krümelnavigation.

![Titel des Tests in der Krümelnavigation des Testeditors markiert](assets/testerstellung_2_12_v2_de.png){ class="shadow lightbox" title="Krümelnavigation im Testeditor · 2026.11.10" }

:octicons-device-camera-video-24: **Video-Einführung**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}

!!! tip "Tipp"

    Feedback hinterlegen Sie für einzelne Fragen im Tab "Feedback" der Frage und für den ganzen Test im Tab "Feedback" des obersten Elements.

<br>

> <h3>Kursbaustein "Test" in den vorhandenen Kurs einfügen</h3>

<br>

13\. Öffnen Sie im Autorenbereich den Kurs, in den der Test gehört. Ihre Kurse finden Sie in den Tabs "Meine Kurse" und "Meine Einträge".

14\. Öffnen Sie den Kurseditor über `Kurs > Administration > Kurseditor`. Klicken Sie auf "Kursbausteine einfügen" und wählen Sie den Typ "Test" oder "Selbsttest".

<br>

> <h3>Test-Lernressource in den Test-Kursbaustein einfügen</h3>

<br>

15\. Öffnen Sie im neuen Kursbaustein den Tab "Test-Konfiguration" und klicken Sie auf "Auswählen".<br>
Im Dialog "Test-Lernressource auswählen" wählen Sie den vorbereiteten Test.

![Neuer Kursbaustein Test im Kurseditor, Tab Test-Konfiguration noch ohne Test-Lernressource, Button Auswählen markiert](assets/testerstellung_2_15_v2_de.png){ class="shadow lightbox" title="Tab Test-Konfiguration im Kursbaustein Test · 2026.11.10" }

16\. Der Tab "Test-Konfiguration" zeigt nun den eingebundenen Test. Mit "Vorschau" sehen Sie ihn an, mit "Lernressource bearbeiten" öffnen Sie ihn zum Bearbeiten. Sobald Teilnehmende den Test gestartet haben, ist die Bearbeitung begrenzt.

![Eingebundene Test-Lernressource im Tab Test-Konfiguration, markiert die Buttons Vorschau und Ersetzen und der Link Lernressource bearbeiten, mit denen Sie den Test ansehen, austauschen oder bearbeiten](assets/testerstellung_1_9_v2_de.png){ class="shadow lightbox" title="Tab Test-Konfiguration mit eingebundenem Test · 2026.11.10" }

17\. Konfigurieren Sie bei Bedarf die weiteren Tabs des Kursbausteins. Einen Teil der Einstellungen der Test-Lernressource übersteuern Sie hier für diesen Kurs. Das lohnt sich, wenn Sie dieselbe Test-Lernressource in verschiedenen Kursen verwenden.

18\. Damit Teilnehmende den Test bearbeiten können, publizieren Sie den Kurs. Schliessen Sie dazu den Kurseditor, zum Beispiel mit einem Klick auf den Namen des Kurses in der Krümelnavigation, und wählen Sie im folgenden Dialog "Manuell publizieren" oder "Automatisch publizieren".

Alternativ klicken Sie im Kurseditor rechts in der Toolbar auf "Publizieren" oder schliessen den Kurseditor über das kleine rote Kreuz rechts oben.

19\. Setzen Sie danach den Status des Kurses auf "Veröffentlicht", damit Teilnehmende den Test bearbeiten können.<br>
Wer Zugang erhält, bestimmen Sie unter `Kurs > Administration > Mitgliederverwaltung`.

20\. Sobald Testergebnisse vorliegen, bewerten Betreuer:innen die Teilnehmenden im Bewertungswerkzeug. Beim Selbsttest entfällt dieser Schritt.<br>
Wie das geht, beschreibt die Seite [Tests bewerten](../../manual_user/learningresources/Assessing_tests.de.md).

<br>

---

## Vorgehen Möglichkeit 3

Teilen Sie sich die Arbeit mit Kolleg:innen und erstellen Sie als Fachexpert:in Fragen, die in mehreren Tests zum Einsatz kommen?<br>
Dann beginnen Sie im Fragenpool: Die Fragen dort stehen für jeden Test bereit, in den Sie sie übernehmen.

<br>

![Vier Schritte vom Erstellen der Fragen im Fragenpool bis zum Einfügen des Tests in den Test-Kursbaustein](assets/flowchart_testerstellung3_v1_de.png){ class="lightbox" title="Vorgehen Möglichkeit 3" }

<br>

> <h3>Fragen im Fragenpool erstellen</h3>

<br>

1\. Öffnen Sie den Fragenpool in der Hauptnavigation. Mit der Rolle Autor:in steht er dort neben dem Autorenbereich.

![Fragenpool markiert und geöffnet, links das Menü Mein Fragenpool](assets/testerstellung_3_1_v1_de.png){ class="lightbox" title="Fragenpool in der Hauptnavigation" }

2\. Wählen Sie unter "Mein Fragenpool" den Eintrag "Meine Fragen" und klicken Sie auf "Frage erstellen". Geben Sie einen Titel ein und wählen Sie unter "Fragetyp" den passenden Typ, zum Beispiel "Multiple Choice".

![Button Frage erstellen markiert, über der Liste Meine Fragen](assets/testerstellung_3_2_v1_de.png){ class="lightbox" title="Fragenpool" }

3\. Geben Sie im Tab "Auswahl" den Titel der Frage, die Fragestellung und die möglichen Antworten ein. Weitere Antworten ergänzen Sie über das Pluszeichen.

![Tab Auswahl einer neuen Multiple-Choice-Frage im Fragenpool mit den Feldern Titel, Frage und vier Antworten, davon drei als korrekt angehakt](assets/testerstellung_3_3_v2_de.png){ class="lightbox" title="Frage im Fragenpool · 2026.09.28" }

4\. Im Tab "Punkte" legen Sie die Bewertungsmethode und die Punktzahl fest.

5\. Im Tab "Feedback" hinterlegen Sie bei Bedarf Rückmeldungen zur Frage. Im Tab "Vorschau" prüfen Sie die Frage.

Weitere Fragen erstellen Sie nach demselben Prinzip, die Einstellungen unterscheiden sich je nach Fragetyp.


!!! warning "Achtung"

    Überlegen Sie sich vor dem Erstellen, welcher Fragetyp Ihren Zweck am besten erfüllt. Den Fragetyp einer erstellten Frage können Sie nachträglich nicht mehr ändern.

!!! tip "Tipp"

    Brauchen Sie mehrere Fragen mit denselben Antworten, etwa einer Skala von 1 bis 5, kopieren Sie eine fertige Frage und passen Sie nur noch die Fragestellung an.

Damit Sie die Fragen später über die Suchfilter wiederfinden und der Kursbaustein "Übung" sie automatisch auswählt, pflegen Sie zu jeder Frage im Fragenpool die Metadaten, etwa Fachbereich, Stufe und Schlagworte. Wie das geht, zeigt die Anleitung [Nutzen von Metadaten](../question_metadata/question_metadata.de.md).

<br>

> <h3>Test-Lernressource erstellen und editieren</h3>

<br>

6\. Erstellen Sie eine Test-Lernressource über `Autorenbereich > Erstellen > Test`.

![Eintrag Test im Menü Erstellen markiert](assets/testerstellung_3_6_v1_de.png){ class="lightbox" title="Autorenbereich" }

!!! note "Hinweis"

    Die neue Test-Lernressource finden Sie im Autorenbereich im Tab "Meine Einträge", denn der Tab "Meine Kurse" listet nur Kurse. In der Spalte "Typ" erkennen Sie sie am Symbol für Test-Lernressourcen.
    ![Tab Meine Einträge mit Filter Typ Test, Test-Symbol in der Spalte Typ markiert](assets/testerstellung_3_6b_v1_de.png){ class="lightbox" title="Tab Meine Einträge im Autorenbereich" }

7\. Öffnen Sie den Testeditor über `Test-Lernressource > Administration > Testeditor`.

![Eintrag Testeditor im Menü Administration markiert](assets/testerstellung_3_7_v2_de.png){ class="lightbox" title="Menü Administration einer Test-Lernressource · 2026.09.28" }

8\. Den Testeditor erkennen Sie an der schraffierten Kopfzeile. Unter "Elemente hinzufügen" fügen Sie hier neue Fragen hinzu.

![Geöffnetes Menü Elemente hinzufügen mit den Fragetypen](assets/testerstellung_3_8_v1_de.png){ class="lightbox" title="Testeditor" }

<br>

> <h3>Fragen aus Fragenpool importieren</h3>

<br>

9\. Ihre Fragen aus dem Fragenpool übernehmen Sie im selben Menü mit "Fragen aus Pool importieren". OpenOlat kopiert sie in den Test; dort sind sie zunächst schreibgeschützt. Wie Sie eine solche Frage bearbeiten, steht unter [Fragen aus dem Fragenpool verwenden](../../manual_user/learningresources/Test_editor_QTI_2.1/index.de.md#questions_from_pool).

![Eintrag Fragen aus Pool importieren im Menü Elemente hinzufügen markiert](assets/testerstellung_3_9_v1_de.png){ class="lightbox" title="Menü Elemente hinzufügen im Testeditor" }

10\. Der Dialog "Fragen auswählen" zeigt Ihre Fragen unter "Meine Favoriten" und "Meine Fragen", je nach Konfiguration auch unter "Meine Listen" und "Meine Shares". Ein Klick auf den Titel einer Frage fügt sie direkt ein. Für mehrere Fragen setzen Sie die Häkchen und klicken auf "Auswählen".

![Ausgewählte Frage und Button Auswählen markiert](assets/testerstellung_3_10_v1_de.png){ class="lightbox" title="Dialog Fragen auswählen" }

11\. Mit Sektionen oder [Test-Parts](../../manual_user/learningresources/Configure_tests.de.md#testpart) gliedern Sie die Fragen im Test bei Bedarf weiter. Sind alle Fragen in der Test-Lernressource, verlassen Sie den Testeditor.

<br>

> <h3>Test-Lernressource in den Test-Kursbaustein einfügen</h3>

<br>

12\. Öffnen Sie im Autorenbereich den Kurs, in den die Test-Lernressource gehört. Ihre Kurse finden Sie in den Tabs "Meine Kurse" und "Meine Einträge".

13\. Öffnen Sie den Kurseditor über `Kurs > Administration > Kurseditor`. Klicken Sie auf "Kursbausteine einfügen" und wählen Sie den Typ "Test" oder "Selbsttest".

14\. Öffnen Sie im neuen Kursbaustein den Tab "Test-Konfiguration" und klicken Sie auf "Auswählen".<br>
Im Dialog "Test-Lernressource auswählen" wählen Sie den vorbereiteten Test.

15\. Der Tab "Test-Konfiguration" zeigt nun den eingebundenen Test. Mit "Vorschau" sehen Sie ihn an, mit "Lernressource bearbeiten" öffnen Sie ihn zum Bearbeiten. Sobald Teilnehmende den Test gestartet haben, ist die Bearbeitung begrenzt.

16\. Konfigurieren Sie bei Bedarf die weiteren Tabs des Kursbausteins. Einen Teil der Einstellungen der Test-Lernressource übersteuern Sie hier für diesen Kurs. Das lohnt sich, wenn Sie dieselbe Test-Lernressource in verschiedenen Kursen verwenden.

17\. Damit Teilnehmende den Test bearbeiten können, publizieren Sie den Kurs. Schliessen Sie dazu den Kurseditor, zum Beispiel mit einem Klick auf den Namen des Kurses in der Krümelnavigation, und wählen Sie im folgenden Dialog "Manuell publizieren" oder "Automatisch publizieren".

Alternativ klicken Sie im Kurseditor rechts in der Toolbar auf "Publizieren" oder schliessen den Kurseditor über das kleine rote Kreuz rechts oben.

18\. Setzen Sie danach den Status des Kurses auf "Veröffentlicht", damit Teilnehmende den Test bearbeiten können.<br>
Wer Zugang erhält, bestimmen Sie unter `Kurs > Administration > Mitgliederverwaltung`.

19\. Sobald Testergebnisse vorliegen, bewerten Betreuer:innen die Teilnehmenden im Bewertungswerkzeug. Beim Selbsttest entfällt dieser Schritt.<br>
Wie das geht, beschreibt die Seite [Tests bewerten](../../manual_user/learningresources/Assessing_tests.de.md).


<br>

---

## Checkliste {: #checklist}

Bevor Teilnehmende den Test bearbeiten, prüfen Sie diese Punkte:

- [x] Kurs vorhanden?

- [x] Kursbaustein "Test" oder "Selbsttest" vorhanden?

- [x] Lernressource "Test" erstellt?

- [x] Vorhandene Fragen aus dem Fragenpool in die Lernressource übernommen?

- [x] Zusätzliche Fragen in der Lernressource erstellt?

- [x] Test-Lernressource konfiguriert?

- [x] Test-Kursbaustein konfiguriert?

- [x] Kurs publiziert und Status "Veröffentlicht" gesetzt?

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../my_first_course/my_first_course.de.md)<br>
[Test konfigurieren >](../../manual_user/learningresources/Configure_tests.de.md)<br>
[Tests bewerten >](../../manual_user/learningresources/Assessing_tests.de.md)<br>
[Nutzen von Metadaten >](../question_metadata/question_metadata.de.md)<br>
[Testeditor >](../../manual_user/learningresources/Test_editor_QTI_2.1/index.de.md)

**Weiterführend**<br>
[Kursbaustein "Test" >](../../manual_user/learningresources/Course_Element_Test/index.de.md)<br>
[Fragenpool: Übersicht >](../../manual_user/area_modules/Question_Bank/index.de.md)<br>
[Wie wechsle ich einen Test aus? >](../exchange_tests/exchange_tests.de.md)

**youtube**<br>
[Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>)<br>
[Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>)<br>
[Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>)<br>
[Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>)<br>
[Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>)<br>
[Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>)<br>
[Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>)<br>
[Tests erstellen/bearbeiten](<https://www.youtube.com/embed/eNNdDdQDlfs>)

[Zum Seitenanfang ^](#test_creation_procedure)
