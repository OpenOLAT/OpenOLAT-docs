# Kurseinstellungen - Tab Bewertung {: #tab_assessment}

In Lernpfadkursen legen Sie unter `Kurs > Administration > Einstellungen > Tab "Bewertung"` fest, wie der Kurs bewertet wird und wann er als bestanden gilt.<br>
Ausserdem können Sie die Verwendung von Leistungsnachweisen und die Vergabe von Kreditpunkten, Zertifikaten und Badges aktivieren.<br>
Den Tab bearbeiten alle, die das Menü "Einstellungen" des Kurses öffnen dürfen: Besitzer:innen des Kurses, Lernressourcenverwalter:innen und Administrator:innen sowie Personen mit dem Recht "Kurseditor", siehe [Kurseinstellungen](Course_Settings.de.md).

Die Optionen dazu finden Sie in den Abschnitten

[Einstellungen Bewertung](#section_assessment_settings)<br>
[Berechtigungen](#section_assessment_rights)<br>
[Leistungsnachweis](#section_evidence_of_achievements)<br>
[Kreditpunkte](#section_credit_points)<br>
[Zertifikat](#section_certificate)<br>
[Badges](#section_badges)

![Tab Bewertung mit sechs hervorgehobenen Abschnittstiteln von Einstellungen Bewertung bis Badges, mit Punkten, Erfolgsstatus und eingeschaltetem Leistungsnachweis](assets/course_settings_assessment_v5_de.png){ class="shadow lightbox" title="Tab Bewertung in den Kurseinstellungen · 2026.10.08" }

[Zum Seitenanfang ^](#tab_assessment)

---


## Abschnitt Einstellungen Bewertung [:octicons-tag-16:{ title="ab Release 15.0 (OO-4582)" }](https://track.frentix.com/issue/OO-4582) {: #section_assessment_settings}

!!! info "Bewertung bei herkömmlichen Kursen"

    Die nachfolgenden Ausführungen beziehen sich auf Lernpfadkurse. Bei herkömmlichen Kursen werden die Kriterien für das Bestehen eines Kurses im Kurseditor auf dem obersten Kursbaustein im Tab "Punkte" eingestellt und das Ergebnis wird auf der Kursstartseite angezeigt.

Für Kursbewertungen gibt es folgende Einstellungen:

- **Mit Punkten** (nur bei Lernpfadkursen) {: #evaluation_with_points}<br>
    Hier können Sie einstellen, ob bzw. welche Art von Punkten angezeigt wird. Für die Kursbewertung mit Punkten stehen 3 Möglichkeiten zur Auswahl:

    * [Summe](#evaluation_with_points_sum)
    * [Summe mit Gewichtung](#evaluation_with_points_weighting) 
    * [Durchschnitt](#evaluation_with_points_average)

    ![Fortschrittsanzeige neben dem Menü Mein Kurs mit 61 % Lernfortschritt und zusätzlich 6 Punkten](assets/course_settings_assessment_points_percentage_v1_de.png){ class="aside-right lightbox" }
    Wird in [Lernpfadkursen](Learning_path_course.de.md) mit Punkten bewertet, wirkt sich dies darauf aus, ob bzw. welche Art von Punkten noch ergänzend zu der Prozentanzeige im Kurs angezeigt wird.

    Es kann mit Punkten bewertet werden, auch wenn sie nicht relevant für das Bestehen des Kurses sind.

- **Mit Einstufung/Noten** (nur bei Lernpfadkursen)<br>
  Bei aktiviertem Einstufungs-/Notenmodul weisen Sie dem Kurs auf Kursebene eine Note zu.<br> [Mehr dazu >](#evaluation_with_grades)

- **Mit Erfolgsstatus**<br>
  Hier können Sie einstellen, wann ein Kurs als bestanden gilt. Der Erfolgsstatus ist das Ergebnis der Kursbewertung: "Bestanden", "Nicht bestanden" oder "Keine Angabe". Neben einer bestimmten erreichten Punktzahl können auch andere Kriterien zu einem "Bestanden" führen.<br> [Mehr dazu >](#evaluation_passed_failed)

[Zum Seitenanfang ^](#tab_assessment)

---

### Kursbewertung mit Punkten: Summe {: #evaluation_with_points_sum}

Es wird aus allen im Kurs erzielten Punkten die Summe gebildet.

![Ausgewählte Option Summe unter Punkteberechnung bei eingeschaltetem Schalter Mit Punkten](assets/course_settings_assessment_points_sum_v3_de.png){ class="shadow lightbox" title="Punkteberechnung im Abschnitt Einstellungen Bewertung · 2026.10.08" }

[Zum Abschnitt Einstellungen Bewertung ^](#section_assessment_settings)<br>
[Zum Seitenanfang ^](#tab_assessment)

---


### Kursbewertung mit Punkten: Summe mit Gewichtung [:octicons-tag-16:{ title="ab Release 18.2.0 (OO-7378)" }](https://track.frentix.com/issue/OO-7378) {: #evaluation_with_points_weighting}

Bei der Summenbildung fliesst die Gewichtung mit ein.

![Ausgewählte Option Summe mit Gewichtung unter Punkteberechnung bei eingeschaltetem Schalter Mit Punkten](assets/course_settings_assessment_points_sum_with_weighting_v3_de.png){ class="shadow lightbox" title="Punkteberechnung im Abschnitt Einstellungen Bewertung · 2026.10.08" }

Sind in einem Kurs mehrere Leistungen zu erbringen, fliessen diese zum Teil mit unterschiedlicher Gewichtung in die Gesamtbewertung des Kurses ein. Die Option "Summe mit Gewichtung" für die Kurs-Bewertung ermöglicht es, bei bewertbaren Kursbausteinen einen Skalierungsfaktor für die Punkte zu hinterlegen. Die Punkte des Kursbausteins werden mit diesem Faktor multipliziert: Mit dem Faktor 0.5 zählen 10 Punkte als 5 Punkte. Voraussetzung ist, dass diese bewertbaren Kursbausteine bei der Kurs-Bewertung berücksichtigt werden.

In der "Übersicht Kurskonfiguration" des Kurseditors kann die Skalierung für alle bewertbaren Kursbausteine geprüft und bei Bedarf direkt gesetzt bzw. editiert werden. Den Faktor geben Sie als Bruch oder Zahl ein, zum Beispiel 1/2, 1/3, 2 oder 0.5. Wählen Sie über der Tabelle "Bewertbar", erscheinen nur die bewertbaren Kursbausteine. Weitere Spalten wie "Maximal erreichbare Punkte" blenden Sie über das Symbol "Spalten auswählen" ein.

![Eintrag Übersicht, über der Tabelle Bewertbar gewählt, Spalten Bei Kurs-Bewertung berücksichtigen und Skalierungsfaktor für Kurs-Bewertung, darunter das geöffnete Eingabefeld mit dem Faktor 0.5](assets/course_settings_assessment_weighting_score_scale_factor_v3_de.png){ class="shadow lightbox" title="Übersicht Kurskonfiguration im Kurseditor · 2026.10.08" }

Die gewichtete Punktzahl wird Betreuenden im Bewertungsformular angezeigt. Für Teilnehmende ist die gewichtete Punktzahl in der Leistungsübersicht des jeweiligen bewertbaren Kursbausteins sowie im Leistungsnachweis sichtbar.

[Zum Abschnitt Einstellungen Bewertung ^](#section_assessment_settings)<br>
[Zum Seitenanfang ^](#tab_assessment)

---

### Kursbewertung mit Punkten: Durchschnitt {: #evaluation_with_points_average}

Es wird der Durchschnitt aus den erzielten Punkten der bewertbaren Kursbausteine gebildet, die bei der Kurs-Bewertung berücksichtigt werden. Kursbausteine ohne Punktzahl zählen dabei nicht mit.

![Ausgewählte Option Durchschnitt unter Punkteberechnung bei eingeschaltetem Schalter Mit Punkten](assets/course_settings_assessment_points_sum_average_v3_de.png){ class="shadow lightbox" title="Punkteberechnung im Abschnitt Einstellungen Bewertung · 2026.10.08" }

!!! tip "HighScore"

    Ist "Mit Punkten" eingeschaltet, kann im Kurseditor auch der Tab "HighScore" des obersten Kursbausteins konfiguriert werden, bei jeder der drei Punkteberechnungen.

[Zum Abschnitt Einstellungen Bewertung ^](#section_assessment_settings)<br>
[Zum Seitenanfang ^](#tab_assessment)

---


### Kursbewertung mit Einstufung/Noten [:octicons-tag-16:{ title="ab Release 21.0 (OO-9511)" }](https://track.frentix.com/issue/OO-9511) {: #evaluation_with_grades}

Ist das Einstufungs-/Notenmodul aktiviert und wird der Kurs mit Punkten bewertet, können Sie mit der Option "Mit Einstufung/Noten" dem Kurs auf Kursebene eine Note zuweisen. Die Kursnote wird aus den Punkten auf Kursebene gebildet (Summe, Summe mit Gewichtung oder Durchschnitt gemäss der gewählten "Punkteberechnung") und über die gewählte "Bewertungsskala" in eine Note übersetzt. Über "Bewertungsskala bearbeiten" wählen Sie das Bewertungssystem und passen die Skala an.

Der Schalter lässt sich erst umlegen, wenn "Mit Punkten" eingeschaltet und "Mit Erfolgsstatus" ausgeschaltet ist. Fehlt eine der beiden Bedingungen, bleibt "Mit Einstufung/Noten" grau.

Ist "Mit Einstufung/Noten" aktiv, bestimmt die Bewertungsskala auch den Erfolgsstatus des Kurses. Der Kurs gilt als bestanden, wenn das "Erfolgskriterium" der Bewertungsskala erfüllt ist, also die tiefste Note oder Leistungsklasse, mit der eine Leistung als bestanden gilt. "Mit Erfolgsstatus" bleibt dann ausgeschaltet und lässt sich nicht mehr ändern. Enthält die gewählte Bewertungsskala kein Erfolgskriterium, hat der Kurs auf Kursebene keinen Erfolgsstatus.

Die Note wird nicht automatisch vergeben: Die "Zuweisung" steht fest auf "Manuell". Kursbesitzer:innen und berechtigte Betreuer:innen weisen die berechnete Note im [Bewertungswerkzeug](Assessment_tool_overview.de.md) zu. Damit auch Betreuende ohne Besitzrecht zuweisen können, setzen Kursbesitzer:innen im [Abschnitt Berechtigungen](#section_assessment_rights) die Option "Einstufung/Noten zuweisen".

!["Mit Einstufung/Noten" eingeschaltet mit Bewertungsskala und Erfolgskriterium, "Mit Erfolgsstatus" gesperrt mit Hinweis auf das Erfolgskriterium](assets/course_settings_assessment_grades_v2_de.png){ class="shadow lightbox" title="Einstufung/Noten im Abschnitt Einstellungen Bewertung · 2026.10.08" }

[Zum Abschnitt Einstellungen Bewertung ^](#section_assessment_settings)<br>
[Zum Seitenanfang ^](#tab_assessment)

---


### Kursbewertung mit Erfolgsstatus {: #evaluation_passed_failed}

Ein Lernpfadkurs kann als bestanden gelten, sobald eines der Kriterien zutrifft:

* **Lernfortschritt 100%**:<br> Wenn alle obligatorischen Kursbausteine abgeschlossen wurden und 100 % angezeigt wird, gilt der Kurs automatisch als bestanden.
* **Regel "Alle relevanten Kursbausteine bestanden"**:<br> Der Kurs gilt als bestanden, wenn alle bewertbaren Kursbausteine, die mit einem "bestanden/nicht bestanden" versehen sind, bestanden wurden, egal ob es sich um obligatorische oder freiwillige Kursbausteine handelt. Um einzelne Kursbausteine auszunehmen, schalten Sie in der Konfiguration des Kursbausteins im Kurseditor den Schalter "Bei Kurs-Bewertung berücksichtigen" aus.
* **Regel "Eine bestimmte Anzahl der relevanten Kursbausteine bestanden"**:<br> Hier können Sie definieren, wie viele und welche Kursbausteine bestanden sein müssen, damit der gesamte Kurs als bestanden gilt. Welche Kursbausteine mitzählen, legt im Kurseditor der Schalter "Bei Kurs-Bewertung berücksichtigen" in der Konfiguration des jeweiligen Kursbausteins fest.
* **Punkteschwelle erreicht**:<br> Hier können Sie definieren, wie viele Punkte Lernende erreichen müssen, damit der gesamte Kurs als bestanden gilt. Ausserdem können Sie kontrollieren, von welchen Kursbausteinen die Punkte stammen müssen. Welche Kursbausteine mitzählen, legt auch hier der Schalter "Bei Kurs-Bewertung berücksichtigen" in der Konfiguration des jeweiligen Kursbausteins fest.


![Mit Erfolgsstatus eingeschaltet, drei Kriterien angehakt: Lernfortschritt 100%, Anzahl bestandener Kursbausteine und Punkteschwelle](assets/course_settings_assessment_passed_v4_de.png){ class="shadow lightbox" title="Erfolgsstatus im Abschnitt Einstellungen Bewertung · 2026.10.08" }

!!! info "Bestanden-Kriterien"

    Die einzelnen Kriterien sind eine "Oder-Verknüpfung". Es genügt also, wenn eines der genannten Kriterien zutrifft.

!!! info "Welche Kursbausteine werden berücksichtigt?"

    Bei der Berechnung des Lernfortschritts zählen nur die obligatorischen Kursbausteine.

    Bei der Berechnung von "Bestanden" und Punkten zählen obligatorische und freiwillige Kursbausteine.

[Zum Abschnitt Einstellungen Bewertung ^](#section_assessment_settings)<br>
[Zum Seitenanfang ^](#tab_assessment)

---


## Abschnitt Berechtigungen {: #section_assessment_rights}

![Optionen für Betreuende zum Zurücksetzen der Daten von Teilnehmenden, zum Zuweisen von Einstufung/Noten und zum Freigeben der Bewertung](assets/course_settings_assessment_user_rights_v1_de.png){ class="lightbox" title="Abschnitt Berechtigungen" }

Betreuenden kann gestattet werden ...

* den Erfolgsstatus "Bestanden/Nicht bestanden" der Kurs-Bewertung manuell zu setzen,
* Daten von Teilnehmenden zurückzusetzen,
* Einstufung/Noten zuzuweisen,
* und die Bewertung für die Teilnehmer:innen freizugeben. 

Die Option für den manuellen Erfolgsstatus erscheint nur, wenn im [Abschnitt Einstellungen Bewertung](#section_assessment_settings) unter "Mit Erfolgsstatus" mindestens ein Kriterium angehakt ist. Wählbar ist sie erst, wenn auch "Bewertung freigeben" angehakt ist.

[Zum Seitenanfang ^](#tab_assessment)

---


## Abschnitt Leistungsnachweis {: #section_evidence_of_achievements}

![Eingeschalteter Schalter Leistungsnachweis den Teilnehmer:innen anzeigen](assets/course_settings_assessment_evidence_of_achievements_v2_de.png){ class="shadow lightbox" title="Abschnitt Leistungsnachweis · 2026.10.08" }

![Eintrag Leistungsnachweis an erster Stelle im Menü Mein Kurs, darunter To-dos, Meine Badges, Notizen und Bookmark](assets/course_settings_assessment_evidence_of_achievements_my_cours_v1_de.png){ class="aside-right lightbox" }

Wenn Sie die Option "Leistungsnachweis den Teilnehmer:innen anzeigen" aktivieren, erscheint im Kurs im Toolbar Menü ["Mein Kurs"](../learningresources/Additional_Course_Features.de.md) die Option "Leistungsnachweis" und die Teilnehmenden sehen einen Überblick über die bewertbaren Kursbausteine mit ihrem jeweiligen aktuellen Bewertungsstatus.

Der Eintrag "Leistungsnachweis" erscheint im Menü "Mein Kurs" für Teilnehmende, sobald diese Option eingeschaltet ist. Er erscheint auch bei ausgeschalteter Option, wenn im [Abschnitt Zertifikat](#section_certificate) "Zertifikat ausstellen" eingeschaltet ist. Gäste sehen den Eintrag nicht, und solange im Kurs eine Prüfung im [Prüfungsmodus](Assessment_mode.de.md) läuft, bleibt er ausgeblendet.

Wenn Sie die Funktion ausschalten, sehen Ihre Teilnehmenden keine Leistungsnachweise mehr. Die Leistungsnachweise gehen nicht verloren, sondern werden lediglich nicht mehr angezeigt. Wenn Sie den Leistungsnachweis wieder einschalten, stehen alle aktuellen Daten wieder zur Verfügung. Auch wenn Sie einen Kurs mit bestehenden Leistungsnachweisen löschen, können die Teilnehmenden ihre [Leistungsnachweise](../personal_menu/Evidence_of_Achievements.de.md) weiterhin einsehen. Dort fehlt für den gelöschten Kurs die Aktion "Kurs öffnen". [:octicons-tag-16:{ title="ab Release 21.0.3 (OO-8667)" }](https://track.frentix.com/issue/OO-8667)

[Zum Seitenanfang ^](#tab_assessment)

---


## Abschnitt Kreditpunkte [:octicons-tag-16:{ title="ab Release 20.1.1 (OO-8558)" }](https://track.frentix.com/issue/OO-8558) {: #section_credit_points}

![Eingeschalteter Schalter Kreditpunkte ausstellen mit Kreditpunktesystem, vergebenen Kreditpunkten und überschriebener Gültigkeitsdauer](assets/course_settings_assessment_credit_points_v2_de.png){ class="shadow lightbox" title="Abschnitt Kreditpunkte · 2026.10.08" }

Ist "Kreditpunkte ausstellen" eingeschaltet, werden den Teilnehmer:innen nach Bestehen des Kurses automatisch Kreditpunkte gutgeschrieben. Dazu können verschiedene (von Administrator:innen definierte) Kreditpunktesysteme gewählt werden.

Als Kursbesitzer:in bestimmen Sie, wie viele Kreditpunkte vergeben werden, wenn dieser Kurs bestanden wird.<br>
Hat das gewählte Kreditpunktesystem eine Gültigkeitsdauer, übernimmt der Kurs sie mit der Option "Vom Kreditpunktesystem übernehmen". Mit "Überschreiben" legen Sie für diesen Kurs eine eigene Gültigkeitsdauer fest.

!!! note "Hinweis"

    Die Vergabe von Kreditpunkten ist auch innerhalb eines Zertifikatsprogramms von Bedeutung.

Weitere Informationen:<br>
[Kreditpunkte systemweit aktivieren >](../../manual_admin/administration/e-Assessment_Credit_Points.de.md)<br>

[Zum Seitenanfang ^](#tab_assessment)

---


## Abschnitt Zertifikat [:octicons-tag-16:{ title="ab Release 10.1 (OO-1254)" }](https://track.frentix.com/issue/OO-1254) {: #section_certificate}

![Eingeschalteter Schalter Zertifikat ausstellen mit PDF Zertifikat erzeugen, Zertifikatvorlage, optionalen Variablen, Gültigkeitsdauer und Rezertifizierung](assets/course_settings_assessment_certificate_v1_de.png){ class="lightbox" title="Abschnitt Zertifikat" }


Als Bestätigung für den Besuch eines Kurses bzw. der Erreichung von bestimmten kursbezogenen Aktivitäten kann ein PDF-Zertifikat ausgestellt werden.

[Details zu Zertifikaten in einem Kurs >](../learningresources/Course_Settings_Assessment_Certificate.de.md)<br>

Ist beim Zertifikat "Gültigkeitsdauer" angehakt, erscheint darunter der Schalter "Rezertifizierung". Damit können Teilnehmende den Kurs vor Ablauf des Zertifikats erneut absolvieren und das Zertifikat erneuern.<br>
[Details zur Rezertifizierung >](../learningresources/Course_Settings_Assessment_Certificate.de.md#recertification)

[Zum Seitenanfang ^](#tab_assessment)

---


## Abschnitt Badges [:octicons-tag-16:{ title="ab Release 18.0.0 (OO-7003)" }](https://track.frentix.com/issue/OO-7003) {: #section_badges}

![Eingeschalteter Schalter Badges vergeben mit den Optionen für die manuelle Vergabe durch Kursbesitzer:innen und Betreuer:innen](assets/course_settings_assessment_badges_v1_de.png){ class="lightbox" title="Abschnitt Badges" }

Wer Teilnehmende im Kurs mit Badges auszeichnen will, schaltet hier "Badges vergeben" ein. Danach erscheint im Menü "Administration" des Kurses der Eintrag "Badges", und bewertbare Kursbausteine erhalten im Kurseditor zusätzlich den Tab "Badges".

Eine manuelle Vergabe von Badges durch Kursbesitzer:innen ist immer möglich, Betreuer:innen können wahlweise ebenfalls berechtigt werden.

Weitere Infos zu Badges finden Sie hier:<br> 
[Infos für Kursbesitzer:innen (Erstellen und Bearbeiten von Badges) >](../learningresources/OpenBadges.de.md)<br>
[Infos für Benutzer:innen (Badges bei den "Persönlichen Werkzeugen") >](../personal_menu/OpenBadges.de.md)<br> 
[Infos für OpenOlat Administrator:innen >](../../manual_admin/administration/e-Assessment_openBadges.de.md)

[Zum Seitenanfang ^](#tab_assessment)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kurseinstellungen >](Course_Settings.de.md)<br>
[Lernpfadkurs - Überblick >](Learning_path_course.de.md)<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview.de.md)<br>
[Zusätzliche Kursfunktionen >](Additional_Course_Features.de.md)<br>
[Prüfungsverwaltung: Prüfungsmodus >](Assessment_mode.de.md)<br>
[Persönliche Erfolge/Leistungen: Leistungsnachweise >](../personal_menu/Evidence_of_Achievements.de.md)<br>
[e-Assessment Administration: Kreditpunkte >](../../manual_admin/administration/e-Assessment_Credit_Points.de.md)<br>
[Kurseinstellungen - Tab Bewertung: Zertifikate und Rezertifizierung >](Course_Settings_Assessment_Certificate.de.md)<br>
[Badges >](OpenBadges.de.md)<br>
[Persönliche Erfolge/Leistungen: Badges >](../personal_menu/OpenBadges.de.md)<br>
[e-Assessment Administration: OpenBadges >](../../manual_admin/administration/e-Assessment_openBadges.de.md)

**Weiterführend**<br>
[Einstufung/Noten >](Assessment_translate_points_in_grades.de.md)<br>
[Lernpfadkurs - Kurseditor >](Learning_path_course_Course_editor.de.md)

[Zum Seitenanfang ^](#tab_assessment)

