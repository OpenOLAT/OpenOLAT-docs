# Kurseinstellungen - Tab Durchführung {: #tab_execution}

![course_settings_execution1_v1_de.png](assets/course_settings_execution1_v1_de.png){ class="shadow lightbox"}


## Einstellungen zur Durchführung {: #config_execution}

**Durchführungszeitraum**

Hier kann gewählt werden, ob der Kurs mit einem konkreten Beginn- und Enddatum versehen wird. 

Ein gewählter Durchführungszeitraum wird in der  Kursinfo angezeigt. Diese Einstellung ist  nicht zu verwechseln mit dem Kursstatus und hat auch keine Auswirkungen auf die Sichtbarkeit oder den Zugang der Kursmitglieder. 

Folgendes sollte man allerdings beachten: 

Wird „mit Beginn- und Enddatum“ gewählt, gelten die hier eingetragenen Daten auch für verschiedene zeitabhängige Funktionen im Kurs, zum Beispiel für Erinnerungen oder im Aufgabenbaustein beim automatischen Einziehen von Aufgaben. 

Das Enddatum des Durchführungszeitraums wird auch für den Kurs-Lebenszyklus verwendet. Welche genauen Konsequenzen damit verbunden sind legen die OpenOlat Administrator:innen fest. Z.B. könnte der Kurs 2 Tage nach dem Endtermin auf "beendet" gesetzt und/oder der Kurs 4 Wochen nach dem Termin gelöscht werden. Erkundigen Sie sich am besten, welche Einstellungen in Ihrer OpenOlat Instanz für den Kurs-Lebenszyklus gelten. 

In herkömmlichen Kursen wird bei der Berechnung von „Bestanden“ berücksichtigt, ob das Ergebnis innerhalb des Durchführungszeitraums erreicht wurde. Wird kein „Bestanden“ bis zum Enddatum erzielt, erscheint automatisch „Nicht bestanden“.


**Durchführungsort**<br>
Die Eingabe in dieses Textfeld wird in der Kursinfo angezeigt.

[Zum Seitenanfang ^](#tab_execution)

---


## Konfiguration Termin- und Absenzenverwaltung im Kurs {: #config_event_and_absence_management}

**Termin- und Absenzenverwaltung einschalten**<br>
Wird hier für den aktuellen Kurs das Termin- und Absenzenmanagement eingeschaltet und es werden weitere Konfigurationsmöglichkeiten angezeigt. 

Darüber hinaus erscheint anschliessend das Menü "Termine und Absenzen" unter der (Kurs-)Administration. Als **Kursbesitzer:in** können Sie dort nach Fertigstellung der Konfiguration (zur Laufzeit) Termine und Absenzen erfassen.<br>

!!! tip "Hinweis"

    Im Unterschied zu Besitzer:innen finden **Betreuer:innen** das Tool zum Erfassen in der Werkzeugleiste.<br>
    **Teilnehmer:innen** finden ihre Absenzen im [persönlichen Menü](../personal_menu/Absences.de.md).


**Standard-Konfiguration überschreiben zulassen**<br>
Ist das Überschreiben nicht zugelassen, wird die Voreinstellung des/der Administrator:in angewendet.
Die nachstehenden Checkboxen und Eingabefelder bleiben inaktiv und zeigen den voreingestellten Wert an.

Wird das Überschreiben zugelassen, sind die nachfolgenden Checkboxen und Eingabefelder editierbar und es kann spezifisch für diesen Kurs eine Konfiguration der Termin- und Absenzenverwaltung vorgenommen werden.

**Anwesenheitskontrolle einschalten**<br>
Wird die Anwesenheitskontrolle eingeschaltet, stehen als weitere Konfigurationsoptionen **"Anwesenheitsquote berechnen"** und **"Absenzenquote global in %"** zur Verfügung.

**Anwesenheitsquote berechnen**<br>
Die Anwesenheitsquote wird berechnet aus Terminen mit mehreren Einheiten und den Absenzen.

**Beispiel:**<br>
Ein Termin besteht aus 10 Einheiten. An einer der Einheiten war der/die Teilnehmer:in abwesend.<br>
=> Es ergibt sich eine Anwesenheitsquote von 90%.

**Absenzenquote global in %**<br>
Über alle Termine des aktuellen Kurses hinweg wird bei allen Teilnehmer:innen eine globale Anwesenheitsquote errechnet und im persönlichen Menü unter dem Punkt "Absenzen" angezeigt. 
Die hier angegebene globale Absenzquote wird für die Beurteilung der Anwesenheitsquote verwendet.

**Dozentenkalender synchronisieren**<br>
Ist die Option gewählt, werden Kurs-Termine bei den Dozenten in ihren persönlichen Kalender eingetragen. (Bei den Terminen handelt es sich um Termine mit der Möglichkeit zum Erfassen einer Absenz.)

**Kurskalender synchronisieren**<br>
Ist die Option gewählt, werden Termine im Kurskalender eingetragen. Ist die Option nicht gewählt, sind nur noch die einfachen Termine im Kurskalender aufgeführt, die Termine mit der Möglichkeit zum Erfassen einer Absenz nicht mehr.

**Prüfungsmodus für Termine erlauben**<br>
Ist die Option eingeschaltet, kann man bei Terminen im 3-Punkte-Menü eine Option "Als Prüfung markieren" wählen. Dadurch wird dann ein Prüfungsmodus erstellt.

**Vorlaufzeit**<br>
Die Vorlaufzeit bezieht sich auf "Prüfungsmodus für Termine erlauben".<br>
Wenn Betreuer:innen oder Besitzer:innen einen Termin "als Prüfung markieren", wird ein Prüfungsmodus mit dieser Vorgabe erstellt. (Alle so erstellen Prüfungsmodi des Kurses haben die gleiche Vorlaufzeit.)

**Nachlaufzeit**<br>
Die Nachlaufzeit bezieht sich auf "Prüfungsmodus für Termine erlauben".<br>
Wenn Betreuer:innen oder Besitzer:innen einen Termin als "als Prüfung markieren", wird ein Prüfungsmodus mit dieser Vorgabe erstellt. (Alle so erstellen Prüfungsmodi des Kurses haben die gleiche Nachlaufzeit.)

**Erlaubte IP-Adressen**<br>
Auch diese Angabe bezieht sich auf "Prüfungsmodus für Termine erlauben".

**Safe Exam Browser Key**<br>
Hier kann der Safe Exam Browser Key hinterlegt werden, sofern das Tool verwendet wird. 


[Zum Seitenanfang ^](#tab_execution)

---


## Zugriff Kursbausteine {: #access_course_elements}

**Typ**<br>
Zur Information wird hier angezeigt, ob der aktuelle Kurs ein Lernpfadkurs oder ein herkömmlicher (klassischer) Kurs ist. 

Herkömmliche Kurse können an dieser Stelle in einen Lernpfad-Kurs konvertiert werden. 

**Lernfortschritt berechnen**

Für Lernpfad Kurse kann definiert werden ob der angezeigte Kursfortschritt anhand der Anzahl der obligatorischen Kursbausteine oder anhand der Bearbeitungszeit der obligatorischen Kursbausteine berechnet wird. Wird die Bearbeitungszeit gewählt müssen alle obligatorischen Kursbausteine im Kurseditor mit entsprechenden Zeiten versehen werden. 
Freiwillige Kursbausteine werden nicht berücksichtigt.

Herkömmliche Kurse verfügen nicht über die Option "Lernfortschritt".


[Zum Seitenanfang ^](#tab_execution)

---


## Weiterführende Informationen {: #further_information}

[Basiskonzept Termine und Absenzen >](../basic_concepts/Events_and_Absences.de.md)<br>
[Aktivierung und Konfiguration des Absenzenmanagements durch Administrator:innen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Erfassung und Verwaltung der Absenzen in einem Kurs durch Kursbesitzer:innen >](../learningresources/Events_and_absences.de.md)<br>
[Erfassung und Verwaltung der Absenzen in einem Kurs durch Betreuer:innen >](../learningresources/Toolbar_Events.de.md)<br>
[Persönliche Absenzen >](../personal_menu/Absences.de.md)<br>
[Kursübergreifende Absenzenerfassung im Coachingtool >](../area_modules/Coaching.de.md)<br>
[Kursübergreifende Absenzenverwaltung durch Absenzenverwalter:innen>](../area_modules/Absence_Management.de.md)<br>

[Zum Seitenanfang ^](#tab_execution)

