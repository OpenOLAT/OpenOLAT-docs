# Reports: Buchungsaufträge {: #booking_orders_report}

Der Report Buchungsaufträge führt je Buchungsauftrag die folgenden Spalten. Die drei Spalten zur Debitorennummer enthält er nur, wenn die [Debitorennummer](../../manual_admin/administration/Modules_Organisations.de.md#customer_number) im Modul Organisationen eingeschaltet ist. [:octicons-tag-16:{ title="ab Release 21.1 (OO-9736)" }](https://track.frentix.com/issue/OO-9736)

| Attribut                    | Quelle                 | Beschreibung                                                             | Linien-/Ausbildungsverantwortlicher                                      |
|-----------------------------|------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Benutzerdaten               | Person                 | Gemäss Konfiguration in der Administration                               |                                                                          |
| Debitorennummer             | Person                 | Debitorennummer der Person                                               |                                                                          |
| Mitgliedschaftsstatus       | Person                 | Status in Durchführung oder Kurs (eigenständig)                          |                                                                          |
| Produkt	                  | Produkt                | Titel des Produkts                                                       |                                                                          |
| Kennzeichen                 | Produkt                | Kennzeichen des Produkts                                                 |                                                                          |
| Org ID (Produkt)            | Produkt                | Organisationsidentifikator des Produkts                                   |                                                                          |
| Org name (Produkt)          | Produkt                | Organisationsname des Produkts                                           |                                                                          |
| Durchführung                | Durchführung           | Titel der Durchführung                                                   |                                                                          |
| Kennzeichen                 | Durchführung           | Kennzeichen der Durchführung                                             |                                                                          |
| Durchführungstyp            | Durchführung           | Elementtyp der Durchführung                                              |                                                                          |
| Durchführungsstatus         | Durchführung           | Status der Durchführung                                                  |                                                                          |
| Durchführungsformat	      | Durchführung           | Durchführungsformat der Durchführung                                     |                                                                          |
| Durchführung von            | Durchführung           | Beginn des Durchführungszeitraums der Durchführung                       |                                                                          |
| Durchführung bis            | Durchführung           | Ende des Durchführungszeitraums der Durchführung                         |                                                                          |
| Durchführungsort	          | Durchführung           | Ort der Durchführung                                                     |                                                                          |
| Buchungsnummer	          | Buchungsauftrag        | Nummer des Buchungsauftrags                                              |                                                                          |
| Buchungsstatus	          | Buchungsauftrag        | Status des Buchungsauftrags                                              |                                                                          |
| Angebot	                  | Buchungsauftrag        | Label des gebuchten Angebots                                              |                                                                          |
| Angebotstyp	              | Buchungsauftrag        | Typ des gebuchten Angebots                                               |                                                                          |
| Kostenstelle	              | Buchungsauftrag        | Kostenstelle des gebuchten Angebots                                      | :material-cancel: Nicht verfügbar                                        |
| Konto	                      | Buchungsauftrag        | Eingegebenes Konto beim Buchungsprozess                                  | :material-cancel: Nicht verfügbar                                        |
| PO Nummer	                  | Buchungsauftrag        | Eingegebene PO Nummer beim Buchungsprozess                               | :material-cancel: Nicht verfügbar                                        |
| Kommentar zur Bestellung    | Buchungsauftrag        | Eingegebener Kommentar beim Buchungsprozess                              |                                                                          |
| Auftragsdatum               | Buchungsauftrag        | Datum der Buchung                                                        |                                                                          |
| Preis	                      | Buchungsauftrag        | Preis beim Zeitpunkt der Buchung                                         |                                                                          |
| Stornogebühr	              | Buchungsauftrag        | Stornogebühr beim Zeitpunkt der Buchung                                  |                                                                          |
| Rechnungsadresse            | Organisation           | Name der Rechnungsadresse                                                |                                                                          |
| Debitorennummer Rechnungsadresse | Organisation           | Debitorennummer der Rechnungsadresse                                     |                                                                          |
| Name / Firma                | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Zusatz / Abteilung          | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Adresszeile 1               | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Adresszeile 2               | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Adresszeile 3               | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Adresszeile 4               | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Postfach                    | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Region                      | Organisation           | Rechnungsadresse                                                         |                                                                          |
| PLZ                         | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Ort                         | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Land                        | Organisation           | Rechnungsadresse                                                         |                                                                          |
| Org ID (Rechnungsadresse)   | Organisation           | Organisationsidentifikator der Rechnungsadresse                           |                                                                          |
| Org name (Rechnungsadresse) | Organisation           | Organisationsname der Rechnungsadresse                                   |                                                                          |
| Debitorennummer Organisation | Organisation           | Debitorennummer der Organisation, zu der die Rechnungsadresse gehört     |                                                                          |
| Erster Besuch               | Kurs                   | Datum des allerersten Besuches in einem Kurs                             |                                                                          |
| Letzter Besuch              | Kurs                   | Datum des allerletzten Besuchs in einem Kurs                             |                                                                          |
| Punkte                      | Kursfortschritt/Status | Punktetotal der Durchführung / des Kurses (eigenständig)                 | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Erfolgsstatus               | Kursfortschritt/Status | Kumulierter Status der Durchführung oder des Kurses (eigenständig)      | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Bestanden                   | Kursfortschritt/Status | Anzahl "Bestanden"                                                       | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Nicht bestanden             | Kursfortschritt/Status | Anzahl "Nicht bestanden"                                                 | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Keine Angabe                | Kursfortschritt/Status | Anzahl "Keine Angabe"                                                    | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Fortschritt                 | Kursfortschritt/Status | Kumulierter Fortschritt der Durchführung oder des Kurses (eigenständig) | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Zertifikat                  | Kursfortschritt/Status | Anzahl Zertifikate                                                       | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Gültigkeit des Zertifikats  | Kursfortschritt/Status | Nächstes Ablaufdatum eines Zertifikates                                  | :material-checkbox-marked-outline: "Kursfortschritt und Status anzeigen" |
| Einheiten                   | Absenz                 | Anzahl Einheiten                                                         | :material-checkbox-marked-outline: "Termine und Absenzen anzeigen"       |
| Anwesend                    | Absenz                 | Anzahl "Anwesend"                                                        | :material-checkbox-marked-outline: "Termine und Absenzen anzeigen"       |
| Unentschuldigt              | Absenz                 | Anzahl "Unentschuldigt"                                                  | :material-checkbox-marked-outline: "Termine und Absenzen anzeigen"       |
| Entschuldigt                | Absenz                 | Anzahl "Entschuldigt"                                                    | :material-checkbox-marked-outline: "Termine und Absenzen anzeigen"       |
| Dispensiert                 | Absenz                 | Anzahl "Dispensiert"                                                     | :material-checkbox-marked-outline: "Termine und Absenzen anzeigen"       |


## Weiterführende Informationen {: #further_information}

[Modul Organisationen >](../../manual_admin/administration/Modules_Organisations.de.md)<br>
[Course Planner: Reports >](Course_Planner_Reports.de.md)<br>
[Course Planner: Durchführungen >](Course_Planner_Implementations.de.md)<br>
[Bezahlungsmodule: Rechnung >](../../manual_admin/administration/Payment_Invoice.de.md)

[Zum Seitenanfang ^](#booking_orders_report)
