# Fragenpool: Beurteilungsprozess {: #review_process}

Mit dem Beurteilungsprozess prüfen Benutzer:innen des Fragenpools ihre Fragen gegenseitig, bevor die Fragen in Tests eingesetzt werden. Andere Benutzer:innen mit Rechten auf denselben Fachbereich bewerten eine Frage mit Sternen und geben mit einem Kommentar Rückmeldung. Erreicht die Frage genügend gute Bewertungen, wechselt sie in den Status "Final". So sichern Sie die Qualität Ihrer Fragen.

## Voraussetzungen

Den Beurteilungsprozess schalten Systemadministrator:innen in der System-Administration ein: `Administration > e-Assessment > Fragenpool`. Details dazu finden Sie auf der Seite [e-Assessment Administration: Fragenpool](../../manual_admin/administration/eAssessment_Question_bank.de.md).

Ausserdem braucht der Beurteilungsprozess Fachbereiche. Ein Fachbereich ist ein Fach oder Themengebiet, zum Beispiel Biologie oder Ornithologie. Jede Frage wird einem Fachbereich zugeordnet. Rechte auf einen Fachbereich erhalten Benutzer:innen über eine Kompetenz in diesem Fachbereich. Nur Fachbereiche, auf die sie Rechte haben, sehen sie im Fragenpool:

  * **Unterrichten**: Sie sehen den Fachbereich unter "Mein Fragenpool" und unter "Beurteilung" und beurteilen dort die Fragen anderer Benutzer:innen.
  * **Verwalten**: Sie sehen den Fachbereich ebenfalls, dazu die Bewertungen einer Frage. Sie können den Status einer Frage ändern, zum Beispiel auf "Final" oder "End of life".

Wie Sie Fachbereiche anlegen, erklärt die Seite [Fragenpool: Administration](Question_Bank_Administration.de.md#subject). Die Kompetenzen vergeben Sie im Tab "Kompetenzen" einer Taxonomieebene, siehe [Modul Taxonomie](../../manual_admin/administration/Modules_Taxonomy.de.md#taxonomy). Die Abbildungen unten zeigen den Beispiel-Fachbereich "Ornithologie".

## Prozess [:octicons-tag-16:{ title="ab Release 12.3 (OO-3111)" }](https://track.frentix.com/issue/OO-3111){:target="_blank"}

In der folgenden Grafik ist ein beispielhafter Prozessablauf dargestellt.

![Weg einer Frage über drei Rollen von Draft über Review nach Final und von dort in einen Test im Fachkurs](assets/question_bank_review_process_flow_v1_de.svg){ class="shadow lightbox" title="Beispielhafter Ablauf des Beurteilungsprozesses · 2026.11.11" }

Folgende Prozessschritte sind also im Beurteilungsprozess des Fragenpools abgebildet:

  1. Fragen werden entweder unter "Meine Fragen" oder direkt in einem eigenen Fachbereich unter "Mein Fragenpool" erstellt. Die Frage befindet sich im Status "Draft".
  2. Die Autor:in gibt die Frage mit "Beurteilungsprozess starten" in der Hinweisbox über der Frage in die Beurteilung und wählt im Dialog den Fachbereich. Der Status der Frage wechselt auf "Review". Ab jetzt lässt sich die Frage nicht mehr bearbeiten, und Bewertungen aus einer früheren Runde werden gelöscht.
  3. Die Fragen werden beurteilt. Die eigenen Fragen können nicht beurteilt werden, sondern nur die Fragen anderer Benutzer:innen mit Rechten auf denselben Fachbereich.
  4. a) Die Beurteilung ist ungenügend. Das heisst, eine Bewertung liegt unter der Untergrenze der Sterne. Die Frage geht zurück an die Autor:in in den Status "Revision". Hier kann die Frage überarbeitet und erneut in die Beurteilung gegeben werden.<br>
b) Die Beurteilung durch die Sterne ist genügend. Die festgelegte Anzahl Personen hat die Frage bewertet, und keine Bewertung liegt unter der Untergrenze. Die Frage wechselt in den Status "Final".
  5. Die Fragen aus dem Bereich "Final" können in Tests eingebunden werden.

Im Menü links erscheint ein Fachbereich an bis zu drei Orten. Die Nummern in der Abbildung gehören zu den Einträgen der folgenden Liste.

![Fachbereich Ornithologie an drei Orten im Menü: unter Mein Fragenpool, Beurteilung und Final, nummeriert 1 bis 3](assets/question_bank_review_process_areas_v1_de.png){ class="shadow lightbox" title="Bereiche eines Fachbereichs im Menü des Fragenpools · 2026.11.11" }

  * **Mein Fragenpool** (1): Hier sehen Sie den Fachbereich mit allen eigenen Fragen, aufgelistet nach Status.
  * **Beurteilung** (2): Hier erscheint derselbe Fachbereich ein zweites Mal. Aufgelistet sind die Fragen anderer Benutzer:innen mit Rechten auf diesen Fachbereich, die sich im Status "Review" befinden. Ihre eigenen Fragen erscheinen hier nicht, da Sie Ihre eigenen Fragen nicht selbst beurteilen. Ebenso fehlen die Fragen, die Sie schon bewertet haben. Hier beurteilen Sie die Fragen.
  * **Final** (3): Sobald die Beurteilungskriterien erfüllt sind, kommt die Frage in den Bereich "Final". Den Bereich "Final" sehen Personen mit der Kompetenz "Verwalten" und, je nach Einstellung des Beurteilungsprozesses, auch Personen mit der Kompetenz "Unterrichten". Fragen unter "Beurteilung" können Sie auch ohne den Bereich "Final" beurteilen.

[Zum Seitenanfang ^](#review_process)



## Status

Wenn Sie unter "Mein Fragenpool" einen Fachbereich auswählen, wird ein Prozessablauf mit verschiedenen Status abgebildet (in der Abbildung markiert). Hier bekommen Sie einen Überblick, welche Ihrer Fragen sich in welchem Status befindet.

![Markierte Statusleiste von Draft bis End of life mit der Anzahl Ihrer Fragen je Status im Fachbereich Ornithologie](assets/question_bank_review_process_status_v1_de.png){ class="shadow lightbox" title="Statusleiste eines Fachbereichs im Fragenpool · 2026.11.11" }

  * **Draft:** Alle Fragen, die noch in Bearbeitung sind und noch nicht in den Beurteilungsprozess gegeben wurden. Sobald eine Frage aus "Meine Fragen" mit dem entsprechenden Fachbereich verknüpft ist, taucht sie hier im Status Draft auf.
  * **Review:** Hier sehen Sie alle Ihre Fragen, die sich momentan gerade im Status Review befinden. Diese Fragen beurteilen andere Benutzer:innen mit Rechten auf denselben Fachbereich. Sie selbst können Ihre Fragen nicht beurteilen.
  * **Revision:** Hierhin gelangen alle Fragen, welche im Beurteilungsprozess die Untergrenze der Beurteilung nicht erreicht haben. Die Untergrenze bezieht sich auf die Bewertung durch die Sterne. Administrator:innen und berechtigte Poolverwalter:innen legen sie fest unter `Fragenpool > Administration > Beurteilungsprozess`, siehe [Fragenpool: Administration](Question_Bank_Administration.de.md#assessment_process). Die Fragen, welche sich hier befinden, müssen von Ihnen überarbeitet und wieder in die Beurteilung gegeben werden.
  * **Final:** Wenn eine Frage die Beurteilungskriterien erfüllt, gelangt sie in den Status Final. Hier sind nun die Fragen, welche die Qualitätssicherung bestanden haben und in Tests eingebunden werden können.
  * **End of life:** Hierhin kommen Fragen, die Administrator:innen, Personen mit der Kompetenz "Verwalten" im Fachbereich oder berechtigte Poolverwalter:innen in den Status End of life gesetzt haben. Nun ist es Ihnen überlassen, ob Sie die Fragen hier belassen oder löschen möchten. Wenn Sie die Frage wieder bearbeiten möchten, müssen Sie eine Kopie davon erstellen. Die Kopie befindet sich im Status Draft, und der Prozess kann von vorne beginnen.

[Zum Seitenanfang ^](#review_process)


## Fragen beurteilen {: #review_questions}

Im Bereich "Beurteilung" beurteilen Sie die Fragen anderer Benutzer:innen mit Rechten auf denselben Fachbereich. Ihre Bewertung entscheidet mit, ob die Frage in den Status "Final" wechselt oder im Status "Revision" zurück an die Autor:in geht. Die Frage befindet sich im Lesemodus. Sie können also die gesamte Frage anschauen, inklusive Punkte, Feedback und Metadaten. Sie können jedoch nichts editieren.

Die Beurteilung starten Sie mit "Frage beurteilen" in der Hinweisbox über der Frage. Administrator:innen und Personen mit der Kompetenz "Verwalten" im Fachbereich sehen rechts im Abschnitt "Bewertungen" die bisher abgegebenen Bewertungen mit Datum und Sternen.

![Markiert: Button Frage beurteilen in der Hinweisbox und rechts der Abschnitt Bewertungen mit Datum und Sternen](assets/question_bank_review_question_v1_de.png){ class="shadow lightbox" title="Zu beurteilende Frage im Bereich Beurteilung · 2026.11.11" }

Anschliessend öffnet sich der Dialog "Beurteilung":

![Dialog Beurteilung mit dem Hinweis zur einmaligen Bewertung, den Sternen, dem Kommentarfeld und den Buttons Beurteilen und Abbrechen](assets/question_bank_review_rating_dialog_v1_de.png){ class="shadow lightbox" title="Dialog zum Beurteilen einer Frage · 2026.11.11" }

Hier bewerten Sie die Frage mit den Sternen und fügen einen Kommentar hinzu. Jede Frage können Sie genau einmal bewerten. Danach erscheint sie nicht mehr in Ihrer Liste unter "Beurteilung". Vor allem wenn die Bewertung unter der Untergrenze liegt, ist ein Kommentar zentral. Ihr Kommentar erscheint unter der Frage bei den Kommentaren. So kann die Autor:in die Frage anhand Ihrer Rückmeldung verbessern. Mit "Beurteilen" speichern Sie Ihre Beurteilung.

[Zum Seitenanfang ^](#review_process)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[e-Assessment Administration: Fragenpool >](../../manual_admin/administration/eAssessment_Question_bank.de.md)<br>
[Fragenpool: Administration >](Question_Bank_Administration.de.md)<br>
[Modul Taxonomie >](../../manual_admin/administration/Modules_Taxonomy.de.md)

**Weiterführend**<br>
[Fragenpool: Fragen erstellen >](Question_Bank_Create_Questions.de.md)<br>
[Fragenpool: Fragen importieren >](Question_Bank_Import_Questions.de.md)<br>
[Fragenpool: Detailansicht einer Frage und Metadaten >](Item_Detailed_View.de.md)<br>
[Fragenpool: Fragen verwenden >](Question_bank_possible_operations.de.md)<br>
[Fragenpool: Freigabemöglichkeiten >](Question_Pool_Sharing_Options.de.md)<br>
[Wie gehe ich vor, wenn ich einen Test erstelle? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md)

[Zum Seitenanfang ^](#review_process)
