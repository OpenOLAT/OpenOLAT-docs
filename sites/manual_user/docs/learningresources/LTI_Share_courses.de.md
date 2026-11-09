# Kurseinstellungen - Tab Freigabe:<br> LTI Zugang zu einem Kurs konfigurieren {: #LTI_share_course}

## Was können Sie mit der LTI-Freigabe tun? {: #lti_share_meaning}

Mit der LTI-Freigabe bieten Sie einen OpenOlat-Kurs in einem anderen Lernmanagementsystem an, zum Beispiel in Moodle. Die Personen dort bleiben in ihrem gewohnten System. Sie klicken auf einen Link und landen direkt in Ihrem OpenOlat-Kurs, ohne ein OpenOlat-Konto zu beantragen und ohne sich separat anzumelden.

Das ist nützlich, wenn eine Partnerorganisation mit einem anderen System arbeitet und Ihren Kurs nutzen soll. Sie pflegen den Kurs einmal in OpenOlat und geben ihn für eine oder mehrere Plattformen frei.

Wie Sie einen Kurs Schritt für Schritt in Moodle einbinden, zeigt die Anleitung [Wie binde ich einen OpenOlat-Kurs in Moodle ein?](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md).

**Was die LTI-Freigabe bewirkt:**

* Der Kurs bleibt in OpenOlat. Die Personen bearbeiten Inhalte und Tests in OpenOlat, das sich dafür in einem neuen Fenster öffnet.
* Beim ersten Aufruf legt OpenOlat für jede Person ein LTI-Konto an. Die Person wird Mitglied der LTI-Gruppe des Kurses, als Teilnehmer:in oder als Betreuer:in.
* OpenOlat meldet das Kursergebnis an das andere System zurück, wenn dort eine Bewertungsspalte dafür vorgesehen ist.
* Die LTI-Freigabe gilt nur für diesen einen Kurs und nur für die Plattform, die Sie auswählen. In der Oberfläche heisst sie "Deployment". Alle anderen Kurse bleiben für die Plattform gesperrt.
* Löschen Sie die LTI-Freigabe, kann die Plattform nicht mehr auf den Kurs zugreifen.

Die Plattform muss vorher in der System-Administration als externe Plattform eingerichtet sein, unter `Administration > Externe Werkzeuge > LTI > Tab "Externe Plattformen"`. Ob Sie die LTI-Freigabe selbst hinzufügen oder über den Button "Neues Deployment anfragen" beim Support beantragen, hängt von Ihrer Rolle ab. Mehr dazu unter [Voraussetzungen](#conditions).

[Zum Seitenanfang ^](#LTI_share_course)

---


## Voraussetzungen {: #conditions}

### Voraussetzungen in der System-Administration {: #conditions_admin}

Die externe Plattform erfassen Systemadministrator:innen in der System-Administration von OpenOlat unter `Administration > Externe Werkzeuge > LTI > Tab "Externe Plattformen"`. Auf der Gegenseite braucht es ebenfalls einen Administrator-Zugang zum anderen LMS. Wer die LTI-Freigabe eines Kurses vornehmen darf, legt die System-Administration fest: [Wer kann Deployments hinzufügen?](../../manual_admin/administration/LTI_Integrations.de.md#deployments)<br>
Richten Sie am besten beide Systeme gleichzeitig ein, weil bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

### Voraussetzungen in der LTI-Freigabe eines Kurses [:octicons-tag-16:{ title="ab Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #conditions_share}

Die LTI-Freigabe erlaubt einer bestimmten externen Plattform, zum Beispiel Moodle, diesen einen Kurs per LTI 1.3 zu starten. Ohne Freigabe weist OpenOlat jeden LTI-Aufruf für den Kurs ab, auch wenn die Plattform in der Administration eingerichtet ist.

### Eine Deployment-ID für mehrere Kurse [:octicons-tag-16:{ title="ab Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092) {: #deployment_id_several_courses}

Wer mehrere OpenOlat-Kurse in derselben Plattform anbietet, erhält von der Plattform oft für alle Kurse dieselbe Deployment-ID. Das geschieht, wenn die Plattform das Tool als gemeinsames Deployment führt. Eine Plattform mit OpenOlat tut das automatisch, sobald dort ein Kursbaustein "LTI-Seite" oder sein Kurs kopiert wird. Jeder OpenOlat-Kurs lässt sich trotzdem mit dieser Deployment-ID freigeben, ein zweites Tool auf der Plattform braucht es dafür nicht.

Tragen Sie die Deployment-ID in der LTI-Freigabe jedes Kurses ein, den die Plattform erreichen soll. Im selben Kurs gilt eine Deployment-ID je Plattform nur einmal. Ein zweiter Versuch endet mit der Meldung "Deployment-ID muss eindeutig für eine bestimmte Plattform und einen Kurs sein."

Welchen Kurs OpenOlat beim Aufruf öffnet, erkennt OpenOlat an der Adresse, die die Plattform mitschickt. In Moodle ist das die "Tool URL" des externen Tools. Diese Adresse muss mit der "Tool URL" beginnen, die OpenOlat im Dialog nach dem Klick auf "Neues Deployment hinzufügen" anzeigt. Passt die Adresse zu keinem freigegebenen Kurs, bricht OpenOlat den Aufruf ab, statt einen anderen Kurs zu öffnen.

Ein kopierter OpenOlat-Kurs übernimmt die LTI-Freigabe des Originals nicht. Er braucht eine eigene LTI-Freigabe, auch wenn die Plattform dieselbe Deployment-ID verwendet.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Welche Angaben werden zwischen den beiden Systemen ausgetauscht? {: #data_exchange}

Moodle schickt bei jedem Aufruf Angaben zur Person und zum Kurskontext an OpenOlat. OpenOlat schickt nur eine Sache zurück: das Kursergebnis der Person.

Welche LTI-Dienste OpenOlat als Tool und als Plattform unterstützt, zeigt die Übersicht [Unterstützte LTI-Dienste](../../manual_admin/administration/LTI_Integrations.de.md#supported_services).


### Von Moodle zu OpenOlat {: #data_exchange_from_moodle}

Moodle schickt ein signiertes Token (LTI 1.3 Launch). OpenOlat liest daraus diese Angaben:

| Angabe |  Wofür OpenOlat sie braucht | 
| -------| --------------------------- | 
| Aussteller und Benutzerkennung | Damit erkennt OpenOlat die Person wieder. Die Kombination wird als LTI-Authentifizierung gespeichert. | 
| Vorname, Nachname, E-Mail-Adresse | Daraus wird das Benutzerkonto angelegt. Bei reinen LTI-Konten werden die Werte bei jedem Aufruf aktualisiert. | 
| Sprache | Wird nur beim Anlegen als Spracheinstellung des Kontos übernommen. | 
| LTI-Rollen | Bestimmen, ob die Person Betreuer:in oder Teilnehmer:in wird. |
| Deployment-ID und Tool URL | Zeigen, welcher freigegebene Kurs oder welche Gruppe gemeint ist. Gilt dieselbe Deployment-ID für mehrere Kurse, entscheidet die Tool URL. | 
| Kontext-ID und Resource-Link-ID | Kennung des Moodle-Kurses und der Aktivität darin. | 
| Adressen der Moodle-Dienste für Bewertungen und Mitgliederlisten | OpenOlat speichert sie pro Moodle-Kurs. | 


### Von OpenOlat zu Moodle {: #data_exchange_from_openolat}

Ändert sich die Bewertung einer Person im Kurs, schickt OpenOlat das Ergebnis des Kurses als Ganzes an den Bewertungsdienst von Moodle (Assignment and Grade Services). Einzelne Kursbausteine werden nicht übertragen. Übertragen werden:

* die Benutzerkennung aus Moodle
* die erreichte Punktzahl
* die maximale Punktzahl (100, wenn keine festgelegt ist)
* der Bearbeitungsstand und der Bewertungsstand
* der Kommentar zur Bewertung
* der Zeitpunkt

Das Ergebnis wird nur gesendet, wenn Moodle beim Aufruf die Adresse einer einzelnen Bewertungsspalte mitgeschickt hat. Es geht an die Moodle-Plattform, über die die Person angemeldet ist.

OpenOlat sendet das Ergebnis bei jeder Änderung der Punkte, nicht erst am Ende des Kurses. Ergebnisse sendet OpenOlat nur für Teilnehmer:innen des Kurses. Wer aus Moodle als Instructor oder Mentor kommt, wird Betreuer:in der LTI-Gruppe und erhält kein Ergebnis: [Welche Rolle erhalten Personen, die einen OpenOlat Kurs von Moodle aus aufrufen?](#roles_for_externals)


### Was nicht ausgetauscht wird {: #data_exchange_non}

* **Mitgliederlisten:** OpenOlat speichert die Adresse des Dienstes für Namen und Rollen, fragt ihn aber nie ab. Mitglieder kommen also nur dazu, wenn sie den Kurs selbst aufrufen.
* **Liste der Bewertungsspalten:** Diese Adresse wird ebenfalls nur gespeichert.
* **Kursinhalte:** Sie bleiben in OpenOlat und werden dort angezeigt.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Welche Rolle erhalten Personen, die einen OpenOlat Kurs von Moodle aus aufrufen? [:octicons-tag-16:{ title="ab Release 15.5 (OO-5207)" }](https://track.frentix.com/issue/OO-5207) {: #roles_for_externals}

Mit jeder LTI-Freigabe eines Kurses legt OpenOlat eine LTI-Gruppe an. Alle via LTI von extern Zugreifenden werden dieser Gruppe hinzugefügt.

Über die Gruppe sind die Personen dann (Gruppen-)Betreuer:in oder (Gruppen-)Teilnehmer:in im Kurs. 
Welche der beiden Rollen sie bekommen, entscheidet die LTI-Rolle, die Moodle beim Aufruf mitschickt.

| LTI-Rolle in Moodle |   | Kursrolle in OpenOlat                               |
| ----------------- | ----- |------------------------------------------- |
| Instructor (Kursrolle oder Rolle in der Institution) | wird zu | Gruppenbetreuer:in in der LTI-Gruppe |
| Mentor            | wird zu | Gruppenbetreuer:in der LTI-Gruppe |
| Learner oder jede andere Rolle | wird zu | Gruppenteilnehmer:in |

Kursbesitzer:in wird über LTI niemand.


### Wo sehen Sie die Personen aus der anderen Plattform? {: #roles_members_management}

Sobald Sie die LTI-Freigabe hinzugefügt haben, legt OpenOlat im Kurs die Gruppe "LTI: Name der Plattform" an. Sie finden sie in der Mitgliederverwaltung unter den Gruppen. Die Gruppe ist zunächst leer. Eine Person erscheint darin erst, wenn sie den Kurs zum ersten Mal aus der anderen Plattform startet. In der Mitgliederliste steht sie dann als Gruppenbetreuer:in oder Gruppenteilnehmer:in.

Kopieren Sie den Kurs, wird die LTI-Gruppe nicht mitkopiert. Für die Kopie richten Sie eine eigene LTI-Freigabe ein.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Ablauf der Konfiguration {: #config_process}

Die Konfiguration verlangt Schritte in Moodle und in OpenOlat. Die Anleitung [Wie binde ich einen OpenOlat-Kurs in Moodle ein?](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md) führt Sie durch den ganzen Ablauf, vom externen Tool in Moodle bis zum Verbindungstest.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Wie und wo werden die Ergebnisse angezeigt? {: #results}

### Externe Kurse im Bewertungswerkzeug {: #results_assessment_tool}

Auch für den Kursbaustein "LTI-Seite" kann das Bewertungsformular ausgefüllt und angepasst werden. Wählen Sie im Kurseditor den Kursbaustein. Im Tab "Seiteninhalt" muss "Punkte übertragen" eingeschaltet sein. Je nachdem muss auch ein Skalierungsfaktor eingetragen und die Punktzahl für das Bestehen definiert werden: [Kursbaustein "LTI-Seite"](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)

[Zum Seitenanfang ^](#LTI_share_course)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Wie binde ich einen OpenOlat-Kurs in Moodle ein? >](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md)<br>
[LTI 1.3 Integrationen >](../../manual_admin/administration/LTI_Integrations.de.md)<br>
[Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)

**Weiterführend**<br>
[LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)<br>
[LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)<br>
[LTI - Externe Werkzeuge >](../../manual_admin/administration/LTI_External_tools.de.md)<br>
[LTI - Deep Linking >](../../manual_admin/administration/LTI_Deeplinking.de.md)<br>
[LTI - Rollen-Mapping >](../../manual_admin/administration/LTI_Role_Mapping.de.md)<br>
[Kurseinstellungen - Tab Freigabe >](Course_Settings_Share/index.de.md)<br>
[Mitgliederverwaltung >](../../manual_user/learningresources/Members_management.de.md)<br>
[Bewertungswerkzeug - Übersicht >](Assessment_tool_overview/index.de.md)<br>
[Zugangskonfiguration / Freigabe >](../../manual_user/learningresources/Access_configuration.de.md)

[Zum Seitenanfang ^](#LTI_share_course)
