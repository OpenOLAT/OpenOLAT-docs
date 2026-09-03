# Qualitätsmanagement: Datenerhebungsgeneratoren {: #Quality_Management_Data_Collection_Generators}


!!! tip "Empfehlung"

    Für das Verständnis des Datenerhebungsgenerators werden Kenntnisse über Datenerhebungen vorausgesetzt.


## Was macht ein Datenerhebungsgenerator? {: #QMgenerator_function}

**Datenerhebungen** können im Modul Qualitätsmanagement auch **automatisiert nach bestimmten Regeln** erstellt werden.

Die Beschreibung und Einrichtung der Regeln geschieht in sogenannten **Datenerhebungsgeneratoren**.

![Ein Datenerhebungsgenerator erzeugt aus einer Formular-Lernressource mehrere Datenerhebungen mit je eigenem Personenkreis und Abgabetermin](assets/quality_management_scheme_generator_v1_de.png){ class="lightbox" }


## Wie wird ein Datenerhebungsgenerator erstellt? {: #create_QMgenerator}

Bei entsprechender Berechtigung (Rolle) erscheint in Ihrer Hauptnavigation das **Qualitätsmanagement**. Klicken Sie auf den Link im Abschnitt **"Datenerhebungsgeneratoren"**.

![Abschnitt Datenerhebungsgeneratoren und Eintrag Qualitätsmanagement im Menü Mehr markiert, Startseite des Qualitätsmanagements](assets/quality_management_data_collection_generators_v1_de.png){ class="shadow lightbox" }

Erstellen Sie dort einen neuen Datenerhebungsgenerator.

![Button Generator erstellen markiert, über der leeren Liste der Datenerhebungsgeneratoren](assets/quality_management_data_collection_generators_create_v1_de.png){ class="shadow lightbox" }

Mit der Wahl eines Typs bestimmen Sie das Regel-Set, nach dem Datenerhebungen erstellt werden.

![Auswahlliste Typ im Dialog Generator erstellen mit den Einträgen Kurs, Termine eines/einer Betreuer:in in einem Kurs und Element](assets/quality_management_data_collection_generators_type_v2_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Generator Typ "Kurs" {: #QMgenerator_type_course}

![Typ Kurs im Dialog Generator erstellen markiert, darunter das Feld Titel des Generators](assets/quality_management_data_collection_generator_course_v1_de.png){ class="shadow lightbox" }

### Tab "Konfiguration" {: #Quality_Management_Data_Collection_Generators_Type_Course_Config}

![Tab Konfiguration eines Generators vom Typ Kurs mit 13 nummerierten Feldern von Titel des Generators bis Bearbeitung einschränken, oben die Tabs Berechtigungen Report, Positivliste und Negativliste](assets/quality_management_data_collection_generator_course_config_v2_de.png){ class="shadow lightbox" }

![1](assets/1_green_24.png) **Titel des Generators**<br>
Verwenden Sie möglichst einen Titel, der eine Aussage zu Inhalt und Verwendung macht, um eine klare Zuordnung und Abgrenzung zu anderen Generatoren zu ermöglichen.

![2](assets/2_green_24.png) **Organisationen**<br>
Wurde das Modul "Organisationseinheiten" aktiviert und eingerichtet, können Datenerhebungen auch auf ausgewählte Organisationseinheiten bezogen werden.

![3](assets/3_green_24.png) **Formular**<br>
Auch bei Datenerhebungsgeneratoren kommt jeweils nur ein Formular zum Einsatz um Vergleichbarkeit und Auswertung zu ermöglichen. Soll ein weiteres Formular verwendet werden, müssten Sie einen weiteren Generator erstellen.

![4](assets/4_green_24.png) **Titel der Datenerhebung**<br>
Geben Sie hier den Titel der vom Datenerhebungsgenerator erzeugten Datenerhebungen an.
Im Titel können auch Variablen verwendet werden.

![5](assets/5_green_24.png) **Rollen der Teilnehmer:innen**<br>
Die Kursmitglieder mit den hier ausgewählten Rollen können an der Datenerhebung teilnehmen. Es besteht die Möglichkeit, diese Datenerhebung z.B. ausschliesslich unter Betreuer:innen zu machen.

![6](assets/6_green_24.png) **Startereignis**<br>
Auslösende Startereignisse können beim Generator vom Typ "Kurs" sein:

* Kursbeginn
* Kursende
* täglich

![7](assets/7_green_24.png) **Tage nach Kurstermin**<br>
(Diese Option wird nur angezeigt, wenn "Kursbeginn" oder "Kursende" als Startereignis gewählt wurde.)<br>
Der Start der Datenerhebung wird aus dem Startereignis und der hier eingetragenen Anzahl Tage berechnet.
Die Anzahl Tage kann auch negativ sein.

**Wochentag**<br>
(Diese Option wird nur angezeigt, wenn "täglich" als Startereignis gewählt wurde.)<br>
Es wird periodisch immer an den angegebenen Wochentagen eine Datenerhebung generiert.

!!! note "Hinweis"

    Hat ein Kurs ein Beginn- oder Enddatum, wird er vor und nach diesen Daten nicht in den Datenerhebungen berücksichtigt.

![8](assets/8_green_24.png) **Dauer der Datenerhebung (Stunden)**<br>
Nach Start der Datenerhebung können alle Teilnehmenden im angegebenen Zeitraum das Formular ausfüllen und abgeben. Nach Ablauf dieser Frist ist eine Abgabe nicht mehr möglich.

![9](assets/9_green_24.png) **Einladung**<br>
Die Einladung ist eine Funktion der Datenerhebung. Werden nun vom Datenerhebungsgenerator mehrere Datenerhebungen automatisch generiert, werden in den Datenerhebungen das Versanddatum der Einladung in Abhängigkeit des jeweiligen Startdatums und des hier eingetragenen Wertes berechnet.

![10](assets/10_green_24.png) ![11](assets/11_green_24.png) **Erinnerungen**<br>
Auch die Erinnerungen sind eine Funktion der Datenerhebung. Werden vom Datenerhebungsgenerator mehrere Datenerhebungen automatisch generiert, werden in den Datenerhebungen das Versanddatum der Erinnerung in Abhängigkeit des jeweiligen Startdatums und des hier eingetragenen Wertes berechnet.


![12](assets/12_green_24.png) **Durchführungsformate ausschliessen**<br>
Zu Kursen kann in den Metadaten ein Durchführungsformat angegeben werden. Es besteht die Möglichkeit, bei erzeugten Datenerhebungen bestimmte [Durchführungsformate](../../manual_admin/administration/Modules.de.md#course) auszuschliessen, z.B. wenn Prüfungskurse nicht berücksichtigt werden sollen.

![13](assets/13_green_24.png) **Bearbeitung einschränken**<br>
Mit der Checkbox "Nur Qualitätsverwalter:innen können bearbeiten" wird die Bearbeitung des Generators auf Qualitätsmanager:innen eingeschränkt.


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

![Typ Termine eines/einer Betreuer:in in einem Kurs im Dialog Generator erstellen markiert](assets/quality_management_data_collection_generator_events_v1_de.png){ class="shadow lightbox" }

### Tab "Konfiguration"

![Tab Konfiguration eines Generators vom Typ Termine eines/einer Betreuer:in in einem Kurs mit 17 nummerierten Feldern von Titel des Generators bis Bearbeitung einschränken](assets/quality_management_data_collection_generator_events_config_v1_de.png){ class="shadow lightbox" }


Siehe auch [Konfiguration im Typ Kurs](#Quality_Management_Data_Collection_Generators_Type_Course_Config).

![5](assets/5_green_24.png) **Rollen der Teilnehmer:innen**<br>

Die Kursmitglieder mit den hier ausgewählten Rollen können an der Datenerhebung teilnehmen.

* Besitzer:innen
* Alle Betreuer:innen (= alle Betreuer:innen des Kurses)
* Unterrichtende:r Betreuer:in (= unterrichtende Person am Termin, der zur Datenerhebung führt)
* Teilnehmer:innen

![6](assets/6_green_24.png) **Beurteilungsgegenstand**<br>
Der Generator trägt in der [Datenerhebung](Quality_Management_Data_Collections.de.md) den Beurteilungsgegenstand ein:

* Betreuer:in oder
* Kurs

!!! note "Hinweis"

    Gibt es in einem Kurs mehrere Betreuer:innen, welche die übrigen Kriterien erfüllen, wird pro Betreuer:in eine [Datenerhebung](Quality_Management_Data_Collections.de.md) initiiert.

![7](assets/7_green_24.png) **Minimale Anzahl Einheiten Betreuer:in**<br>
Die Datenerhebung findet nur statt, wenn der/die Betreuer:in die hier angegebene minimale Anzahl Einheiten in einem Kurs insgesamt hat. (Nicht nur die bereits durchgeführten Lektionen.)

![8](assets/8_green_24.png) **Maximale Anzahl Einheiten Betreuer:in**<br>
Die Datenerhebung findet nur statt, wenn der/die Betreuer:in die hier angegebene maximale Anzahl Einheiten in einem Kurs insgesamt nicht überschreitet.

!!! note "Beispiel"

    In der Datenerhebung für den Regelfall, sollen nur Betreuer:innen beurteilt werden, die mind. 10 Einheiten zu halten haben. Hierfür wird die minimale Anzahl Einheiten verwendet.

    Sollen nur selten unterrichtende Betreuer:innen beurteilt werden, kann in einem weiteren Generator eine Datenerhebung für Betreuer:innen mit einer maximalen Anzahl Einheiten erzeugt werden.

![9](assets/9_green_24.png) **Start der Datenerhebung**<br>

* Am letzten Termin (welchen der/die Betreuer:in in einem Kurs unterrichtet)
* Am Termin mit der Einheit x (Termine, die der/die Betreuer:in unterrichtet)

![10](assets/10_green_24.png) **Start x Minuten vor dem Ende des Termins**<br>

Wird die Befragung kurz vor dem Ende durchgeführt, ist in der Regel mit einer höheren Beteiligung zu rechnen.


![11](assets/11_green_24.png) **Dauer der Datenerhebung (Tage)**<br>

Nach Start der Datenerhebung können alle Teilnehmenden im angegebenen Zeitraum das Formular ausfüllen und abgeben. Nach Ablauf dieser Frist ist eine Abgabe nicht mehr möglich.

![12](assets/12_green_24.png) **Ankündigung für Betreuer:innen (Tage vor Start der Datenerhebung)**<br>

Wenn hier keine Angaben gemacht werden, wird keine Ankündigung verschickt.
In manchen Fällen ist es sinnvoll, dass z.B. Betreuer:innen vorab eine Ankündigung erhalten und ggf. intervenieren können.

![13](assets/13_green_24.png) **Einladung (Tage nach Start der Datenerhebung)**<br>

Die Einladung ist eine E-Mail an die Teilnehmer:innen mit dem Link zum Formular. Wird keine Angabe gemacht, wird keine E-Mail verschickt, die Teilnehmenden müssen anderweitig informiert werden. (Z.B. durch Dozierende im Unterricht.)


![14](assets/14_green_24.png) ![15](assets/15_green_24.png) **Erinnerung (Tage nach Start der Datenerhebung)**<br>
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

![Typ Element im Dialog Generator erstellen markiert](assets/quality_management_data_collection_generator_element_v1_de.png){ class="shadow lightbox" }

### Tab "Konfiguration"

![Tab Konfiguration eines Generators vom Typ Element mit 13 nummerierten Feldern, darunter Elementtyp, Element Termin und Tage nach Element Termin](assets/quality_management_data_collection_generator_element_config_v1_de.png){ class="shadow lightbox" }

Siehe auch [Konfiguration im Typ Kurs](#Quality_Management_Data_Collection_Generators_Type_Course_Config).

![6](assets/6_green_24.png) **Elementtyp**<br>

Zu jedem Element gibt es eine Datenerhebung.

Abhängig davon, wie das Produkt eingerichtet ist, können Elemente z.B. sein:

* Semester
* Lehrgang
* Modul

![7](assets/7_green_24.png) **Element Termin**<br>
Auslösende Startereignisse können beim Generator vom Typ "Element" sein:

* Beginn
* Ende

![8](assets/8_green_24.png) **Tage nach Element Termin**<br>
Der Start der Datenerhebung wird aus dem Startereignis und der hier eingetragenen Anzahl Tage berechnet.
Die Anzahl Tage kann auch negativ sein.


### Tab "Berechtigungen Report"

Die hier eingegebene Konfiguration wird 1:1 in die erstellten Datenerhebungen übertragen.
Siehe [Datenerhebung](Quality_Management_Data_Collections.de.md).


### Tab "Positivliste"

Wurde ein Generator erstellt, ergibt sich daraus eine Liste von Elementen, zu welchen Datenerhebungen generiert werden.

Wird zudem noch eine Positivliste definiert, werden nur noch Elemente für Datenerhebungen berücksichtigt, die sowohl in der ursprünglich vom Generator erzeugten Liste enthalten sind, als auch in dieser Positivliste.


### Tab "Negativliste"

Wurde ein Generator erstellt, ergibt sich daraus eine Liste von Elementen, zu welchen Datenerhebungen generiert werden. In der Negativliste können einzelne dieser Elemente ausgenommen werden.

!!! note "Hinweis"

    Es macht nur Sinn, entweder eine Positivliste oder eine Negativliste zu erstellen.<br>Soll **nur zu einem kleinen Teil der Elemente** Datenerhebungen gemacht werden, empfiehlt sich eine **Positivliste**.<br> Soll **zum überwiegenden Teil der Elemente** Datenerhebungen gemacht werden, empfiehlt sich eine **Negativliste**.

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Generator einschalten {: #activate_QMgenerator}

Jeder neu erstellte Generator ist zunächst noch ausgeschaltet. So kann er in Ruhe konfiguriert werden. Das Einschalten und Aktivieren eines Generators erfolgt über den Button links oben.

![Button Ausgeschaltet links oben markiert, über den Tabs Konfiguration, Berechtigungen Report, Positivliste und Negativliste eines Generators](assets/quality_management_data_collection_generator_switch_v1_de.png){ class="shadow lightbox" }

!!! note "Hinweis"

    Das Editieren eines Generators ist nur möglich, wenn der Generator ausgeschaltet ist.

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)

---


## Weiterführende Informationen {: #further_information}

[Module: Übersicht >](../../manual_admin/administration/Modules.de.md)<br>
[Qualitätsmanagement: Datenerhebung >](Quality_Management_Data_Collections.de.md)

[Zum Seitenanfang ^](#Quality_Management_Data_Collection_Generators)
