# e-Assessment Administration: Test {: #test}

Die Testeinstellungen liegen in der System-Administration unter `Administration > e-Assessment > Test`, verteilt auf vier Tabs.

## Tab QTI [:octicons-tag-16:{ title="ab Release 11.3 (OO-2535)" }](https://track.frentix.com/issue/OO-2535) {: #tab_QTI}

Die Testquittung bestätigt Teilnehmer:innen, dass sie den Test zum angegebenen Zeitpunkt absolviert haben. Auf diesem Tab schalten Sie mit "Testquittung der Testergebnisse" die digital signierte Testquittung ein. Für die Signatur laden Sie unter "Zertifikat" ein Zertifikat im Format .pfx mit privatem Schlüssel hoch und geben im Feld "Certificat password" das zugehörige Passwort ein.

Mit "Testquittung validieren" laden Sie die XML-Datei einer Testquittung hoch, und OpenOlat prüft, ob die Testquittung gültig ist.

![e-Assessment, Test und Tab QTI hell, gerahmt Testquittung der Testergebnisse, Zertifikat und Certificat password: Hier schalten Sie die signierte Testquittung ein](assets/e-assessment_test_tab_QTI_v2_de.png){ class="shadow lightbox" title="Tab QTI auf der Seite Test · 2026.11.18" }

[Zum Seitenanfang ^](#test)

---

## Tab Korrektur  {: #tab_correction}

Systemadministrator:innen legen mit "Anonym" unter "Korrekturwerkzeug" fest, ob das Korrekturwerkzeug für anonyme Korrekturen eingerichtet ist.

Unter "Freigabe Bewertung" legen sie ausserdem fest, ob eine Bewertung nach der manuellen Korrektur freigegeben ist und Teilnehmer:innen sie einsehen können: "Nicht freigegeben" oder "Freigegeben". Diese Einstellung ist die Vorgabe für den Kursbaustein Test; im Kursbaustein lässt sie sich unter "Freigabe Bewertung" für den einzelnen Test ändern.

![Tab Korrektur hell, gerahmt Korrekturwerkzeug mit Anonym und Freigabe Bewertung mit Nicht freigegeben und Freigegeben: Hier legen Sie die anonyme Korrektur und die Freigabe der Bewertung fest](assets/e-assessment_test_tab_correction_v2_de.png){ class="shadow lightbox" title="Tab Korrektur auf der Seite Test · 2026.11.18" }


[Zum Seitenanfang ^](#test)

---

## Tab Korrektur-Workflow  {: #tab_correction-workflow}

Tests können auch Korrektor:innen korrigieren, die nicht Mitglied des Kurses sind. Sie sind in OpenOlat registriert, gehören aber nicht zum Kurs. Für sie steht der Korrektur-Workflow zur Verfügung, sobald Sie hier "Korrektur-Workflow einschalten" anhaken.

Mit dem Korrektur-Workflow erstellen Sie persönliche Korrekturaufträge und weisen sie festgelegten Korrektor:innen zu. Steht die Korrektur eines Tests auf "Manuell durch Korrektor:innen", korrigieren Betreuer:innen ihn nicht mehr über das Bewertungswerkzeug im Kurs. Wie Sie den Korrektur-Workflow für einen Test einrichten, beschreibt [Test: Korrektur-Workflow](../../manual_user/learningresources/Test_correction_workflow.de.md).

Für das Management der Korrekturen durch mehrere verschiedene Korrektor:innen benötigt es E-Mails zur Kommunikation. Unter "E-Mail Vorlagen" formulieren Sie die Mails an die verschiedenen Beteiligten vor, mit "Übersetzen" auch in weiteren Sprachen.

Unter "Sichtbarkeit Korrektur echte Minuten" legen Sie fest, welche Rollen die tatsächlich aufgewendete Korrekturzeit sehen: Administrator:in, Lernressourcenverwalter:in, Autor:in und Korrektor:in.


![Tab Korrektur-Workflow hell, gerahmt Korrektur-Workflow einschalten, Sichtbarkeit Korrektur echte Minuten und die E-Mail Vorlagen: Hier schalten Sie den Workflow ein und passen die Mails an](assets/e-assessment_test_tab_correction_workflow_v2_de.png){ class="shadow lightbox" title="Tab Korrektur-Workflow auf der Seite Test · 2026.11.18" }


[Zum Seitenanfang ^](#test)

---

## Tab Prüfungsexport [:octicons-tag-16:{ title="ab Release 16.1 (OO-5648)" }](https://track.frentix.com/issue/OO-5648) {: #tab_tests_export}

Werden OpenOlat-Prüfungen als handschriftliche Prüfungen ausgegeben, kann eine zusätzliche Seite angehängt werden. Den Text dieser Seite legen Sie hier unter "Zusätzliche Seite" mit "Bearbeiten" fest. Wie Autor:innen einen Test als handschriftliche Prüfung exportieren, beschreibt [Test: Handschriftliche Prüfungen generieren](../../manual_user/learningresources/Test_handwritten_exams.de.md).

![Tab Prüfungsexport hell, gerahmt Zusätzliche Seite mit Bearbeiten: Hier legen Sie den Text der angehängten Seite fest](assets/e-assessment_test_tab_tests_export_v2_de.png){ class="shadow lightbox" title="Tab Prüfungsexport auf der Seite Test · 2026.11.18" }


[Zum Seitenanfang ^](#test)

---

## Weiterführende Informationen {: #further_information}

[Test: Korrektur-Workflow >](../../manual_user/learningresources/Test_correction_workflow.de.md)<br>
[Test: Handschriftliche Prüfungen generieren >](../../manual_user/learningresources/Test_handwritten_exams.de.md)<br>
[Bewertungswerkzeug - Übersicht >](../../manual_user/learningresources/Assessment_tool_overview/index.de.md)<br>
[Coaching - Übersicht >](../../manual_user/area_modules/Coaching/index.de.md)<br>
[Test: Einstellungen >](../../manual_user/learningresources/Test_settings.de.md)

[Zum Seitenanfang ^](#test)
