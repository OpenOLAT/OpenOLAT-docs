# Modul Course Planner {: #module_course_planner}


## Aktivierung des Course Planners {: #activation}

Das Modul Course Planner ist optional an Stelle des Moduls Curriculum in OpenOlat verfügbar und muss in der Administration aktiviert werden.

!!! tip "Hosting-Kunden von frentix"
	 Wenden Sie sich für die Aktivierung bitte an [contact@frentix.com](mailto:contact@frentix.com). <br> Nach der Aktivierung kann zusätzlich die Anzeige des persönlichen Curriculums («Lehrgänge») im Bereich «Kurse» aktiviert werden.


### Tab Course Planner {: #tab_course_planner}

![Der Tab «Course Planner» der Modulkonfiguration mit dem Schalter zum Einschalten, der Option Produkt in «Meine Kurse», dem Optionsbaum "Benutzer:innen-Übersicht" und den verknüpften Taxonomien, in der System-Administration](assets/modules_course_planner_config_v1_de.png){ class="shadow lightbox" }

**Course Planner einschalten**<br>
Mit dieser Checkbox wird das gesamte Modul aktiviert.

**Produkt in "Meine Kurse"**<br>
Alle Teilnehmer:innen finden in der Hauptnavigation in der Kopfzeile den Menü-Eintrag "Kurse". Unter diesem Menüpunkt können den Teilnehmer:innen ebenfalls Produkte angezeigt werden.

**Benutzer:innen-Übersicht**<br>
Hier bestimmen Sie als Administrator:in, welche Optionen die Rollen Kursplaner:in, Ausbildungsverantwortliche:r und Linienvorgesetzte:r angezeigt bekommen. Also was eine mit dem Course Planner arbeitende Person von den Teilnehmenden sehen darf. Zu jedem Bereich lassen sich einzelne Angaben separat freigeben, etwa Kursfortschritt und Status, Termine und Absenzen, Leistungsnachweise, Badges, Buchungen oder der Zugriff auf den Qualitätsmanagementreport.

**Verknüpfte Taxonomien**<br>
Von den im Modul "Taxonomie" erstellten Taxonomien können hier diejenigen ausgewählt werden, die auch im Course Planner verfügbar sein sollen.

**Hinweis:**<br>
Die hier gewählten Taxonomien sollten die gleichen sein, wie die im Katalog verwendeten. Nur dann kann im Katalog auch nach diesen Taxonomien gesucht werden.

**Standardmässiger Verwendungszweck für neue Kurse**<br>
Kurse können für eigenständige Verwendung oder zur Einbindung in ein Produkt vorgesehen werden. Als Administrator:in legen Sie hier fest, welche Verwendung standardmässig voreingestellt ist.

* **Eigenständig**: Ein eigenständiger Kurs besitzt eine Mitgliederverwaltung. Der Zugang kann mit der Angebotsart "Privat" durch Eintragung als Mitglied (z.B. durch Kursbesitzer:innen), durch Vergabe eines Zugangscodes oder über eine Veröffentlichung im Katalog erfolgen.
* **Verwendung im Course Planner**: Wird der Kurs in ein Produkt eingebunden, werden die Mitgliedschaften durch den Course Planner vergeben und verwaltet. Der Kurs benötigt dann keine zweite, eigenständige Mitgliederverwaltung.

![Die Einstellung «Standardmässiger Verwendungszweck für neue Kurse» mit den Karten Eigenständig und Verwendung im Course Planner, im Menüpunkt Course Planner der System-Administration](assets/modules_course_planner_usage_v1_de.png){ class="shadow lightbox" }

!!! tip "Tipp"

	Wird der Course Planner umfassend eingesetzt, bietet es sich an, den Standard-Verwendungszweck für neue Kurse unter `Systemadministration > Course Planner-Settings` auf "Einbindung in Produkt" einzustellen.

[Zum Seitenanfang ^](#module_course_planner)

---
## Tab Elementtypen {: #tab_element_types}

### Übersicht der Elementtypen [:octicons-tag-16:{ title="ab Release 21.0 (OO-8924)" }](https://track.frentix.com/issue/OO-8924){:target="_blank"} {: #element_types_overview}

Element-Typen definieren, welche Elemente ein Produkt enthalten kann und geben diesen Elementen eine Bedeutung. Beim Anlegen der Element-Typen kann eine hierarchische Struktur abgebildet werden. **Ein Beispiel** für ein hierarchisches Produkt: **von** *Lehrgang* **zu** *Semester* **zu** *Modul* **zu** *Kurs*.

Die Übersichtstabelle zeigt alle angelegten Elementtypen. Ein Elementtyp wird über das :fontawesome-regular-pen-to-square:-Symbol bearbeitet. Über den 3-Punkte-Link kann der Typ kopiert oder gelöscht werden.

**Tabellenspalten:**

| Spalte | Bedeutung |
|---|---|
| Titel | Der Name des Elementtyps |
| Kennzeichen | Der eindeutige Identifier des Elementtyps |
| Status | Ob der Typ für neue Elemente zur Auswahl steht: «Aktiv» oder «Inaktiv» |
| Verwendung als | Funktion des Elementtyps im Produkt: «Durchführung», «Element» oder «Durchführung oder Element (legacy)» |
| Unterelemente | Ob Elemente dieses Typs Unterelemente enthalten können |
| Inhalt | Welchen Kursinhalt Elemente dieses Typs tragen: «Kein Inhalt», «Einzelkurs» oder «Kurs-Bundle» |
| #Verwendungen | Anzahl der im System vorhandenen Elemente dieses Typs |
| #Eltern | Anzahl übergeordneter Elementtypen, die diesen Typ als Kindelement zulassen |
| #Kinder | Anzahl der Elementtypen, die als Kindelemente dieses Typs definiert sind |

![Die Übersichtstabelle der Elementtypen mit Titel, Kennzeichen, Status, Verwendung als, Unterelementen, Inhalt und den Zählern, dazu die Buttons zum Erstellen neuer Typen, im Tab Elementtypen der System-Administration](assets/modules_course_planner_element_types_v1_de.png){ class="shadow lightbox" }


[Zum Seitenanfang ^](#module_course_planner)

---


### Elementtyp erstellen und bearbeiten {: #create_element_types}

Zwei Buttons legen neue Elementtypen an: **«Typ für Durchführung erstellen»** und **«Typ für Element erstellen»**. Die Wahl des Buttons bestimmt die Verwendung des Typs und lässt sich im Dialog nicht mehr ändern. Einen bestehenden Typ öffnen Sie über das :fontawesome-regular-pen-to-square:-Symbol.

![Der Dialog «Typ für Durchführung erstellen» mit Titel, Kennzeichen, Beschreibung, den Features und der Konfiguration von Unterelementen und Inhalt, in der System-Administration](assets/modules_course_planner_element_type_create_v1_de.png){ class="shadow lightbox" }

**Titel** (Pflichtfeld)<br>
Der Name des Elementtyps, der bei der Auswahl beim Anlegen eines Elements angezeigt wird.

**Kennzeichen** (Pflichtfeld)<br>
Ein eindeutiger Identifier, der zur Unterscheidung bei Elementen mit gleichem Titel dient. Erscheint bei der Erstellung eines neuen Curriculum-Elements als Auswahloption.

**Beschreibung**<br>
Erklärender Text zum Elementtyp.

**Features**<br>
* **Absenzmanagement**: Kursplaner:innen erhalten auf Elementen dieses Typs den Tab «Absenzen» und können die Absenzen aller Teilnehmer:innen einsehen. Voraussetzung: Modul Absenzenverwaltung ist aktiviert.
* **Stundenplan**: Vereint alle Kurskalender-Termine der dem Produkt-Element zugeordneten Kurse.
* **Fortschritt**: Zeigt den Lernfortschritt in Lernpfadkursen als Kreisdiagramm. Bei mehreren Unterelementen wird der Durchschnitt der Unterelemente berechnet.

!!! note "CSS class"
	Hier kann per CSS-Klasse ein typenspezifisches Layout hinterlegt werden. Bei Interesse an spezifischen Layouts wenden Sie sich an frentix: [contact@frentix.com](mailto:contact@frentix.com).

Im Abschnitt **Konfiguration** legen Sie die Struktur fest:

**Verwendung als**<br>
Zeigt die Funktion von Elementen dieses Typs im Produkt. Der Wert ergibt sich aus dem gewählten Button und ist nicht editierbar:

* **Durchführung**: Elemente dieses Typs sind Durchführungen (das oberste Elternelement). Sie verfügen über einen Durchführungszeitraum und sind der Ausgangspunkt für Automatisierungsregeln.
* **Element**: Elemente dieses Typs sind Subelemente unterhalb einer Durchführung und haben keinen eigenen Durchführungszeitraum.
* **Durchführung oder Element (legacy)**: Elemente dieses Typs können sowohl als Durchführung als auch als Subelement verwendet werden. Dieser Modus dient der Abwärtskompatibilität mit bestehenden Produktstrukturen und steht für neue Typen nicht zur Wahl.

**Unterelemente**<br>
* **Nein**: Elemente dieses Typs stehen eigenständig, ohne Unterelemente.
* **Ja**: Elemente dieses Typs können Unterelemente enthalten.

**Inhalt**<br>
* **Kein Inhalt**: Das Element trägt keinen Kurs. Es ist ein reines Strukturelement, vergleichbar mit dem Kursbaustein «Struktur».
* **Einzelkurs**: Das Element hat genau einen Kurs.
* **Kurs-Bundle**: Das Element kann mehrere Kurse haben.

**Elternelemente** und **Kindelemente**<br>
Bei einem bestehenden Typ bestimmen Sie hier, unter welchen Typen er eingesetzt werden darf und welche Typen ihm untergeordnet werden können. So entsteht die Hierarchie eines Produkts.

**Status**<br>
* **Aktiv**: Der Typ steht beim Anlegen neuer Elemente zur Auswahl.
* **Inaktiv**: Der Typ ist ausgeblendet und steht für neue Elemente nicht mehr zur Auswahl. Bestehende Elemente dieses Typs bleiben erhalten.


[Zum Seitenanfang ^](#module_course_planner)

---


### Automatisierungsregeln je Elementtyp [:octicons-tag-16:{ title="ab Release 21.0 (OO-9452)" }](https://track.frentix.com/issue/OO-9452){:target="_blank"} {: #automation_rules}

Für jeden Elementtyp lassen sich Automatisierungsregeln hinterlegen. Diese Regeln gelten als Vorlage für alle Elemente dieses Typs: Elemente können die Vorlage übernehmen oder individuell überschreiben (siehe [Automatisierung in den Einstellungen einer Durchführung](../../manual_user/area_modules/Course_Planner_Implementations.de.md#tab_settings_automation)).

**Automatisierungsregeln konfigurieren**

Öffnen Sie den gewünschten Elementtyp über das :fontawesome-regular-pen-to-square:-Symbol und wechseln Sie zum Tab **«Automatisierung»**. Über **«Automatisierungsregel hinzufügen»** fügen Sie neue Regeln hinzu.

![Der Abschnitt Automatisierung im Dialog eines Elementtyps mit dem Schalter, den Filtern und der Regeltabelle aus Kontext, Automatisierung, Zielstatus, Bedingung und vorausgesetztem Status, dazu die Eltern- und Kindelemente, in der System-Administration](assets/modules_course_planner_element_type_automation_v1_de.png){ class="shadow lightbox" }

Jede Automatisierungsregel enthält:

* **Auslösertyp**:
  * **Bei Statuswechsel**: Die Aktion wird ausgelöst, sobald der Durchführungs- oder Elementstatus einen definierten Wert annimmt.
  * **Zeitgesteuert**: Die Aktion wird relativ zum Beginn oder Ende des Durchführungszeitraums ausgelöst. Dabei legen Sie das Bezugsdatum (Beginn oder Ende) sowie einen optionalen Versatz (Anzahl Tage/Wochen/Monate vor oder nach dem Bezugsdatum) fest.
* **Aktion**: Was automatisch ausgeführt wird, z. B. Kurs aus Vorlage erstellen (Instanzierung) oder Kursstatus setzen.


[Zum Seitenanfang ^](#module_course_planner)

---

## Weitere Informationen {: #further_information}

[Wie kann ich mit dem Course Planner Kursdurchführungen planen und durchführen? >](../../manual_how-to/course_planner_courses/course_planner_courses.de.md)<br>
[Wie kann ich mit dem Course Planner einen Bildungsgang planen und durchführen? >](../../manual_how-to/course_planner_curriculum/course_planner_curriculum.de.md)<br>
[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Produkte >](../../manual_user/area_modules/Course_Planner_Products.de.md)<br>
[Course Planner: Durchführungen >](../../manual_user/area_modules/Course_Planner_Implementations.de.md)<br>
[Course Planner: Termine >](../../manual_user/area_modules/Course_Planner_Events.de.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.de.md)<br>

[Zum Seitenanfang ^](#module_course_planner)


