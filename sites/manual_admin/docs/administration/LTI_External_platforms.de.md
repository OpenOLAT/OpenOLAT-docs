# LTI - Externe Plattformen [:octicons-tag-16:{ title="ab Release 15.5 (OO-5205)" }](https://track.frentix.com/issue/OO-5205) {: #LTI_external_platforms}


## OpenOlat als "Tool" {: #openolat_tool}

Wird OpenOlat im Sinn der LTI-Terminologie als "Tool" eingesetzt, werden in OpenOlat vorhandene Kurse auf einem anderen LMS dargestellt. Seitens OpenOlat müssen für die reibungslose Kommunikation der beiden Systeme Angaben zur empfangenden Plattform (consumer) gemacht werden.

Administrator:innen konfigurieren das Zusammenspiel mit den anderen Plattformen (auch "platform" im Sinn der LTI-Terminologie) in der System-Administration unter: `Administration > Externe Werkzeuge > LTI`, Tab "Externe Plattformen". OpenOlat ist dann das **Tool**, in das der Kurs von den hier definierten Plattformen eingebunden wird.

![Tab Externe Plattformen ohne Eintrag mit dem Button Neue externe Plattform und dem Hinweis, dass noch keine externe LMS-Plattform verknüpft ist. Bereich LTI in der System-Administration.](assets/LTI_admin_platform_v2_de.png){ class="shadow lightbox" }

Für jede externe Plattform muss eine eigene Konfiguration eingerichtet werden. Verwenden Sie den Button "Neue externe Plattform", um die Verbindung zu einer neuen Plattform anzulegen.


!!! info "Wichtig"

    Werden mehrere verschiedene OpenOlat-Kurse von der gleichen externen Plattform genutzt, genügt es, die externe Plattform in der System-Administration nur einmal zu konfigurieren. Die weitere Konfiguration pro Kurs nehmen die Kursbesitzer:innen in den Einstellungen des jeweiligen Kurses vor: `Kurs > Administration > Einstellungen > Freigabe`, Abschnitt "LTI 1.3 Zugangskonfiguration". Für Gruppen gilt dasselbe im Tab "Freigabe" der Gruppe.


## Konfiguration {: #config}

Ein Muster einer gesamten Konfiguration finden Sie unter [LTI-Zugang zu einem Kurs konfigurieren](../../manual_user/learningresources/LTI_Share_courses.de.md).

In OpenOlat werden im Dialog "Neue externe Plattform" die folgenden Parameter der externen Partner-Instanz erfasst:

| Feld | Bemerkung |
| --------------------- | ---------------------------------------------- |
| Name | Frei definierbar. Pflichtfeld |
| Benutzer:innen mit E-mail Adresse paaren | Standard "Nein". Bei "Ja" verbindet OpenOlat eine Person, die aus der externen Plattform zum ersten Mal zugreift, mit dem bestehenden OpenOlat-Konto, das dieselbe E-Mail-Adresse trägt, statt ein neues LTI-Konto anzulegen. Das funktioniert nur, wenn die E-Mail-Adressen im System eindeutig sein müssen und genau ein Konto mit dieser Adresse existiert. Aktivieren Sie die Option nur für Plattformen, denen Sie vertrauen |
| Plattform-ID / Issuer | URL zur externen Instanz. Pflichtfeld |
| Client-ID | Client ID aus dem Dialog "Tool configuration details" in der externen Plattform. Pflichtfeld |
| Anmelde-URL | Von OpenOlat vorgegeben, nur lesbar. Diese URL tragen Sie in der externen Plattform als Initiate login URL ein |
| Umleitungs-URL | Von OpenOlat vorgegeben, nur lesbar. Diese URL tragen Sie in der externen Plattform als Redirection URL ein |
| Öffentlicher Schlüsseltyp | "RSA-Schlüssel" (Standard) oder "Schlüsselsatz-URL". Die Auswahl bestimmt, ob OpenOlat darunter den öffentlichen Schlüssel oder die URL des öffentlichen Schlüsselsatzes anzeigt |
| Öffentlicher Schlüssel / Öffentlicher Schlüsselsatz | Von OpenOlat erzeugt, nur lesbar. Diesen Schlüssel oder diese URL tragen Sie anschliessend in der Tool-Konfiguration der externen Plattform ein |
| Authorization | Aus der externen Instanz: Authentication request URL. Pflichtfeld |
| URL für Zugriffstoken | Aus der externen Instanz: Access token URL. Pflichtfeld |
| URL des öffentlichen Schlüsselbundes | Aus der externen Instanz: Public Keyset URL. Pflichtfeld |


Tragen Sie nach Abschluss des Formulars den öffentlichen Schlüssel auf der externen Instanz in der dortigen Tool-Konfiguration ein.

![Sechs Pflichtfelder für die Angaben der externen Plattform, dazu die von OpenOlat vorgegebene Anmelde-URL, Umleitungs-URL und der erzeugte öffentliche Schlüssel. Dialog Neue externe Plattform.](assets/LTI_admin_platform_config_v2_de.png){ class="lightbox" }


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[LTI-Zugang zu einem Kurs konfigurieren >](../../manual_user/learningresources/LTI_Share_courses.de.md)

**Weiterführend**<br>
[Learning Tools Interoperability Core Specification (IMS Global Learning Consortium) >](http://www.imsglobal.org/spec/lti/v1p3/)<br>
[LTI 1.3 Integrationen >](../administration/LTI_Integrations.de.md)<br>
[LTI - Externe Werkzeuge >](../administration/LTI_External_tools.de.md)<br>
[LTI - Deep Linking >](../administration/LTI_Deeplinking.de.md)<br>
[LTI - Rollen-Mapping >](../administration/LTI_Role_Mapping.de.md)<br>
[Kursbaustein "LTI-Seite" >](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
[LTI-Zugang zu einer Gruppe konfigurieren >](../../manual_user/groups/LTI_Share_groups.de.md)

[Zum Seitenanfang ^](#LTI_external_platforms)
