# LTI 1.3 Integrationen [:octicons-tag-16:{ title="ab Release 15.5 (OO-5205)" }](https://track.frentix.com/issue/OO-5205) {: #LTI_integrations}

## Grundlagen {: #basics}

Wichtige Begriffe in der LTI-Terminologie:

* **Platform** (entspricht Client): das LMS, in das der externe Inhalt eingebunden wird.
* **Tool** (entspricht Host): das LMS oder die Applikation, die einen Inhalt anderen zur Verfügung stellt.

OpenOlat kann beide Rollen einnehmen: Als Tool stellt OpenOlat einen Kurs oder eine Gruppe für ein anderes LMS bereit. Als Platform zeigt OpenOlat den Inhalt eines externen Tools im Kurs an, über den Kursbaustein "LTI-Seite".

![OpenOlat als Tool stellt einen Kurs für die Platform eines anderen LMS bereit, OpenOlat als Platform zeigt den Inhalt eines Tools aus einem anderen LMS](assets/LTI_platform_tool_v1_de.png){ class="lightbox" }

## LTI aktivieren {: #activate_lti}

Administrator:innen aktivieren LTI in der System-Administration unter `Administration > Externe Werkzeuge > LTI`, Tab "Konfiguration". Die Checkbox "Eingeschaltet" beim Feld Modul "LTI 1.3" steht an oberster Stelle. Erst danach lassen sich LTI-Verbindungen einrichten.

![Checkbox Eingeschaltet für das Modul LTI 1.3 an oberster Stelle im Tab Konfiguration der Seite LTI in der System-Administration](assets/LTI_admin_config_v2_de.png){ class="shadow lightbox" }

Nach dem Einschalten zeigt der Tab zwei weitere Felder:

| Feld | Bemerkung |
|---|---|
| Plattform-ID | Die URL, mit der sich OpenOlat gegenüber externen Systemen identifiziert. Von OpenOlat vorgegeben, nur lesbar. Standard ist die Domain der Instanz. |
| Organisation | Die Organisation, der OpenOlat die Benutzerkonten zuordnet, die beim Zugriff aus einer externen Plattform neu angelegt werden. Ohne Auswahl gilt die Standard-Organisation. |

Die Seite LTI hat vier Tabs: "Konfiguration" für die Grundeinstellungen auf dieser Seite, "Externe Plattformen" für OpenOlat als Tool, "Externe Tools" für OpenOlat als Platform und "Rollen-Mapping" für die Zuordnung der OpenOlat-Rollen zu den LTI-Rollen. Die Detailseiten dazu sind unten verlinkt.

## Deployments {: #deployments}

**Was ist ein Deployment?**

Das Deployment eines Tools bestimmt, in welchem Umfang das Tool zur Verfügung gestellt wird:

* Einsatz in einem einzelnen Kurs
* Einsatz im gesamten System
* Einsatz nur für den aktuellen Kontext
* Einsatz generell ermöglicht (auch für zukünftige Kontexte)

**Wer kann Deployments hinzufügen?**

Administrator:innen bestimmen im Tab "Konfiguration" unter `Administration > Externe Werkzeuge > LTI`, wer Deployments hinzufügen darf. Die Einstellung gibt es getrennt für Kurse und für Gruppen.

**Kurs**

* "Rolle kann Deployment hinzufügen": Administrator:innen dürfen es immer. Zusätzlich lassen sich Lernressourcenverwalter:innen freischalten.
* "Besitzer:in mit Autorenrecht kann Deployment hinzufügen": "Für alle Kurse aktivieren" oder "Muss pro Kurs aktiviert werden".

**Gruppe**

* "Rolle kann Deployment hinzufügen": Administrator:innen dürfen es immer. Zusätzlich lassen sich Gruppenverwalter:innen freischalten.
* "Gruppenbetreuer:in mit Autorenrecht kann Deployment hinzufügen": "Für alle Gruppen aktivieren" oder "Muss pro Gruppe aktiviert werden".

![Rollen und Freigaben für das Hinzufügen von Deployments, getrennt nach Kurs und Gruppe, im Tab Konfiguration der Seite LTI](assets/LTI_admin_deploy_v2_de.png){ class="shadow lightbox" }

## Weiterführende Informationen {: #further_information}

**Weiterführend**<br>
[Learning Tools Interoperability Core Specification (IMS Global Learning Consortium) >](http://www.imsglobal.org/spec/lti/v1p3/)<br>
[LTI - Externe Werkzeuge >](../administration/LTI_External_tools.de.md)<br>
[LTI - Externe Plattformen >](../administration/LTI_External_platforms.de.md)<br>
[LTI - Deep Linking >](../administration/LTI_Deeplinking.de.md)<br>
[LTI - Rollen-Mapping >](../administration/LTI_Role_Mapping.de.md)<br>
[LTI-Zugang zu einem Kurs konfigurieren >](../../manual_user/learningresources/LTI_Share_courses.de.md)<br>
[Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
[LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)

[Zum Seitenanfang ^](#LTI_integrations)
