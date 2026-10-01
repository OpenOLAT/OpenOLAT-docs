# Kurseinstellungen - Tab Freigabe:<br> LTI Zugang zu einem Kurs konfigurieren {: #LTI_share_course}

OpenOlat ermöglicht es anderen LMS, via LTI auf einzelne OpenOlat-Kurse zuzugreifen. Ihre OpenOlat-Kurse können so auch von Personen besucht werden, die auf einem anderen LMS arbeiten.

**Beispiel:**<br>
Ein OpenOlat-Kurs wird von Moodle aus via LTI 1.3 gestartet. Dabei werden die Benutzer beim Aufruf in OpenOlat als LTI-Benutzer:innen angelegt und erhalten Zugriff auf den OpenOlat-Kurs (in der Rolle Teilnehmer:in oder Betreuer:in).<br>
Eine ausführliche Anleitung finden Sie [hier](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md).


## Voraussetzungen {: #conditions}

### Voraussetzungen in der Systemadministration {: #conditions_admin}

Für die Konfiguration muss ein Administrator-Zugang in beiden Systemen gewährleistet sein. (In OpenOlat kann dies auch die Rolle Systemadministrator:in sein).  Vorzugsweise erfolgt die Konfiguration auf beiden Systemen gleichzeitig, da bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

### Voraussetzungen in der LTI-Freigabe eines Kurses [:octicons-tag-16:{ title="ab Release 15.5 (OO-5206)" }](https://track.frentix.com/issue/OO-5206) {: #conditions_share}

Die LTI-Freigabe erlaubt einer bestimmten externen Plattform, zum Beispiel Moodle, diesen einen Kurs per LTI 1.3 zu starten. Ohne Freigabe weist OpenOlat jeden LTI-Aufruf für den Kurs ab, auch wenn die Plattform in der Administration eingerichtet ist.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Welche Angaben werden zwischen den beiden Systemen ausgetauscht? {: #data_exchange}

Moodle schickt bei jedem Aufruf Angaben zur Person und zum Kurskontext an OpenOlat. OpenOlat schickt nur eine Sache zurück: das Kursergebnis der Person.


### Von Moodle zu OpenOlat {: #data_exchange_from_moodle}

Moodle schickt ein signiertes Token (LTI 1.3 Launch). OpenOlat liest daraus diese Angaben:

| Angabe |  Wofür OpenOlat sie braucht | 
| -------| --------------------------- | 
| Aussteller und Benutzerkennung | Damit erkennt OpenOlat die Person wieder. Die Kombination wird als LTI-Authentifizierung gespeichert. | 
| Vorname, Nachname, E-Mail-Adresse | Daraus wird das Benutzerkonto angelegt. Bei reinen LTI-Konten werden die Werte bei jedem Aufruf aktualisiert. | 
| Sprache | Wird nur beim Anlegen als Spracheinstellung des Kontos übernommen. | 
| LTI-Rollen | Bestimmen, ob die Person Betreuer:in oder Teilnehmer:in wird. |
| Deployment ID und Ziel-URL | Zeigen, welcher freigegebene Kurs oder welche Gruppe gemeint ist. OpenOlat prüft die Ziel-URL gegen die Freigabe. | 
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


### Was nicht ausgetauscht wird {: #data_exchange_non}

* **Mitgliederlisten:** OpenOlat speichert die Adresse des Dienstes für Namen und Rollen, fragt ihn aber nie ab. Mitglieder kommen also nur dazu, wenn sie den Kurs selbst aufrufen.
* **Liste der Bewertungsspalten:** Diese Adresse wird ebenfalls nur gespeichert.
* **Kursinhalte:** Sie bleiben in OpenOlat und werden dort angezeigt.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Welche Rolle erhalten Personen, die einen OpenOlat Kurs von Moodle aus aufrufen? [:octicons-tag-16:{ title="ab Release 15.5 (OO-5207)" }](https://track.frentix.com/issue/OO-5207) {: #roles_for_externals}

Mit jeder LTI-Kursfreigabe wird von OpenOlat eine LTI-Gruppe anlegt. Alle via LTI von extern Zugreifenden werden dieser Gruppe hinzugefügt.

Über die Gruppe sind die Personen dann (Gruppen-)Betreuer:in oder (Gruppen-)Teilnehmer:in im Kurs. 
Welche der beiden Rollen sie bekommen, entscheidet die LTI-Rolle, die Moodle beim Aufruf mitschickt.

| LTI-Rolle in Moodle |   | Kursrolle in OpenOlat                               |
| ----------------- | ----- |------------------------------------------- |
| Instructor (Kursrolle oder Rolle in der Institution) | wird zu | Gruppenbetreuer:in in der LTI-Gruppe |
| Mentor            | wird zu | Gruppenbetreuer:in der LTI-Gruppe |
| Learner oder jede andere Rolle | wird zu | Gruppenteilnehmer:in |

Kursbesitzer:in wird über LTI niemand.

[Zum Seitenanfang ^](#LTI_share_course)

---


## Ablauf der Konfiguration {: #config_process}

1. Setup "External Tool" in Moodle
2. Setup "externe Plattform" in OpenOlat
3. LTI-Freigabe des Kurses in OpenOlat
4. Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs
5. Verbindungstest

Eine ausführliche Anleitung mit diesen 5 Schritten finden Sie [hier](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md).

[Zum Seitenanfang ^](#LTI_share_course)

---


## Wie und wo werden das Ergebnisse angezeigt? {: #results}

### Externe Kurse im Bewertungswerkzeug {: #results_assessment_tool}

Auch für den Kursbaustein LTI kann das Bewertungsformular ausgefüllt und angepasst werden. Wählen Sie im Kurseditor den Kursbaustein. Unter dem Tab "Seiteninhalt" muss zwingend "Punkte übertragen" ausgewählt sein. Je nachdem muss auch ein Skalierungsfaktor eingetragen und die Punktzahl für das Bestehen definiert werden. Weitere Informationen zur Konfiguration von LTI-Seiten finden Sie [hier](../../manual_user/learningresources/Course_Element_LTI_Page.de.md).

[Zum Seitenanfang ^](#LTI_share_course)

---

## Weiterführende Informationen {: #further_information}

How-to: [Wie binde ich einen OpenOlat-Kurs in Moodle ein? >](../../manual_how-to/LTI_integrate_course_into_moodle/LTI_integrate_course_into_moodle.de.md)<br>
Benutzerhandbuch: [LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)<br>
Benutzerhandbuch: [Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
Administrationshandbuch: [LTI 1.3 Integrationen im Überblick >](../../manual_admin/administration/LTI_Integrations.de.md)<br>
Administrationshandbuch: [LTI - Externe Werkzeuge >](../../manual_admin/administration/LTI_External_tools.de.md)<br>
Administrationshandbuch: [LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)<br>
Administrationshandbuch: [LTI - Deep Linking](../../manual_admin/administration/LTI_Deeplinking.de.md)<br>
Administrationshandbuch: [LTI - Rollen-Mapping](../../manual_admin/administration/LTI_Role_Mapping.de.md)

Benutzerhandbuch: [Mitgliederverwaltung >](../../manual_user/learningresources/Members_management.de.md)<br>
Benutzerhandbuch: [Bewertungswerkzeug - Übersicht >](../../manual_user/learningresources/Assessment_tool_overview.de.md)<br>
Benutzerhandbuch: [Zugangskonfiguration / Freigabe >](../../manual_user/learningresources/Access_configuration.de.md)<br>

[Zum Seitenanfang ^](#LTI_share_course)
