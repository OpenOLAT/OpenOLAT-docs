# Prüfungsverwaltung: Prüfungsmodus {: #Assessment_mode}

!!! note "Hinweis"

    Die Konfiguration des Prüfungsmodus finden Sie in der Prüfungsverwaltung des Kurses: `Kurs > Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"`.


## Was versteht man unter "Prüfungsmodus"? [:octicons-tag-16:{ title="ab Release 10.2 (OO-1349)" }](https://track.frentix.com/issue/OO-1349)

Ein Prüfungsmodus ist eine Prüfungskonfiguration, mit der Teilnehmende Tests und Prüfungen während einer festgelegten Zeit in einem geschützten Modus ablegen (sogenannter Kioskmodus).

Während dieser Zeit ist nur der Zugriff auf zuvor festgelegte Kursbausteine im betroffenen Kurs gestattet. Alle weiteren Funktionen in OpenOlat, wie andere Kurse, Gruppen, Notizen etc., werden während der Prüfungsdauer (Laufzeit des Prüfungsmodus) ausgeblendet. Nur ein Logout ist während der Prüfung möglich.

---


## Prüfungsmodus hinzufügen

Einen Prüfungsmodus erstellen und konfigurieren Sie in der Prüfungsverwaltung des Kurses:

1. Öffnen Sie den Kurs mit dem Test.
2. Wählen Sie `Kurs > Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"`.
3. Klicken Sie auf "Prüfungsmodus hinzufügen".

Für einen Termin des Kurses entsteht der Prüfungsmodus stattdessen in der Terminliste: [Prüfungsmodus aus einem Termin](#exam_from_event)

![Tab "Konfiguration Prüfungsmodus" und Button "Prüfungsmodus hinzufügen" markiert](assets/assessment_management_create_exam_setting_v2_de.png){ class="shadow lightbox" title="Seite Prüfungsverwaltung im Kurs" }

Im Tab "Konfiguration Prüfungsmodus" sehen Sie alle für einen Kurs bereits abgehaltenen, laufenden oder geplanten Prüfungen. Der Modus geplanter Prüfungen kann bis zur Prüfung noch bearbeitet werden, eine nachträgliche Bearbeitung ist nicht möglich. Die Übersicht enthält Informationen zu Datum und Dauer, Vor- und Nachlaufzeiten, sowie Benutzergruppen.

![Übersichtstabelle der Prüfungsmodi mit Status, Vorlauf- und Nachlaufzeit sowie Zielgruppe je Prüfung](assets/assessment_management_exam_settings_overview_v2_de.png){ class="shadow lightbox" title="Tab Konfiguration Prüfungsmodus" }

Sie erstellen einen Prüfungsmodus vor der Prüfung. Er enthält

* eine Start- und Endzeit,
* auf Wunsch Vor- und Nachlaufzeiten,
* auf Wunsch Einschränkungen auf bestimmte Nutzergruppen.

Ein Prüfungsmodus kann gelten

* nur für die Teilnehmenden des Kurses,
* nur für die Teilnehmenden ausgewählter Gruppen,
* nur für die Teilnehmenden ausgewählter Produkte des Course Planner, sofern das Modul Course Planner eingeschaltet ist,
* oder für die Teilnehmenden des Kurses und der ausgewählten Gruppen oder Produkte.

Dadurch ist es möglich, zeitgleich unterschiedlich konfigurierte Prüfungen für verschiedene Nutzergruppen desselben Kurses abzuhalten.

Neben der Benutzergruppe können Sie festlegen, ob und auf welche Kursbausteine der Zugriff eingeschränkt werden soll, und ob ein Kursbaustein davon als Startbaustein verwendet wird.<br>
Des Weiteren kann der Zugang zur Prüfung auf spezifische IP-Adressen beschränkt, oder die Nutzung des [Safe Exam Browsers](http://www.safeexambrowser.org) vorausgesetzt werden.

!!! tip "Tipp"

    Für den Prüfungsmodus wird bevorzugt ein herkömmlicher Kurs empfohlen. Wenn Sie einen Lernpfadkurs verwenden, müssen Sie sicherstellen, dass die betroffenen Kursbausteine zugänglich sind.

    Im herkömmlichen Kurs haben Sie ausserdem die Möglichkeit, beim Editieren eines Kursbausteins unter den Tabs "Sichtbarkeit" und "Zugang" die Option **"Nur im Prüfungsmodus"** zu wählen. Diese Option steht in Lernpfadkursen nicht zur Verfügung.

!!! info "Vor- und Nachlaufzeit auf 0 setzen"

    Beim Erstellen eines neuen Prüfungsmodus sind Vor- und Nachlaufzeit mit je 10 Minuten vorbelegt. Beide Felder sind Pflichtfelder. Dieser Vorschlagswert lässt sich pro Prüfungsmodus frei überschreiben: auch auf **0**, wenn OpenOlat vor bzw. nach der Prüfung nicht gesperrt werden soll. Ein globaler Standardwert ist nicht konfigurierbar; die 0 muss also in jeder Prüfungskonfiguration einzeln eingetragen werden.

---


## Tab "Allgemein"

![Tab "Allgemein" mit Feldern Titel, Beschreibung, Beginn, Vorlaufzeit, Ende, Nachlaufzeit und Art des Beginns/Endes](assets/assessment_management_create_exam_setting_tab_general_v1_de.png){ class="shadow lightbox" title="Dialog einer neuen Prüfung" }

Titel und Beschreibung sehen die Teilnehmenden in der Benachrichtigung zur Prüfung. Daneben legen Sie in diesem Tab fest:

**Beginn**: Legen Sie hier Datum und Uhrzeit für den Beginn der Prüfung fest.

Die **Vorlaufzeit**, die Sie in Minuten angeben, sperrt OpenOlat während der angegebenen Dauer vor Prüfungsbeginn.

**Ende**: Legen Sie hier Datum und Uhrzeit für das Ende der Prüfung fest.

Wird eine **Nachlaufzeit** in Minuten angegeben, bleibt OpenOlat während dieser Dauer im Anschluss an die Prüfung noch gesperrt.

Vorlaufzeit und Nachlaufzeit regeln, wie lange OpenOlat gesperrt ist, nicht wie lange der Test dauert. Wie Prüfungsmodus, Testzeitraum, Zeitbeschränkung und Verlängerung zusammenwirken, zeigt [Wie hängen die Zeiten einer Prüfung zusammen?](../../manual_how-to/exam_preparation/exam_preparation.de.md#exam_times)

**Art des Beginns/Endes**: Wählen Sie, ob die Prüfung "Automatisch" zur konfigurierten Zeit beginnt und endet oder "Manuell". Bei "Manuell" startet und beendet eine Person die Prüfung am Prüfungstag selbst. Wer das darf, beschreibt der Abschnitt [Wer eine Prüfung manuell starten und beenden kann](#start_stop_rights).

---


## Tab "Einschränkungen Kursbaustein"

![Tab "Einschränkungen Kursbaustein" mit Checkbox "Zugriff auf Kursbaustein einschränken" und Auswahl des Startbausteins](assets/assessment_management_create_exam_setting_tab_element_restriction_v1_de.png){ class="shadow lightbox" title="Dialog einer Prüfung" }

**Zugriff auf Kursbaustein einschränken**: Um die Prüfung auf ausgewählte Kursbausteine des betroffenen Kurses zu beschränken, wählen Sie hier die Checkbox aus, und klicken Sie dann auf die Schaltfläche "Kursbausteine auswählen". Es öffnet sich eine Liste aller Kursbausteine des Kurses. Wählen Sie die Kursbausteine aus, die den Teilnehmenden während der Prüfung angezeigt werden sollen. Alle anderen Kursbausteine werden für die Dauer der Prüfung ausgeblendet.

**Startbaustein**: Soll den Teilnehmenden ein bestimmter Kursbaustein direkt beim Start angezeigt werden, klicken Sie auf "Kursbaustein auswählen" und wählen einen der verfügbaren Kursbausteine aus. Es werden nur die Kursbausteine angezeigt, die im Schritt zuvor zur Anzeige ausgewählt wurden.

---


## Tab "Zugang"

![Tab "Zugang" mit IP-Einschränkung, den vier Teilnehmenden-Optionen und der Checkbox "Prüfungskonfiguration auch bei Betreuenden anwenden"](assets/assessment_management_create_exam_setting_tab_access_v1_de.png){ class="shadow lightbox" title="Tab Zugang im Dialog einer Prüfung" }

**Einschränkung auf IP-Adressen**: Um eine Ausführung der Prüfung nur an bestimmten Computern oder Orten zuzulassen, markieren Sie hier die Checkbox und tragen dann die zulässigen IP-Adressen ein. Diese sollten Sie von Ihrer Informatik-Abteilung erhalten können. Sie können dadurch z.B. verhindern, dass Teilnehmende eine Prüfung von zuhause ablegen.

**Teilnehmende**: Hier legen Sie fest, für welche Teilnehmenden die Prüfung gültig ist. Wählen Sie aus den folgenden Optionen aus:

* "Nur Kursteilnehmende"
* "Nur Gruppenteilnehmende"
* "Nur CPL Teilnehmende", sofern das Modul Course Planner eingeschaltet ist
* "Teilnehmer:innen des Kurses und der ausgewählten Gruppen", bei eingeschaltetem Course Planner "Teilnehmer:innen des Kurses und der ausgewählten Gruppen oder Produkten"

Sobald eine Option mit Gruppen ausgewählt wurde, müssen Sie zwingend immer über die Schaltflächen "Gruppen auswählen" oder "Lernbereiche auswählen" die betroffenen Gruppen auswählen. Gilt die Prüfung für Teilnehmende des Course Planner, wählen Sie die Produkte über die Schaltfläche "Produkt auswählen" aus.

**Prüfungskonfiguration auch bei Betreuenden anwenden**:
Ist diese Option gewählt, gilt der Prüfungsmodus auch für die Betreuer:innen der gewählten Teilnehmenden. Wie die Teilnehmenden erreichen sie während der Prüfung in OpenOlat nur noch die Prüfung. Soll eine Betreuer:in als Aufsicht die Prüfung manuell starten, lassen Sie die Option ausgeschaltet.

!!! note "Hinweis"

    Kursbesitzer:innen können während der Prüfung weiterhin normal auf ihren Kurs zugreifen.

---


## Tab "Safe Exam Browser" [:octicons-tag-16:{ title="ab Release 20.3 (OO-9159)" }](https://track.frentix.com/issue/OO-9159) {: #tab-safe-exam-browser}

![Ausgeschalteter Schalter "Safe Exam Browser verwenden", weitere Felder erscheinen erst nach dem Einschalten](assets/assessment_management_create_exam_setting_tab_seb_v1_de.png){ class="shadow lightbox" title="Tab Safe Exam Browser im Dialog einer Prüfung" }

**Safe Exam Browser verwenden**: Die Verwendung des [Safe Exam Browsers](http://www.safeexambrowser.org) erlaubt die sichere Ausführung von Online-Prüfungen, in dem der Computer in den sogenannten Kioskmodus versetzt wird. Dadurch wird die Verwendung unerlaubter Quellen während einer Prüfung unterbunden. Teilnehmende werden darüber benachrichtigt, dass der SEB für die Prüfung Voraussetzung ist. Erst wenn OpenOlat im Safe Exam Browser gestartet wurde kann die Prüfung durchgeführt werden.

![Markierte Auswahl SEB-Konfiguration mit Aus Vorlage (empfohlen), Benutzerdefiniert und Mit manuellen Keys, darunter Vorlage, Vorlage Typ und Prüfungsmodus-spezifische Konfiguration](assets/assessment_management_create_exam_setting_tab_seb_fields_v2_de.png){ class="shadow lightbox" title="Tab Safe Exam Browser im Dialog einer Prüfung · 2026.10.02" }

**SEB-Konfiguration** [:octicons-tag-16:{ title="ab Release 20.3.10 / 21.0.4 (OO-9730)" }](https://track.frentix.com/issue/OO-9730): Legen Sie fest, woher der Safe Exam Browser seine Einstellungen für diese Prüfung bezieht. Drei Arten stehen zur Auswahl:

- **Aus Vorlage (empfohlen)**: Die Einstellungen kommen aus einer Vorlage. Die Gültigkeit prüft OpenOlat über den Konfigurationsschlüssel.
- **Benutzerdefiniert**: Sie erstellen eine eigene Konfiguration für diese Prüfung. Vorbelegt sind die Werte der Standardvorlage, wenn diese eine Formularvorlage ist.
- **Mit manuellen Keys**: Sie verwenden eine eigene SEB-Datei, die ausserhalb von OpenOlat gepflegt wird, und tragen deren Safe Exam Browser Keys im Feld "Safe Exam Browser Keys" ein.

Die Wahl gilt nur für diese Prüfung. Die Einstellung "Safe Exam Browser - Art der Benutzung" der System-Administration wirkt nicht auf sie, sondern nur auf Prüfungen aus Terminen: [Prüfungsmodus aus einem Termin](#exam_from_event)

**Vorlage**: Erscheint bei "Aus Vorlage (empfohlen)". Mit den beiden Schaltflächen wählen Sie die Quelle der Vorlage:

- **System**: Wählen Sie im Dropdown eine der aktiven Konfigurationsvorlagen, die die Administration bereitstellt. Die als Standard markierte Vorlage ist vorausgewählt. Wurde eine gespeicherte Vorlage nachträglich deaktiviert, bleibt sie ausgewählt, bis eine andere Vorlage gewählt wird.
- **Eigenes**: Laden Sie mit "Hochladen" eine eigene SEB-Datei hoch. OpenOlat liest die Einstellungen aus der Datei, berechnet den Konfigurationsschlüssel und zeigt die Einstellungen schreibgeschützt an. Die Datei darf nicht verschlüsselt sein.

**Vorlage Typ**: Zeigt, ob die Vorlage ein "Formular" oder eine "SEB-Datei" ist. Bei einem Formular steht daneben der Button "Kopie erstellen und anpassen": Er übernimmt die Werte der Vorlage in eine Konfiguration "Benutzerdefiniert", die Sie für diese Prüfung ändern können.

**Hinweis für Autoren**: Ist in der gewählten Vorlage ein Hinweis für Autor:innen hinterlegt, erscheint er hier.

Unter der Legende **Prüfungsmodus-spezifische Konfiguration** stehen die Einstellungen, die für genau diese Prüfung gelten:

**Herunterladbare Konfigurationsdatei**: Legt fest, ob Teilnehmende die SEB-Konfigurationsdatei für diese Prüfung herunterladen können. Das Feld erscheint bei "Aus Vorlage (empfohlen)" und "Benutzerdefiniert".

**Hinweis für Teilnehmende**: Ein Text, der den Teilnehmenden zusammen mit der SEB-Konfiguration angezeigt wird.

**Beenden von SEB erlauben**: Erlaubt den Prüfungsteilnehmenden, den Safe Exam Browser nach Abgabe der Prüfung zu beenden. Der Schalter ändert nur diese Einstellung, die übrigen Werte der Prüfung bleiben erhalten. [:octicons-tag-16:{ title="ab Release 20.3.9 / 21.0.3 (OO-9740)" }](https://track.frentix.com/issue/OO-9740)

**Beenden/Entsperren-Kennwort**: Erscheint, wenn "Beenden von SEB erlauben" eingeschaltet ist. Mit diesem Kennwort beenden die Teilnehmenden den Safe Exam Browser. Bei einer SEB-Datei, aus dem System oder hochgeladen, überschreibt das Kennwort das Kennwort der Datei für genau diese Prüfung. Unter dem Feld steht dann der Hinweis "Überschreibt das Passwort der Vorlage. Der Config Key wird automatisch neu berechnet." Bei "Benutzerdefiniert" gehört das Kennwort zur eigenen Konfiguration, der Hinweis erscheint nicht. [:octicons-tag-16:{ title="ab Release 20.3.9 / 21.0.3 (OO-9743)" }](https://track.frentix.com/issue/OO-9743)

Welcher Wert gilt, hängt von der Vorlage ab. Bei einem Formular aus dem System übernimmt die Prüfung "Hinweis für Teilnehmende", "Beenden von SEB erlauben" und das Kennwort aus der Vorlage; die Felder sind dann nicht änderbar, nur "Herunterladbare Konfigurationsdatei" legen Sie pro Prüfung fest. Bei einer SEB-Datei und bei "Benutzerdefiniert" speichert die Prüfung ihre eigenen Werte. Öffnen Sie die Prüfung erneut oder wechseln Sie den Tab, zeigen die Felder die gespeicherten Werte der Prüfung. Wählen Sie eine andere Vorlage, übernehmen die Felder deren Werte. [:octicons-tag-16:{ title="ab Release 20.3.9 / 21.0.3 (OO-9741)" }](https://track.frentix.com/issue/OO-9741)

Bei "Mit manuellen Keys" zeigt die Legende nur "Hinweis für Teilnehmende". Darunter steht das Pflichtfeld "Safe Exam Browser Keys".

Unter der Legende **Konfiguration anhand der Vorlage** stehen bei einem Formular und bei "Benutzerdefiniert" die Detaileinstellungen des Safe Exam Browser, darunter der "Konfigurationsschlüssel der gespeicherten Konfiguration". Ändern lassen sie sich nur bei "Benutzerdefiniert". Bei einer SEB-Datei zeigt stattdessen die Legende **Konfiguration anhand der SEB-Datei Vorlage** die Einstellungen der Datei schreibgeschützt an.

![Aus der Vorlage übernommene SEB-Detaileinstellungen wie Browser-Ansichtsmodus, Taskleiste und Konfigurationsschlüssel, schreibgeschützt](assets/assessment_management_create_exam_setting_tab_seb_config_v1_de.png){ class="shadow lightbox" title="Legende Konfiguration anhand der Vorlage" }

!!! tip "Voraussetzung"
    Die Vorlagenauswahl "System" steht nur zur Verfügung, wenn in der System-Administration unter `Administration > e-Assessment > Prüfungsverwaltung > Tab "Safe Exam Browser Konfiguration"` mindestens eine aktive Vorlage angelegt wurde.

!!! note "Weitere Informationen"
    [Safe Exam Browser (SEB) konfigurieren >](../../manual_how-to/SEB/SEB.de.md)

---


## Prüfungsmodus aus einem Termin [:octicons-tag-16:{ title="ab Release 14.0 (OO-4045)" }](https://track.frentix.com/issue/OO-4045) {: #exam_from_event}

Wer im Kurs Termine führt, macht einen Termin direkt zur Prüfung, ohne einen Prüfungsmodus von Grund auf anzulegen. Wählen Betreuer:innen oder Kursbesitzer:innen im 3-Punkte-Menü eines Termins "Als Prüfung markieren", legt OpenOlat einen Prüfungsmodus an und öffnet den Dialog "Prüfung". Wer den Eintrag erhält und warum er fehlen kann, beschreibt die Seite zur Toolbar: [Termin als Prüfung markieren](../learningresources/Toolbar_Events.de.md#mark_event_as_exam)

Der Dialog ist kürzer als der eines direkt angelegten Prüfungsmodus und hat keine Tabs:

![Dialog mit Titel, Beschreibung, Datum und Zeit samt Vor- und Nachlaufzeit, Teilnehmenden, Kursbausteinen und dem Schalter Safe Exam Browser verwenden](assets/assessment_mode_event_exam_dialog_v1_de.png){ class="shadow lightbox" title="Dialog Prüfung zu einem Termin · 2026.10.02" }

- **Titel** und **Beschreibung**: Der Titel ist ein Pflichtfeld.
- **Datum und Zeit**: übernommen aus dem Termin. In Klammern stehen Vorlaufzeit und Nachlaufzeit in Minuten, zum Beispiel "(-10/+10 Min.)". Sie kommen aus den Vorgabewerten des Kurses oder der System-Administration.
- **Teilnehmende**: übernommen aus dem Termin.
- **Kursbaustein auswählen**: Pflichtfeld. Mit "Kursbausteine auswählen" legen Sie fest, auf welche Kursbausteine die Teilnehmenden während der Prüfung zugreifen.
- **Safe Exam Browser verwenden**: schaltet den Safe Exam Browser für diese Prüfung ein.
- **Zulässige IP-Adressen**: erscheint, wenn die Vorgabewerte erlaubte IP-Adressen enthalten, und ist nicht änderbar.

Nach dem Einschalten von "Safe Exam Browser verwenden" zeigt der Dialog keine Auswahl "SEB-Konfiguration". Die Art legt die System-Administration mit der Einstellung ["Safe Exam Browser - Art der Benutzung"](../../manual_admin/administration/Modules_Events_and_Absences.de.md#seb_type_of_use) für alle Prüfungen aus Terminen fest:

- **Aus Vorlage (empfohlen)**: Im Feld "Konfiguration" wählen Sie eine der aktiven Vorlagen, die als Standard markierte ist vorausgewählt. "Bereitgestellte Konfiguration anzeigen" zeigt die Einstellungen der gewählten Vorlage. Ob Teilnehmende die Konfigurationsdatei herunterladen können, legt die System-Administration fest.
- **Mit manuellen Keys**: Das Feld "Safe Exam Browser Keys" zeigt die Keys aus den Vorgabewerten des Kurses oder der System-Administration. Im Dialog sind sie nicht änderbar.

![Eingeschalteter Schalter Safe Exam Browser verwenden mit dem Feld Konfiguration und dem Link Bereitgestellte Konfiguration anzeigen](assets/assessment_mode_event_exam_seb_template_v1_de.png){ class="shadow lightbox" title="Dialog Prüfung zu einem Termin · 2026.10.02" }

![Eingeschalteter Schalter Safe Exam Browser verwenden mit dem nicht änderbaren Feld Safe Exam Browser Keys](assets/assessment_mode_event_exam_seb_keys_v1_de.png){ class="shadow lightbox" title="Dialog Prüfung zu einem Termin · 2026.10.02" }

Eine Prüfung aus einem Termin erscheint auch in der Prüfungsverwaltung des Kurses und öffnet dort denselben Dialog. Direkt in der Prüfungsverwaltung angelegte Prüfungsmodi wählen die Art dagegen pro Prüfung im Feld "SEB-Konfiguration", siehe [Tab "Safe Exam Browser"](#tab-safe-exam-browser).

---


## Prüfung durchführen

Teilnehmende, die einer Prüfung zugeteilt wurden, werden zu Beginn der Prüfung bzw. zu Beginn der Vorlaufzeit über den Start der Prüfung informiert. Sollte OpenOlat durch eine Nachlaufzeit am Ende der Prüfung noch gesperrt sein, werden sie ebenfalls darüber informiert.

![Benachrichtigung "Aktuelle Prüfung" mit Kurs, Zeitraum, Sperrhinweisen und Countdown bis zum Prüfungsbeginn](assets/assessment_management_exam_info1_v1_de.png){ class="shadow lightbox" title="Benachrichtigung für Teilnehmende" }

Ist bei "Art des Beginns/Endes" die Option "Manuell" gewählt, startet eine Person die Prüfung selbst, zum Beispiel die Aufsicht im Prüfungsraum, sobald alle bereit sind. Dafür zeigt die Übersicht des [Bewertungswerkzeugs](Assessment_tool_overview.de.md) im Bereich "Prüfungsmodus" bei der Prüfung den Button "Prüfung starten". Der Button erscheint ab dem Tag, an dem die Prüfung beginnt, und nicht erst zur konfigurierten Uhrzeit.

![Kachel Prüfungsmodus mit Button "Starten" markiert](assets/assessment_management_exam_coach_v1_de.png){ class="shadow lightbox" title="Übersicht des Bewertungswerkzeugs" }

Startet die Prüfung später als geplant, bleibt die Vorlaufzeit so, wie sie konfiguriert ist. Das Ende der Prüfung verschiebt sich um dieselbe Zeit nach hinten, die konfigurierte Prüfungsdauer bleibt also gleich.

Während der Prüfung verfolgen Betreuer:innen den Prüfungsmodus in der Übersicht des Bewertungswerkzeugs.

Im Bewertungswerkzeug bewerten sie auch Aufgaben und Freitextfragen von Tests direkt und geben die Bewertung für die Teilnehmenden frei. So lässt sich eine Prüfung gleich im Anschluss besprechen.


### Wer eine Prüfung manuell starten und beenden kann {: #start_stop_rights}

Betreuer:innen sehen eine Prüfung mit manuellem Start im Bereich "Prüfungsmodus" des Bewertungswerkzeugs, den Button "Prüfung starten" aber nur mit einem zusätzlichen Recht. Legen Sie deshalb vor dem Prüfungstag fest, wer die Prüfung startet, und geben Sie dieser Person das passende Recht.

Den Button "Prüfung starten" und danach "Prüfung beenden" sehen im Bewertungswerkzeug:

* Personen mit Besitzerrechten am Kurs, also Besitzer:innen, Lernressourcenverwalter:innen und Administrator:innen, dazu Principals, Kursplaner:innen und Klassenlehrer:innen
* Mitglieder mit dem Recht "Bewertungs-Werkzeug"
* Betreuer:innen, die beim Termin der Prüfung als Dozent:in eingetragen sind (siehe [Prüfungsmodus aus einem Termin](#exam_from_event))

Mitglieder mit dem Recht "Bewertungs-Werkzeug" und Dozent:innen des Termins finden denselben Button auch im [Kursbaustein "Test"](Course_Element_Test.de.md) im Tab "Prüfungsmodus".

In der Prüfungsverwaltung starten und beenden Personen mit Besitzerrechten und Mitglieder mit dem Recht "Prüfungsmodus" oder "Kurseditor" die Prüfung, mit den Buttons "Starten" und "Beenden" in der Liste der Prüfungen:<br>
`Kurs > Administration > Prüfungsverwaltung > Tab "Konfiguration Prüfungsmodus"`

Die Rechte vergeben Besitzer:innen in der Mitgliederverwaltung, für alle Kursbetreuer:innen oder gezielt für die Betreuer:innen einer Gruppe, zum Beispiel einer Gruppe "Aufsicht":<br>
`Kurs > Administration > Mitgliederverwaltung > Rechte`<br>
Die beiden Rechte für den Prüfungsstart geben unterschiedlich viel frei. Was jedes Recht sonst noch erlaubt, beschreibt die Mitgliederverwaltung unter [Vergabe zusätzlicher Rechte](Members_management.de.md#additional_rights).

* **Bewertungs-Werkzeug**: Die Person startet und beendet die Prüfung im Bewertungswerkzeug und arbeitet dort mit allen Funktionen des Werkzeugs.
* **Prüfungsmodus**: Die Person startet und beendet die Prüfung in der Prüfungsverwaltung. Dort legt sie auch Prüfungsmodi an, bearbeitet und löscht sie.

!!! info "Wichtig"

    Mit dem Recht "Bewertungs-Werkzeug" sieht eine Betreuer:in im Bewertungswerkzeug alle Teilnehmer:innen des Kurses, nicht nur die Teilnehmenden ihrer Gruppe. Sie bewertet alle und kann Bewertungsdaten zurücksetzen. Wägen Sie deshalb ab, ob die Aufsicht diesen Zugriff braucht oder ob das Recht "Prüfungsmodus" genügt.

Soll eine Betreuer:in die Prüfung starten, lassen Sie im Tab "Zugang" die Option "Prüfungskonfiguration auch bei Betreuenden anwenden" ausgeschaltet. Sonst gilt der Prüfungsmodus auch für sie, und sie erreicht in OpenOlat nur noch die Prüfung.

---

## Prüfung beenden

Ein laufender Prüfungsmodus endet automatisch oder manuell, je nach Einstellung bei "Art des Beginns/Endes".

Bei "Manuell" beenden die Personen, die die Prüfung auch starten dürfen, sie mit dem Button "Prüfung beenden" im Bewertungswerkzeug, siehe [Wer eine Prüfung manuell starten und beenden kann](#start_stop_rights).

![Banner zum aktiven Prüfungsmodus mit Button "Beenden" und Kachel Prüfungsmodus mit Status Gestartet markiert](assets/assessment_management_exam_stop_v1_de.png){ class="shadow lightbox" title="Übersicht des Bewertungswerkzeugs" }

Der Prüfungsmodus wird auch beendet, wenn der entsprechende Kurs beendet oder gelöscht wird.

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Safe Exam Browser >](http://www.safeexambrowser.org)<br>
[Wie bereite ich eine Online-Prüfung vor? >](../../manual_how-to/exam_preparation/exam_preparation.de.md)<br>
[Wie bereite ich eine Prüfung mit dem Safe Exam Browser (SEB) vor? >](../../manual_how-to/SEB/SEB.de.md)<br>
[Toolbar: Termine >](../learningresources/Toolbar_Events.de.md)<br>
[Modul Termine und Absenzen >](../../manual_admin/administration/Modules_Events_and_Absences.de.md)<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview.de.md)<br>
[Kursbaustein "Test" >](Course_Element_Test.de.md)<br>
[Mitgliederverwaltung >](Members_management.de.md)

**Weiterführend**<br>
[Prüfungsverwaltung: Prüfungseinsicht >](Assessment_inspection.de.md)<br>
[Test Einstellungen - Administration >](Test_settings.de.md)

[Zum Seitenanfang ^](#Assessment_mode)
