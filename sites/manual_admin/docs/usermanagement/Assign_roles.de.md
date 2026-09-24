# Rollen zuweisen {: #assign_roles}

Sobald eine Person erfasst und ihr Konto angelegt wurde, lässt sich dieses weiter konfigurieren. Eine wichtige Einstellung ist die Zuordnung der gewünschten Rolle(n).

Suchen Sie in der Benutzerverwaltung die gewünschte Person und öffnen Sie ihr Konto:<br>
`Benutzerverwaltung > "Name der Person" > Rollen`<br>
So gelangen Sie zur Seite "Kontoeinstellungen verwalten". Hier stehen verschiedene Reiter zur Verfügung. Wählen Sie "[Rollen](../../manual_user/basic_concepts/Roles_Rights.de.md)" und ordnen Sie die gewünschte Rolle zu.

Welche Rechte eine Rolle mit sich bringt, beschreibt das Benutzerhandbuch: [Welche Rollen gibt es?](../../manual_user/basic_concepts/Roles.de.md) für die Organisationsrollen und [Rechte in Kursen](../../manual_user/basic_concepts/Authorisation_Concept.de.md) für die Rollen in einem Kurs.

Welche Rollen Sie vergeben können, hängt von Ihrer eigenen Rolle ab. Benutzerverwalter:innen vergeben die Rollen Benutzer:in und Autor:in. Rollenverwalter:innen vergeben die administrativen Rollen der Organisation sowie Gruppenverwalter:in und Poolverwalter:in. Die Rollen Principal, Administrator:in und Systemadministrator:in vergeben nur Administrator:innen.



## Rollen in einer Organisation

Arbeitet Ihre Instanz mit mehreren Organisationen, geben Sie einer Person in jeder Organisation eigene Rollen, zum Beispiel Autor:in in der einen und nur Benutzer:in in der anderen. Voraussetzung ist, dass das Modul "Organisationen" eingeschaltet ist.

### Zugehörigkeit und zusätzliche Rollen [:octicons-tag-16:{ title="ab Release 20.0.3 (OO-8610)" }](https://track.frentix.com/issue/OO-8610) {: #affiliation_additional_roles}

Mit eingeschaltetem Modul "Organisationen" gliedert sich der Reiter "Rollen" in zwei Abschnitte. So sehen Sie getrennt, wo die Person dazugehört und welche Aufgaben sie zusätzlich übernimmt.

Im Abschnitt "Zugehörigkeit" wählen Sie im Feld "Benutzer:in in", in welchen Organisationen die Person die Rolle Benutzer:in hat. Mindestens eine Organisation ist Pflicht.

Im Abschnitt "Zusätzliche Rollen" steht für jede Organisation der Person eine eigene Auswahlliste "Rollen in "Organisation"". Hat die Person dort keine weitere Rolle, zeigt die Liste "Keine zusätzliche Rolle ausgewählt". Eine weitere Organisation nehmen Sie mit dem Button "Organisation hinzufügen" auf. Der Button erscheint, solange es Organisationen gibt, die Sie verwalten und die dem Konto noch fehlen.

Ist das Modul "Organisationen" ausgeschaltet, zeigt der Reiter nur den Abschnitt "Zusätzliche Rollen" mit einer einzigen Auswahlliste "Rollen".

![Abschnitte Zugehörigkeit mit dem Feld Benutzer:in in und Zusätzliche Rollen mit dem Button Organisation hinzufügen, beide markiert, Reiter Rollen eines Kontos](assets/assign_roles_orgunit_v2_de.png){ class="shadow lightbox"}

!!! note "Hinweis"

    Weitere Einstellungen zu den Rollen nehmen Sie in den Reitern "Beziehungen", "Gruppen" und "Lernressourcen" vor.


## Rollenverlauf [:octicons-tag-16:{ title="ab Release 20.0.4 (OO-6304)" }](https://track.frentix.com/issue/OO-6304) {: #role_history}

Wollen Sie nachvollziehen, wer einer Person wann eine Rolle gegeben oder entzogen hat, finden Sie das unter den Rollen im Abschnitt "Rollenverlauf". Jede Änderung steht dort als eigene Zeile.

Die Tabelle zeigt die Spalten "Datum", "Rolle", "Vererbung", "Aktivität", "Originalwert", "Neuer Wert", "Administrative Kommentar" und "Benutzer" mit der Person, welche die Änderung vorgenommen hat. Mit eingeschaltetem Modul "Organisationen" kommt die Spalte "Organisation" dazu.

Über die Tabs "Alle", "7 Tage", "4 Wochen" und "12 Monate" grenzen Sie den Zeitraum ein. Zusätzlich filtern Sie nach "Rolle", "Organisationen" und "Datum" oder zeigen mit "Nicht vererbt" nur die direkt vergebenen Rollen. Die Tabelle lässt sich als Excel-Datei herunterladen.

[Zum Seitenanfang ^](#assign_roles)


## Weiterführende Informationen {: #further_information}

**Auf dieser Seite erwähnt**<br>
[Rollen und Rechte: Übersicht >](../../manual_user/basic_concepts/Roles_Rights.de.md)<br>
[Rollen und Rechte: Welche Rollen gibt es? >](../../manual_user/basic_concepts/Roles.de.md)<br>
[Rollen und Rechte: Rechte in Kursen >](../../manual_user/basic_concepts/Authorisation_Concept.de.md)

**Weiterführend**<br>
[Konto konfigurieren >](Configure_User.de.md)<br>
[Kontosuche >](Search_Users.de.md)<br>
[Modul Organisationen >](../administration/Modules_Organisations.de.md)<br>
[Rollen und Rechte: Rollen zuweisen >](../../manual_user/basic_concepts/Assign_Roles.de.md)

[Zum Seitenanfang ^](#assign_roles)
