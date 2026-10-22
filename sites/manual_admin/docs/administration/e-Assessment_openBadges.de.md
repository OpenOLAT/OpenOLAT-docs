# e-Assessment Administration: OpenBadges {: #badges}

OpenBadges sind nach dem OpenBadges-Standard implementiert und voll kompatibel mit diesem.
Weitere Informationen zum Standard finden Sie [hier](https://www.imsglobal.org/activity/openbadges).

## Tab "Konfiguration" {: #tab_config}

* Hier schalten Sie Badges für die gesamte Instanz Ihres OpenOlat ein/aus.
* Ausserdem können LinkedIn-Organisationen, die Badges verwenden, hier hinzugefügt werden.

![OpenBadges eingeschaltet, darunter die noch leere Liste der LinkedIn-Organisationen und der Button LinkedIn-Organisation hinzufügen](assets/badges_global_config_v2_de.png){ class="shadow lightbox" title="Tab Konfiguration in der Administration OpenBadges" }

[Zum Seitenanfang ^](#badges)

---

## Tab "Vorlagen" {: #tab_templates}

Ein Standardset von Vorlagen ist bereits auf der OpenOlat Instanz vorbereitet. 

![Liste der vorbereiteten Badge-Vorlagen mit Bild, Name und Anwendungsbereich, darüber der Button Vorlage hochladen](assets/badges_global_templates_v2_de.png){ class="shadow lightbox" title="Tab Vorlagen in der Administration OpenBadges" }

Weitere Vorlagen können  erstellt werden, indem  Bild, Name und eine Beschreibung der Vorlage spezifiziert wird.

![Pflichtfelder Bild, Name und Anwendungsbereich mit den Optionen "Global" und "Kurs", bei Name und Beschreibung der Link "Übersetzung"](assets/badges-admin-global-templates_de.jpg){ class="shadow lightbox" title="Dialog Vorlage hochladen im Tab Vorlagen" }

#### Name {: #name }

Der Name der Vorlage wird im Wizard angezeigt.

#### Beschreibung {: #description }

Die Beschreibung der Vorlage wird automatisch aus der Vorlagen-Übersetzung übernommen und ist hier nicht bearbeitbar.

#### Kategorien {: #categories }

Hier kann man die Vorlagen nach Kategorien einteilen. Badge-Vorlagen mit gleicher Kategorie werden im gleichen Reiter im Wizard angezeigt.

#### Anwendungsbereich {: #scope }

Der Anwendungsbereich legt fest, ob ein Badge global (für das Ausstellen in der ganzen OpenOlat-Instanz) oder für Kurse verfügbar sein soll.

[Zum Seitenanfang ^](#badges)

---

## Tab "Globale Badges" {: #tab_global_badges}

Globale Badges können in einem separaten Tab eingesehen werden, ebenso ihr Status (aktiv / in Vorbereitung) und ob sie bereits vergeben wurden. Sie können auch bearbeitet und gelöscht werden. Globale Badges sind nicht an einen Kurs gebunden.

![Liste der globalen Badges mit Bild, Name, Status und Anzahl Vergaben, darunter der Button Globalen Badge hinzufügen](assets/badges_global_tab_globalBadges_v2_de.png){ class="shadow lightbox" title="Tab Globale Badges in der Administration OpenBadges" }


### Erstellen und Bearbeiten eines globalen Badges

Im Tab "Globale Badges" befindet sich auch der Button "Globalen Badge hinzufügen". Er startet den Wizard mit den folgenden Schritten:

1. **Bild**: Der erste Schritt ist die Auswahl einer Vorlage oder das Hochladen eines eigenen Bildes. OpenOlat unterstützt die Bildformate SVG und PNG. Für ein eigenes Bild wählen Sie "Eigener Badge" und laden die Datei hoch.
![Eigener Badge gewählt, darunter das Feld zum Hochladen der Datei, daneben die Vorlagen der Kategorie Motivation](assets/badges-wizard_step1_v2_de.png){ class="shadow lightbox" title="Schritt Bild im Wizard für globale Badges" }
2. **Anpassung**: Wenn die Vorlage entsprechend erstellt wurde, können Sie Farben und Text während der Erstellung des Badges ändern.
![Hintergrundfarbe Gold und Titel Gut gemacht! mit der Vorschau des fertigen Badges](assets/badges-wizard_step2_v2_de.png){ class="shadow lightbox" title="Schritt Anpassung im Wizard für globale Badges" }
3. **Vergabekriterien**: Geben Sie die Kriterien und die Erklärung für die von Ihnen gewählten Regeln an. Im Unterschied zu Badges, die von Autor:innen in einem Kurs vergeben werden, können globale Badges z.B. auch kursübergreifend für das Bestehen mehrerer Kurse vergeben werden.
![Kriterien-Beschreibung, Vergabeverfahren Automatisch vergeben oder Nur manuell vergeben und die Auswahl einer neuen Regel](assets/badges-wizard_step3_v2_de.png){ class="shadow lightbox" title="Schritt Vergabekriterien im Wizard für globale Badges" }
4. **Details**: Obligatorische Details sind der Name und die Beschreibung des Badges sowie der Herausgeber. Unter "Sprache" wählen Sie die Sprache des Badges. Sie können zusätzlich eine Herausgeber-URL und eine Herausgeber-E-Mail hinzufügen. Sind im Tab "Konfiguration" LinkedIn-Organisationen hinzugefügt, wählen Sie unter "LinkedIn-Organisation" zusätzlich eine davon aus. [:octicons-tag-16:{ title="ab Release 19.0 (OO-7741)" }](https://track.frentix.com/issue/OO-7741) Unter "Verfall" wählen Sie "Nie" oder "Gültig für" mit einer Gültigkeitsdauer, z.B. 12 Monate.
![Felder Sprache, Name, Beschreibung, Herausgeber, Herausgeber-URL, Herausgeber-E-Mail, LinkedIn-Organisation und Verfall mit der Wahl Nie](assets/badges-wizard_step4_v2_de.png){ class="shadow lightbox" title="Schritt Details im Wizard für globale Badges" }
5. **Zusammenfassung**: Zeigt zur Kontrolle Bild, Name, Sprache, Beschreibung, Ablauf des Badges und die Vergabekriterien.
![Badge-Bild, Name, Sprache, Beschreibung, Ablauf des Badges Nie und die Regel, wenn der Kurs bestanden ist, dann wird der Badge vergeben](assets/badges-wizard_step5_v2_de.png){ class="shadow lightbox" title="Schritt Zusammenfassung im Wizard für globale Badges" }
6. **Empfänger**: Zeigt die Empfänger in einer Tabelle an, um zu sehen, welche Teilnehmer:innen sich bereits gemäss der von Ihnen gewählten Kriterien qualifiziert haben. Dieser Schritt erscheint nur, wenn Sie unter "Vergabeverfahren" die Option "Automatisch vergeben" gewählt haben.
![Tabelle der Personen, die sich gemäss den gewählten Kriterien bereits qualifiziert haben und den Badge nach "Fertigstellen" erhalten](assets/badges-wizard_step6_v2_de.png){ class="shadow lightbox" title="Schritt Empfänger im Wizard für globale Badges" }

Solange ein globaler Badge den Status "Vorbereitung" hat, bearbeiten Sie ihn im Tab "Globale Badges" mit "Badge bearbeiten". Hat er den Status "Aktiv", steht stattdessen "Neue Version erstellen und bearbeiten" zur Verfügung. Beide Aktionen öffnen den Wizard erneut. [:octicons-tag-16:{ title="ab Release 20.1 (OO-8287)" }](https://track.frentix.com/issue/OO-8287)


### Globale Badges manuell vergeben

Die manuelle Vergabe ist in der System-Administration möglich unter:<br>
`Administration > e-Assessment > OpenBadges > Tab "Globale Badges" > "Badgename" > Tab "Übersicht" > Button "Manuell vergeben"`

![Weg zum Button Manuell vergeben über e-Assessment, OpenBadges, Tab Globale Badges, den gewählten Badge und Tab Übersicht](assets/badges_global_manually_v3_de.png){ class="shadow lightbox" title="Tab Übersicht eines globalen Badges in der Administration OpenBadges" }


### Globale Badges automatisch vergeben

Die automatische Vergabe wird während des Erstellens im Wizard eingerichtet.

!!! note "Hinweis"

    Bei der Vergabe eines globalen Badges wird dieser der empfangenden Person zusätzlich automatisch per E-Mail zugestellt, unabhängig davon, ob er manuell oder automatisch vergeben wird.

[Zum Seitenanfang ^](#badges)

---

## Tab "Vergebene globale Badges" {: #tab_awarded}

In diesem Tab werden vergebene **globale Badges** aufgelistet. (Die Kurs-Badges sind hier nicht enthalten.)


!!! note "Hinweis"

    **Kurs-Badges** können durch Betreuer:innen und Besitzer:innen im Bewertungswerkzeug eingesehen werden. Dort können die automatisch vergebenen Kurs-Badges eingesehen und Kurs-Badges manuell vergeben werden.


!!! note "Hinweis"

    Für Kursteilnehmer:innen sind erworbene Badges im Persönlichen Menü aufgelistet. [Hier](../../manual_user/personal_menu/OpenBadges.de.md) mehr dazu.


[Zum Seitenanfang ^](#badges)

---


## Tab "Verifizierung" {: #verification}

Im Tab "Verifizierung" kann eine Badge-Datei hochgeladen werden. (Sie kann einfach per Drag&drop in ein Feld gezogen werden.) Nach Klick auf den Button "Badge verifizieren" prüft OpenOlat, ob es sich um einen rechtmässig ausgestellen Badge handelt.

[Zum Seitenanfang ^](#badges)

---


## Weiterführende Informationen {: #further_information}

[Badges im Bewertungswerkzeug >](../../manual_user/learningresources/OpenBadges.de.md)<br>
[Persönliche Erfolge/Leistungen: Badges >](../../manual_user/personal_menu/OpenBadges.de.md)<br>
[Wie vergebe ich in meinem Kurs Badges? >](../../manual_how-to/badges/badges.de.md)<br>
[Der OpenBadges-Standard >](https://www.imsglobal.org/activity/openbadges)<br>

[Zum Seitenanfang ^](#badges)
