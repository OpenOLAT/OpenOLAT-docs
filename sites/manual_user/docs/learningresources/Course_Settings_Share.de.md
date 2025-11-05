# Kurseinstellungen - Tab Freigabe {: #tab_share}

Im Tab Freigabe finden Sie die Abschnitte

 ![1_green_24.png](assets/1_green_24.png) [Verwendung](#section_usage)<br>
![2_green_24.png](assets/2_green_24.png) [Freigabe](#section_share)<br>
![3_green_24.png](assets/3_green_24.png) [Angebot](#section_offer)<br>
![4_green_24.png](assets/4_green_24.png) [LTI 1.3 Zugriffskonfiguration](#section_LTI)<br>
![5_green_24.png](assets/5_green_24.png) [Freigabeübersicht](#section_share_overview)<br>

<br>

![course_settings_share1_v1_de.png](assets/course_settings_share1_v1_de.png){ class="shadow lightbox"}

---

## ![1_green_24.png](assets/1_green_24.png) Abschnitt Verwendung {: #section_usage}

Wird kein Course Planner verwendet, sind die Kurse eigenständig.

![course_settings_share_usage1_v1_de.png](assets/course_settings_share_usage1_v1_de.png){ class="shadow lightbox"}


!!! warning "Achtung"

    Durch Klick auf "Ändern" kann eine andere Verwendung gewählt werden. Beachten Sie jedoch, dass bei anderen Verwendungen die Mitgliederverwaltung nicht im Kurs erfolgt. Deshalb ist eine Änderung nicht mehr möglich, wenn bereits Mitglieder zu einem Kurs hinzugefügt wurden. 


![course_settings_share_usage2_v1_de.png](assets/course_settings_share_usage2_v1_de.png){ class="shadow lightbox"}


**Eigenständig**<br>
Eigenständige Lernressourcen besitzen eine eigene Mitgliederverwaltung. Zum Hinzufügen neuer Mitglieder öffnen Sie also im Kurs "Administration > Mitgliederverwaltung".<br>
Der Zugang kann mit der Buchungsmethode "Privat" durch Eintragung als Mitglied (z.B. durch Kursbesitzer:innen), durch Vergabe eines Zugangscodes oder über eine Veröffentlichung im Katalog erfolgen.

**Einbindung in Produkt**<br>
Wird der Kurs in ein Produkt eingebunden, werden die Mitgliedschaften durch den Course Planner vergeben und verwaltet. Der Kurs benötigt dann keine zweite, eigenständige Mitgliederverwaltung.

**Template**<br>
Auch diese Kurse sind durch den Course Planner verwaltet und ohne eigenständige Mitgliederverwaltung. Der Unterschied zur Option "Verwendung im Course Planner" besteht darin, dass ein Template zur Instanzierung verwendet wird. Der Kurs in einer Durchführung wird erst zu einem bestimmten Zeitpunkt aus diesem Template erstellt (instanziert).

!!! hint "Hinweis"

    Achten Sie beim Erstellen neuer Kurse darauf, welcher Verwendungszweck voreingestellt ist. Administrator:innen können den standardmässigen Verwendungszweck für neue Kurse einstellen unter **Administration > Module > Modul Courser Planner > Tab Course Planner**

[Zum Seitenanfang ^](#tab_share)

---


## ![2_green_24.png](assets/2_green_24.png) Abschnitt Freigabe {: #section_share}
![course_settings_share_share_v1_de.png](assets/course_settings_share_share_v1_de.png){ class="shadow lightbox"}

**Zugang für Teilnehmer:innen**<br>
Bei der Wahl **"Privat"** werden die Teilnehmenden durch die Kursbesitzer:in bzw. Personen, die über das Recht der Mitgliederverwaltung verfügen, hinzugefügt. Dies geschieht im Kurs unter "Administration > Mitgliederverwaltung". Es ist also wie eine persönliche Einladung in den Kurs durch Kursbesitzer:innen.<br>
Bei der Wahl der Option **"Buchbare und offene Angebote"** können die Lernenden einen Kurs selbst buchen, müssen aber eventuell (je nach Einstellung) ein Passwort eingeben. Soll die Buchung nach Wahl eines Angebots im Katalog erfolgen, muss ebenfalls diese Option angewählt sein. 

**Direktlink**<br> 
Wenn Sie diesen Link weitergeben, kann damit dieser Kurs direkt aufgerufen werden. Ist die Person noch nicht in OpenOlat bekannt (registriert) und eingeloggt, erscheint zunächst der Login-Bildschirm.

**Teilnehmer:innen können austreten**<br>
**Jederzeit**: Möchten Teilnehmende ihre Mitgliedschaft im Kurs selbst beenden, können sie das jederzeit tun.<br>
**Nach Enddatum**: Ein Beenden der Kursmitgliedschaft aus Eigeninitiative der Teilnehmenden ist nur nach Ende des Durchführungszeitraums möglich. Wurde diese Option gewählt ohne zuvor in der Beschreibung einen Durchführungszeitraum zu wählen, wird es den Teilnehmenden zu keinem Zeitpunkt gestattet sein, den Kurs zu verlassen.<br>
**Nie**: Der Besuch des Kurses ist Pflicht und Teilnehmer:innen können deshalb nicht selbst austreten.

**Administrative Freigabe**<br>
Aus den hier ausgewählten Organisationseinheiten können Personen mit bestimmten übergeordneten Rollen (z.B. Administrator:innen, Lernressourcenverwalter:innen) ebenfalls auf diesen Kurs zugreifen. Weil es diese Rollen pro Organisationseinheit gibt (z.B. Admin für Abteilung xy), können Sie hier bestimmen, welche Organisationseinheiten administrativen Zugriff auf Ihren Kurs erhalten werden.
Ist das Modul Organisationseinheiten nicht aktiviert, finden Sie hier nur eine einzige Organisation (in der Regel "OpenOlat").<br> 
Wieviele Personen administrativ zugreifen können, sehen Sie in der [Freigabeübersicht >](#section_share_overview)

**Autor:innen können**<br>
Erlauben Sie hier, ob andere Autor:innen, ihren Kurs referenzieren, kopieren oder exportieren dürfen.

**Externe OER-Kataloge und Suchmaschinen**<br>
Mit OAI-PMH lassen sich Metadaten von Lernressourcen für Internet-Portale oder Kataloge ausserhalb OpenOlat freigeben, damit Suchmaschinen einen Inhalt besser finden können. (OER = Open Educational Resources)

Die Funktion muss zunächst generell durch einen/eine Administrator:in aktiviert werden.<br>
Damit die Informationen eines ganz bestimmten Kurses an die Suchmaschinen weiter gegeben werden, muss anschliessend der/die jeweilige Autor:in (Kursbesitzer:in) dies für den eigenen Kurs erlauben.

Mehr über OER finden Sie hier:<br>
How-To: [Kurse zur Indexierung freigeben >](../../manual_how-to/oai_pmh/oai_pmh.de.md#wie-sehe-ich-im-autorenbereich-welche-kurselernressourcen-zur-indexierung-freigegeben-sind)<br>
Admin-Handbuch: [Modul OAI PMH >](../../manual_admin/administration/Modules_OAI.de.md)

[Zum Seitenanfang ^](#tab_share)

---

## ![3_green_24.png](assets/3_green_24.png) Abschnitt Angebote {: #section_offer}

![course_settings_share_offer_v1_de.png](assets/course_settings_share_offer_v1_de.png){ class="shadow lightbox"}

Damit ein Kurs im Katalog aufgeführt wird, muss ein Angebot erstellt werden. Es können auch mehrere Angebote erstellt werden, wenn der gleiche Kurs zu verschiedenen Bedingungen angeboten werden soll (z.B. kostenlos für eine bestimmte Zielgruppe, kostenpflichtig für andere).

Damit ein Angebot für den Katalog erstellt werden kann, muss im Abschnitt "Freigabe" bei "Zugang für Teilnehmer:innen" die Option "Buchbare und offene Angebote" gewählt sein. 


Mehr über Angebote und den Katalog finden Sie hier:<br>
[Katalog >](../area_modules/catalog2.0.de.md)<br>
[Angebotsarten >](../learningresources/Offer_Types.de.md)<br>
[Angebote erstellen >](../area_modules/catalog2.0_angebote.de.md)<br>
[Anbieten von Durchführungen im Katalog >](../area_modules/Course_Planner_Implementations.de.md#tab_catalog)<br>

[Zum Seitenanfang ^](#tab_share)

---

## ![4_green_24.png](assets/4_green_24.png) Abschnitt LTI 1.3 Zugriffskonfiguration {: #section_LTI}

OpenOlat-Kurse können via LTI 1.3 auch von einem anderen LMS aus aufgerufen werden. Für diesen Zugriff von aussen braucht es aber Sicherheitsvorkehrungen und genau festgelegte Berechtigungen.<br>
In diesem Abschnitt können Sie dazu ein sogenanntes Deployment einrichten, um den Kurs für ein anderes LMS aufrufbar zu machen.

Mehr über die Freigabe eines Kurses via LTI finden Sie hier:<br>
[LTI Zugang zu einem Kurs konfigurieren >](../learningresources/LTI_Share_courses.de.md)<br>

[Zum Seitenanfang ^](#tab_share)

---


## ![5_green_24.png](assets/5_green_24.png) Freigabeübersicht {: #section_share_overview}

![course_settings_share_overview_v2_de.png](assets/course_settings_share_overview_v2_de.png){ class="shadow lightbox"}

Im Block **Mitglieder** finden Sie die Anzahl der Kursmitglieder, aufgegliedert nach Besitzer:innen, Betreuer:innen und Teilnehmer:innen.

Im Block **Administrative Freigabe** sind alle Personen aufgeführt, die aufgrund ihrer Rolle ebenfalls Zugriff auf diesen Kurs haben.

Wurde der Kurs Gruppen zugeordnet, finden Sie die betreffenden Gruppen im Block **Gruppen** angezeigt.

Wurde der Kurs im Course Planner einem Produkt zugeordnet, finden Sie die Verwendungen im Block **Produkt** angezeigt.

[Zum Seitenanfang ^](#tab_share)

---


## Weiterführende Informationen {: #further_information}

[Zugangskonfiguration/Freigabe >](../learningresources/Acceess_configuration.de.md)<br>
[Katalog >](../area_modules/catalog2.0.de.md)<br>
[Angebotsarten >](../learningresources/Offer_Types.de.md)<br>
[Angebote erstellen >](../area_modules/catalog2.0_angebote.de.md)<br>
[Anbieten von Durchführungen im Katalog >](../area_modules/Course_Planner_Implementations.de.md#tab_catalog)<br>
[LTI Zugang zu einem Kurs konfigurieren >](../learningresources/LTI_Share_courses.de.md)<br>

[Zum Seitenanfang ^](#tab_share)

