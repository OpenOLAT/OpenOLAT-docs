# Qualitätsmanagement: Datenerhebungsgeneratoren {: #Quality_Management_Data_Collection_Generators}


!!! info "Empfehlung"

    Für das Verständnis des Datenerhebungsgenerators werden Kenntnisse über Datenerhebungen vorausgesetzt.


## Was macht ein Datenerhebungsgenerator? {: #QMgenerator_function}

**Datenerhebungen** können im Modul Qualitätsmanagement auch **automatisiert nach bestimmten Regeln** erstellt werden. 

Die Beschreibung und Einrichtung der Regeln geschieht in sogenannten **Datenerhebungsgeneratoren**. 

![quality_management_scheme_generator_v1_de.png](assets/quality_management_scheme_generator_v1_de.png){ class="lightbox" }


## Wie wird ein Datenerhebungsgenerator erstellt? {: #create_QMgenerator}

Bei entsprechender Berechtigung (Rolle) erscheint in Ihrer Hauptnavigation das **Qualitätsmanagement**. Klicken Sie auf den Link im Abschnitt **"Datenerhebungsgeneratoren"**.

![quality_management_data_collection_generators_v1_de.png](assets/quality_management_data_collection_generators_v1_de.png){ class="shadow lightbox" }

Erstellen Sie dort einen neuen Datenerhebungsgenerator.

![quality_management_data_collection_generators_create_v1_de.png](assets/quality_management_data_collection_generators_create_v1_de.png){ class="shadow lightbox" }

Mit der Wahl eines Typs bestimmen Sie das Regel-Set, nach dem Datenerhebungen erstellt werden.

![quality_management_data_collection_generators_type_v2_de.png](assets/quality_management_data_collection_generators_type_v2_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Generator Typ "Kurs" {: #QMgenerator_type_course}

![quality_management_data_collection_generator_course_v1_de.png](assets/quality_management_data_collection_generator_course_v1_de.png){ class="shadow lightbox" }

### Tab "Konfiguration" {: #Quality_Management_Data_Collection_Generators_Type_Course_Config}

![quality_management_data_collection_generator_course_config_v2_de.png](assets/quality_management_data_collection_generator_course_config_v2_de.png){ class="shadow lightbox" }

![1_green_24.png](assets/1_green_24.png) **Titel des Generators**<br>
Verwenden Sie möglichst einen Titel, der eine Aussage zu Inhalt und Verwendung macht, um eine klare Zuordnung und Abgrenzung zu anderen Generatoren zu ermöglichen.

![2_green_24.png](assets/2_green_24.png) **Organisationen**<br>
Wurde das Modul "Organisationseinheiten" aktiviert und eingerichtet, können Datenerhebungen auch auf ausgewählte Organisationseinheiten bezogen werden.

![3_green_24.png](assets/3_green_24.png) **Formular**<br>
Auch bei Datengeneratoren kommt jeweils nur ein Formular zum Einsatz um Vergleichbarkeit und Auswertung zu ermöglichen. Soll ein weiteres Formular verwendet werden, müssten Sie einen weiteren Generator erstellen. 

![4_green_24.png](assets/4_green_24.png) **Titel der Datenerhebung**<br>
Geben Sie hier den Titel der vom Datengenerator erzeugten Datenerhebungen an. 
Im Titel können auch Variablen verwendet werden. 

![5_green_24.png](assets/5_green_24.png) **Rollen der Teilnehmer:innen**
Die Kursmitglieder mit den hier ausgewählten Rollen können an der Datenerhebung teilnehmen. Es besteht die Möglichkeit, diese Datenerhebung z.B. ausschliesslich unter Betreuer:innen zu machen. 

![6_green_24.png](assets/6_green_24.png) **Startereignis**<br>
Auslösende Startereignisse können beim Generator vom Typ "Kurs" sein:

* Kursbeginn
* Kursende
* täglich

![7_green_24.png](assets/7_green_24.png) **Tage nach Kurstermin**<br> 
(Diese Option wird nur angezeigt, wenn "Kursbeginn" oder "Kursende" als Startereignis gewählt wurde.)<br>
Der Start der Datenerhebung wird aus dem Startereignis und der hier eingetragenen Anzahl Tage berechnet.
Die Anzahl Tage kann auch negativ sein. 

**Wochentag**<br>
(Diese Option wird nur angezeigt, wenn "täglich" als Startereignis gewählt wurde.)<br>
Es wird periodisch immer an den angegebenen Wochentagen eine Datenerhebung generiert.

!!! note "Hinweis"

    Hat ein Kurs ein Beginn- oder Enddatum, wird er vor und nach diesen Daten nicht in den Datenerhebungen berücksichtigt.

![8_green_24.png](assets/8_green_24.png) **Dauer der Datenerhebung (Stunden)**<br>
Nach Start der Datenerhebung können alle Teilnehmenden im angegebenen Zeitraum das Formular ausfüllen und abgeben. Nach Ablauf dieser Frist ist eine Abgabe nicht mehr möglich. 

![9_green_24.png](assets/9_green_24.png) **Einladung**<br>
Die Einladung ist eine Funktion der Datenerhebung. Werden nun vom Datengenerator mehrere Datenerhebungen automatisch generiert, werden in den Datenerhebungen das Versanddatum der Einladung in Abhängigkeit des jeweiligen Startdatums und des hier eingetragenen Wertes berechnet.

![10_green_24.png](assets/10_green_24.png) ![11_green_24.png](assets/11_green_24.png)**Erinnerungen**<br>
Auch die Erinnerungen sind eine Funktion der Datenerhebung. Werden vom Datengenerator mehrere Datenerhebungen automatisch generiert, werden in den Datenerhebungen das Versanddatum der Erinnerung in Abhängigkeit des jeweiligen Startdatums und des hier eingetragenen Wertes berechnet.


![12_green_24.png](assets/12_green_24.png) **Durchführungsformate ausschliessen**<br>
Zu Kursen kann in den Metadaten ein Durchführungsformat angegeben werden. Es besteht die Möglichkeit, bei erzeugten Datenerhebungen bestimmte [Durchführungsformate](../../manual_admin/administration/Modules.de.md#kurs) auszuschliessen, z.B. wenn Prüfungskurse nicht berücksichtigt werden sollen.

![13_green_24.png](assets/13_green_24.png) **Bearbeitung einschränken**<br>
Die Bearbeitung des Generators kann auf Qualitätsverantwalter:innen eingeschränkt werden.


### Tab "Berechtigungen Report"

Die hier eingegebene Konfiguration wird 1:1 in die erstellten Datenerhebungen übertragen.
Siehe [Datenerhebung](Quality_Management_Data_Collections.de.md).


### Tab "Positivliste" {: #Quality_Management_Data_Collection_Generators_Type_Course_PositivList}

Wurde ein Generator erstellt, ergibt sich daraus eine Liste von Kursen, zu welchen Datenerhebungen generiert werden.

Wird zudem noch eine Positivliste definiert, werden nur noch Kurse für Datenerhebungen berücksichtigt, die sowohl in der ursprünglich vom Generator erzeugten Liste enthalten sind, als auch in dieser Positivliste.



### Tab "Negativliste" {: #Quality_Management_Data_Collection_Generators_Type_Course_NegativList}

Wurde ein Generator erstellt, ergibt sich daraus eine Liste von Kursen, zu welchen Datenerhebungen generiert werden. In der Negativliste können einzelne dieser Kurse ausgenommen werden.

!!! note "Hinweis"

    Es macht nur Sinn, entweder eine Positivliste oder eine Negativliste zu erstellen.<br> 
    Sollen **nur zu einem kleinen Teil der Kurse** Datenerhebungen gemacht werden, empfiehlt sich eine **Positivliste**.<br> Sollen **zum überwiegenden Teil der Kurse** Datenerhebungen gemacht werden, empfiehlt sich eine **Negativliste**.

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Generator Typ "Termine eines/einer Betreuer:in in einem Kurs" {: #QMgenerator_type_events}

![quality_management_data_collection_generator_events_v1_de](assets/quality_management_data_collection_generator_events_v1_de.png){ class="shadow lightbox" }

### Tab "Konfiguration"

![quality_management_data_collection_generator_events_config_v1_de.png](assets/quality_management_data_collection_generator_events_config_v1_de.png){ class="shadow lightbox" }


Siehe auch [Konfiguration im Typ Kurs](#Quality_Management_Data_Collection_Generators_Type_Course_Config).

![5_green_24.png](assets/5_green_24.png) **Rollen der Teilnehmer:innen**<br>

Die Kursmitglieder mit den hier ausgewählten Rollen können an der Datenerhebung teilnehmen.

* Besitzer:innen
* Alle Betreuer:innen (= alle Betreuer:innen des Kurses)
* Unterrichtende:r Betreuer:in (= Unterrichtende(r) am Termin, der zur Datenerhebung führt)
* Teilnehmer:innen

![6_green_24.png](assets/6_green_24.png) **Beurteilungsgegenstand**<br>
Der Generator trägt in der [Datenerhebung](Quality_Management_Data_Collections.de.md) den Beurteilungsgegenstand ein:

* Betreuer:in oder
* Kurs

!!! note "Hinweis"

    Gibt es in einem Kurs mehrere Betreuer:innen, welche die übrigen Kriterien erfüllen, wird pro Betreuer:in eine [Datenerhebung](Quality_Management_Data_Collections.de.md) initiiert.

![7_green_24.png](assets/7_green_24.png) **Minimale Anzahl Einheiten Betreuer:in**<br>
Die Datenerhebung findet nur statt, wenn der/die Betreuer:in die hier angegebene minmale Anzahl Einheiten in einem Kurs insgesamt hat. (Nicht nur die bereits durchgeführten Lektionen.)

![8_green_24.png](assets/8_green_24.png) **Maximale Anzahl Einheiten Betreuer:in**<br>
Die Datenerhebung findet nur statt, wenn der/die Betreuer:in die hier angegebene maximale Anzahl Einheiten in einem Kurs insgesamt nicht überschreitet.

!!! note "Beispiel"

    In der Datenerhebung für den Regelfall, sollen nur Betreuer:innen beurteilt werden, die mind. 10 Einheiten zu halten haben. Hierfür wird die minimale Anzahl Einheiten verwendet.
    
    Sollen nur selten unterrichtende Betreuer:innen beurteilt werden, kann in einem weiteren Generator eine Datenerhebung für Betreuer:innen mit einer maximalen Anzahl Einheiten erzeugt werden.

![9_green_24.png](assets/9_green_24.png) **Start der Datenerhebung**<br>

* Am letzten Termin (welchen der/die Betreuer:in in einem Kurs unterrichtet)
* Am Termin mit der Einheit x (Termine, die der/die Betreuer:in unterrichtet)

![10_green_24.png](assets/10_green_24.png) **Start x Minuten vor dem Ende des Termins**<br>

Wird die Befragung kurz vor dem Ende durchgeführt, ist in der Regel mit einer höheren Beteiligung zu rechnen.

![12_green_24.png](assets/12_green_24.png) **Ankündigung für Betreuer:innen (Tage vor Start der Datenerhebung)**<br>

Wenn hier keine Angaben gemacht werden, wird keine Ankündigung verschickt.
In manchen Fällen ist es sinnvoll, dass z.B. Betreuer:innen vorab eine Ankündigung erhalten und ggf. intervienieren können.

![13_green_24.png](assets/13_green_24.png) **Einladung (Tage nach Start der Datenerhebung)**<br>

Die Einladung ist eine E-Mail an die Teilnehmer:innen mit dem Link zum Formular. Wird keine Angabe gemacht, wird keine E-Mail verschickt, die Teilnehmenden müssen anderweitig informiert werden. (Z.B. durch Dozierende im Unterricht.)


![14_green_24.png](assets/14_green_24.png) ![15_green_24.png](assets/15_green_24.png) **Erinnerung (Tage nach Start der Datenerhebung)**<br>
Siehe auch [Konfiguration im Typ Kurs](#Quality_Management_Data_Collection_Generators_Type_Course_Config).



### Tab "Berechtigungen Report"

Die hier eingegebene Konfiguration wird 1:1 in die erstellten Datenerhebungen übertragen.
Siehe [Datenerhebung](Quality_Management_Data_Collections.de.md).


### Tab "Positivliste"

Siehe [Typ Kurs Positivliste](#Quality_Management_Data_Collection_Generators_Type_Course_PositivList).


### Tab "Negativliste"

Siehe [Typ Kurs Negativliste](#Quality_Management_Data_Collection_Generators_Type_Course_NegativList).

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Generator Typ "Element" {: #QMgenerator_type_element}

![quality_management_data_collection_generator_element_v1_de.png](assets/quality_management_data_collection_generator_element_v1_de.png){ class="shadow lightbox" }

### Tab "Konfiguration"

![quality_management_data_collection_generator_element_config_v1_de.png](assets/quality_management_data_collection_generator_element_config_v1_de.png){ class="shadow lightbox" }

Siehe auch [Konfiguration im Typ Kurs](#Quality_Management_Data_Collection_Generators_Type_Course_Config).

![6_green_24.png](assets/6_green_24.png) **Elementtyp**<br>

Zu jedem Element gibt es eine Datenerhebung.

Abhänging davon, wie das Produkt eingerichtet ist, können Elemente z.B. sein:

* Semester
* Lehrgang
* Modul

![7_green_24.png](assets/7_green_24.png) **Element Termin**<br>
Auslösende Startereignisse können beim Generator vom Typ "Element" sein:

* Beginn
* Ende

![8_green_24.png](assets/8_green_24.png) **Tage nach Element Termin**<br>
Der Start der Datenerhebung wird aus dem Startereignis und der hier eingetragenen Anzahl Tage berechnet.
Die Anzahl Tage kann auch negativ sein. 


### Tab "Berechtigungen Report"

Die hier eingegebene Konfiguration wird 1:1 in die erstellten Datenerhebungen übertragen.
Siehe [Datenerhebung](Quality_Management_Data_Collections.de.md).


### Tab "Positivliste"

Wurde ein Generator erstellt, ergibt sich daraus eine Liste von Ementen, zu welchen Datenerhebungen generiert werden.

Wird zudem noch eine Positivliste definiert, werden nur noch Elemente für Datenerhebungen berücksichtigt, die sowohl in der ursprünglich vom Generator erzeugten Liste enthalten sind, als auch in dieser Positivliste.


### Tab "Negativliste"

Wurde ein Generator erstellt, ergibt sich daraus eine Liste von Elementen, zu welchen Datenerhebungen generiert werden. In der Negativliste können einzelne dieser Elemente ausgenommen werden.

!!! note "Hinweis"

    Es macht nur Sinn, entweder eine Positivliste oder eine Negativliste zu erstellen.<br>Soll **nur zu einem kleinen Teil der Elemente** Datenerhebungen gemacht werden, empfiehlt sich eine **Positivliste**.<br> Soll **zum überwiegenden Teil der Elemente** Datenerhebungen gemacht werden, empfiehlt sich eine **Negativliste**.

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Generator einschalten {: #activate_QMgenerator}

Jeder neu erstellte Generator ist zunächst noch ausgeschaltet. So kann er in Ruhe konfiguriert werden. Das Einschalten und Aktivieren eines Generators erfolgt über den Button links oben.

![quality_management_data_collection_generator_switch_v1_de.png](assets/quality_management_data_collection_generator_switch_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Ein Editieren eines Generators ist nur möglich, wenn der Generator ausgeschaltet ist.

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---