# Wie binde ich einen OpenOlat Kurs in Moodle ein? {: #LTI_integrate_course_into_moodle}


??? abstract "Ziel und Inhalt dieser Anleitung"

    Sie haben einen Kurs in OpenOlat erstellt und möchten diesen ausserhalb Ihres OpenOlat auf einer Moodle-Plattform anbieten?<br>
    Die folgende Anleitung zeigt Ihnen das Vorgehen Schritt für Schritt. 

??? abstract "Zielgruppe"

    [x] Autor:innen [ ] Betreuer:innen  [ ] Teilnehmer:innen

    [ ] Anfänger:innen [x] Fortgeschrittene  [x] Experten/Expertinnen

??? abstract "Erwartete Vorkenntnisse"

    * Administrationshandbuch: [LTI 1.3 Integrationen im Überblick >](../../manual_admin/administration/LTI_Integrations.de.md)
	* Administrationshandbuch: [LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)
	* Benutzerhandbuch: [LTI-Zugang zu einem Kurs konfigurieren >](../../manual_user/learningresources/LTI_Share_courses.de.md)
    

---

Zur Anzeige eines OpenOlat-Kurses auf einer anderen Plattform - in der nachstehenden Anleitung ist das Moodle - wird eine Verbindung nach dem LTI 1.3-Standard hergestellt.<br>

Damit die Benutzer:innen der Moodle-Plattform von ihrem System aus auf den OpenOlat-Kurs zugreifen können, müssen die beiden Plattformen miteinander kommunizieren und auf Seite OpenOlat muss der Kurs (und nur dieser Kurs...) für diesen Zugriff von aussen freigegeben werden.


## Voraussetzungen {: #conditions}

Für die Konfiguration muss ein Administrator-Zugang in beiden Systemen gewährleistet sein. (In OpenOlat kann dies auch die Rolle Systemadministrator:in sein).  Vorzugsweise erfolgt die Konfiguration auf beiden Systemen gleichzeitig, da bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)

---


## Ablauf der Konfiguration {: #config_process}

1. [Setup "External Tool" in Moodle](#setup_step1)
2. [Setup "externe Plattform" in OpenOlat](#setup_step2)
3. [LTI-Freigabe des Kurses in OpenOlat](#setup_step3)
4. [Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs](#setup_step4)
5. [Verbindungstest](#setup_step5)


## 1. Setup "External Tool" in Moodle  {: #setup_step1}

Die Administration der externen Tools in Moodle befinden sich unter folgendem Pfad:<br>
`Site administration > Plugins > External Tool > Manage Tools`

![Eintrag External tool mit Manage tools, im Menü Plugins der Site administration in Moodle](assets/LTI_integrate_course_into_moodle-setup1_v1_en.png){ class="shadow lightbox" }

Für die Konfiguration mit OpenOlat ist die Option "**configure a tool manually**" zu wählen.

![Der Link 'configure a tool manually' zum manuellen Anlegen eines externen Tools, im Dialog Manage tools in Moodle](assets/LTI_integrate_course_into_moodle-setup2_v1_en.png){ class="shadow lightbox" }


Folgende Parameter sind als Mindestanforderung im Dialog zu definieren:

| Feld					| Bemerkung |
| --------------------- | ---------------------------------------------- |
| Tool name				| Frei definierbar |
| Tool URL				| Direkt-Link zu OpenOlat-Kurs. <br> Die URL hat folgendes Format: https:// < OpenOlat-URL > /auth/RepositoryEntry/ < KursID > <br>(Achten Sie darauf, dass kein / am Ende der URL eingefügt wird.) |
| LTI Version			| LTI 1.3 |
| Client ID				| Wird erst nach dem Speichern in dieser Maske ersichtlich |
| Public key type		| RSA key |
| Public key			| Wird in OpenOlat generiert, kann erst nachträglich eingetragen werden |
| Initiate Login URL	| Anmelde-URL (Form: hdps://<OpenOlat-URL/lT/login_iniTaTon) |
| Redirection URL(s)	| Umleitungs-URL (Form: hdps://<OpenOlat-URL/lT/login) |
| Tool Configuration Usage| Show in activity chooser and as a preconfigured tool |
| Default Launch Container	| New window (OpenOlat unterstützt die Ausführung der Kurse nur in einem neuen Fenster.) |

![Ausgefülltes Formular External tool configuration mit Tool-URL, LTI-Version und öffentlichem Schlüssel, in Moodle](assets/LTI_integrate_course_into_moodle-setup3_v1_en.png){ class="shadow lightbox" }

Nach dem Speichern können Sie weitere Details in der Übersicht über den Detail-Link im LTI-Tool abrufen. Die Details werden beim Setup der externen Plattform in OpenOlat benötigt:

![Tool configuration details mit Platform-ID, Client-ID und Deployment-ID, in der Tool-Übersicht in Moodle](assets/LTI_integrate_course_into_moodle-setup4_v1_en.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)

---


## 2. Setup "externe Plattform" in OpenOlat {: #setup_step2}

Die Administration von LTI 1.3 befindet sich in OpenOlat unter folgendem Pfad:<br>
`Administration > Externe Werkzeuge > LTI`

![Modul 'LTI 1.3' mit Plattform-ID und Organisation, im Tab Konfiguration unter Externe Werkzeuge > LTI der System-Administration](assets/LTI_integrate_course_into_moodle-setup5_v2_de.png){ class="shadow lightbox" }

Unter “Externe Plattorm” kann die Moodle-Instanz erfasst werden:

| Feld					| Bemerkung |
| --------------------- | ---------------------------------------------- |
| Tool name				| Frei definierbar |
| Plattform-ID / Issuer	| URL zur Moodle-Instanz |
| Client-ID				| Client ID aus dem Dialog "Tool configuration details" in Moodle |
| Öffentlicher Schlüsseltyp | RSA-Schlüssel -> dieser Schlüssel wird anschliessend in der Tool-Konfiguration auf Moodle ergänzt |
| Authorization	 		| Aus Moodle: Authentication request URL |
| URL für Zugriffstoken	| Aus Moodle: Access token URL |
| URL des öffentlichen Schlüsselbundes | Aus Moodle: Public Keyset URL |


Tragen Sie nach Abschluss des Formulars den Öffentlichen Schlüssel auf Moodle in der Tool- Konfiguration ein.

![Ausgefülltes Formular zum Bearbeiten der Plattform mit Plattform-ID, Client-ID und öffentlichem Schlüssel, im Dialog Plattform editieren in OpenOlat](assets/LTI_integrate_course_into_moodle-setup6_v2_en.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)

---


## 3. LTI-Freigabe des Kurses in OpenOlat {: #setup_step3}

Die Freigabe eines OpenOlat-Kurses (oder einer OpenOlat-Gruppe) erfolgt in den Einstellungen unter folgendem Pfad:<br>
`OpenOlat-Kurs > Einstellungen > Tab "Freigabe" > LTI 1.3 Zugangskonfiguration`

![Abschnitt LTI 1.3 Zugangskonfiguration mit dem eingerichteten Deployment, im Tab Freigabe der Kurseinstellungen](assets/LTI_integrate_course_into_moodle-setup7_v2_en.png){ class="shadow lightbox" }

Ergänzen Sie ein Deployment für den Kurs (oder die Gruppe):

| Feld					| Bemerkung |
| --------------------- | ---------------------------------------------- |
| Plattform				| Auswahl der konfigurierten Moodle-Instanz |
| Deployment-ID 		| Aus Moodle: Deployment ID aus dem Dialog "Tool configuration details" |

![Ausgefülltes Formular Neues Tool hinzufügen mit Plattform und Deployment-ID, im Dialog für ein neues Deployment in OpenOlat](assets/LTI_integrate_course_into_moodle-setup8_v2_en.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)

---


## 4. Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs {: #setup_step4}

Im Moodle-Kurs kann nun das externe Tool (OpenOlat) eingefügt werden.

![Suche nach External tool im Dialog Add an activity or resource, im Moodle-Kurs](assets/LTI_integrate_course_into_moodle-setup9_v1_en.png){ class="shadow lightbox" }

Der konfigurierte OpenOlat-Kurs lässt sich hier im externen Tool auf Moodle als "preconfigured tool" auswählen.

![Auswahl des vorkonfigurierten Tools im Feld Preconfigured tool, beim Hinzufügen des externen Tools im Moodle-Kurs](assets/LTI_integrate_course_into_moodle-setup10_v1_en.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)

---


## 5. Verbindungstest {: #setup_step5}

Ob die Konfiguration geklappt hat, ist mit einem einfachen Test-Aufruf möglich.

![Das eingebundene externe Tool im Kursbereich General, im Moodle-Kurs](assets/LTI_integrate_course_into_moodle-setup11_v1_en.png){ class="shadow lightbox" }

Der Link in Moodle sollte den gewünschten OpenOlat-Kurs in einem neuen Fenster öffnen. 

!!! warning "Achtung"

	Wenn Sie schon in einem anderen Tab in OpenOlat eingeloggt sind, werden Sie dort ausgeloggt.  


Im OpenOlat-Kurs können Sie den Test-Aufruf in der Mitgliederverwaltung verifizieren: Der LTI-Aufruf hat einen neuen LTI-Benutzer angelegt und einer LTI-Gruppe hinzugefügt:

![Neu angelegter LTI-Benutzer mit der Rolle Gruppenbetreuer:in in der LTI-Gruppe, in der Mitgliederverwaltung des Kurses](assets/LTI_integrate_course_into_moodle-setup12_v1_en.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)

---

## Weiterführende Informationen {: #further_information}

Benutzerhandbuch: [LTI-Zugang zu einem Kurs konfigurieren >](../../manual_user/learningresources/LTI_Share_courses.de.md)<br>
Benutzerhandbuch: [LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)<br>
Benutzerhandbuch: [Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
Administrationshandbuch: [LTI 1.3 Integrationen im Überblick >](../../manual_admin/administration/LTI_Integrations.de.md)<br>
Administrationshandbuch: [LTI - Externe Werkzeuge >](../../manual_admin/administration/LTI_External_tools.de.md)<br>
Administrationshandbuch: [LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)<br>
Administrationshandbuch: [LTI - Deep Linking](../../manual_admin/administration/LTI_Deeplinking.de.md)<br>
Administrationshandbuch: [LTI - Rollen-Mapping](../../manual_admin/administration/LTI_Role_Mapping.de.md)

[Zum Seitenanfang ^](#LTI_integrate_course_into_moodle)


