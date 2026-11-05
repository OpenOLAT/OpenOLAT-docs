# LTI 1.3 Integrationen [:octicons-tag-16:{ title="ab Release 15.5 (OO-5205)" }](https://track.frentix.com/issue/OO-5205) {: #LTI_integrations}

## Grundlagen {: #basics}

Wichtige Begriffe in der LTI-Terminologie:

* **Plattform** (entspricht Client): das LMS, in das der externe Inhalt eingebunden wird.
* **Tool** (entspricht Host): das LMS oder die Applikation, die einen Inhalt anderen zur Verfügung stellt.

OpenOlat kann beide Rollen einnehmen: Als Tool stellt OpenOlat einen Kurs oder eine Gruppe für ein anderes LMS bereit. Als Plattform zeigt OpenOlat den Inhalt eines externen Tools im Kurs an, über den Kursbaustein "LTI-Seite".

![OpenOlat als Tool stellt einen Kurs für die Plattform eines anderen LMS bereit, OpenOlat als Plattform nutzt den Inhalt eines Tools aus einem anderen LMS](assets/lti_platform_tool_v1_de.svg){ class="shadow lightbox" title="Rollen Tool und Plattform zwischen zwei Systemen · 2026.11.04" }

## Unterstützte LTI-Dienste {: #supported_services}

Wer ein externes Tool oder eine andere Plattform an OpenOlat anbinden will, sieht hier auf einen Blick, ob OpenOlat den benötigten LTI-Dienst unterstützt und in welcher Richtung. Welche Dienste OpenOlat unterstützt, hängt davon ab, ob OpenOlat ein externes Tool einbindet (Plattform) oder einen Kurs oder eine Gruppe für eine andere Plattform bereitstellt (Tool). Die Dienste für Punkte, Mitgliederliste und Inhaltsauswahl fasst der Standard unter dem Namen LTI Advantage zusammen.

![Start und Punkte in beiden Richtungen, Mitgliederliste und Inhaltsauswahl nur mit OpenOlat als Plattform](assets/lti_supported_services_v1_de.svg){ class="shadow lightbox" title="LTI-Dienste in beiden Richtungen · 2026.11.04" }

| Dienst | OpenOlat als Plattform (Kursbaustein "LTI-Seite") | OpenOlat als Tool (LTI-Freigabe eines Kurses oder einer Gruppe) |
|---|---|---|
| Start des Tools (LTI 1.3, Resource Link Launch) | ja, über den [Kursbaustein "LTI-Seite"](../../manual_user/learningresources/Course_Element_LTI_Page.de.md) | ja, für [Kurse](../../manual_user/learningresources/LTI_Share_courses.de.md) und [Gruppen](../../manual_user/groups/LTI_Share_groups.de.md). OpenOlat legt beim ersten Aufruf ein Konto an. |
| Bewertungsdienst (Assignment and Grade Services, AGS) | ja, wenn im Kursbaustein "Punkte übertragen" eingeschaltet ist. Das Tool liest die Bewertungsspalte des Kursbausteins und die Resultate und sendet Punkte an OpenOlat. | ja, aus Kursen. OpenOlat sendet das Ergebnis des ganzen Kurses an die Plattform, bei jeder Änderung der Punkte und nur für Teilnehmer:innen. Aus Gruppen sendet OpenOlat keine Ergebnisse. |
| LTI-Dienst für Namen und Rollen (Names and Role Provisioning Service, NRPS 2.0) | ja. OpenOlat stellt dem Tool die Liste der Teilnehmer:innen des Kurses bereit, mit Vorname, Nachname und der LTI-Rolle "Learner". Dafür braucht es keine Einstellung. | nein. OpenOlat speichert die Adresse dieses Dienstes der Plattform, fragt die Mitgliederliste aber nicht ab. |
| Deep Linking 2.0 (Inhaltsauswahl) | ja, mit dem Button "Inhalt auswählen" im Kursbaustein. Er erscheint bei "LTI 1.3" und bei einem vorkonfigurierten Tool, bei dem "Deep-Linking aktivieren" eingeschaltet ist: [LTI - Deep Linking](LTI_Deeplinking.de.md) [:octicons-tag-16:{ title="ab Release 18.1 (OO-7173)" }](https://track.frentix.com/issue/OO-7173) | nein. OpenOlat bietet der Plattform keine Inhaltsauswahl an. |
| LTI 1.0 / 1.1 (Start mit "Schlüssel" und "Passwort", Punkte über Basic Outcomes) | ja. Das Tool sendet Punkte als Wert von 0 bis 1. | nein |

## LTI aktivieren {: #activate_lti}

Systemadministrator:innen aktivieren LTI in der System-Administration unter `Administration > Externe Werkzeuge > LTI`, Tab "Konfiguration". Die Checkbox "Eingeschaltet" beim Feld Modul "LTI 1.3" steht an oberster Stelle. Erst danach lassen sich LTI-Verbindungen einrichten.

![Markierter Menüeintrag LTI unter Externe Werkzeuge und markierte Checkbox Eingeschaltet beim Modul LTI 1.3](assets/LTI_admin_config_v3_de.png){ class="shadow lightbox" title="Tab Konfiguration der Seite LTI in der System-Administration · 2026.10.07" }

Nach dem Einschalten zeigt der Tab zwei weitere Felder:

| Feld | Bemerkung |
|---|---|
| Plattform-ID | Die URL, mit der sich OpenOlat gegenüber externen Systemen identifiziert. Von OpenOlat vorgegeben, nur lesbar. Standard ist die Domain der Instanz. |
| Organisation | Die Organisation, der OpenOlat die Benutzerkonten zuordnet, die beim Zugriff aus einer externen Plattform neu angelegt werden. Ohne Auswahl gilt die Standard-Organisation. |

Die Seite LTI hat vier Tabs: "Konfiguration" für die Grundeinstellungen auf dieser Seite, "Externe Plattformen" für OpenOlat als Tool, "Externe Tools" für OpenOlat als Plattform und "Rollen-Mapping" für die Zuordnung der OpenOlat-Rollen zu den LTI-Rollen. Die Detailseiten dazu sind unten verlinkt.

## Deployments {: #deployments}

**Was ist ein Deployment?**

Auf der Seite der Plattform bestimmt das Deployment eines Tools, in welchem Umfang die Plattform das Tool zur Verfügung stellt:

* Einsatz in einem einzelnen Kurs
* Einsatz im gesamten System
* Einsatz nur für den aktuellen Kontext
* Einsatz generell ermöglicht (auch für zukünftige Kontexte)

Auf der Seite des Tools heisst das Gegenstück LTI-Freigabe: Ist OpenOlat das Tool, gibt eine LTI-Freigabe genau einen Kurs oder eine Gruppe für eine externe Plattform frei. In der Oberfläche heisst sie Deployment, etwa beim Button "Neues Deployment hinzufügen".

**Gilt eine Deployment-ID für mehrere Kurse?** [:octicons-tag-16:{ title="ab Release 21.1 (OO-9092)" }](https://track.frentix.com/issue/OO-9092)

Ja, wenn OpenOlat das Tool ist. Eine externe Plattform sendet oft für mehrere Kurse dieselbe Deployment-ID, nämlich wenn sie das Tool als gemeinsames Deployment führt. Als Plattform verwendet OpenOlat selbst eine gemeinsame Deployment-ID bei der Option "Mit Shared Deployment" und beim Kopieren eines Kursbausteins "LTI-Seite", siehe [Globales oder lokales Deployment](LTI_External_tools.de.md#deployment_scope). Diese Deployment-ID tragen Sie in der LTI-Freigabe jedes Kurses und jeder Gruppe ein, die die Plattform erreichen soll. Eindeutig sein muss sie nur je Plattform und Kurs beziehungsweise je Plattform und Gruppe. Welchen Kurs OpenOlat beim Aufruf öffnet, erkennt OpenOlat an der Adresse, die die Plattform mitschickt: [Eine Deployment-ID für mehrere Kurse](../../manual_user/learningresources/LTI_Share_courses.de.md#deployment_id_several_courses)

**Wer kann Deployments hinzufügen?** [:octicons-tag-16:{ title="ab Release 17.0 (OO-6300)" }](https://track.frentix.com/issue/OO-6300)

Systemadministrator:innen bestimmen in der System-Administration im Tab "Konfiguration" unter `Administration > Externe Werkzeuge > LTI`, wer Deployments hinzufügen darf. Die Einstellung gibt es getrennt für Kurse und für Gruppen.

**Kurs**

* "Rolle kann Deployment hinzufügen": Administrator:innen dürfen es immer. Zusätzlich lassen sich Lernressourcenverwalter:innen freischalten.
* "Besitzer:in mit Autorenrecht kann Deployment hinzufügen": "Für alle Kurse aktivieren" oder "Muss pro Kurs aktiviert werden".

**Gruppe**

* "Rolle kann Deployment hinzufügen": Administrator:innen dürfen es immer. Zusätzlich lassen sich Gruppenverwalter:innen freischalten.
* "Gruppenbetreuer:in mit Autorenrecht kann Deployment hinzufügen": "Für alle Gruppen aktivieren" oder "Muss pro Gruppe aktiviert werden".

![Markierte Bereiche Kurs und Gruppe mit den Rollen und Freigaben, die ein Deployment hinzufügen dürfen](assets/LTI_admin_deploy_v3_de.png){ class="shadow lightbox" title="Tab Konfiguration der Seite LTI · 2026.10.07" }

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
[LTI-Zugang zu einem Kurs konfigurieren >](../../manual_user/learningresources/LTI_Share_courses.de.md)<br>
[LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)<br>
[LTI - Deep Linking >](../administration/LTI_Deeplinking.de.md)<br>
[LTI - Externe Werkzeuge >](../administration/LTI_External_tools.de.md)

**Weiterführend**<br>
[Learning Tools Interoperability Core Specification (IMS Global Learning Consortium) >](http://www.imsglobal.org/spec/lti/v1p3/)<br>
[LTI - Externe Plattformen >](../administration/LTI_External_platforms.de.md)<br>
[LTI - Rollen-Mapping >](../administration/LTI_Role_Mapping.de.md)

[Zum Seitenanfang ^](#LTI_integrations)
