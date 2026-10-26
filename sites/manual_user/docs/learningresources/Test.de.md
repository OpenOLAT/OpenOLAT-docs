# Tests erstellen {: #create_tests}


Dieses Kapitel erklärt, wie Autor:innen in OpenOlat Tests erstellen, welche Fragetypen zur Verfügung stehen und welche Einstellungen bereitstehen. Darüber hinaus erfahren Sie, wie Sie Tests und Selbsttests in Kurse einbinden und nutzen und wie Sie Testergebnisse auswerten und bereitstellen.

OpenOlat Tests liegen in dem standardisierten Dokumentformat QTI 2.1 vor. QTI steht für "Question & Test Interoperability" und ist ein definiertes, standardisiertes Datenformat, das zur Konzipierung von Online-Tests verwendet wird. Der Vorteil ist, dass diese standardisierten Tests in diversen LMS und anderen Systemen, die den Standard unterstützen, genutzt werden können. [IMS](http://www.imsglobal.org/ "IMS") bemüht sich um die Entwicklung derartiger offener Standards für den E-Learning-Bereich.

In OpenOlat gehören Tests zu den "Lernressourcen". Lernressourcen werden separat erstellt und lassen sich in Online-Kurse integrieren. So kann z.B. dieselbe Lernressource "Test (QTI 2.1)" in mehreren Kursen verwendet werden.

[Zum Seitenanfang ^](#create_tests)

---


## Was ist ein Test? {: #definition_test}

Tests werden zur Leistungskontrolle, zur Überprüfung des aktuellen Wissensstandes oder auch als Online-Klausur verwendet. Sie können zu Beginn, während oder am Ende eines Kurses oder auch unabhängig von Kursen eingesetzt werden.

Bei formativen Tests geht es darum, einen Lernzwischenstand zu erfassen und basierend auf automatisierten oder manuellen Feedbacks eine lernbegleitende Verbesserung zu erreichen.  

Summative Tests werden erst am Ende eines Lernprozesses bzw. einer Veranstaltung eingesetzt. Dabei wird geprüft ob die geplanten Lernziele erreicht wurden. Ein Beispiel dafür sind scharfe Prüfungen bzw. Online-Klausuren.

Tests werden mit dem [OpenOlat-Testeditor](Test_editor_QTI_2.1.de.md) als QTI 2.1 Test erstellt. Dabei können die Länge des Tests, die [Fragetypen](Test_question_types.de.md) und eine Reihe von weiteren Konfigurationen bestimmt werden.

Teilnehmende können im Quellcode des Tests oder Selbsttests nicht nachlesen, welche Lösungen richtig und welche falsch sind, da die Antworten an den OpenOlat-Server geschickt und erst dort ausgewertet werden.

Wenn Sie einen Test in Ihrem Kurs einbinden, entscheiden Sie, ob Sie ihn als Selbsttest, also zu Übungszwecken, oder als Prüfungstest ("scharfer" Test) einsetzen. Im ersten Fall verwenden Sie bei der Einbindung des Tests in den Kurs den Kursbaustein "Selbsttest", im zweiten Fall den Kursbaustein "Test". Selbsttestresultate werden anonymisiert, Prüfungstestresultate personalisiert gespeichert. Bei Selbsttests sehen Betreuer:innen nicht, welche Resultate einzelne Teilnehmende erzielt haben.

Je nach Lehrszenario ist es aber sinnvoll, auch für Übungszwecke normale "Tests" und keine "Selbsttests" zu verwenden, nämlich immer dann, wenn Betreuer:innen wissen möchten, wie sich einzelne Teilnehmende entwickeln, oder wenn es darum geht, schwächere Kursmitglieder zu erkennen und gezielt zu unterstützen. Insofern sollte immer individuell geprüft werden, welcher Baustein der jeweils passende ist.

[Zum Seitenanfang ^](#create_tests)

---


## Wie kommen die Fragen in einen Test? {: #create_questions_in_tests}

Fragen können entweder direkt in der Lernressource Test erstellt werden oder im [Fragenpool](../area_modules/Question_Bank.de.md) erstellt und dann in den Test eingebunden werden. Im Kapitel [Wie gehe ich vor, wenn ich einen Test erstelle?](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md) erfahren Sie wie Sie einen Test erstellen können.

Beim Importieren einer Frage aus dem Fragenpool in einen Test wird eine Kopie der Frage zum jeweiligen Zeitpunkt angefertigt. Die Frage im Test ist somit unabhängig von der Original-Frage im Fragenpool. Wird die Original-Frage im Fragenpool modifiziert, wirkt sich das nicht auf die importierte Frage im Test aus. Diese bleibt unverändert.

Die in Tests importierten Fragen aus dem Fragenpool können im Editor nicht bearbeitet werden!

Soll eine Frage bearbeitet werden, kann über "Kopie erstellen und bearbeiten" eine Kopie der Frage erstellt und die Bearbeitung ermöglicht werden. Die Frage bekommt dann eine neue eigene ID. Über die "Master ID" gelangen Sie jedoch weiterhin zur ursprünglich importierten Original-Frage im Fragenpool.

Möglicherweise haben Sie bereits eine Testdatei im IMS-QTI-Format aus einem anderen LMS exportiert und möchten diese in OpenOlat importieren. Wie Sie dabei vorgehen, beschreibt der Abschnitt [Lernressourcen importieren](../area_modules/authoring_new_course.de.md#lernressourcen-importieren).

!!! info "Wichtig"

    Beim Import wird die Testdatei auf ein gültiges QTI-2.1-Paket geprüft. Fehlerhaft erzeugte Pakete, zum Beispiel aus externen Tools, werden mit einer Fehlermeldung abgelehnt. [:octicons-tag-16:{ title="ab Release 20.3.2 (OO-9454)" }](https://track.frentix.com/issue/OO-9454)

[Zum Seitenanfang ^](#create_tests)

---


## Weiterführende Informationen {: #further_information}

[Von QTI 1.2 zu QTI 2.1 >](Changing_from_QTI_1.2_to_QTI_2.1.de.md)<br>
[Wie gehe ich vor, wenn ich einen Test erstelle? >](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md)<br>
[Testeditor >](Test_editor_QTI_2.1.de.md)<br>
[Test Fragetypen >](Test_question_types.de.md)<br>
[Testfragen konfigurieren >](Configure_test_questions.de.md)<br>
[Test konfigurieren >](Configure_tests.de.md)<br>
[Test Einstellungen - Administration >](Test_settings.de.md)<br>
[Tests auf Kursebene >](Tests_at_course_level.de.md)<br>
[Tests exportieren >](Test_export.de.md)

[Zum Seitenanfang ^](#create_tests)