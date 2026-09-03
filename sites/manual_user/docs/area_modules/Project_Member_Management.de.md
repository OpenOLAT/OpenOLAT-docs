# Projekte: Mitgliederverwaltung {: #member_management}

Die Projektmitglieder werden in der Regel durch den/die Projektbesitzer:in zu Projektmitgliedern gemacht. (In der Regel liegt die Projektleitung bei der Person, die das neue Projekt anlegt.)

Sie öffnen die Mitgliederverwaltung im Projekt über das 3-Punkte-Menü rechts oben: `Projekte > Tab "Meine Projekte" > Projekt wählen > 3-Punkte-Menü > "Mitgliederverwaltung"`.

![Eintrag Mitgliederverwaltung im 3-Punkte-Menü rechts oben im Cockpit eines Projekts](assets/projekte_mitgliederverwaltung_aufrufen_v1_de.png){ class="shadow lightbox" }

![Mitgliederliste mit Rollen und dem Button Mitglieder hinzufügen auf der Seite Mitgliederverwaltung eines Projekts](assets/projekte_mitgliederverwaltung_v1_de.png){ class="shadow lightbox" }

!!! info "Wichtig"

    Den Tab "Administration" sehen nur OpenOlat-Administrator:innen. Projektbesitzer:innen sehen ihn nicht.

[Zum Seitenanfang ^](#member_management)

---


## Externe Mitglieder {: #external}

Sollen auch Personen im Projekt mitarbeiten, die nicht in OpenOlat als Benutzer:innen registriert sind, können sie als externe Mitglieder eingeladen werden. Sie können OpenOlat dann für maximal 180 Tage nutzen.

Sobald ein Projektmitglied erfasst ist, erhält es einen Link. Nach Aufruf des Links führt ein Wizard das neue Projektmitglied durch Anmeldung und Registration.

![Option Externe Mitglieder einladen im Pulldown des Buttons Mitglieder hinzufügen auf der Seite Mitgliederverwaltung](assets/projekte_mitgliederverwaltung_externe_einladen_v1_de.png){ class="shadow lightbox" }

!!! info "Wichtig"

    "Externes Mitglied" ist keine OpenOlat-Rolle. Ein externes Mitglied kann alle Rollen erhalten, ausser Besitzer:in (Rolle, mit der das ganze Projekt gelöscht werden kann).

[Zum Seitenanfang ^](#member_management)

---


## Rollen {: #roles}

|    | Projekt| Objekte im Projekt | Mitglieder verwalten | externe Mitglieder verwalten |
| ------------------------------------------------------------- | :--------------: | :--------------: | :--------------: | :--------------: |
|                                                                                       |
|**Besitzer:in (Projektbesitzer:in)** | anlegen, bearbeiten, abschliessen, löschen | anlegen, bearbeiten, löschen | anlegen, bearbeiten, löschen, kann Leitungsrolle vergeben | anlegen, bearbeiten, löschen |
|**Leiter:in (Projektleiter:in)**| bearbeiten | anlegen, bearbeiten, abschliessen, löschen | anlegen, bearbeiten, löschen | :material-cancel: |
|**Projektbüro** | bearbeiten | anlegen, bearbeiten, löschen | anlegen, bearbeiten, löschen | :material-cancel: |
|**Teilnehmer:in (Projektmitarbeiter:in)**              | nur lesen | anlegen, bearbeiten, löschen            | :material-cancel: |     :material-cancel:    |
|**Business-Analyst:in / Lieferant:in**         | nur lesen           | anlegen, bearbeiten, löschen | :material-cancel:| :material-cancel: |
|**Sponsor:in / Auftraggeber:in**          | nur lesen           | :material-cancel: | :material-cancel: | :material-cancel: |
|**Lenkungsausschuss**         | nur lesen          | :material-cancel: | :material-cancel:| :material-cancel: |
| Rollen, die über mehrere Projekte hinweg agieren können:                                                                                                   |
|**Projektverwalter:in**                                        | anlegen, bearbeiten, abschliessen, löschen, Tab "Administration" im Bereich Projekte      | sieht keine Inhalte | anlegen, bearbeiten, löschen, kann Leitungsrolle vergeben | anlegen, bearbeiten, löschen  |
|**Administrator:in**                                         | Tab "Administration" im Bereich Projekte      | hat nur Einblick in ein Projekt, wenn auch Mitglied*       | kann Leitungsrolle vergeben | anlegen, bearbeiten, löschen  |


*Administrator:innen können sich zwar selbst zum Mitglied machen, aber das ist dann protokolliert. Auf diese Art soll missbräuchlicher Zugriff eingedämmt werden.

[Zum Seitenanfang ^](#member_management)

