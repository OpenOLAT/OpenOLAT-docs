# LTI-Zugang zu einer Gruppe konfigurieren [:octicons-tag-16:{ title="ab Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #LTI_access_to_a_group}

Mit LTI lassen sich nicht nur Inhalte (Kurse) auf einem anderen LMS nutzen. Via LTI können auch Daten über die Kursteilnehmer:innen und Betreuer:innen ausgetauscht werden (LTI-Services für das Provisioning von Namen und Rollen, sowie LTI-Services "Assignments and Grades"). 

So lassen sich z.B. Noten sicher mit dem Prüfungsamt via API austauschen. Es können auch Stärken und Schwächen der abgelieferten Arbeit mit den Studierenden diskutiert werden, wenn der besuchte Kurs von einem anderen LMS stammt und die Kommunikationsinfrastruktur des eigenen LMS dort nicht zur Verfügung steht.

## Richtung des Austauschs

Die Informationen zu Gruppen und Mitgliedern können grundsätzlich in beiden Richtungen ausgetauscht werden:

* von OpenOlat (= Tool) zum anderen LMS (= Platform)
* vom anderen LMS (= Tool) zu OpenOlat (= Platform)


![Austauschrichtungen zwischen OpenOlat und einem anderen LMS: OpenOlat als Tool oder als Platform](assets/LTI_share_groups_platform_tool_v1_de.png){ class="shadow lightbox" title="Rollen Tool und Platform zwischen zwei Systemen" }

Ist OpenOlat die Platform, binden Sie das externe Tool in einem Kurs über den Kursbaustein "LTI-Seite" ein. Welche Daten der Personen OpenOlat dabei an das Tool überträgt, etwa Name, E-Mail-Adresse und Rollen, legen Sie im Kursbaustein fest: [Kursbaustein "LTI-Seite"](../learningresources/Course_Element_LTI_Page.de.md). Die folgenden Abschnitte beschreiben OpenOlat als Tool.


## Voraussetzungen

Die externe Plattform wird in der System-Administration von OpenOlat erfasst, dafür braucht es in OpenOlat die Rolle Systemadministrator:in. Auf der Gegenseite braucht es ebenfalls einen Administrator-Zugang zum anderen LMS. Wer die LTI-Freigabe einer Gruppe vornehmen darf, legt die System-Administration fest: [Wer kann Deployments hinzufügen?](../../manual_admin/administration/LTI_Integrations.de.md#deployments)<br>
Vorzugsweise erfolgt die Konfiguration auf beiden Systemen gleichzeitig, da bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

## Ablauf der Konfiguration

1. Setup "External Tool" in Moodle
2. Setup "externe Plattform" in OpenOlat
3. LTI-Freigabe der Gruppe in OpenOlat
4. Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs
5. Verbindungstest

Der ausführliche Ablauf einer Konfiguration ist beschrieben unter [LTI-Zugang zu einem Kurs konfigurieren](../learningresources/LTI_Share_courses.de.md).


## Daten zur Gruppe per LTI übertragen

Eine OpenOlat-Gruppe wird für den LTI-Zugang genauso freigegeben wie ein Kurs. Die Freigabe erfolgt mit dem Button "Neues Deployment hinzufügen" unter:<br>
`Gruppe > Administration > Tab "Freigabe" > Abschnitt "LTI 1.3 Zugangskonfiguration"`

Im Deployment-Dialog wählen Sie wie bei der Kursfreigabe die zuvor konfigurierte "Plattform" und tragen die "Deployment-ID" ein. Die übrigen Angaben gibt OpenOlat vor und zeigt sie nur an: die "Tool URL" der Gruppe im Format `https://<OpenOlat-URL>/auth/BusinessGroup/<Gruppen-ID>`, die "Anmelde-URL", die "Umleitungs-URL" und im Feld "Öffentlicher Schlüssel" den Schlüssel der Plattform. Der ausführliche Ablauf inklusive der Gegenkonfiguration im externen LMS ist unter [LTI-Zugang zu einem Kurs konfigurieren](../learningresources/LTI_Share_courses.de.md) beschrieben und gilt für Gruppen gleichermassen.

Dieselbe Deployment-ID einer Plattform lässt sich für mehrere Gruppen und Kurse freigeben. In derselben Gruppe gilt sie je Plattform nur einmal, ein zweiter Versuch endet mit der Meldung "Deployment-ID muss eindeutig für eine bestimmte Plattform und eine Gruppe sein." Welche Gruppe OpenOlat beim Aufruf öffnet, erkennt OpenOlat an der Adresse, die die Plattform mitschickt, wie bei Kursen: [Eine Deployment-ID für mehrere Kurse](../learningresources/LTI_Share_courses.de.md#deployment_id_several_courses) [:octicons-tag-16:{ title="ab Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092)

Der Austausch der Mitgliederdaten (Namen und Rollen) erfolgt über den LTI-Standarddienst "Names and Role Provisioning Service" (NRPS). Welche Mitgliederdaten übermittelt werden, bestimmt jeweils das System, das die Verbindung als Plattform bereitstellt. Die grundlegenden LTI-1.3-Einstellungen verwalten Systemadministrator:innen in der System-Administration: `Administration > Externe Werkzeuge > LTI`

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
