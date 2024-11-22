# Rollen und Rechte: Welche Rollen gibt es? {: #roles} 


Entsprechend den Aufgaben lassen sich die Rollen folgenden Kontexten zuordnen:

## Organisationsweit gültige Rollen {: #org} 

Zu Organisationsrollen gehören organisationsweit (wie innerhalb der OpenOlat-Instanz definiert) gültige Berechtigungen. Die Organisationsrollen werden in der Benutzerverwaltung vergeben.

![roles_rights_system_roles_v1_de.png](assets/roles_rights_system_roles_v1_de.png)


* **Einladung**: Eingeladene Personen mit Benutzertyp "externe Benutzer:in" (Siehe [Benutzertypen](User_Types.de.md))
* **Benutzer:in**: Standardrolle für registrierte Personen 
* **Autor:in**: Autor:innen haben Zugriff auf den Autorenbereich in der obersten Navigation. Damit sind sie berechtigt, Kurse und alle weiteren Lernressourcen zu erstellen. In der Suchmaske finden Autor:innen alle Kurse und Lernressourcen wie Tests, Filme und Portfoliovorlagen, welche für sie zugänglich sind. Diese Rolle wird häufig an Lehrende oder E-Learning Verantwortliche vergeben.  
* **Benutzerverwalter:in**: Benutzerverwalter:innen haben Zugriff auf die [Benutzerverwaltung](../../manual_admin/usermanagement/index.de.md) und alle Benutzer:innen der eigenen Organisation. Sie können Benutzer:innen erstellen, bearbeiten und inaktiv setzen. Zudem können sie die Rolle Autor und weitere Rollen vergeben. Benutzerverwalter verfügen über den Menüpunkt "Benutzerverwaltung" in der obersten Navigation. 
* **Rollenverwalter:in**: Rollenverwalter:innen haben Zugriff auf die Benutzerverwaltung (separater Menüpunkt in der obersten Navigation) und können alle Benutzer:innen der eigenen Organisationen sehen und organisieren. Rollenverwalter können, ausser die Rollen Administrator und Systemadministrator, alle Rollen der Benutzer:innen ändern, sie vergeben und entfernen.
* **Gruppenverwalter:in**: Gruppenverwalter:innen haben im Menüpunkt "Gruppen" zusätzlich Zugriff auf den Tab [Gruppenverwaltung](../area_modules/Group_Management.de.md). 
* **Poolverwalter:in**: Poolverwalter:innen haben Zugriff auf den [Fragenpool](../area_modules/Question_Bank.de.md). Im Fragenpool können sie den Bereich Administration öffnen.
* **Curriculumverwalter:in**: Curriculumverwalter:innen haben Zugriff auf den Menüpunkt [Curriculumverwaltung](../area_modules/Curriculum_Management.de.md). Sie können neue Curricula erstellen und bereits bestehende verwalten. Sind Curriculumverwalter:innen einer Organisation zugeordnet, so besitzen sie nur Zugang zu Curricula dieser Organisation.
* **Lektionenblockverwalter:in**: Lektionenblockverwalter haben Zugriff auf den Menüpunkt "Lektionenverwaltung" in der obersten Navigation. Sie können sämtlich Lektionen und Absenzen inklusive der jeweiligen Benutzer:innen der eigenen Organisationen sehen.    
* **Projektverwalter:in**: Projektverwalter verfügen zusätzlich im Menüpunkt "Projekte" über den Tab "Administration" und haben hier Zugriff auf alle Projekte inklusive Mitgliederverwaltung und Konfiguration.
* **Qualityverwalter:in**: Qualityverwalter:innen haben Zugriff auf den Menüpunkt Qualitätsmanagement und können dort sämtliche Einstellungen und Objekte wie Fragebögen, Datenerhebungsgeneratoren sowie das Analysewerkzeug verwalten.
* **Linienvorgesetzte/r**: Linienvorgesetzte können für alle Benutzer innerhalb ihrer Organisation automatisch über den Erhalt von Zertifikaten informiert werden.
* **Lernressourcenverwalter:in**: Lernressourcenverwalter:innen haben automatisch Besitzerrechte (= Vollzugriff) für alle Kurse und Lernressourcen, die der eigenen Organisation (siehe [Administrative Freigabe](../learningresources/Access_configuration.de.md#administrative-freigabe)) angehören. Im Status "Beendet" und "Gelöscht" ist der Zugriff lesend. Über den Autorenbereich sind die Kurse und Lernressourcen auffindbar und können kopiert sowie exportiert werden.
* **Principal**: Der Principal sieht viele Bereiche des Systems, hat aber nur Lesezugriff und kann keine Änderungen vornehmen, Objekte bearbeiten etc.
* **Administrator:in**: Administrator:innen besitzen Modul- und Funktionsverwaltung und haben auf alle Bereiche des Systems z.B. Benutzerverwaltung, Katalogverwaltung, Curriculumverwaltung, Lektionenverwaltung Zugriff, ausser auf die Administrationsseite. Diese Rolle kann auf eine Organisation beschränkt werden. Administrator:innen können Benutzer:innen löschen und zudem weiteren Personen das Recht für die Katalogverwaltung einräumen.
* **Systemadministrator:in**: Systemadministrator:innen haben Zugriff auf die Administrationsseite und sind für die technische Systemkonfiguration und deren Überwachung zuständig. Dies ist eine globale Rolle, die nicht an eine Organisation gebunden ist.

!!! warning "Hinweis"

    Die genannten Rollen stellen Optionen dar, normalen Usern organisationsweit umfangreiche weitere Rechte zu geben. In der Regel wird bei einer OpenOlat Instanz gezielt eine passende Rollenzusammensetzung gewählt und nicht alle spezifischen Rollen vergeben. Typisch ist eine Kombination aus Benutzer:in, Autor:in und Administrator:in bzw. Systemadministrator:in. Darüber hinausgehende Rollen ergeben sich aus der Struktur der jeweiligen Institution und der Nutzung von bestimmten Tools wie [Curriculum](../area_modules/Curriculum_Management.de.md) oder [Absenzen](../learningresources/Lectures_and_absences.de.md). Es ist also möglich, dass in Ihrer Instanz nicht alle potenziellen OpenOlat-Rollen verwendet werden. 
    
    Wenden Sie sich bei Rückfragen bezüglich der Rollenvergabe an den jeweiligen Support Ihrer OpenOlat Instanz.

[zum Seitenanfang ^](#roles)

---

## Rollen in einem Kurs {: #course} 

![roles_rights_course_members_v1_de.png](assets/roles_rights_course_members_v1_de.png){ class=" shadow lightbox" }

Innerhalb eines Kurses unterscheiden wir die 3 Kursrollen: 

* **Besitzer:in**: Diese Benutzer:innen haben alle Rechte im Kurs. Sie können den Kurs bearbeiten, Mitglieder verwalten und den Kurs auch löschen. Somit ist der/die Besitzer:in Kursadministrator:in.

    :octicons-device-camera-video-24: **Video-Einführung**: [Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>){:target="_blank”}

* **Betreuer:in**: Der/die Kursbetreuer:in hat Zugriff auf das [Bewertungswerkzeug](../learningresources/Assessment_tool_overview.de.md) des Kurses, wie auch auf die Test- und Fragebogen-Statistik. Ein/eine Kursbetreuer:in kann jedoch den Kurs weder im Kurseditor bearbeiten noch den Kurs löschen. Im Bewertungswerkzeug sehen die Kursbetreuer:innen alle Kursteilnehmenden, jedoch keine Gruppenteilnehmenden. Weitere Details der Kursrolle Betreuer:in finden Sie [hier](coach.de.md).

* **Teilnehmer:in**: Teilnehmer:innen können den Kurs öffnen und die bereitgestellten Kursbausteine und Inhalte bearbeiten (je nach Konfiguration). Sie haben jedoch keine zusätzlichen Rechte im Kurs.

![Kursrollen](assets/course_rights_DE.png){ class="shadow" }

Neben den kursbezogenen Rollen können in herkömmlichen Kursen auch [Gäste](guest_access.de.md) ohne OpenOlat Account Zugang zu einem Kurs erhalten.  

!!! success "Rollenwechsel"

    Es ist ferner möglich, dass Personen mehrere Kursrollen erhalten und so verschiedene Perspektiven auf den Kurs einnehmen können. Ein Rollenwechsel ist, nachdem einer Person mehrere kursbezogene Rollen zugewiesen wurden, über den Wechsel der "Benutzerrolle" in der Toolbar des Kurses möglich.
      
    ![Benutzer Rollenwechsel](assets/user_role_switch_DE.png){ class="shadow" }


[zum Seitenanfang ^](#roles)

---

## Rollen in Gruppen {: #groups} 

Werden in Kursen Gruppen verwendet, können die Mitglieder entweder als Gruppenteilnehmer:innen oder Gruppenbetreuer:innen eingetragen werden.

* **Gruppenbetreuer:in**:<br>
Gruppenbetreuer:innen haben praktisch die gleichen Rechte wie die Rolle Kursbetreuer:in, jedoch nur für ihre Gruppe. Sie haben im Kurs also Zugriff auf das Bewertungswerkzeug und die Test und Fragebogen Statistik. Im Bewertungswerkzeug sehen sie jedoch nur die Teilnehmer ihrer eigenen Gruppe.

* **Gruppenteilnehmer:in**:<br>
Gruppenteilnehmer:innen haben die gleichen Rechte wie die Rolle Kursteilnehmer:in.

Im Rechtemanagement des Kurses können weitergehende *Rechtepakete* entweder an Gruppenteilnehmer:innen oder Gruppenbetreuer:innen vergeben werden.

![Zusätzliche Rechte im Kurs konfigurieren](assets/memebers_managent_DE.png){ class="shadow" }

!!! warning "Kurs-/Gruppenrollen"

    Sowohl die Kurs- als auch die Gruppenrechte sind unabhängig von der _systemweiten Rolle_, welche Benutzer:innen in der Benutzerverwaltung erhalten haben. Registrierte Benutzer:innen ohne zugewiesene Rolle können auch Kursbesitzer:in, Kursbetreuer:in oder Gruppenbetreuer:in sein.

!!! note "Hinweis"

    Gruppenteilnehmer:innen und Gruppenbetreuer:innen sind Rollen innerhalb einer bestimmten Gruppe. Die Rolle "Gruppenverwalter:in" ist dagegen eine organisationsweit gültige Rolle, denn ihre Aufgabe ist es gruppen**übergreifend** Verwaltungsaufgaben wahrzunehmen.

[zum Seitenanfang ^](#roles)

---

## Rollen in Curricula {: #curriculum} 

Ist das optionale Zusatzmodul "Curriculum" aktiviert, stehen neben üblichen Kursrollen noch weitere Rollen zur Verfügung, die an Mitglieder eines Curriculums vergeben werden können.

* Curriculumbesitzer:in
* Curriculumelementbesitzer:in
* Klassenlehrer:in (Master Coach)

* (Curriculum-)Kursbesitzer:in 
* (Curriculum-)Kursbetreuer:in
* (Curriculum-)Kursteilnehmer:in

**Die Rolle Curriculumbesitzer:in**<br>
Importiert oder erstellt eine Person mit Zugriff auf das Curriculummanagement (Curriculumverwalter:innen) ein neues Curriculum, wird diese Person zum Curriculumbesitzer/zur Curriculumbesitzerin. Damit ist dann insbesondere das Recht verbunden, das Curriculum zu strukturieren und dem Curriculum Kurse und (Curriculum-)Teilnehmer:innen hinzuzufügen.

![roles_rights_curriculum_owner_v1_de.png](assets/roles_rights_curriculum_owner_v1_de.png){ class=" shadow lightbox" }

**Die Rolle Curriculumelementbesitzer:in**<br>
Wie Besitzer:innen, haben auch Elementbesitzer:innen das Recht, das Curriculum zu strukturieren und dem Curriculum Kurse und (Curriculum-)Teilnehmer:innen hinzuzufügen - allerdings beschränkt auf ein Curriculumelement.

**Die Rolle Klassenlehrer:in (Master Coach)**<br>
Beispiel:<br>
Hat eine Klasse unterschiedliche Fächer (Fächer entsprechen in OpenOlat Curriculumelementen), dann haben die Klassenlehrer:innen Zugriff auf die verschiedenen Curriculumelemente (Leserecht), während Fachlehrer:innen (Curriculumelementbesitzer:innen) nur Zugriff auf ihr Curriculumelement (Fach) haben.


**Besitzer:in, Betreuer:in** und **Teilnehmer:in** sind die 3 Rollen von Kursmitgliedern. Ein Curriculum wird aus Kursen zusammengestellt. Deshalb gibt es diese 3 Rollen auch für alle Kurse eines bestimmten Curriculums - mit ein paar Besonderheiten. 

**Die Rolle (Curriculum-)Kursbesitzer:in**<br>
Im Normalfall können Benutzer:innen mit der organisationsweit gültigen Autorenrolle im Autorenbereich Kurse erstellen. In jedem neu erstellten Kurs erhält der/die Erstellerin automatisch die Kursrolle "Kursbesitzer:in". Die Rolle "Kursbesitzer:in" gilt jeweils für einen Kurs.

Wird ein/eine Benutzer:in zum Curriculumsmitglied und erhält **innerhalb des Curriculums** die Rolle "Kursbesitzer:in", wird die Person dadurch in **allen Kursen dieses Curriculums** zur Kursbesitzer:in.

Ausserhalb der Curriculumelemente hat ein/eine (Curriculum-)Kursbesitzer:in keine Autorenrechte, wenn er/sie nicht die organisationsweit gültige Rolle Autor:in innehat. 

Wird die Curriculummitgliedschaft entzogen, wird dadurch auch in allen Kurses dieses Curriculums die Besitzerrolle aus den Kursen entfernt.

Für die Rollen **(Curriculum-)Kursbetreuer:innen** und **(Curriculum-)Kursteilnehmer:innen** gilt Entsprechendes.

!!! note "Hinweis"

    Die vorstehend aufgeführten Rollen sind Rollen **innerhalb** eines bestimmten Curriculums. Die Rolle "Curriculumverwalter:in" ist dagegen eine organisationsweit gültige Rolle, denn ihre Aufgabe ist es curriculum**übergreifend** Verwaltungsaufgaben wahrzunehmen.<br>
    (Siehe [Curriculumverwaltung](../area_modules/Curriculum_Management.de.md))

[zum Seitenanfang ^](#roles)

---

## Rollen in einer Organisation {: #orgunit} 

Ist das optionale Zusatzmodul "Organisationseinheiten" aktiviert, können Rollen auch nur für eine bestimmte Organisationseinheit vergeben werden.

Benutzer:innen können Mitglied in verschiedenen Organisationseinheiten sein und dort jeweils unterschiedliche Rollen zugewiesen bekommen.

Zu den Rollen, die begrenzt auf eine Organisationseinheit vergeben werden können, gehören

* Alle Systembenutzer:innen
* Autor:innen
* Gruppenverwalter:innen
* Lektionenblockverwalter:innen
* Projektverwalter:innen
* Qualityverwalter:innen
* Poolverwalter:innen
* Benutzerverwalter:innen
* Rollenverwalter:innen
* Curriculumverwalter:innen
* Lernressourcenverwalter:innen
* Linienvorgesetzte
* Principals
* Administrator:innen

(Systemadministrator:innen sind per Definition für das Gesamtsystem zuständig und nicht auf Organisationseinheiten beschränkbar.)

Organisationsrollen werden in der Benutzerverwaltung vergeben.<br>
(Siehe [Rollenzuweisung organisationsspezifischer Rollen](Assign_Roles.de.md#role_assignment_orgunit))

!!! info "Ohne aktivierte Organisationseinheiten"

    Ist das Modul "Organisationseinheiten" nicht eingerichtet, sind alle Benutzer:innen automatisch Mitglieder in der einzigen vorhandenen Gesamtorganisation (OpenOlat) und alle Rollen beziehen sich darauf.

[zum Seitenanfang ^](#roles)

---

## Selbst definierte Rollen und Beziehungen {: #relations} 

Neben den in OpenOlat vorgegebenen Rollen gibt es auch die Möglichkeit, dass Administrator:innen selbst Rollen erstellen.<br>
(**Administration > Module > Rolle Benutzer zu Benutzer**)<br>
Diese frei definierbaren Rollen können von Adminstrator:innen mit spezifischen Rechten ausgestattet werden.

Für diese Rollen können mit Benutzer-zu-Benutzer-Beziehungen zum Beispiel kursübergreifende Betreuungsfunktionen wie Mentoren, Lernbegleiter und Vorgesetzte eingerichtet werden.<br>
(Siehe [Coaching - Personenbeziehungen](../../area_modules/coaching_personenbeziehungen.de.md))

**Voraussetzungen:**<br>
Bevor Beziehungen zwischen Rollen definiert werden können, müssen einerseits zuerst die **Rollen** vorhanden sein und es muss eine **Systematik** vorhanden sein (welche Rolle ist welcher anderen Rolle über- bzw. untergeordnet).

Die **Systematik** wird durch **Administrator:innen** festgelegt. 

Sind die Rollen und ihre Systematik eingerichtet, können anschliessend die Beziehungen in der **Benutzerverwaltung** bestimmt werden.<br>
(Siehe [Beziehungen definieren](Assign_Roles.de.md#role_assignment_relations))

[zum Seitenanfang ^](#roles)

---

## Rolle "Einladung" {: #invitee} 

Die Rolle "Einladung" ist für Personen, welche kein Benutzerkonto in OpenOlat haben und trotzem Daten in OpenOlat erfassen müssen. Sie erhalten eine Art Pseudo-Benutzerkonto, mit nur ganz wenigen Rechten. Die Rolle wird z.B. im Modul ePortfolio verwendet. Hier können die Verfasser:innen eines Beitrages auch externe Personen (z.B. den/die Lehrmeister:in) zur Beurteilung des Beitrages einladen. Diese externen Personen erhalten die Rolle "Einladung".

Die "Rolle", bzw. den zugehörigen Rechtestatus, erhalten alle Personen, die über die Option "**Externe Mitglieder einladen**" einem Kurs hinzugefügt wurden. Im Benutzermanagement sollte nur ausnahmsweise die Rolle "Einladung" zugeteilt werden. 

Als externe Benutzer:innen werden solche Personen nicht vollständig registriert (nur mit E-Mail) und haben deshalb **keine vollen Benutzerrechte**, wie die Standard-Rolle "Benutzer:in".<br>
(Siehe [Benutzertypen](User_Types.de.md))

(Seit Release 17.0 verfügbar.)

[zum Seitenanfang ^](#roles)

---

## Kontorollen {: #account_roles} 

Die Kontorollen sind nur für die Suchfunktion der Administrator:innen relevant.<br>
(Siehe [Kontorollen](../../manual_admin/usermanagement/Search_Users.de.md#kontorollen))

[zum Seitenanfang ^](#roles)


---


!!! danger "Zugriff Bewertungswerkzeug"

    Möchte man vermeiden, dass eine Person auf das Bewertungswerkzeug zugreifen kann, sollte man ihr weder im Kurs noch in der Gruppe Betreuerrechte geben!

!!! danger "Zugriff Mitgliederverwaltung"

    Personen, die das Recht "[Mitgliederverwaltung](../learningresources/Members_management.de.md)" haben, können sowohl sich selbst weitere Rechte geben als auch andere Mitglieder des Kurses, auch den/die Ersteller:in oder andere Besitzer:innen, entfernen oder deren Rechteumfang reduzieren.


[zum Seitenanfang ^](#roles)

---

## Weiterführende Informationen

[Rollenzuweisung für Organisationsrollen](Assign_Roles.de.md#role_assignment_org)<br>

[Rollenzuweisung für Kursrollen](Assign_Roles.de.md#role_assignment_course)<br> 

[Rollenzuweisung für Gruppenrollen](Assign_Roles.de.md#role_assignment_group)<br> 

[Rollenzuweisung für Curricula](Assign_Roles.de.md#role_assignment_curriculum)<br> 
[Rechte der Curriculum-Rollen](../basic_concepts/Authorisation_Concept.de.md#rechte-der-curriculum-rollen)<br> 

[Rollenzuweisung der "Einladung"](Assign_Roles.de.md#role_assignment_invitee)<br> 

[Eigene Rollen und Beziehungen definieren](Assign_Roles.de.md#role_assignment_relations)<br> 

<br>

[zum Seitenanfang ^](#roles)