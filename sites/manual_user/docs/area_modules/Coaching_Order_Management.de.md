# Coaching - Auftragsverwaltung {: #order_management}


![Markierter Eintrag Auftragsverwaltung unter Administration führt zur Verwaltung der Korrektor:innen, ihrer Korrekturaufträge und der offenen Zuweisungen von Betreuenden, auf der Startseite Coaching.](assets/coaching_order_management1_v1_de.png){ class="shadow lightbox" }

Wenn mehrere Personen Tests von Hand korrigieren oder wenn Teilnehmende auf betreuende Personen verteilt werden, behalten Sie in der Auftragsverwaltung den Überblick darüber, wer was noch zu erledigen hat. Das Menü fasst dafür zwei Bereiche zusammen: den Korrektur-Workflow für die manuelle Bewertung von OpenOlat Tests und die offenen Zuweisungen von Betreuenden zu Teilnehmenden.

In der Lernressource Test kann der [Korrektur-Workflow](../learningresources/Test_settings.de.md) aktiviert werden. Sie können dann Tests zu einer oder mehreren Personen als Korrektor:innen zuordnen. Die beiden Tabs zum Korrektur-Workflow sehen Administrator:innen, Lernressourcenverwalter:innen und Besitzer:innen eines Tests, bei dem diese Option aktiviert wurde. Der Tab "Offene Zuweisungen" hat eigene Voraussetzungen, sie stehen in dessen Abschnitt.

[Zum Seitenanfang ^](#order_management)

---


## Tab "Korrektor:innen" [:octicons-tag-16:{ title="ab Release 15.0 (OO-4446)" }](https://track.frentix.com/issue/OO-4446) {: #tab_correctors}

![Filter Status, Test, Korrektor:in und Korrekturzeitraum, Button Korrektor:in hinzufügen und die Liste mit Total, Erledigt, Offen, Überfällig, Korrekturzeiten und Urlaub, im Tab Korrektor:innen.](assets/coaching_order_management_tab_correctors_v1_de.png){ class="shadow lightbox" }

Hier erhalten Sie einen Überblick über alle Ihre Korrektor:innen und deren Bewertungsstand. Sie können die Korrektor:innen nach verschiedenen Kriterien filtern, z.B. nach bestimmten Kursen, konkreten Tests oder noch offenen Bewertungen.

Über die entsprechende Spaltenauswahl können Sie sich anzeigen lassen,

* wie viele Tests ein:e Korrektor:in insgesamt bewerten soll,
* wie viele davon schon erledigt sind,
* wie viele offen sind und welche überfällig sind,
* seit wann der älteste offene Auftrag zugewiesen ist (Spalte "Älteste"),
* ob eine Abwesenheit hinterlegt ist (Spalte "Urlaub")
* und welche Korrekturzeit vorgesehen ist.

Die Spalte "Status" zeigt, ob eine Korrektor:in aktiviert oder deaktiviert ist. Die Spalte "Korrektur (echte Minuten)" zeigt die tatsächlich erfasste Korrekturzeit. Welche Rollen sie sehen, legt die System-Administration unter `Administration > e-Assessment > Test` im Segment "Korrektur-Workflow" fest.

Über den Button "Korrektor:in hinzufügen" fügen Sie einem Test weitere Korrektor:innen hinzu. Bestehende Zuordnungen können Sie deaktivieren.

Ein Hinzufügen von Korrektor:innen ist ebenfalls direkt bei der jeweiligen [Test-Lernressource](../learningresources/Test_settings.de.md) möglich.

Im Zeilenmenü einer Korrektor:in öffnen Sie den Eintrag "Report herunterladen" und erzeugen so eine Excel-Datei mit dem Stand der Korrekturaufträge dieser Korrektor:in. Aufbau und Filter des Reports beschreibt der Abschnitt [Test-Einstellungen, Report / Excel-Export](../learningresources/Test_settings.de.md#correction-workflow). [:octicons-tag-16:{ title="ab Release 21.0 (OO-9569)" }](https://track.frentix.com/issue/OO-9569)

Dasselbe Zeilenmenü führt zu den weiteren Aktionen: "Zuweisungen anzeigen" wechselt in den Tab "Korrekturaufträge" mit den Aufträgen dieser Person, "Korrektor:in kontaktieren" öffnet eine E-Mail, "Abwesenheit erfassen" hinterlegt eine Abwesenheit, die anschliessend in der Spalte "Urlaub" erscheint, und "Entfernen" nimmt die Person als Korrektor:in zurück und verteilt ihre Zuweisungen neu. Ist eine Korrektor:in deaktiviert, steht statt "Deaktivieren" der Eintrag "Aktivieren" zur Verfügung.

![Zeilenmenü mit Zuweisungen anzeigen, Korrektor:in kontaktieren, Report herunterladen, Abwesenheit erfassen, Deaktivieren und Entfernen, im Tab Korrektor:innen der Auftragsverwaltung.](assets/coaching_order_management_report_download_v1_de.png){ class="shadow lightbox" }



[Zum Seitenanfang ^](#order_management)

---


## Tab "Korrekturaufträge" {: #tab_grading_assignments}

Wollen Sie wissen, welcher Test gerade bei wem liegt und was davon überfällig ist, finden Sie hier alle Korrekturaufträge Ihrer Tests mit der zuständigen Korrektor:in und deren Stand.

Über den Button "Bericht" erzeugen Sie den Excel-Report über die angezeigten Korrekturaufträge. Aufbau und Filter des Reports beschreibt der Abschnitt [Test-Einstellungen, Report / Excel-Export](../learningresources/Test_settings.de.md#correction-workflow).

![Zu ausgewählten Korrekturaufträgen die Aktionen Korrektor:in wählen, wechseln, kontaktieren, Frist verlängern und Entfernen, im Tab Korrekturaufträge.](assets/coaching_order_management_tab_grading_assignments_v1_de.png){ class="shadow lightbox" }

Wählen Sie einzelne Korrekturaufträge aus, erscheinen die Aktionen "Korrektor:in wählen", "Korrektor:in wechseln", "Korrektor:in kontaktieren", "Frist verlängern" und "Entfernen". "Entfernen" hebt nur die Zuordnung zur Korrektor:in auf, der Korrekturauftrag selbst bleibt bestehen.


Ihre eigenen Korrekturaufträge als Korrektor:in finden Sie nicht hier, sondern unter `Coaching > Bewertungsaufträge`: [Coaching: Bewertungsaufträge](Coaching_Assessment_Orders.de.md#tab_grading_assignments).


[Zum Seitenanfang ^](#order_management)

---


## Tab "Offene Zuweisungen" [:octicons-tag-16:{ title="ab Release 17.2.1 (OO-6698)" }](https://track.frentix.com/issue/OO-6698) {: #tab_open_grading_assignments}

![Je Zeile Kurs, Kursbaustein und Anzahl offener Zuweisungen mit dem Link Zuweisen, im Tab Offene Zuweisungen der Auftragsverwaltung.](assets/coaching_order_management_tab_open_grading_assignments_v1_de.png){ class="shadow lightbox" }

Verteilen Sie die Teilnehmenden einer Aufgabe auf mehrere betreuende Personen, sehen Sie hier über alle Ihre Kurse hinweg, wo diese Verteilung noch nicht vollständig ist. Dieser Tab gehört deshalb nicht zum Korrektur-Workflow, sondern zur Zuweisung der Betreuenden. Ihn sehen Administrator:innen, Lernressourcenverwalter:innen, Principals und Autor:innen; aufgeführt sind die Kurse, in denen Sie Besitzer:in sind oder in denen Sie eine dieser Rollen innehaben.

Angezeigt werden die Kursbausteine "Aufgabe", bei denen die "Zuweisung Betreuende/Teilnehmende" eingeschaltet ist und teilnehmende Personen noch keiner betreuenden Person zugewiesen sind. Die Spalte "Offene Zuweisungen" nennt deren Anzahl. Über den Namen des Kursbausteins oder über die Anzahl öffnen Sie ihn direkt, über den Link "Zuweisen" nehmen Sie die Zuordnung vor.


[Zum Seitenanfang ^](#order_management)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Test Einstellungen - Administration >](../learningresources/Test_settings.de.md)<br>
[Coaching: Bewertungsaufträge >](../area_modules/Coaching_Assessment_Orders.de.md)

**Weiterführend**<br>
[Coaching: Personensuche >](../area_modules/Coaching_User_Search.de.md)<br>
[Coaching: Personen >](../area_modules/Coaching_People.de.md)<br>
[Coaching: Kurse >](../area_modules/Coaching_Courses.de.md)<br>
[Coaching: Bildungsprodukte >](../area_modules/Coaching_Educational_Products.de.md)<br>
[Coaching: Termine / Absenzen >](../area_modules/Coaching_Events_Absences.de.md)<br>
[Coaching: Reports >](../area_modules/Coaching_Reports.de.md)<br>
[Coaching: Gruppen >](../area_modules/Coaching_Groups.de.md)<br>
[Rollen >](../basic_concepts/Roles.de.md)<br>
[Bewertungswerkzeug >](../learningresources/Assessment_tool_overview.de.md)

[Zum Seitenanfang ^](#order_management)
