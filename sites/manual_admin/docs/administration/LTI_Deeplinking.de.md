# LTI - Deep Linking {: #LTI_deeplinking}


OpenOlat unterstützt Deep Linking entsprechend dem [LTI 1.3 Deep-Linking Protokoll](https://www.imsglobal.org/spec/lti-dl/v2p0).

## Funktionsbeschreibung {: #functional_description}

Deep Linking ist ein Service des LTI 1.3, der es Autor:innen ermöglicht, in den externen Inhalten, die via LTI eingebunden werden, die Kursteilnehmer:innen direkt an eine bestimmte Stelle zu führen.  

**Beispiel:**<br>
Statt im Kursbaustein einen Link zu einem Buch anzugeben und die Lernenden ein empfohlenes Kapitel selbst suchen zu lassen (Scrollen), kann direkt ein bestimmtes Kapitel angezeigt werden.

Damit die OpenOlat-Autor:innen die Deep Links zum externen Tool in den Kursbausteinen ermöglichen können, ohne immer wieder Angaben zu Anmeldung und Parameterübergabe machen zu müssen, kann die Deep Linking Funktion von den Administrator:innen der OpenOlat-Instanz aktiviert werden. Dies vereinfacht die Arbeit der Autor:innen bei der Konfiguration eines LTI-Kursbausteins.

## Verfügbare Features {: #available_features}

Zwischen OpenOlat und dem eingebundenen Tool können verschiedene Informationen zu Kurs und Kursteilnehmer:in ausgetauscht werden. In OpenOlat umfasst dies:

* Content Types
    * ResourceLink
    * Link
    * Image
    * File
    * HTML
* Properties
    * type
    * url
    * title
    * text
    * thumbnail
    * window
    * iframe


## Konfiguration {: #configuration}

### Globale Konfiguration

Wenn von Administrator:innen auf globaler Ebene ein LTI-Tool eingerichtet wird, kann dabei auch eine Option für Deep Links aktiviert werden.
Die Aktivierung bewirkt, dass alle gemachten Einstellungen für das Tool (Ermöglichung der Nutzung ohne erneute separate Anmeldung) auch für Deep Links gelten, die Kursautor:innen im LTI-Kursbaustein angeben.

Den Toggle-Button "Deep-Linking aktivieren" finden Sie in der System-Administration unter:<br>
`Administration > Externe Werkzeuge > LTI > Tab "Externe Tools" > Button "Bearbeiten"`

![Toggle Deep-Linking aktivieren auf EIN, im Dialog für ein LTI-Tool unter Externe Werkzeuge](assets/LTI_admin_deeplinking_activate_v1_de.png){ class="shadow lightbox" }

### Konfiguration im Kurs

Wurde Deep Linking für Autor:innen gestattet, können sie bei der Konfiguration des LTI-Kursbausteins vorkonfigurierte Links unter "LTI Version" auswählen:<br>
`Kurs > Kurseditor > Kursbaustein "LTI-Seite" > Tab "Seiteninhalt"`

Wird eine der Vorkonfigurationen ausgewählt, wird die benötigte URL gleich eingetragen und als Autor:in muss man sich nicht mehr darum kümmern.

![Auswahlliste LTI Version mit dem Wert LTI 1.3, im Tab Seiteninhalt des Kursbausteins LTI-Seite](assets/LTI_page_content_version_v1_de.png){ class="shadow lightbox" }

![Geöffnete Auswahlliste LTI Version mit den beiden LTI-Versionen und darunter den vorkonfigurierten Tools](assets/LTI_page_content_version_select_v1_de.png){ class="shadow lightbox" }


Anschliessend können die dabei erzeugten Parameter Client-ID und Deployment-ID verwendet werden, um damit auf Seite des eingebundenen Tools den Abschluss vorzunehmen.

!!! tip "Tipp"

    Damit die Deployment-ID erzeugt wird, muss eine Änderung im Tab "Seiteninhalt" zuerst gespeichert werden. Das gilt besonders dann, wenn unter "LTI Version" ein vorkonfigurierter Link ausgewählt wurde.

Der Button "Inhalt auswählen" erscheint nur, wenn Deep Linking für das externe Tool aktiviert ist. Nutzbar wird er, sobald Client-ID und Deployment-ID vorliegen. Er öffnet die Inhaltsauswahl des externen Tools. Die dort gewählten Inhalte erscheinen anschliessend im Feld "Ressourcen". [:octicons-tag-16:{ title="ab Release 18.1 (OO-7173)" }](https://track.frentix.com/issue/OO-7173)


### Seitenaufruf

Wenn im Kursbaustein "LTI-Seite" der externe Inhalt sofort gestartet werden soll, muss im Kurseditor im Tab "Seiteninhalt" die Option "Inhalt automatisch starten" angewählt sein. Andernfalls erscheint ein Button, mit dem von den Lernenden explizit die eingebundene Seite gestartet werden muss.

![Checkbox Inhalt automatisch starten, darüber die ausgefüllten Felder URL, Client-ID und Deployment-ID](assets/LTI_page_content_launch_v1_de.png){ class="shadow lightbox" }



## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**
IMS Global Learning Consortium: [LTI 1.3 Deep-Linking protocol](https://www.imsglobal.org/spec/lti-dl/v2p0)

**Weiterführend**
IMS Global Learning Consortium: [Learning Tools Interoperability Core Specification](http://www.imsglobal.org/spec/lti/v1p3/)<br>
Administrationshandbuch: [LTI 1.3 Integrationen](../administration/LTI_Integrations.de.md)<br>
Administrationshandbuch: [LTI - Externe Werkzeuge](../administration/LTI_External_tools.de.md)<br>
Administrationshandbuch: [LTI - Externe Plattformen](../administration/LTI_External_platforms.de.md)<br>
Administrationshandbuch: [LTI - Rollen-Mapping](../administration/LTI_Role_Mapping.de.md)<br>
Benutzerhandbuch: [LTI-Zugang zu einem Kurs konfigurieren](../../manual_user/learningresources/LTI_Share_courses.de.md)<br>
Benutzerhandbuch: [Kursbaustein "LTI-Seite"](../../manual_user/learningresources/Course_Element_LTI_Page.de.md)<br>
Benutzerhandbuch: [LTI-Zugang zu einer Gruppe konfigurieren](../../manual_user/groups/LTI_Share_groups.de.md)

[Zum Seitenanfang ^](#LTI_deeplinking)
