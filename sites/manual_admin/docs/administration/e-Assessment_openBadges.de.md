# e-Assessment Administration: OpenBadges {: #badges}

Badges sind digitale Auszeichnungen mit Bild, Kriterien und ausstellender Stelle. Wer einen Badge erhält, kann ihn auch ausserhalb von OpenOlat vorweisen, und jede Stelle kann maschinell prüfen, ob er echt ist. OpenOlat setzt dafür den [OpenBadges-Standard](https://www.imsglobal.org/activity/openbadges) um und ist voll kompatibel mit ihm.

Systemadministrator:innen schalten die Badges für die ganze OpenOlat-Instanz ein, pflegen die Badge-Vorlagen, erstellen globale Badges und prüfen die Echtheit von Badges. Alle diese Einstellungen liegen in der System-Administration unter:<br>
`Administration > e-Assessment > OpenBadges`

## Tab "Konfiguration" [:octicons-tag-16:{ title="ab Release 18.0 (OO-6999)" }](https://track.frentix.com/issue/OO-6999) {: #tab_config}

Im Tab "Konfiguration" schalten Sie die Badges ein und legen fest, wie sich ihre Echtheit prüfen lässt.

* Mit der Checkbox "OpenBadges" schalten Sie Badges für die gesamte OpenOlat-Instanz ein. Sobald OpenBadges eingeschaltet ist, lassen sich die Tabs "Globale Badges" und "Vergebene globale Badges" anklicken. Der Tab "Konfiguration" zeigt dann zusätzlich die Einstellung "Verifizierung" und die Liste der LinkedIn-Organisationen.
* Unter "Verifizierung" legen Sie fest, wie sich die Echtheit der Badges Ihrer Instanz prüfen lässt. Bei "Hosted" holt die Prüfung die Angaben des Badges von Ihrer OpenOlat-Instanz ab. Bei "Signed" trägt jeder vergebene Badge zusätzlich eine digitale Signatur, die belegt, dass er von Ihrer Instanz stammt und unverändert ist. Den Schlüssel für die Signatur legt OpenOlat für jeden Badge selbst an. Voreingestellt ist "Hosted". Die Einstellung gilt für alle Badges, die danach erstellt werden, für globale Badges wie für Kurs-Badges. Bestehende Badges behalten ihre Methode, auch wenn Sie später eine neue Version eines Badges erstellen. [:octicons-tag-16:{ title="ab Release 20.1 (OO-8288)" }](https://track.frentix.com/issue/OO-8288)
* Mit dem Button "LinkedIn-Organisation hinzufügen" erfassen Sie LinkedIn-Organisationen. Die erfassten Organisationen stehen beim Erstellen eines Badges im Schritt "Details" unter "LinkedIn-Organisation" zur Wahl. Übernimmt eine empfangende Person den Badge mit "Zu LinkedIn hinzufügen" in ihr LinkedIn-Profil, nennt LinkedIn die gewählte Organisation als Herausgeberin.

![OpenBadges eingeschaltet, die Verifizierung Hosted oder Signed, darunter die Liste der LinkedIn-Organisationen und der Button LinkedIn-Organisation hinzufügen](assets/badges_global_config_v3_de.png){ class="shadow lightbox" title="Tab Konfiguration unter OpenBadges in der System-Administration · 2026.11.10" }

[Zum Seitenanfang ^](#badges)

---

## Tab "Vorlagen" {: #tab-templates}

Mit Vorlagen geben Sie das Bild eines Badges vor, damit Autor:innen beim Erstellen schnell loslegen. Ein Standardset von Vorlagen ist auf der OpenOlat-Instanz bereits vorbereitet. Die Tabelle zeigt je Vorlage "Bild", "Name", "Anwendungsbereich" und "Tags". Unter "Tags" stehen die Kategorien der Vorlage. Mit "Bearbeiten" und "Löschen" ändern oder entfernen Sie eine Vorlage.

![Liste der vorbereiteten Badge-Vorlagen mit Bild, Name, Anwendungsbereich und Tags, darüber der Button Vorlage hochladen](assets/badges_global_templates_v3_de.png){ class="shadow lightbox" title="Tab Vorlagen unter OpenBadges in der System-Administration · 2026.11.10" }

Mit dem Button "Vorlage hochladen" fügen Sie eine eigene Vorlage hinzu. Im gleichnamigen Dialog laden Sie das Bild hoch und legen Name, Beschreibung, Kategorien und Anwendungsbereich fest.

![Pflichtfelder Bild, Name und Anwendungsbereich mit den Optionen "Global" und "Kurs", bei Name und Beschreibung der Link "Übersetzung"](assets/badges-admin-global-templates_de.jpg){ class="shadow lightbox" title="Dialog Vorlage hochladen im Tab Vorlagen" }

#### Name {: #name }

Der Name erscheint in der Liste der Vorlagen und im Wizard. Sie geben ihn über den Link "Übersetzung" für jede Sprache ein.

#### Beschreibung {: #description }

Auch die Beschreibung geben Sie über den Link "Übersetzung" für jede Sprache ein. Der Dialog zeigt den eingegebenen Text danach an.

#### Kategorien {: #categories }

Mit Kategorien gruppieren Sie die Vorlagen. Im Schritt "Bild" des Wizards stehen die Kategorien über den Vorlagen. Ein Klick auf eine Kategorie zeigt nur noch deren Vorlagen.

#### Anwendungsbereich {: #scope }

Der Anwendungsbereich legt fest, wo die Vorlage zur Wahl steht: mit "Global" beim Erstellen globaler Badges, mit "Kurs" beim Erstellen von Kurs-Badges. Sie können beide Optionen zusammen wählen.

[Zum Seitenanfang ^](#badges)

---

## Tab "Globale Badges" {: #global_badges}

Globale Badges sind nicht an einen Kurs gebunden. Im Tab "Globale Badges" behalten Sie alle globalen Badges der Instanz im Blick, sehen, wie oft sie vergeben sind, und bearbeiten oder löschen sie. Der Tab lässt sich anklicken, sobald OpenBadges im Tab "Konfiguration" eingeschaltet ist.

Die Tabelle zeigt in der Standardansicht die Spalten "Bild", "Name", "Erstellt am", "Status", "Typ", "Version" und "Vergeben an". Der Status ergibt sich aus den Vergaben: "Vorbereitung", solange der Badge noch nicht vergeben ist, "Aktiv", sobald mindestens eine Vergabe gilt, und "Widerrufen", wenn alle Vergaben widerrufen sind. Die Spalte "Typ" zeigt, ob der Badge automatisch oder nur manuell vergeben wird: "Automatisch" steht für das Vergabeverfahren "Automatisch vergeben", "Manuell" für "Nur manuell vergeben". Die Spalte "Vergeben an" zeigt, wie oft der Badge über alle seine Versionen vergeben ist. Widerrufene Vergaben zählen nicht mit. Die Spalte "Verifizierung" mit der Methode "Hosted" oder "Signed" ist ausgeblendet. Sie blenden sie über das Zahnrad-Symbol "Spalten auswählen" über der Tabelle ein.

![Liste der globalen Badges mit Bild, Name, Erstellungsdatum, Status, Typ, Version und Anzahl Vergaben, darüber der Button Einen neuen Badge erstellen](assets/badges_global_tab_globalBadges_v3_de.png){ class="shadow lightbox" title="Tab Globale Badges unter OpenBadges in der System-Administration · 2026.11.10" }

Die Aktionen zu einem Badge erreichen Sie direkt in seiner Zeile, an zwei Stellen. Das Plus-Symbol am Zeilenanfang ("Details dieser Zeile anzeigen") klappt die Zeile auf: Dort stehen die Kriterien des Badges als Satz und darunter Buttons. Bei einem Badge vom Typ "Manuell" bleibt der Bereich der Kriterien leer. Das Menü "Weitere Aktionen" am Zeilenende bietet zusätzlich "Kopieren" und "Löschen". Welche Aktionen erscheinen, hängt vom Status des Badges ab:

| Status | Buttons in den Details der Zeile | Menü "Weitere Aktionen" |
|---|---|---|
| Vorbereitung | "Badge bearbeiten", "Manuell vergeben" | "Manuell vergeben", "Bearbeiten", "Kopieren", "Löschen" |
| Aktiv | "Neue Version erstellen und bearbeiten", "Manuell vergeben" | "Manuell vergeben", "Widerrufen", "Neue Version erstellen und bearbeiten", "Kopieren", "Löschen" |

"Widerrufen" im Menü widerruft alle Vergaben des Badges. Der Eintrag erscheint nur, solange der Badge mindestens eine Vergabe hat, die nicht widerrufen ist.

### Erstellen und Bearbeiten eines globalen Badges

Mit dem Button "Einen neuen Badge erstellen" über der Tabelle im Tab "Globale Badges" starten Sie den Wizard. Gibt es noch keinen globalen Badge, steht derselbe Button zusätzlich in der Mitte der leeren Tabelle. Der Wizard führt durch die folgenden Schritte:

1. **Bild**: Wählen Sie eine Vorlage oder laden Sie ein eigenes Bild hoch. OpenOlat unterstützt die Bildformate SVG und PNG. Für ein eigenes Bild wählen Sie "Eigener Badge" und laden die Datei hoch.
![Eigener Badge gewählt, darunter das Feld zum Hochladen der Datei, daneben die Vorlagen der Kategorie Motivation](assets/badges-wizard_step1_v2_de.png){ class="shadow lightbox" title="Schritt Bild im Wizard für globale Badges" }
2. **Anpassung**: Dieser Schritt erscheint, wenn die gewählte Vorlage anpassbar ist. Hier ändern Sie zum Beispiel Hintergrundfarbe und Titel des Badges.
![Hintergrundfarbe Gold und Titel Gut gemacht! mit der Vorschau des fertigen Badges](assets/badges-wizard_step2_v2_de.png){ class="shadow lightbox" title="Schritt Anpassung im Wizard für globale Badges" }
3. **Vergabekriterien**: Unter "Kriterien-Beschreibung" erklären Sie, wofür der Badge vergeben wird. Unter "Vergabeverfahren" wählen Sie "Automatisch vergeben" oder "Nur manuell vergeben", unter "Kriterien" die Regeln für die automatische Vergabe. Für globale Badges sind das "Kurse bestanden" (die gewählten Kurse sind bestanden) und "Badges erworben" (die gewählten anderen globalen Badges sind schon vergeben). Anders als Kurs-Badges, die Autor:innen in einem Kurs vergeben, vergeben Sie globale Badges auch kursübergreifend, zum Beispiel für das Bestehen mehrerer Kurse.
![Kriterien-Beschreibung, Vergabeverfahren Automatisch vergeben oder Nur manuell vergeben und die Auswahl einer neuen Regel](assets/badges-wizard_step3_v2_de.png){ class="shadow lightbox" title="Schritt Vergabekriterien im Wizard für globale Badges" }
4. **Details**: Pflichtangaben sind Name und Beschreibung des Badges sowie der Herausgeber. Unter "Sprache" wählen Sie die Sprache des Badges. Sie können zusätzlich eine Herausgeber-URL und eine Herausgeber-E-Mail hinzufügen. Sind im Tab "Konfiguration" LinkedIn-Organisationen hinzugefügt, wählen Sie unter "LinkedIn-Organisation" zusätzlich eine davon aus. [:octicons-tag-16:{ title="ab Release 19.0 (OO-7741)" }](https://track.frentix.com/issue/OO-7741) Unter "Verfall" wählen Sie "Nie" oder "Gültig für" mit einer Gültigkeitsdauer, z.B. 12 Monate.
![Felder Sprache, Name, Beschreibung, Herausgeber, Herausgeber-URL, Herausgeber-E-Mail, LinkedIn-Organisation und Verfall mit der Wahl Nie](assets/badges-wizard_step4_v2_de.png){ class="shadow lightbox" title="Schritt Details im Wizard für globale Badges" }
5. **Zusammenfassung**: Zeigt zur Kontrolle Bild, Name, Sprache, Beschreibung, Ablauf des Badges (die Angabe unter "Verfall") und die Vergabekriterien.
![Badge-Bild, Name, Sprache, Beschreibung, Ablauf des Badges Nie und die Regel, wenn der Kurs bestanden ist, dann wird der Badge vergeben](assets/badges-wizard_step5_v2_de.png){ class="shadow lightbox" title="Schritt Zusammenfassung im Wizard für globale Badges" }
6. **Empfänger**: Zeigt in einer Tabelle, welche Personen die gewählten Kriterien bereits erfüllen. Diese Personen erhalten den Badge, sobald Sie auf "Fertigstellen" klicken. Dieser Schritt erscheint nur, wenn Sie unter "Vergabeverfahren" die Option "Automatisch vergeben" gewählt haben.
![Tabelle mit Anmeldename, Nachname und Vorname der Personen, die den Badge nach "Fertigstellen" erhalten](assets/badges-wizard_step6_v2_de.png){ class="shadow lightbox" title="Schritt Empfänger im Wizard für globale Badges" }

Solange ein globaler Badge den Status "Vorbereitung" hat, bearbeiten Sie ihn im Tab "Globale Badges" mit "Badge bearbeiten". Hat er den Status "Aktiv", steht stattdessen "Neue Version erstellen und bearbeiten" zur Verfügung. Beide Aktionen öffnen den Wizard erneut. [:octicons-tag-16:{ title="ab Release 20.1 (OO-8287)" }](https://track.frentix.com/issue/OO-8287)


### Globale Badges manuell vergeben

Einen globalen Badge vergeben Sie manuell in der System-Administration unter:<br>
`Administration > e-Assessment > OpenBadges > Tab "Globale Badges" > "Badgename" > Tab "Übersicht" > Button "Manuell vergeben"`

![Weg zum Button Manuell vergeben über e-Assessment, OpenBadges, Tab Globale Badges, den gewählten Badge und Tab Übersicht](assets/badges_global_manually_v4_de.png){ class="shadow lightbox" title="Tab Übersicht eines globalen Badges unter OpenBadges in der System-Administration · 2026.11.10" }

Denselben Button finden Sie auch in der Liste des Tabs "Globale Badges", in den Details einer Zeile und im Menü "Weitere Aktionen". Der Button öffnet den Wizard "Globalen Badge … vergeben". Im Schritt "Benutzersuche" wählen Sie die Personen aus, im Schritt "Überprüfen" kontrollieren Sie die Auswahl. Mit "Fertigstellen" erhalten die gewählten Personen den Badge. Wer den Badge schon erhalten hat, sehen Sie im Tab "Empfänger" neben dem Tab "Übersicht".

### Globale Badges automatisch vergeben

Die automatische Vergabe richten Sie beim Erstellen im Wizard ein, im Schritt "Vergabekriterien". Personen, die die Regeln erst später erfüllen, erhalten den Badge ebenfalls automatisch, zum Beispiel sobald sie den letzten der gewählten Kurse bestanden haben.

!!! note "Hinweis"

    OpenOlat stellt jeden vergebenen globalen Badge der empfangenden Person zusätzlich per E-Mail zu, ob er manuell oder automatisch vergeben wird.

[Zum Seitenanfang ^](#badges)

---

## Tab "Vergebene globale Badges" {: #tab-awarded-global-badges}

In diesem Tab sehen Sie, wer welchen globalen Badge erhalten hat. Die Tabelle zeigt je Vergabe unter anderem "Empfänger", "Vergeben von" und "Vergeben am". Mit dem Link "Widerrufen" in der Zeile einer aktiven Vergabe entziehen Sie sie. Eine widerrufene Vergabe entfernen Sie danach mit dem Papierkorb-Symbol: Es erscheint nur in Zeilen widerrufener Vergaben, in einer eigenen Spalte ohne Beschriftung, deren Kopf ebenfalls nur das Symbol zeigt. Ist das Ablaufdatum einer widerrufenen Vergabe überschritten, zeigt die Spalte "Status" "Abgelaufen" statt "Widerrufen", weil OpenOlat den Ablauf vor dem Widerruf anzeigt; der Papierkorb steht trotzdem in der Zeile. Kurs-Badges erscheinen hier nicht.


!!! note "Hinweis"

    Kurs-Badges sehen Betreuer:innen und Besitzer:innen im Bewertungswerkzeug des Kurses unter `Kurs > Administration > Bewertungswerkzeug`. Dort vergeben sie Kurs-Badges auch manuell, siehe [Badges im Bewertungswerkzeug](../../manual_user/learningresources/OpenBadges.de.md).


!!! note "Hinweis"

    Teilnehmer:innen finden ihre erworbenen Badges im persönlichen Menü, siehe [Persönliche Erfolge/Leistungen: Badges](../../manual_user/personal_menu/OpenBadges.de.md).


[Zum Seitenanfang ^](#badges)

---


## Tab "Verifizierung" {: #verification}

Im Tab "Verifizierung" prüfen Sie, ob ein Badge echt ist. Laden Sie die Badge-Datei hoch oder ziehen Sie sie per Drag and Drop in das Feld. Nach einem Klick auf den Button "Badge verifizieren" prüft OpenOlat, ob der Badge rechtmässig ausgestellt ist, und zeigt das Ergebnis unter "Verifizierungs-Bericht".

[Zum Seitenanfang ^](#badges)

---


## Weiterführende Informationen {: #further_information}

[Badges im Bewertungswerkzeug >](../../manual_user/learningresources/OpenBadges.de.md)<br>
[Persönliche Erfolge/Leistungen: Badges >](../../manual_user/personal_menu/OpenBadges.de.md)<br>
[Wie vergebe ich in meinem Kurs Badges? >](../../manual_how-to/badges/badges.de.md)<br>
[Der OpenBadges-Standard >](https://www.imsglobal.org/activity/openbadges)<br>
[e-Assessment Administration: Übersicht >](e-Assessment_Administration/index.de.md)<br>
[Wie mache ich Erfolge und Leistungen sichtbar? >](../../manual_how-to/achievements/achievements.de.md)

[Zum Seitenanfang ^](#badges)
