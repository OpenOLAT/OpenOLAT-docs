# Formulare - Übersicht {: #overview}

Mit einem Formular sammeln Sie in OpenOlat Angaben, Meinungen und Bewertungen, zum Beispiel:

* als klassische Formulare (mit Auswahlfeldern oder Freitexteingaben)
* für Online-Umfragen
* als Rubrik-Bewertung, die Leistungen nach festen Kriterien in Stufen bewertet
* zur Selbsteinschätzung
* oder beim Buchen von Angeboten im Course Planner

## Steckbrief

Name | Formular
---------|----------
Icon | :o_icon_o_FileResource-FORM_icon:
Verfügbar seit | Release 11.2 (OO-2329)
Zweck | Angaben, Meinungen und Bewertungen sammeln
Im Kurs | Kursbausteine "Formular" und "Umfrage", als Rubrik auch in "Bewertung" und "Aufgabe"

## Aufbau und Einsatz {: #structure}

Ein Formular ist in OpenOlat eine eigene Lernressource, also ein Inhaltsobjekt, das Sie im Autorenbereich verwalten und an verschiedenen Orten einsetzen. Als Autor:in legen Sie es im Autorenbereich an: `Autorenbereich > Erstellen > Formular`. Wer ein Formular anlegt, ist Besitzer:in der Formular-Lernressource. Bearbeiten können es Besitzer:innen, Lernressourcenverwalter:innen und Administrator:innen.

Den [Formulareditor](../Form_Editor/index.de.md) öffnen Sie in der Formular-Lernressource selbst, im Menü "Administration" mit dem Eintrag "Formulareditor": `Formular > Administration > Formulareditor`. Elemente fügen Sie also direkt in der Lernressource ein, ein Kurs ist dafür nicht nötig. Zur Lernressource gelangen Sie im Autorenbereich mit einem Klick auf ihren Titel oder aus einem Kurs, in dem ein Kursbaustein das Formular einbindet. Im Kurs öffnen Sie dazu den Kurseditor: `Kurs > Administration > Kurseditor`. Dort wählen Sie den Kursbaustein aus, der das Formular einbindet. Im Tab "Formular" des Kursbausteins "Formular" klicken Sie auf "Lernressource bearbeiten", beim Kursbaustein "Umfrage" im Tab "Umfrage". Der Button öffnet die Formular-Lernressource.

Im Editor bauen Sie das Formular aus Layouts auf, die Spalten und Zeilen der Seite festlegen. In die Layouts fügen Sie [Elemente](../Form_Elements/index.de.md) ein, etwa Texte und Fragen. Mit [Frageregeln](../Form_Question_Rules.de.md) legen Sie fest, dass ein Bereich des Formulars erst erscheint, wenn die ausfüllende Person eine bestimmte Antwort gewählt hat.

!!! info "Wichtig"

    Es gibt eine Lernressource "Formular" und einen Kursbaustein "Formular". Die Lernressource enthält das Formular selbst, der Kursbaustein bindet es in einen Kurs ein. Wie beide zusammenspielen, erklärt die Anleitung [Wie erstelle ich eine Formular-Lernressource?](../../../manual_how-to/create_a_form/create_a_form.de.md#step2) im Abschnitt "Kursbaustein und Lernressource".

Antworten sammelt ein Formular dort, wo Sie es einsetzen: in einem Kurs, in einer Portfolio 2.0 Vorlage oder beim Buchen im Course Planner (siehe [Einsatzorte](#usage)). Beim Buchen im Course Planner holt das Formular die Angaben direkt beim Buchen eines Angebots ein, ganz ohne Kurs. Öffnen Sie die Formular-Lernressource direkt, etwa mit einem Klick auf ihren Titel im Autorenbereich, sehen Sie das Formular und können es zum Ausprobieren ausfüllen. Ihre Antworten speichert OpenOlat dort nicht, und einreichen lässt sich das Formular nicht. Wer Antworten sammeln will, setzt das Formular an einem der Einsatzorte ein, meist in einem Kurs, siehe [Formulare in Kursen](../Forms_in_Courses.de.md).

## Seiten zur Formular-Lernressource {: #pages}

Diese Seiten beschreiben die Formular-Lernressource selbst, in der Reihenfolge der Navigation:

Thema | Wozu
---------|----------
[Formulareditor](../Form_Editor/index.de.md) | Wie Sie den Editor öffnen, auch aus einem Kursbaustein, und wie Sie ein Formular aus Layouts und Elementen aufbauen.
[Elemente](../Form_Elements/index.de.md) | Alle Inhaltselemente und Fragetypen, die Sie in ein Layout einfügen, mit ihren Einstellungen.
[Rubrik](../Form_Element_Rubric.de.md) | Mehrere Fragen auf derselben Bewertungsskala beantworten oder bewerten lassen.
[Frageregeln](../Form_Question_Rules.de.md) | Einen Bereich des Formulars nur anzeigen, wenn er zur gewählten Antwort passt.
[In Kursen](../Forms_in_Courses.de.md) | Mit welchen Kursbausteinen ein Formular in einem Kurs Antworten sammelt.

## Einsatzorte {: #usage}

An diesen Orten setzen Sie ein Formular ein. Beschrieben sind sie im Handbuch bei ihrem jeweiligen Thema:

Einsatzort | Wozu
---------|----------
[Kursbaustein "Formular"](../Course_Element_Form.de.md) | Teilnehmende füllen ein Formular standardmässig einmal aus, etwa als Bestätigung vor einem Laborpraktikum; OpenOlat ordnet die Antworten ihrem Namen zu.
[Kursbaustein "Umfrage"](../Course_Element_Survey.de.md) | Die Mitglieder eines Kurses beantworten einen Online-Fragebogen, etwa zur Zufriedenheit; die Resultate speichert OpenOlat anonymisiert.
[Rubrik-Bewertung](../Forms_in_Rubric_Scoring.de.md) | Betreuer:innen und Kursbesitzer:innen bewerten im Kursbaustein "Bewertung" Leistungen nach festen Kriterien mit einer Rubrik.
[Peer-Review in der Aufgabe](../Course_Element_Task/Task_Peer_Review.de.md#peer_review_rubric) | Teilnehmende einer Aufgabe beurteilen ihre Abgaben gegenseitig mit einem Rubrik-Formular.
[Portfolio 2.0 Vorlage](../Forms_in_the_ePortfolio_template.de.md) | Teilnehmende reflektieren in einer Aufgabe der Vorlage ihre Arbeit oder schätzen ihre Leistung ein.
[Buchungsaufträge im Course Planner](../../area_modules/Course_Planner_Implementations.de.md#booking_order_forms) [:octicons-tag-16:{ title="ab Release 21.1 (OO-9724)" }](https://track.frentix.com/issue/OO-9724){:target="_blank"} | Beim Buchen eines Angebots holt ein Formular zusätzliche Angaben ein, etwa Essenswünsche oder Vorkenntnisse.


## Weiterführende Informationen {: #further_information}

[Kursbaustein "Bewertung" >](../Course_Element_Assessment.de.md)<br>
[Kursbaustein "Aufgabe" >](../Course_Element_Task/index.de.md)<br>
[Kursbaustein "Gruppenaufgabe" >](../Course_Element_Grouptask.de.md)

[Zum Seitenanfang ^](#overview)
