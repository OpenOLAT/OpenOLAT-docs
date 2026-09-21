# Bezahlungsmodule: Rechnung {: #invoice}

Verfügbar ab :octicons-tag-24: Release 20

Sind in OpenOlat Buchungsaufträge vorhanden, können dort Excel-Dateien exportiert werden.
Die Strategie ist hier, dass über diese Excel-Reports die relevanten Daten an andere, auf Rechnungsstellung spezialisierte Programme, übergeben werden und dort weiter verarbeitet werden können.

OpenOlat selbst kann aktuell keine Rechnungen generieren. Entsprechend können auch keine Mahnungen usw. in OpenOlat direkt erstellt und verwaltet werden.

---


## Buchungsauftrag mit Rechnung {: #booking_order_with_invoice}

Buchungsaufträge mit Rechnung können momentan (Stand Release 20.1) nur mit dem Course Planner erstellt werden.

Dazu werden im Course Planner Angebote hinterlegt. Diese (Kurs-)Angebote werden z.B. in einem externen Katalog angezeigt, sowohl die Preise als auch die Anzahl der verfügbaren Plätze. 

Benutzer:innen können diese Kurse buchen, indem sie sich aus dem Katalog heraus anmelden (wenn sie schon Benutzer:in von OpenOlat sind) oder registrieren. 

Wenn aus dem Course Planner heraus ein Angebot im Katalog gemacht wurde, das mit Rechnung gebucht werden kann, werden die Interessent:innen beim Anmeldevorgang zur Angabe der Rechnungsadresse usw. geführt. Es wird dabei auch eine Buchungsnummer erstellt.

Der Buchungsauftrag kann anschliessend bestätigt werden. 

Wenn der geplante Kurs tatsächlich stattfindet, wird evtl. erst dann ein dazugehöriger OpenOlat Kurs erstellt.

Im Course Planner unter:<br>
`Course Planner > Durchführungen > "Ihre Durchführung" > Tab Katalog`<br>
sind im Teilbereich "Buchungsaufträge" die Buchungsaufträge gesammelt und können als Excel-Datei exportiert werden.

[Zum Seitenanfang ^](#invoice)

---


## Weiterführende Informationen {: #further_information}

[Course Planner: Übersicht >](../../manual_user/area_modules/Course_Planner.de.md)<br>
[Course Planner: Durchführungen >](../../manual_user/area_modules/Course_Planner_Implementations.de.md)

[Zum Seitenanfang ^](#invoice)