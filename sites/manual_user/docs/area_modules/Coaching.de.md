# Coaching - Übersicht {: #coaching}

## Wozu dient das Coaching Tool? {: #purpose}

Das Coaching Tool dient der **kursübergreifenden** Organisation und Verwaltung von Kursen, Teilnehmenden und Gruppen, sowie der **kursübergreifenden** Korrektur von Assessmentbausteinen, dem **kursübergreifenden** Absenzenmanagement und dem externen Korrektoren-Flow von OpenOlat Tests.

Mit dem Coaching-Tool haben Kursbesitzer:innen, Kursbetreuer:innen, Gruppenbetreuer:innen, Ausbildungsverantwortliche und andere Berechtigte die Möglichkeit, alle ihnen zugewiesenen Kurs- oder Gruppenteilnehmenden auf einen Blick zu sehen und zu verwalten. Sie gelangen von diesen Übersichten dann schnell auf unterschiedlichen Wegen zum Bewertungswerkzeug für einzelne Teilnehmende.

---


## Die Werkzeuge [:octicons-tag-16:{ title="ab Release 20.0 (OO-8374)" }](https://track.frentix.com/issue/OO-8374) {: #tools}

Den Zugang zu den Daten der betreuten Personen und die Werkzeuge finden Sie unter den Buttons

* Personen
* Kurse
* Gruppen
* Termine / Absenzen
* Bewertungsaufträge
* Reports
* Auftragsverwaltung

![coaching_tools_v1_de.png](assets/coaching_tools_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Ihr Menü wird oft nicht alle hier gezeigten Optionen enthalten. Je nach aktivierten Modulen und Rollen wird eine andere Zusammensetzung angezeigt. Hier im Handbuch soll zur Erklärung die maximale Auswahl gezeigt werden.

[Zum Seitenanfang ^](#coaching)

---

## Wann ist das Coaching Tool verfügbar? {: #availability}

Die Menüoption "Coaching" wird grundsätzlich nur angezeigt, wenn das Coaching in der OpenOlat Administration auch aktiviert wurde.

Ob das Coaching Tool im Hauptmenü für Sie angezeigt wird, hängt dann von weiteren Faktoren ab:

* **Systemrolle**: Gäste und Externe können kein Coaching vornehmen.
* Die **Kursrolle** muss Betreuer:in oder Besitzer:in sein. Teilnehmende können kein Coaching vornehmen. 
* Der **Kursstatus** muss "Veröffentlicht", "Freigabe an Betreuer:innen" oder "Beendet" sein.
* Ob es **Teilnehmende** (mind. 1 Person) in einem Kurs bzw. einer Gruppe hat.


[Zum Seitenanfang ^](#coaching)

---


## Wer verwendet das Coaching Tool typischerweise? {: #users}

Das Coaching Tool wird verwendet von

* Betreuer:innen, die Teilnehmende mehrerer Kurse betreuen
* Ausbildungsverantwortlichen
* Linienvorgesetzten
* Personen mit definierten Person-zu-Person-Beziehungen, z.B. Mentor - Mentee

Daneben haben auch administrative Rollen Zugriff.

[Zum Seitenanfang ^](#coaching)

---


## Die Fokus-Elemente [:octicons-tag-16:{ title="ab Release 20.0 (OO-8374)" }](https://track.frentix.com/issue/OO-8374) {: #focus_elements}

Im Coaching Tool wird Ihnen oft eine Liste mit den von Ihnen betreuten Personen angezeigt.
Sind Sie z.B. nur in einem Kurs direkt Betreuer:in, aber daneben Ausbildungsverantwortliche:r, dann können Sie auf Grund dieser Rolle auch auf alle anderen Teilnehmenden zugreifen.

Mit den Fokus-Elementen über der Liste können Sie eine Ihrer Rollen wählen. Damit erhalten Sie eine Vorauswahl. In der Liste befinden sich dann nur noch von Ihnen betreute Personen, die Sie in dieser Rolle betreuen.

![coaching_focus_elements_v1_de.png](assets/coaching_focus_elements_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#coaching)

---

#### Übersicht [:octicons-tag-16:{ title="ab Release 20.3 (OO-9305)" }](https://track.frentix.com/issue/OO-9305) {: #widget_overview}

Ein Trennbereich mit der Bezeichnung **"Übersicht"** grenzt den nachfolgend beschriebenen Widget-Bereich optisch von den darüberliegenden Buttons/Launchern ab.
![coaching_overview_v1_de.png](assets/coaching_overview_v1_de.png){ class="shadow lightbox" }

#### Das Kurs-Widget [:octicons-tag-16:{ title="ab Release 20.3 (OO-9195)" }](https://track.frentix.com/issue/OO-9195) {: #widget_courses}

Das Widget **Kurse - Als Betreuer:in** zeigt die von Ihnen betreuten Kurse.

Über den definierten Filter **"Relevant"** (standardmässig ausgewählt) oder eine der weiteren Filtervarianten erhalten Sie eine entsprechende Vorauswahl:

* **Favoriten** (standardmässig ausgewählt)
* **Alle** (nicht standardmässig ausgewählt)
* **Relevant** (standardmässig ausgewählt, Hauptkennzahl)
* **Veröffentlicht** (standardmässig ausgewählt)
* **Freigabe Betreuer:innen** (standardmässig ausgewählt)
* **Beendet** (nicht standardmässig ausgewählt)

[Zum Seitenanfang ^](#coaching)

---

#### Das Termine-Widget {: #widget_events}

Das Widget **Termine** erscheint als Kachel auf der Coaching-Übersicht und zeigt die anstehenden Termine ab dem heutigen Tag bis zum Ende der aktuellen Woche auf einen Blick.

#### Kopfbereich und Tagesanzeige

Der Kopfbereich des Widgets zeigt das aktuelle Datum mit Monat, Jahr und der Beschriftung **Heute, \<Wochentag\>**. Der heutige Tag ist hervorgehoben. Das Wochenende wird optisch zurückgenommen (gedämpft dargestellt).

#### Wochennavigation

Mit den Schaltflächen `<` und `>` navigieren Sie wochenweise durch die Termine. Eine Woche läuft immer von Montag bis Sonntag. Initial wird die aktuelle Woche ab dem heutigen Tag angezeigt.

#### Terminliste

Pro Termin werden folgende Informationen angezeigt:

- Wochentag und Datum
- Status-Indikator
- Externe Referenz und Titel
- Ort (mit Ortssymbol)
- Zeit und Dauer (mit Uhrsymbol)

!!! note "Hinweis"
    In der schmalen (mobilen) Ansicht entfällt die Ortsspalte. Es wird nur die Uhrzeit angezeigt.

![coaching_widget_events_v1.de.png](assets/coaching_widget_events_v1.de.png){ class="shadow lightbox" }

#### Leerer Zustand

Sind in der angezeigten Woche keine Termine vorhanden, erscheint der Hinweis **Keine Termine bis Ende der Woche**. Über die Schaltflächen **Vorheriger Termin** und **Nächster Termin** springen Sie zum nächstgelegenen Termin in der Vergangenheit oder Zukunft.

!!! note "Hinweis"
    Gibt es für diesen Coach überhaupt keine Termine, wird das Widget komplett ausgeblendet.

#### Zur Vollansicht

Über den Link **Alle Termine anzeigen** gelangen Sie in das Werkzeug **Termine / Absenzen**.

!!! tip "Wichtig"
    Das Widget ist eine Schnellübersicht der aktuellen Woche. Das vollständige Werkzeug **Termine / Absenzen** bietet zusätzlich die Tabs Cockpit, Absenzen, Meldungen, Rekurse und Personensuche.

[Zum Seitenanfang ^](#coaching)

---

## Weiterführende Informationen {: #further_information}

[Coaching: Personensuche >](../area_modules/Coaching_User_Search.de.md)<br>
[Coaching: Personen >](../area_modules/Coaching_People.de.md)<br>
[Coaching: Kurse >](../area_modules/Coaching_Courses.de.md)<br>
[Coaching: Bildungsprodukte >](../../manual_user/area_modules/Coaching_Educational_Products.de.md)<br>
[Coaching: Termine / Absenzen >](../area_modules/Coaching_Events_Absences.de.md)<br>
[Coaching: Bewertungsaufträge >](../area_modules/Coaching_Assessment_Orders.de.md)<br>
[Coaching: Reports >](../area_modules/Coaching_Reports.de.md)<br>
[Coaching: Gruppen >](../area_modules/Coaching_Groups.de.md)<br>
[Coaching: Auftragsverwaltung >](../area_modules/Coaching_Order_Management.de.md)

[Zum Seitenanfang ^](#coaching)
