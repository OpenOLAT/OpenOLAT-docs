# Reports: Zertifikate {: #certificate_reports}

Diese Seite beschreibt den Aufbau der Excel-Dateien, die mit den [Reportvorlagen der Kategorie Zertifikate](../area_modules/Coaching_Reports.de.md) erzeugt werden. Jede Datei enthält das Worksheet "Einzelkurse" und, falls das Modul Course Planner aktiv ist, zusätzlich das Worksheet "Produkte".

## Worksheet "Einzelkurse" [:octicons-tag-16:{ title="ab Release 20.0 (OO-8371)" }](https://track.frentix.com/issue/OO-8371) {: #individual_courses}

| Spalte           | Quelle     | Beschreibung                               |
|------------------|------------|--------------------------------------------|
| Zertifikats-ID   | Zertifikat | Eindeutige Nummer des Zertifikats          |
| Kurs             | Kurs       | Titel des Kurses                           |
| Kennzeichen      | Kurs       | Kennzeichen des Kurses                     |
| Benutzerdaten    | Person     | Konfigurierbar unter `Administration > Customizing > Benutzer:innen-Attribute`, Kontext "Certificates report"; standardmässig Nachname, Vorname und E-mail-Adresse |
| Start des Kurses | Kurs       | Datum des ersten Besuchs im Kurs           |
| Erfolgsstatus    | Kurs       | "Bestanden", "Nicht bestanden" oder "Undefiniert" |
| Ausgestellt am   | Zertifikat | Ausstellungsdatum des Zertifikats          |
| Gültig bis       | Zertifikat | Ablaufdatum des Zertifikats; leer, wenn keine Gültigkeitsdauer konfiguriert ist |

## Worksheet "Produkte" [:octicons-tag-16:{ title="ab Release 20.0 (OO-8371)" }](https://track.frentix.com/issue/OO-8371) {: #products}

Das Worksheet "Produkte" listet die Zertifikate der Kurse, die einem Bildungsprodukt (Curriculum-Element) zugeordnet sind. Es enthält zusätzlich zu allen Spalten des Worksheets "Einzelkurse" folgende Spalten am Zeilenanfang:

| Spalte      | Quelle         | Beschreibung                  |
|-------------|----------------|-------------------------------|
| Element     | Course Planner | Titel des Curriculum-Elements |
| Kennzeichen | Course Planner | Kennzeichen des Elements      |
| Elementtyp  | Course Planner | Titel des Elementtyps         |

Ist ein Kurs mehreren Curriculum-Elementen zugeordnet, werden die Werte in der Zelle mit einem senkrechten Strich getrennt aufgeführt.

[Zum Seitenanfang ^](#certificate_reports)
