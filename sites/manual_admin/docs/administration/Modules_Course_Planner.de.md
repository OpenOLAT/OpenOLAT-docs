# Modul Course Planner {: #module_course_planner}


## Aktivierung des Course Planners {: #activation}

Das Modul Course Planner ist ab Release 20 optional an Stelle des Moduls Curriculum in OpenOlat verfügbar und muss in der Administration aktiviert werden. 

!!! tip "Aktivierung"

	Kunden von frentix kontaktieren für die Aktivierung bitte [contact@frentix.com.](mailto:contact@frentix.com.) Nach der Aktivierung kann zusätzlich die Anzeige des persönlichen Curriculums (= "Lehrgänge") im Bereich "Kurse" aktiviert werden.  
		
	:material-alert: **Nicht Hosting-Kunde von frentix?** Fragen Sie Ihren Systembetreiber!
 
### Tab Course Planner

![modules_course_planner_tab_cp_v1_de.png](assets/modules_course_planner_tab_cp_v1_de.png){ class="shadow lightbox" }


![1_green_24.png](assets/1_green_24.png) **Course Planner einschalten**<br>
Mit dieser Checkbox wird das gesamte Modul aktiviert.

![2_green_24.png](assets/2_green_24.png) **Curriculum in "Meine Kurse"**<br>
Alle Teilnehmer:innen finden in der Hauptnavigation in der Kopfzeile den Menü-Eintrag "Kurse". Unter diesem Menüpunkt können den Teilnehmer:innen ebenfalls Curricula angezeigt werden. 

![3_green_24.png](assets/3_green_24.png) **Benutzer:innen Übersicht**<br>
Hier bestimmen Sie als Administrator:in, welche Optionen die Rollen.

* Course Planner
* Education Manager und
* Linienvorgesetzter

angezeigt bekommen. Was also z.B. eine mit dem Course Planner arbeitende Person von den Benutzer:innen sehen darf. 

![4_green_24.png](assets/4_green_24.png) **Verknüpfte Taxonomien**<br>
Von den im Modul "Taxonomie" erstellten Taxonomien können hier diejenigen ausgewählt werden, die auch im Course Planner verfügbar sein sollen.

**Hinweis:**<br>
Die hier gewählten Taxonomien sollten die gleichen sein, wie die im Katalog verwendeten. Nur dann kann im Katalog auch nach diesen Taxonomien gesucht werden.

![5_green_24.png](assets/5_green_24.png) **Standardmässiger Verwendungszweck für neue Kurse**<br>

Kurse können für eigenständige Verwendung oder zur Einbindung in ein Curriculum/Produkt vorgesehen werden. Als Administrator:in legen Sie hier fest, welche Verwendung standardmässig voreingestellt ist.

**Eigenständig**: Ein eigenständiger Kurs besitzt eine Mitgliederverwaltung. Der Zugang kann mit der Buchungsmethode "Privat" durch Eintragung als Mitglied (z.B. durch Kursbesitzer:innen), durch Vergabe eines Zugangscodes oder über eine Veröffentlichung im Katalog erfolgen. 

**Einbindung in Curriculum/Produkt**: Wird der Kurs in ein Curriculum/Produkt eingebunden, werden die Mitgliedschaften durch den Course Planner vergeben und verwaltet. Der Kurs benötigt dann keine zweite, eigenständige Mitgliederverwaltung.


[Zum Seitenanfang ^](#module_course_planner)
  
---
## Tab Elementtypen

### Definieren von Element-Typen {: #define_element_types}

Element-Typen definieren, welche Elemente ein Curriculum enthalten kann und
geben diesen Elementen eine nähere Bedeutung. Beim Anlegen der Element-Typen kann eine hierarchische Struktur abgebildet werden, dies ist aber nicht zwingend. Ein Beispiel für ein hierarchisches Curriculum ist `Lehrgang → Semester → Modul → Kurs`.

Ein Element kann ein reines Strukturelement sein ("Mit Kursinhalt" ausgeschaltet, 
vergleichbar mit Kursbaustein "Struktur".)

Für ein Element mit einem oder mehreren Kursen als Inhalt muss "Mit Kursinhalt" eingeschaltet sein.
(Siehe Element-Typ erstellen, Punkt 7.)


In der Tabelle werden die bereits angelegten Element-Typen angezeigt. Eine Bearbeitung der Daten ist über das
:fontawesome-regular-pen-to-square:-Symbol möglich. Über den 3-Punkte-Link kann der jeweilige Typ kopiert oder gelöscht werden.

![modules_course_planner_tab_elementtypes_v1_de.png](assets/modules_course_planner_tab_elementtypes_v1_de.png){ class="shadow lightbox" }



[Zum Seitenanfang ^](#module_course_planner)
  
---


### Element-Typ erstellen {: #create_element_types}

Über den Button "Neuen Typ hinzufügen" können weitere Element-Typen angelegt werden. 

![modules_course_planner_tab_elementtypes_create_v1_de.png](assets/modules_course_planner_tab_elementtypes_create_v1_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Titel**<br>
Es ist zwingend ein Titel anzugeben.

![2_green_24.png](assets/2_green_24.png) **Kennzeichen**<br>
Das Kennzeichen ist ebenfalls ein Pflichtfeld. (Es wird als Identifier zur Unterscheidung bei Elementen mit gleichem Titel verwendet.) Der hier eingegebene Text erscheint bei der Erstellung eines neuen Curriculum-Elements als Auswahloption.<br> (Course Planner > Curriculum/Produkt > Tab Durchführung > Button Erstellen)

![3_green_24.png](assets/3_green_24.png) **CSS class**<br>
Es ist an dieser Stelle möglich, per CSS-Klasse ein nur für diesen Element-Typ geltendes Layout zu hinterlegen. Bei Interesse an spezifischen Layouts melden Sie sich bitte bei frentix.

![4_green_24.png](assets/4_green_24.png) **Beschreibung**<br>
Erklären Sie hier mit einem Beschreibungstext Ihren Elementtyp.

![5_green_24.png](assets/5_green_24.png) **Features**<br>
Mit aktiviertem **Absenzenmanagement** haben Sie in der Rolle als Course Planner das Tab "Absenz" auf deiesem Element und können für alle Teilnehmer:innen dieses Elements die Absenzen einsehen. (Voraussetzung ist, dass das Modul "Absenzenverwaltung" aktiviert ist.)

Ebenfalls kann für diesen Element-Typ die Anzeige des **Stundenplans**
aktiviert werden. Dieser vereint alle Kurskalender-Termine der zu diesem
Curriculum-Element zugeordneten Kurse.

Wird **Fortschritt** selektiert, wird der Fortschritt in Lernpfadkursen als Kreisdiagramm angezeigt. 
Besteht das Element aus mehreren Unterelementen, wird der Fortschritt aus dem Durchschnitt der Unterelemente (nur Lernpfadkurse) berechnet. (In herkömmlichen Kursen steht die Fortschrittsanzeige nicht zur Verfügung.)

![6_green_24.png](assets/6_green_24.png) **Als Durchführung erlauben**<br>
Mit dieser Angabe bestimmen Sie, welches Element ein Eltern-Element sein darf.
Eine Durchführung ("Durchführungs-Element") ist das oberste Eltern-Element.

![7_green_24.png](assets/7_green_24.png) **Mit Kursinhalt**<br>
Wie oben beschrieben, kann ein Element ein reines Strukturelement sein, vergleichbar mit Kursbaustein "Struktur" ("Mit Kursinhalt" ausgeschaltet).

Für ein Element mit einem oder mehreren Kursen als Inhalt muss "Mit Kursinhalt" eingeschaltet sein.

![8_green_24.png](assets/8_green_24.png) **Typ Composite**<br>
Nach der Aktivierung können bereits bestehende Element-Typen dem neuen Typ zusätzlich als Sub-
Typen untergeordnet werden.


[Zum Seitenanfang ^](#module_course_planner)
  
---

## Weitere Informationen

[Wie kann ich mit dem Course Planner Kursdurchführungen planen und durchführen? >](../../manual_how-to/course_planner_courses/course_planner_courses.de.md)<br>
[Wie kann ich mit dem Course Planner einen Bildungsgang planen und durchführen? >](../../manual_how-to/course_planner_curriculum/course_planner_curriculum.de.md)<br>
[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Curricula/Produkte >](../../manual_user/area_modules/Course_Planner_Products.de.md)<br>
[Course Planner: Durchführungen >](../../manual_user/area_modules/Course_Planner_Implementations.de.md)<br>
[Course Planner: Termine >](../../manual_user/area_modules/Course_Planner_Events.de.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.de.md)<br>

[Zum Seitenanfang ^](#module_course_planner)


