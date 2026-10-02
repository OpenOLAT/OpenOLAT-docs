# Wie wechsle ich einen Test aus? {: #exchange_tests}

??? abstract "Ziel und Inhalt dieser Anleitung"

    Diese Anleitung zeigt Ihnen, wie Sie eine Test-Lernressource in einem Kursbaustein "Test" durch eine andere ersetzen und welche Vorbereitungen notwendig sind, wenn bereits Teilnehmer:innen den Test absolviert haben.

??? abstract "Zielgruppe"

    [x] Autor:innen [x] Betreuer:innen  [ ] Teilnehmer:innen

    [x] Anfänger:innen [x] Fortgeschrittene  [ ] Expert:innen


??? abstract "Erwartete Vorkenntnisse"

    * ["Wie erstelle ich meinen ersten OpenOlat-Kurs?"](../my_first_course/my_first_course.de.md)
    * ["Wie gehe ich vor, wenn ich einen Test erstelle?"](../test_creation_procedure/test_creation_procedure.de.md)
    * [Bewertungswerkzeug - Übersicht](../../manual_user/learningresources/Assessment_tool_overview.de.md)

---


## Was muss ich vor dem Austausch wissen? {: #situation}

Ein **Kursbaustein** "Test" referenziert immer eine Test-**Lernressource**. Beim Austausch wird diese Referenz auf eine andere Lernressource umgestellt. Die bisherige Test-Lernressource bleibt im System erhalten: Sie wird lediglich aus dem Kursbaustein ausgehängt und an ihrer Stelle eine neue Test-Lernressource eingebunden.

**Das zentrale Problem:** Wenn Teilnehmer:innen den Test bereits gestartet oder abgeschlossen haben, existieren Bewertungsdaten, die auf den Inhalt des alten Tests (Fragen, Punktzahlen) abgestimmt sind. Nach dem Austausch passen diese Daten möglicherweise nicht mehr zum neuen Test. Das kann zu Inkonsistenzen in der Bewertung führen.

**Beispiel:**<br>
Sie möchten in einem Test eine zusätzliche Frage einfügen. Teilnehmer:innen, die den Test noch vor dieser Bearbeitung absolviert haben, konnten die Frage gar nie sehen und Punkte für diese Frage erwerben. In einem bereits von Teilnehmer:innen abgegebenen Test die Fragen nachträglich zu ändern, ist Urkundenfälschung und darf keinesfalls passieren. Deshalb schränkt OpenOlat die Bearbeitung ein, sobald eine Test-Lernressource verwendet wird: Fragen lassen sich dann weder hinzufügen noch löschen, kopieren oder verschieben.

Als Faustregel gilt deshalb:

* **Noch kein/keine Teilnehmer:in hat den Test absolviert:** Ein Austausch ist unproblematisch, es sind keine Vorbereitungen notwendig.
* **Teilnehmer:innen haben den Test bereits absolviert:** Vor dem Austausch sorgfältig abwägen. Gegebenenfalls können Daten zurückgesetzt werden. Wenn eine Test-Lernressource ausgetauscht werden soll, gibt es in OpenOlat einen eigenen Prozess, der auch die Archivierung von Daten vor dem Austausch umfasst.

[Zum Seitenanfang ^](#exchange_tests)

---


## Wo nehme ich den Austausch vor? {: #exchange}

Der Austausch erfolgt im **Kurseditor**. Sie benötigen dafür die Rolle **Kursbesitzer:in** oder eine entsprechende Berechtigung zur Kursbearbeitung.

Den Kurseditor öffnen Sie über:<br>
`Kurs > Administration > Kurseditor > Kursbaustein "Test" > Tab "Test-Konfiguration"`

!!! tip "Voraussetzung"

    Die neue Test-Lernressource muss bereits im System vorhanden sein, selbst erstellt oder von einer anderen Person freigegeben. Alternativ importieren Sie sie beim Austausch als Testdatei. Neu erstellen lässt sich die Test-Lernressource beim Austausch nicht.


[Zum Seitenanfang ^](#exchange_tests)

---


## Schritt 1: Vorhandene Testdaten prüfen {: #check_existing_data}

Bevor Sie den Test austauschen, sollten Sie sich im **Bewertungswerkzeug** einen Überblick über die vorhandenen Testdaten verschaffen.

1. Öffnen Sie das Bewertungswerkzeug über `Kurs > Administration > Bewertungswerkzeug`.
2. Wählen Sie in der linken Seitenleiste den Kursbaustein "Test", dessen Test Sie austauschen möchten.
3. Wählen Sie den Button **Teilnehmer:innen**.
4. Prüfen Sie in der Tabelle, ob und wie viele Teilnehmer:innen den Test bereits gestartet oder abgeschlossen haben (Spalten **"Versuche"** und **"Status"**).

![Spalten Versuche und Status zeigen je Person, ob der Test nicht gestartet, gestartet oder schon zur Korrektur abgegeben ist](assets/exchange_tests_check_data_v1_de.png){ class="shadow lightbox" title="Teilnehmer:innen eines Tests im Bewertungswerkzeug" }

!!! info "Wichtig"

    Wenn in der Spalte "Versuche" für **alle** Teilnehmer:innen keine Versuche eingetragen sind und der Status **"Nicht gestartet"** ist, sind keine Vorbereitungen notwendig. Sie können direkt mit Schritt 3 fortfahren.


[Zum Seitenanfang ^](#exchange_tests)

---


## Schritt 2: Sollen alle Teilnehmer:innen den neuen Test nochmals machen müssen? {: #reset_data}

Auch wenn nur eine einzelne Person den Test "mal probehalber durchgeklickt" hat, gilt die Test-Lernressource bereits als "verwendet" und lässt sich nur noch eingeschränkt bearbeiten. OpenOlat kann nicht unterscheiden, ob der Testversuch ernst gemeint war oder nicht.

In einem solchen Fall setzen Sie die Daten der Teilnehmer:innen zurück, damit sie mit dem neuen Test von vorn beginnen. OpenOlat annulliert dabei die bisherigen Testläufe. Die Bearbeitung der Test-Lernressource selbst bleibt trotzdem eingeschränkt, weil die annullierten Testläufe erhalten bleiben.

Verwenden Sie dazu den Button **Daten zurücksetzen**. Sie können den Kursbaustein "Test" direkt im Kurs oder im Bewertungswerkzeug auswählen:<br>
`(Bewertungswerkzeug >) Kursbaustein "Test" wählen > Tab "Teilnehmer:innen" > Teilnehmer:innen selektieren > Button "Daten zurücksetzen"`

Daten zurücksetzen dürfen unter anderem Kursbesitzer:innen und Personen, denen im Kurs das Recht "Bewertungs-Werkzeug" zugewiesen ist. Betreuer:innen ohne dieses Recht sehen den Button nicht.

Sie können auch nur die Tests von bestimmten Personen zurücksetzen.

* Selektieren Sie dazu einen (oder auch mehrere oder alle) Namen in der Liste.
* Sobald mindestens ein Name markiert ist, erscheint über der Liste unter anderem auch ein Button "Daten zurücksetzen".
* Dieser setzt dann nur die Daten der selektierten Teilnehmer:innen zurück.

![Nach dem Markieren aller Teilnehmer:innen erscheint über der Liste der Button Daten zurücksetzen](assets/exchange_tests_reset_data_v1_de.png){ class="shadow lightbox" title="Tab Teilnehmer:innen im Kursbaustein Test" }

Je nach Kursbaustein werden folgende Daten zurückgesetzt, beziehungsweise annulliert:

* Fortschritt
* Anzahl Versuche
* Testdurchläufe
* Punkte und Erfolgsstatus
* Freigabe Bewertung
* Erinnerungen

!!! warning "Achtung"

    Das Zurücksetzen von Testdaten ist **nicht umkehrbar**. Beim Zurücksetzen wird eine entsprechende Archivdatei mit den relevanten Daten erstellt und im Anschluss heruntergeladen. Das Archiv steht zusätzlich als Download im Leistungsnachweis der Teilnehmenden zur Verfügung.

Mehr dazu finden Sie im Benutzerhandbuch unter:<br>
[Bewertungswerkzeug - Daten zurücksetzen >](../../manual_user/learningresources/Assessment_tool_reset_data.de.md)

[Zum Seitenanfang ^](#exchange_tests)

---

## Schritt 3: Lernressource austauschen {: #exchange_resource}

1. Öffnen Sie den Kurseditor und wählen Sie den betreffenden Kursbaustein "Test".
2. Wählen Sie den Tab "Test-Konfiguration". Wird die Test-Lernressource bereits verwendet, zeigt OpenOlat den Hinweis "Die Lernressource wird bereits für die Auswertung verwendet. Die Bearbeitung ist begrenzt."
3. Klicken Sie auf den Button "Ersetzen" und wählen Sie eine vorhandene Test-Lernressource. Über den Pfeil neben "Ersetzen" importieren Sie stattdessen eine Testdatei.

![Hinweis zur bereits verwendeten Lernressource und der Button Ersetzen mit dem Pfeil für den Import](assets/exchange_tests_exchange1_v1_de.png){ class="shadow lightbox" title="Tab Test-Konfiguration im Kurseditor" }

Lässt sich der Kursbaustein nicht publizieren, verweigert OpenOlat das Ersetzen mit der Meldung "Bevor die Test-Ressource ersetzt werden kann, muss der Kursbaustein publizierbar sein."

Ist der Kursbaustein bereits publiziert, öffnet OpenOlat den Dialog "Test ersetzen". Er stellt den aktuellen und den neuen Test gegenüber und bietet unter "Austauschoptionen" zwei Optionen:

* **Kontrollierter Austausch**
* **Nur ersetzen**

![Austauschoptionen mit ihren Auswirkungen, Vergleich der Eigenschaften beider Tests und Bestätigung vor dem Ersetzen](assets/exchange_tests_exchange2_v1_de.png){ class="shadow lightbox" title="Dialog Test ersetzen" }


|                   | Kontrollierter Austausch |  Nur ersetzen  |
| ----------------- | ------------------------ | ------------------------ |
| **Laufende und pausierte Testläufe:** | werden eingezogen und als ungültig markiert | werden eingezogen und als ungültig markiert |
| **Beendete Testläufe:** | werden als ungültig markiert | bleiben gültig |
| **Bestehende Bewertungen:** | werden gelöscht | bleiben unverändert |
| **Veröffentlichung:** | Um inkonsistente Testdaten zu vermeiden, wird der Kursbaustein sofort veröffentlicht | Um inkonsistente Testdaten zu vermeiden, wird der Kursbaustein sofort veröffentlicht   |

Beim kontrollierten Austausch erstellt OpenOlat zuerst eine Archivdatei mit den Daten des Kursbausteins und lädt sie herunter.

Unter "Eigenschaften der Test-Ressourcen" vergleicht der Dialog die beiden Tests, etwa die Fragetypen und die erreichbaren Punkte. Unterschiede kennzeichnet er in der Spalte "Meldung".

Aktivieren Sie zum Schluss das Kontrollkästchen "Ich verstehe die Auswirkungen und möchte den Test ersetzen." und klicken Sie auf "Ersetzen und publizieren".

[Zum Seitenanfang ^](#exchange_tests)

---


## Kurs publizieren {: #publish}

Nach Arbeiten im Kurseditor publizieren Sie einen Kurs normalerweise selbst und verlassen danach den Editor. Bis dahin können Sie gemachte Änderungen wieder verwerfen.

Beim Austausch über den Dialog "Test ersetzen" publiziert OpenOlat den Kursbaustein mit dem Button "Ersetzen und publizieren" sofort, damit keine Dateninkonsistenzen entstehen. Ein eigener Schritt "Publizieren" ist in diesem Fall nicht nötig.

Ist der Kursbaustein noch nie publiziert worden, ersetzt OpenOlat die Test-Lernressource ohne diesen Dialog. Publizieren Sie den Kurs dann wie gewohnt.

[Zum Seitenanfang ^](#exchange_tests)

---

## Checkliste {: #checklist}

- [x] Muss die Test-Lernressource zwingend ausgetauscht werden?
- [x] Könnte der Kurs/der Kursbaustein "Test" auch kopiert werden? (Damit wieder eine unbenutzte Lernressource vorliegt.)
- [x] Wurde die neue Test-Lernressource bereits im Autorenbereich angelegt?
- [x] Haben Teilnehmende bereits den vorherigen Test bearbeitet? Liegen Daten vor?
- [x] Könnten die Test-Daten zurückgesetzt werden?
- [x] Sollen vorhandene Test-Daten ganz gelöscht werden?
- [x] Wurde ein Archiv der bisher angefallenen Daten erstellt?
- [x] Wurde die Archivdatei an einem passenden Ort abgelegt?
- [x] Sollen die Kurs-Teilnehmer:innen über die neue Version des Tests informiert werden?

[Zum Seitenanfang ^](#exchange_tests)

---


## Weiterführende Informationen {: #further_information}

["Wie erstelle ich meinen ersten OpenOlat-Kurs?" >](../my_first_course/my_first_course.de.md)<br>
["Wie gehe ich vor, wenn ich einen Test erstelle?" >](../test_creation_procedure/test_creation_procedure.de.md)<br>
[Bewertungswerkzeug - Übersicht >](../../manual_user/learningresources/Assessment_tool_overview.de.md)<br>
[Bewertungswerkzeug - Daten zurücksetzen >](../../manual_user/learningresources/Assessment_tool_reset_data.de.md)<br>
[Tests erstellen >](../../manual_user/learningresources/Test.de.md)<br>
[Kursbaustein "Test" >](../../manual_user/learningresources/Course_Element_Test.de.md)<br>
["Wie bereite ich eine Online-Prüfung vor?" >](../exam_preparation/exam_preparation.de.md)

[Zum Seitenanfang ^](#exchange_tests)
