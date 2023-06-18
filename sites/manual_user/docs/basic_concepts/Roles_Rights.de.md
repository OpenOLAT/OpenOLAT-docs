# Rollen und Rechte

:octicons-device-camera-video-24: **Video-Einführung**: [Benutzerverwaltung](<https://www.youtube.com/embed/V1RuH0q08J8>){:target="_blank”}

## Systemweite Rollen und Rechte

### Benutzertypen

OpenOlat arbeitet mit einem Rollen und Rechte Management. Zuerst wird zwischen 2 grundsätzlichen Benutzertypen unterschieden. Dies sind:

* **Anonymer Gast:** Gäste haben - ohne sich zu registrieren – beschränkten Zugang zu OpenOlat. Sie können für Gäste freigegebene Lerninhalte betrachten, sich jedoch nicht an den Lernaktivitäten beteiligen. Der Link zum Gastzugang befindet sich auf der Login-Seite. Weitere Informationen zum Gast finden Sie [hier](guest_access.de.md).
* **Registrierter Benutzer:** Jeder Benutzer hat einen eindeutigen Benutzernamen, der nach der Registrierung nicht mehr geändert werden kann. Benutzer können freigeschaltete Lerninhalte nutzen und sich an allen Lernaktivitäten beteiligen. Zudem hat jeder Benutzer eine individuell konfigurierbare Startseite und [Speicherplatz](../personal_menu/Personal_folders.de.md) zur Verfügung. Darüber hinaus kann er Gruppen erstellen.

!!! info "Info"

    Bei registrierten Benutzern ohne weitere Rollen und Rechte handelt es sich in der Regel um die Lernenden.

### Rollen

Registrierte Benutzer können zusätzlich eine oder mehrere Rollen erhalten.

Hier ein Überblick über alle OpenOlat Rollen.

![Rollen in OpenOlat](assets/roles_DE.png)

* **Benutzer**: Standardrolle (siehe oben)
* **Autor**: Der Autor hat Zugriff auf den Autorenbereich. Damit ist er berechtigt, Kurse und alle weiteren Lernressourcen zu erstellen. In der Suchmaske findet der Autor alle Kurse und Lernressourcen wie Tests, Filme und Portfoliovorlagen, welche für Autoren zugänglich sind. Diese Rolle wird häufig an Lehrende oder E-Learning Verantwortliche vergeben.  
* **Benutzerverwalter**: Der Benutzerverwalter hat Zugriff auf die [Benutzerverwaltung](../../manual_admin/usermanagement/index.de.md) und alle Benutzer der eigenen Organisation. Er kann Benutzer erstellen, bearbeiten und inaktiv setzen. Zudem kann er die Rolle Autor vergeben.
* **Rollenverwalter**: Der Rollenverwalter hat Zugriff auf die Benutzerverwaltung und alle Benutzer der eigenen Organisationen. Er kann, ausser die Rollen Administrator und Systemadministrator, alle Rollen der Benutzer ändern, sie vergeben und entfernen.
* **Gruppenverwalter**: Der Gruppenverwalter hat Zugriff auf den Bereich Gruppen und darin Zugriff auf den Tab Gruppenverwaltung. Weitere Informationen zu Gruppen allgemein finden Sie [hier](../groups/index.de.md).
* **Poolverwalter**: Der Poolverwalter hat Zugriff auf den [Fragenpool](../area_modules/Question_Bank.de.md). Im Fragenpool kann er den Bereich Administration öffnen.
* **Curriculumverwalter**: Der Curriculumverwalter hat Zugriff auf die [Curriculumverwaltung](../area_modules/Curriculum_Management.de.md). Er kann neue Curricula erstellen und bereits bestehende verwalten. Ist der Curriculumverwalter einer Organisation zugeordnet, so besitzt er nur Zugang zu Curricula dieser Organisation.
* **Lektionenblockverwalter**: Konfiguration des Moduls "[Lektionen und Absenzen](../learningresources/Lectures_and_absences.de.md)"  
* **Qualityverwalter**: Der Qualityverwalter hat Zugriff auf den Bereich Qualitätsmanagement und kann dort sämtliche Einstellungen und Objekte wie Fragebögen, Datenerhebungsgeneratoren sowie das Analysewerkzeug verwalten.
* **Linienvorgesetzter**: Der Linienvorgesetzte kann für alle Benutzer innerhalb seiner Organisation automatisch über den Erhalt von Zertifikaten informiert werden.
* **Lernressourcenverwalter**: Ein Lernressourcenverwalter hat automatisch Besitzerrechte (= Vollzugriff) für alle Kurse und Lernressourcen, die der eigenen Organisation (siehe [Administrative Freigabe](../learningresources/Access_configuration.de.md#administrative-freigabe)) angehören. Im Status "Beendet" und "Gelöscht" ist der Zugriff lesend. Über den Autorenbereich sind die Kurse und Lernressourcen auffindbar und können kopiert sowie exportiert werden.
* **Principal**: Der Principal sieht – ausser der Administration – alle Bereiche des Systems, hat aber nur Lesezugriff und kann keine Änderungen vornehmen, Objekte bearbeiten etc.
* **Administrator**: Der Administrator besitzt Modul- und Funktionsverwaltung und hat auf alle Bereiche des Systems z.B.  Benutzerverwaltung, Katalogverwaltung, Curriculumverwaltung, Lektionenverwaltung Zugriff, ausser auf die Administrationsseite. Diese Rolle kann auf eine Organisation beschränkt werden. Der Administrator kann Benutzer löschen und zudem weiteren Personen das Recht für die Katalogverwaltung einräumen.
* **Systemadministrator**: Der Systemadministrator hat Zugriff auf die Administrationsseite und ist für die technische Systemkonfiguration und deren Überwachung zuständig. Dies ist eine globale Rolle, die nicht an eine Organisation gebunden ist.

!!! warning "Hinweis"

    Die genannten Rollen stellen Optionen dar, normalen Usern systemweit umfangreiche weitere Rechte zu geben. In der Regel wird bei einer OpenOlat Instanz gezielt eine passende Rollenzusammensetzung gewählt und nicht alle spezifischen Rollen vergeben. Typisch ist eine Kombination aus Benutzer, Autor und Administrator bzw. Systemadministrator. Darüberhinausgehende Rollen ergeben sich aus der Struktur der jeweiligen Institution und der Nutzung von bestimmten Tools wie [Curriculum](../area_modules/Curriculum_Management.de.md) oder [Absenzen](../learningresources/Lectures_and_absences.de.md). Es ist also möglich, dass in Ihrer Instanz nicht alle potenziellen OpenOlat Rollen verwendet werden. 
    
    Wenden Sie sich bei Rückfragen bezüglich der Rollenvergabe an den jeweiligen Support Ihrer OpenOlat Instanz.

## Kursbezogene Rollen und Rechte

### Kursrollen

Wenn ein Benutzer einem Kurs hinzugefügt wird, kann definiert werden, welche
Mitgliederrechte der Benutzer in diesem einen Kurs erhalten soll. Zur Auswahl stehen:

* **Besitzer**: Dieser Benutzer hat alle Rechte im Kurs. Er kann den Kurs bearbeiten, Mitglieder verwalten und den Kurs auch löschen. Somit ist der Besitzer Kursadministrator.

    :octicons-device-camera-video-24: **Video-Einführung**: [Voraussetzungen für Autoren](<https://www.youtube.com/embed/L0jc_LBKXLE>){:target="_blank”}

* **Betreuer**: Der Kursbetreuer hat Zugriff auf das [Bewertungswerkzeug](../course_operation/Assessment_tool_-_overview.de.md) des Kurses, wie auch auf die Test- und Fragebogen-Statistik. Ein Kursbetreuer kann jedoch den Kurs weder im Kurseditor bearbeiten noch den Kurs löschen. Im Bewertungswerkzeug sieht der Kursbetreuer alle Kursteilnehmenden, jedoch keine Gruppenteilnehmenden. Weitere Details der Kursrolle Betreuer finden Sie [hier](coach.de.md).
* **Teilnehmer**: Ein Teilnehmer kann den Kurs öffnen und die bereitgestellten Kursbausteine und Inhalte bearbeiten (je nach Konfiguration). Ein Teilnehmer hat jedoch keine zusätzlichen Rechte im Kurs.

Neben den kursbezogenen Rollen können, je nach Konfiguration, auch [Gäste](guest_access.de.md) ohne OpenOlat Account Zugang zu einem Kurs erhalten.  

![Kursrollen](assets/course_rights_DE.png){ class="shadow" }

!!! success "Rollenwechsel"

    Es ist ferner möglich, dass Personen mehrere Kursrollen erhalten und so verschiedene Perspektiven auf den Kurs einnehmen können. Ein Rollenwechsel ist, nachdem einer Person mehrere kursbezogene Rollen zugewiesen wurden, über den Wechsel der "Benutzerrolle" in der Toolbar des Kurses möglich.
    
    Ferner bietet es sich an, dass auch der Besitzer des Kurses sich in den weiteren Rollen im Kurs einträgt um so den Kurs aus einer anderen Perspektive/Rolle zu betrachten.

    ![Benutzer Rollenwechsel](assets/user_role_switch_DE.png){ class="shadow" }

### Gruppenrollen

Werden in Kursen Gruppen verwendet, können die Mitglieder entweder als Gruppeteilnehmer oder Gruppenbetreuer eingetragen werden.

* **Gruppenbetreuer**: Der Gruppenbetreuer hat praktisch die gleichen Rechte wie der Kursbetreuer, jedoch nur für seine Gruppe. Er hat also Zugriff auf das Bewertungswerkzeug und die Test und Fragebogen Statistik. Im Bewertungswerkzeug sieht er jedoch nur die **Teilnehmer** seiner Gruppe.
* **Gruppenteilnehmer**: Der Gruppenteilnehmer hat die gleichen Rechte wie der Kursteilnehmer.

Im Rechtemanagement können weitergehende Rechtepakete entweder an Gruppen Teilnehmende oder Gruppen Betreuer vergeben werden.

![Zusätzliche Rechte im Kurs konfigurieren](assets/memebers_managent_DE.png){ class="shadow" }

!!! warning "Kurs-/Gruppenrollen"
    Sowohl die Kurs- als auch die Gruppenrechte sind unabhängig von der _systemweiten Rolle_, welche ein Benutzer in der Benutzerverwaltung erhalten hat. Ein registrierter Benutzer ohne zugewiesene Rolle kann auch Kursbesitzer, Kursbetreuer oder Gruppenbetreuer sein.

!!! danger "Zugriff Bewertungswerkzeug"
    Möchte man vermeiden, dass eine Person auf das Bewertungswerkzeug zugreifen kann, sollte man ihr weder im Kurs noch in der Gruppe Betreuerrechte geben!

!!! danger "Zugriff Mitgliederverwaltung"
    Personen, die das Recht "[Mitgliederverwaltung](../learningresources/Members_management.de.md)" haben, können sowohl sich selbst weitere Rechte geben als auch andere Mitglieder des Kurses, auch den Ersteller oder andere Besitzer, entfernen oder deren Rechteumfang reduzieren.
