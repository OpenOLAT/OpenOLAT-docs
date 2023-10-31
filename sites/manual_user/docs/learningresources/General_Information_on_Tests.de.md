# Allgemeines zu Tests

OpenOlat Tests liegen in dem standardisierten Dokumentformat QTI 2.1 vor. QTI steht für „Question & Test Interoperability“ und ist ein definiertes, standardisiertes Datenformat, das zur Konzipierung von Online-Tests verwendet wird. Der Vorteil ist, dass diese standardisierten Tests in diversen LMS und anderen Systemen, die den Standard unterstützen, genutzt werden kann. [IMS](http://www.imsglobal.org/ "IMS") bemüht sich um die Entwicklung derartiger offener Standards für den E-Learning-Bereich.

In OpenOlat gehören Tests zu den "Lernressourcen". Lernressourcen werden separat erstellt und lassen sich in Online-Kurse integrieren. So kann z.B. dieselbe Lernressource "Test (QTI 2.1)" in mehreren Kursen verwendet werden.

## Was ist ein Test?

Tests werden zur Leistungskontrolle, zur Überprüfung des aktuellen Wissensstandes oder auch als Online-Klausur verwendet. Sie können zu Beginn, während oder am Ende eines Kurses oder auch unabhängig von Kursen eingesetzt werden.

Bei formativen Tests geht es darum, einen Lernzwischenstand zu erfassen und basierend auf automatisierten oder manuellen Feedbacks eine lernbegleitende Verbesserung zu erreichen.  

Summative Tests werden erst am Ende eines Lernprozesses bzw. einer Veranstaltung eingesetzt. Dabei wird geprüft ob die geplanten Lernziele erreicht wurden. Ein Beispiel dafür sind scharfe Prüfungen bzw. Online-Klausuren.

Tests werden mit dem [OpenOlat-Testeditor](Test_editor_QTI_2.1.de.md) als QTI 2.1 Test erstellt. Dabei können die Länge des Tests, die [Fragetypen](Test_question_types.de.md) und eine Reihe von weiteren Konfigurationen bestimmt werden.

Testpersonen können im Quellcode des Tests oder Selbsttests nicht nachlesen, welche Lösungen richtig und welche falsch sind, da die Antworten an den OpenOlat-Server geschickt und erst dort ausgewertet werden.

Wenn Sie einen Test in Ihrem [Kurs](Tests_at_course_level.de.md) einbinden, können Sie entscheiden, ob sie ihn als Selbsttest, also zu Übungszwecken, oder als Prüfungstest ("scharfer" Test) einsetzen wollen. Im ersten Fall verwenden Sie bei der Einbindung des Tests in den Kurs den Kursbaustein "Selbsttest", im zweiten Fall den Kursbaustein "Test". Selbsttestresultate werden anonymisiert, Prüfungstestresultate personalisiert gespeichert. Bei Selbsttests kann der Lehrende nicht nachvollziehen, welche Resultate ein bestimmter Lerner erzielt hat.

Je nach Lehrszenario macht es aber auch durchaus Sinn auch für Übungszwecke normale "Tests" und keine "Selbsttests" zu verwenden, nämlich immer dann, wenn die Lehrperson wissen möchte, wie sich einzelne Lernende entwickeln oder wenn es darum geht, schwächere Kursmitglieder zu erkennen und gezielt zu unterstützen. Insofern sollte immer individuell geprüft werden, welcher Baustein der jeweils passende ist.

## Wie kommen die Fragen in einen Test?

Fragen können entweder direkt in der Lernressource Test erstellt werden oder im [Fragenpool](../area_modules/Question_Bank.de.md) erstellt und dann in den Test eingebunden werden. Im Kapitel [Vier Schritte zu Ihrem Test oder Selbsttest](../../manual_how-to/test_creation_procedure/test_creation_procedure.de.md) erfahren Sie wie Sie einen Test erstellen können.

Beim Importieren einer Frage aus dem Fragenpool in einen Test wird eine Kopie der Frage zum jeweiligen Zeitpunkt angefertigt. Die Frage im Test ist somit unabhängig von der Original-Frage im Fragenpool. Wird die Original-Frage im Fragenpool modifiziert, wirkt sich das nicht auf die importierte Frage im Test aus. Diese bleibt unverändert.

Die in Tests importierten Fragen aus dem Fragenpool können im Editor nicht bearbeitet werden!

Soll eine Frage bearbeitet werden, kann über "Kopie erstellen und bearbeiten" eine Kopie der Frage erstellt und die Bearbeitung ermöglicht werden. Die Frage bekommt dann eine neue eigene ID. Über die Master-ID kann jedoch weiterhin auf die ursprünglich importierte Original-Frage im Fragenpool zugegriffen werden.

Möglicherweise haben Sie bereits eine Testdatei im IMS-QTI-Format aus einem anderen LMS exportiert und möchten diese in OpenOlat importieren. Im Kapitel „Aktionen im Autorenbereich“ steht unter dem Punkt [Importieren](../area_modules/authoring_new_course.de.md#lernressourcen-importieren), wie Sie vorgehen müssen.
