# Wie bewerte ich einen Test? {: #assessing_tests}

??? abstract "Ziel und Inhalt dieser Anleitung"

    Im Kurs gibt es einen Test-Kursbaustein, und die Teilnehmenden haben den Test bearbeitet.<br>
    Wie gehen Sie nun vor, um die Testergebnisse der Teilnehmenden einzusehen, manuell zu bewerten, zu kommentieren und abzuschliessen? Die folgende Anleitung zeigt es Ihnen.

??? abstract "Zielgruppe"

    [ ] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Experten/Expertinnen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    * ["Wie gehe ich vor, wenn ich einen Test erstelle?"](../test_creation_procedure/test_creation_procedure.de.md)
    * [Bewertungswerkzeug >](../../manual_user/learningresources/Assessment_tool_overview.de.md)

---


## Was bedeutet "einen Test bewerten"? {: #meaning}

In OpenOlat können Tests automatisch oder manuell ausgewertet werden. 

**Automatisch bewertbare Fragen** (z. B. Single Choice, Multiple Choice) können direkt nach der Abgabe vom System ausgewertet werden.<br> 
**Manuell zu bewertende Fragen** sind z. B. Freitext oder Zeichnen. Sie erfordern zwingend eine Bewertung durch Betreuer:innen. Aber auch bereits automatisch ausgewertete Fragen können nachbearbeitet werden.

Als Betreuer:in können Sie im **Bewertungswerkzeug**:

* Testergebnisse aller Teilnehmer:innen einsehen
* Einzelne Fragen manuell mit Punkten bewerten
* Gesamtpunktzahl und Bestanden-Status manuell überschreiben
* Kommentare für Teilnehmer:innen und andere Betreuer:innen hinterlassen
* Bewertungen einzeln oder per Sammelaktion abschliessen

[zum Seitenanfang ^](#assessing_tests)

---

## Wie wird ein Bewertungsauftrag erstellt und vergeben? {: #assessment_order}

Ob für einen Test ein Bewertungsauftrag entsteht, entscheidet die Einstellung "Korrektur" am Kursbaustein Test: Wertet OpenOlat den Test automatisch aus, oder korrigiert eine Person ihn von Hand?<br>
Automatisch ausgewertete Tests brauchen keinen Bewertungsauftrag, OpenOlat zeigt das Resultat sofort. Für manuell korrigierte Tests erstellt OpenOlat einen Auftrag. Kursbesitzer:innen wählen die Variante unter:<br> `Kurs > Administration > Kurseditor > Kursbaustein Test wählen > Tab "Test-Konfiguration" > Abschnitt "Korrektur"`

Als Betreuer:in ohne Besitzrecht ändern Sie diese Einstellung nur, wenn Ihnen im Kurs das Recht "Kurseditor" erteilt wurde. Den Auftrag bearbeiten Sie, sobald OpenOlat ihn angelegt hat.

Soll manuell korrigiert werden? Sobald eine teilnehmende Person den Test abschliesst, erstellt OpenOlat einen Bewertungsauftrag. Wer ihn erhält, hängt von der gewählten Variante ab:

* **Manuell durch Kursbetreuer:in oder -besitzer:in**: Der Auftrag steht bei allen Betreuenden der Person und bei den Kursbesitzer:innen, unter `Coaching > Bewertungsaufträge > Tab "Offene Bewertungen"`. Eine Zuweisung an eine bestimmte Person gibt es bei dieser Variante nicht.
* **Manuell durch Korrektor:innen**: OpenOlat weist den Auftrag einer Person zu, die im Korrektur-Workflow der Lernressource Test eingetragen ist. Diese Variante steht zur Wahl, sobald die Besitzer:innen des Tests in der Lernressource Test den [Korrektur-Workflow](../../manual_user/learningresources/Test_settings.de.md#correction-workflow) eingeschaltet haben. Korrektor:innen brauchen keine Mitgliedschaft im Kurs. Sie finden den Auftrag als Korrekturauftrag unter `Coaching > Bewertungsaufträge > Tab "Korrekturaufträge"`.

Ist beim Abschluss keine Korrektor:in verfügbar, wartet der Korrekturauftrag mit dem Status "Nicht zugeordnet" unter `Coaching > Auftragsverwaltung > Tab "Korrekturaufträge"`. Dort weisen Besitzer:innen des Tests, Lernressourcenverwalter:innen oder Administrator:innen ihn einer Korrektor:in zu, und er erscheint in deren Tab "Korrekturaufträge".

Welche Einstellung welchen Tab im Coaching füllt, zeigt der Abschnitt [Bewertungsaufträge erstellen](../../manual_user/area_modules/Coaching_Assessment_Orders.de.md#create_assessment_orders).

[zum Seitenanfang ^](#assessing_tests)

---


## Wie gelange ich zu meinen Bewertungsaufträgen (Tests)? {: #access}

Als Betreuer:in sehen Sie die Bewertungsaufträge der Personen, die Sie betreuen, als Kursbesitzer:in die Aufträge aller Teilnehmenden des Kurses. Als Korrektor:in sehen Sie die Korrekturaufträge, die Ihnen zugewiesen sind.

Ein Test wird jeweils mit einem Bewertungsformular bewertet. Um es aufzurufen, gibt es 3 Einstiegspunkte:

### 1. Einstieg direkt im Kursbaustein {: #access_course_element}

![Drei markierte Schritte vom Kursbaustein über den Tab Teilnehmer:innen zur Zeile einer teilnehmenden Person, im Kurs bei geschlossenem Editor](assets/assessing_tests_access1a_v1_de.png){ class="shadow lightbox" }

![1](assets/1_green_24.png) Wer als Betreuer:in angemeldet ist, sieht bei **Klick auf einen Test-Kursbaustein** nicht den Test (wie die Teilnehmer:innen), sondern eine Übersicht zum Bearbeitungsstatus der betreuten Teilnehmer:innen (den ausgewählten Test-Kursbaustein betreffend).

![2](assets/2_green_24.png) Im **Tab "Teilnehmer:innen"** erhalten Sie die Liste der betreuten Teilnehmer:innen mit Bearbeitungsstatus dieses Kursbausteins.

![3](assets/3_green_24.png) Nach **Wahl eines/einer Teilnehmer:in** gelangen Sie zum **Bewertungsformular** des Gesamttests.

![Liste der Testversuche und darunter das Bewertungsformular mit Punktezahl, Bestanden und den Schaltflächen Zwischenspeichern und Bewertung abschliessen, dazu das Zeilenmenü mit Korrigieren](assets/assessing_tests_access1b_v1_de.png){ class="shadow lightbox" }

![4](assets/4_green_24.png) Im **Bewertungsformular des gesamten Tests** finden Sie alle bisherigen Testversuche des/der Teilnehmer:in aufgelistet und können den Gesamttest bewerten. Auch Zwischenspeichern ist möglich. Sie können

* Punkte vergeben oder bereits automatisch vergebene Punkte überschreiben
* "Bestanden" oder "Nicht bestanden" vergeben
* Kommentare für die Teilnehmer:in ergänzen
* Bewertungsdokumente hinzufügen
* Kommentare für andere Betreuende hinterlegen


![5](assets/5_green_24.png) Mit Klick auf das **Korrektur-Icon** oder die **3 Punkte und dann "Korrigieren"** in der Zeile des aktuellen Testversuchs öffnen Sie das **Korrekturwerkzeug**. Sie erhalten die Liste der Fragen dieses Tests und können jede Einzelfrage bewerten. (Zu jeder Frage gibt es ein **Bewertungsformular der Einzelfrage**.) Sie können

* sich die Resultate anzeigen lassen
* einen Testversuch annullieren
* die Resultate dieses/dieser Teilnehmer:in als pdf exportieren
* mit Log-Dateien den Verlauf des Testversuchs nachvollziehen.


Wurde eine Bewertung abgeschlossen, ändern sich die angebotenen Buttons. Sie können dann

* die abgegebene Bewertung wieder eröffnen
* die Bewertung freigeben
* die Freigabe wieder zurückziehen  


[zum Seitenanfang ^](#assessing_tests)

---


### 2. Einstieg durch Aufruf des Bewertungswerkzeuges {: #access_assessment_tool}

Das Bewertungswerkzeug wird aufgerufen via<br>
**Kurs > Administration > Bewertungswerkzeug**

![Aufgeklapptes Menü Administration mit dem markierten Eintrag Bewertungswerkzeug, im Kurs](assets/assessing_tests_access2a_v1_de.png){ class="shadow lightbox" }

Die nun folgenden Schritte sind die gleichen, wie beim Einstieg direkt im Kursbaustein (siehe [vorangehender Abschnitt](#access_course_element)). Im Bewertungswerkzeug werden links alle bewertbaren Kursbausteine des ganzen Kurses angezeigt. Wählen Sie den relevanten Test-Kursbaustein, den Tab "Teilnehmer:innen", usw.

Beachten Sie auch die Optionen unter dem Icon am Ende der Zeile.

![Drei markierte Schritte im Bewertungswerkzeug vom Kursbaustein über den Tab Teilnehmer:innen zur Zeile, dazu das Zeilenmenü mit Details anzeigen und Korrigieren](assets/assessing_tests_access2b_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#assessing_tests)

---


### 3. Einstieg über das Coachingtool {: #access_coaching_tool}

Wird Ihnen im **Menü der Kopfzeile die Option "Coachingtool"** angezeigt, können Sie auch darüber zur Bewertung des Test-Kursbausteins gelangen.

Das **Coachingtool** zeigt **kursübergreifend** anstehende Bewertungsaufträge an.
Sie können von der Übersichtsseite des Coachingtools über viele Links zu Ihrer Bewertungsaufgabe gelangen. Zum Beispiel, indem Sie eine bestimmte Person suchen oder nur die unerledigten Bewertungsaufträge. 

Die darauf folgenden Schritte entsprechen dann wieder denen, wie beim Einstieg direkt im Kursbaustein (siehe [vorangehender Abschnitt](#access_course_element)).

Welche Einstellung welchen Tab des Coachingtools füllt, steht im Abschnitt [Bewertungsaufträge erstellen](../../manual_user/area_modules/Coaching_Assessment_Orders.de.md#create_assessment_orders).

![Startseite Coaching mit den markierten Einstiegen Personensuche, Personen, Kurse und Bewertungsaufträge sowie den Favoriten](assets/assessing_tests_access3a_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#assessing_tests)

---


## Automatische und manuelle Bewertung {: #automatic-manually}

Die meisten Fragetypen können automatisch bewertet werden (z.B. Single Choice, Multiple Choice).
Wird automatisch bewertet, können Sie die automatische Bewertung so übernehmen oder sie manuell mit einer eigenen (manuellen Bewertung) übersteuern.

Daneben gibt es Fragetypen, die zwingend manuell bewertet werden müssen, weil sie nicht automatisch auswertbar sind (z.B. das Freitext-Eingabefeld).

Ob automatisch oder grundsätzlich alles manuell korrigiert und bewertet werden soll, legen die Besitzer:innen des Kurses im Kurseditor am Kursbaustein Test fest:<br>
`Kurs > Administration > Kurseditor > Kursbaustein Test > Tab "Test-Konfiguration" > Abschnitt "Korrektur"`<br>
Was die drei Varianten bewirken, steht auf der Seite [Tests auf Kursebene](../../manual_user/learningresources/Tests_at_course_level.de.md#correction).

[zum Seitenanfang ^](#assessing_tests)

---


## Das Bewertungsformular {: #assessment_form}

**Pro Frage** eines Tests gibt es für jede:n Kursteilnehmer:in in OpenOlat ein Bewertungsformular.

Ausserdem gibt es ein Bewertungsformular für den **gesamten Test-Kursbaustein**.<br>
Siehe [1. Einstieg direkt im Kursbaustein, Schritt 3 ^](#access_course_element)

Dort können Sie

* kurze Feedbacks geben (Kommentar für Teilnehmende)
* Punkte vergeben
* bestanden/nicht bestanden definieren 
* die Freigabe der Resultate für Lernende einstellen
* Kommentare für andere Betreuende hinterlassen
* Bewertungsdokumente verteilen
* eine Bewertung abschliessen

[zum Seitenanfang ^](#assessing_tests)

---


## Das Korrekturwerkzeug {: #correction_tool}

In OpenOlat wird unterschieden zwischen **Bewertungswerkzeug** und **Korrekturwerkzeug**.<br>
Mit Hilfe des Korrekturworkflows können Sie persönliche Korrekturaufträge generieren und diese definierten Korrektoren zuweisen. Die Korrektur über das Bewertungswerkzeug ist dann nicht mehr möglich.

Mit dem **Bewertungswerkzeug** können verschiedene **bewertbare Kursbausteine** bewertet werden:

* Checkliste
* Bewertung
* Portfolioaufgabe
* Kursbaustein "Struktur", sowie der gesamte Kurs
* Kursbaustein "Teilnehmer:innen Ordner"
* Integrierte externe Bausteine wie SCORM
* Aufgabe und Gruppenaufgabe
* Tests

Für **Tests** ist zusätzlich ein **Korrekturwerkzeug** verfügbar, in dem die Tests auch **fragenweise** korrigiert werden können. Sie gelangen z.B. über das Bewertungswerkzeug dorthin.

**Kurs wählen > Administration > Bewertungswerkzeug > Kursbaustein wählen > Tab "Teilnehmer" > Button "Korrekturwerkzeug"**

![Vier markierte Schritte vom Bewertungswerkzeug über den Kursbaustein und den Tab Teilnehmer:innen zum Button Korrekturwerkzeug](assets/assessing_tests_correction_tool1_v1_de.png){ class="shadow lightbox" }

Es kann damit auf 2 Arten korrigiert werden:

1. Eine bestimmte **Frage auswählen** und diese Frage bei allen Teilnehmenden korrigieren.
2. Einen **Teilnehmenden auswählen** und dann nacheinander alle Fragen dieses Teilnehmenden korrigieren, bevor Sie zum nächsten Teilnehmenden wechseln.

![Umschalter Fragen und Teilnehmer:innen über der Fragenliste mit Fragetyp, beantwortet sowie automatisch und manuell korrigiert, im Korrekturwerkzeug](assets/assessing_tests_correction_tool_process1_v1_de.png){ class="shadow lightbox" }

![Bewertungsformular einer Einzelfrage mit Punkte überschreiben, Kommentarfeld, Bewertungsdokument und Zur Überprüfung markieren, im Korrekturwerkzeug](assets/assessing_tests_correction_tool_process2_v1_de.png){ class="shadow lightbox" }

Es ist möglich, Tests in OpenOlat auch anonym korrigieren zu lassen. Mehr darüber erfahren Sie im How-to [Wie macht man in OpenOlat eine anonyme Test-Korrektur?  >](../../manual_how-to/assessing_tests_anonymously/assessing_tests_anonymously.de.md)

[zum Seitenanfang ^](#assessing_tests)

---


## Bewertungssysteme {: #grading_systems}

Standardmässig wird in OpenOlat jede Frage mit Punkten bewertet.

Die Punkte je Fragen werden zur Punktesumme des Kursbausteins addiert.

Die Endsumme der Punkte kann umgerechnet werden in

* Noten (Details sind konfigurierbar, z.B. 1-6 oder 6-1)
* Begriffe zur Bewertung (z.B. "sehr gut", "gut", usw. oder A1, B1, usw. für Sprachniveaus)
* Grafische Bewertung (z.B. verschiedene Emojis)

Ob und wie eine Umwandlung der Punkte stattfindet, wird von dem/der Kursautor:in festgelegt und kann nicht von bewertenden Personen eingestellt werden.<br>
[Mehr dazu >](../../manual_user/learningresources/Assessment_translate_points_in_grades.de.md)

[zum Seitenanfang ^](#assessing_tests)

---


## Sammelaktionen: Mehrere Teilnehmer:innen gleichzeitig bearbeiten {: #bulk_action}

Das Bewertungswerkzeug bietet **Sammelaktionen**, um den Status mehrerer Teilnehmer:innen auf einmal zu setzen, ohne jede Person einzeln zu öffnen.

* Selektieren Sie in der Teilnehmer:innenliste die **Checkboxen** der gewünschten Personen in der ersten Spalte. Wenn Sie die Checkbox in der Kopfzeile selektieren, werden alle Checkboxen dieser Spalte selektiert.
* Sobald mindestens eine Person ausgewählt ist, erscheinen mehrere Buttons für Sammelaktionen oberhalb der Tabelle.
* Wählen Sie eine der Aktionen.

![Sammelaktionen Bewertung abschliessen, Freigeben, Freigabe zurückziehen, Korrekturwerkzeug und E-Mail über der Liste, für zwei ausgewählte Teilnehmende](assets/assessing_tests_bulk_actions_v1_de.png){ class="shadow lightbox" }

[zum Seitenanfang ^](#assessing_tests)


---

## Checkliste {: #checklist}

- [x] Wurde der Test von allen Kursteilnehmer bearbeitet?
- [x] Ist der späteste erlaubte Bearbeitungszeitpunkt bereits überschritten?
- [x] Ist klar, wer die Testergebnisse bewertet?
- [x] Soll eine Person korrigieren, die nicht Mitglied des Kurses ist? 
- [x] Sollen Korrekturaufträge vergeben werden?
- [x] Wurde der Test so konfiguriert, dass er automatisch bewertet wird oder soll er manuell bewertet werden?
- [x] Enthält der Test ausschliesslich Fragen, die automatisch ausgewertet werden können?

[zum Seitenanfang ^](#assessing_tests)

---


## Weiterführende Informationen {: #further_information}

**youtube**<br>
:octicons-device-camera-video-24: **Video-Einführung**: [Überblick Testing](<https://www.youtube.com/embed/fkqH41-8CaI>){:target="_blank”}<br>
:octicons-device-camera-video-24: **Video-Einführung**: [Wie funktionieren Tests in OpenOlat?](<https://www.youtube.com/embed/M0p3UKaEOlg>){:target="_blank”}

**Weiterführend**<br>
[Bewertungswerkzeug - Übersicht >](../../manual_user/learningresources/Assessment_tool_overview.de.md)<br>
[Bewertungswerkzeug - Tab Teilnehmer:innen >](../../manual_user/learningresources/Assessment_tool_tab_Users.de.md)<br>
[Bewertungswerkzeug - Lernende bewerten >](../../manual_user/learningresources/Assessment_of_learners.de.md)<br>
[Bewertung von Kursbausteinen >](../../manual_user/learningresources/Assessment_of_course_modules.de.md)<br>
[Test erstellen >](../../manual_user/learningresources/Test.de.md)<br>
[Test konfigurieren >](../../manual_user/learningresources/Configure_tests.de.md)<br>
[Tests bewerten >](../../manual_user/learningresources/Assessing_tests.de.md)<br>
[Das Bewertungsformular >](../../manual_user/learningresources/The_assessment_form.de.md)<br>
[Einstufung/Noten >](../../manual_user/learningresources/Assessment_translate_points_in_grades.de.md)<br>
[Daten zurücksetzen >](../../manual_user/learningresources/Assessment_tool_reset_data.de.md)<br>
[Test Einstellungen - Administration >](../../manual_user/learningresources/Test_settings.de.md)<br>
[Coaching - Bewertungsaufträge >](../../manual_user/area_modules/Coaching_Assessment_Orders.de.md)<br>
[Tests auf Kursebene >](../../manual_user/learningresources/Tests_at_course_level.de.md)<br>
[Wie macht man in OpenOlat eine anonyme Test-Korrektur?  >](../../manual_how-to/assessing_tests_anonymously/assessing_tests_anonymously.de.md)<br>

[zum Seitenanfang ^](#assessing_tests)