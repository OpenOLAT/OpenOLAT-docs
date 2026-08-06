# Kurseinstellungen - Tab Durchführung {: #tab_execution}

Kurse verfügen, im Gegensatz zu anderen Lernressourcen, im Menü "Einstellungen" noch über den Tab "Durchführung".

![course_settings_execution1_v2_de.png](assets/course_settings_execution1_v2_de.png){ class="shadow lightbox"}


## Einstellungen zur Durchführung {: #config_execution}

![1_green_24.png](assets/1_green_24.png) **Durchführungszeitraum**

Bei Lernressourcen vom Typ "Kurs" kann ein Durchführungszeitraum festgelegt werden. Folgende Optionen sind möglich:

* _Ohne_: Wählen Sie diese Option, wenn der Kurs nicht zu einem bestimmten Daten beginnt und aufhört oder Sie den Termin nicht explizit in den Informationen einbauen möchten.

* _Mit Beginn- und Enddatum_: Der Kursbesitzer kann hier das Start- und Enddatum des Kurses eintragen. Dabei ist beim Enddatum der Endtag miteingeschlossen (23:59).

* _Zeitabschnitt_: Bei Wahl dieser Option werden Ihnen vordefiniert Zeitabschnitte, wie z.B. Semester, zur Auswahl angeboten. Siehe Punkt 2.

Ein gewählter Durchführungszeitraum wird in der Kursinfo angezeigt. 

!!! info "Wichtig"

    Diese Einstellung ist nicht zu verwechseln mit dem Kursstatus und hat auch keine Auswirkungen auf die Sichtbarkeit oder den Zugang der Kursmitglieder. 

Folgendes sollte man allerdings beachten: 

Wird "mit Beginn- und Enddatum" gewählt, gelten die hier eingetragenen Daten auch für verschiedene zeitabhängige Funktionen im Kurs, zum Beispiel für Erinnerungen oder im Aufgabenbaustein beim automatischen Einziehen von Aufgaben. 

Das Enddatum des Durchführungszeitraums wird auch für den Kurs-Lebenszyklus verwendet. Welche genauen Konsequenzen damit verbunden sind, legen die OpenOlat-Administrator:innen fest. Z.B. könnte der Kurs 2 Tage nach dem Endtermin auf "beendet" gesetzt und/oder der Kurs 4 Wochen nach dem Termin gelöscht werden. Erkundigen Sie sich am besten, welche Einstellungen in Ihrer OpenOlat-Instanz für den Kurs-Lebenszyklus gelten. 

In herkömmlichen Kursen wird bei der Berechnung von "Bestanden" berücksichtigt, ob das Ergebnis innerhalb des Durchführungszeitraums erreicht wurde. Wird kein "Bestanden" bis zum Enddatum erzielt, erscheint automatisch "Nicht bestanden".

!!! note "Hinweis"

    Beim Einsatz des automatischen Lebenszyklus wird der Kursstatus durch das Enddatum gesteuert.


![2_green_24.png](assets/2_green_24.png) **Zeitabschnitt**<br>
Wenn auf Systemebene vom OpenOlat Administrator Zeitabschnitte (z.B. Semester) konfiguriert wurden, kann bei gewähltem Durchführungszeitraum "Zeitabschnitt" hier eine der vordefinierten Optionen ausgewählt werden. Der Zeitabschnitt erscheint anschliessend als Information in der Kursübersicht. Der Zeitabschnitt ist jedoch unabhängig vom Kursstatus und den Kurszugangsrechten (siehe Kapitel ["Zugangskonfiguration"](../learningresources/Access_configuration.de.md)). Er hat also keine Auswirkung auf die Sichtbarkeit und den Zugang für die Kursmitglieder.


![3_green_24.png](assets/3_green_24.png) **Durchführungsort**<br>
Der Ort, an dem ein Kurs bzw. eine Lernressource durchgeführt wird. Dieser Punkt ist vor allem bei Blended Learning Angeboten sinnvoll. Bei einer reinen online Nutzung kann das Feld auch frei bleiben. Alternativ kann hier "online" oder "Internet" eingetragen werden. 
Die Eingabe in diesem Textfeld wird in der Kursinfo angezeigt.

[Zum Seitenanfang ^](#tab_execution)

---


## Konfiguration Termin- und Absenzenverwaltung im Kurs {: #config_event_and_absence_management}

![4_green_24.png](assets/4_green_24.png) **Termin- und Absenzenverwaltung einschalten**<br>
Diese Option steht zur Verfügung, wenn das Modul "Termine und Absenzen" [systemweit aktiviert](../../manual_admin/administration/Modules_Events_and_Absences.de.md) ist. Ohne aktiviertes Modul erscheint der gesamte Abschnitt (Punkte 4 bis 15) im Tab "Durchführung" nicht.

Wird hier für den aktuellen Kurs das Termin- und Absenzenmanagement eingeschaltet, werden die Punkte 5 bis 11 zur weiteren Konfiguration angezeigt, bei erlaubtem Prüfungsmodus zusätzlich die Punkte 12 bis 15. 

Darüber hinaus erscheint anschliessend das Menü "Termine und Absenzen" unter der (Kurs-)Administration. Als **Kursbesitzer:in** können Sie dort nach Fertigstellung der Konfiguration (zur Laufzeit) Termine und Absenzen erfassen.<br>

!!! note "Hinweis"

    Im Unterschied zu Besitzer:innen finden **Betreuer:innen** das Tool zum Erfassen in der Werkzeugleiste.<br>
    **Teilnehmer:innen** finden ihre Absenzen im [persönlichen Menü](../personal_menu/Absences.de.md).


![5_green_24.png](assets/5_green_24.png) **Standard-Konfiguration überschreiben zulassen**<br>
Wird das Überschreiben zugelassen, sind die nachfolgenden Checkboxen und Eingabefelder editierbar und es kann spezifisch für diesen Kurs eine Konfiguration der Termin- und Absenzenverwaltung vorgenommen werden.

Ist das Überschreiben nicht zugelassen, wird die Voreinstellung des/der Administrator:in angewendet. Die nachstehenden Checkboxen und Eingabefelder bleiben inaktiv und zeigen den voreingestellten Wert an. Die dort voreingestellten Funktionen sind im Kurs dennoch wirksam.

Ob das Überschreiben im Kurs aktiviert werden kann, steuert die Administration mit der Einstellung "Überschreiben der Standard-Konfiguration zulassen".

![6_green_24.png](assets/6_green_24.png) **Anwesenheitskontrolle einschalten**<br>
Wird die Anwesenheitskontrolle eingeschaltet, stehen als weitere Konfigurationsoptionen **"Anwesenheitsquote berechnen"** und **"Absenzenquote global in %"** zur Verfügung.

![7_green_24.png](assets/7_green_24.png) **Anwesenheitsquote berechnen**<br>
Die Anwesenheitsquote wird berechnet aus Terminen mit mehreren Einheiten und den Absenzen.

**Beispiel:**<br>
Ein Termin besteht aus 10 Einheiten. An einer der Einheiten war der/die Teilnehmer:in abwesend.<br>
=> Es ergibt sich eine Anwesenheitsquote von 90%.

![8_green_24.png](assets/8_green_24.png) **Absenzenquote global in %**<br>
Über alle Termine des aktuellen Kurses hinweg wird bei allen Teilnehmer:innen eine globale Anwesenheitsquote errechnet und im persönlichen Menü unter dem Punkt "Absenzen" angezeigt. 
Die hier angegebene globale Absenzquote wird für die Beurteilung der Anwesenheitsquote verwendet.

![9_green_24.png](assets/9_green_24.png) **Dozentenkalender synchronisieren**<br>
Ist die Option gewählt, werden Kurs-Termine bei den Dozenten in ihren persönlichen Kalender eingetragen. (Bei den Terminen handelt es sich um Termine mit der Möglichkeit zum Erfassen einer Absenz.)

![10_green_24.png](assets/10_green_24.png) **Kurskalender synchronisieren**<br>
Ist die Option gewählt, werden Termine im Kurskalender eingetragen. Ist die Option nicht gewählt, sind nur noch die einfachen Termine im Kurskalender aufgeführt, die Termine mit der Möglichkeit zum Erfassen einer Absenz nicht mehr.

![11_green_24.png](assets/11_green_24.png) **Prüfungsmodus für Termine erlauben**<br>
Ist der Prüfungsmodus für Termine erlaubt, kann man bei Terminen im 3-Punkte-Menü die Option "Als Prüfung markieren" wählen. Dadurch wird ein Prüfungsmodus erstellt. Ausserdem werden die nachfolgenden Punkte 12 bis 15 mit den kursweiten Vorgabewerten für diese Prüfungsmodi angezeigt. Die Vorgabewerte werden beim Markieren übernommen; bereits erstellte Prüfungsmodi bleiben bei späteren Änderungen unverändert.

Zum Ändern dieser Einstellung im Kurs ist die Option "Standard-Konfiguration überschreiben zulassen" nötig. Ist das Überschreiben nicht zugelassen und der Prüfungsmodus in der Administration erlaubt, erscheint dieses Feld angehakt und inaktiv, und "Als Prüfung markieren" arbeitet mit den Vorgabewerten der Administration.

![12_green_24.png](assets/12_green_24.png) **Vorlaufzeit**<br>
Die Vorlaufzeit bezieht sich auf "Prüfungsmodus für Termine erlauben".<br>
Wenn Betreuer:innen oder Besitzer:innen einen Termin "als Prüfung markieren", wird ein Prüfungsmodus mit dieser Vorgabe erstellt. (Alle so erstellten Prüfungsmodi des Kurses haben die gleiche Vorlaufzeit.)

![13_green_24.png](assets/13_green_24.png) **Nachlaufzeit**<br>
Die Nachlaufzeit bezieht sich auf "Prüfungsmodus für Termine erlauben".<br>
Wenn Betreuer:innen oder Besitzer:innen einen Termin "als Prüfung markieren", wird ein Prüfungsmodus mit dieser Vorgabe erstellt. (Alle so erstellten Prüfungsmodi des Kurses haben die gleiche Nachlaufzeit.)

![14_green_24.png](assets/14_green_24.png) **Erlaubte IP-Adressen**<br>
Auch diese Angabe bezieht sich auf "Prüfungsmodus für Termine erlauben".<br>
Die hier erfassten IP-Adressen werden in den Prüfungsmodus übernommen, wenn ein Termin "als Prüfung markiert" wird.

![15_green_24.png](assets/15_green_24.png) **Safe Exam Browser Key**<br>
Dieses Feld ist der kursweite Vorgabewert für die Variante "SEB mit manuellen Keys". Der hinterlegte Key wird übernommen, wenn ein Termin "als Prüfung markiert" und die Prüfung mit dem Safe Exam Browser abgesichert wird. Im Prüfungsmodus des Termins wird der Key zur Information angezeigt und dort nicht bearbeitet.

Das Feld erscheint nur, wenn die Administration bei "Safe Exam Browser - Art der Benutzung" die Variante "SEB mit manuellen Keys" gewählt hat. Sie finden die Einstellung unter:<br>
`Administration > Module > Termine / Absenzen`, Tab "Konfiguration".

Bleibt das Feld bei zugelassenem Überschreiben leer, erhalten die Prüfungsmodi dieses Kurses keinen Key; der Key aus der Administration wird in diesem Fall nicht verwendet.

Ist "SEB-Config (empfohlen)" aktiv, wird der Safe Exam Browser pro Prüfung über [Konfigurationsvorlagen](../learningresources/Assessment_mode.de.md) konfiguriert und dieses Feld wird nicht angezeigt. Beim Markieren als Prüfung steht im Prüfungsmodus des Termins das Feld "Konfiguration" mit den aktiven Vorlagen zur Verfügung, wobei die Standardvorlage vorausgewählt ist. Ob die Konfigurationsdatei heruntergeladen werden kann, legt in diesem Fall die Administration fest.

Prüfungsmodi, die direkt über die [Prüfungsverwaltung](../learningresources/Assessment_mode.de.md) erstellt werden, verwenden diesen kursweiten Key nicht. Dort wird die SEB-Variante pro Prüfungsmodus über "Typ von Anwendung" gewählt.

[Zum Seitenanfang ^](#tab_execution)

---


## Zugriff Kursbausteine {: #access_course_elements}

![16_green_24.png](assets/16_green_24.png) **Typ**<br>
Zur Information wird hier angezeigt, ob der aktuelle Kurs ein Lernpfadkurs oder ein herkömmlicher (klassischer) Kurs ist. 

Herkömmliche Kurse können an dieser Stelle in einen Lernpfad-Kurs konvertiert werden. 

![17_green_24.png](assets/17_green_24.png) **Lernfortschritt berechnen**

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
[Kursübergreifende Absenzenverwaltung durch Absenzenverwalter:innen >](../area_modules/Absence_Management.de.md)<br>

[Zum Seitenanfang ^](#tab_execution)




