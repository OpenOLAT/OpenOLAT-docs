# Produkt anlegen und strukturieren {: #product}

!!! warning "Konzeptstudie: mögliche neue Darstellung"
    Diese Seite ist Teil eines Versuchs, wie der visuelle Einstieg in den Course Planner künftig aussehen könnte. Die Inhalte sind bewusst verkürzt. Verbindlich ist die reguläre Handbuchseite [Course Planner](../../Course_Planner/).

Die Bildungsverantwortliche legt ein Produkt an und baut die Struktur auf: Lehrgang, Module, Einzelkurse. Jedes Element durchläuft die Status «Vorbereitung», «Provisorisch», «Bestätigt» und «Aktiv» bis «Beendet» oder «Abgebrochen». Für die Durchführung heisst dieser Ablauf Durchführungs-Lebenszyklus. [:octicons-tag-16:{ title="ab Release 20.0 (OO-8092)" }](https://track.frentix.com/issue/OO-8092)

Der Durchführungs-Lebenszyklus löscht nichts und steht nicht bei den drei Lebenszyklen für Gruppen, Kurse und Konten unter `Administration > Lebenszyklen`. Die Status lassen sich von Hand setzen oder über die [Automatisierung](../Course_Planner_Implementations.de.md#tab_settings_automation): Der Elementtyp gibt die Regeln vor, die einzelne Durchführung kann sie überschreiben. [:octicons-tag-16:{ title="ab Release 21.0 (OO-9452)" }](https://track.frentix.com/issue/OO-9452)

## Wie setze ich das um?

Im Course Planner den Bereich «Produkte» öffnen und ein Produkt anlegen. Titel und Kennzeichen sind Pflichtfelder; optional Organisation, Absenzenmanagement und Beschreibung ergänzen.

## Vorbedingungen

Course Planner aktiviert. Für die Organisationsbeschränkung muss das Modul «Organisationen» aktiv sein. Für das Absenzenmanagement muss die System-Administration das Modul aktiviert und freigegeben haben:<br>
`Administration > Module > Termine / Absenzen`

## Wo finde ich die Einstellung

`Course Planner > Produkte > Produkt erstellen`

## Zusammenhänge

Das Produkt ist die zentrale Kopiervorlage, auf der die Durchführungen basieren. Strukturierte Produkte bilden Kurse und Lernressourcen in einer Baumstruktur aus Elementen ab.

## Weiterführende Informationen {: #further_information}

[Course Planner: Übersicht >](../Course_Planner.de.md)<br>
[Course Planner: Anwendungsmap >](../Course_Planner_Map.de.md)<br>
[Course Planner: Durchführungen >](../Course_Planner_Implementations.de.md)<br>
[Course Planner: Produkte >](../Course_Planner_Products.de.md)<br>
[Lebenszyklen: Übersicht >](../../../manual_admin/administration/Life_cycles_-_Administration.de.md)

[Zum Seitenanfang ^](#product)
