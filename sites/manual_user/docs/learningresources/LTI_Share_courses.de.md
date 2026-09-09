# Kurseinstellungen - Tab Freigabe:<br> LTI Zugang zu einem Kurs konfigurieren {: #LTI_share_course}

OpenOlat ermöglicht es anderen LMS, via LTI auf einzelne OpenOlat-Kurse zuzugreifen. Ihre OpenOlat-Kurse können so auch von Personen besucht werden, die auf einem anderen LMS arbeiten.

**Beispiel:**<br>
Ein OpenOlat-Kurs wird von Moodle aus via LTI 1.3 gestartet. Dabei werden die Benutzer beim Aufruf in OpenOlat als LTI-Benutzer:innen angelegt und erhalten Zugriff auf den OpenOlat-Kurs (in der Rolle Teilnehmer:in oder Betreuer:in).


## Voraussetzungen

Für die Konfiguration muss ein Administrator-Zugang in beiden Systemen gewährleistet sein. (In OpenOlat kann dies auch die Rolle Systemadministrator:in sein).  Vorzugsweise erfolgt die Konfiguration auf beiden Systemen gleichzeitig, da bestimmte Dialoge in beiden Systemen direkt aufeinanderfolgend zu konfigurieren sind.

## Ablauf der Konfiguration

1. Setup "External Tool" in Moodle
2. Setup "externe Plattform" in OpenOlat
3. LTI-Freigabe des Kurses in OpenOlat
4. Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs
5. Verbindungstest


## 1. Setup "External Tool" in Moodle 

Die Administration der externen Tools in Moodle befinden sich unter folgendem Pfad:<br>
`Site administration > Plugins > External Tool > Manage Tools`

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup1_v1_en.png" alt="Eintrag External tool mit Manage tools, im Menü Plugins der Site administration in Moodle" />
</details>

Für die Konfiguration mit OpenOlat ist die Option "**configure a tool manually**" zu wählen.

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup2_v1_en.png" alt="Der Link 'configure a tool manually' zum manuellen Anlegen eines externen Tools, im Dialog Manage tools in Moodle" />
</details>

Folgende Parameter sind als Mindestanforderung im Dialog zu definieren:

| Feld					| Bemerkung |
| --------------------- | ---------------------------------------------- |
| Tool name				| Frei definierbar |
| Tool URL				| Direkt-Link zu OpenOlat-Kurs. <br> Die URL hat folgendes Format: https:// < OpenOlat-URL > /auth/RepositoryEntry/ < KursID > <br>(Achten Sie darauf, dass kein / am Ende der URL eingefügt wird.) |
| LTI Version			| LTI 1.3 |
| Client ID				| Wird erst nach dem Speichern in dieser Maske ersichtlich |
| Public key type		| RSA key |
| Public key			| Wird in OpenOlat generiert, kann erst nachträglich eingetragen werden |
| Initiate Login URL	| Anmelde-URL (Form: hdps://<OpenOlat- URL/lT/login_iniTaTon) |
| Redirection URL(s)	| Umleitungs-URL (Form: hdps://<OpenOlat-URL/lT/login) |
| Tool Configuration Usage| Show in actvity chooser and as a preconfigured tool |
| Default Launch Container	| New window (OpenOlat unterstützt die Ausführung der Kurse nur in einem neuen Fenster.) |

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup3_v1_en.png" alt="Ausgefülltes Formular External tool configuration mit Tool-URL, LTI-Version und öffentlichem Schlüssel, in Moodle" />
</details>

Nach dem Speichern können Sie weitere Details in der Übersicht über den Detail-Link im LTI-Tool abrufen. Die Details werden beim Setup der externen Plattform in OpenOlat benötigt:

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup4_v1_en.png" alt="Tool configuration details mit Platform-ID, Client-ID und Deployment-ID, in der Tool-Übersicht in Moodle" />
</details>


<br>

## 2. Setup "externe Plattform" in OpenOlat

Die Administration von LTI 1.3 befindet sich in OpenOlat unter folgendem Pfad:<br>
`Administration > Externe Werkzeuge > LTI`

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup5_v2_de.png" alt="Modul 'LTI 1.3' mit Plattform-ID und Organisation, im Tab Konfiguration unter Externe Werkzeuge > LTI der System-Administration" />
</details>

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

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup6_v2_en.png" alt="Ausgefülltes Formular zum Bearbeiten der Plattform mit Plattform-ID, Client-ID und öffentlichem Schlüssel, im Dialog Plattform editieren in OpenOlat" />
</details>

<br>

## 3. LTI-Freigabe des Kurses in OpenOlat

Die Freigabe eines OpenOlat-Kurses (oder einer OpenOlat-Gruppe) erfolgt in den Einstellungen unter folgendem Pfad:<br>
`OpenOlat-Kurs > Einstellungen > Tab "Freigabe" > LTI 1.3 Zugangskonfiguration`

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup7_v2_en.png" alt="Abschnitt LTI 1.3 Zugangskonfiguration mit dem eingerichteten Deployment, im Tab Freigabe der Kurseinstellungen" />
</details>


Ergänzen Sie ein Deployment für den Kurs (oder die Gruppe):

| Feld					| Bemerkung |
| --------------------- | ---------------------------------------------- |
| Plattform				| Auswahl der konfigurierten Moodle-Instanz |
| Deployment-ID 		| Aus Moodle: Deployment ID aus dem Dialog "Tool configuration details" |

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup8_v2_en.png" alt="Ausgefülltes Formular Neues Tool hinzufügen mit Plattform und Deployment-ID, im Dialog für ein neues Deployment in OpenOlat" />
</details>

<br>

## 4. Einbinden des externen Tools (=OpenOlat) im Moodle-Kurs

Im Moodle-Kurs kann nun das externe Tool (OpenOlat) eingefügt werden.

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup9_v1_en.png" alt="Suche nach External tool im Dialog Add an activity or resource, im Moodle-Kurs" />
</details>

Der konfigurierte OpenOlat-Kurs lässt sich hier im externen Tool auf Moodle als "preconfigured tool" auswählen.

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup10_v1_en.png" alt="Auswahl des vorkonfigurierten Tools im Feld Preconfigured tool, beim Hinzufügen des externen Tools im Moodle-Kurs" />
</details>


<br>

## 5. Verbindungstest

Ob die Konfiguration geklappt hat, ist mit einem einfachen Test-Aufruf möglich.

<details>
    <summary>Screen</summary>
	<img src="../assets/LTI_share_coures_moodle-setup11_v1_en.png" alt="Das eingebundene externe Tool im Kursbereich General, im Moodle-Kurs" />
</details>

Der Link in Moodle sollte den gewünschten OpenOlat-Kurs in einem neuen Fenster öffnen. 

!!! warning "Achtung"

	Wenn Sie schon in einem anderen Tab in OpenOlat eingeloggt sind, werden Sie dort ausgeloggt.  


Im OpenOlat-Kurs können Sie den Test-Aufruf in der Mitgliederverwaltung verifizieren: Der LTI-Aufruf hat einen neuen LTI-Benutzer angelegt und einer LTI-Gruppe hinzugefügt:

![Neu angelegter LTI-Benutzer mit der Rolle Gruppenbetreuer:in in der LTI-Gruppe, in der Mitgliederverwaltung des Kurses](assets/LTI_share_coures_moodle-setup12_v1_en.png){ class="shadow lightbox" }


## Externe Kurse im Bewertungswerkzeug

Auch für den Kursbaustein LTI kann das Bewertungsformular ausgefüllt und angepasst werden. Wählen Sie im Kurseditor den Kursbaustein. Unter dem Tab "Seiteninhalt" muss zwingend "Punkte übertragen" ausgewählt sein. Je nachdem muss auch ein Skalierungsfaktor eingetragen und die Punktzahl für das Bestehen definiert werden. Weitere Informationen zur Konfiguration von LTI-Seiten finden Sie [hier](../../manual_user/learningresources/Course_Element_LTI_Page.de.md).

## Weiterführende Informationen {: #further_information}

Benutzerhandbuch: [LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)<br>
Benutzerhandbuch: [Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
Administrationshandbuch: [LTI 1.3 Integrationen im Überblick >](../../manual_admin/administration/LTI_Integrations.de.md)<br>
Administrationshandbuch: [LTI - Externe Werkzeuge >](../../manual_admin/administration/LTI_External_tools.de.md)<br>
Administrationshandbuch: [LTI - Externe Plattformen >](../../manual_admin/administration/LTI_External_platforms.de.md)<br>
Administrationshandbuch: [LTI - Deep Linking](../../manual_admin/administration/LTI_Deeplinking.de.md)<br>
Administrationshandbuch: [LTI - Rollen-Mapping](../../manual_admin/administration/LTI_Role_Mapping.de.md)

[Zum Seitenanfang ^](#LTI_share_course)