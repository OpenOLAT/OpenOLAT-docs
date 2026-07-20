# e-Assessment Administration: OpenBadges {: #badges}

OpenBadges sind nach dem OpenBadges-Standard implementiert und voll kompatibel mit diesem.
Weitere Informationen zum Standard finden Sie [hier](https://www.imsglobal.org/activity/openbadges).

## Tab "Konfiguration" {: #tab_config}

* Hier schalten Sie Badges für die gesamte Instanz Ihres OpenOlat ein/aus.
* Ausserdem können Organisationen, die Badges verwenden, hier hinzugefügt werden.

![badges_global_config_v2_de.png](assets/badges_global_config_v2_de.png){ class="shadow lightbox" }

[Zum Seitenanfang ^](#badges)

---

## Tab "Vorlagen" {: #tab_templates}

Ein Standardset von Vorlagen ist bereits auf der OpenOlat Instanz vorbereitet. 

![badges_global_templates_v2_de.png](assets/badges_global_templates_v2_de.png){ class="shadow lightbox" }

Weitere Vorlagen können  erstellt werden, indem  Bild, Name und eine Beschreibung der Vorlage spezifiziert wird.

![Templateansicht](assets/badges-admin-global-templates.de.jpg)

### Name

Der Name der Vorlage wird im Wizard angezeigt.

### Kategorien

Hier kann man die Vorlagen nach Kategorien einteilen. Badge-Vorlagen mit gleicher Kategorie werden im gleichen Reiter im Wizard angezeigt.

### Anwendungsbereich

Der Anwendungsbereich legt fest, ob ein Badge global (für das Ausstellen auf Instanzebene) oder für Kurse verfügbar sein soll.

[Zum Seitenanfang ^](#badges)

---

## Tab "Globale Badges" {: #tab_global_badges}

Globale Badges können in einem separaten Tab eingesehen werden, ebenso ihr Status (aktiv / in Vorbereitung) und ob sie bereits vergeben wurden. Sie können auch bearbeitet und gelöscht werden. Globale Badges sind nicht an einen Kurs gebunden.

![badges_global_tab_globalBadges_v2_de.png](assets/badges_global_tab_globalBadges_v2_de.png){ class="shadow lightbox" }


### Erstellen und Bearbeiten eines globalen Badges

Im Tab "Globale Badges" befindet sich auch der Button "Globalen Badge hinzufügen". Er startet das Badge-Tool (Wizard) mit den folgenden Schritten:

1. **Vorlage**: Der erste Schritt ist die Auswahl einer Vorlage oder das Hochladen eines eigenen Bildes. Derzeit wird SVG unterstützt.
![Wizard Schritt 1](assets/badges-wizard_step1_v2_de.png){ class="shadow lightbox" }
2. **Anpassung**: Wenn die Vorlage entsprechend erstellt wurde, können Sie Farben und Text während der Erstellung des Badges ändern.
![Wizard Schritt 2](assets/badges-wizard_step2_v2_de.png){ class="shadow lightbox" }
3. **Vergabekriterien**: Geben Sie die Kriterien und die Erklärung für die von Ihnen gewählten Regeln an. Im Unterschied zu Badges, die von Autor:innen in einem Kurs vergeben werden, können globale Badges z.B. auch kursübergreifend für das Bestehen mehrerer Kurse vergeben werden.
![Wizard Schritt 3](assets/badges-wizard_step3_v2_de.png){ class="shadow lightbox" }
4. **Details & Validierungszeitraum:** Obligatorische Details sind der Name, die Version und die Beschreibung des Badge sowie der Aussteller. Sie können zusätzlich eine URL und einen Kontakt zu den Ausstellereigenschaften hinzufügen. Die Gültigkeitsdauer kann auch so festgelegt werden, dass sie nie abläuft oder z.B. 12 Monate beträgt.
![Wizard Schritt 4](assets/badges-wizard_step4_v2_de.png){ class="shadow lightbox" }
5. **Zusammenfassung**: Bildschirm mit einer Zusammenfassung der wichtigen Details.
![Wizard Schritt 5](assets/badges-wizard_step5_v2_de.png){ class="shadow lightbox" }
6. **Empfänger**: Zeigt die Empfänger in einer Tabelle an, um zu sehen, welche Teilnehmer:innen sich bereits gemäss der von Ihnen gewählten Kriterien qualifiziert haben.
![Wizard Schritt 6](assets/badges-wizard_step6_v2_de.png){ class="shadow lightbox" }


### Globale Badges manuell vergeben

Die manuelle Vergabe ist möglich unter<br>
**Administration > e-Assessment > OpenBadges > Tab "Globale Badges" > Badge wählen > Tab Übersicht > Button "Manuell vergeben"**.

![badges_global_manually_v3_de.png](assets/badges_global_manually_v3_de.png){ class="shadow lightbox" }


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


## Weiterführende Informationen  {: #further_information}

[Badges im Bewertungswerkzeug >](../../manual_user/learningresources/OpenBadges.de.md)<br>
[Wie vergebe ich in meinem Kurs Badges? >](../../manual_how-to/badges/badges.de.md)<br>
[Der OpenBadges-Standard >](https://www.imsglobal.org/activity/openbadges)<br>
