# Kurseinstellungen - Tab Freigabe {: #tab_share}

Den Tab Freigabe öffnen Sie im Kurs über `Kurs > Administration > Einstellungen > Tab "Freigabe"`.

![Über das Werkzeug-Menü Administration und den Eintrag Einstellungen erreichen Sie die Einstellungs-Tabs, darunter den Tab Freigabe](assets/course_settings_share_entry_v1_de.png){ class="shadow lightbox" title="Menü Administration eines Kurses" }

Im Tab Freigabe finden Sie diese Abschnitte. Welche davon ein Kurs tatsächlich zeigt, hängt an seinem Verwendungszweck: siehe [Welche Abschnitte erscheinen?](#sections_by_usage)

[Verwendung](#section_usage)<br>
[Freigabe](#section_share)<br>
[Angebot](#section_offer)<br>
[LTI 1.3 Zugangskonfiguration](#section_LTI)<br>
[Freigabeübersicht](#section_share_overview)<br>

---

## Welche Abschnitte erscheinen? {: #sections_by_usage}

Der Tab Freigabe sieht nicht bei jedem Kurs gleich aus. Ausschlaggebend ist der Verwendungszweck im [Abschnitt Verwendung](#section_usage). Ein eigenständiger Kurs regelt Zugang, Buchung und Austritt selbst und zeigt darum alle Abschnitte. Bei einem Kurs im Course Planner übernimmt der Course Planner diese Aufgaben, und die entsprechenden Einstellungen entfallen im Kurs. Ein Template hat keine Teilnehmenden, deshalb entfällt dort alles, was den Zugang von Teilnehmenden betrifft.

| Abschnitt oder Einstellung | Eigenständig | Verwendung im Course Planner | Template |
|---|---|---|---|
| Verwendung | ja | ja | ja |
| Freigabe: Zugang für Teilnehmer:innen | ja | nein | nein |
| Freigabe: Direktlink | ja | nein | ja |
| Freigabe: Teilnehmer:innen können austreten | ja | nein | nein |
| Freigabe: Administrative Freigabe | ja | ja | ja |
| Freigabe: Autor:innen können | ja | nein | ja, ohne "in Gruppen einbinden" |
| Freigabe: Externe OER-Kataloge und Suchmaschinen | ja | nein | nein |
| Angebot | ja | nein | nein |
| LTI 1.3 Zugangskonfiguration | ja | nein | nein |
| Freigabeübersicht | ja | ja | ja |

Bei einem Kurs im Course Planner bleibt im Abschnitt Freigabe deshalb nur die Administrative Freigabe stehen. Mitgliedschaft, Buchung und Austritt regeln Sie dort in der Durchführung des Course Planner. Auch die Freigabeübersicht fällt kürzer aus: Sie zählt nur die Besitzer:innen, weil der Kurs selbst keine Betreuer:innen und Teilnehmer:innen verwaltet.

![Bei Verwendung im Course Planner bleibt im Abschnitt Freigabe nur die Administrative Freigabe, und die Freigabeübersicht zählt bei den Mitgliedern allein die Besitzer:innen](assets/course_settings_share_cpl_v3_de.png){ class="shadow lightbox" title="Tab Freigabe eines Kurses im Course Planner · 2026.10.09" }

!!! info "Wichtig"

    Der Abschnitt Externe OER-Kataloge und Suchmaschinen erscheint zusätzlich nur, wenn das Modul OAI-PMH aktiviert ist, und die Administrative Freigabe nur, wenn das Modul Organisationen aktiviert ist. Den Verwendungszweck "Verwendung im Course Planner" gibt es nur, wenn das Modul Course Planner aktiviert ist.

Die Beschreibungen der folgenden Abschnitte gehen vom Verwendungszweck "Eigenständig" aus.

[Zum Seitenanfang ^](#tab_share)

---

## Abschnitt Verwendung [:octicons-tag-16:{ title="ab Release 18.2.0 (OO-7277)" }](https://track.frentix.com/issue/OO-7277) {: #section_usage}

Wird kein Course Planner verwendet, sind die Kurse eigenständig.

![Verwendungszweck Eigenständig mit dem Link Ändern](assets/course_settings_share_usage1_v1_de.png){ class="shadow lightbox" title="Abschnitt Verwendung im Tab Freigabe" }

**Eigenständig**<br>
Eigenständige Lernressourcen besitzen eine eigene Mitgliederverwaltung. Zum Hinzufügen neuer Mitglieder öffnen Sie also `Kurs > Administration > Mitgliederverwaltung`.<br>
Der Zugang kann mit der Buchungsmethode "Privat" durch Eintragung als Mitglied (z.B. durch Kursbesitzer:innen), durch Vergabe eines Zugangscodes oder über eine Veröffentlichung im Katalog erfolgen.

**Verwendung im Course Planner**<br>
Wird der Kurs in ein Produkt des Course Planner eingebunden, werden die Mitgliedschaften durch den Course Planner vergeben und verwaltet. Der Kurs benötigt dann keine zweite, eigenständige Mitgliederverwaltung.

**Template**<br>
Auch diese Kurse sind durch den Course Planner verwaltet und ohne eigenständige Mitgliederverwaltung. Der Unterschied zur Option "Verwendung im Course Planner" besteht darin, dass ein Template zur Instanzierung verwendet wird. Der Kurs in einer Durchführung wird erst zu einem bestimmten Zeitpunkt aus diesem Template erstellt (instanziert).

Durch Klick auf "Ändern" öffnet sich der Dialog "Verwendungszweck ändern". Er zeigt oben den aktuellen Verwendungszweck und darunter die Verwendungszwecke, zu denen Sie wechseln können. Der aktuelle Verwendungszweck steht deshalb nicht in der Auswahl.

Ausser bei "Eigenständig" erfolgt die Mitgliederverwaltung nicht im Kurs. Deshalb sperrt OpenOlat einen Wechsel, sobald der Kurs eine Voraussetzung nicht erfüllt. Ein gesperrter Verwendungszweck steht im Dialog, ist aber nicht anwählbar. Die Gründe nennt der Dialog über der Auswahl unter dem Satz "Aufgrund der folgenden Voraussetzungen sind bestimmte Optionen nicht verfügbar:":

- **Keine Mitglieder mit Ausnahme der Besitzer:innen:** Der Kurs hat Betreuer:innen oder Teilnehmer:innen. Sperrt den Wechsel zu "Verwendung im Course Planner" und zu "Template".
- **Keine Gruppen, die auch in anderen Kursen eingebunden sind:** Eine Gruppe des Kurses ist zugleich in einem anderen Kurs eingebunden. Sperrt den Wechsel zu "Verwendung im Course Planner" und zu "Template".
- **"Zugang für Teilnehmer:innen" muss auf "Privat" gesetzt sein:** Im Abschnitt Freigabe ist "Buchbare und offene Angebote" gewählt. Sperrt den Wechsel zu "Verwendung im Course Planner" und zu "Template".
- **Keine Verwendung durch Course Planner:** Der Kurs oder das Template ist einer Durchführung zugeordnet. Sperrt jeden Wechsel ausser dem von "Eigenständig" zu "Verwendung im Course Planner".

![Über der Auswahl nennt der Dialog, warum ein Wechsel gesperrt ist, hier wegen Betreuer:innen und Teilnehmer:innen im Kurs; beide Verwendungszwecke sind deshalb nicht anwählbar](assets/course_settings_share_usage2_v3_de.png){ class="shadow lightbox" title="Dialog Verwendungszweck ändern bei einem Kurs mit Mitgliedern · 2026.10.09" }

Hat ein Kurs bereits Mitglieder, ist eine Kopie der einfachste Weg in den Course Planner: Sie entsteht ohne Betreuer:innen und Teilnehmer:innen und lässt sich umstellen. Die Schritte finden Sie hier:<br>
[Wenn sich der Verwendungszweck nicht ändern lässt >](../../manual_how-to/course_planner_courses/course_planner_courses.de.md#embedding_locked)

!!! tip "Tipp"

    Achten Sie beim Erstellen neuer Kurse darauf, welcher Verwendungszweck voreingestellt ist. Administrator:innen stellen den Verwendungszweck für neue Kurse in der System-Administration ein, im Feld "Verwendungszweck für neue Kurse" unter:<br>
    `Administration > Module > Course Planner > Tab "Einstellungen"`

[Zum Seitenanfang ^](#tab_share)

---


## Abschnitt Freigabe {: #section_share}

![Alle Einstellungen eines eigenständigen Kurses auf einen Blick: Zugang Privat, Direktlink, Austritt mit der Option Nie, Administrative Freigabe und die Rechte für Autor:innen](assets/course_settings_share_share_v4_de.png){ class="shadow lightbox" title="Abschnitt Freigabe im Tab Freigabe · 2026.10.09" }

#### Zugang für Teilnehmer:innen {: #section_share_access}

Bei der Wahl **"Privat"** werden die Teilnehmenden durch die Kursbesitzer:in bzw. Personen, die über das Recht der Mitgliederverwaltung verfügen, hinzugefügt. Dies geschieht unter `Kurs > Administration > Mitgliederverwaltung`. Es ist also wie eine persönliche Einladung in den Kurs durch Kursbesitzer:innen.<br>
Bei der Wahl der Option **"Buchbare und offene Angebote"** können die Lernenden einen Kurs selbst buchen, müssen aber eventuell (je nach Einstellung) ein Passwort eingeben. Soll die Buchung nach Wahl eines Angebots im Katalog erfolgen, muss ebenfalls diese Option angewählt sein. 

#### Direktlink {: #section_share_direct_link}

Wenn Sie diesen Link weitergeben, kann damit dieser Kurs direkt aufgerufen werden. Ist die Person noch nicht in OpenOlat bekannt (registriert) und eingeloggt, erscheint zunächst der Login-Bildschirm.

#### Teilnehmer:innen können austreten [:octicons-tag-16:{ title="ab Release 20.3.0 (OO-9272)" }](https://track.frentix.com/issue/OO-9272) {: #section_share_leave}

**Jederzeit**: Möchten Teilnehmende ihre Mitgliedschaft im Kurs selbst beenden, können sie das jederzeit tun.<br>
**Nach Kursenddatum oder Status "Beendet"**: Ein Beenden der Kursmitgliedschaft aus Eigeninitiative der Teilnehmenden ist erst möglich, sobald der Durchführungszeitraum abgelaufen ist oder der Kurs den Status "Beendet" hat. Wurde diese Option gewählt, ohne zuvor in der Beschreibung einen Durchführungszeitraum zu wählen, ist ein Austritt erst möglich, sobald der Kurs den Status "Beendet" erhält.<br>
**Nie**: Der Besuch des Kurses ist Pflicht und Teilnehmer:innen können deshalb nicht selbst austreten.

!!! info "Wichtig"

    Diese Einstellung gibt es nur bei Kursen mit dem Verwendungszweck **"Eigenständig"**. Verwaltet stattdessen der Course Planner den Kurs (Verwendungszweck **"Verwendung im Course Planner"**), erscheint sie im Tab Freigabe nicht, und den Teilnehmenden steht die Funktion "Kurs verlassen" nicht zur Verfügung. Haben Teilnehmende eine Durchführung gebucht, stornieren sie die Buchung selbst: Sie öffnen im Katalog die Infoseite der Durchführung und wählen dort die Aktion "Buchung stornieren". Fällt eine Stornogebühr an, heisst die Aktion "Buchung kostenpflichtig stornieren", und der Bestätigungsdialog nennt den Betrag. Die Aktion erscheint nur bei einer Durchführung mit Anfangsdatum, bis zum Tag vor dem Beginn, und nur, wenn das Angebot stornierbar ist (siehe [Stornierungsbedingungen](../basic_concepts/Offer_Concepts.de.md#offer_invoice_cancellation)). Danach hilft die Verwaltung Ihrer Organisation weiter. [:octicons-tag-16:{ title="ab Release 20.0 (OO-8397)" }](https://track.frentix.com/issue/OO-8397)

#### Administrative Freigabe {: #section_share_admin_access}

Aus den hier ausgewählten Organisationen können Personen mit bestimmten übergeordneten Rollen (z.B. Administrator:innen, Lernressourcenverwalter:innen) ebenfalls auf diesen Kurs zugreifen. Weil es diese Rollen pro Organisation gibt (z.B. Admin für Abteilung xy), können Sie hier bestimmen, welche Organisationen administrativen Zugriff auf Ihren Kurs erhalten. Das Feld erscheint nur, wenn das Modul Organisationen aktiviert ist.<br>
Wie viele Personen administrativ zugreifen können, sehen Sie in der [Freigabeübersicht >](#section_share_overview)

#### Autor:innen können {: #section_share_authors}

Erlauben Sie hier, was andere Autor:innen mit Ihrem Kurs tun dürfen: "in Gruppen einbinden", "kopieren" und "Inhalt exportieren". Bei anderen Lernressourcen als Kursen heisst die erste Option "einbinden".

#### Externe OER-Kataloge und Suchmaschinen {: #section_share_oer}

Mit OAI-PMH lassen sich Metadaten von Lernressourcen für Internet-Portale oder Kataloge ausserhalb OpenOlat freigeben, damit Suchmaschinen einen Inhalt besser finden können. (OER = Open Educational Resources)

Die Funktion muss zunächst generell durch einen/eine Administrator:in aktiviert werden.<br>
Damit die Informationen eines ganz bestimmten Kurses an die Suchmaschinen weiter gegeben werden, muss anschliessend der/die jeweilige Autor:in (Kursbesitzer:in) dies für den eigenen Kurs erlauben.

Mehr über OER finden Sie hier:<br>
How-To: [Kurse zur Indexierung freigeben >](../../manual_how-to/oai_pmh/oai_pmh.de.md#wie-sehe-ich-im-autorenbereich-welche-kurselernressourcen-zur-indexierung-freigegeben-sind)<br>
Admin-Handbuch: [Modul OAI PMH >](../../manual_admin/administration/Modules_OAI.de.md)

[Zum Seitenanfang ^](#tab_share)

---

## Abschnitt Angebot [:octicons-tag-16:{ title="ab Release 17.0.0 (OO-6141)" }](https://track.frentix.com/issue/OO-6141) {: #section_offer}

![Solange der Zugang für Teilnehmer:innen auf Privat steht, ist der Button Angebot hinzufügen inaktiv, und der Abschnitt nennt den Grund](assets/course_settings_share_offer_v2_de.png){ class="shadow lightbox" title="Abschnitt Angebot im Tab Freigabe · 2026.10.09" }

Damit ein Kurs im Katalog aufgeführt wird, muss ein Angebot erstellt werden. Es können auch mehrere Angebote erstellt werden, wenn der gleiche Kurs zu verschiedenen Bedingungen angeboten werden soll (z.B. kostenlos für eine bestimmte Zielgruppe, kostenpflichtig für andere).

Damit ein Angebot für den Katalog erstellt werden kann, muss im Abschnitt "Freigabe" bei "Zugang für Teilnehmer:innen" die Option "Buchbare und offene Angebote" gewählt sein. 


Mehr über Angebote und den Katalog finden Sie hier:<br>
[Katalog >](../area_modules/catalog2.0.de.md)<br>
[Angebotsarten >](../learningresources/Offer_Types.de.md)<br>
[Angebote erstellen >](../area_modules/catalog2.0_angebote.de.md)<br>
[Anbieten von Durchführungen im Katalog >](../area_modules/Course_Planner_Implementations.de.md#tab_catalog)<br>

[Zum Seitenanfang ^](#tab_share)

---

## Abschnitt LTI 1.3 Zugangskonfiguration [:octicons-tag-16:{ title="ab Release 18.2.3 (OO-7664)" }](https://track.frentix.com/issue/OO-7664) {: #section_LTI}

OpenOlat-Kurse können via LTI 1.3 auch von einem anderen LMS aus aufgerufen werden. Für diesen Zugriff von aussen braucht es aber Sicherheitsvorkehrungen und genau festgelegte Berechtigungen.<br>
In diesem Abschnitt können Sie dazu ein sogenanntes Deployment einrichten, um den Kurs für ein anderes LMS aufrufbar zu machen.

Mehr über die Freigabe eines Kurses via LTI finden Sie hier:<br>
[LTI Zugang zu einem Kurs konfigurieren >](../learningresources/LTI_Share_courses.de.md)<br>

[Zum Seitenanfang ^](#tab_share)

---


## Freigabeübersicht {: #section_share_overview}

![Mitgliederzahlen nach Rolle, zugeordnete Gruppen und Produkte sowie administrativ Zugriffsberechtigte mit ihren Rechten](assets/course_settings_share_overview_v2_de.png){ class="shadow lightbox" title="Freigabeübersicht im Tab Freigabe" }

Im Block **Mitglieder** finden Sie die Anzahl der Kursmitglieder, aufgegliedert nach Besitzer:innen, Betreuer:innen und Teilnehmer:innen. Mit "Mitgliederverwaltung öffnen" wechseln Sie direkt in die Mitgliederverwaltung des Kurses.

Im Block **Administrative Freigabe** steht je Rolle, wie viele Personen aufgrund dieser Rolle ebenfalls auf diesen Kurs zugreifen können und mit welchem Recht, etwa "Vollzugriff" für Lernressourcenverwalter:innen und Administrator:innen.

Wurde der Kurs Gruppen zugeordnet, finden Sie die betreffenden Gruppen im Block **Gruppen** angezeigt.

Wurde der Kurs im Course Planner einem Produkt zugeordnet, finden Sie die Verwendungen im Block **Produkt** angezeigt.

[Zum Seitenanfang ^](#tab_share)

---

## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Wie kann ich mit dem Course Planner Kursdurchführungen planen und durchführen? >](../../manual_how-to/course_planner_courses/course_planner_courses.de.md)<br>
[Angebotskonzepte: Stornierungsbedingungen bei Rechnungsangeboten >](../basic_concepts/Offer_Concepts.de.md)<br>
[Wie kann ich meine Kurse durch Suchmaschinen finden lassen? >](../../manual_how-to/oai_pmh/oai_pmh.de.md)<br>
[Modul OAI PMH >](../../manual_admin/administration/Modules_OAI.de.md)<br>
[Katalog 2.0: Übersicht >](../area_modules/catalog2.0.de.md)<br>
[Angebotsarten >](../learningresources/Offer_Types.de.md)<br>
[Katalog 2.0 - Angebote >](../area_modules/catalog2.0_angebote.de.md)<br>
[Course Planner: Durchführungen >](../area_modules/Course_Planner_Implementations.de.md)<br>
[Kurseinstellungen - Tab Freigabe: LTI Zugang zu einem Kurs konfigurieren >](../learningresources/LTI_Share_courses.de.md)

**Weiterführend**<br>
[Zugangskonfiguration / Freigabe >](../learningresources/Access_configuration.de.md)<br>
[Kurseinstellungen >](../learningresources/Course_Settings.de.md)<br>
[Kopieren (eines Kurses) >](../learningresources/Course_Copy.de.md)

[Zum Seitenanfang ^](#tab_share)
