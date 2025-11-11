# Course Planner: Produkte {: #products}

![course_planner_products_v3_de.png](assets/course_planner_products_v3_de.png){ class="shadow lightbox" }  

## Was verstehen wir in OpenOlat unter einem Produkt? {: #definition}

Ein Bildungsprodukt ist ein nach innen oder aussen gerichtetes Lernangebot mit Durchführungen. Meistens sind es mehrfache Durchführungen, also von Lernangeboten der gleichen "Art" (-> Produkt). 

Oft bestehen Produkte aus mehreren Kursen und haben eine bestimmte Struktur/Abfolge, in der die enthaltenen Kurse kombiniert sind (strukturierte Produkte). Die Kurse und Lernressourcen werden in zeitlicher Abfolge in einer Baumstruktur abgebildet.

Im Kontext von Unternehmen wird statt von "Curriculum" öfter von (Bildungs-)"Produkt" gesprochen. Deshalb wird in OpenOlat seit Release 20 in der Regel der Begriff "Produkt" verwendet.

Ab Release 20 wurde statt der Curriculumverwaltung eine erweiterte, allgemeine Kursplanung in OpenOlat integriert (Course Planner). 

[zum Seitenanfang ^](#products)

---


## Wo werden Produkte verwendet? {: #usage_of_products}

Produkte werden im **Course Planner** für die Planung eines Bildungsgangs mit mehreren Kursen und Lernressourcen ("Kurspaket") verwendet. Ein Produkt kann dann in mehreren Durchführungen zu verschiedenen Terminen angeboten werden.    

Die Durchführungen eines Produkts können im [Katalog ](../../manual_user/area_modules/catalog2.0_angebote.de.md) angeboten werden.

Werden Teilnehmer:innen nicht nur einem einzelnen Kurs als Mitglieder zugeordnet, sondern der [Durchführung](../../manual_user/area_modules/Course_Planner_Implementations.de.md) eines Produkts, ist die Mitgliedschaft für die Teilnehmer:innen ersichtlich, wenn sie im Hauptmenü die Option "Kurse" wählen".<br>
Kurse, die einem Produkt zugeordnet sind, erscheinen dort im Bereich "Bildungsprogramme".

![course_planner_products_education_programs_v1_de.png](assets/course_planner_products_education_programs_v1_de.png){ class="shadow lightbox" }  


[zum Seitenanfang ^](#products)

---


## Wo und wie werden Produkte aktiviert? {: #activation}

Der für die Erstellung von Produkten verwendete Course Planner ist ein Zusatzmodul in OpenOlat und muss zunächst frei geschaltet werden.<br>
Kunden von frentix kontaktieren für die Aktivierung bitte [contact@frentix.com.](mailto:contact@frentix.com.)<br>
Sind Sie kein Hosting-Kunde von frentix, fragen Sie bitte Ihren Systembetreiber. 

Nach erfolgter Freischaltung können Systemadministrator:innen das Modul aktivieren und einrichten unter: 
**Administration > Module > Course Planner**


[zum Seitenanfang ^](#products)

---


## Produkt erstellen {: #create_product}

Zum Erstellen eines Produkts öffnen Sie den Course Planner und dort den Unterbereich "Produkte".

![course_planner_products1_v3_de.png](assets/course_planner_products1_v3_de.png){ class="shadow lightbox" }  

![course_planner_products2_v2_de.png](assets/course_planner_products2_v2_de.png){ class="shadow lightbox" }  

![course_planner_products3_v2_de.png](assets/course_planner_products3_v2_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Titel**: 
Die Angabe eines Titels ist zwingend erforderlich. 

![2_green_24.png](assets/2_green_24.png) **Kennzeichen**: 
Das Kennzeichen ist ebenfalls ein Pflichtfeld. (Es wird als Identifier zur Unterscheidung bei Elementen mit gleichem Titel verwendet.)

![3_green_24.png](assets/3_green_24.png) **Organisationen**: 
Wenn Sie ein neues Produkt erstellen, können Sie es auch auf die Verwendung innerhalb einer bestimmten Organisationseinheit beschränken, falls bei Ihnen das Modul "Organisationen" aktiviert ist.  

![4_green_24.png](assets/4_green_24.png) **Absenzenmanagement**: 
Mit dieser Auswahl bestimmen Sie, ob das Absenzenmanagement für dieses Produkt verwendet werden soll. (Voraussetzung ist, dass es von einem/einer Administrator:in grundsätzlich aktiviert und für die Kursautor:innen verfügbar gemacht wurde.) 

![5_green_24.png](assets/5_green_24.png) **Beschreibung**: 
In diesem Editor für die Beschreibung können Sie neben Text, Bildern und Links auch Videos einfügen oder direkt durch Klick auf den Mikrofon-Button ein Audio aufnehmen.


[zum Seitenanfang ^](#products)

---


## Produkt importieren {: #import_product}

Soll ein bereits bestehendes Produkt für Ihre Planung verwendet werden, können Sie auch Produkte importieren. Klicken Sie dazu auf die 3 Punkte neben dem Button "Produkt erstellen".

![course_planner_product_import_v1_de.png](assets/course_planner_product_import_v1_de.png){ class="shadow lightbox" }  

[zum Seitenanfang ^](#products)

---


## Einstellung in den Kursen des Produkts {: #course_settings}

Zu einem Produkt gehören im Normalfall mehrere Kurse.
In den Einstellungen jedes Kurses kann sein **Verwendungszweck** festgelegt werden:

* eigenständige Lernressource 
* als Template 
* zur Einbindung in ein Produkt

Wird ein Kurs über den Course Planner verwaltet, ist die Einstellung "**Einbindung in Produkt**". Der Kurs hat dann keine eigenständige Mitgliederverwaltung. Die Mitgliederverwaltung geschieht in diesem Fall in der Mitgliederverwaltung der [Durchführung](../../manual_how-to/course_planner_courses/course_planner_courses.de.md#add_members).

Sie finden die Einstellung unter:<br>
**(Wahl eines Kurses >) Administration > Einstellungen > Tab Freigabe > Einbindung in Produkt**

![course_planner_products_share_v2_de.png](assets/course_planner_products_share_v2_de.png){ class="shadow lightbox" }  



[zum Seitenanfang ^](#products)

---


## Weitere Informationen {: #further_information}

[Wie erstelle ich meinen ersten OpenOlat-Kurs >](../../manual_how-to/my_first_course/my_first_course.de.md)<br>
[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Durchführungen >](../../manual_user/area_modules/Course_Planner_Implementations.de.md)<br>
[Course Planner: Termine >](../../manual_user/area_modules/Course_Planner_Events.de.md)<br>
[Course Planner: Zertifikatsprogramme >](../../manual_user/area_modules/Course_Planner_Certification_Programs.de.md)<br>
[Course Planner: Reports >](../../manual_user/area_modules/Course_Planner_Reports.de.md)<br>
[Wie kann ich mit dem Course Planner eine Kursdurchführung planen und durchführen? >](../../manual_how-to/course_planner_courses/course_planner_courses.de.md)<br>
[Wie kann ich mit dem Course Planner einen Bildungsgang planen und durchführen? >](../../manual_how-to/course_planner_curriculum/course_planner_curriculum.de.md)<br>
[Course Planner aktivieren (Admin) >](../../manual_admin/administration/Modules_Course_Planner.de.md)<br>

[zum Seitenanfang ^](#products)
