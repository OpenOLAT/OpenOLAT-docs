# Bezahlungsmodule: Rechnung [:octicons-tag-16:{ title="ab Release 20.0 (OO-8210)" }](https://track.frentix.com/issue/OO-8210){:target="_blank"} {: #invoice}

Sind in OpenOlat Buchungsaufträge vorhanden, können dort Excel-Dateien exportiert werden.
Die Strategie ist hier, dass über diese Excel-Dateien die relevanten Daten an andere, auf Rechnungsstellung spezialisierte Programme, übergeben werden und dort weiter verarbeitet werden können.

OpenOlat selbst erstellt keine Rechnungen. Entsprechend lassen sich auch Mahnungen in OpenOlat weder erstellen noch verwalten.

---


## Buchungsauftrag mit Rechnung [:octicons-tag-16:{ title="ab Release 20.0 (OO-8211)" }](https://track.frentix.com/issue/OO-8211){:target="_blank"} {: #booking_order_with_invoice}

Buchungsaufträge mit Rechnung entstehen nur über Angebote einer Durchführung im Course Planner.

Dazu werden im Course Planner Angebote hinterlegt. Diese (Kurs-)Angebote werden z.B. in einem externen Katalog angezeigt, sowohl die Preise als auch die Anzahl der verfügbaren Plätze. 

Benutzer:innen können diese Kurse buchen, indem sie sich aus dem Katalog heraus anmelden (wenn sie schon Benutzer:in von OpenOlat sind) oder registrieren. 

Wenn aus dem Course Planner heraus ein Angebot im Katalog gemacht wurde, das mit Rechnung gebucht werden kann, werden die Interessent:innen beim Anmeldevorgang zur Angabe der Rechnungsadresse usw. geführt. Es wird dabei auch eine Buchungsnummer erstellt.

Der Buchungsauftrag kann anschliessend bestätigt werden. 

Wenn der geplante Kurs tatsächlich stattfindet, wird evtl. erst dann ein dazugehöriger OpenOlat Kurs erstellt.

Im Course Planner unter:<br>
`Course Planner > Durchführungen > "Ihre Durchführung" > Tab Katalog`<br>
sind im Teilbereich "Buchungsaufträge" die Buchungsaufträge gesammelt und können als Excel-Datei exportiert werden.

Ist die [Debitorennummer](Modules_Organisations.de.md#customer_number) im Modul Organisationen eingeschaltet, enthält die Excel-Datei auch die Debitorennummer der Person, die der Rechnungsadresse und die der Organisation, zu der die Rechnungsadresse gehört. So ordnet Ihre Buchhaltung jede Buchung direkt dem richtigen Konto zu. Alle Spalten der Datei beschreibt die Seite [Reports: Buchungsaufträge](../../manual_user/area_modules/Reports_BookingOrders.de.md). [:octicons-tag-16:{ title="ab Release 21.1 (OO-9736)" }](https://track.frentix.com/issue/OO-9736){:target="_blank"}

[Zum Seitenanfang ^](#invoice)

---


## Weiterführende Informationen {: #further_information}

[Modul Organisationen >](Modules_Organisations.de.md)<br>
[Reports: Buchungsaufträge >](../../manual_user/area_modules/Reports_BookingOrders.de.md)<br>
[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Durchführungen >](../../manual_user/area_modules/Course_Planner_Implementations.de.md)

[Zum Seitenanfang ^](#invoice)