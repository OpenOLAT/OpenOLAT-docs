# Einstufung/Noten {: #rating_grades}

:octicons-tag-24: Release 16.2

Sofern ein Assessment-Kursbaustein, wie beispielsweise ein Test, eine Aufgabe usw. mit Punkten versehen werden, können die Punkte auch in Noten übersetzt werden. 

Kursbesitzer:innen können die Funktion im Kurseditor aktivieren und dort konfigurieren. 


## Konfigurieren eines Kursbausteins für Einstufungen und Noten

!!! info "Voraussetzung"

    Das Modul Einstufung/Noten wurde von den OpenOlat Administrator:innen aktiviert und es wurde mindestens ein Bewertungssystem angelegt.

1. **Einstufung/Noten für einen Kursbaustein aktivieren**<br> 
Gehen Sie in den Kurseditor und wählen Sie den Kursbaustein, für den die Einstufung aktiviert werden soll. Im Tab "Bewertung" können Sie die Einzelheiten einrichten. 
(Bei Tests im Tab "Testkonfiguration".) Achten Sie darauf, dass auch "Punkte vergeben" aktiviert ist und aktivieren Sie "Bewertung mit Einstufung/Noten". 
2. **Zuweisung wählen**<br>
Sie können zwischen manueller und automatischer Zuweisung wählen. Bei manueller Zuweisung muss der/die Betreuer:in die Zuordnung manuell auslösen und für die Benutzer:innen sichtbar machen. 

3. **Bewertungsskala auswählen und anpassen**<br>
Definieren Sie die minimalen und maximalen Punkte (speichern) und klicken Sie auf "Bewertungsskala bearbeiten". Es öffnet sich ein Einstellungsfenster. Hier können Sie ein Bewertungssystem auswählen und die Bewertungsskala weiter anpassen.

    ![Bewertungsskala](assets/ratingscale_de.png){class="shadow"}

4. **Speichern**

[Zum Seitenanfang ^](#rating_grades)

---

## Grenzwerte der Bewertungsskala lesen {: #grade_boundaries}

In der Bewertungsskala wird jeder Note bzw. Stufe ein Punktebereich mit einem "von"- und einem "bis"-Wert zugeordnet. In der Spalte "Punkte" wird dieser Bereich angezeigt, in der Spalte "Note" die zugehörige Note.

Bei automatisch berechneten Skalen kann der "bis"-Wert einer Stufe mit dem "von"-Wert der nächsthöheren Stufe übereinstimmen. Ein und derselbe Punktewert erscheint dann in zwei aufeinanderfolgenden Zeilen. In diesem Fall gilt:

!!! info "So wird der Grenzwert gelesen"

    Der Grenzwert gehört immer zur höheren Stufe. Der "von"-Wert einer Stufe ist also eingeschlossen, der "bis"-Wert ausgeschlossen (der "bis"-Wert zählt bereits zur nächsthöheren Stufe).

**Beispiel** (Schweizer Notensystem, erreichbare Punkte 0 bis 5):

| Punkte | Note |
| ------ | ---- |
| 3.25 bis 3.75 | 4.5 |
| 3.75 bis 4.25 | 5 |

Ein Ergebnis von genau 3.75 Punkten ergibt die Note 5 und nicht die Note 4.5, weil der Grenzwert zur höheren Stufe zählt. Ein Ergebnis von 3.74 Punkten ergibt dagegen die Note 4.5.

[Zum Seitenanfang ^](#rating_grades)

---

## Noten im Bewertungswerkzeug

Die Einstufungs- und Notenskala spiegelt sich auch im Bewertungswerkzeug wider. 

* **Tab "Übersicht" eines Kursbausteins**:<br>
Die Kennzahlen für die Bewertung wurden um Noten erweitert. Man sieht die Normalverteilung und wichtige Einstellungen.

* **Tab "Teilnehmer:innen" eines Kursbausteins**:<br>
Im Bewertungswerkzeug sieht man die Noten in einer separaten Spalte hinter der Punktzahl. (Sofern die Spalte angezeigt wird. -> Zahnrad-Button) Man kann, wenn auf manuell gestellt, hier auch Noten manuell übernehmen.

Um die Bewertungsskala nachträglich anzupassen oder um neue Noten zu vergeben, klicken Sie oben auf den Button "Bewertungsskala anpassen". 

[Zum Seitenanfang ^](#rating_grades)