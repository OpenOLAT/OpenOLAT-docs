# LTI-Zugang zu einer Gruppe konfigurieren [:octicons-tag-16:{ title="ab Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #LTI_access_to_a_group}

## Was können Sie mit der LTI-Freigabe einer Gruppe tun? {: #lti_share_meaning}

Mit der LTI-Freigabe einer Gruppe holen Sie Personen aus einem anderen Lernmanagementsystem (LMS), zum Beispiel aus Moodle, in eine OpenOlat-Gruppe, ohne einen Kurs freizugeben. Die Personen klicken in ihrem System auf einen Link und landen direkt in der Gruppe, ohne ein OpenOlat-Konto zu beantragen und ohne sich separat anzumelden. Die beiden Systeme verbinden sich dafür über den Standard LTI (Learning Tools Interoperability).

Das ist nützlich, wenn Personen aus einer Partnerorganisation mit Ihnen zusammenarbeiten sollen, ihr eigenes System dafür aber keinen gemeinsamen Ort bietet. In der Gruppe nutzen sie die Werkzeuge, die Sie im Tab "Werkzeuge" eingeschaltet haben, etwa "Forum" oder "Ordner", zum Beispiel um abgegebene Arbeiten zu besprechen. Ist die Gruppe im Tab "Kurse" mit Kursen verbunden, sind die Personen über die Gruppe auch Mitglieder dieser Kurse: [Gruppenadministration](Group_Administration/index.de.md#courses)

Eine Schritt-für-Schritt-Anleitung für Moodle finden Sie im How-to: [Wie binde ich einen OpenOlat-Kurs in Moodle ein?](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md)

**Was die LTI-Freigabe einer Gruppe bewirkt:**

* Die Gruppe bleibt in OpenOlat. Die Personen arbeiten in OpenOlat mit den Werkzeugen der Gruppe.
* Beim ersten Aufruf legt OpenOlat für jede Person ein Konto an. Ist bei der externen Plattform "Benutzer:innen mit E-mail Adresse paaren" eingeschaltet, verbindet OpenOlat die Person stattdessen mit ihrem bestehenden Konto, wenn genau ein Konto diese E-Mail-Adresse trägt.
* Die Person wird direkt Mitglied der freigegebenen Gruppe, als Teilnehmer:in oder als Betreuer:in.
* Ergebnisse meldet OpenOlat aus einer Gruppe nicht an die Plattform zurück. Das tut nur die LTI-Freigabe eines Kurses.
* Die LTI-Freigabe gilt nur für diese eine Gruppe und nur für die Plattform, die Sie auswählen. In der Oberfläche heisst sie "Deployment".
* Löschen Sie die LTI-Freigabe, kann die Plattform nicht mehr auf die Gruppe zugreifen.

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Richtung des Austauschs {: #exchange_direction}

Die Informationen zu Gruppen und Mitgliedern können grundsätzlich in beiden Richtungen ausgetauscht werden:

* von OpenOlat (= Tool) zum anderen LMS (= Plattform)
* vom anderen LMS (= Tool) zu OpenOlat (= Plattform)


![Austauschrichtungen zwischen OpenOlat und einem anderen LMS: OpenOlat als Tool oder als Plattform](assets/LTI_share_groups_platform_tool_v1_de.png){ class="shadow lightbox" title="Rollen Tool und Plattform zwischen zwei Systemen" }

Ist OpenOlat die Plattform, binden Sie das externe Tool in einem Kurs über den Kursbaustein "LTI-Seite" ein. Welche Daten der Personen OpenOlat dabei an das Tool überträgt, etwa Name, E-Mail-Adresse und Rollen, legen Sie im Kursbaustein fest: [Kursbaustein "LTI-Seite"](../learningresources/Course_Element_LTI_Page.de.md). Die folgenden Abschnitte beschreiben OpenOlat als Tool.

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Voraussetzungen {: #conditions}

Die externe Plattform erfassen Systemadministrator:innen in der System-Administration von OpenOlat unter `Administration > Externe Werkzeuge > LTI > Tab "Externe Plattformen"`. Auf der Gegenseite braucht es ebenfalls einen Administrator-Zugang zum anderen LMS. Wer die LTI-Freigabe einer Gruppe hinzufügen darf, legt die System-Administration fest. Je nach Einstellung sind das Administrator:innen, Gruppenverwalter:innen und Gruppenbetreuer:innen mit Autorenrecht: [Wer kann Deployments hinzufügen?](../../manual_admin/administration/LTI_Integrations.de.md#deployments)<br>
Richten Sie am besten beide Systeme gleichzeitig ein, weil bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Ablauf der Konfiguration {: #config_process}

Die Konfiguration verbindet beide Systeme in fünf Schritten. Schritt 3 und den Verbindungstest beschreibt diese Seite, die übrigen Schritte das How-to für Moodle. Sie gelten für eine Gruppe gleich wie für einen Kurs.

1. [Setup "External Tool" in Moodle](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md#setup_step1)
2. [Setup "Externe Plattform" in OpenOlat](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md#setup_step2)
3. [LTI-Freigabe der Gruppe in OpenOlat](#group_share)
4. [Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md#setup_step4)
5. [Verbindungstest](#roles_members_management)

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Gruppe per LTI freigeben {: #group_share}

Mit der LTI-Freigabe erlauben Sie einer externen Plattform, diese eine Gruppe aufzurufen. Sie fügen die LTI-Freigabe mit dem Button "Neues Deployment hinzufügen" hinzu, unter:<br>
`Gruppe > Administration > Tab "Freigabe" > Abschnitt "LTI 1.3 Zugangskonfiguration"`

Den Abschnitt "LTI 1.3 Zugangskonfiguration" sehen nur Personen, die eine LTI-Freigabe hinzufügen dürfen, siehe [Voraussetzungen](#conditions).

Im Dialog wählen Sie die zuvor eingerichtete "Plattform" und tragen die "Deployment-ID" aus der Plattform ein. Die übrigen Angaben gibt OpenOlat vor und zeigt sie nur an: die "Tool URL" der Gruppe im Format `https://<OpenOlat-URL>/auth/BusinessGroup/<Gruppen-ID>`, die "Anmelde-URL", die "Umleitungs-URL" und im Feld "Öffentlicher Schlüssel" den Schlüssel der Plattform. Wohin diese Angaben in Moodle gehören, zeigt Schritt 3 des How-to. Er beschreibt den Kurs und gilt für die Gruppe gleich: [LTI-Freigabe des Kurses in OpenOlat](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md#setup_step3)

Dieselbe Deployment-ID einer Plattform können Sie in der LTI-Freigabe mehrerer Gruppen und Kurse eintragen. In derselben Gruppe gilt sie je Plattform nur einmal, ein zweiter Versuch endet mit der Meldung "Deployment-ID muss eindeutig für eine bestimmte Plattform und eine Gruppe sein." Welche Gruppe OpenOlat beim Aufruf öffnet, erkennt OpenOlat an der Adresse, die die Plattform mitschickt, wie bei Kursen: [Eine Deployment-ID für mehrere Kurse](../learningresources/LTI_Share_courses.de.md#deployment_id_several_courses) [:octicons-tag-16:{ title="ab Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092)

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Welche Angaben werden ausgetauscht? {: #data_exchange}

Wer die Gruppe aus der Plattform aufruft, bringt Angaben zur eigenen Person mit. OpenOlat schickt für eine Gruppe nichts zurück.

Die Plattform schickt bei jedem Aufruf Vorname, Nachname, E-Mail-Adresse, Sprache und die LTI-Rolle der Person mit. Daraus legt OpenOlat beim ersten Aufruf das Konto an und bestimmt die Rolle in der Gruppe. Welche Angaben zur Person die Plattform übermittelt, bestimmt die Plattform. Die vollständige Liste steht bei der LTI-Freigabe eines Kurses, sie gilt für die Gruppe gleich: [Von Moodle zu OpenOlat](../learningresources/LTI_Share_courses.de.md#data_exchange_from_moodle)

Ergebnisse überträgt OpenOlat nur aus einem Kurs mit LTI-Freigabe an die Plattform, nicht aus einer Gruppe. Den LTI-Dienst für Namen und Rollen (Names and Role Provisioning Service, NRPS) fragt OpenOlat nicht ab. Eine Person kommt deshalb erst in die Gruppe, wenn sie die Gruppe selbst aufruft.

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Wo sehen Sie die Personen aus der anderen Plattform? [:octicons-tag-16:{ title="ab Release 15.5 (OO-5207)" }](https://track.frentix.com/issue/OO-5207) {: #roles_members_management}

Ob die Verbindung steht, sehen Sie in der Gruppe: Ruft eine Person die Gruppe zum ersten Mal aus der Plattform auf, erscheint sie in der Mitgliederliste unter:<br>
`Gruppe > Administration > Tab "Mitglieder"`

OpenOlat nimmt die Person direkt in die freigegebene Gruppe auf. Eine eigene Gruppe "LTI: Name der Plattform" wie bei der LTI-Freigabe eines Kurses entsteht nicht. Welche Rolle die Person in der Gruppe erhält, entscheidet die LTI-Rolle, die die Plattform beim Aufruf mitschickt:

| LTI-Rolle in der Plattform |   | Rolle in der Gruppe |
| -------------------------- | ------- | ------------------- |
| Instructor (Kursrolle oder Rolle in der Institution) | wird zu | Betreuer:in |
| Mentor | wird zu | Betreuer:in |
| Learner oder jede andere Rolle | wird zu | Teilnehmer:in |

Für den Verbindungstest aus Schritt 5 rufen Sie die Gruppe in Moodle über den Link des externen Tools auf und prüfen danach, ob das neue Konto in der Mitgliederliste der Gruppe steht.

[Zum Seitenanfang ^](#LTI_access_to_a_group)

---


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Gruppenadministration >](Group_Administration/index.de.md)<br>
[Wie binde ich einen OpenOlat-Kurs in Moodle ein? >](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md)<br>
[Kursbaustein "LTI-Seite" >](../learningresources/Course_Element_LTI_Page.de.md)<br>
[LTI 1.3 Integrationen >](../../manual_admin/administration/LTI_Integrations.de.md)<br>
[LTI-Zugang zu einem Kurs konfigurieren >](../learningresources/LTI_Share_courses.de.md)

**Weiterführend**<br>
[LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)<br>
[LTI - Externe Werkzeuge >](../../manual_admin/administration/LTI_External_tools.de.md)<br>
[LTI - Deep Linking >](../../manual_admin/administration/LTI_Deeplinking.de.md)<br>
[LTI - Rollen-Mapping >](../../manual_admin/administration/LTI_Role_Mapping.de.md)<br>
[Gruppenmitglied werden >](Group_Membership.de.md)

[Zum Seitenanfang ^](#LTI_access_to_a_group)
