# Wie führe ich ein Peer-Review durch? {: #peer_review} 

??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie haben bereits einen Kurs mit einem Kursbaustein "Aufgabe" erstellt?<br>
    Sie möchten die Ergebnisse dieser Aufgabe von den Kursteilnehmer:innen gegenseitig reviewen lassen?<br> 
    Die folgende Anleitung zeigt Ihnen, wie Sie dazu vorgehen.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [ ] Anfänger:innen [x] Fortgeschrittene  [ ] Expert:innen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    * [Erste Erfahrung mit dem Kursbaustein "Aufgabe"](../../manual_user/learningresources/Course_Element_Task.de.md)


---

## Wie bereite ich ein Peer-Review vor? {: #prepare_peer_review} 

Bei einem Peer-Review sollen Kursteilnehmer:innen gegenseitig abgegebene Aufgabenergebnisse reviewen. Dies kann mit Hilfe eines **Formulars** im Kursbaustein "**Aufgabe**" vorbereitet werden. 

1. Fügen Sie im Kurseditor einen **Kursbaustein "Aufgabe"** in Ihren Kurs ein.

2. Editieren Sie den Kursbaustein und wählen Sie den **Tab "Workflow"**.

3. Ein Schritt im Workflow des Kursbausteins "Aufgabe" ist der **Schritt "Feedback"**. Aktivieren Sie diesen Schritt für die Aufgabe.
![Schalter Feedback eingeschaltet, als Art Mit Peer-Review gewählt, darunter Datum und Uhrzeit für den Peer-Review-Zeitraum](assets/course_element_task_workflow_activate_fb_v1_de.png){ class="shadow lightbox" title="Tab Workflow im Kursbaustein Aufgabe" }

4. Wählen Sie unter **Art** die Option **"Mit Peer-Review"**. 

5. Bestimmen Sie den **Peer-Review-Zeitraum**, in dem das Peer-Review durchgeführt werden muss.

6. Wurde im Tab Workflow die Option "Mit Peer-Review" gewählt, können nun im **Tab "Rückgabe und Feedback"** die Regeln für die Abgabe eines Feedbacks durch andere Teilnehmer:innen festgelegt werden. 
![Gewähltes Formular für das Peer-Review, darunter Beziehung, Review-Form, Zuweisung, Anzahl Reviews und Qualitäts-Feedback](assets/course_element_task_fb_v1_de.png){ class="shadow lightbox" title="Tab Rückgabe und Feedback im Kursbaustein Aufgabe" }

7. Das Feedback der Reviewer:innen wird jeweils in einem **Formular** gegeben. Als Kursbesitzer:in geben Sie dieses Formular vor. Wählen Sie ein bereits vorhandenes oder erstellen Sie ein neues Formular, mit dem die Kursteilnehmer:innen den Review vornehmen können. Für den Anfang wird ein Formular mit nur einer Rubrik-Frage empfohlen.

8. Beziehung<br>
Mit dem Kontrollkästchen **"Gegenseitige Beurteilung"** legen Sie fest, ob Teilnehmer:innen sich gegenseitig reviewen sollen oder nicht.

9. Review-Form<br>
    * **Doppelblind-Review**: alle Namen sind anonym (ausgenommen Betreuende)
    * **Einfachblind-Review**: Der Name der Reviewer:in ist anonym.
    * **Offenes Review**: Alle Namen sind ersichtlich.

10. Zuweisung<br>
    * **Dieselbe Aufgabenstellung**: Die Reviewer:innen erhalten Review-Objekte mit derselben Aufgabenstellung wie sie selbst.
    * **Andere Aufgabenstellung**: Die Reviewer:innen erhalten Review-Objekte mit der gleichen Aufgabenstellung, aber nicht wie die eigene.
    * **Zufällige Aufgabe**: Die Reviewer:innen erhalten zufällige Review-Objekte.

11. Anzahl Reviews<br>
Die Teilnehmer:innen des Kurses erhalten einen Reviewauftrag für eine bestimmte Anzahl anderer Teilnehmer:innen (nicht für *alle* anderen Teilnehmer:innen). Diese Anzahl wird hier vorgegeben: 1 bis 5 Reviews, voreingestellt sind 3.

12. Qualitäts-Feedback für Reviewer:in<br>
Auch eine Rückmeldung an die Reviewer:innen kann ermöglicht werden. Ist der Schalter eingeschaltet, wählen Sie unter **"Form des Feedbacks"** zwischen "Hilfreich - Ja/Nein" und "Sterne Bewertung".

13. Berechtigungen<br>
Den Button "Review-Zuweisung auslösen" im Tab "Workflow" sehen standardmässig nur Kursbesitzer:innen. Aktivieren Sie unter **"Auslösung automatische Review-Zuweisung"** die Option "Betreuer:innen", wenn auch Betreuer:innen die Review-Zuweisung auslösen dürfen.

<br>

---

### Empfohlener Musterprozess

Als Standard empfehlen wir:

- Führen Sie das Peer-Review mit einem **klar definierten Zeitraum** durch.
- Verwenden Sie ein **Formular**, das nur eine **Rubrik-Frage** als Pflicht-Rubrik enthält. Die Option "Keine Antwort möglich" sollte deaktiviert sein. 
- Lassen Sie die Bewertung durch Teilnehmer:innen erfolgen. (Das heisst, die Punkte werden von den Teilnehmer:innen vergeben.)



### Variante 1: Ohne Bewertung durch Kursteilnehmer:innen

Soll das Peer-Review der Teilnehmer:innen **nicht** in die Bewertung einfliessen, sondern nur ein allgemeines Feedback abgegeben werden, zählt nur die Bewertung der Expert:in. Für eine Bewertung ausschliesslich durch die Expert:in gehen Sie folgendermassen vor:

* Erstellen und konfigurieren Sie den Kursbaustein Aufgabe, wie oben beschrieben.
* Verwenden Sie für den Peer-Review z.B. ein Formular, das nur ein Textfeld für ein allgemeines Feedback der Reviewer:innen ermöglicht. 
* Lassen Sie im **Tab "Workflow"** die Einstellung "Mit Peer-Review" selektiert. Wenn Sie hier umstellen auf "Durch Betreuende", würde der Peer-Review-Prozess insgesamt deaktiviert. Auch eine allgemeine Rückmeldung ohne Punktebewertung würde damit deaktiviert.
* Die Bewertung nur durch Expert:innen (Betreuer:innen) konfigurieren Sie im **Tab "Bewertung"**. Wenn Sie unter "Bestanden/Nicht bestanden ausgeben" die Art "Manuell durch Betreuer:in" wählen, ist nicht zwingend eine Punktevergabe erforderlich. Stattdessen kann für die Betreuer:innen auch die "Rubrik-Bewertung" eingeschaltet werden.

Ein Setting dieser Art kann z.B. verwendet werden, wenn die Reviews der Teilnehmer:innen den Expert:innen als Input dienen sollen, die Bewertung aber ausschliesslich bei den Expert:innen/Betreuer:innen bleiben soll.


### Variante 2: Gegenseitige Bewertung in Selbstlerngruppen

Ist es Ihr Ziel, weitgehend selbstständig arbeitende Lerngruppen ohne grossen Betreuungsaufwand zu haben, sollte auch das Peer-Review entsprechend organisiert sein.

* Erstellen und konfigurieren Sie den Kursbaustein Aufgabe, wie oben beschrieben.
* Schalten Sie im Tab "Bewertung" "Punkte vergeben" ein.
* Wählen Sie im Tab "Bewertung" unter "Bestanden/Nicht bestanden ausgeben" die Art "Automatisch durch Punkteschwelle".
* Wurde die Punktevergabe aktiviert, werden im Tab "Bewertung" die möglichen Quellen für die Punkteberechnung sichtbar.<br>
Unter "Gesamtpunkte aus" stehen zur Auswahl:<br>
\- Rubrik-Bewertung<br>
\- Rubrik-Peer-Review<br>
\- Abgegebene Reviews


### Variante 3: Gemeinsame Bewertung durch Teilnehmer:innen und Expert:innen

Sie können auch ein Setting einrichten, bei dem Teilnehmer:innen und Expert:innen gemeinsam bewerten.
Zum Beispiel könnte eine Gewichtung vorgenommen werden bei der die Reviews der Teilnehmer:innen einfach zählen und die Reviews der Expert:innen doppelt. 


!!! tip "Empfehlung für Selbstlerngruppen"

    Aktivieren Sie unter "Gesamtpunkte aus" die Option "Abgegebene Reviews". Es erhöht die Wahrscheinlichkeit, dass in Selbstlerngruppen gegenseitige Reviews gemacht werden, wenn die Reviewer:innen pro gemachtem Review eine fixe Punktzahl erhalten. Wenn es nur darum geht, ob ein Review abgegeben wurde, entfallen ausserdem viele ergebnisverzerrende soziale Prozesse in der Gruppe.


!!! tip "Allgemeine Empfehlungen"

    Der Kursbaustein Aufgabe und das Peer-Review können in vielen, auch ungewöhnlichen Varianten konfiguriert werden. Insbesondere für Anfänger:innen gibt es deshalb ein paar Stolpersteine.

    * Vermeiden Sie Peer-Reviews ohne Zeitangabe.
    * Vermeiden Sie Peer-Reviews mit relativen Datumsangaben.
    * Zu beachten bei Peer-Review mit Gruppen und Gruppenbetreuer:innen:<br>
     Kursbetreuer:innen sehen nur Teilnehmer:innen der eigenen Gruppe. So kann es vorkommen, dass Kursbetreuer:innen zwar Punktevergaben sehen, aber nicht zuordnen können, woher sie kommen.


<br>

---

## Wie betreue ich ein Peer-Review? {: #coach_peer_review} 

Wurde das Peer-Review von der Kursbesitzer:in vorbereitet, können Sie als Betreuer:in im Kursmenü einfach auf den entsprechenden Kursbaustein mit der Aufgabe klicken. Sie erhalten als Betreuer:in dann eine andere Ansicht als die Teilnehmer:innen. 

Im Tab "Workflow" erhalten Sie im Schritt "Peer-Review" eine Übersicht über alle getätigten Peer-Reviews Ihrer Kursteilnehmer:innen. Der Bereich "Konfiguration" fasst die Einstellungen zusammen, die aufklappbaren Listen "Vergebene Beurteilungen" und "Erhaltene Beurteilungen" zeigen je Person die Reviews mit ihrem Status.

![Schritt Peer-Review mit der Konfiguration aus Anzahl Reviews, Zuweisung und Review-Form, darunter die aufklappbaren Listen der Beurteilungen](assets/peer_review_coach_workflow_v1_de.png){ class="shadow lightbox" title="Tab Workflow in der Ansicht für Betreuer:innen" }

![Je Verfasser:in die Reviewer:innen mit Beurteilung, Mittelwert, Summe und Status der Beurteilung](assets/peer_review_coach_workflow_received_v1_de.png){ class="shadow lightbox" title="Liste Erhaltene Beurteilungen" }

![Je Person die vergebenen Reviews mit Beurteilung, Mittelwert, Summe und Status der Beurteilung](assets/peer_review_coach_workflow_given_v1_de.png){ class="shadow lightbox" title="Liste Vergebene Beurteilungen" }


<br>

---

## Muster zum Download {: #sample} 

[Musterformular für Peer-Review](assets/Musterformular_PeerReview.zip)


## Checkliste {: #checklist} 

- [x] Ist der gewünschte Prozess für das Peer-Review geklärt und beschrieben?
- [x] Welche Rolle nehmen die Betreuer:innen beim Peer-Review ein?
- [x] Zeigt der Kursbaustein "Aufgabe" im Kurseditor keine Fehlermeldungen mehr?<br> (z.B. "Sie haben noch keine Aufgabe erstellt" oder "Sie haben noch kein Formular für Peer-review definiert.")
- [x] Ist im Tab "Workflow" der Schritt "Feedback" aktiviert? (Ist im Kurseditor der Tab "Rückgabe und Feedback" aktiv?)
- [x] Deckt das zum Review verwendete Formular alle Anforderungen ab?
- [x] Wurde ein Zeitraum für das Peer-Review festgelegt?
- [x] Wurde die Punktebewertung sinnvoll geregelt?

[Zum Seitenanfang ^](#peer_review)

---


## Weiterführende Informationen {: #further_information}

[Wie erstelle ich meinen ersten OpenOlat-Kurs? >](../my_first_course/my_first_course.de.md)<br>
[Kursbaustein "Aufgabe" >](../../manual_user/learningresources/Course_Element_Task.de.md)<br>
[Wie erstelle ich eine Formular-Lernressource? >](../../manual_how-to/create_a_form/create_a_form.de.md)<br>
[Formular als Rubrik-Bewertung >](../../manual_user/learningresources/Forms_in_Rubric_Scoring.de.md)<br>
[Das Formular-Element Rubrik >](../../manual_user/learningresources/Form_Element_Rubric.de.md)<br>
[Aufgaben und Gruppenaufgaben bewerten >](../../manual_user/learningresources/Assessing_tasks_and_group_tasks.de.md)

[Zum Seitenanfang ^](#peer_review)
