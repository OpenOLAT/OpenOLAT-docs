# :o_icon_o_icon_qpool: Fragenpool: Übersicht {: #question_bank}

Der kollaborative Fragenpool in OpenOlat erlaubt Autor:innen, Testfragen als eigenständige Items in einer katalogähnlichen Struktur zu erstellen, zu speichern, zu bearbeiten und weiter zu verwenden. 

Es ist eine **Sammlung (Datenbank)** vieler einzelner Testfragen, in der Regel im QTI-Format, inklusive aller zugehörigen Informationen und Metadaten.

Die Fragen können mit anderen Personen, die auch Zugriff auf den Pool haben, geteilt werden.

**Ziel** ist die **Wiederverwendung** einmal erstellter Fragen. Sei es in Tests, als Quizfrage in einem interaktiven Video oder in einem Kursbaustein vom Typ "Seite". Durch Sie selbst oder (bei Freigabe) durch andere Autor:innen.

**Zugriff** auf den Fragenpool haben **Autor:innen**, Poolverwalter:innen und Administrator:innen. Ihnen zeigt OpenOlat den Fragenpool in der Hauptnavigation in der Kopfzeile an.

![Fragenpool als eigener Eintrag in der Hauptnavigation, links sein Menü mit vier Bereichen, rechts die Willkommensseite. Startseite des Fragenpools.](assets/question_bank_navigation1_v1_de.png){ class="shadow lightbox" }

## Steckbrief

Name | Fragenpool
---------|----------
Verfügbar seit | Release 9.0 (OO-533)


!!! note "Quick Links"

    * [Handhabung der Daten](Data_Management.de.md)
    * [Fragen importieren](Question_Bank_Import_Questions.de.md)
    * [Detailansicht einer Frage](Item_Detailed_View.de.md)
    * [Mögliche Aktionen im Fragenpool](Question_bank_possible_operations.de.md)
    * [Suche im Fragenpool](Question_Pool_Search.de.md)
    * [Freigabemöglichkeiten im Fragenpool](Question_Pool_Sharing_Options.de.md)
    * [Beurteilungsprozess für Fragen im Pool](Question_Bank_Review_Process.de.md)
    * [Fragenpool-Administration](Question_Bank_Administration.de.md)

Das Menü des Fragenpools ist in folgende Bereiche gegliedert:

## Mein Fragenpool {: #my_question_bank}

Unter "**Meine Fragen**"  finden Sie Ihre eigenen Fragen. Sie können die Fragen als **Favoriten** markieren und sie in **Listen** zusammenfassen. Favoriten und Listen sind zwei Möglichkeiten um Items zu sortieren und zu organisieren. 

Items, die unter "**Meine Fragen**" als Favorit gekennzeichnet wurden, erscheinen unter dem Menüpunkt "**Meine Favoriten**" erneut. Es handelt sich dabei um ein und dasselbe Item. Änderungen in den "Favoriten" werden somit auch unter "Meine Fragen" gespeichert.

Ist der [Beurteilungsprozess](Question_Bank_Review_Process.de.md) aktiviert (Autor:innen beurteilen die erstellten Fragen gegenseitig), zeigt "Mein Fragenpool" zusätzlich Ihre Fachbereiche. Je nach Berechtigung erscheinen im Menü ausserdem die Bereiche **"Beurteilung"** und **"Final"**.

![Aufgeklappter Bereich Mein Fragenpool mit Meine Fragen, Meine Favoriten und zwei eigenen Listen, rechts die Fragentabelle mit den Aktionsbuttons. Fragenpool.](assets/question_bank_navigation_my_question_bank_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#question_bank)


## Freigaben {: #sharing_options}

Im Bereich "**Freigaben**" werden Pools und Gruppen zum Austausch von Fragen zur Verfügung gestellt. Während Favoriten und Listen der persönlichen Ordnung und Sortierung dienen, sind die Pools die Sammelstelle für alle freigegebenen Items. Bevor ein Item in einem Pool gelistet wird, muss dieses entweder zuerst von der Besitzer:in freigegeben, oder direkt in den entsprechenden Pool importiert werden. 

Das Symbol vor jedem Eintrag zeigt die Art der Freigabe: :o_icon_o_icon_pool_pool: steht für einen Pool, :o_icon_o_icon_pool_share: für eine Gruppe, für die Fragen freigegeben sind.

Listen, Pools und Gruppen können Administrator:innen in der System-Administration deaktivieren, sie sind deshalb eventuell nicht sichtbar: `Administration > e-Assessment > Fragenpool`

[Zum Seitenanfang ^](#question_bank)


## Fragen {: #questions}

Den Bereich "Fragen" sehen Administrator:innen sowie Poolverwalter:innen, wenn ihnen in der System-Administration das Recht "alle Fragen sehen und die Metadaten bearbeiten" erteilt ist. Im Unterschied zu "**Meine Fragen**" listet er **alle** Fragen des Fragenpools auf, auch Fragen anderer Autor:innen. Die Einträge "Ohne Fachbereich" und "Ohne Autor:in" zeigen Fragen, denen diese Angaben fehlen.

Fragen können auch [mit Hilfe von KI erstellt](Question_Bank_Create_Questions.de.md#create_with_AI) werden, als Multiple-Choice-Fragen und als Freitextfragen mit KI-Korrektur.

Einzelne Fragen, ganze Sektionen oder Tests können auch direkt aus dem [Testeditor](../learningresources/Test_editor_QTI_2.1.de.md) in den Pool exportiert werden. Wählen Sie dazu im Testeditor in der Toolbar: `Export > Zum Pool exportieren`. Abhängig davon auf welcher Stufe Sie sich im Menübaum links befinden, werden entweder einzelne Fragen, einzelne Sektionen oder der ganze Test in den Fragenpool exportiert.

Die Fragen können mit anderen Personen geteilt werden, die entsprechend der Konfiguration in der [System-Administration](../../manual_admin/administration/eAssessment_Question_bank.de.md) Zugriff auf den Pool haben.

Dieses Kapitel erklärt, wie einzelne Testfragen, sogenannte Items, mit dem Fragenpool erstellt, bearbeitet und verwaltet werden können. Jedes Item enthält nicht nur die Frage samt den dazugehörigen Antworten, sondern auch Informationen zu z.B. Autor:in, Erstelldatum, Schlagworte, aber auch Kennwerte zur Itemanalyse können hinzugefügt werden.


[Zum Seitenanfang ^](#question_bank)


## Administration {: #administration}

[Poolverwalter:innen](Question_Bank_Administration.de.md#pool_manager) bekommen zusätzlich den Bereich Administration des Fragenpools angezeigt und haben dort Zugriff auf weitere spezifische Konfigurationen.

![Aufgeklappter Bereich Administration mit Beurteilungsprozess, Fachbereich, Pool-Verwaltung, Fragetyp und Stufe, rechts die Einstellungen des Beurteilungsprozesses. Fragenpool.](assets/question_bank_navigation_administration_v1_de.png){ class="shadow lightbox" }


[Zu den Details >](Question_Bank_Administration.de.md)<br>
[Zum Seitenanfang ^](#question_bank)


## Weiterführende Informationen {: #further_information}

[Tests erstellen >](../learningresources/Test.de.md)<br>
[Test Fragetypen >](../learningresources/Test_question_types.de.md)

[Zum Seitenanfang ^](#question_bank)