# LTI-Zugang zu einer Gruppe konfigurieren [:octicons-tag-16:{ title="ab Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #LTI_access_to_a_group}

Mit LTI lassen sich nicht nur Inhalte (Kurse) auf einem anderen LMS nutzen. Via LTI können auch Daten über die Kursteilnehmer:innen und Betreuer:innen ausgetauscht werden (LTI-Services für das Provisioning von Namen und Rollen, sowie LTI-Services "Assignments and Grades"). 

So lassen sich z.B. Noten sicher mit dem Prüfungsamt via API austauschen. Es können auch Stärken und Schwächen der abgelieferten Arbeit mit den Studierenden diskutiert werden, wenn der besuchte Kurs von einem anderen LMS stammt und die Kommunikationsinfrastruktur des eigenen LMS dort nicht zur Verfügung steht.

## Richtung des Austauschs

Die Informationen zu Gruppen und Mitgliedern können grundsätzlich in beiden Richtungen ausgetauscht werden:

* von OpenOlat (= Tool) zum anderen LMS (= Platform)
* vom anderen LMS (= Tool) zu OpenOlat (= Platform)


![Austauschrichtungen zwischen OpenOlat und einem anderen LMS: OpenOlat als Tool oder als Platform](assets/LTI_share_groups_platform_tool_v1_de.png){ class="shadow lightbox" title="Rollen Tool und Platform zwischen zwei Systemen" }


## Voraussetzungen

Die externe Plattform wird in der System-Administration von OpenOlat erfasst, dafür braucht es einen Administrator-Zugang (in OpenOlat kann dies auch die Rolle Systemadministrator:in sein). Auf der Gegenseite braucht es ebenfalls einen Administrator-Zugang zum anderen LMS. Wer die LTI-Freigabe einer Gruppe vornehmen darf, legt die System-Administration fest: [Wer kann Deployments hinzufügen?](../../manual_admin/administration/LTI_Integrations.de.md#deployments)<br>
Vorzugsweise erfolgt die Konfiguration auf beiden Systemen gleichzeitig, da bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

## Ablauf der Konfiguration

1. Setup "External Tool" in Moodle
2. Setup "externe Plattform" in OpenOlat
3. LTI-Freigabe der Gruppe in OpenOlat
4. Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs
5. Verbindungstest

Der ausführliche Ablauf einer Konfiguration ist beschrieben unter [LTI-Zugang zu einem Kurs konfigurieren](../learningresources/LTI_Share_courses.de.md).



## Lernerdaten in der LTI Konfiguration

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_groups_course_element_page_content_v1_de.png" alt="Konfiguration der Lernerdaten und OpenOlat-Rollen im Tab Seiteninhalt des Kursbausteins LTI-Seite" />
</details>

**Vorname/Name übertragen:**<br> 
Wenn Sie diese Checkbox ankreuzen, wird der Vor- und Nachname der Person an die externe Lernapplikation weitergegeben. Ansonsten kann die Person die externe Lernapplikation anonym nutzen.

**E-Mailadresse übertragen:**<br>
Markieren Sie die Checkbox, wird die E-Mail-Adresse der Person an die externe Lernapplikation weitergegeben.

**Zusätzliche Attribute:**<br> 
In dieses Eingabefeld können Sie weitere Parameter eingeben, die an die Lernapplikation übermittelt werden sollen. So kann der Lernapplikation beispielsweise mitgeteilt werden, dass die Anfrage von der Lernplattform OpenOlat übermittelt wird. (Die externe Lernapplikation muss die weitergegebenen Informationen verarbeiten können, weshalb eine Absprache mit dem Anbieter nötig ist). Sie haben die Wahl zwischen statischen Text-Attributen (für alle Personen ist der Wert identisch) oder zusätzlichen dynamischen Benutzerattributen (pro Person unterschiedlich). Sie können beliebig viele Zusatzattribute definieren, die LTI-Ressource muss allerdings wissen, dass es diese Attribute gibt, da diese nicht im Standard definiert sind.

**OpenOlat Rollen:**<br>
In diesem Bereich können Sie definieren, welche Rolle die einzelnen Personen einnehmen, wenn sie die LTI-Ressource starten. Es werden dabei die drei OpenOlat-Kursrollen Besitzer:in, Betreuer:in und Teilnehmer:in unterstützt. Für jede Rolle kann genau definiert werden, welche Rollen dafür auf Seiten der LTI-Ressource angewendet werden sollen. Die folgenden LTI-Rollen können konfiguriert werden: Lerner, Instruktor, Administrator:in, Assistent Lehrperson, Inhaltersteller und Mentor.

**Punkte übertragen:**<br>
Wählen Sie diese Checkbox, wenn die LTI-Ressource Punkte erzeugen und mit dem LTI-Standard an OpenOlat übermitteln soll. Dies ist optional. Übermittelte Punkte erscheinen bei der Person auf der Startseite des LTI-Bausteins, sowie auf dem Leistungsnachweis. Bitte beachten Sie, dass LTI gemäss Standard nur einen Wert zwischen 0 und 1 liefern kann.

Wird die Option „Punkte übertragen“ aktiviert, kann die LTI-Seite als bewertbares Kurselement zum Kurs hinzugefügt werden und erscheint dann im Bewertungswerkzeug. Zusätzlich erscheinen die übermittelten Punkte bei der Person auf der Startseite des LTI-Bausteins.

**Skalierungsfaktor:**<br>
Mit dem Skalierungsfaktor können Sie die LTI-Resultate, die gemäss Standard einen Wert zwischen 0 und 1 einnehmen müssen, auf einen im OpenOlat-Kurs praktischeren Wert skalieren. Möchten Sie beispielsweise in OpenOlat maximal 10 Punkte für eine LTI-Aufgabe vergeben, so müssen Sie als Skalierungsfaktor den Wert "10" eintragen. Möchten Sie die Punkte unverändert übernehmen, wählen Sie den Wert "1".

**Notwendige Punktzahl für 'bestanden':**<br>
Geben Sie hier den optionalen Schwellenwert an, ab dem der Kursbaustein LTI-Seite als bestanden gilt. Dieser Schwellenwert bezieht sich auf das skalierte Endresultat und nicht auf die von LTI übermittelten Rohdaten! Im obigen Beispiel wäre ein Schwellwert von "5" gleichbedeutend mit "50%".


## Daten zur Gruppe per LTI übertragen

Eine OpenOlat-Gruppe wird für den LTI-Zugang genauso freigegeben wie ein Kurs. Die Freigabe erfolgt in der Gruppenverwaltung im Tab "Freigabe" im Abschnitt "LTI 1.3 Zugangskonfiguration" über die Schaltfläche "Neues Deployment hinzufügen".

Im Deployment-Dialog werden dieselben Angaben erfasst wie bei der Kursfreigabe: die zuvor konfigurierte "Plattform", die "Deployment-ID" sowie die technischen Adressen ("Tool URL", "Anmelde-URL", "Umleitungs-URL") und der "Öffentliche Schlüssel". Der ausführliche Ablauf inklusive der Gegenkonfiguration im externen LMS ist unter [LTI-Zugang zu einem Kurs konfigurieren](../learningresources/LTI_Share_courses.de.md) beschrieben und gilt für Gruppen gleichermassen.

Dieselbe Deployment-ID einer Plattform lässt sich für mehrere Gruppen und Kurse freigeben. In derselben Gruppe gilt sie je Plattform nur einmal, ein zweiter Versuch endet mit der Meldung "Deployment-ID muss eindeutig für eine bestimmte Plattform und eine Gruppe sein." Welche Gruppe OpenOlat beim Aufruf öffnet, erkennt OpenOlat an der Adresse, die die Plattform mitschickt, wie bei Kursen: [Eine Deployment-ID für mehrere Kurse](../learningresources/LTI_Share_courses.de.md#deployment_id_several_courses) [:octicons-tag-16:{ title="ab Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092)

Der Austausch der Mitgliederdaten (Namen und Rollen) erfolgt über den LTI-Standarddienst "Names and Role Provisioning Service" (NRPS). Welche Mitgliederdaten übermittelt werden, bestimmt jeweils das System, das die Verbindung als Plattform bereitstellt. Die grundlegenden LTI-1.3-Einstellungen werden von den Administrator:innen in der System-Administration verwaltet: `Administration > Externe Werkzeuge > LTI`

## Gruppen ohne Kurszugehörigkeit

Eine Gruppe kann unabhängig von einem Kurs per LTI freigegeben werden. Das ist sinnvoll, wenn nicht ein ganzer Kurs geteilt werden soll, sondern nur Daten zu Benutzer:innen und deren Gruppenzugehörigkeit ausgetauscht werden. So lassen sich beispielsweise ausschliesslich die Ergebnisse einer Prüfung übertragen, ohne den zugehörigen Kurs freizugeben.

## Weiterführende Informationen {: #further_information}

[LTI 1.3 Integrationen >](../../manual_admin/administration/LTI_Integrations.de.md)<br>
[LTI-Zugang zu einem Kurs konfigurieren >](../learningresources/LTI_Share_courses.de.md)<br>
[Kursbaustein "LTI-Seite" >](../learningresources/Course_Element_LTI_Page.de.md)<br>
[LTI - Externe Werkzeuge >](../../manual_admin/administration/LTI_External_tools.de.md)<br>
[LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)<br>
[LTI - Deep Linking >](../../manual_admin/administration/LTI_Deeplinking.de.md)<br>
[LTI - Rollen-Mapping >](../../manual_admin/administration/LTI_Role_Mapping.de.md)

[Zum Seitenanfang ^](#LTI_access_to_a_group)
