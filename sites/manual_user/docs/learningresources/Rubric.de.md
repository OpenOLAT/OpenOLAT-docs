# Rubrik

Ein Rubrik ist in OpenOlat ein Element der Lernressource "Formular". Rubriks bieten sich an, wenn Sie mehrere Fragen für die gleiche Bewertungsskala verwenden wollen. Der Anwendungsbereich von Rubrik Bewertungen ist gross. Generell können Rubrik Elemente in allen Formularen und für sämtliche Kursbausteine und Lernressourcen, die Formulare nutzen, verwendet werden. Konkret sind das:

* [Kursbaustein Umfrage](Forms_in_Questionnaires.de.md)
* [Kursbaustein Formular](Forms_in_Forms_Element.de.md)
* [Kursbaustein Bewertung](Forms_in_Rubric_Scoring.de.md)
* [Kursbaustein Aufgabe mit Peer-Review](Course_Element_Task.de.md#revisions)
* [Portfolio 2.0 Vorlage](Forms_in_the_ePortfolio_template.de.md)

## Einsatzbeispiele für Rubriks

In OpenOlat können Rubriks z.B. eingesetzt werden um

* den Zustimmungsgrad zu einer Fragestellung abzufragen

  ![Rubrik Beispiel Radiobutton1](assets/Rubrik_Beispiel1.jpg){ class="shadow lightbox" }

<br>

* Ausprägungen zwischen zwei extremen Skalen abzufragen

  ![Rubrik Beispiel Slider](assets/Rubrik_Beispiel2.jpg){ class="shadow lightbox" }

<br>

* Bewertungsraster für Lernenden-Aktionen zu erstellen

  ![Rubrik Beispiel Radiobutton2](assets/Rubrik_Beispiel3.jpg){ class="shadow lightbox" }

<br>

* eine Selbsteinschätzung z.B. Stärken und Schwächen vornehmen zu lassen

  ![Rubrik Beispiel Selbseinschätzung](assets/Rubrik_Beispiel4.jpg){ class="shadow lightbox" }

<br>

* Kriterien bezogene Punkte zu vergeben

  ![Rubrik Feedback](assets/rubrik_skalentexte.jpg){ class="shadow lightbox" }

<br>

* in einem Peer-Review die anderen Teilnehmer:innen zu bewerten und/oder eine Bewertung durch Betreuer:innen vorzunehmen

  ![Rubrik Peer-Review](assets/Rubrik_Peer-Review.png){ class="shadow lightbox" }

<br>

Rubriks können über "Inhalt hinzufügen" einem OpenOlat Formular hinzugefügt und anschliessend konfiguriert werden.

## Rubrik Konfiguration im Formular Editor

![Rubrik Editor](assets/formular_rubik17a.png){ class="shadow lightbox" }

Ein Rubrik besteht immer aus Zeilen und Spalten die sinnvoll beschriftet und definiert werden müssen. 

Geben Sie im Bereich "Spaltenbeschriftung" für jede Spalte eine sinnvolle _Bewertungsskala_ ein z.B. sehr gut, gut mittel, schlecht, sehr schlecht. Jede Spalte ist immer mit einem bestimmten Wert verbunden, der in den erweiterten Einstellungen des Rubrik Inspektors konkreter spezifiziert werden kann.
  
Geben Sie im Bereich der Zeilen einzelne (Bewertungs-)Kriterien, Statements oder Fragestellungen ein. Weitere Zeilen werden über "Frage hinzufügen" ergänzt. Sie können die kurzen Statements auch formatieren. Einzelne Zeilen können mit Hilfe der oben/unten Doppelpfeile verschoben werden. Zusätzlich können Sie jede Zeile mit einer Gewichtung  versehen und so einzelne Kriterien besondere Bedeutung zuweisen, was sich auch bei der Punktevergabe widerspiegelt, z.B. durch doppelte oder dreifache Punkte. 
Ferner ist es möglich den Wert auf 0 zu setzen um einzelne Fragen aus den Reports auszuschliessen. 
 
Ein bearbeitetes Rubrik kann eingebunden in einen Kurs automatisch eine entsprechende Punktzahl erhalten, was besonders bei der Verwendung im Kursbaustein "[Bewertung](../learningresources/Course_Element_Assessment.de.md)" relevant ist. 
 
Über den Quer-Doppelpfeil kann ein Rubrik mit zwei Enden erstellt werden. 

![Rubrik Skalenbereich](assets/Rubrik_2_enden.jpg){ class="shadow lightbox" }


!!! info "Hinweis"

    Wird ein Rubrik in einem Kursbaustein Bewertung eingebunden kann die Gewichtung nicht mehr geändert werden.

### Rubrik Inspektor

![Rubrik Varianten](assets/Rubrik_Inspektor.png){ class="shadow lightbox" }

Im Tab **"Generell"** wird der Rubrik-Typ festgelegt. Es werden drei verschiedene Typen bzw. Darstellungsvarianten von Rubriks unterschieden. Die Anzahl der Schritte definiert die Anzahl der Rubrik-Spalten. 2-10 Spalten sind möglich. 

Wird "Beschreibung der Kriterien" aktiviert :octicons-tag-24: Release 18.1  kann jede Zelle der Rubrik-Tabelle mit kurzen Beschreibungstexten versehen werden, so dass die Kriterien basierte Bewertung noch deutlicher wird. 

![Rubric Zellentext](assets/Rubric_zellentext.png){ class="shadow lightbox" }

Ferner kann die Option "keine Antwort möglich" aktiviert und definiert werden ob die Bearbeitung des Rubriks freiwillig oder obligatorisch ist. 

Wenn Sie den Tab **"Erweitert"** aktivieren stehen Ihnen folgende zusätzliche Optionen zur Verfügung:

![Erweitertes Rubrik Einstellungen](assets/Rubric_erweitert.png){ class="shadow lightbox" }

Sie können dem Rubrik einen Namen geben, was Ihnen später die Zuordnung bei der Auswertung erleichtert. Zusätzlich kann der Name bei Bedarf auch direkt im Fragebogen angezeigt werden.

Unter Skalentyp können Sie die Art der verwendeten Likert –Skala näher bestimmen und somit auch den Wertebereich definieren: Legen Sie fest an welchem Ende der Skala sich die positive Bewertung befindet und definieren Sie bei Bedarf die Bereiche für ungenügend, neutral und gut. Diese Information wird in der Auswertung berücksichtigt.

!!! info "Info"

    Der Rubrik-Inspektor kann frei im Formularbereich positioniert und verschoben werden.


## Weitere Informationen

[Formular als Rubrik Bewertung](Forms_in_Rubric_Scoring.de.md)


