# Wie gehe ich vor, wenn ich einen Test erstelle? {: #test_creation_procedure}

??? abstract "Ziel und Inhalt dieser Anleitung"

    Für das Erstellen von Tests gibt es in OpenOlat verschiedene Wege. Hier werden Ihnen im Überblick die gängigen Wege aufgezeigt. Lernen Sie die Möglichkeiten kennen und wählen Sie dann das für Sie passende Vorgehen.

    Alle drei Wege setzen die Rolle Autor:in voraus. Mit ihr zeigt die Hauptnavigation den Autorenbereich und den Fragenpool.

??? abstract "Zielgruppe"

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Expert:innen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)


---

## Das Zusammenwirken der Bestandteile

![Kursbaustein vom Typ Test mit eingefügter Lernressource Test, deren Fragen mit dem Fragenpool ausgetauscht werden](assets/kurs-kursbaustein-lernressource-frage_v1_de.png){ class="lightbox" title="Kurs, Kursbaustein, Lernressource und Fragenpool" }

**Kurs:**<br> Er wird im Kurseditor aus Kursbausteinen zusammengesetzt.

**Kursbaustein:** <br>Die meisten Kursbausteine sind Behälter, in die eine Lernressource eingefügt wird. Z.B. wird in den Kursbaustein "Test" eine Lernressource "Test" eingefügt. Bitte diese beiden "Tests" unterscheiden!

**Fragen:** <br>Eine Test-Lernressource besteht aus mehreren einzelnen Fragen, z.B. Single Choice, Multiple Choice usw.

**Fragenpool:** <br>Die Einzelfragen können in einem Fragenpool gesammelt werden. Beim Erstellen verschiedener Test-Lernressourcen kann dann auf den Fragenpool zugegriffen werden. Bereits vorhandene Fragen des Fragenpools können übernommen (von dort kopiert) werden und evtl. zusätzliche weitere Fragen neu erstellt werden. <br>
Fragen können im Fragenpool oder der Lernressource erstellt werden. In der Lernressource erstellte Fragen sind nur in dieser Test-Lernressource vorhanden, solange sie nicht zur Mehrfachnutzung in den Fragenpool übergeben werden.

<br>

Zu jedem der Elemente können Einstellungen (Konfigurationen) vorgenommen werden. Die Konfigurationen können also auf unterschiedlichen Ebenen vorgenommen werden.

![Vier ineinander liegende Ebenen mit je eigener Konfiguration: Kurs, Kursbaustein Test, Lernressource Test und Frage](assets/grafik_konfigurationsebenen_v1_de.png){ width=450px class="lightbox" title="Konfigurationsebenen eines Tests" }


**Konfiguration des Kurses:**<br>
`Autorenbereich > Kurs wählen > Administration > Einstellungen`

**Konfiguration des Kursbausteins:**<br>
`Autorenbereich > Kurs wählen > Administration > Kurseditor > Kursbaustein wählen > Einstellungen in den Tabs`

**Konfiguration der Lernressource:**<br>
`Autorenbereich > Test-Lernressource auswählen > Administration > Einstellungen`

**Konfiguration einer Frage:**<br>
`Autorenbereich > Test-Lernressource auswählen > Administration > Testeditor > Frage in der Baumstruktur wählen > Einstellungen in den Tabs`

<br>

:octicons-device-camera-video-24: **Video-Einführung**: [Funktionsprinzipien](<https://www.youtube.com/embed/M-JkSAFN298>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Kurse erstellen und bearbeiten](<https://www.youtube.com/embed/SfOSyDG0qvE>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>){:target="_blank"}

:octicons-device-camera-video-24: **Video-Einführung**: [Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>){:target="_blank"}

<br>

---

## Vorgehen Möglichkeit 1

Wenn Sie völlig von vorne mit der Erstellung eines Kurses beginnen, liegt folgendes Vorgehen nahe.<br>

<br>

![Vier Schritte vom Erstellen des Kurses bis zum Erstellen der Fragen in der Test-Lernressource](assets/flowchart_testerstellung1_v1_de.png){ class="lightbox" title="Vorgehen Möglichkeit 1" }

<br>

> <h3>Kurs erstellen</h3>

<br>

!!! note "Hinweis"

    Sollten Sie noch keine Erfahrung in der Kurserstellung haben, finden Sie im Kapitel [„Wie erstelle ich meinen ersten OpenOlat-Kurs"](../my_first_course/my_first_course.de.md) eine Anleitung.

1\. Gehen Sie in den Autorenbereich und erstellen Sie dort einen neuen Kurs.

![Menü Erstellen geöffnet, Eintrag Kurs markiert](assets/testerstellung_1_1_v1_de.png){ class="lightbox" title="Autorenbereich" }

2\. Vergeben Sie einen Titel und nehmen Sie erste Einstellungen zum Kurs vor. Entscheiden Sie sich für ein Design.

![Titel des Kurses eingetragen und Kursdesign Mit Lernpfad gewählt, darunter der Button Erstellen](assets/testerstellung_1_2_v1_de.png){ class="lightbox" title="Dialog Kurs erstellen" }

3\. Wenn Sie für den weiteren Prozess der Kurserstellung einen Wizard (Kursassistent:in) verwenden wollen, werden Sie gefragt, ob Sie einen Prüfungskurs erstellen wollen.<br>
Ein Prüfungskurs ist ein normaler Kurs (egal ob Lernpfadkurs oder herkömmlicher Kurs), der bereits eine bestimmte Konfiguration enthält. Diese Option bietet also eine spätere Arbeitserleichterung.

![Button Mit Kursassistent:in erstellen geöffnet, mit den Einträgen Einfacher Kurs und Prüfungskurs](assets/testerstellung_1_3_v1_de.png){ class="lightbox" title="Dialog Kurs erstellen mit Kursassistent:in" }

4\. Der erste Screen nach Klick auf den Button "Erstellen" ist die Übersicht der Einstellungen (Konfiguration des Kurses).

!!! tip "Tipp"

    Abgesehen vom Kursdesign, können Sie die übrigen Angaben auch später unter `Kurs > Administration > Einstellungen` wieder aufrufen und anpassen.

![Eintrag Einstellungen im Menü Administration markiert, daneben die Tabs der Kurseinstellungen von Info bis Optionen](assets/testerstellung_1_4_v1_de.png){ class="lightbox" title="Einstellungen des Kurses" }

<br>

> <h3>Kursbaustein "Test" einfügen</h3>

<br>

5\. Öffnen Sie über die "Administration" den **Kurseditor**. Wählen Sie "Kursbausteine einfügen" und klicken Sie dort auf den gewünschten Kursbaustein-Typ "Test" oder "Selbsttest". Dadurch wird ein Kursbaustein dieses Typs eingefügt.

![Eintrag Kurseditor im Menü Administration und Button Kursbausteine einfügen markiert](assets/testerstellung_1_5_v1_de.png){ class="lightbox" title="Kurseditor" }

<br>

> <h3>im Kursbaustein Test-Lernressource erstellen</h3>

<br>

6\. Wählen Sie links im Kursmenü den Test-Kursbaustein an.

7\. In den zugehörigen Tabs auf der rechten Seite befindet sich unter "Test-Konfiguration" der Button "Erstellen". Erstellen Sie mit ihm eine neue Test-Lernressource.

![Kursbaustein Test im Kursmenü, Tab Test-Konfiguration und Button Erstellen markiert](assets/testerstellung_1_7_v1_de.png){ class="lightbox" title="Kursbaustein Test im Kurseditor" }

8\. Vergeben Sie auch für die Test-Lernressource einen Namen.

![Titel der neuen Test-Lernressource im Feld Titel eingetragen](assets/testerstellung_1_8_v1_de.png){ class="lightbox" title="Dialog Test erstellen" }

<br>

> <h3>Lernressource editieren und Fragen erstellen</h3>

<br>

9\. Nach dem Erstellen der neuen Test-Lernressource haben Sie die Möglichkeit, die Lernressource zu bearbeiten, also Fragen zu ergänzen.

![Eingebundene Test-Lernressource mit Fragetypen und Punkten, Link Lernressource bearbeiten markiert](assets/testerstellung_1_9_v1_de.png){ class="lightbox" title="Tab Test-Konfiguration im Kursbaustein Test" }

10\. Standardmässig ist bereits eine Single Choice Frage vorhanden. Sie können diese als Muster verwenden, löschen oder entsprechend Ihren Bedürfnissen abändern.

![Neue Test-Lernressource mit einer Single-Choice-Frage und der Antwort Neue Antwort, in der Toolbar die Links Administration und Infoseite](assets/testerstellung_1_10_v2_de.png){ class="lightbox" title="Test-Lernressource · 2026.09.28" }

11\. Wählen Sie in der "Administration" der Test-Lernressource nun den Eintrag "Testeditor". Sie gelangen in den Testeditor der Lernressource, nicht in den Kurseditor.

![Eintrag Testeditor im Menü Administration markiert](assets/testerstellung_1_11_v2_de.png){ class="lightbox" title="Menü Administration einer Test-Lernressource · 2026.09.28" }

12\. Wählen Sie "Elemente hinzufügen" und den passenden Fragetyp, z.B. Multiple Choice.

![Button Elemente hinzufügen markiert, darunter eine neue Multiple-Choice-Frage im Tab Auswahl](assets/testerstellung_1_12_v1_de.png){ class="lightbox" title="Testeditor" }

13\. Geben Sie im Tab "Auswahl" den Titel der Frage, die Fragestellung und die möglichen Antworten ein. Weitere Antwortmöglichkeiten werden über das Pluszeichen ergänzt.

14\. Im Tab "Punkte" definieren Sie die Art und die Summe der Punkte.

15\. Bei Bedarf definieren Sie ein Feedback zur Frage. Über "Vorschau" können Sie sich die Frage ansehen.

Nach dem gleichen Prinzip fügen Sie weitere Fragen hinzu. Dabei können die Details der Einstellungen je nach Fragetyp variieren. Sie können Ihren Test auch mit Sektionen oder Test-Parts weiter strukturieren.


!!! warning "Achtung"

    Überlegen Sie sich unbedingt im Vorfeld, welcher Fragetyp für Ihre jeweilige Zwecke am geeignetsten ist, da der Fragetyp im Nachhinein nicht mehr geändert werden kann.

!!! tip "Tipp"

    Das Kopieren von Fragen empfiehlt sich dann, wenn Sie mehrere Fragen mit denselben Antwortmöglichkeiten haben, z.B. mehrere Fragen mit einem Wert aus einer Skala von 1-5.

<br>

---

## Vorgehen Möglichkeit 2

Haben Sie bereits etwas Erfahrung als Autor:in und besteht bereits ein Kurs, können Sie mit der Lernressource "Test" beginnen.

<br>

![Fünf Schritte vom Erstellen der Test-Lernressource bis zum Einfügen in den Test-Kursbaustein](assets/flowchart_testerstellung2_v1_de.png){ class="lightbox" title="Vorgehen Möglichkeit 2" }

<br>

> <h3>Test-Lernressource erstellen</h3>

<br>

1\. Im Autorenbereich den Link "Erstellen" wählen und die Lernressource "Test" wählen.

![Eintrag Test (QTI 2.1) im Menü Erstellen gewählt](assets/testerstellung_2_1_v1_de.png){ class="shadow lightbox" title="Autorenbereich" }

2\. Titel des Tests eintragen

![Titel der Lernressource E-Learning Grundlagen eingetragen, darunter der Button Erstellen](assets/testerstellung_2_2_v1_de.png){ class="shadow lightbox" title="Dialog zum Erstellen eines Tests" }

3\. Es erscheint ein Menü. Hier können Sie in den unterschiedlichen Tabs bei Bedarf weitere Einstellungen vornehmen.

Das Menü entspricht den Einstellungen im Bereich Administration und kann auch später noch bearbeitet werden.

![Tabs Info, Metadaten, Freigabe, Katalog und Optionen](assets/testerstellung_2_3_v1_de.png){ class="shadow lightbox" title="Einstellungen der Test-Lernressource" }

:octicons-device-camera-video-24: **Video-Einführung**: [Test-Lernressource erstellen](<https://www.youtube.com/embed/WUs-upCf2tQ>){:target="_blank"}

<br>

> <h3>Lernressource editieren und Fragen erstellen</h3>

<br>

4\. Wählen Sie in der "Administration" der Lernressource Test den Eintrag "Testeditor". Sie gelangen in den Testeditor.

![Eintrag Testeditor im Menü Administration markiert](assets/testerstellung_1_11_v2_de.png){ class="shadow lightbox" title="Menü Administration einer Test-Lernressource · 2026.09.28" }

5\. "Elemente hinzufügen" wählen und den passenden Fragetyp auswählen, z.B. Multiple Choice.

6\. Im Tab "Auswahl" den Titel der Frage, die Fragestellung und die möglichen Antworten eingeben. Weitere Antwortmöglichkeiten werden über das Pluszeichen ergänzt.

7\. Im Tab "Punkte" die Art und die Summe der Punkte definieren.

8\. Bei Bedarf ein Feedback zur Frage definieren und sich die Frage über die Vorschau anschauen.

Nach dem gleichen Prinzip fügen Sie weitere Fragen hinzu. Dabei können die Details der Einstellungen je nach Fragetyp variieren. Sie können Ihren Test auch mit Sektionen oder Test-Parts weiter strukturieren.

:octicons-device-camera-video-24: **Video-Einführung**: [Fragen erstellen](<https://www.youtube.com/embed/2ZrINPQ6tYw>){:target="_blank"}

!!! info "Wichtig"

    Standardmässig ist bereits eine Single Choice Frage angelegt, die Sie nutzen und bearbeiten oder löschen sollten.

!!! warning "Achtung"

    Überlegen Sie sich unbedingt im Vorfeld, welcher Fragetyp für Ihre jeweilige Zwecke am geeignetsten ist, da der Fragetyp im Nachhinein nicht mehr geändert werden kann.

!!! tip "Tipp"

    Das Kopieren von Fragen empfiehlt sich dann, wenn Sie mehrere Fragen mit denselben Antwortmöglichkeiten haben, z.B. mehrere Fragen mit einem Wert aus einer Skala von 1-5.

<br>

> <h3>Test-Lernressource konfigurieren</h3>

<br>

9\. Wählen Sie das oberste Element der Test-Lernressource und bearbeiten Sie die zugehörigen Tabs nach Bedarf.

![Maximal 50 Punkte, Ausgabe von Bestanden automatisch durch Punkteschwelle und eine Zeitbeschränkung von 30 Minuten](assets/testerstellung_2_9_v1_de.png){ class="shadow lightbox" title="Tab Test Konfiguration im Testeditor" }

10\. **Test Konfiguration:** Definieren Sie ab wieviel Punkten der Test bestanden ist und ob bzw. welche Zeitbeschränkung es gibt.

Definieren Sie, falls gewünscht, ein **generelles Feedback:** für den Fall, dass der Test bestanden wurde bzw. nicht bestanden wurde (gilt für automatisches Bestehen).

11\. **Expert:** Weitere Details des Testablaufs konfigurieren, z.B. Art der Navigation oder die Anzeige von Lösungen.

12\. Abschliessend den Testeditor schliessen, indem man in der Krümelnavigation auf den Titel des Tests klickt.

![Titel des Tests in der Krümelnavigation angeklickt](assets/testerstellung_2_12_v1_de.png){ class="shadow lightbox" title="Krümelnavigation im Testeditor" }

:octicons-device-camera-video-24: **Video-Einführung**: [Kursbausteine konfigurieren](<https://www.youtube.com/embed/SAkzzoOQEoQ>){:target="_blank"}

!!! tip "Tipp"

    Sie können sowohl ein Feedback für einzelne Fragen als auch für den gesamten Test erstellen.

<br>

> <h3>Kursbaustein "Test" in den vorhandenen Kurs einfügen</h3>

<br>

13\. Gehen Sie in den Autorenbereich. Im Bereich "Meine Einträge" finden Sie Ihre Kurse. Öffnen Sie den Kurs in dem der Test eingebunden werden soll.

14\. Öffnen Sie über die "Administration" den "Kurseditor". Wählen Sie "Kursbausteine einfügen" und klicken Sie auf den gewünschten Kursbaustein-Typ "Test" oder "Selbsttest".

<br>

> <h3>Test-Lernressource in den Test-Kursbaustein einfügen</h3>

<br>

15\. Gehen Sie in den Tab "Test-Konfiguration" und klicken Sie den Button "Datei wählen, erstellen oder importieren"<br>
Es erscheint eine Liste mit Ihren Test-Lernressourcen. Wählen Sie den vorbereiteten Test aus, indem Sie auf den Auswahlhaken klicken.

![Gewählte Datei noch leer, darunter der Button Datei wählen, erstellen oder importieren](assets/testerstellung_2_15_v1_de.png){ class="shadow lightbox" title="Tab Test-Konfiguration im Kursbaustein Test" }

16\. Bei Bedarf können Sie sich im Tab "Test-Konfiguration" unter "Gewählte Datei" den eingebundenen Test in der Vorschau anzeigen lassen und auch noch editieren, solange er nicht von Teilnehmenden bearbeitet wurde.

![Eingebundener Test unter Gewählte Datei mit den Buttons Datei auswechseln, Editieren und Vorschau anzeigen](assets/testerstellung_2_16_v1_de.png){ class="shadow lightbox" title="Tab Test-Konfiguration mit gewähltem Test" }

17\. Bei Bedarf können noch die weiteren Tabs des Kursbausteins konfiguriert werden. Sie können teilweise die Einstellungen der Test-Lernressource mit den Einstellungen des Kursbausteins übersteuern. Das macht Sinn, wenn die gleiche Test-Lernressource in verschiedenen Kursen verwendet wird.

18\. Damit der Test von den Lernenden bearbeitet werden kann, muss der Kurs noch publiziert werden. Dafür einfach den Kurseditor z.B. durch Klick auf den Namen des Kurses in der Krümelnavigation schliessen und im erscheinenden Dialog "Manuell publizieren" oder "Automatisch publizieren" wählen.

Alternativ kann auch der "Publizieren"-Button im Editor rechts in der Toolleiste oder das kleine rote Kreuz rechts oben verwendet werden.

19\. Damit die Lernenden den Test bearbeiten können, muss der Status des Kurses noch auf "Veröffentlicht" umgestellt werden.<br>
Welche Lernenden Zugriff erhalten, bestimmen Sie in der Mitgliederverwaltung des Kurses.

20\. Sobald Testergebnisse vorhanden sind, können Betreuende im Bewertungswerkzeug Bewertungen vornehmen. (Gilt nicht bei Selbsttests.)<br>
Weitere Infos dazu finden Sie im Kapitel "[Tests bewerten](../../manual_user/learningresources/Assessing_tests.de.md)".

<br>

---

## Vorgehen Möglichkeit 3

Besteht Arbeitsteilung und Sie sollen als Fachexpert:in die Fragen erstellen, die verschiedene Kolleg:innen in ihren Tests verwenden können?<br>
Dann können Sie auch mit dem Erstellen der einzelnen Fragen im Fragenpool beginnen.

<br>

![Vier Schritte vom Erstellen der Fragen im Fragenpool bis zum Einfügen des Tests in den Test-Kursbaustein](assets/flowchart_testerstellung3_v1_de.png){ class="lightbox" title="Vorgehen Möglichkeit 3" }

<br>

> <h3>Fragen im Fragenpool erstellen</h3>

<br>

1\. Wenn Sie Autorenrechte besitzen, wird in der Hauptnavigation ausser dem Autorenbereich auch der Fragenpool angezeigt. Gehen Sie in den Fragenpool.

![Fragenpool markiert und geöffnet, links das Menü Mein Fragenpool](assets/testerstellung_3_1_v1_de.png){ class="lightbox" title="Fragenpool in der Hauptnavigation" }

2\. Wählen Sie "Frage erstellen" und den passenden Fragetyp, z.B. Multiple Choice.

![Button Frage erstellen markiert, über der Liste Meine Fragen](assets/testerstellung_3_2_v1_de.png){ class="lightbox" title="Fragenpool" }

3\. Geben Sie im Tab "Auswahl" den Titel der Frage, die Fragestellung und die möglichen Antworten ein. Weitere Antwortmöglichkeiten werden über das Pluszeichen ergänzt.

![Tab Auswahl einer neuen Multiple-Choice-Frage im Fragenpool mit den Feldern Titel, Frage und vier Antworten, davon drei als korrekt angehakt](assets/testerstellung_3_3_v2_de.png){ class="lightbox" title="Frage im Fragenpool · 2026.09.28" }

4\. Im Tab "Punkte" definieren Sie die Art und die Summe der Punkte.

5\. Bei Bedarf definieren Sie ein Feedback zur Frage. Über "Vorschau" können Sie sich die Frage ansehen.

Nach dem gleichen Prinzip fügen Sie weitere Fragen hinzu. Dabei können die Details der Einstellungen je nach Fragetyp variieren. Sie können Ihren Test auch mit Sektionen oder Test-Parts weiter strukturieren.


!!! warning "Achtung"

    Überlegen Sie sich unbedingt im Vorfeld, welcher Fragetyp für Ihre jeweilige Zwecke am geeignetsten ist, da der Fragetyp im Nachhinein nicht mehr geändert werden kann.

!!! tip "Tipp"

    Das Kopieren von Fragen empfiehlt sich dann, wenn Sie mehrere Fragen mit denselben Antwortmöglichkeiten haben, z.B. mehrere Fragen mit einem Wert aus einer Skala von 1-5.


<br>

> <h3>Test-Lernressource erstellen und editieren</h3>

<br>

6\. Wechseln Sie in den Autorenbereich und erstellen Sie einen Test (Test-Lernressource).

![Eintrag Test im Menü Erstellen markiert](assets/testerstellung_3_6_v1_de.png){ class="lightbox" title="Autorenbereich" }

!!! note "Hinweis"

    Die neue Test-Lernressource wird im Autorenbereich nicht unter dem Tab "Meine Kurse" aufgelistet, sondern unter "Meine Einträge". Erkennbar am Symbol für Test-Lernressourcen.
    ![Tab Meine Einträge mit Filter Typ Test, Test-Symbol in der Spalte Typ markiert](assets/testerstellung_3_6b_v1_de.png){ class="lightbox" title="Tab Meine Einträge im Autorenbereich" }

7\. Öffnen Sie den Editor durch Klick auf **Administration** und dann **"Testeditor"**.

![Eintrag Testeditor im Menü Administration markiert](assets/testerstellung_3_7_v2_de.png){ class="lightbox" title="Menü Administration einer Test-Lernressource · 2026.09.28" }

8\. Im Testeditor (erkennbar an der schraffierten Kopfzeile) können Sie nun unter **"Elemente hinzufügen"** neue Fragen hinzufügen.

![Geöffnetes Menü Elemente hinzufügen mit den Fragetypen](assets/testerstellung_3_8_v1_de.png){ class="lightbox" title="Testeditor" }

<br>

> <h3>Fragen aus Fragenpool importieren</h3>

<br>

9\. Alternativ zur Erstellung neuer Fragen, können Sie unter dem gleichen Menüpunkt bereits vorhandene Fragen mit **"Fragen aus Pool importieren"** übernehmen.

![Eintrag Fragen aus Pool importieren im Menü Elemente hinzufügen markiert](assets/testerstellung_3_9_v1_de.png){ class="lightbox" title="Menü Elemente hinzufügen im Testeditor" }

10\. Klicken Sie auf den Titel einer einzelnen Frage, wird sie direkt eingefügt. Um mehrere Fragen zu importieren, markieren Sie die Fragen und bestätigen mit Klick auf den Button "Auswählen".

![Ausgewählte Frage und Button Auswählen markiert](assets/testerstellung_3_10_v1_de.png){ class="lightbox" title="Dialog Fragen auswählen" }

11\. Sind alle Fragen in der Test-Lernressource erfasst, verlassen Sie den Editor der Lernressource.

<br>

> <h3>Test-Lernressource in den Test-Kursbaustein einfügen</h3>

<br>

12\. Gehen Sie in den Autorenbereich. Im Bereich "Meine Einträge" finden Sie Ihre Kurse. Öffnen Sie den Kurs in dem die Test-Lernressource eingebunden werden soll.

13\. Öffnen Sie über die "Administration" den "Kurseditor". Wählen Sie "Kursbausteine einfügen" und klicken Sie auf den gewünschten Kursbaustein-Typ "Test" oder "Selbsttest".

14\. Gehen Sie in den Tab "Test-Konfiguration" und klicken Sie den Button "Datei wählen, erstellen oder importieren".<br>
Es erscheint eine Liste mit Ihren Test-Lernressourcen. Wählen Sie den vorbereiteten Test aus, indem Sie auf den Auswahlhaken klicken.

15\. Bei Bedarf können Sie sich im Tab "Test-Konfiguration" unter "Gewählte Datei" den eingebundenen Test in der Vorschau anzeigen lassen und auch noch editieren, solange er nicht von Teilnehmenden bearbeitet wurde.

16\. Je nach Bedarf können noch die weiteren Tabs des Kursbausteins konfiguriert werden. Sie können teilweise die Einstellungen der Test-Lernressource mit den Einstellungen des Kursbausteins übersteuern. Das macht Sinn, wenn die gleiche Test-Lernressource in verschiedenen Kursen verwendet wird.

17\. Damit der Test von den Lernenden bearbeitet werden kann, muss der Kurs noch publiziert werden. Dafür einfach den Kurseditor z.B. durch Klick auf den Namen des Kurses in der Krümelnavigation schliessen und im erscheinenden Dialog "Manuell publizieren" oder "Automatisch publizieren" wählen.

Alternativ kann auch der "Publizieren"-Button im Editor rechts in der Toolleiste oder das kleine rote Kreuz rechts oben verwendet werden.

18\. Damit die Lernenden den Test bearbeiten können, muss der Status des Kurses noch auf "Veröffentlicht" umgestellt werden.<br>
Welche Lernenden Zugriff erhalten, bestimmen Sie in der Mitgliederverwaltung des Kurses.

19\. Sobald Testergebnisse vorhanden sind, können Betreuende im Bewertungswerkzeug Bewertungen vornehmen. (Gilt nicht bei Selbsttests.)<br>
Weitere Infos dazu finden Sie im Kapitel "[Tests bewerten](../../manual_user/learningresources/Assessing_tests.de.md)".


<br>

---

## Checkliste {: #checklist}

- [x] Kurs vorhanden?

- [x] Kursbaustein "Test" oder "Selbsttest" vorhanden?

- [x] Lernressource "Test" erstellt?

- [x] im Fragenpool vorhandene Fragen in Lernressource übernommen?

- [x] zusätzliche Fragen innerhalb der Lernressource erstellt?

- [x] Test-Lernressource konfiguriert?

- [x] Test-Kursbaustein konfiguriert?

---

## Weiterführende Informationen {: #further_information}

[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../my_first_course/my_first_course.de.md)<br>
[Tests bewerten >](../../manual_user/learningresources/Assessing_tests.de.md)<br>
[Testeditor >](../../manual_user/learningresources/Test_editor_QTI_2.1.de.md)<br>
[Kursbaustein "Test" >](../../manual_user/learningresources/Course_Element_Test.de.md)<br>
[Fragenpool: Übersicht >](../../manual_user/area_modules/Question_Bank.de.md)<br>
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
