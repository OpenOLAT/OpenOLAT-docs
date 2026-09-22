# Coaching - Bewertungsaufträge {: #assessment_orders}

![Markierter Eintrag Bewertungsaufträge unter Aufgaben führt zu den offenen Bewertungen, Einstufungen und Korrekturaufträgen, auf der Startseite Coaching.](assets/coaching_assessment_orders1_v1_de.png){ class="shadow lightbox" }


Hier sehen Sie, an welchen Stellen noch konkrete Coaching-Aktionen wie Bewertungen oder Einstufungen vorgenommen werden müssen, bzw. ob diese noch freigegeben werden müssen.

Je nach Rolle sind neben Ihren eigenen Bewertungsaufträgen auch die übrigen angezeigt und Sie können sich einen Überblick verschaffen.

![Liste mit Anmeldename, Name, Betreuer:in, Kursname, Baustein, letzter Aktualisierung und dem Link Bewerten, im Tab Offene Bewertungen.](assets/coaching_assessment_orders_open_assessments_v1_de.png){ class="shadow lightbox" }

---

### Bewertungsaufträge erstellen {: #create_assessment_orders}

Wer einen Kursbaustein auf manuelle Bewertung stellt, erstellt damit die Bewertungsaufträge für die Betreuung: Sobald eine teilnehmende Person ihre Arbeit abschliesst, legt OpenOlat den Auftrag an und zeigt ihn im passenden Tab. Betreuende sehen damit an einer Stelle, was ansteht.

Die Tabs "Offene Bewertungen", "Offene Einstufungen/Noten" und "Freizugebende Bewertungen" sehen Kursbesitzer:innen für alle Teilnehmenden des Kurses, Betreuende für die Personen, die sie betreuen. Den Tab "Korrekturaufträge" sehen die Personen, die im Korrektur-Workflow als Korrektor:in eingetragen sind.

![Vier Einstellungen führen zu den vier Tabs, dazu zwei weitere Wege zu einem Auftrag.](assets/coaching_assessment_orders_create_v1_de.svg){ class="shadow lightbox" }

Die Seiten, auf denen Sie die jeweilige Einstellung setzen:

* **Offene Bewertungen**: [Tests auf Kursebene](../learningresources/Tests_at_course_level.de.md#correction), [Kursbaustein Aufgabe](../learningresources/Course_Element_Task.de.md), [Kursbaustein Bewertung](../learningresources/Course_Element_Assessment.de.md)
* **Offene Einstufungen/Noten**: [Einstufung/Noten](../learningresources/Assessment_translate_points_in_grades.de.md)
* **Freizugebende Bewertungen**: [Tests auf Kursebene](../learningresources/Tests_at_course_level.de.md#correction), [Kurseinstellungen, Abschnitt Berechtigungen](../learningresources/Course_Settings_Assessment.de.md#section_assessment_rights)
* **Korrekturaufträge**: [Test Einstellungen](../learningresources/Test_settings.de.md#correction-workflow)

Der Kursbaustein muss dafür bewertbar und auf manuelle Bewertung gestellt sein, Punkte oder "Bestanden" werden also am Kursbaustein gesetzt. Steht die Korrektur eines Tests auf "Automatisch", wertet OpenOlat den Test selbst aus und gibt das Resultat sofort frei; das Gleiche gilt für die Zuweisung "Automatisch bei Punktänderungen" bei Einstufung und Noten.

Zwei weitere Wege führen zu einem Bewertungsauftrag:

* **Bewertung wieder eröffnen**: Mit der Schaltfläche "Bewertung wieder eröffnen" im [Bewertungsformular](../learningresources/The_assessment_form.de.md) geht der Status zurück auf "Korrigieren". Die Zeile steht danach erneut im Tab "Offene Bewertungen".
* **Zuweisung Betreuende/Teilnehmende**: Beim [Kursbaustein Aufgabe](../learningresources/Course_Element_Task.de.md#coach_assignment_table) ordnen Kursbesitzer:innen jeder teilnehmenden Person eine betreuende Person zu. Diese wird benachrichtigt und findet ihre Aufträge über den Filter "Mir zugewiesen".

[Zum Seitenanfang ^](#assessment_orders)

---

### Tab Offene Bewertungen [:octicons-tag-16:{ title="ab Release 16.1 (OO-5851)" }](https://track.frentix.com/issue/OO-5851) {: #tab_open_assessments}

Hier haben Sie Zugriff auf alle Kursbausteine, die noch zu bewerten sind. Diese können entsprechend der Spalten sortiert und dann einzeln ausgewählt und bewertet werden. Mit Klick auf den Link "Bewerten" gelangt man in das entsprechende Bewertungsformular.

Eine Zeile erscheint, sobald der Bewertungseintrag der teilnehmenden Person auf dem Status "Korrigieren" steht. Diesen Status erzeugen die manuelle Korrektur eines [Tests](../learningresources/Tests_at_course_level.de.md#correction), der Schritt Korrektur beim Kursbaustein [Aufgabe](../learningresources/Course_Element_Task.de.md) sowie der Schalter "Status Korrigieren setzen, wenn Zugriff gewährt" beim Kursbaustein [Bewertung](../learningresources/Course_Element_Assessment.de.md).

Über den Filter "Mir zugewiesen" schränken Sie die Liste auf die Aufträge ein, die Ihnen persönlich zugewiesen sind.

[Zum Seitenanfang ^](#assessment_orders)

---

### Tab Offene Einstufungen/Noten [:octicons-tag-16:{ title="ab Release 16.2 (OO-6009)" }](https://track.frentix.com/issue/OO-6009) {: #tab_open_classifications_scores}

Hier finden Sie alle Kursbausteine, die zwar schon bewertet wurden, bei denen aber die manuelle Zuordnung zu einer Notenskala bzw. einem Bewertungssystem noch nicht abgeschlossen wurde.

Eine Zeile erscheint, wenn am Kursbaustein "Bewertung mit Einstufung/Noten" eingeschaltet und die "Zuweisung" auf "Manuell" gestellt ist, die Punkte gesetzt sind und die Note noch aussteht. Sie setzen beides im Kurseditor am Kursbaustein, beim Test im Tab "Test-Konfiguration", sonst im Tab "Bewertung". Zusätzlich braucht es das Modul [Einstufung/Noten](../learningresources/Assessment_translate_points_in_grades.de.md) und eine hinterlegte Bewertungsskala.

Damit auch Betreuende ohne Besitzrecht die Zeile sehen und die Note zuweisen können, setzen Kursbesitzer:innen unter `Kurs > Administration > Einstellungen > Tab "Bewertung"` im [Abschnitt Berechtigungen](../learningresources/Course_Settings_Assessment.de.md#section_assessment_rights) die Option "Einstufung/Noten zuweisen".

[Zum Seitenanfang ^](#assessment_orders)

---

### Tab Freizugebende Bewertungen {: #tab_assessments_to_be_released}

Hier finden Sie alle Bewertungen, die noch nicht für die Teilnehmer:innen sichtbar sind und noch freigegeben werden müssen.

In diesem Tab ist es auch möglich, alle Kursbausteine auszuwählen und alle auf einmal freizugeben.

Beim Test steuert das Feld "Freigabe Bewertung" im [Abschnitt Korrektur](../learningresources/Tests_at_course_level.de.md#correction), ob OpenOlat die Bewertung nach abgeschlossener Korrektur selbst freigibt. Bei den übrigen manuell bewerteten Kursbausteinen entscheidet die Kursoption "Bewertung freigeben" im [Abschnitt Berechtigungen](../learningresources/Course_Settings_Assessment.de.md#section_assessment_rights); dieselbe Option gibt Betreuenden ohne Besitzrecht den Zugriff auf diesen Tab.

[Zum Seitenanfang ^](#assessment_orders)

---


### Tab Korrekturaufträge [:octicons-tag-16:{ title="ab Release 15.0 (OO-4442)" }](https://track.frentix.com/issue/OO-4442) {: #tab_grading_assignments}

Dieser Tab erscheint nur, wenn Sie als Korrektor:in für einen Test eingetragen wurden. Sie sehen eine Übersicht der Tests in den verschiedenen Kursen, die Sie noch manuell prüfen und korrigieren müssen. Je nach Einstellung in der Lernressource "Test" erfolgt die Bewertung anonym oder nicht.

Sind Sie weder Betreuer:in noch Besitzer:in einer Lernressource, fehlen die übrigen Tabs; die Überschrift "Meine Zuweisungen" mit Ihrer Liste steht dann direkt unter dem Titel "Bewertungsaufträge". Verwalten Sie den Korrektur-Workflow dagegen selbst, also als Besitzer:in einer Test-Lernressource mit Korrektur-Workflow, als Lernressourcenverwalter:in oder als Administrator:in, fehlt dieser Tab; Ihre Aufträge finden Sie dann unter `Coaching > Auftragsverwaltung` im Tab [Korrekturaufträge](Coaching_Order_Management.de.md#tab_grading_assignments).

![Filter für Taxonomie, Kurs, Test, Korrektor:in, Status, Korrekturzeitraum, Punkte und Bestanden, darunter die Liste mit Frist, Kurs, Kursbaustein und dem Link Korrigieren, im Tab Korrekturaufträge.](assets/coaching_assessment_orders_grading_assignments_v1_de.png){ class="shadow lightbox" }

Im Beispiel ist die Korrektur anonym eingestellt. Deshalb zeigen die Spalten "Vorname" und "Nachname" nur einen Strich. Die Einstellung dazu treffen Sie in der Lernressource unter `Test > Administration > Korrektur-Workflow > Tab "Konfiguration"`.

Über den Link "Korrigieren" gelangen Sie direkt zum zu korrigierenden Test und nehmen dort manuelle Bewertungen vor. Automatische Bewertungen können Sie überschreiben. Hinterlassen Sie dazu einen Kommentar.

#### So erstellen Sie einen Korrekturauftrag {: #create_grading_assignment}

Ein Korrekturauftrag entsteht in fünf Schritten. Er erreicht die Korrektor:in, sobald alle fünf gesetzt sind.

![Fünf Schritte vom Modul bis zum Korrekturauftrag, dazu die Zuweisung in der Auftragsverwaltung.](assets/coaching_assessment_orders_grading_chain_v1_de.svg){ class="shadow lightbox" }

1. In der System-Administration ist der Korrektur-Workflow eingeschaltet: `Administration > e-Assessment > Test`.
2. In der Lernressource Test ist die Korrektur eingeschaltet: `Test > Administration > Korrektur-Workflow > Tab "Konfiguration"`.
3. Im Tab "Korrektor:innen" sind die korrigierenden Personen eingetragen. Ihre Rolle in OpenOlat spielt dabei keine Rolle.
4. Am Kursbaustein Test steht die Korrektur auf "Manuell durch Korrektor:innen". Diese Option steht zur Auswahl, sobald Schritt 2 gesetzt ist. Mehr dazu auf der Seite [Tests auf Kursebene](../learningresources/Tests_at_course_level.de.md#correction).
5. Eine teilnehmende Person schliesst den Test ab.

Ist beim Abschluss keine Korrektor:in verfügbar, trägt der Auftrag den Status "Nicht zugeordnet" und wartet in der [Auftragsverwaltung](Coaching_Order_Management.de.md). Dort weisen ihn Lernressourcenverwalter:innen einer Person zu, und er erscheint in deren Liste.

Bei Freitextfragen laden Sie die Antwort einer Person über den Button "Als PDF herunterladen" oben rechts als PDF herunter. Das PDF enthält im Kopfbereich Angaben zu Kurs, Kursbaustein und Test. Bei anonymer Korrektur erscheint anstelle der persönlichen Angaben die "Teilnehmendenkennung". Alle Antworten einer Frage auf einmal laden Sie im [Korrekturwerkzeug des Kurses](../learningresources/Assessing_tests.de.md) herunter.

!!! tip "Voraussetzung"

    Der Download setzt voraus, dass in der System-Administration ein [PDF-Service](../../manual_admin/administration/External_Tools_-_Administration.de.md#pdf_generator) konfiguriert ist.

Die Verwaltung aller Korrektor:innen und ihrer Aufträge liegt dagegen in der [Auftragsverwaltung](Coaching_Order_Management.de.md).

[Zum Seitenanfang ^](#assessment_orders)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Tests auf Kursebene >](../../manual_user/learningresources/Tests_at_course_level.de.md)<br>
[Kursbaustein "Aufgabe" >](../../manual_user/learningresources/Course_Element_Task.de.md)<br>
[Kursbaustein "Bewertung" >](../../manual_user/learningresources/Course_Element_Assessment.de.md)<br>
[Einstufung/Noten >](../../manual_user/learningresources/Assessment_translate_points_in_grades.de.md)<br>
[Test Einstellungen - Administration >](../../manual_user/learningresources/Test_settings.de.md)<br>
[Das Bewertungsformular >](../../manual_user/learningresources/The_assessment_form.de.md)<br>
[Kurseinstellungen - Tab Bewertung >](../../manual_user/learningresources/Course_Settings_Assessment.de.md)<br>
[Tests bewerten >](../../manual_user/learningresources/Assessing_tests.de.md)<br>
[Externe Werkzeuge: Übersicht >](../../manual_admin/administration/External_Tools_-_Administration.de.md)<br>
[Coaching: Auftragsverwaltung >](../../manual_user/area_modules/Coaching_Order_Management.de.md)

**Weiterführend**<br>
[Coaching: Personensuche >](../../manual_user/area_modules/Coaching_User_Search.de.md)<br>
[Coaching: Personen >](../../manual_user/area_modules/Coaching_People.de.md)<br>
[Coaching: Kurse >](../../manual_user/area_modules/Coaching_Courses.de.md)<br>
[Coaching: Bildungsprodukte >](../../manual_user/area_modules/Coaching_Educational_Products.de.md)<br>
[Coaching: Termine / Absenzen >](../../manual_user/area_modules/Coaching_Events_Absences.de.md)<br>
[Coaching: Reports >](../../manual_user/area_modules/Coaching_Reports.de.md)<br>
[Coaching: Gruppen >](../../manual_user/area_modules/Coaching_Groups.de.md)<br>
[Rollen >](../../manual_user/basic_concepts/Roles.de.md)<br>
[Bewertungswerkzeug >](../../manual_user/learningresources/Assessment_tool_overview.de.md)

[Zum Seitenanfang ^](#assessment_orders)
