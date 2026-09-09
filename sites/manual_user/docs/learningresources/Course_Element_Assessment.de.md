# Kursbaustein "Bewertung" {: #course_element_assessment}


## Steckbrief

Name | Bewertung
---------|----------
Icon | :o_icon_o_ms_icon:
Verfügbar seit | 
Funktionsgruppe | Wissensüberprüfung
Verwendungszweck | Bewertung von Leistungen, auch wenn sie ausserhalb von OpenOlat erbracht wurden (z.B. Präsenz-Referate, praktische Arbeiten)
Bewertbar | ja
Spezialität / Hinweis |


Der Kursbaustein "Bewertung" eignet sich, um Leistungen zu bewerten, welche nicht explizit elektronisch abgegeben werden, z.B. Präsenz-Referate oder Online-Webseiten. 

## Bewertung im Kurseditor erstellen und einrichten

Die Konfiguration des Kursbausteins Bewertung erfolgt im Kurseditor im Tab "Bewertung". Hier können Sie die Bewertung so konfigurieren, dass

  * ein [Rubrik](../learningresources/Form_Element_Rubric.de.md) als Basis für die Bewertung verwendet wird,
  * Punkte vergeben werden (oder nicht),
  * Bestanden/nicht bestanden angezeigt wird,
  * ein individueller Kommentar hinzugefügt werden kann,
  * ein individuelles Dokument hinzugefügt werden kann

![Sechs Schalter der Bewertungskonfiguration, im Beispiel nur Bestanden/Nicht bestanden ausgeben und Bei Kurs-Bewertung berücksichtigen aktiviert, im Tab Bewertung des Kurseditors](assets/KB_Bewertung_Tab_Bewertung19.jpg){ class="shadow lightbox" }

Die Einstellungen haben Einfluss auf die späteren Bewertungsoptionen und den für die Teilnehmenden sichtbaren Informationen.

!!! warning "Achtung"

    Sobald eine Bewertung eines Teilnehmenden stattgefunden hat, können Sie die Konfiguration im Kurseditor nicht mehr verändern. 


## Tab "Bewertung" konfigurieren

### Rubrik-Bewertung
Eine interessante Möglichkeit der Kriterien basierten Bewertung mit Hilfe des Kursbausteins "Bewertung" bietet die [Rubrik-Bewertung](../learningresources/Forms_in_Rubric_Scoring.de.md).

Dabei wird ein OpenOlat Formular, das mindestens ein Rubrik-Element enthält, mit dem Kursbaustein Bewertung verknüpft. Anschliessend kann die durch das Rubrik-Formular generierte Punktzahl automatisch als Summe oder Durchschnitt übernommen werden. Bei der Wahl der "Summe" werden die Punkte, die pro Zeile vergeben werden, aufaddiert. Bei der Wahl "Durchschnitt" wird die Durchschnittsumme aller Rubrik-Zeilen ermittelt. Alternativ kann auch eine manuelle Punktevergabe gewählt oder ganz auf Punkte verzichtet werden.

### Punkte vergeben

Sofern aktiviert können manuell durch die Betreuer:innen und Besitzer:innen Punkte vergeben werden. Für die Punktevergabe müssen die minimalen und maximalen Punkte angegeben werden. 

Bei zusätzlicher Aktivierung der Rubrik-Bewertung können auch automatisiert Punkte aus dem Rubrik übernommen werden.   

### Bewertung mit Einstufung/Noten

Sobald "Punkte vergeben" eingeschaltet wurde, kann auch die Option "Bewertung mit Einstufung/Noten" eingeschaltet und weiter konfiguriert werden. 

Klicken sie auf "Bewertungsskala bearbeiten" um eine Skala auszuwählen und eventuell weitere Einstellungen vorzunehmen. In der Skala ist auch definiert ob bzw. ab wann eine Bewertungsskala mit einem bestanden/nicht bestanden verbunden ist. 

Anschliessend definieren Sie noch ab die Zuweisung zur gewählten Bewertungsskala manuell durch die Betreuenden oder automatisch durch die Zuordnung der erreichten Punktzahl erfolgen soll. 


### Bestanden / Nicht bestanden ausgeben

Schalten Sie die Option ein, wenn den Lernenden angezeigt werden soll, ob der Kursbaustein bestanden wurde oder nicht. 

Sofern aktiviert kann bei Lernpfadkursen im nächsten Schritt auch definiert werden ob der Kursbaustein bei der Bewertung des Kurses berücksichtigt werden soll oder nicht. Bei herkömmlichen Kursen wird dies im Tab "Punkte" des obersten Kursbausteins definiert. 

Wenn zusätzlich zu Bestanden/Nicht bestanden auch Punkte aktiviert wurden kann neben der standardmässigen manuellen Bewertung durch die Betreuer:innen noch eine automatische, punkteabhängige Bewertung aktiviert werden. 

![Punktevergabe von 0 bis 20, Bestanden/Nicht bestanden aktiviert und Ausgabe automatisch durch Punkteschwelle statt manuell durch Betreuer:in, im Tab Bewertung des Kurseditors](assets/KB_Bewertung_Punkte_bestanden19.jpg){ class="shadow lightbox" }

Auch kann das Bestehen durch die ausgewählte Bewertungsskala erfolgen. 

Sofern Punkte und/oder bestanden aktiviert wurde gibt es bei Lernpfadkursen noch eine weitere Option: **„Bei Kurs-Bewertung berücksichtigen“**.  Ist die Option aktiviert, werden die von den Teilnehmenden erreichten Punkte auf die in `Kurs > Administration > Einstellungen > Bewertung` definierten Punktschwelle, die für das Bestehendes Kurses notwendig ist, angerechnet bzw. der Kursbaustein als Teil der notwendigen Kursbausteine, die für das Bestehen des gesamten Kurses dienen, berücksichtigt. 

### Individuelle Kommentare, Dokumente und Infos

Aktivieren Sie die gewünschte Checkbox. um den Lernenden individuelle Kommentare und/oder Dokumente z.B. als Feedback bereitzustellen.

### Status "Korrigieren" setzen 
Bei aktivierter Option erscheint für die Betreuenden beim Status "Korrigieren" und für die Teilnehmenden "in Korrektur" bzw. bei nicht Auswahl "Nicht gestartet" und für die Teilnehmenden "Information nicht verfügbar". Aktivieren Sie die Option nur, wenn Sie die Info auch wirklich haben möchten. 

## Bewertung im Kursrun durchführen

Die Bewertung der Teilnehmenden wird von den Besitzer:innen oder Betreuer:innen entweder im Kursrun bei geschlossenem Kurseditor oder im [Bewertungswerkzeug](../learningresources/Assessment_tool_overview.de.md) durchgeführt. 

Im **Tab "Übersicht"** erscheint eine Gesamtübersicht zum Kursbaustein 

![Gesamtübersicht mit Teilnehmerzahl, Bestehensquote im Kreisdiagramm, Punkteverteilung im Histogramm sowie Aufschlüsselung nach Gruppe und Curriculumelement, im Tab Übersicht](assets/KB_Bewertung_Uebersicht19.png){ class="shadow lightbox" }

Im **Tab "Teilnehmer:innen"** werden alle Teilnehmenden angezeigt. Je nach Konfiguration der Spalten werden weitere Informationen wie die erreichte Punktzahl, der Status usw. für die jeweilige Person sichtbar. Ferner kann im Tab auch eine Massenbewertung erfolgen oder die Daten aller Teilnehmenden zurückgesetzt werden.

Um eine Bewertung vorzunehmen wird der/die entsprechende Teilnehmer:in ausgewählt und die angezeigten Felder ausgefüllt bzw. bei Rubrikbewertungen die Rubrik-Felder ausgefüllt. Die Bewertung kann zwischengespeichert oder direkt abgeschlossen und freigegeben werden. 

Die Teilnehmenden haben nach der Freigabe Zugriff auf ihre Bewertung inklusive Bewertungsrubrik und sonstiger Feedbacks.  

Im **"Tab Erinnerungen"** erscheinen die  für den Kursbaustein im Kurseditor angelegten [Erinnerungen](../learningresources/Course_Reminders.de.md). Auch neue Erinnerungen können hier erstellt oder vorhandene bearbeitet und gelöscht werden. 


### Tab Badges
Wurde von dem/der Kursbesitzer:in unter [`Kurs > Administration > Einstellungen > Bewertung > Badges`](../learningresources/Course_Settings_Assessment.de.md#section_badges) die Vergabe von Badges aktiviert, wird im Kurseditor zu diesem Kursbaustein der Tab "Badges" angezeigt und es kann ein spezifischer Badge für diesen Kursbaustein erstellt werden.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Rubrik](../learningresources/Form_Element_Rubric.de.md)<br>
[Rubrik-Formular](../learningresources/Forms_in_Rubric_Scoring.de.md)<br>
[Bewertungswerkzeug](../learningresources/Assessment_tool_overview.de.md)<br>
[Erinnerungen](../learningresources/Course_Reminders.de.md)<br>
[Kurseinstellungen - Tab Bewertung](../learningresources/Course_Settings_Assessment.de.md)

**Weiterführend**<br>
[Einstufung/Noten](../learningresources/Assessment_translate_points_in_grades.de.md)<br>
[Das Bewertungsformular](../learningresources/The_assessment_form.de.md)

[Zum Seitenanfang ^](#course_element_assessment)
